import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const notebookUrl = "https://notebooklm.google.com/notebook/f6296b14-a456-47e9-b24a-a5a2b3a7dc9b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const statePaths = [
  "/Users/pro16/Library/Application Support/notebooklm-mcp/accounts/default/browser_state/state.json",
  "/Users/pro16/Library/Application Support/notebooklm-mcp/accounts/default/state.json",
  "/Users/pro16/Library/Application Support/notebooklm-mcp/browser_state/state.json"
];

const sourcePath = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vingroup-van-cuoc-dia-chinh-tri/research_vault/009-vingroup-dinh-huong-doanh-nghiep-kien-tao-dhdcd-2026.md";

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

async function run() {
  console.log("🚀 Launching Chrome in headless mode...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-sandbox',
    ]
  });

  // Inject cookies from the first existing state.json
  let injected = false;
  for (const statePath of statePaths) {
    if (fs.existsSync(statePath)) {
      try {
        const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));
        if (state && Array.isArray(state.cookies) && state.cookies.length > 0) {
          await context.addCookies(state.cookies);
          console.log(`✅ Manually injected ${state.cookies.length} cookies from: ${statePath}`);
          injected = true;
          break;
        }
      } catch (err) {
        console.warn(`⚠️ Failed to inject cookies from ${statePath}: ${err}`);
      }
    }
  }

  if (!injected) {
    console.warn("⚠️ No valid state.json found to inject cookies!");
  }

  const page = await context.newPage();
  console.log(`🌐 Navigating to: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(10000); // Wait for initial load

  // Read the markdown source content
  const sourceContent = fs.readFileSync(sourcePath, 'utf-8');
  
  // Upload to NotebookLM
  await addTextSource(page, "Vingroup doanh nghiep kien tao DHDCD 2026", sourceContent);

  // Find chat textarea to ask question
  const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
  if (!(await chatInput.isVisible())) {
    console.error("❌ Chat input not found!");
    await context.close();
    return;
  }

  const question = "Trong các tài liệu nguồn của notebook này, đặc biệt là nguồn tài liệu mới ĐHĐCĐ 2026, Vingroup tuyên bố chuyển dịch sang doanh nghiệp kiến tạo thế nào? Định nghĩa kiến tạo và các trụ cột đi kèm là gì? Trích xuất cụ thể từng điểm.";
  console.log(`⌨️ Typing question: "${question}"`);
  await chatInput.click();
  await chatInput.fill(question);
  await page.waitForTimeout(1000);

  console.log("📤 Submitting question...");
  await page.keyboard.press('Enter');
  await page.waitForTimeout(5000); // Wait for response to start

  console.log("⏳ Waiting for response...");
  let lastText = "";
  let stableCount = 0;
  for (let i = 0; i < 30; i++) {
    const responses = page.locator('.chat-response, .response-bubble, .message-content, chat-response, .markdown-content');
    const count = await responses.count();
    let currentText = "";
    if (count > 0) {
      currentText = await responses.last().innerText();
    }
    
    console.log(`  [${i}] Text length: ${currentText.length}`);
    if (currentText.length > 0 && currentText === lastText) {
      stableCount++;
      if (stableCount >= 3) {
        console.log("✅ Response stabilized!");
        break;
      }
    } else {
      stableCount = 0;
      lastText = currentText;
    }
    await page.waitForTimeout(3000);
  }

  console.log("\n======================================\nRESPONSE:\n");
  console.log(lastText);
  console.log("\n======================================\n");

  if (lastText && !lastText.includes("không thể trả lời")) {
    const outputDoc = `# BÁO CÁO NGHIÊN CỨU VÀ TỔNG HỢP NOTEBOOKLM: ĐỊNH HƯỚNG "DOANH NGHIỆP KIẾN TẠO" CỦA VINGROUP TẠI ĐHĐCĐ 2026\n\n*Được trích xuất trực tiếp bằng NotebookLM vào ngày 18/07/2026*\n\n## Kết quả phân tích từ NotebookLM:\n\n${lastText}\n`;
    fs.writeFileSync(sourcePath, outputDoc);
    console.log(`✅ Updated research document with NotebookLM output: ${sourcePath}`);
  } else {
    console.warn("⚠️ NotebookLM returned an empty or invalid response. Check state.");
  }
  
  await context.close();
}

run().catch(err => console.error(err));
