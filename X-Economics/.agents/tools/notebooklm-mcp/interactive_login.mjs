import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

async function run() {
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
  
  // Clean up lock files before starting
  const lockFiles = ['SingletonLock', 'SingletonSocket', 'SingletonCookie'];
  for (const file of lockFiles) {
    const lockPath = path.join(userDataDir, file);
    if (fs.existsSync(lockPath)) {
      try {
        fs.unlinkSync(lockPath);
        console.log(`Removed stale lock file: ${file}`);
      } catch (err) {
        console.error(`Failed to remove lock file ${file}:`, err.message);
      }
    }
  }

  console.log('Launching headed Playwright Chromium with zero system conflicts...');
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    // Using default Playwright Chromium (no channel: 'chrome') to prevent version conflicts
    viewport: { width: 1280, height: 800 }
  });
  
  const page = browser.pages()[0] || await browser.newPage();
  console.log('Navigating to NotebookLM...');
  await page.goto('https://notebooklm.google.com/', { waitUntil: 'domcontentloaded' });
  
  console.log('\n==================================================================');
  console.log('Cửa sổ trình duyệt Chromium đã được mở.');
  console.log('Hãy thực hiện đăng nhập tài khoản Google của bạn.');
  console.log('Sau khi đăng nhập thành công và nhìn thấy trang chủ NotebookLM,');
  console.log('hãy TẮT CỬA SỔ TRÌNH DUYỆT này để lưu phiên làm việc.');
  console.log('==================================================================\n');
  
  // Keep script running until browser context is closed
  await new Promise((resolve) => {
    browser.on('close', () => {
      console.log('Browser context closed successfully.');
      resolve();
    });
  });
  
  console.log('Authentication complete. Session saved to profile.');
}

run().catch(console.error);
