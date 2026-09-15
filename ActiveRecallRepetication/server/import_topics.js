import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { query, initDatabase, seedDefaultFlashcards, getUsePostgres } from './db.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Paths to scraped JSON files
const SCRATCH_DIR = '/Users/pro16/.gemini/antigravity/brain/8b31e1dd-e953-4604-a59b-16e1cc887483/scratch';
const MATH_PATH = path.join(SCRATCH_DIR, 'math_topics.json');
const VN_PATH = path.join(SCRATCH_DIR, 'vietnamese_topics.json');
const ENG_PATH = path.join(SCRATCH_DIR, 'english_topics.json');

const main = async () => {
  console.log('📖 Reading JSON files...');
  const mathData = JSON.parse(fs.readFileSync(MATH_PATH, 'utf-8'));
  const vnData = JSON.parse(fs.readFileSync(VN_PATH, 'utf-8'));
  const engData = JSON.parse(fs.readFileSync(ENG_PATH, 'utf-8'));

  console.log(`Loaded:
  - Math: ${mathData.length} topics
  - Tiếng Việt: ${vnData.length} topics
  - Tiếng Anh: ${engData.length} topics
  `);

  try {
    // 1. Drop existing tables to ensure clean schema recreation
    console.log('🗑️ Dropping existing tables for clean schema recreation...');
    await query('DROP TABLE IF EXISTS study_logs');
    await query('DROP TABLE IF EXISTS spaced_repetition_states');
    await query('DROP TABLE IF EXISTS questions');
    await query('DROP TABLE IF EXISTS topic_practice_logs');
    await query('DROP TABLE IF EXISTS flashcards');
    await query('DROP TABLE IF EXISTS chapters');
    await query('DROP TABLE IF EXISTS subjects');
    await query('DROP TABLE IF EXISTS achievements');

    console.log('🏗️ Recreating database schemas...');
    await initDatabase();

    // 2. Helper to insert topics for a subject
    const insertTopics = async (topics, subjectId) => {
      console.log(`📥 Inserting topics for Subject ID: ${subjectId}...`);
      let count = 0;
      for (const t of topics) {
        const name = `${t.subChapter} - ${t.titleVn}`;
        const parentChapter = t.parentChapter || '';
        const subChapter = t.subChapter || '';
        const titleVn = t.titleVn || '';
        const titleEn = t.titleEn || '';
        const url = t.href || '';
        const originalScore = parseInt(t.score || '0', 10);
        const sortOrder = count + 1;

        await query(
          `INSERT INTO chapters (
            subject_id, name, parent_chapter, sub_chapter, title_vn, title_en, url, original_score, sort_order
          ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)`,
          [
            subjectId,
            name.slice(0, 250),
            parentChapter.slice(0, 250),
            subChapter.slice(0, 250),
            titleVn.slice(0, 250),
            titleEn.slice(0, 250),
            url.slice(0, 500),
            originalScore,
            sortOrder
          ]
        );
        count++;
      }
      console.log(`✅ Inserted ${count} chapters for Subject ID: ${subjectId}`);
    };

    // 3. Insert Math
    await insertTopics(mathData, 1);

    // 4. Insert Tiếng Việt
    await insertTopics(vnData, 2);

    // 5. Insert English
    await insertTopics(engData, 3);

    // 6. Seed default flashcards now that chapters exist
    console.log('🌱 Seeding default flashcards (with dynamic chapter resolution)...');
    // Clear flashcards and states just in case initDatabase tried to seed them beforehand
    await query('DELETE FROM spaced_repetition_states');
    await query('DELETE FROM flashcards');
    
    // Reset sequence if postgres
    try {
      await query('ALTER SEQUENCE flashcards_id_seq RESTART WITH 1');
      await query('ALTER SEQUENCE spaced_repetition_states_id_seq RESTART WITH 1');
    } catch (e) {
      // Ignore if SQLite
    }

    const isPostgres = getUsePostgres();
    await seedDefaultFlashcards(query, isPostgres);

    console.log('🎉 Successfully imported all TAK12 syllabus topics and seeded default flashcards!');
    process.exit(0);
  } catch (error) {
    console.error('❌ Error during import:', error);
    process.exit(1);
  }
};

main();
