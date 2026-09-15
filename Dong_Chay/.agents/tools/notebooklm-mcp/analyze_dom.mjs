import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to analyze NotebookLM DOM...");
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

  // Chụp ảnh màn hình kiểm tra trạng thái
  const screenshotPath = "/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/tools/notebooklm-mcp/notebooklm_loaded.png";
  await page.screenshot({ path: screenshotPath });
  console.log(`📸 Screenshot saved to ${screenshotPath}`);

  // Tìm tất cả các textarea và input
  const textareas = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('textarea')).map(t => ({
      tagName: t.tagName,
      className: t.className,
      placeholder: t.placeholder,
      ariaLabel: t.getAttribute('aria-label'),
      id: t.id
    }));
  });

  console.log("📝 Textareas found on page:", textareas);

  // Tìm các nút bấm có thể liên quan đến việc gửi tin nhắn
  const buttons = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('button')).map(b => ({
      text: b.innerText || b.textContent,
      className: b.className,
      ariaLabel: b.getAttribute('aria-label'),
      icon: b.querySelector('mat-icon')?.textContent || ""
    })).filter(b => b.ariaLabel || b.icon || b.text);
  });

  console.log("🔘 Key buttons found on page:", buttons.slice(0, 30));

  await context.close();
}

run().catch(err => console.error(err));
