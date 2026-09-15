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
    console.log('Found page. Dumping sidebar text...');
    // We can evaluate and print the text contents of the left area
    const text = await page.evaluate(() => {
      // Find the sources list container
      // Usually there is a sidebar or container with 'Nguồn' or 'Sources'
      const sidebar = document.querySelector('mat-sidenav, .sidebar, .left-panel, [role="navigation"]') || document.body;
      return sidebar.innerText;
    });
    console.log('--- Sidebar Text Content ---');
    console.log(text.substring(0, 2000));
    console.log('--- End Sidebar Text Content ---');
  } else {
    console.log('Page not found.');
  }
  
  await browser.close();
}

main().catch(console.error);
