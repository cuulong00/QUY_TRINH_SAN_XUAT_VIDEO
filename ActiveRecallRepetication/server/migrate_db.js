import { query, getUsePostgres } from './db.js';
import sqlite3 from 'sqlite3';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

async function runMigration() {
  console.log('🔄 Starting database migration...');
  
  // Trigger connection fallback check if Postgres is down
  try {
    await query('SELECT 1');
  } catch (e) {
    // Ignore error, fallback has already triggered if needed
  }
  
  const isPostgres = getUsePostgres();
  
  try {
    if (isPostgres) {
      console.log('🐘 Migrating PostgreSQL database...');
      // In Postgres, we can use ADD COLUMN IF NOT EXISTS (since Postgres 9.6+)
      await query(`
        ALTER TABLE learning_recall.questions 
        ADD COLUMN IF NOT EXISTS difficulty VARCHAR(50)
      `);
      await query(`
        ALTER TABLE learning_recall.questions 
        ADD COLUMN IF NOT EXISTS cognitive_level VARCHAR(50)
      `);
      await query(`
        ALTER TABLE learning_recall.questions 
        ADD COLUMN IF NOT EXISTS grade_level INT
      `);
      console.log('✅ PostgreSQL database migrated successfully.');
    } else {
      console.log('📦 Migrating local SQLite database...');
      const dbPath = path.join(__dirname, 'database.sqlite');
      if (!fs.existsSync(dbPath)) {
        console.log('ℹ️ SQLite database file does not exist yet. It will be created with the new schema on first start.');
        return;
      }
      
      const db = new sqlite3.Database(dbPath);
      
      const getColumns = () => {
        return new Promise((resolve, reject) => {
          db.all('PRAGMA table_info(questions)', (err, rows) => {
            if (err) reject(err);
            else resolve(rows.map(r => r.name));
          });
        });
      };
      
      const runSql = (sql) => {
        return new Promise((resolve, reject) => {
          db.run(sql, (err) => {
            if (err) reject(err);
            else resolve();
          });
        });
      };
      
      const cols = await getColumns();
      console.log('Current columns in SQLite questions table:', cols);
      
      if (!cols.includes('difficulty')) {
        console.log('Adding column "difficulty" to SQLite questions table...');
        await runSql('ALTER TABLE questions ADD COLUMN difficulty TEXT');
      }
      if (!cols.includes('cognitive_level')) {
        console.log('Adding column "cognitive_level" to SQLite questions table...');
        await runSql('ALTER TABLE questions ADD COLUMN cognitive_level TEXT');
      }
      if (!cols.includes('grade_level')) {
        console.log('Adding column "grade_level" to SQLite questions table...');
        await runSql('ALTER TABLE questions ADD COLUMN grade_level INTEGER');
      }
      
      db.close();
      console.log('✅ SQLite database migrated successfully.');
    }
  } catch (err) {
    console.error('❌ Migration failed:', err);
    process.exit(1);
  }
  
  process.exit(0);
}

runMigration();
