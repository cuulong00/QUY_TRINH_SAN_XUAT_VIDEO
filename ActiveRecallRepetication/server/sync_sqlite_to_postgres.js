import pg from 'pg';
import sqlite3 from 'sqlite3';
import path from 'path';
import fs from 'fs';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.join(__dirname, '.env') });

async function runSync() {
  console.log('🔄 Starting SQLite to PostgreSQL sync on VPS...');
  
  // 1. Connect to SQLite
  const sqlitePath = path.join(__dirname, 'database.sqlite');
  if (!fs.existsSync(sqlitePath)) {
    console.error(`❌ SQLite database not found at ${sqlitePath}`);
    process.exit(1);
  }
  
  const sqliteDb = new sqlite3.Database(sqlitePath);
  
  const querySqlite = (sql, params = []) => {
    return new Promise((resolve, reject) => {
      sqliteDb.all(sql, params, (err, rows) => {
        if (err) reject(err);
        else resolve(rows);
      });
    });
  };

  // 2. Connect to PostgreSQL
  const pgPool = new pg.Pool({
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT || '5432'),
    user: process.env.DB_USER || 'n8n',
    password: process.env.DB_PASSWORD || 'n8npassword',
    database: process.env.DB_DATABASE || 'dental_clinic',
  });

  let client = null;
  try {
    // Connect and keep the client active
    client = await pgPool.connect();
    console.log('✅ Connected to PostgreSQL successfully!');
    
    // Set schema search path
    await client.query('SET search_path TO learning_recall, public');
    
    // 3. Load all questions and their chapter details from SQLite
    console.log('📖 Reading questions from SQLite...');
    const sqliteQuestions = await querySqlite(`
      SELECT q.*, c.name as chapter_name, c.url as chapter_url
      FROM questions q
      JOIN chapters c ON q.chapter_id = c.id
    `);
    
    console.log(`📊 Found ${sqliteQuestions.length} total questions in SQLite.`);
    
    if (sqliteQuestions.length === 0) {
      console.log('ℹ️ No questions to sync.');
      sqliteDb.close();
      client.release();
      await pgPool.end();
      process.exit(0);
    }
    
    // Load all Postgres chapters to map them by URL
    const pgChaptersRes = await client.query('SELECT id, name, url FROM chapters');
    const pgChaptersByUrl = new Map();
    const pgChaptersByName = new Map();
    
    pgChaptersRes.rows.forEach(ch => {
      if (ch.url) pgChaptersByUrl.set(ch.url.toLowerCase(), ch.id);
      pgChaptersByName.set(ch.name.toLowerCase(), ch.id);
    });
    
    // 4. Truncate PostgreSQL questions table to do a clean import
    console.log('🗑️ Clearing existing questions in PostgreSQL...');
    await client.query('TRUNCATE TABLE questions RESTART IDENTITY CASCADE');
    
    // 5. Insert questions into PostgreSQL
    console.log('📥 Inserting questions into PostgreSQL (within a single transaction)...');
    await client.query('BEGIN');
    
    let insertCount = 0;
    for (const q of sqliteQuestions) {
      // Find corresponding chapter ID in Postgres
      let pgChapterId = null;
      if (q.chapter_url) {
        pgChapterId = pgChaptersByUrl.get(q.chapter_url.toLowerCase());
      }
      if (!pgChapterId && q.chapter_name) {
        pgChapterId = pgChaptersByName.get(q.chapter_name.toLowerCase());
      }
      
      if (!pgChapterId) {
        console.warn(`⚠️ Could not map SQLite chapter ID ${q.chapter_id} (${q.chapter_name}) to Postgres. Skipping question.`);
        continue;
      }
      
      // Ensure options is double-checked as valid JSON array
      let optionsStr = q.options;
      try {
        // Test parsing, if it fails, try to stringify
        JSON.parse(optionsStr);
      } catch (err) {
        optionsStr = JSON.stringify(q.options);
      }
      
      await client.query(`
        INSERT INTO questions (
          chapter_id, question_text, question_type, options, correct_answer, explanation, hint, difficulty, cognitive_level, grade_level
        ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
      `, [
        pgChapterId,
        q.question_text,
        q.question_type || 'multiple_choice',
        optionsStr,
        q.correct_answer,
        q.explanation || '',
        q.hint || '',
        q.difficulty || null,
        q.cognitive_level || null,
        q.grade_level || null
      ]);
      insertCount++;
    }
    
    await client.query('COMMIT');
    console.log(`✅ Successfully synced ${insertCount} / ${sqliteQuestions.length} questions to PostgreSQL!`);
    
  } catch (err) {
    if (client) {
      try {
        await client.query('ROLLBACK');
      } catch (rbErr) {
        console.error('❌ Rollback failed:', rbErr);
      }
    }
    console.error('❌ Sync failed:', err);
  } finally {
    if (client) {
      client.release();
    }
    sqliteDb.close();
    await pgPool.end();
  }
}

runSync();
