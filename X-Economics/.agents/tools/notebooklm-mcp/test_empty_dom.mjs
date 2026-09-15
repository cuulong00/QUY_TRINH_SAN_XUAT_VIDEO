import { chromium } from 'patchright';
import path from 'path';
import os from 'os';
import fs from 'fs';

(async () => {
  const userDataDir = path.join(os.homedir(), 'Library', 'Application Support', 'Google', 'Chrome');
  const browser = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: false,
  });

  const page = await browser.newPage();
  await page.goto('https://notebooklm.google.com/');
  await page.waitForTimeout(3000);
  
  // Click new notebook
  const newBtn = page.locator('.new-notebook-card, button:has-text("New notebook"), button:has-text("Sổ tay mới")').first();
  if (await newBtn.isVisible()) {
    await newBtn.click();
  }
  await page.waitForTimeout(5000);
  
  // Dump DOM
  const html = await page.content();
  fs.writeFileSync('empty_notebook_dom.html', html);
  await browser.close();
  console.log('DOM saved to empty_notebook_dom.html');
})();
