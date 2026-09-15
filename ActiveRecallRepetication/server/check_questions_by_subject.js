import { query, initDatabase } from './db.js';

const run = async () => {
  try {
    await initDatabase();
    
    // Group questions by subject
    const res = await query(`
      SELECT ch.subject_id, s.name as subject_name, COUNT(q.id) as question_count
      FROM chapters ch
      JOIN subjects s ON ch.subject_id = s.id
      LEFT JOIN questions q ON q.chapter_id = ch.id
      GROUP BY ch.subject_id, s.name
    `);
    console.log('--- Questions count by subject ---');
    console.log(res.rows);
    
    // Check how many chapters have 0 questions
    const zeroRes = await query(`
      SELECT ch.subject_id, s.name as subject_name, COUNT(*) as chapters_with_zero_questions
      FROM chapters ch
      JOIN subjects s ON ch.subject_id = s.id
      LEFT JOIN (
        SELECT chapter_id, COUNT(*) as count FROM questions GROUP BY chapter_id
      ) q ON q.chapter_id = ch.id
      WHERE q.count IS NULL OR q.count = 0
      GROUP BY ch.subject_id, s.name
    `);
    console.log('\n--- Chapters with ZERO questions ---');
    console.log(zeroRes.rows);
    
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

run();
