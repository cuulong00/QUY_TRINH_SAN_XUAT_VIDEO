import { chromium } from 'patchright';

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
    console.log('Found page. Listing all chat messages...');
    
    const info = await page.evaluate(() => {
      const messages = Array.from(document.querySelectorAll('chat-message'));
      return messages.map(msg => {
        const isToUser = msg.querySelector('.to-user-container') !== null;
        const text = msg.innerText;
        return {
          type: isToUser ? 'model' : 'user',
          textLength: text.length,
          preview: text.substring(0, 100) + '...'
        };
      });
    });
    
    console.log('Chat messages:', JSON.stringify(info, null, 2));
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
