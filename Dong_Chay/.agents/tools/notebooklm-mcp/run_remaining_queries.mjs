import { chromium } from 'patchright';

const notebookUrl = "https://notebooklm.google.com/notebook/82423261-2307-4bda-9621-35220650023b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const queries = [
  "Napoleon Hill brain as broadcasting station pseudoscience electromagnetism physics analysis",
  "Law of Attraction pseudoscience psychology magical thinking cognitive reframing",
  "Think and Grow Rich victim blaming self help ideology socioeconomic factors",
  "Napoleon Hill biography frauds scams bankruptcies Matt Novak Gizmodo analysis",
  "Scientific benefits of visualization in goal setting mental contrasting Gabriele Oettingen WOOP",
  "How positive fantasizing drains energy motivation psychology studies Gabriele Oettingen"
];

async function run() {
  console.log("🚀 Launching Chrome context with persistent profile...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-first-run',
      '--no-default-browser-check',
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-gpu',
    ]
  });

  const page = await context.newPage();
  console.log(`🌐 Navigating to notebook: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(8000);

  // Helper to count sources
  async function countSources() {
    try {
      const c1 = await page.locator('.single-source-container').count();
      const c2 = await page.locator('input.mdc-checkbox__native-control').count();
      const checkboxCount = c2 > 0 ? c2 - 1 : 0;
      return Math.max(c1, checkboxCount);
    } catch {
      return 0;
    }
  }

  // Helper to dismiss overlays
  async function dismissOverlays() {
    try {
      const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').filter({ visible: true }).first();
      if (await closeBtn.isVisible()) {
        await closeBtn.click({ force: true });
        console.log("  ✅ Closed popup overlay");
        await page.waitForTimeout(1000);
      }
    } catch (e) {}

    try {
      const backdrop = page.locator('.cdk-overlay-backdrop').filter({ visible: true }).first();
      if (await backdrop.isVisible()) {
        await page.keyboard.press('Escape');
        console.log("  ✅ Pressed Escape for backdrop");
        await page.waitForTimeout(1000);
      }
    } catch (e) {}
  }

  // Helper to handle pending imports and clear panel
  async function clearSearchPanel() {
    await dismissOverlays();
    const importBtn = page.locator('button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
    if (await importBtn.isVisible()) {
      console.log("  ✅ Found Import button! Clicking it...");
      await importBtn.click({ force: true });
      await page.waitForTimeout(8000);
    }

    const deleteBtn = page.locator('button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').filter({ visible: true }).first();
    if (await deleteBtn.isVisible()) {
      console.log("  🧹 Clearing completed search panel...");
      await deleteBtn.click({ force: true });
      await page.waitForTimeout(3000);
    }
  }

  await dismissOverlays();
  await clearSearchPanel();

  let sourcesBefore = await countSources();
  console.log(`📊 Starting sources count: ${sourcesBefore}`);

  for (let idx = 0; idx < queries.length; idx++) {
    const query = queries[idx];
    console.log(`\n======================================`);
    console.log(`📝 Query ${idx + 2}/7: "${query}"`);
    console.log(`======================================`);

    try {
      await dismissOverlays();
      await clearSearchPanel();

      // 1. Switch to Deep Research mode if not already there
      const trigger = page.locator('button.corpus-select.researcher-menu-trigger, button.corpus-select:has-text("Nghiên cứu nhanh"), button.corpus-select:has-text("Nghiên cứu sâu"), button.corpus-select:has-text("Deep Research"), button.corpus-select:has(mat-icon:has-text("search_spark"))').filter({ visible: true }).first();
      if (await trigger.isVisible()) {
        const text = await trigger.textContent();
        if (!text.includes('Deep Research') && !text.includes('Nghiên cứu sâu')) {
          console.log("  🔄 Switching mode trigger to Deep Research...");
          await trigger.click({ force: true });
          await page.waitForTimeout(1500);

          const deepOption = page.locator('.cdk-overlay-pane button.research-option-deep-research, .cdk-overlay-pane button:has-text("Deep Research"), .cdk-overlay-pane button:has-text("Nghiên cứu sâu")').filter({ visible: true }).first();
          if (await deepOption.isVisible()) {
            await deepOption.click({ force: true });
            await page.waitForTimeout(2000);
            console.log(`  ✅ Switched to Deep Research mode: "${await trigger.textContent()}"`);
          }
        } else {
          console.log("  ✅ Already in Deep Research mode");
        }
      }

      // 2. Type query into textarea
      const textarea = page.locator('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]').filter({ visible: true }).first();
      if (!(await textarea.isVisible())) {
        throw new Error("Textarea is not visible!");
      }

      const isDisabled = await textarea.isDisabled();
      if (isDisabled) {
        console.log("  ⚠️ Textarea is disabled! Attempting recovery via page reload...");
        await page.reload();
        await page.waitForTimeout(8000);
        await dismissOverlays();
        await clearSearchPanel();
        if (await textarea.isDisabled()) {
          throw new Error("Textarea remains disabled after page reload recovery!");
        }
      }

      console.log("  ⌨️ Typing query...");
      await textarea.click({ force: true });
      await textarea.fill(query);
      await page.waitForTimeout(500);

      // 3. Submit search
      console.log("  📤 Submitting search...");
      const submitBtn = page.locator('button.actions-enter-button, button[aria-label="Gửi"], button[aria-label="Submit"]').filter({ visible: true }).first();
      if (await submitBtn.isVisible() && !(await submitBtn.isDisabled())) {
        await submitBtn.click({ force: true });
      } else {
        await page.keyboard.press('Enter');
      }
      await page.waitForTimeout(5000);

      // 4. Wait for completion
      console.log("  ⏳ Waiting for Deep Research to complete (timeout: 10 minutes)...");
      const startTime = Date.now();
      const timeoutMs = 600000;
      let querySuccess = false;
      let progressLog = "";

      while (Date.now() - startTime < timeoutMs) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        
        // Check for Import button
        const importBtnLoop = page.locator('button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
        if (await importBtnLoop.isVisible()) {
          console.log(`  ✅ Import button appeared after ${elapsed}s! Clicking...`);
          await importBtnLoop.click({ force: true });
          await page.waitForTimeout(8000);

          const deleteBtn = page.locator('button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').filter({ visible: true }).first();
          if (await deleteBtn.isVisible()) {
            console.log("  🧹 Clearing completed search panel...");
            await deleteBtn.click({ force: true });
            await page.waitForTimeout(2000);
          }

          const newCount = await countSources();
          console.log(`  📊 Sources count updated: ${newCount} (added ${newCount - sourcesBefore} sources)`);
          sourcesBefore = newCount;
          querySuccess = true;
          break;
        }

        // Read status
        const hasProgress = await page.locator('mat-progress-bar, [role="progressbar"], mat-progress-spinner, [class*="spinner"]').count() > 0;
        const status = hasProgress ? `Researching... (${elapsed}s)` : `Waiting... (${elapsed}s)`;
        if (status !== progressLog) {
          console.log(`    ${status}`);
          progressLog = status;
        }

        await page.waitForTimeout(5000);
      }

      if (!querySuccess) {
        throw new Error("Deep Research wait timed out!");
      }

      console.log(`  ✅ Query ${idx + 2} successfully completed!`);

    } catch (queryErr) {
      console.error(`  ❌ Error processing query ${idx + 2}:`, queryErr.message);
      try {
        await page.screenshot({ path: `/tmp/error_query_${idx+2}.png` });
        console.log(`  📸 Saved error screenshot to /tmp/error_query_${idx+2}.png`);
      } catch (screenshotErr) {}
    }
  }

  const finalSources = await countSources();
  console.log(`\n🎉 All remaining Deep Research queries completed! Final sources count: ${finalSources}`);

  console.log("🔒 Closing context...");
  await context.close();
}

run().catch(err => {
  console.error("❌ Uncaught error in main runner:", err);
});
