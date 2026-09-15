import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const notebookUrl = "https://notebooklm.google.com/notebook/f6461b05-ea1d-4023-946e-3e3aa40c7323";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const scratchFiles = [
  { path: "/Users/pro16/.gemini/antigravity/brain/46445cce-f268-42d9-a5b0-2e7dc861e9a8/scratch/cafef_clean.txt", title: "CafeF - Sieu Lien Minh 3 Chu Tich Ho Tran" },
  { path: "/Users/pro16/.gemini/antigravity/brain/46445cce-f268-42d9-a5b0-2e7dc861e9a8/scratch/vtm_laocai_gov_clean.txt", title: "Cong Thong Tin Lao Cai - Du An VTM" },
  { path: "/Users/pro16/.gemini/antigravity/brain/46445cce-f268-42d9-a5b0-2e7dc861e9a8/scratch/kvs_project_clean.txt", title: "KVS Group - Du An Golf va Bieu Do Cong Ty" },
  { path: "/Users/pro16/.gemini/antigravity/brain/46445cce-f268-42d9-a5b0-2e7dc861e9a8/scratch/song_hau_wind_clean.txt", title: "Dien Gio Song Hau - Co Cau Co Dong va Giay Phep" },
  { path: "/Users/pro16/.gemini/antigravity/brain/46445cce-f268-42d9-a5b0-2e7dc861e9a8/scratch/c03_vtm_prosecution.txt", title: "Bo Cong An - Khoi To 24 Bi Can Dai An VTM Quoc Gia" }
];

const queries = [
  "Báo cáo tài chính, nợ nần, tái cơ cấu Công ty Luyện kim Việt Trung VTM và mỏ sắt Quý Xa Lào Cai mới nhất 2025 2026",
  "Cơ chế BT Luật Thủ đô 2024 dự án Trục đại lộ cảnh quan sông Hồng Hà Nội liên danh Đại Quang Minh Thaco Hòa Phát",
  "Sai phạm hình sự, khởi tố C03 Bộ Công an tại mỏ sắt Quý Xa và Công ty Luyện kim Việt Trung VTM Lào Cai",
  "CBAM EU carbon tax steel export Vietnam Hoa Phat green steel transition mitigation strategy",
  "Japanese Keiretsu industrial group role in Shinkansen high speed rail development history Mitsubishi Sumitomo",
  "Korean Chaebol role in Gyeongbu expressway infrastructure development Park Chung-hee Hyundai"
];

async function addTextSource(page, fileTitle, fileContent) {
  console.log(`\n📄 Importing Text Source: "${fileTitle}"...`);
  
  // Close any pre-existing dialog first to start clean
  const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').first();
  if (await closeBtn.isVisible()) {
    console.log("🧹 Closing existing dialog to start fresh...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(2000);
  }

  // Click Add Source button
  console.log("👉 Clicking Add Source button...");
  const addSourceBtn = page.locator('button:has-text("Thêm nguồn"), button:has-text("Add source"), button[aria-label*="Add source" i]').first();
  await addSourceBtn.click({ force: true });
  await page.waitForTimeout(3000);

  // Click Copied Text option
  console.log("👉 Clicking Copied Text option...");
  const copiedTextBtn = page.locator('button:has-text("Văn bản đã sao chép"), button:has-text("Copied text"), mat-icon:has-text("content_paste")').first();
  await copiedTextBtn.click({ force: true });
  await page.waitForTimeout(3000);

  // Use evaluate to fill title
  console.log("👉 Typing title...");
  await page.evaluate((title) => {
    const titleInput = document.querySelector('input[placeholder*="Tiêu đề" i], input[placeholder*="Title" i], input[aria-label*="title" i]');
    if (titleInput) {
      titleInput.value = title;
      titleInput.dispatchEvent(new Event('input', { bubbles: true }));
      titleInput.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, fileTitle);

  // Use evaluate to fill content
  console.log("👉 Typing content...");
  await page.evaluate((content) => {
    const contentTextarea = document.querySelector('textarea[placeholder*="Dán văn bản" i], textarea[placeholder*="Paste text" i], textarea[aria-label*="text" i], mat-dialog-content textarea');
    if (contentTextarea) {
      contentTextarea.value = content;
      contentTextarea.dispatchEvent(new Event('input', { bubbles: true }));
      contentTextarea.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }, fileContent);

  await page.waitForTimeout(2000);

  // Click Insert/Add button
  console.log("👉 Clicking Insert button...");
  const insertBtn = page.locator('button:has-text("Thêm"), button:has-text("Insert"), button:has-text("Add"), button.mat-accent, button.mat-primary').filter({ visible: true }).first();
  await insertBtn.click({ force: true });
  
  console.log("⏳ Waiting for import to finish...");
  await page.waitForTimeout(10000);

  // Close the dialog after successful import
  if (await closeBtn.isVisible()) {
    console.log("🧹 Closing dialog after import...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(2000);
  }
}

async function runDeepResearch(page, query, index) {
  console.log(`\n========================================`);
  console.log(`🚀 [${index + 1}/${queries.length}] Deep Research Query: "${query}"`);
  console.log(`========================================`);

  // Close any overlay dialog
  const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').first();
  if (await closeBtn.isVisible()) {
    console.log("⚠️ Found Add Sources dialog. Clicking close...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(2000);
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

  // Find textarea and type query using evaluate
  console.log("⌨️ Filling query via evaluate...");
  const textFilled = await page.evaluate((q) => {
    const textarea = document.querySelector('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]');
    if (textarea) {
      textarea.value = q;
      textarea.dispatchEvent(new Event('input', { bubbles: true }));
      textarea.dispatchEvent(new Event('change', { bubbles: true }));
      return true;
    }
    return false;
  }, query);

  if (!textFilled) {
    throw new Error("Could not find Deep Research textarea in DOM");
  }

  await page.waitForTimeout(2000);
  
  // Submit search by clicking the send button (circle blue button with arrow)
  console.log("📤 Submitting search by clicking send button...");
  const sendBtn = page.locator('button.actions-enter-button, button[aria-label="Gửi"], button[aria-label="Send"], button:has(mat-icon:has-text("search")), button:has(mat-icon:has-text("arrow_forward")), button.actions-enter-button:has-text("search")').first();
  if (await sendBtn.isVisible()) {
    console.log("👉 Found send button, clicking...");
    await sendBtn.click({ force: true });
  } else {
    console.log("⚠️ Send button not found, falling back to Enter key...");
    await page.keyboard.press('Enter');
  }
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
}

async function main() {
  console.log("🧹 Launching Chromium with persistent context...");
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
  console.log(`🌐 Navigating to Notebook URL: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(12000);

  // Close any overlay dialog first
  let closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').first();
  if (await closeBtn.isVisible()) {
    console.log("⚠️ Found Add Sources dialog. Clicking close...");
    await closeBtn.click({ force: true });
    await page.waitForTimeout(3000);
  }

  // Step 1: Import 5 scratch files
  console.log("\n--- STEP 1: IMPORT SCRATCH TEXT SOURCES ---");
  for (const fileObj of scratchFiles) {
    try {
      if (fs.existsSync(fileObj.path)) {
        const content = fs.readFileSync(fileObj.path, 'utf8');
        await addTextSource(page, fileObj.title, content);
      } else {
        console.warn(`⚠️ Scratch file not found: ${fileObj.path}`);
      }
    } catch (err) {
      console.error(`❌ Error importing scratch file "${fileObj.title}":`, err);
    }
  }

  // Step 2: Run 6 Deep Research Queries
  console.log("\n--- STEP 2: EXECUTE DEEP RESEARCH QUERIES ---");
  for (let i = 0; i < queries.length; i++) {
    try {
      await runDeepResearch(page, queries[i], i);
      console.log(`⏳ Waiting 5 seconds before next query...`);
      await page.waitForTimeout(5000);
    } catch (err) {
      console.error(`❌ Error running query ${i + 1}:`, err);
    }
  }

  console.log("\n🏁 All imports and research queries processed successfully!");
  await context.close();
}

main().catch(console.error);
