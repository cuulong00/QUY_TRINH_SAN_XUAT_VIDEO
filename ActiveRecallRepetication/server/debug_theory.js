import { query, initDatabase } from './db.js';

const run = async () => {
  try {
    await initDatabase();
    const res = await query("SELECT id, name, subject_id, theory FROM chapters WHERE theory IS NOT NULL AND theory != ''");
    console.log(`Found ${res.rows.length} chapters with theory.`);
    res.rows.forEach(ch => {
      console.log(`\nChapter ID: ${ch.id} | Subject: ${ch.subject_id} | Name: ${ch.name}`);
      console.log(`Theory Length: ${ch.theory.length} chars`);
      console.log(`Sample (first 300 chars):`, ch.theory.slice(0, 300));
      console.log(`Sample (last 300 chars):`, ch.theory.slice(-300));
    });
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

run();
