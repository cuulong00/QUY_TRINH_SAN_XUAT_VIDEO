import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';
import { query, initDatabase, getUsePostgres } from './db.js';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, '.env') });

const app = express();
const PORT = process.env.PORT || 5002;

app.use(cors());
app.use(express.json({ limit: '10mb' }));

// Initialize Gemini SDK safely
const genAI = process.env.GEMINI_API_KEY ? new GoogleGenerativeAI(process.env.GEMINI_API_KEY) : null;

// Helper to call Gemini with fallback chain and retries
const generateContentWithFallback = async (prompt, mimeType = 'application/json') => {
  const models = ['gemini-3.5-flash', 'gemini-2.5-flash', 'gemini-flash-latest'];
  let lastError = null;
  for (const modelName of models) {
    for (let attempt = 1; attempt <= 2; attempt++) {
      try {
        console.log(`🤖 Attempting to call Gemini model: ${modelName} (attempt ${attempt}/2)...`);
        const model = genAI.getGenerativeModel({
          model: modelName,
          generationConfig: mimeType ? { responseMimeType: mimeType } : undefined
        });
        const result = await model.generateContent(prompt);
        if (result && result.response) {
          return result;
        }
      } catch (err) {
        console.warn(`⚠️ Model ${modelName} attempt ${attempt} failed:`, err.message || err);
        lastError = err;
        // Wait 1.5s before retry/fallback
        await new Promise(resolve => setTimeout(resolve, 1500));
      }
    }
  }
  throw lastError || new Error('All fallback Gemini models failed.');
};

// Initialize Database (Postgres or SQLite fallback)
initDatabase();

// 1. Get Subjects
app.get('/api/subjects', async (req, res) => {
  try {
    const result = await query('SELECT * FROM subjects ORDER BY id ASC');
    res.json(result.rows);
  } catch (error) {
    console.error('Error getting subjects:', error);
    res.status(500).json({ error: 'Failed to retrieve subjects' });
  }
});

// Helper to award XP and update streak
const awardXP = async (xpAmount) => {
  try {
    const achRes = await query('SELECT * FROM achievements LIMIT 1');
    if (achRes.rows.length === 0) {
      const isPostgres = getUsePostgres();
      if (isPostgres) {
        await query(
          "INSERT INTO achievements (streak_days, total_score, last_active_date, badges_unlocked) VALUES (1, $1, CURRENT_DATE, '{}')",
          [xpAmount]
        );
      } else {
        await query(
          "INSERT INTO achievements (streak_days, total_score, last_active_date, badges_unlocked) VALUES (1, $1, CURRENT_DATE, '[]')",
          [xpAmount]
        );
      }
    } else {
      const ach = achRes.rows[0];
      let streak = ach.streak_days || 0;
      const totalScore = (ach.total_score || 0) + xpAmount;
      const lastActive = ach.last_active_date;
      
      const todayStr = new Date().toISOString().split('T')[0];
      if (lastActive) {
        const lastDate = new Date(lastActive);
        const todayDate = new Date(todayStr);
        const diffDays = Math.round((todayDate - lastDate) / (1000 * 60 * 60 * 24));
        
        if (diffDays === 1) {
          streak += 1;
        } else if (diffDays > 1) {
          streak = 1;
        }
      } else {
        streak = 1;
      }
      
      await query(
        'UPDATE achievements SET streak_days = $1, total_score = $2, last_active_date = CURRENT_DATE WHERE id = $3',
        [streak, totalScore, ach.id]
      );
    }
  } catch (error) {
    console.error('Error awarding XP:', error);
  }
};

// 2. Get Chapters
app.get('/api/chapters', async (req, res) => {
  const { subject_id } = req.query;
  try {
    let result;
    if (subject_id) {
      result = await query(`
        SELECT c.*, COALESCE(q.q_count, 0) as question_count
        FROM chapters c
        LEFT JOIN (
          SELECT chapter_id, COUNT(*) as q_count
          FROM questions
          GROUP BY chapter_id
        ) q ON c.id = q.chapter_id
        WHERE c.subject_id = $1
        ORDER BY c.sort_order ASC
      `, [subject_id]);
    } else {
      result = await query(`
        SELECT c.*, COALESCE(q.q_count, 0) as question_count
        FROM chapters c
        LEFT JOIN (
          SELECT chapter_id, COUNT(*) as q_count
          FROM questions
          GROUP BY chapter_id
        ) q ON c.id = q.chapter_id
        ORDER BY c.subject_id ASC, c.sort_order ASC
      `);
    }
    res.json(result.rows);
  } catch (error) {
    console.error('Error getting chapters:', error);
    res.status(500).json({ error: 'Failed to retrieve chapters' });
  }
});

// 2b. Get Due Chapters for Spaced Repetition Review
app.get('/api/chapters/due', async (req, res) => {
  try {
    const result = await query('SELECT * FROM chapters WHERE next_review_date <= CURRENT_DATE ORDER BY subject_id ASC, sort_order ASC');
    res.json(result.rows);
  } catch (error) {
    console.error('Error getting due chapters:', error);
    res.status(500).json({ error: 'Failed to retrieve due chapters' });
  }
});

// 2c. Get Topic Questions (with Gemini AI generation fallback)
app.get('/api/chapters/:id/questions', async (req, res) => {
  const chapterId = parseInt(req.params.id, 10);
  let textRes = '';
  let cleanedText = '';
  try {
    // Check if questions already exist in database
    const questionsRes = await query('SELECT * FROM questions WHERE chapter_id = $1', [chapterId]);
    if (questionsRes.rows.length >= 5) {
      const easy = questionsRes.rows.filter(q => q.difficulty === 'easy');
      const medium = questionsRes.rows.filter(q => q.difficulty === 'medium');
      const hard = questionsRes.rows.filter(q => q.difficulty === 'hard');
      const others = questionsRes.rows.filter(q => q.difficulty !== 'easy' && q.difficulty !== 'medium' && q.difficulty !== 'hard');
      
      // Shuffle helper
      const shuffle = (arr) => [...arr].sort(() => Math.random() - 0.5);
      
      const shufEasy = shuffle(easy);
      const shufMedium = shuffle(medium);
      const shufHard = shuffle(hard);
      const shufOthers = shuffle(others);
      
      const selected = [];
      
      // Select balanced set: 1 Easy, 2 Medium, 2 Hard
      const easyPart = shufEasy.splice(0, 1);
      const mediumPart = shufMedium.splice(0, 2);
      const hardPart = shufHard.splice(0, 2);
      
      selected.push(...easyPart, ...mediumPart, ...hardPart);
      
      // Fallback borrowing: if we have fewer than 5, borrow from other categories
      const remainingPool = [...shufMedium, ...shufHard, ...shufEasy, ...shufOthers];
      while (selected.length < 5 && remainingPool.length > 0) {
        selected.push(remainingPool.shift());
      }
      
      const questions = selected.map(q => {
        try {
          return { ...q, options: JSON.parse(q.options) };
        } catch (e) {
          return q;
        }
      });
      return res.json({ questions });
    }

    // Otherwise, generate questions using Gemini AI
    if (!genAI) {
      return res.status(500).json({ error: 'Gemini AI API Key is not configured on the server' });
    }

    const chapterRes = await query('SELECT ch.*, s.name as subject_name FROM chapters ch JOIN subjects s ON ch.subject_id = s.id WHERE ch.id = $1', [chapterId]);
    if (chapterRes.rows.length === 0) {
      return res.status(404).json({ error: 'Topic not found' });
    }
    const chapter = chapterRes.rows[0];

    const prompt = `
      Bạn là chuyên gia giáo dục tiểu học tại Việt Nam, chuyên luyện thi học sinh lớp 5 ôn thi vào lớp 6 trường chất lượng cao.
      Hãy tạo ra 5 câu hỏi luyện tập (trắc nghiệm) bám sát chương trình học cho chủ đề sau:
      - Môn học: "${chapter.subject_name}"
      - Danh mục lớn: "${chapter.parent_chapter}"
      - Nhóm chuyên đề: "${chapter.sub_chapter}"
      - Chủ điểm chi tiết: "${chapter.title_vn}" (Tiếng Anh: "${chapter.title_en}")
      
      Yêu cầu thiết kế câu hỏi:
      1. Độ khó: Phù hợp với học sinh lớp 5 ôn thi vào lớp 6. Có sự phân hóa từ nhận biết đến vận dụng.
      2. Mỗi câu hỏi phải là trắc nghiệm có đúng 4 phương án lựa chọn (A, B, C, D), bắt đầu bằng chữ cái "A. ", "B. ", "C. ", "D. ".
      3. Đáp án chính xác phải trùng khớp hoàn toàn với một trong bốn phương án lựa chọn.
      4. Có gợi ý (hint) ngắn gọn giúp trẻ định hướng cách làm.
      5. Có giải thích (explanation) chi tiết, khoa học nhưng dễ hiểu với trẻ em.
      
      Xuất kết quả duy nhất ở định dạng JSON thô có cấu trúc như sau:
      {
        "questions": [
          {
            "question_text": "Đề bài câu hỏi...",
            "options": ["A. Phương án 1", "B. Phương án 2", "C. Phương án 3", "D. Phương án 4"],
            "correct_answer": "A. Phương án 1",
            "explanation": "Giải thích chi tiết tại sao chọn phương án này...",
            "hint": "Gợi ý làm bài..."
          }
        ]
      }
    `;

    console.log(`🤖 Call Gemini with fallback chain to generate questions for topic: "${chapter.name}" (Subject: ${chapter.subject_name})...`);
    const result = await generateContentWithFallback(prompt, 'application/json');
    const response = await result.response;
    textRes = response.text();

    // Clean and sanitize the JSON string from Gemini (e.g. handle LaTeX unescaped backslashes)
    cleanedText = textRes.trim();
    if (cleanedText.startsWith('```')) {
      cleanedText = cleanedText.replace(/^```json\s*/i, '').replace(/```$/, '').trim();
    }
    cleanedText = cleanedText.replace(/\\([a-zA-Z]+|[\(\)\[\]\{\}])/g, (match, p1) => {
      if (['n', 't', 'r', 'b', 'f'].includes(p1)) return match;
      if (p1.startsWith('u') && p1.length === 5 && /^[0-9a-fA-F]{4}$/.test(p1.slice(1))) return match;
      return '\\\\' + p1;
    });

    const data = JSON.parse(cleanedText);

    const questionsList = data.questions || [];
    const insertedQuestions = [];

    for (const q of questionsList) {
      const optionsJson = JSON.stringify(q.options);
      
      let newId;
      const isPostgres = getUsePostgres();
      if (isPostgres) {
        const insertRes = await query(
          `INSERT INTO questions (
            chapter_id, question_text, question_type, options, correct_answer, explanation, hint
          ) VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING id`,
          [
            chapterId,
            q.question_text,
            q.question_type || 'multiple_choice',
            optionsJson,
            q.correct_answer,
            q.explanation || '',
            q.hint || ''
          ]
        );
        newId = insertRes.rows[0]?.id;
      } else {
        const insertRes = await query(
          `INSERT INTO questions (
            chapter_id, question_text, question_type, options, correct_answer, explanation, hint
          ) VALUES (?, ?, ?, ?, ?, ?, ?)`,
          [
            chapterId,
            q.question_text,
            q.question_type || 'multiple_choice',
            optionsJson,
            q.correct_answer,
            q.explanation || '',
            q.hint || ''
          ]
        );
        newId = insertRes.lastID;
      }
      
      insertedQuestions.push({
        id: newId,
        chapter_id: chapterId,
        question_text: q.question_text,
        question_type: q.question_type || 'multiple_choice',
        options: q.options,
        correct_answer: q.correct_answer,
        explanation: q.explanation || '',
        hint: q.hint || ''
      });
    }

    res.json({ questions: insertedQuestions });
  } catch (error) {
    console.error('Error generating questions:', error);
    console.error('Raw Gemini response was:', textRes);
    console.error('Cleaned text was:', cleanedText);
    res.status(500).json({ error: 'Failed to retrieve or generate questions' });
  }
});

// 2d. Submit Topic Practice Results (and calculate Spaced Repetition)
app.post('/api/chapters/:id/practice', async (req, res) => {
  const chapterId = parseInt(req.params.id, 10);
  const { score, total_questions, correct_answers } = req.body;

  try {
    const chRes = await query('SELECT box_number, interval_days FROM chapters WHERE id = $1', [chapterId]);
    if (chRes.rows.length === 0) {
      return res.status(404).json({ error: 'Topic not found' });
    }

    const current = chRes.rows[0];
    let box = current.box_number || 1;
    let interval = current.interval_days || 0;

    if (score >= 80) {
      box = Math.min(box + 1, 5);
      const intervalMap = { 1: 1, 2: 3, 3: 7, 4: 14, 5: 30 };
      interval = intervalMap[box] || 30;
    } else if (score >= 50) {
      box = Math.max(1, box);
      interval = 1;
    } else {
      box = 1;
      interval = 1;
    }

    const isPostgres = getUsePostgres();
    if (isPostgres) {
      await query(`
        UPDATE chapters 
        SET current_score = $1,
            box_number = $2,
            interval_days = $3,
            next_review_date = CURRENT_DATE + CAST($4 AS INTEGER)
        WHERE id = $5
      `, [score, box, interval, interval, chapterId]);
    } else {
      await query(`
        UPDATE chapters 
        SET current_score = $1,
            box_number = $2,
            interval_days = $3,
            next_review_date = DATE('now', '+' || $4 || ' days')
        WHERE id = $5
      `, [score, box, interval, interval, chapterId]);
    }

    await query(
      'INSERT INTO topic_practice_logs (chapter_id, score, total_questions, correct_answers) VALUES ($1, $2, $3, $4)',
      [chapterId, score, total_questions, correct_answers]
    );

    const xpAwarded = correct_answers * 10;
    await awardXP(xpAwarded);

    res.json({
      success: true,
      score,
      box_number: box,
      next_review_in: interval,
      xp_awarded: xpAwarded
    });
  } catch (error) {
    console.error('Error logging practice session:', error);
    res.status(500).json({ error: 'Failed to record practice session' });
  }
});

// 3. Get Flashcards by Chapter
app.get('/api/flashcards', async (req, res) => {
  const { chapter_id } = req.query;
  try {
    let result;
    if (chapter_id) {
      result = await query('SELECT f.*, s.box_number, s.next_review_date FROM flashcards f LEFT JOIN spaced_repetition_states s ON f.id = s.flashcard_id WHERE f.chapter_id = $1 ORDER BY f.id ASC', [chapter_id]);
    } else {
      result = await query('SELECT f.*, s.box_number, s.next_review_date FROM flashcards f LEFT JOIN spaced_repetition_states s ON f.id = s.flashcard_id ORDER BY f.id ASC');
    }
    res.json(result.rows);
  } catch (error) {
    console.error('Error getting flashcards:', error);
    res.status(500).json({ error: 'Failed to retrieve flashcards' });
  }
});

// 4. Create Flashcard
app.post('/api/flashcards', async (req, res) => {
  const { chapter_id, sub_topic_id, front_content, back_content, hint, image_url } = req.body;
  try {
    // Insert flashcard
    const insertRes = await query(
      'INSERT INTO flashcards (chapter_id, sub_topic_id, front_content, back_content, hint, image_url) VALUES ($1, $2, $3, $4, $5, $6) RETURNING id',
      [chapter_id, sub_topic_id || null, front_content, back_content, hint || null, image_url || null]
    );
    const newCardId = insertRes.rows[0]?.id || insertRes.lastID;

    // Create default spaced repetition state for this card
    await query(
      'INSERT INTO spaced_repetition_states (flashcard_id, box_number, easiness_factor, repetition_count, interval_days, next_review_date) VALUES ($1, 1, 2.5, 0, 0, CURRENT_DATE) ON CONFLICT (flashcard_id) DO NOTHING',
      [newCardId]
    );

    res.json({ success: true, id: newCardId });
  } catch (error) {
    console.error('Error creating flashcard:', error);
    res.status(500).json({ error: 'Failed to create flashcard' });
  }
});

// 5. Get Due Flashcards for Today (Active Recall Deck)
app.get('/api/study/due', async (req, res) => {
  try {
    // Select flashcards due today or earlier
    const result = await query(`
      SELECT f.*, s.box_number, s.easiness_factor, s.repetition_count, s.interval_days, ch.subject_id 
      FROM flashcards f 
      JOIN spaced_repetition_states s ON f.id = s.flashcard_id 
      JOIN chapters ch ON f.chapter_id = ch.id
      WHERE s.next_review_date <= CURRENT_DATE 
      ORDER BY s.box_number DESC, f.id ASC
    `);
    res.json(result.rows);
  } catch (error) {
    console.error('Error getting due flashcards:', error);
    res.status(500).json({ error: 'Failed to retrieve due flashcards' });
  }
});

// 6. Review Flashcard (Submit Rating)
app.post('/api/study/review', async (req, res) => {
  const { card_id, score } = req.body; // score is 1 (Very Hard), 2 (Hard), 3 (Good), 4 (Easy)
  
  try {
    // Get current repetition state
    const stateRes = await query('SELECT * FROM spaced_repetition_states WHERE flashcard_id = $1', [card_id]);
    if (stateRes.rows.length === 0) {
      return res.status(404).json({ error: 'Spaced repetition state not found for this card' });
    }

    const current = stateRes.rows[0];
    let box = current.box_number || 1;
    let ef = current.easiness_factor || 2.5;
    let rep = current.repetition_count || 0;
    let interval = current.interval_days || 0;

    // Map Child's 1-4 scale to traditional SM-2 quality scores (1-5)
    // 1 (Very Hard) -> traditional 1 (Incorrect, but remembered)
    // 2 (Hard) -> traditional 3 (Correct, with significant effort)
    // 3 (Good) -> traditional 4 (Correct, with minor effort)
    // 4 (Easy) -> traditional 5 (Perfect recall)
    const qualityMap = { 1: 1, 2: 3, 3: 4, 4: 5 };
    const q = qualityMap[score] || 3;

    // SM-2 Calculation
    if (q >= 3) {
      if (rep === 0) {
        interval = 1; // 1 day
      } else if (rep === 1) {
        interval = 3; // 3 days
      } else {
        interval = Math.round(interval * ef);
      }
      rep = rep + 1;
      box = Math.min(box + 1, 5); // Leitner box increases
    } else {
      rep = 0;
      interval = 1; // review again in 1 day
      box = 1; // reset to box 1
    }

    // Adjust Easiness Factor
    ef = ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02));
    if (ef < 1.3) ef = 1.3;
    ef = parseFloat(ef.toFixed(2));

    // Calculate next review date
    // SQLite uses DATE('now', '+N days') or DATE('now'), Postgres uses CURRENT_DATE + N
    const updateRes = await query(`
      UPDATE spaced_repetition_states 
      SET box_number = $1, 
          easiness_factor = $2, 
          repetition_count = $3, 
          interval_days = $4, 
          next_review_date = (CURRENT_DATE + CAST($5 AS INTEGER)), 
          last_reviewed_at = CURRENT_TIMESTAMP,
          updated_at = CURRENT_TIMESTAMP
      WHERE flashcard_id = $6
    `, [box, ef, rep, interval, interval, card_id]);

    // Insert into study logs for history
    await query(
      'INSERT INTO study_logs (flashcard_id, score) VALUES ($1, $2)',
      [card_id, score]
    );

    // Update Achievements (XP and Streak)
    const xpAwarded = 10;
    await awardXP(xpAwarded);

    res.json({ 
      success: true, 
      xp_awarded: xpAwarded,
      next_review_in: interval, 
      box_number: box 
    });

  } catch (error) {
    console.error('Error reviewing flashcard:', error);
    res.status(500).json({ error: 'Failed to submit review' });
  }
});

// 7. Get Study Stats (XP, Streak, Progress)
app.get('/api/study/stats', async (req, res) => {
  try {
    const achRes = await query('SELECT * FROM achievements LIMIT 1');
    const totalCardsRes = await query('SELECT COUNT(*) as count FROM flashcards');
    const dueCardsRes = await query('SELECT COUNT(*) as count FROM spaced_repetition_states WHERE next_review_date <= CURRENT_DATE');
    const logsRes = await query('SELECT COUNT(*) as count FROM study_logs');
    
    const achievements = achRes.rows[0] || { streak_days: 0, total_score: 0, last_active_date: null, badges_unlocked: [] };
    const totalCards = parseInt(totalCardsRes.rows[0]?.count || 0);
    const dueCards = parseInt(dueCardsRes.rows[0]?.count || 0);
    const totalReviews = parseInt(logsRes.rows[0]?.count || 0);

    res.json({
      streak_days: achievements.streak_days,
      total_score: achievements.total_score,
      total_cards: totalCards,
      due_cards: dueCards,
      total_reviews: totalReviews,
    });
  } catch (error) {
    console.error('Error getting stats:', error);
    res.status(500).json({ error: 'Failed to retrieve stats' });
  }
});

// 8. AI Generate Flashcards via Gemini
app.post('/api/ai/generate-flashcards', async (req, res) => {
  const { text, subject_name, count = 5 } = req.body;
  
  if (!genAI) {
    return res.status(500).json({ error: 'Gemini AI API Key is not configured on the server' });
  }
  
  if (!text) {
    return res.status(400).json({ error: 'Missing text content to generate flashcards from' });
  }

  try {
    const prompt = `
      Bạn là chuyên gia giáo dục tiểu học tại Việt Nam. Hãy đọc đoạn văn bản sau và tự động tạo ra ${count} thẻ Flashcards học tập giúp học sinh ghi nhớ theo phương pháp Active Recall (Chủ động nhớ lại).
      Đoạn văn bản: "${text}"
      Môn học: "${subject_name || 'Học tập'}"

      Yêu cầu thiết kế thẻ:
      - Mặt trước (front): Là câu hỏi, từ khóa bị khuyết (fill-in-the-blank) hoặc bài toán/câu đố cần giải. Đối với Toán, hãy đưa ra đề bài. Đối với Tiếng Anh, hãy ghi rõ từ cần đoán hoặc câu điền từ. Đối với Tiếng Việt, hãy hỏi cách dùng từ, nghĩa từ hoặc câu nghệ thuật.
      - Mặt sau (back): Là đáp án chính xác kèm theo giải thích chi tiết, ngắn gọn phù hợp với trẻ lớp 5 ôn thi vào 6.
      - Gợi ý (hint): Là một gợi ý nhỏ giúp trẻ suy luận khi gặp khó khăn (Ví dụ: Chữ cái đầu tiên, công thức vận tốc...).

      Hãy xuất kết quả duy nhất ở định dạng JSON thô có cấu trúc như sau:
      {
        "flashcards": [
          {
            "front": "Nội dung mặt trước",
            "back": "Nội dung mặt sau và giải thích",
            "hint": "Gợi ý"
          }
        ]
      }
    `;

    console.log(`🤖 Call Gemini with fallback chain to generate flashcards...`);
    const result = await generateContentWithFallback(prompt, 'application/json');
    const response = await result.response;
    const textRes = response.text();
    
    res.json(JSON.parse(textRes));
  } catch (error) {
    console.error('Error generating AI flashcards:', error);
    res.status(500).json({ error: 'Failed to generate flashcards via Gemini API' });
  }
});

// Phục vụ các file tĩnh của Frontend React (dist/)
app.use(express.static(path.join(__dirname, '../dist')));

// Fallback tất cả các route khác về index.html (SPA routing)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../dist/index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Active Recall Study Sync Server running on port ${PORT}`);
});
