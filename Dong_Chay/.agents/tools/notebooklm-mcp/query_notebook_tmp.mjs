import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/f6296b14-a456-47e9-b24a-a5a2b3a7dc9b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";
const statePath = "/Users/pro16/Library/Application Support/notebooklm-mcp/browser_state/state.json";

async function run() {
  console.log("🚀 Launching Chrome in headless mode...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-sandbox',
    ]
  });

  // Inject cookies from state.json
  if (fs.existsSync(statePath)) {
    try {
      const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));
      if (state && Array.isArray(state.cookies) && state.cookies.length > 0) {
        await context.addCookies(state.cookies);
        console.log(`✅ Manually injected ${state.cookies.length} cookies into persistent context.`);
      }
    } catch (err) {
      console.warn(`⚠️ Failed to manually inject cookies: ${err}`);
    }
  } else {
    console.warn(`⚠️ State file not found at: ${statePath}`);
  }

  const page = await context.newPage();
  console.log(`🌐 Navigating to: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(10000); // Wait for page load

  // Find chat textarea
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (!(await chatInput.isVisible())) {
    console.error("❌ Chat input not found! Capturing screenshot...");
    await page.screenshot({ path: 'debug_not_found.png' });
    console.log("📸 Screenshot saved to debug_not_found.png");
    
    // Dump page text content to check if it's the login screen
    const textContent = await page.evaluate(() => document.body.innerText);
    console.log("\n--- BODY TEXT CONTENT START ---");
    console.log(textContent.substring(0, 1000));
    console.log("--- BODY TEXT CONTENT END ---\n");
    
    await context.close();
    return;
  }

  const question = "Trong các tài liệu nguồn của notebook này, Vingroup có tuyên bố trở thành doanh nghiệp kiến tạo hay tập đoàn công nghệ - công nghiệp không? Định nghĩa kiến tạo là gì? Hãy trích xuất thông tin chính xác từ tài liệu, tránh ảo giác.";
  console.log(`⌨️ Typing question: "${question}"`);
  await chatInput.click();
  await chatInput.fill(question);
  await page.waitForTimeout(1000);

  console.log("📤 Submitting question...");
  await page.keyboard.press('Enter');
  await page.waitForTimeout(5000); // Wait for response to start

  console.log("⏳ Waiting for response...");
  let lastText = "";
  let stableCount = 0;
  for (let i = 0; i < 30; i++) {
    const responses = page.locator('.chat-response, .response-bubble, .message-content, chat-response, .markdown-content');
    const count = await responses.count();
    let currentText = "";
    if (count > 0) {
      currentText = await responses.last().innerText();
    }
    
    console.log(`  [${i}] Text length: ${currentText.length}`);
    if (currentText.length > 0 && currentText === lastText) {
      stableCount++;
      if (stableCount >= 3) {
        console.log("✅ Response stabilized!");
        break;
      }
    } else {
      stableCount = 0;
      lastText = currentText;
    }
    await page.waitForTimeout(3000);
  }

  console.log("\n======================================\nRESPONSE:\n");
  console.log(lastText);
  console.log("\n======================================\n");
  
  await context.close();
}

run().catch(err => console.error(err));
