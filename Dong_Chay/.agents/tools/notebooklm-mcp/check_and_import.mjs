import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/eff2b2e7-4c41-4b26-a863-ce8b664775ee";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching chromium with profile...");
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
  
  console.log("⏳ Waiting 15 seconds for page to load and stabilize...");
  await page.waitForTimeout(15000);
  
  // Take screenshot and save DOM of current state
  await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/nblm_current.png' });
  const html = await page.content();
  fs.writeFileSync('/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/nblm_current.html', html);
  console.log("📸 Current state screenshot and DOM saved.");

  // Check if Add Sources dialog is open and close it if necessary
  const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').first();
  if (await closeBtn.isVisible()) {
    console.log("⚠️ Found Add Sources dialog. Clicking close button...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(3000);
    await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/nblm_after_close_dialog.png' });
  }

  // Look for the Import (Nhập) button
  console.log("🔍 Looking for Import button...");
  const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').first();
  if (await importBtn.isVisible()) {
    console.log("✅ Import button is visible! Clicking it...");
    await importBtn.click({ force: true });
    console.log("⏳ Waiting 15 seconds for import to process...");
    await page.waitForTimeout(15000);
    
    await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/nblm_after_import.png' });
    console.log("📸 Screenshot after import saved.");
    
    // Clear completed search if delete button is visible
    const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').first();
    if (await deleteBtn.isVisible()) {
      console.log("🧹 Clearing completed search panel...");
      await deleteBtn.click({ force: true });
      await page.waitForTimeout(3000);
    }
  } else {
    console.log("❌ Import button is NOT visible.");
    
    // Let's print out all visible buttons to debug
    const buttons = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('button')).map(b => ({
        text: (b.innerText || b.textContent || '').trim(),
        class: b.className,
        visible: b.getBoundingClientRect().width > 0 && b.getBoundingClientRect().height > 0
      })).filter(b => b.text || b.class);
    });
    console.log("🔘 Visible buttons on page:", buttons.filter(b => b.visible));
  }

  await context.close();
  console.log("🏁 Done.");
}

run().catch(console.error);
