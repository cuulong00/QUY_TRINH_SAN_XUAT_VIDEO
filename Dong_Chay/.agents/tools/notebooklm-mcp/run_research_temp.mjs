import { chromium } from 'patchright';
import fs from 'fs';

const notebookUrl = "https://notebooklm.google.com/notebook/f6461b05-ea1d-4023-946e-3e3aa40c7323";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const queries = [
  "Báo cáo tài chính, nợ nần, tái cơ cấu Công ty Luyện kim Việt Trung VTM và mỏ sắt Quý Xa Lào Cai mới nhất 2025 2026",
  "Cơ chế BT Luật Thủ đô 2024 dự án Trục đại lộ cảnh quan sông Hồng Hà Nội liên danh Đại Quang Minh Thaco Hòa Phát",
  "Sai phạm hình sự, khởi tố C03 Bộ Công an tại mỏ sắt Quý Xa và Công ty Luyện kim Việt Trung VTM Lào Cai",
  "CBAM EU carbon tax steel export Vietnam Hoa Phat green steel transition mitigation strategy",
  "Japanese Keiretsu industrial group role in Shinkansen high speed rail development history Mitsubishi Sumitomo",
  "Korean Chaebol role in Gyeongbu expressway infrastructure development Park Chung-hee Hyundai"
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
    const errorScr = `/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch/error_query_${index}.png`;
    fs.mkdirSync('/Users/pro16/Documents/VideoProject/Dòng Chảy/scratch', { recursive: true });
    await page.screenshot({ path: errorScr });
  }

  await context.close();
}

async function main() {
  console.log("🧹 Initializing bulk deep research script...");
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
