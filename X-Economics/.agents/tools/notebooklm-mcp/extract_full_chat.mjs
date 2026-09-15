import { chromium } from 'patchright';
import fs from 'fs';

async function main() {
  console.log('Connecting to Chrome via CDP...');
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  
  const notebookId = '9891a2f0-8e48-445a-a2c4-4b25ee3c3800';
  let page;
  
  for (const ctx of browser.contexts()) {
    const found = ctx.pages().find(p => p.url().includes(notebookId));
    if (found) {
      page = found;
      break;
    }
  }
  
  if (page) {
    console.log('Found page. Extracting body innerText...');
    const fullText = await page.evaluate(() => document.body.innerText);
    
    // Save full page text to a debug file
    fs.writeFileSync('/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch/full_page_text.txt', fullText);
    console.log('Saved full page text to scratch/full_page_text.txt');
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
