import { query } from './db.js';

const run = async () => {
  try {
    const subjects = await query('SELECT * FROM subjects');
    console.log('Subjects:', subjects.rows);
    
    const chaptersCount = await query('SELECT subject_id, COUNT(*) FROM chapters GROUP BY subject_id');
    console.log('Chapters count by subject:', chaptersCount.rows);
    
    const flashcardsCount = await query('SELECT COUNT(*) FROM flashcards');
    console.log('Total flashcards:', flashcardsCount.rows);
    
    const allFlashcards = await query(`
      SELECT f.id, f.front_content, f.chapter_id, ch.subject_id, s.name as subject_name, ch.name as chapter_name 
      FROM flashcards f 
      JOIN chapters ch ON f.chapter_id = ch.id
      JOIN subjects s ON ch.subject_id = s.id
      ORDER BY f.id ASC
    `);
    console.log('--- All Flashcards ---');
    allFlashcards.rows.forEach(card => {
      console.log(`[ID: ${card.id}] Subject: ${card.subject_name} | Chapter ID: ${card.chapter_id} | Name: ${card.chapter_name.slice(0, 40)}... | Front: ${card.front_content.slice(0, 30)}...`);
    });
    
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

run();
