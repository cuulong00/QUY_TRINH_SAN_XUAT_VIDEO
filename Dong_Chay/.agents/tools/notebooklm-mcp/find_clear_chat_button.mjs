import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome to search for clear chat button...");
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

  // Tìm tất cả các button và in ra thông tin chi tiết
  const buttonsInfo = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('button, [role="button"], mat-icon')).map(el => {
      const iconText = el.tagName === 'MAT-ICON' ? el.textContent : el.querySelector('mat-icon')?.textContent;
      return {
        tagName: el.tagName,
        text: el.innerText || el.textContent || "",
        className: el.className,
        ariaLabel: el.getAttribute('aria-label') || el.getAttribute('title') || "",
        icon: iconText || ""
      };
    });
  });

  // Lọc ra các phần tử có khả năng là nút xóa chat hoặc chat mới
  const potentialButtons = buttonsInfo.filter(b => {
    const txt = b.text.toLowerCase();
    const lbl = b.ariaLabel.toLowerCase();
    const cls = b.className.toLowerCase();
    const ico = b.icon.toLowerCase();
    
    return txt.includes('xóa') || txt.includes('clear') || txt.includes('mới') || txt.includes('new') || txt.includes('reset') ||
           lbl.includes('xóa') || lbl.includes('clear') || lbl.includes('mới') || lbl.includes('new') || lbl.includes('reset') ||
           ico.includes('delete') || ico.includes('clear') || ico.includes('refresh') || ico.includes('restart') || ico.includes('bin') || ico.includes('trash') ||
           cls.includes('delete') || cls.includes('clear') || cls.includes('reset');
  });

  console.log("🔍 Potential clear/new chat buttons found:");
  console.log(JSON.stringify(potentialButtons, null, 2));

  // Chụp ảnh màn hình toàn cảnh khu vực chat
  await page.screenshot({ path: "/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/chat_layout_debug.png" });
  console.log("📸 Screenshot saved to scratch/chat_layout_debug.png");

  await context.close();
}

run().catch(err => console.error(err));
