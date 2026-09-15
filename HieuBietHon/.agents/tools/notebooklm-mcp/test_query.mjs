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
    console.log('Found page. Inspecting textareas...');
    
    const textareas = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('textarea')).map(ta => ({
        tag: 'textarea',
        className: ta.className,
        id: ta.id,
        placeholder: ta.placeholder,
        value: ta.value
      }));
    });
    
    console.log('Found Textareas:', JSON.stringify(textareas, null, 2));
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
