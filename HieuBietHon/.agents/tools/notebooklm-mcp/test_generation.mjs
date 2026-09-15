import { chromium } from 'patchright';
import fs from 'fs';

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function main() {
  console.log('Connecting to Chrome via CDP...');
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  console.log('Connected!');
  
  const notebookId = '9891a2f0-8e48-445a-a2c4-4b25ee3c3800';
  let page;
  
  for (const ctx of browser.contexts()) {
    const found = ctx.pages().find(p => p.url().includes(notebookId));
    if (found) {
      page = found;
      break;
    }
  }
  
  if (!page) {
    console.error('Page not found!');
    await browser.close();
    return;
  }
  
  console.log('Page found. Bringing to front...');
  await page.bringToFront();
  
  // Locate the chat textarea
  console.log('Locating chat input textarea...');
  const textarea = page.locator('textarea[placeholder="Đặt câu hỏi hoặc tạo nội dung"], textarea.query-box-input').first();
  await textarea.waitFor({ timeout: 5000 });
  
  const query = "Gensol and BluSmart scandal: Jaggi brothers SEBI ban in April 2025, ED asset attachment in January 2026, diversion of ₹262 crore, BluSmart's 7500 EV fleet grounding. Hãy trích xuất chi tiết số liệu, ngày tháng, các mốc thời gian và cơ chế pháp lý/tài chính liên quan để phục vụ viết kịch bản.";
  console.log('Typing query...');
  await textarea.click({ force: true });
  await textarea.focus();
  // Clear existing content
  await page.keyboard.down('Meta');
  await page.keyboard.press('a');
  await page.keyboard.up('Meta');
  await page.keyboard.press('Backspace');
  await delay(500);
  
  // Type query character by character
  await page.keyboard.type(query, { delay: 5 });
  await delay(1000);
  
  // Click submit button
  console.log('Locating submit button...');
  const submitBtn = page.locator('button.submit-button, button[aria-label="Gửi"]').first();
  await submitBtn.waitFor({ timeout: 5000 });
  
  console.log('Clicking submit button...');
  await submitBtn.click();
  console.log('Submitted! Monitoring generation...');
  
  // Monitor the last message's text content length
  let lastLength = 0;
  let stableCount = 0;
  
  for (let i = 0; i < 40; i++) { // Check for up to 120 seconds (40 * 3s)
    await delay(3000);
    
    const messages = await page.evaluate(() => {
      const msgs = Array.from(document.querySelectorAll('chat-message'));
      return msgs.map(m => m.innerText);
    });
    
    if (messages.length === 0) {
      console.log('No messages found in DOM...');
      continue;
    }
    
    const lastMsg = messages[messages.length - 1];
    const currentLength = lastMsg.length;
    
    console.log(`[${i * 3}s] Messages count: ${messages.length}, Last message length: ${currentLength}`);
    
    if (currentLength > 0 && currentLength === lastLength) {
      stableCount++;
      if (stableCount >= 4) { // Stable for 12 seconds
        console.log('Response length has stabilized. Generation complete!');
        break;
      }
    } else {
      stableCount = 0;
      lastLength = currentLength;
    }
  }
  
  // Save screenshot
  const screenshotPath = '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/after_first_query_submit.png';
  await page.screenshot({ path: screenshotPath });
  console.log('Saved screenshot to:', screenshotPath);
  
  // Fetch and save the last message content
  const lastMessageContent = await page.evaluate(() => {
    const msgs = Array.from(document.querySelectorAll('chat-message'));
    if (msgs.length === 0) return '';
    const lastMsg = msgs[msgs.length - 1];
    // Check if it is indeed from the model
    const isToUser = lastMsg.querySelector('.to-user-container') !== null;
    return isToUser ? lastMsg.innerText : 'ERROR: Last message is not from model';
  });
  
  console.log('Last message preview (first 200 chars):');
  console.log(lastMessageContent.substring(0, 200));
  
  await browser.close();
}

main().catch(console.error);
