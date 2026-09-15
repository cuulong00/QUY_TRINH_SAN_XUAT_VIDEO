import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to test clearing chat...");
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

  // Click vào nút menu 3 chấm ở tiêu đề chat
  // Dựa trên screenshot, tiêu đề là "Cuộc trò chuyện" và bên phải có 3 chấm dọc.
  // Tìm nút 3 chấm trong chat-panel
  console.log("🔍 Locating more_vert menu button in chat-panel...");
  const menuBtn = page.locator('.chat-panel button:has(mat-icon:has-text("more_vert")), .chat-panel-content button:has(mat-icon:has-text("more_vert")), button[aria-label="Xem thêm"]').first();
  
  if (await menuBtn.isVisible()) {
    console.log("🎯 Found menu button! Clicking it...");
    await menuBtn.click({ force: true });
    await page.waitForTimeout(2000);

    // Chụp màn hình menu đang mở
    await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_menu_opened.png" });
    console.log("📸 Screenshot saved to scratch/chat_menu_opened.png");

    // Lấy tất cả các lựa chọn trong menu
    const menuOptions = await page.evaluate(() => {
      const items = document.querySelectorAll('.cdk-overlay-pane button, .mat-mdc-menu-item');
      return Array.from(items).map(el => ({
        text: el.innerText || el.textContent || "",
        className: el.className
      }));
    });

    console.log("📋 Menu options found:", menuOptions);
  } else {
    console.log("❌ Menu button not found in chat-panel!");
  }

  await context.close();
}

run().catch(err => console.error(err));
