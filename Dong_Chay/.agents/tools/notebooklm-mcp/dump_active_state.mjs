import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/82423261-2307-4bda-9621-35220650023b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();
  await page.goto(notebookUrl);
  await page.waitForTimeout(5000);
  
  const html = await page.content();
  fs.writeFileSync('/tmp/active_state_dom.html', html);
  await page.screenshot({ path: '/tmp/active_state_screenshot.png' });
  console.log("DOM and screenshot saved.");
  await context.close();
}

run().catch(console.error);
