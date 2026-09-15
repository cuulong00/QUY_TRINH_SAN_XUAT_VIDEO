import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const stateFile = '/Users/pro16/Library/Application Support/notebooklm-mcp/browser_state/state.json';
const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
const vaultDir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/pham-nhat-vuong-tinh-than-dan-toc/research_vault';
const outputResponsePath = '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/notebook_response.txt';
const notebookUrlPath = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/pham-nhat-vuong-tinh-than-dan-toc/.notebook_url';

async function run() {
  console.log('🚀 Checking auth state file...');
  if (!fs.existsSync(stateFile)) {
    throw new Error(`State file not found at ${stateFile}`);
  }

  console.log('🚀 Launching browser with authenticated profile:', userDataDir);
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: true,
    channel: 'chrome',
    viewport: { width: 1280, height: 800 }
  });

  const page = await browser.newPage();
  
  try {
    console.log('📌 Navigating to NotebookLM homepage...');
    await page.goto('https://notebooklm.google.com/', { waitUntil: 'networkidle', timeout: 45000 });
    await page.waitForTimeout(3000);

    // Save screenshot to verify we are logged in
    await page.screenshot({ path: '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/01_homepage.png' });
    console.log('📸 Saved homepage screenshot to check login');

    // Look for create button
    const createSelectors = [
      'button:has-text("Tạo mới")',
      'button:has-text("Tạo sổ ghi chú mới")',
      'button:has-text("Create")',
      'button:has-text("Créer")',
      'button:has-text("New notebook")',
      'button:has-text("Nouveau")',
      '[aria-label*="Create"]',
      '[aria-label*="Tạo"]',
      '.create-notebook-button',
      'button.mdc-button:has-text("Create")',
      'button:has(span:has-text("New notebook"))',
      'button:has-text("New")'
    ];

    let clicked = false;
    for (const selector of createSelectors) {
      try {
        const btn = page.locator(selector).first();
        if (await btn.isVisible({ timeout: 2000 })) {
          console.log(`✅ Clicking create button: ${selector}`);
          await btn.click();
          clicked = true;
          break;
        }
      } catch (e) {
        // Try next
      }
    }

    if (!clicked) {
      // Fallback: click any button with "+"
      const allButtons = await page.locator('button').all();
      for (const btn of allButtons) {
        const txt = await btn.textContent();
        if (txt && (txt.includes('Create') || txt.includes('New') || txt.includes('+'))) {
          console.log(`✅ Clicking fallback button: "${txt.trim()}"`);
          await btn.click();
          clicked = true;
          break;
        }
      }
    }

    if (!clicked) {
      throw new Error('Could not find Create notebook button on homepage.');
    }

    console.log('⏳ Waiting for notebook to be created...');
    const NOTEBOOK_UUID_URL = /notebooklm\.google\.com\/notebook\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/;
    await page.waitForURL(NOTEBOOK_UUID_URL, { timeout: 30000 });
    await page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(3000);

    const notebookUrl = page.url();
    console.log('🎉 Created brand new notebook:', notebookUrl);
    fs.writeFileSync(notebookUrlPath, notebookUrl);
    console.log(`💾 Saved notebook URL to ${notebookUrlPath}`);

    await page.screenshot({ path: '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/02_new_notebook.png' });

    // Upload the 9 source files from research_vault
    const files = fs.readdirSync(vaultDir).filter(f => f.endsWith('.md')).sort();
    console.log(`📁 Found ${files.length} markdown source files to upload.`);

    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const filePath = path.join(vaultDir, file);
      const content = fs.readFileSync(filePath, 'utf-8');
      const title = file.replace('.md', '').replace(/_/g, ' ');

      console.log(`📤 [${i+1}/${files.length}] Uploading source: "${title}" (${content.length} chars)`);

      // Click Add Source button
      const addSourceSelectors = [
        'button.add-source-button',
        'button[aria-label*="Add source" i]',
        'button[aria-label*="Thêm nguồn" i]',
        'button:has-text("Add source")',
        'button:has-text("Thêm nguồn")',
        'button.mat-fab',
        'button.mat-mini-fab',
        'button:has(mat-icon:has-text("add"))'
      ];

      let openedDialog = false;
      for (const sel of addSourceSelectors) {
        try {
          const btn = page.locator(sel).first();
          if (await btn.isVisible({ timeout: 1500 })) {
            await btn.click();
            openedDialog = true;
            break;
          }
        } catch (e) {}
      }

      if (!openedDialog) {
        // Try fallback: find any button with "add" or "+"
        const btns = await page.locator('button').all();
        for (const btn of btns) {
          const aria = await btn.getAttribute('aria-label');
          const txt = await btn.textContent();
          if ((aria && /add|source/i.test(aria)) || (txt && /add|source/i.test(txt))) {
            await btn.click();
            openedDialog = true;
            break;
          }
        }
      }

      if (!openedDialog) {
        await page.screenshot({ path: `/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/error_upload_${i}.png` });
        throw new Error(`Failed to click Add Source button for file: ${file}`);
      }

      await page.waitForTimeout(1000);

      // Click "Pasted text" option
      const pasteTextSelectors = [
        'span:has-text("Văn bản đã sao chép")',
        'button:has-text("Văn bản đã sao chép")',
        ':has-text("Văn bản đã sao chép")',
        'span:has-text("Văn bản sao chép")',
        'span:has-text("Văn bản đã dán")',
        'span:has-text("Pasted text")',
        'span:has-text("Paste text")',
        'span:has-text("Copier-coller du texte")',
        ':has-text("Văn bản sao chép")',
        ':has-text("Văn bản đã dán")',
        ':has-text("Pasted text")',
        ':has-text("Paste text")',
        '[data-type="text"]'
      ];

      let clickedPaste = false;
      for (const sel of pasteTextSelectors) {
        try {
          const btn = page.locator(sel).first();
          if (await btn.isVisible({ timeout: 1500 })) {
            await btn.click();
            clickedPaste = true;
            break;
          }
        } catch (e) {}
      }

      if (!clickedPaste) {
        // Fallback: look at elements with role="menuitem" or role="option"
        const items = await page.locator('[role="menuitem"], [role="option"], span').all();
        for (const item of items) {
          const txt = await item.textContent();
          if (txt && (txt.includes('Pasted text') || txt.includes('Paste text') || txt.includes('Copier-coller') || txt.includes('Văn bản sao chép') || txt.includes('Văn bản đã dán'))) {
            await item.click();
            clickedPaste = true;
            break;
          }
        }
      }

      if (!clickedPaste) {
        await page.screenshot({ path: `/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/error_paste_${i}.png` });
        throw new Error(`Failed to click Pasted Text option for file: ${file}`);
      }

      await page.waitForTimeout(1000);

      // Fill textarea with document content
      const textarea = page.locator('[role="dialog"] textarea, .mdc-dialog textarea, textarea:not(.query-box-input)').first();
      await textarea.fill(content);

      // Fill title
      const titleInput = page.locator('input[placeholder*="title" i], input[placeholder*="Title" i], input[placeholder*="name" i], [role="dialog"] input[type="text"]:not([readonly])').first();
      if (await titleInput.isVisible({ timeout: 1000 })) {
        await titleInput.fill(title);
      } else {
        console.log('⚠️ Title input not found, prepending title to content');
        await textarea.fill(`${title}\n\n${content}`);
      }

      await page.waitForTimeout(500);

      // Click Insert button
      const insertSelectors = [
        'button.mdc-button--raised:has-text("Chèn")',
        'button:has-text("Chèn")',
        'button.mdc-button--raised:has-text("Insert")',
        'button.mdc-button--raised:has-text("Thêm")',
        'button.mat-flat-button:has-text("Insert")',
        'button:has-text("Insert")',
        'button:has-text("Thêm")',
        'button:has-text("Save")',
        'button[type="submit"]',
        '[role="dialog"] button:not(:has-text("Cancel")):not(:has-text("Close"))'
      ];

      let clickedInsert = false;
      for (const sel of insertSelectors) {
        try {
          const btn = page.locator(sel).first();
          if (await btn.isVisible({ timeout: 1000 })) {
            await btn.click();
            clickedInsert = true;
            break;
          }
        } catch (e) {}
      }

      if (!clickedInsert) {
        throw new Error(`Failed to click Insert button for file: ${file}`);
      }

      console.log(`⏳ Waiting for source "${title}" to finish processing...`);
      await page.waitForTimeout(5000); // Wait for upload to complete
    }

    console.log('✅ All 9 sources uploaded successfully!');
    await page.screenshot({ path: '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/03_sources_uploaded.png' });

    // Ask the RAG query
    const query = `Dựa vào toàn bộ các tài liệu nguồn trong notebook, hãy phân tích chi tiết:
1. Bối cảnh thị trường bất động sản Việt Nam trong giai đoạn hiện nay (pháp lý, tín dụng, thanh khoản)?
2. Tại sao Vinhomes tuyên bố ngừng mở rộng quỹ đất? Bản chất thực sự của chiến lược này là gì?
3. Điều này có ý nghĩa gì đối với việc điều phối nguồn vốn của Vingroup cho các mảng khác như VinFast hay các dự án hạ tầng lớn?
Hãy trích xuất thông tin khách quan, chính xác nhất từ các tài liệu nguồn.`;

    console.log('💬 Querying NotebookLM...');
    const chatInputSelectors = [
      'textarea.query-box-input',
      'textarea[placeholder*="Đặt câu hỏi"]',
      'textarea[placeholder*="Ask"]',
      'textarea[placeholder*="Hỏi"]',
      'textarea:not(.query-box-textarea)'
    ];

    let queryInput = null;
    for (const sel of chatInputSelectors) {
      try {
        const el = page.locator(sel).first();
        if (await el.isVisible({ timeout: 2000 })) {
          queryInput = el;
          break;
        }
      } catch (e) {}
    }

    if (!queryInput) {
      throw new Error('Could not find chat input field.');
    }

    await queryInput.click();
    await queryInput.fill(query);
    await page.waitForTimeout(1000);
    
    const sendButton = page.locator('button.submit-button, button[aria-label="Gửi" i], button[aria-label="Send" i], button:has(mat-icon:has-text("arrow_forward"))').first();
    if (await sendButton.isVisible({ timeout: 2000 }) && !(await sendButton.isDisabled())) {
      await sendButton.click();
      console.log('✅ Clicked submit button');
    } else {
      await queryInput.press('Enter');
      console.log('✅ Sent query via Enter keypress');
    }
    console.log('⏳ Waiting for response...');

    const responseSelectors = ['.response-text', '.message-content', '[role="log"]'];
    let responseText = '';
    let lastResponse = '';
    let stableCount = 0;
    let attempts = 0;
    
    while (attempts < 120) {
      await page.waitForTimeout(1000);
      attempts++;
      
      let currentResponse = '';
      for (const sel of responseSelectors) {
        try {
          const responses = page.locator(sel);
          const count = await responses.count();
          if (count > 0) {
            currentResponse = await responses.nth(count - 1).innerText();
            if (currentResponse && currentResponse.length > 50) {
              break;
            }
          }
        } catch (e) {}
      }
      
      if (currentResponse) {
        currentResponse = currentResponse.trim();
        const lower = currentResponse.toLowerCase();
        const isLoading = lower.includes('đang tạo') || lower.includes('đang xử lý') || lower.includes('loading') || lower.includes('generating') || currentResponse.endsWith('...');
        
        if (currentResponse === lastResponse && !isLoading && currentResponse.length > 100) {
          stableCount++;
          if (stableCount >= 4) {
            console.log(`✅ Response stable! Length: ${currentResponse.length}`);
            responseText = currentResponse;
            break;
          }
        } else {
          stableCount = 0;
          lastResponse = currentResponse;
          if (isLoading) {
            console.log(`⏳ Response is still generating...`);
          } else {
            console.log(`⏳ Response text updated: ${currentResponse.length} chars...`);
          }
        }
      } else {
        console.log('⏳ Waiting for response element to appear...');
      }
    }

    if (responseText) {
      fs.writeFileSync(outputResponsePath, responseText);
      console.log(`🎉 Got response and saved to ${outputResponsePath}!`);
      console.log('\n--- RESPONSE PREVIEW ---');
      console.log(responseText.slice(0, 1000) + '...\n------------------------');
    } else {
      console.log('❌ Could not extract response text. Saving HTML source for debugging...');
      const html = await page.content();
      fs.writeFileSync('/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/error_rag.html', html);
      await page.screenshot({ path: '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/error_rag.png' });
    }

  } finally {
    await browser.close();
    console.log('🔌 Browser closed.');
  }
}

run().catch(e => {
  console.error('❌ Script failed:', e);
  process.exit(1);
});
