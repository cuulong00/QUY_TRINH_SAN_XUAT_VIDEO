import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/eff2b2e7-4c41-4b26-a863-ce8b664775ee";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const queries = [
  "kinh tế phi chính thức lao động tự do vỉa hè Việt Nam bộ giảm chấn xã hội tỷ lệ thất nghiệp",
  "mục tiêu du lịch TP.HCM 2026 doanh thu 12.5 tỷ USD 11 triệu khách quốc tế kinh tế ban đêm",
  "Nghị định 165/2024/NĐ-CP Quyết định 2828/QĐ-UBND bãi bỏ Quyết định 32/2023/QĐ-UBND vỉa hè lòng đường",
  "street food Vietnam plastic stools tourist experience review netnography",
  "economic leakage du lịch Việt Nam rò rỉ kinh tế chuỗi cung ứng nông sản vỉa hè",
  "Singapore hawker centers history street food relocation tourist attraction Chinatown"
];

async function runQuery(query, index) {
  console.log(`\n========================================`);
  console.log(`🚀 [${index + 1}/${queries.length}] Query: "${query}"`);
  console.log(`========================================`);

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
  await page.waitForTimeout(10000);

  // Close any overlay dialog
  const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').first();
  if (await closeBtn.isVisible()) {
    console.log("⚠️ Found Add Sources dialog. Clicking close...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(3000);
  }

  // Check if Import button is already there from a failed run
  const initialImportBtn = page.locator('button.source-discovery-completed-action-import-button').first();
  if (await initialImportBtn.isVisible()) {
    console.log("✅ Found pre-existing Import button! Clicking it first...");
    await initialImportBtn.click({ force: true });
    await page.waitForTimeout(10000);
    const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button').first();
    if (await deleteBtn.isVisible()) {
      await deleteBtn.click({ force: true });
      await page.waitForTimeout(2000);
    }
  }

  // Switch to Deep Research mode
  console.log("🔄 Switching to Deep Research mode...");
  const trigger = page.locator('button.corpus-select.researcher-menu-trigger, button.corpus-select:has-text("Nghiên cứu nhanh"), button.corpus-select:has-text("Nghiên cứu sâu"), button.corpus-select:has-text("Deep Research")').first();
  if (await trigger.isVisible()) {
    const text = await trigger.textContent();
    if (!text.includes('Deep Research') && !text.includes('Nghiên cứu sâu')) {
      await trigger.click({ force: true });
      await page.waitForTimeout(2000);
      const deepBtn = page.locator('.cdk-overlay-pane button.research-option-deep-research, .cdk-overlay-pane button:has-text("Deep Research"), .cdk-overlay-pane button:has-text("Nghiên cứu sâu")').first();
      if (await deepBtn.isVisible()) {
        await deepBtn.click({ force: true });
        await page.waitForTimeout(3000);
      }
    } else {
      console.log("✅ Already in Deep Research mode.");
    }
  } else {
    console.log("⚠️ Trigger button not visible, trying fallback Add Source method...");
    const addSourceBtn = page.locator('button:has-text("Thêm nguồn"), button:has-text("Add source")').first();
    if (await addSourceBtn.isVisible()) {
      await addSourceBtn.click({ force: true });
      await page.waitForTimeout(2000);
      const deepOption = page.locator('button.research-option-deep-research, button:has-text("Deep Research"), button:has-text("Nghiên cứu sâu")').first();
      if (await deepOption.isVisible()) {
        await deepOption.click({ force: true });
        await page.waitForTimeout(3000);
      }
    }
  }

  // Find textarea and type query
  console.log("⌨️ Finding textarea...");
  const textarea = page.locator('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]').first();
  if (!(await textarea.isVisible())) {
    throw new Error("Could not find Deep Research textarea");
  }

  await textarea.click({ force: true });
  await textarea.fill(query);
  await page.waitForTimeout(1000);
  
  // Submit search
  console.log("📤 Submitting search...");
  await page.keyboard.press('Enter');
  await page.waitForTimeout(5000);

  // Poll for completion (max 10 minutes)
  console.log("⏳ Waiting for research to complete...");
  const startTime = Date.now();
  const timeoutMs = 600000; // 10 minutes
  let completed = false;

  while (Date.now() - startTime < timeoutMs) {
    const elapsed = Math.round((Date.now() - startTime) / 1000);
    
    // Check if Import button is visible
    const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').first();
    const isImportVisible = await importBtn.isVisible();

    // Check for progress indicator
    let hasProgress = false;
    for (const sel of ['mat-progress-bar', '[role="progressbar"]', 'mat-progress-spinner']) {
      if (await page.locator(sel).first().isVisible()) {
        hasProgress = true;
        break;
      }
    }

    if (isImportVisible && !hasProgress) {
      console.log(`\n✅ Research completed in ${elapsed}s! Clicking Import...`);
      await importBtn.click({ force: true });
      console.log("⏳ Waiting 15 seconds for import to process...");
      await page.waitForTimeout(15000);
      
      const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').first();
      if (await deleteBtn.isVisible()) {
        console.log("🧹 Clearing completed search panel...");
        await deleteBtn.click({ force: true });
        await page.waitForTimeout(3000);
      }
      
      completed = true;
      break;
    }

    process.stdout.write(`\r⏳ Researching... (${elapsed}s elapsed)`);
    await page.waitForTimeout(5000);
  }

  if (!completed) {
    console.log(`\n❌ Query timed out or failed to complete after 10 minutes.`);
    await page.screenshot({ path: `/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/error_query_${index}.png` });
  }

  await context.close();
}

async function main() {
  // First, ensure all headless chromium processes are killed to release profiles
  console.log("🧹 Killing existing headless shell processes...");
  // We already ran killall headless_shell, but let's run it just in case
  
  for (let i = 0; i < queries.length; i++) {
    try {
      await runQuery(queries[i], i);
      console.log(`⏳ Waiting 5 seconds before next query...`);
      await new Promise(resolve => setTimeout(resolve, 5000));
    } catch (err) {
      console.error(`❌ Error running query ${i + 1}:`, err);
    }
  }
  console.log("\n🏁 All queries processed.");
}

main().catch(console.error);
