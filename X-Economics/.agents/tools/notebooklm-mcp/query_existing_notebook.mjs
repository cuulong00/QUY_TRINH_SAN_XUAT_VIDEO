import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
const notebookUrl = 'https://notebooklm.google.com/notebook/292d93b8-7919-4f00-9d83-8e98c49046c2';
const outputResponsePath = '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/notebook_response.txt';

async function run() {
  console.log('🚀 Launching browser with authenticated profile:', userDataDir);
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: true,
    channel: 'chrome',
    viewport: { width: 1280, height: 800 }
  });

  const page = await browser.newPage();
  
  try {
    console.log(`📌 Navigating directly to notebook: ${notebookUrl}`);
    await page.goto(notebookUrl, { waitUntil: 'networkidle', timeout: 45000 });
    await page.waitForTimeout(3000);

    console.log('⏳ Waiting for notebook data to load...');
    let loaded = false;
    let loadAttempts = 0;
    while (loadAttempts < 30) {
      await page.waitForTimeout(1000);
      loadAttempts++;
      
      const pageTitleElement = page.locator('h2.cover-title, [class*="title"]').first();
      const pageTitle = (await pageTitleElement.isVisible()) ? await pageTitleElement.textContent() : '';
      
      if (pageTitle && !pageTitle.includes('Loading') && !pageTitle.includes('Đang tải')) {
        const sourceCountElement = page.locator('.cover-subtitle-source-count, [class*="source-count"]').first();
        if (await sourceCountElement.isVisible()) {
          const txt = await sourceCountElement.textContent();
          console.log(`  Detected source count: "${txt?.trim()}"`);
          if (txt && (txt.includes('nguồn') || txt.includes('source') || txt.includes('1') || txt.includes('2') || txt.includes('3') || txt.includes('4') || txt.includes('5') || txt.includes('6') || txt.includes('7') || txt.includes('8') || txt.includes('9'))) {
            console.log('✅ Notebook is fully loaded with sources!');
            loaded = true;
            break;
          }
        }
      }
    }
    
    if (!loaded) {
      console.log('⚠️ Warning: Notebook did not load fully in 30 seconds. Proceeding anyway...');
    }

    // Save screenshot to verify we loaded it correctly
    await page.screenshot({ path: '/Users/pro16/.gemini/antigravity/brain/e82f82ec-8ed3-421e-a57f-1371db35dcc8/scratch/04_notebook_loaded.png' });
    console.log('📸 Saved loaded notebook screenshot');

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

    // Click submit button
    const sendButton = page.locator('button.submit-button, button[aria-label="Gửi" i], button[aria-label="Send" i], button:has(mat-icon:has-text("arrow_forward"))').first();
    if (await sendButton.isVisible({ timeout: 2000 }) && !(await sendButton.isDisabled())) {
      await sendButton.click();
      console.log('✅ Clicked submit button');
    } else {
      await queryInput.press('Enter');
      console.log('✅ Sent query via Enter keypress');
    }
    console.log('⏳ Waiting for response stability...');

    // Poll for response stability
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
