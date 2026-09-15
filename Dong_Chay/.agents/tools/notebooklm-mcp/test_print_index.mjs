import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to inspect chat messages...");
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
  console.log(`🌐 Navigating to: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(10000); // Đợi tải xong

  const responseSelector = '.message-content, chat-response, .chat-response';
  const countBefore = await page.locator(responseSelector).count();
  console.log(`📊 Message count before sending: ${countBefore}`);

  // In ra nội dung của tất cả tin nhắn cũ
  const textsBefore = await page.evaluate((sel) => {
    return Array.from(document.querySelectorAll(sel)).map((el, i) => ({
      index: i,
      tagName: el.tagName,
      className: el.className,
      length: el.innerText.length,
      preview: el.innerText.substring(0, 100)
    }));
  }, responseSelector);
  console.log("📝 Messages BEFORE sending:", textsBefore);

  // Tìm textarea chat và gửi câu hỏi 1
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (await chatInput.isVisible()) {
    await chatInput.click();
    await chatInput.fill("Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha của Vinhomes tại Việt Nam.");
    await page.keyboard.press('Enter');
    console.log("📤 Sent question! Waiting 15 seconds...");
    await page.waitForTimeout(15000);

    const countAfter = await page.locator(responseSelector).count();
    console.log(`📊 Message count after sending: ${countAfter}`);

    // In ra nội dung của tất cả tin nhắn sau khi gửi
    const textsAfter = await page.evaluate((sel) => {
      return Array.from(document.querySelectorAll(sel)).map((el, i) => ({
        index: i,
        tagName: el.tagName,
        className: el.className,
        length: el.innerText.length,
        preview: el.innerText.substring(0, 100)
      }));
    }, responseSelector);
    console.log("📝 Messages AFTER sending:", textsAfter);
  } else {
    console.log("❌ Chat input not found!");
  }

  await context.close();
}

run().catch(err => console.error(err));
