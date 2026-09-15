import { query, initDatabase } from './db.js';

const run = async () => {
  try {
    await initDatabase();
    const res = await query("SELECT id, name, theory FROM chapters WHERE theory IS NOT NULL AND theory != ''");
    console.log(`Checking ${res.rows.length} chapters...`);
    
    for (const ch of res.rows) {
      // Find all iframe src attributes
      const matches = ch.theory.matchAll(/src="([^"]+)"/g);
      const urls = Array.from(matches).map(m => m[1]);
      
      if (urls.length === 0) {
        console.log(`Chapter ID ${ch.id} "${ch.name}": No iframe URLs found.`);
        continue;
      }
      
      for (let url of urls) {
        // Replace &amp; with &
        url = url.replace(/&amp;/g, '&');
        try {
          const checkRes = await fetch(url, { method: 'HEAD', timeout: 5000 });
          console.log(`Chapter ID ${ch.id} "${ch.name.slice(0, 30)}...": URL: ${url.slice(0, 60)}... -> Status: ${checkRes.status}`);
        } catch (err) {
          console.log(`Chapter ID ${ch.id} "${ch.name.slice(0, 30)}...": URL: ${url.slice(0, 60)}... -> ERROR: ${err.message}`);
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
