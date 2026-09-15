import puppeteer from 'puppeteer-core';
import { query } from './db.js';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Helper to generate options from correct answer for textbox questions
function generateOptionsFromAnswer(answer, context) {
  let cleanAns = answer.trim();
  if (cleanAns.startsWith('(') && cleanAns.endsWith(')')) {
    cleanAns = cleanAns.slice(1, -1).trim();
  }
  
  // Handle multiple correct options separated by "/"
  const parts = cleanAns.split('/');
  let primaryAnswer = parts[0].trim();
  
  const variations = new Set();
  variations.add(primaryAnswer);
  
  const words = primaryAnswer.split(/[\s,]+/);
  
  // Variation 1: remove last word
  if (words.length > 2) {
    const v1 = words.slice(0, -1).join(', ');
    if (v1 && v1 !== primaryAnswer) variations.add(v1);
  }
  
  // Variation 2: modify word
  const contextWords = context.split(/[\s,，.。“”"':]+/g).filter(w => w.length > 2 && !words.includes(w));
  if (contextWords.length > 0 && words.length > 0) {
    const copy = [...words];
    copy[Math.floor(Math.random() * copy.length)] = contextWords[0];
    const v2 = copy.join(', ');
    if (v2 && v2 !== primaryAnswer) variations.add(v2);
  }
  
  // Variation 3: reverse
  if (words.length > 1) {
    const shuffled = [...words].reverse().join(', ');
    if (shuffled && shuffled !== primaryAnswer) variations.add(shuffled);
  }
  
  const fallbacks = [
    "Đáp án khác",
    primaryAnswer + " (không có)",
    "Không xác định",
    "Không có từ phù hợp"
  ];
  
  for (const fb of fallbacks) {
    if (variations.size >= 4) break;
    variations.add(fb);
  }
  
  const finalOptions = Array.from(variations).slice(0, 4);
  
  // Prefix with A. B. C. D.
  const prefixes = ['A. ', 'B. ', 'C. ', 'D. '];
  const mappedOptions = finalOptions.map((opt, idx) => prefixes[idx] + opt);
  
  return {
    options: mappedOptions,
    correct_answer: mappedOptions[0] // Correct answer is always mapped to A
  };
}

async function scrapeQuizPage(page) {
  const scrapedQuestions = [];
  let lastKey = '';
  
  for (let step = 0; step < 25; step++) {
    console.log(`👉 Scraping question page ${step + 1}...`);
    
    // Wait up to 6 seconds for the page content key to load and be different from lastKey
    let currentKey = '';
    const startTime = Date.now();
    while (Date.now() - startTime < 6000) {
      try {
        currentKey = await page.evaluate(() => {
          const qHeaderEl = document.querySelector('.question-header') || Array.from(document.querySelectorAll('strong')).find(el => /^Question\s*\d+/i.test(el.innerText) || /^Câu\s*\d+/i.test(el.innerText));
          const qHeader = qHeaderEl ? qHeaderEl.innerText.trim() : '';
          
          const questionTextEl = document.querySelector('.question-content, .question-text-container, .quiz-question') || document.querySelector('p');
          const qText = questionTextEl ? questionTextEl.innerText.trim() : '';
          
          const optionEls = Array.from(document.querySelectorAll('.ui.feed .event .content, .option, .choice, .choice-item, li, label'));
          const options = optionEls.map(el => el.innerText.trim()).filter(Boolean).slice(0, 10);
          
          if (!qText && !qHeader) return '';
          return qHeader + '::' + qText + '::' + options.join('|');
        });
        
        if (currentKey && currentKey !== lastKey) {
          break;
        }
      } catch (e) {
        // Suppress and wait for navigation to complete
      }
      await delay(100);
    }
    
    if (!currentKey || currentKey === lastKey) {
      console.log('⚠️ Page key is identical or empty. Checking if Next button exists to skip...');
      const hasNext = await page.evaluate(() => {
        const nextBtn = Array.from(document.querySelectorAll('button, a')).find(b => b.innerText.trim() === 'Next' || b.innerText.trim() === 'Câu tiếp theo');
        if (nextBtn) {
          nextBtn.click();
          return true;
        }
        return false;
      });
      if (hasNext) {
        console.log('⏭️ Clicked Next to skip stuck/reading page.');
        await delay(1000);
        continue;
      } else {
        console.log('🏁 No Next button found. Breaking loop!');
        break;
      }
    }
    lastKey = currentKey;
    
    // 1. Click "Submit" to show "Xem đáp án"
    const clickedSubmit = await page.evaluate(() => {
      const submitBtn = Array.from(document.querySelectorAll('button, a')).find(el => el.innerText.trim() === 'Submit');
      if (submitBtn) {
        submitBtn.click();
        return true;
      }
      return false;
    });
    
    if (clickedSubmit) {
      // Poll for "Nộp" confirmation button and click it
      let clickedNop = false;
      const nopStartTime = Date.now();
      while (Date.now() - nopStartTime < 1500) {
        clickedNop = await page.evaluate(() => {
          const confirmBtn = Array.from(document.querySelectorAll('button, a')).find(el => el.innerText.trim() === 'Nộp');
          if (confirmBtn) {
            confirmBtn.click();
            return true;
          }
          return false;
        });
        if (clickedNop) break;
        await delay(50);
      }
      
      // Poll for "Xem đáp án" button to appear
      const revealStartTime = Date.now();
      let hasRevealBtn = false;
      while (Date.now() - revealStartTime < 2000) {
        hasRevealBtn = await page.evaluate(() => {
          return !!document.querySelector('.can-retry-info-text.text-underline');
        });
        if (hasRevealBtn) break;
        await delay(50);
      }
    }
    
    // 2. Click "Xem đáp án" to reveal correct answer
    const clickedReveal = await page.evaluate(() => {
      const showBtn = document.querySelector('.can-retry-info-text.text-underline');
      if (showBtn) {
        showBtn.click();
        return true;
      }
      return false;
    });
    
    if (clickedReveal) {
      // Poll for checkmarks or correct status to show up
      const checkStartTime = Date.now();
      let hasCheck = false;
      while (Date.now() - checkStartTime < 1500) {
        hasCheck = await page.evaluate(() => {
          return !!(document.querySelector('.check.icon, .fa-check, .text-success, .correct') ||
                    document.querySelector('.text-success, span[style*="color: rgb(33, 186, 69)"], span[style*="color: green"]'));
        });
        if (hasCheck) break;
        await delay(50);
      }
    }
    
    // 3. Click "Giải thích" & "Ghi nhớ" to reveal explanation and memory notes
    const clickedNotes = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button, a'));
      const expBtn = btns.find(b => b.innerText.includes('Giải thích'));
      if (expBtn) expBtn.click();
      const hintBtn = btns.find(b => b.innerText.includes('Ghi nhớ'));
      if (hintBtn) hintBtn.click();
      return !!(expBtn || hintBtn);
    });
    
    if (clickedNotes) {
      // Poll for explanation or hint content container to load
      const notesStartTime = Date.now();
      let hasNotesContent = false;
      while (Date.now() - notesStartTime < 1500) {
        hasNotesContent = await page.evaluate(() => {
          const expContent = document.querySelector('.explanation, .analysis, .explanation-content') || 
                             document.querySelector('[data-testid^="feedback-content-"]');
          const hintContent = document.querySelector('.hint, .suggestion') || 
                              document.querySelector('[data-testid^="question-note-content-"]');
          return !!(expContent || hintContent);
        });
        if (hasNotesContent) break;
        await delay(50);
      }
    }
    
    // 4. Extract question data
    const qData = await page.evaluate(() => {
      const cleanText = (str) => str ? str.replace(/\s+/g, ' ').trim() : '';
      
      // Find split-pane reading passage and stem separately
      const passageEl = document.querySelector('.reading-text-section, .reading-text-panel, .passage-content, .passage, .reading-text');
      const stemEl = document.querySelector('.question-text-container, [data-testid="question-text-container"]');
      
      let questionText = '';
      if (passageEl && stemEl) {
        // If both exist on split screen, combine them
        questionText = passageEl.innerText.trim() + '\n\n' + stemEl.innerText.trim();
      } else if (stemEl) {
        questionText = stemEl.innerText.trim();
      } else {
        // Fallback: clone and remove options/choices to get clean text
        const wrapperEl = document.querySelector('.quiz-question, .question-content') || document.querySelector('p');
        if (wrapperEl) {
          const clone = wrapperEl.cloneNode(true);
          const toRemove = clone.querySelectorAll('.option, .choice, .choice-item, .writing-status-bar, .textarea-container, .prewriting-sidebar, .button-section, button, script, style');
          toRemove.forEach(el => el.remove());
          questionText = clone.innerText.trim();
        }
      }
      
      // Clean up headers like "Question N" or "Câu N" from question text
      const questionHeaderEl = document.querySelector('.question-header') || Array.from(document.querySelectorAll('strong, span')).find(el => /^Question\s*\d+/i.test(el.innerText.trim()) || /^Câu\s*\d+/i.test(el.innerText.trim()));
      if (questionHeaderEl) {
        const headerText = questionHeaderEl.innerText.trim();
        if (questionText.startsWith(headerText)) {
          questionText = questionText.slice(headerText.length).trim();
        }
      }
      
      // Options using feed selectors (.ui.feed .event)
      const feedItems = Array.from(document.querySelectorAll('.ui.feed .event'));
      let options = [];
      let correct_answer = '';
      
      if (feedItems.length > 0) {
        feedItems.forEach(item => {
          const contentEl = item.querySelector('.content');
          if (contentEl) {
            const text = cleanText(contentEl.innerText);
            if (text) {
              options.push(text);
              
              // Check if correct (has check icon)
              const hasCheck = item.querySelector('.check.icon');
              if (hasCheck) {
                correct_answer = text;
              }
            }
          }
        });
      } else {
        // Sibling fallback
        const optionEls = Array.from(document.querySelectorAll('.option, .choice, .choice-item, li, label'));
        if (optionEls.length > 0) {
          optionEls.forEach(optEl => {
            const text = cleanText(optEl.innerText);
            if (text && !options.includes(text) && !text.startsWith('💡') && !text.includes('Giải thích') && !text.startsWith('Retry') && !text.startsWith('Next')) {
              const isCorrect = optEl.querySelector('.fa-check, .text-success, .correct') || text.includes('✔') || optEl.innerText.includes('✔');
              let cleanOpt = text.replace(/^[✔✖]\s*/, '').trim();
              if (cleanOpt) {
                options.push(cleanOpt);
                if (isCorrect) {
                  correct_answer = cleanOpt;
                }
              }
            }
          });
        }
      }
      
      // Textbox correct answer fallbacks
      if (!correct_answer && options.length === 0) {
        const correctTextEls = Array.from(document.querySelectorAll('.text-success, span[style*="color: rgb(33, 186, 69)"], span[style*="color: green"]'));
        if (correctTextEls.length > 0) {
          correct_answer = correctTextEls[0].innerText.trim();
        } else {
          const spans = Array.from(document.querySelectorAll('span'));
          const correctSpan = spans.find(s => s.innerText.trim().startsWith('(') && s.innerText.trim().endsWith(')'));
          if (correctSpan) {
            correct_answer = correctSpan.innerText.trim();
          }
        }
      }
      
      // Explanation
      let explanation = '';
      const expEl = document.querySelector('.explanation, .analysis, .explanation-content') || 
                    Array.from(document.querySelectorAll('div, p')).find(el => el.innerText && (el.innerText.includes('Tính từ là') || el.innerText.includes('Động từ là') || el.innerText.includes('Danh từ là') || el.innerText.includes('Từ “nhưng”')));
      if (expEl) {
        explanation = expEl.innerText.trim();
      } else {
        const items = Array.from(document.querySelectorAll('.question-note-item'));
        const expItem = items.find(item => {
          const btn = item.querySelector('button');
          return btn && btn.innerText.includes('Giải thích');
        });
        if (expItem) {
          const contentEl = expItem.querySelector('[data-testid^="feedback-content-"], .ui.container');
          if (contentEl) {
            explanation = contentEl.innerText.trim();
          }
        }
      }
      
      // Hint / Ghi nhớ
      let hint = '';
      const hintEl = document.querySelector('.hint, .suggestion');
      if (hintEl) {
        hint = hintEl.innerText.replace(/^💡\s*Gợi ý\s*:\s*/, '').trim();
      } else {
        const items = Array.from(document.querySelectorAll('.question-note-item'));
        const hintItem = items.find(item => {
          const btn = item.querySelector('button');
          return btn && btn.innerText.includes('Ghi nhớ');
        });
        if (hintItem) {
          const contentEl = hintItem.querySelector('[data-testid^="question-note-content-"], .ui.container');
          if (contentEl) {
            hint = contentEl.innerHTML.trim(); // Save innerHTML to preserve image/tags
          }
        }
      }
      
      return {
        question_text: questionText,
        options: options,
        correct_answer: correct_answer,
        explanation: explanation,
        hint: hint
      };
    });
    
    if (qData.question_text) {
      let correct = qData.correct_answer;
      let finalOptions = qData.options;
      
      if (finalOptions.length === 0 && correct) {
        const generated = generateOptionsFromAnswer(correct, qData.question_text);
        finalOptions = generated.options;
        correct = generated.correct_answer;
      }
      
      // Ensure prefixes A. B. C. D.
      finalOptions = finalOptions.map((opt, i) => {
        const prefixes = ['A. ', 'B. ', 'C. ', 'D. '];
        if (i < 4 && !/^[A-D]\./i.test(opt)) {
          return prefixes[i] + opt;
        }
        return opt;
      });
      
      if (correct && !/^[A-D]\./i.test(correct)) {
        const idx = finalOptions.findIndex(opt => opt.includes(correct));
        if (idx !== -1) {
          correct = finalOptions[idx];
        } else {
          correct = finalOptions[0] || '';
        }
      }
      
      scrapedQuestions.push({
        question_text: qData.question_text,
        options: finalOptions.slice(0, 4),
        correct_answer: correct,
        explanation: qData.explanation,
        hint: qData.hint
      });
      
      console.log(`✅ Scraped Question ${step + 1}: "${qData.question_text.slice(0, 50)}..."`);
      console.log(`   Choices:`, finalOptions);
      console.log(`   Answer: "${correct}"`);
    }
    
    // Click "Next" button to navigate to next question
    const hasNext = await page.evaluate(() => {
      const nextBtn = Array.from(document.querySelectorAll('button, a')).find(b => b.innerText.trim() === 'Next' || b.innerText.trim() === 'Câu tiếp theo');
      if (nextBtn) {
        nextBtn.click();
        return true;
      }
      return false;
    });
    
    if (!hasNext) {
      console.log('🏁 Reached the end of paginated quiz!');
      break;
    }
    
    await delay(100); // Wait for next page to load
  }
  
  return scrapedQuestions;
}

async function run() {
  const args = process.argv.slice(2);
  let limitSubjectId = 2; // Default to Tiếng Việt (Subject ID 2)
  let singleChapterId = null;
  
  if (args.includes('--subject')) {
    limitSubjectId = parseInt(args[args.indexOf('--subject') + 1], 10);
  }
  if (args.includes('--single')) {
    singleChapterId = parseInt(args[args.indexOf('--single') + 1], 10);
  }
  
  console.log('🔌 Connecting to existing Chrome instance on port 9222...');
  let browser;
  try {
    browser = await puppeteer.connect({
      browserURL: 'http://127.0.0.1:9222',
      defaultViewport: null
    });
    console.log('✅ Connected to browser!');
  } catch (err) {
    console.error('❌ Failed to connect to Chrome. Make sure Chrome is running with --remote-debugging-port=9222');
    console.error('Error message:', err.message);
    process.exit(1);
  }

  // Get chapters to crawl
  let queryText = '';
  let queryParams = [];
  
  if (singleChapterId) {
    queryText = 'SELECT * FROM chapters WHERE id = ?';
    queryParams = [singleChapterId];
  } else {
    // Only crawl chapters for the subject that have less than 5 questions cached
    queryText = `
      SELECT c.id, c.name, c.url 
      FROM chapters c
      LEFT JOIN (
        SELECT chapter_id, COUNT(*) as q_count 
        FROM questions 
        GROUP BY chapter_id
      ) q ON c.id = q.chapter_id
      WHERE c.subject_id = ? AND (q.q_count IS NULL OR q.q_count < 5)
      ORDER BY c.id ASC
    `;
    queryParams = [limitSubjectId];
  }

  const dbResult = await query(queryText, queryParams);
  const chapters = dbResult.rows;
  
  console.log(`📚 Found ${chapters.length} chapters to process.`);
  
  if (chapters.length === 0) {
    console.log('🎉 No chapters need crawling.');
    process.exit(0);
  }
  
  // REUSE existing tab instead of browser.newPage() to avoid "opened in another tab" lockout!
  const pages = await browser.pages();
  let page = pages.find(p => p.url().includes('tak12.com'));
  if (!page) {
    page = await browser.newPage();
  } else {
    console.log(`🔌 Reusing existing browser page: ${page.url()}`);
  }
  
  // Forward browser console logs matching [BROWSER] prefix to Node process
  page.on('console', msg => {
    const txt = msg.text();
    if (txt.startsWith('[BROWSER]')) {
      console.log(`🧭 ${txt}`);
    }
  });
  
  for (const chapter of chapters) {
    if (!chapter.url) {
      console.log(`⚠️ Skip Chapter ID: ${chapter.id} (${chapter.name}) - No URL`);
      continue;
    }
    
    let targetUrl = chapter.url;
    if (targetUrl.startsWith('/')) {
      targetUrl = 'https://tak12.com' + targetUrl;
    }
    
    try {
      // 1. Navigate to chapter main page
      await page.goto(targetUrl, { waitUntil: 'networkidle2', timeout: 30000 });
      await delay(2000);
      
      // Check if we are logged in
      let isLoggedIn = await page.evaluate(() => {
        const bodyText = document.body.innerText;
        return !bodyText.includes('Đăng nhập') || bodyText.includes('Đăng xuất') || bodyText.includes('Trần Hoàng My') || bodyText.includes('My');
      });
      
      if (!isLoggedIn) {
        console.log('⚠️ Session not active. Attempting to click "Đăng nhập" to restore session...');
        const clicked = await page.evaluate(() => {
          const el = Array.from(document.querySelectorAll('a, button, span, div')).find(e => e.innerText.trim() === 'Đăng nhập');
          if (el) {
            el.click();
            return true;
          }
          return false;
        });
        if (clicked) {
          await delay(3000);
          // Check again
          isLoggedIn = await page.evaluate(() => {
            const bodyText = document.body.innerText;
            return !bodyText.includes('Đăng nhập') || bodyText.includes('Đăng xuất') || bodyText.includes('Trần Hoàng My') || bodyText.includes('My');
          });
        }
      }
      
      if (!isLoggedIn) {
        console.error('❌ Session error: Not logged in. Please log in first on TAK12 in your Chrome browser.');
        break; // Halt the crawler if not logged in
      }
      
      // 1.5 Extract theory HTML if it exists
      const theoryHtml = await page.evaluate(() => {
        const el = document.querySelector('.topic-detail-description');
        return el ? el.innerHTML.trim() : '';
      });
      if (theoryHtml) {
        console.log(`   📖 Scraped theory notes (${theoryHtml.length} chars)`);
        await query('UPDATE chapters SET theory = ? WHERE id = ?', [theoryHtml, chapter.id]);
      } else {
        console.log('   ℹ️ No theory notes found on main page.');
      }

      // Loop through difficulties
      const difficulties = [
        { name: 'Dễ', key: 'easy' },
        { name: 'Trung bình', key: 'medium' },
        { name: 'Khó', key: 'hard' }
      ];
      
      const allScrapedQuestions = [];
      
      for (const diff of difficulties) {
        console.log(`   Selected Difficulty: ${diff.name} (${diff.key})`);
        
        // Go back to the main page to open difficulty modal
        await page.goto(targetUrl, { waitUntil: 'networkidle2', timeout: 30000 });
        await delay(2000);
        
        // Click "Chọn độ khó" button
        const clickedModal = await page.evaluate(() => {
          const buttons = Array.from(document.querySelectorAll('button, a'));
          const target = buttons.find(b => b.innerText.trim() === 'Chọn độ khó');
          if (target) {
            console.log('[BROWSER] Clicked Chọn độ khó button');
            target.click();
            return true;
          }
          console.log('[BROWSER] Chọn độ khó button NOT found');
          return false;
        });
        
        if (!clickedModal) {
          console.log(`      ⚠️ "Chọn độ khó" button not found. Scraping default/all...`);
          // Try to click "Luyện ngay" directly
          const detailButton = await page.$('.topic-detail-button');
          if (!detailButton) {
            await page.evaluate(() => {
              const btns = Array.from(document.querySelectorAll('button, a'));
              const target = btns.find(b => {
                const txt = b.innerText.trim();
                return txt === 'Luyện ngay' || txt === 'Luyện tiếp' || txt === 'Làm lại' || txt === 'Tiếp tục luyện';
              });
              if (target) target.click();
            });
          } else {
            await detailButton.click();
          }
        } else {
          await delay(1500);
          
          // Click "Tự chọn"
          const clickedTuChon = await page.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button, submit, [role="button"], a'));
            const target = buttons.find(b => b.innerText.includes('Tự chọn'));
            if (target) {
              console.log('[BROWSER] Clicked Tự chọn button');
              target.click();
              return true;
            }
            console.log('[BROWSER] Tự chọn button NOT found');
            return false;
          });
          
          if (!clickedTuChon) {
            console.log(`      ⚠️ "Tự chọn" button not found inside modal. Skipping difficulty settings.`);
          } else {
            await delay(1000);
            
            // Click difficulty button
            const clickedDiff = await page.evaluate((diffName) => {
              const buttons = Array.from(document.querySelectorAll('button, submit, .option-card-button'));
              const target = buttons.find(b => {
                const txt = b.innerText;
                // Exclude 0 Question/0 câu để tránh click nhầm lúc không có câu hỏi
                return txt.includes(diffName) && !txt.includes('0 Question') && !txt.includes('0 câu');
              });
              if (target) {
                console.log('[BROWSER] Clicked difficulty button:', diffName, target.innerText);
                target.click();
                return true;
              }
              console.log('[BROWSER] Difficulty button NOT found for:', diffName);
              return false;
            }, diff.name);
            
            if (!clickedDiff) {
              console.log(`      ℹ️ No active questions for difficulty "${diff.name}". Skipping this difficulty.`);
              continue;
            }
            
            await delay(1000);
            
            // Click green "Luyện ngay" button in modal
            const clickedConfirm = await page.evaluate(() => {
              const buttons = Array.from(document.querySelectorAll('.ui.green.button, button.green'));
              const target = buttons.find(b => b.innerText.includes('Luyện ngay') || b.innerText.includes('Luyện tiếp') || b.innerText.includes('Làm lại'));
              if (target) {
                console.log('[BROWSER] Clicked final green button:', target.innerText);
                target.click();
                return true;
              }
              console.log('[BROWSER] Final green button NOT found');
              return false;
            });
            
            if (!clickedConfirm) {
              console.log(`      ⚠️ "Luyện ngay" confirmation button not found in modal. Skipping.`);
              continue;
            }
          }
        }
        
        console.log('      ⏳ Waiting for quiz page to load...');
        let currentUrl = page.url();
        const quizWaitStart = Date.now();
        while (Date.now() - quizWaitStart < 8000) {
          currentUrl = page.url();
          if (currentUrl.includes('/q/') || currentUrl.includes('/atid/')) {
            break;
          }
          await delay(200);
        }
        console.log(`      📍 Current quiz URL: ${currentUrl}`);
        
        if (!currentUrl.includes('/q/') && !currentUrl.includes('/atid/')) {
          console.log(`      ⚠️ Did not redirect to a quiz page. Current URL: ${currentUrl}`);
          continue;
        }
        
        console.log('      🔍 Scraping quiz page...');
        const questionsData = await scrapeQuizPage(page);
        
        const validQuestions = questionsData.filter(q => q.options && q.options.length > 0);
        console.log(`      📊 Scraped ${questionsData.length} questions for ${diff.name} (${validQuestions.length} valid).`);
        
        for (const q of validQuestions) {
          q.difficulty = diff.key;
          allScrapedQuestions.push(q);
        }
        
        // Break difficulty loop if "Chọn độ khó" button was not found (default mode has already scraped all)
        if (!clickedModal) {
          break;
        }
        
        await delay(2000);
      }
      
      // Save all scraped questions
      if (allScrapedQuestions.length >= 3) {
        // Delete any existing questions for this chapter
        await query('DELETE FROM questions WHERE chapter_id = ?', [chapter.id]);
        
        let insertCount = 0;
        for (const q of allScrapedQuestions) {
          await query(`
            INSERT INTO questions (
              chapter_id, question_text, question_type, options, correct_answer, explanation, hint, difficulty
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
          `, [
            chapter.id,
            q.question_text,
            'multiple_choice',
            JSON.stringify(q.options),
            q.correct_answer,
            q.explanation || '',
            q.hint || '',
            q.difficulty
          ]);
          insertCount++;
        }
        console.log(`✅ Saved ${insertCount} questions across difficulties for Chapter ID: ${chapter.id} into database.`);
      } else {
        console.log(`⚠️ Too few valid questions parsed total (${allScrapedQuestions.length}). Skipping database update to preserve existing questions.`);
      }
      
    } catch (err) {
      console.error(`❌ Error scraping Chapter ID ${chapter.id}:`, err.message);
    }
    
    await delay(3000);
  }
  
  console.log('\n🎉 Finished crawling questions from TAK12!');
  process.exit(0);
}

run();
