import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

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
  
  const q = {
    id: '014',
    slug: 'vfs_india_-014-strategic-analysis',
    question: "Phân tích các nước đi chiến lược chủ động của Vingroup và VinFast tại Ấn Độ và Indonesia: Mục tiêu tối thượng của các cuộc viễn chinh này là gì? Mối liên hệ chặt chẽ giữa việc tái cấu trúc tài chính mảng sản xuất nội địa (chuyển nợ 182.000 tỷ sang Công ty Tương Lai, chuyển sang mô hình Asset-Light OEM) và canh bạc bành trướng quốc tế này là gì? Đâu là mục đích cao cả đứng sau (ví dụ: giải cứu dòng tiền, đa dạng hóa rủi ro địa chính trị, xây dựng hộ chiếu xuất khẩu lách rào cản quốc tế, tìm kiếm định giá lành mạnh hơn trên NASDAQ)? Trình bày phân tích sâu sắc bằng tiếng Việt để phục vụ viết kịch bản phân tích vĩ mô.",
    title: "Phân tích Chiến lược Viễn chinh Vĩ mô của VinFast: Nước đi chủ động và Mục đích cao cả đứng sau cuộc tái cấu trúc tài chính"
  };
  
  const vaultDir = '/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/vinfast-an-do/research_vault';
  const mdPath = path.join(vaultDir, `${q.slug}.md`);
  const jsonPath = path.join(vaultDir, `${q.slug}.json`);
  
  // Locate the chat textarea
  console.log('Locating chat input textarea...');
  const textarea = page.locator('chat-panel textarea.query-box-input, textarea[placeholder="Đặt câu hỏi hoặc tạo nội dung"]').first();
  await textarea.waitFor({ timeout: 10000 });
  
  // Type query
  console.log('Typing query...');
  await textarea.click({ force: true });
  await textarea.focus();
  
  // Select all and delete
  await page.keyboard.down('Meta');
  await page.keyboard.press('a');
  await page.keyboard.up('Meta');
  await page.keyboard.press('Backspace');
  await delay(500);
  
  // Type query
  await page.keyboard.type(q.question, { delay: 2 });
  await delay(1000);
  
  // Locate submit button
  console.log('Locating submit button...');
  const submitBtn = page.locator('chat-panel button.submit-button, chat-panel button[aria-label="Gửi"]').first();
  await submitBtn.waitFor({ timeout: 5000 });
  
  const isEnabled = await submitBtn.isEnabled();
  if (!isEnabled) {
    console.log('Submit button is disabled. Trying page.keyboard.press("Enter")...');
    await textarea.focus();
    await page.keyboard.press('Enter');
  } else {
    console.log('Clicking submit button...');
    await submitBtn.click();
  }
  
  console.log('Submitted! Monitoring generation progress...');
  
  // Monitor response generation
  let lastLength = 0;
  let stableCount = 0;
  let responseText = '';
  
  for (let j = 0; j < 60; j++) {
    await delay(3000);
    
    const messages = await page.evaluate(() => {
      const msgs = Array.from(document.querySelectorAll('chat-message'));
      return msgs.map(m => {
        const isToUser = m.querySelector('.to-user-container') !== null;
        return { isToUser, text: m.innerText };
      });
    });
    
    if (messages.length === 0) {
      console.log('No messages found in DOM...');
      continue;
    }
    
    const lastMsg = messages[messages.length - 1];
    if (!lastMsg.isToUser) {
      console.log('Last message in DOM is still user query, waiting...');
      continue;
    }
    
    const currentLength = lastMsg.text.length;
    console.log(`[${(j + 1) * 3}s] Last message length: ${currentLength}`);
    
    if (currentLength > 0 && currentLength === lastLength) {
      stableCount++;
      if (stableCount >= 4) {
        console.log('Response length has stabilized. Generation complete!');
        responseText = lastMsg.text;
        break;
      }
    } else {
      stableCount = 0;
      lastLength = currentLength;
    }
  }
  
  if (!responseText) {
    console.error('Timeout waiting for response. Fetching whatever is available...');
    responseText = await page.evaluate(() => {
      const msgs = Array.from(document.querySelectorAll('chat-message'));
      const lastMsg = msgs[msgs.length - 1];
      return lastMsg ? lastMsg.innerText : '';
    });
  }
  
  console.log('Saving files...');
  const timestamp = new Date().toISOString();
  const sessionId = Math.random().toString(36).substring(2, 10);
  
  // Create markdown output
  const mdContent = `---
title: "${q.title}"
type: nblm-answer
asked_at: ${timestamp}
notebook_url: "https://notebooklm.google.com/notebook/${notebookId}"
session_id: "${sessionId}"
citations_count: 0
sources: []
---

# ${q.title}

> Asked on ${timestamp} against [NotebookLM notebook](https://notebooklm.google.com/notebook/${notebookId})

## Answer

${responseText}
`;
  
  fs.writeFileSync(mdPath, mdContent);
  console.log(`Saved markdown: ${mdPath}`);
  
  // Create JSON output
  const jsonContent = {
    "$schema": "https://schemas.roomi-fields.com/nblm-answer-v1.json",
    "type": "nblm-answer",
    "version": "1.0",
    "asked_at": timestamp,
    "session_id": sessionId,
    "notebook": {
      "id": notebookId,
      "name": "VinFast India",
      "url": `https://notebooklm.google.com/notebook/${notebookId}`
    },
    "question": q.question,
    "answer": {
      "text": responseText,
      "format": "markdown"
    },
    "citations": [],
    "metadata": {
      "tags": [],
      "extraction_success": true,
      "citations_count": 0,
      "source_names": []
    }
  };
  
  fs.writeFileSync(jsonPath, JSON.stringify(jsonContent, null, 2));
  console.log(`Saved JSON: ${jsonPath}`);
  
  try {
    await page.screenshot({ path: `/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/extraction_progress_${q.id}.png` });
  } catch {}
  
  await browser.close();
  console.log('\nStrategy analysis extraction complete!');
}

main().catch(console.error);
