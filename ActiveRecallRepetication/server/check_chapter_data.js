import { query, initDatabase } from './db.js';

const run = async () => {
  try {
    await initDatabase();
    
    // Find the chapter
    const chapterRes = await query("SELECT * FROM chapters WHERE name LIKE '%Từ loại%' OR name LIKE '%Danh từ, động từ%'");
    console.log('--- Matching Chapters ---');
    console.log(chapterRes.rows);
    
    if (chapterRes.rows.length > 0) {
      for (const ch of chapterRes.rows) {
        // Count questions for this chapter
        const qCountRes = await query("SELECT COUNT(*) as count FROM questions WHERE chapter_id = ?", [ch.id]);
        console.log(`\nChapter ID: ${ch.id}`);
        console.log(`Name: ${ch.name}`);
        console.log(`Has Theory: ${ch.theory ? 'YES' : 'NO'} (length: ${ch.theory ? ch.theory.length : 0})`);
        console.log(`Questions Count: ${qCountRes.rows[0].count}`);
        
        // Show sample questions if any
        if (qCountRes.rows[0].count > 0) {
          const qRes = await query("SELECT id, question_text FROM questions WHERE chapter_id = ? LIMIT 3", [ch.id]);
          console.log('Sample questions:');
          qRes.rows.forEach(q => console.log(`- [Q ID: ${q.id}] ${q.question_text.slice(0, 80)}...`));
        }
      }
    }
    
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

run();
