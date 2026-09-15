import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const queries = [
  "Vinhomes quỹ đất Việt Nam 29.500 ha lớn nhất thị trường dự án mới phát triển 5-7 năm",
  "Vinhomes kế hoạch tài chính 2026 doanh thu 250.000 tỷ lợi nhuận 50.000 tỷ và áp lực tài chính",
  "Vingroup DRC Holding Congo Kinshasa 6.300 ha đại đô thị ven sông",
  "VHM debt ratio interest expense cash flow support VinFast financial pressure",
  "Vingroup Congo green transport VinFast GSM electric vehicles 300.000 vehicles",
  "Democratic Republic of the Congo infrastructure investment risks political instability Kinshasa GDP"
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
  async function handlePendingImport() {
    await dismissOverlays();
    
    const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
    const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').filter({ visible: true }).first();
    
    if (await importBtn.isVisible()) {
      console.log("  ✅ Found pending Import button! Clicking it...");
      await importBtn.click({ force: true });
      await page.waitForTimeout(10000); // Wait for import to complete
    }

    if (await deleteBtn.isVisible()) {
      console.log("  🧹 Clearing completed search panel...");
      await deleteBtn.click({ force: true });
      await page.waitForTimeout(3000);
    }
  }

  await dismissOverlays();
  await handlePendingImport();

  let sourcesBefore = await countSources();
  console.log(`📊 Starting sources count: ${sourcesBefore}`);

  // Now execute each query in sequence
  for (let idx = 0; idx < queries.length; idx++) {
    const query = queries[idx];
    console.log(`\n======================================`);
    console.log(`📝 Query ${idx + 1}/${queries.length}: "${query}"`);
    console.log(`======================================`);

    try {
      // Refresh the page for a clean slate
      console.log("  🔄 Refreshing page for a clean slate...");
      await page.reload();
      await page.waitForTimeout(10000);
      await dismissOverlays();
      await handlePendingImport();

      // 1. Switch to Deep Research mode
      const trigger = page.locator('button.corpus-select.researcher-menu-trigger, button.corpus-select:has-text("Nghiên cứu nhanh"), button.corpus-select:has-text("Nghiên cứu sâu"), button.corpus-select:has-text("Deep Research"), button.corpus-select:has(mat-icon:has-text("search_spark"))').filter({ visible: true }).first();
      if (await trigger.isVisible()) {
        const text = await trigger.textContent();
        if (!text.includes('Deep Research') && !text.includes('Nghiên cứu sâu')) {
          console.log("  🔄 Switching mode trigger to Deep Research...");
          await trigger.click({ force: true });
          await page.waitForTimeout(2000);

          const deepOption = page.locator('.cdk-overlay-pane button.research-option-deep-research, .cdk-overlay-pane button:has-text("Deep Research"), .cdk-overlay-pane button:has-text("Nghiên cứu sâu")').filter({ visible: true }).first();
          if (await deepOption.isVisible()) {
            await deepOption.click({ force: true });
            await page.waitForTimeout(2000);
            console.log(`  ✅ Switched to Deep Research mode: "${await trigger.textContent()}"`);
          } else {
            console.log("  ⚠️ Could not find Deep Research button in overlay");
          }
        } else {
          console.log("  ✅ Already in Deep Research mode");
        }
      } else {
        console.log("  ⚠️ Trigger not visible, trying fallback to Add source button...");
        const addSourceBtn = page.locator('button:has-text("Thêm nguồn"), button:has-text("Add source")').filter({ visible: true }).first();
        if (await addSourceBtn.isVisible()) {
          await addSourceBtn.click({ force: true });
          await page.waitForTimeout(2000);
          const deepOption = page.locator('button.research-option-deep-research, button:has-text("Deep Research"), button:has-text("Nghiên cứu sâu")').filter({ visible: true }).first();
          if (await deepOption.isVisible()) {
            await deepOption.click({ force: true });
            await page.waitForTimeout(2000);
          }
        }
      }

      // 2. Type query into textarea
      const textarea = page.locator('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]').filter({ visible: true }).first();
      if (!(await textarea.isVisible())) {
        throw new Error("Textarea is not visible!");
      }

      const isDisabled = await textarea.isDisabled();
      if (isDisabled) {
        console.log("  ⚠️ Textarea is disabled! Retrying clear...");
        const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa")').filter({ visible: true }).first();
        if (await deleteBtn.isVisible()) {
          await deleteBtn.click({ force: true });
          await page.waitForTimeout(3000);
        }
        if (await textarea.isDisabled()) {
          throw new Error("Textarea remains disabled after clear attempt!");
        }
      }

      console.log("  ⌨️ Typing query...");
      await textarea.click({ force: true });
      await textarea.fill(query);
      await page.waitForTimeout(1000);

      // 3. Submit search
      console.log("  📤 Submitting search...");
      const submitBtn = page.locator('button.actions-enter-button, button[aria-label="Gửi"], button[aria-label="Submit"]').filter({ visible: true }).first();
      if (await submitBtn.isVisible() && !(await submitBtn.isDisabled())) {
        await submitBtn.click({ force: true });
      } else {
        await page.keyboard.press('Enter');
      }
      await page.waitForTimeout(6000);

      // 4. Wait for completion
      console.log("  ⏳ Waiting for Deep Research to complete (timeout: 10 minutes)...");
      const startTime = Date.now();
      const timeoutMs = 600000;
      let querySuccess = false;
      let progressLog = "";

      while (Date.now() - startTime < timeoutMs) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        
        // Precise checks for completion
        const isCompletedText = await page.locator('text="Đã hoàn tất Deep Research!", text="Deep Research completed!"').count() > 0;
        const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
        const isImportVisible = await importBtn.isVisible();
        
        // Progress indicators
        const hasProgress = await page.locator('mat-progress-bar, [role="progressbar"], mat-progress-spinner, [class*="spinner"]').count() > 0;
        const isRunningText = await page.locator('text="Đang phân tích kết quả...", text="Analyzing results..."').count() > 0;

        // Successful completion check:
        // We must see either the "Đã hoàn tất" message or the "Nhập" button,
        // and we MUST NOT see any progress bars or "Đang phân tích" texts.
        if ((isCompletedText || isImportVisible) && !hasProgress && !isRunningText) {
          console.log(`  ✅ Deep Research completed after ${elapsed}s! Clicking Import...`);
          
          if (isImportVisible) {
            await importBtn.click({ force: true });
            await page.waitForTimeout(10000); // Wait for import to complete
          }

          const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa")').filter({ visible: true }).first();
          if (await deleteBtn.isVisible()) {
            console.log("  🧹 Clearing completed search panel...");
            await deleteBtn.click({ force: true });
            await page.waitForTimeout(3000);
          }

          const newCount = await countSources();
          console.log(`  📊 Sources count updated: ${newCount} (added ${newCount - sourcesBefore} sources)`);
          sourcesBefore = newCount;
          querySuccess = true;
          break;
        }

        const status = (hasProgress || isRunningText) ? `Researching... (${elapsed}s)` : `Waiting... (${elapsed}s)`;
        if (status !== progressLog) {
          console.log(`    ${status}`);
          progressLog = status;
        }

        await page.waitForTimeout(5000);
      }

      if (!querySuccess) {
        throw new Error("Deep Research wait timed out!");
      }

      console.log(`  ✅ Query ${idx + 1} successfully completed!`);

    } catch (queryErr) {
      console.error(`  ❌ Error processing query ${idx + 1}:`, queryErr.message);
      try {
        await page.screenshot({ path: `/tmp/error_vinhomes_query_${idx+1}.png` });
        console.log(`  📸 Saved error screenshot to /tmp/error_vinhomes_query_${idx+1}.png`);
      } catch (screenshotErr) {
        console.error("  ⚠️ Failed to take error screenshot:", screenshotErr.message);
      }
    }
  }

  const finalSources = await countSources();
  console.log(`\n🎉 Deep Research bulk execution finished! Final sources count: ${finalSources}`);

  console.log("🔒 Closing context...");
  await context.close();
}

run().catch(err => {
  console.error("❌ Uncaught error in main runner:", err);
});
