import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/82423261-2307-4bda-9621-35220650023b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

async function run() {
  console.log("🚀 Launching Chrome context...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();
  console.log(`🌐 Navigating to ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(8000);

  // Click Nhập if visible
  const importBtn = page.locator('button:has-text("Nhập")').filter({ visible: true }).first();
  if (await importBtn.isVisible()) {
    console.log("  ✅ Found Nhập button! Clicking...");
    await importBtn.click({ force: true });
    await page.waitForTimeout(8000);
  } else {
    console.log("  ❌ Nhập button NOT visible");
  }

  // Click Xoá if visible
  const deleteBtn = page.locator('button:has-text("Xoá")').filter({ visible: true }).first();
  if (await deleteBtn.isVisible()) {
    console.log("  ✅ Found Xoá button! Clicking...");
    await deleteBtn.click({ force: true });
    await page.waitForTimeout(4000);
  } else {
    console.log("  ❌ Xoá button NOT visible");
  }

  // Check if textarea is enabled
  const textarea = page.locator('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]').first();
  if (await textarea.isVisible()) {
    const disabled = await textarea.isDisabled();
    console.log(`  📊 Textarea disabled status: ${disabled}`);
  } else {
    console.log("  ❌ Textarea NOT visible");
  }

  await page.screenshot({ path: '/tmp/test_click_end.png' });
  console.log("📸 Saved screenshot to /tmp/test_click_end.png");
  await context.close();
}

run().catch(console.error);
