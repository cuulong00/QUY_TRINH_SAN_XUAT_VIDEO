import { chromium } from 'patchright';

async function run() {
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
  console.log('Launching headless browser with profile...');
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: true,
    channel: 'chrome'
  });
  const page = await browser.newPage();
  
  console.log('Navigating to NotebookLM home...');
  await page.goto('https://notebooklm.google.com/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(5000);
  
  const title = await page.title();
  const url = page.url();
  console.log('Page title:', title);
  console.log('Page URL:', url);
  
  const isLoggedIn = url.includes('notebook') && !url.includes('signin');
  console.log('Is logged in:', isLoggedIn);
  
  await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/check_login_result.png' });
  console.log('Screenshot saved to scratch/check_login_result.png');
  
  await browser.close();
}

run().catch(console.error);
