import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to debug message content...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-sandbox',
    ]
  });

  const page = await context.newPage();
  await page.goto(notebookUrl);
  await page.waitForTimeout(10000);

  const responseSelector = '.message-content, chat-response, .chat-response';
  
  // Gửi câu hỏi 1
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (await chatInput.isVisible()) {
    await chatInput.click();
    await chatInput.fill("Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha của Vinhomes tại Việt Nam.");
    await page.keyboard.press('Enter');
    console.log("📤 Sent question! Waiting 40 seconds for generation...");
    await page.waitForTimeout(40000);

    const count = await page.locator(responseSelector).count();
    console.log(`📊 Message count: ${count}`);
    if (count > 0) {
      const lastText = await page.locator(responseSelector).last().innerText();
      console.log(`📝 Last message length: ${lastText.length}`);
      console.log("================ MESSAGE CONTENT ================");
      console.log(lastText);
      console.log("=================================================");
    }
    
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_debug_screenshot.png" });
    console.log("📸 Screenshot saved to scratch/chat_debug_screenshot.png");
  } else {
    console.log("❌ Chat input not found!");
  }

  await context.close();
}

run().catch(err => console.error(err));
