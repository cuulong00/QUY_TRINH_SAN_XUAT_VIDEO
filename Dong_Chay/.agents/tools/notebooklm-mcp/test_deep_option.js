import { chromium } from 'patchright';
import { randomDelay } from './dist/utils/stealth-utils.js';
import fs from 'fs';

(async () => {
  console.log("Khởi động Chrome với profile hiện tại...");
  const profilePath = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
  
  const context = await chromium.launchPersistentContext(profilePath, {
    headless: true,
    viewport: { width: 1280, height: 800 },
  });

  const page = await context.newPage();
  const url = "https://notebooklm.google.com/notebook/a92ef47c-1822-4b43-8476-7b9c8db09ec6";
  
  console.log(`Điều hướng đến: ${url}`);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await randomDelay(5000, 7000);

  // Click vào nút researcher-menu-trigger
  const trigger = page.locator('button.corpus-select.researcher-menu-trigger').first();
  if (await trigger.isVisible()) {
    console.log("Tìm thấy researcher-menu-trigger! Đang click...");
    await trigger.click();
    await randomDelay(2000, 3000);
    
    // Chụp màn hình và lưu DOM sau khi click
    await page.screenshot({ path: '/tmp/nblm_menu_debug.png' });
    const domHtml = await page.content();
    fs.writeFileSync('/tmp/nblm_menu_dom.html', domHtml);
    console.log("Đã lưu screenshot và DOM sau khi click menu trigger.");
    
    // Tìm các phần tử menu item xuất hiện trong overlay
    const menuItems = await page.locator('.cdk-overlay-pane button, .cdk-overlay-pane [role="menuitem"], .cdk-overlay-pane span').all();
    console.log(`Tìm thấy ${menuItems.length} elements trong overlay:`);
    for (const item of menuItems) {
      const text = await item.textContent();
      const outer = await item.evaluate(el => el.outerHTML);
      if (text && text.trim().length > 0) {
        console.log(`- Text: "${text.trim().replace(/\s+/g, ' ')}" | Tag: ${outer.substring(0, 150)}`);
      }
    }
  } else {
    console.log("Không tìm thấy researcher-menu-trigger trên trang!");
    // Screenshot to debug
    await page.screenshot({ path: '/tmp/nblm_not_found.png' });
    console.log("Đã chụp screenshot khi không tìm thấy nút.");
  }

  await context.close();
})();
