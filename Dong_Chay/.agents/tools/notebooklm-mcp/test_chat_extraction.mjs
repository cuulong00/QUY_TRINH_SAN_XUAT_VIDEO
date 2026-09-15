import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to test chat extraction...");
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

  // Tìm textarea chat
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (!(await chatInput.isVisible())) {
    console.error("❌ Chat input not found!");
    await context.close();
    return;
  }

  console.log("⌨️ Typing test question...");
  await chatInput.click();
  await chatInput.fill("Vinhomes đang sở hữu quỹ đất bao nhiêu hecta tại Việt Nam?");
  await page.waitForTimeout(1000);

  console.log("📤 Submitting question via Enter...");
  await page.keyboard.press('Enter');
  await page.waitForTimeout(5000); // Đợi phản hồi bắt đầu sinh

  // Đợi câu trả lời hoàn thành. 
  // NotebookLM thường hiển thị progress bar hoặc hiệu ứng pulsing trong lúc sinh.
  // Ta có thể đợi cho đến khi nút gửi (actions-enter-button) không còn bị disabled hoặc đợi một khoảng thời gian cố định và check xem văn bản đã ngừng thay đổi chưa.
  console.log("⏳ Waiting for response...");
  let lastText = "";
  let stableCount = 0;
  for (let i = 0; i < 30; i++) {
    // Lấy câu trả lời mới nhất (thường nằm trong chat-response hoặc container markdown)
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

  // Dump các phần tử chứa câu trả lời để nghiên cứu class của nó
  const htmlDump = await page.evaluate(() => {
    // Lấy nội dung xung quanh phần chat
    const chats = document.querySelectorAll('chat-response, .chat-response, .response-bubble, .markdown-content');
    return Array.from(chats).map(c => ({
      tagName: c.tagName,
      className: c.className,
      text: c.innerText || c.textContent
    }));
  });

  console.log("📝 Chat Responses found:", htmlDump);
  
  await context.close();
}

run().catch(err => console.error(err));
