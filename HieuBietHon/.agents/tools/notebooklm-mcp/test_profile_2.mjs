import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

async function testProfile2() {
  const profileName = 'Profile 2';
  const sourceCookies = `/Users/pro16/Library/Application Support/Google/Chrome/${profileName}/Cookies`;
  const destDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile_p2/Default';
  const destCookies = path.join(destDir, 'Cookies');
  
  if (!fs.existsSync(sourceCookies)) {
    console.error(`Profile ${profileName} cookies do not exist.`);
    return;
  }
  
  console.log(`Copying cookies from ${profileName}...`);
  fs.mkdirSync(destDir, { recursive: true });
  fs.copyFileSync(sourceCookies, destCookies);
  
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile_p2';
  
  // Clean up lock files
  const lockFiles = ['SingletonLock', 'SingletonSocket', 'SingletonCookie'];
  for (const file of lockFiles) {
    const lockPath = path.join(userDataDir, file);
    if (fs.existsSync(lockPath)) {
      try { fs.unlinkSync(lockPath); } catch {}
    }
  }
  
  console.log('Launching headless Chrome with Profile 2 cookies...');
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: true,
    channel: 'chrome'
  });
  
  try {
    const page = browser.pages()[0] || await browser.newPage();
    console.log('Navigating to NotebookLM URL...');
    await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(5000);
    
    const url = page.url();
    const title = await page.title();
    console.log('Final URL:', url);
    console.log('Final Title:', title);
    
    const isLoggedIn = url.includes('notebook') && !url.includes('signin');
    console.log('Is Logged In:', isLoggedIn);
    
    // Take a screenshot to verify what it sees
    const screenshotPath = '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/test_profile_2_result.png';
    await page.screenshot({ path: screenshotPath });
    console.log('Screenshot saved to:', screenshotPath);
    
  } catch (err) {
    console.error('Error during test:', err);
  } finally {
    await browser.close();
  }
}

testProfile2().catch(console.error);
