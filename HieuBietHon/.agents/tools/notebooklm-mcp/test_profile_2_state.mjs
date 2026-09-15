import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

async function testWithLocalState() {
  const chromeDir = '/Users/pro16/Library/Application Support/Google/Chrome';
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile_test_state';
  
  const destDefaultDir = path.join(userDataDir, 'Default');
  fs.mkdirSync(destDefaultDir, { recursive: true });
  
  // Copy Local State
  const sourceLocalState = path.join(chromeDir, 'Local State');
  const destLocalState = path.join(userDataDir, 'Local State');
  if (fs.existsSync(sourceLocalState)) {
    console.log('Copying Local State...');
    fs.copyFileSync(sourceLocalState, destLocalState);
  } else {
    console.error('Local State does not exist at:', sourceLocalState);
    return;
  }
  
  // Copy Profile 2 Cookies to Default/Cookies
  const sourceCookies = path.join(chromeDir, 'Profile 2', 'Cookies');
  const destCookies = path.join(destDefaultDir, 'Cookies');
  if (fs.existsSync(sourceCookies)) {
    console.log('Copying Profile 2 Cookies...');
    fs.copyFileSync(sourceCookies, destCookies);
  } else {
    console.error('Profile 2 Cookies do not exist at:', sourceCookies);
    return;
  }
  
  // Clean up lock files
  const lockFiles = ['SingletonLock', 'SingletonSocket', 'SingletonCookie'];
  for (const file of lockFiles) {
    const lockPath = path.join(userDataDir, file);
    if (fs.existsSync(lockPath)) {
      try { fs.unlinkSync(lockPath); } catch {}
    }
  }
  
  console.log('Launching headless Chrome with copied Local State and Profile 2 cookies...');
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
    
    const screenshotPath = '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/test_profile_2_state_result.png';
    await page.screenshot({ path: screenshotPath });
    console.log('Screenshot saved to:', screenshotPath);
    
  } catch (err) {
    console.error('Error during test:', err);
  } finally {
    await browser.close();
  }
}

testWithLocalState().catch(console.error);
