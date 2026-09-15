import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to debug with screenshots...");
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
  await page.waitForTimeout(10000); // Chờ load trang 10s

  await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_1_loaded.png" });
  console.log("📸 Saved scratch/chat_1_loaded.png");

  // Tìm textarea chat
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (await chatInput.isVisible()) {
    console.log("⌨️ Filling question...");
    await chatInput.click();
    await chatInput.fill("Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha của Vinhomes tại Việt Nam.");
    await page.waitForTimeout(1000);
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_2_filled.png" });
    console.log("📸 Saved scratch/chat_2_filled.png");

    console.log("📤 Sending...");
    await page.keyboard.press('Enter');
    await page.waitForTimeout(5000); // Đợi 5s
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_3_sent_5s.png" });
    console.log("📸 Saved scratch/chat_3_sent_5s.png");

    await page.waitForTimeout(15000); // Đợi thêm 15s (tổng 20s)
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_4_sent_20s.png" });
    console.log("📸 Saved scratch/chat_4_sent_20s.png");

    await page.waitForTimeout(30000); // Đợi thêm 30s (tổng 50s)
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_5_sent_50s.png" });
    console.log("📸 Saved scratch/chat_5_sent_50s.png");
  } else {
    console.log("❌ Chat input not found!");
  }

  await context.close();
  console.log("🔒 Done debug session.");
}

run().catch(err => console.error(err));
