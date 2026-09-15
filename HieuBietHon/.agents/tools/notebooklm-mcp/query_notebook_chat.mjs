import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function main() {
  console.log('Connecting to Chrome via CDP...');
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  console.log('Connected!');
  
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
    console.log('Found page. Taking screenshot to see current state...');
    await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/pre_query_chat_state.png' });
    
    // Evaluate page content to find the response text
    const pageText = await page.evaluate(() => {
      // Look at all message content or formatted text elements
      const elements = Array.from(document.querySelectorAll('.conversation-container, .chat-container, mat-sidenav-content, [role="log"]'));
      return elements.map(el => el.innerText).join('\n\n');
    });
    
    console.log('--- Page text content ---');
    console.log(pageText.substring(0, 1000));
    console.log('--- End of page text ---');
    
    // Save page text to output
    fs.writeFileSync('/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/notebooklm_current_chat_content.txt', pageText);
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
