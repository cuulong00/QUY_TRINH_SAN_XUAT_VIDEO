import sqlite3 from 'sqlite3';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dbPath = path.join(__dirname, 'database.sqlite');

const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  // Count questions per chapter
  db.all(`
    SELECT c.id, c.subject_id, c.name, c.parent_chapter, c.sub_chapter, c.title_vn, COALESCE(q.q_count, 0) as q_count
    FROM chapters c
    LEFT JOIN (
      SELECT chapter_id, COUNT(*) as q_count
      FROM questions
      GROUP BY chapter_id
    ) q ON c.id = q.chapter_id
    ORDER BY c.subject_id ASC, c.id ASC
  `, [], (err, rows) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    console.log(`Total chapters: ${rows.length}`);
    const noQuestions = rows.filter(r => r.q_count === 0);
    console.log(`Chapters with 0 questions: ${noQuestions.length}`);

    noQuestions.forEach(r => {
      console.log(`- ID: ${r.id} | Subject: ${r.subject_id} | Name: ${r.name} | Title: ${r.title_vn}`);
    });

    db.close();
  });
});
