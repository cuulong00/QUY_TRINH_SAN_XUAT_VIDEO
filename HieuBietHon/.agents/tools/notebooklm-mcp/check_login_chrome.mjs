import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

async function testProfile(profileName) {
  const sourceCookies = `/Users/pro16/Library/Application Support/Google/Chrome/${profileName}/Cookies`;
  const destDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile/Default';
  const destCookies = path.join(destDir, 'Cookies');
  
  if (!fs.existsSync(sourceCookies)) {
    console.log(`Profile ${profileName} cookies do not exist.`);
    return false;
  }
  
  console.log(`\n--- Testing ${profileName} ---`);
  console.log(`Copying cookies from ${profileName}...`);
  fs.mkdirSync(destDir, { recursive: true });
  fs.copyFileSync(sourceCookies, destCookies);
  
  // Clean up lock files to prevent locking errors
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
  const lockFiles = ['SingletonLock', 'SingletonSocket', 'SingletonCookie'];
  for (const file of lockFiles) {
    const lockPath = path.join(userDataDir, file);
    if (fs.existsSync(lockPath)) {
      try { fs.unlinkSync(lockPath); } catch {}
    }
  }
  
  console.log('Launching headless official Google Chrome...');
  try {
    const browser = await chromium.launchPersistentContext(userDataDir, {
      headless: true,
      channel: 'chrome' // Crucial: use official Chrome to decrypt the copied cookies!
    });
    
    const page = browser.pages()[0] || await browser.newPage();
    console.log('Navigating to NotebookLM home...');
    await page.goto('https://notebooklm.google.com/', { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(3000);
    
    const url = page.url();
    const title = await page.title();
    console.log('URL:', url);
    console.log('Title:', title);
    
    const isLoggedIn = url.includes('notebook') && !url.includes('signin');
    console.log(`Is logged in with ${profileName}:`, isLoggedIn);
    
    await page.screenshot({ path: `/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/check_${profileName}.png` });
    
    await browser.close();
    return isLoggedIn;
  } catch (err) {
    console.error(`Error testing ${profileName}:`, err.message);
    return false;
  }
}

async function main() {
  // Try Profile 2 first (most recently modified)
  let loggedIn = await testProfile('Profile 2');
  if (loggedIn) {
    console.log('Success! Logged in using Profile 2.');
    return;
  }
  
  // Try Default second
  loggedIn = await testProfile('Default');
  if (loggedIn) {
    console.log('Success! Logged in using Default profile.');
    return;
  }

  // Try Profile 36 third
  loggedIn = await testProfile('Profile 36');
  if (loggedIn) {
    console.log('Success! Logged in using Profile 36.');
    return;
  }
  
  console.log('Failed to log in automatically using any Chrome profiles.');
}

main().catch(console.error);
