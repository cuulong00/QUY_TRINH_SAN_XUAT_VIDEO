import { chromium } from 'patchright';

async function main() {
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
    console.log('Found page. Taking screenshot...');
    await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch/current_notebook_status.png' });
    console.log('Screenshot saved.');
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
