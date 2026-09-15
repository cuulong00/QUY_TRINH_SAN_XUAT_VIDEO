import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to inspect chat-specific elements...");
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

  // Gửi câu hỏi để tạo bong bóng chat
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (await chatInput.isVisible()) {
    await chatInput.click();
    await chatInput.fill("Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha của Vinhomes tại Việt Nam.");
    await page.keyboard.press('Enter');
    console.log("📤 Sent question! Waiting 15s to let messages render...");
    await page.waitForTimeout(15000);

    // Dump cấu trúc DOM của khung chat ở giữa
    const chatPanelDOM = await page.evaluate(() => {
      // Tìm container của cuộc trò chuyện bằng cách tìm element chứa câu hỏi của ta
      const userMsg = Array.from(document.querySelectorAll('*')).find(el => 
        el.textContent.includes("Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha") &&
        el.tagName !== 'TEXTAREA'
      );
      
      if (!userMsg) return "User message element not found in DOM!";

      // Lấy thẻ cha của nó để xem cấu trúc
      let parent = userMsg.parentElement;
      let hierarchy = [];
      for (let i = 0; i < 5; i++) {
        if (!parent) break;
        hierarchy.push({
          tagName: parent.tagName,
          className: parent.className,
          id: parent.id
        });
        parent = parent.parentElement;
      }
      
      // Tìm tất cả các element là anh em hoặc con của container chat
      // Thường thì khung chat có tag là chat-messages, chat-thread, hoặc có class chat-messages
      const chatContainers = Array.from(document.querySelectorAll('[class*="chat" i], [id*="chat" i], chat-thread, chat-messages, chat-response'));
      
      return {
        hierarchy,
        chatContainers: chatContainers.map(c => ({
          tagName: c.tagName,
          className: c.className,
          textLength: c.innerText?.length || 0,
          preview: c.innerText?.substring(0, 100) || ""
        }))
      };
    });

    console.log("📝 Chat DOM Structure:");
    console.log(JSON.stringify(chatPanelDOM, null, 2));
  } else {
    console.log("❌ Chat input not found!");
  }

  await context.close();
}

run().catch(err => console.error(err));
