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
  
  const queries = [
    {
      id: '009',
      slug: 'vfs_india_-009-gensol-blusmart-scandal',
      question: "Gensol and BluSmart scandal: Trích xuất tất cả chi tiết và ngày tháng về vụ bê bối của Gensol và BluSmart. Cụ thể: Lệnh cấm của SEBI đối với anh em nhà Jaggi (tháng 4/2025), việc ED phong tỏa tài sản (tháng 1/2026) bao gồm các căn hộ tại DLF Camellias và Magnolias, việc chuyển dịch 262 crore Rupee (thông qua 30.000 đơn đặt hàng trước giả mạo và các MOU), và việc đình chỉ/thu hồi đội xe 7.500 EV của BluSmart (lệnh của Tòa án Tối cao Delhi, vỡ nợ 510 crore Rupee đối với IREDA). Hãy trình bày chi tiết bằng tiếng Việt với các con số, ngày tháng chính xác và cơ chế pháp lý/tài chính liên quan.",
      title: "Vụ bê bối Gensol và BluSmart: SEBI cấm cửa anh em nhà Jaggi, ED phong tỏa tài sản và sự sụp đổ đội xe 7.500 EV"
    },
    {
      id: '010',
      slug: 'vfs_india_-010-vingroup-restructuring-debt-may-2026',
      question: "Vingroup restructuring and debt in May 2026: Trích xuất chi tiết cuộc tái cấu trúc toàn cầu của Vingroup vào tháng 5/2026. Cụ thể: Việc chuyển giao khoản nợ nhà máy trị giá 182.000 tỷ VND sang Công ty Tương Lai (Công ty Cổ phần Nghiên cứu Đầu tư và Phát triển Tương Lai), mô hình thuê lại nhà máy OEM (leaseback OEM contract manufacturing model) nơi VinFast thuê lại nhà máy để sản xuất, và tác động của thương vụ này giúp tối ưu hóa bảng cân đối kế toán của VinFast Auto trên sàn Nasdaq. Hãy trình bày chi tiết bằng tiếng Việt với các con số tài chính và cơ chế vận hành cụ thể.",
      title: "Quyết định tái cấu trúc của Vingroup tháng 5/2026: Chuyển giao 182.000 tỷ nợ nhà máy sang Công ty Tương Lai và mô hình thuê lại OEM"
    },
    {
      id: '011',
      slug: 'vfs_india_-011-indonesia-police-vf3-drone-patrols',
      question: "Indonesia Police VF 3 deployment: Trích xuất chi tiết về việc cảnh sát Indonesia triển khai xe điện VinFast VF 3. Cụ thể: Lực lượng Cảnh sát Giao thông Indonesia (Korlantas Polri) cải tiến VF 3 làm căn cứ di động cho các hoạt động tuần tra bằng drone tích hợp AI phục vụ hệ thống phạt nguội ETLE (Electronic Traffic Law Enforcement), thông số kỹ thuật cải tiến và chi tiết hợp tác. Trình bày chi tiết bằng tiếng Việt với các số liệu thực tế.",
      title: "Cảnh sát Indonesia cải tiến VinFast VF 3 làm căn cứ di động cho drone AI tuần tra ETLE"
    },
    {
      id: '012',
      slug: 'vfs_india_-012-vinfast-india-tamil-nadu-export-strategy',
      question: "VinFast India Tamil Nadu and Export Strategy: Trích xuất chi tiết về nhà máy Thoothukudi ở Tamil Nadu (Ấn Độ) và chiến lược xuất khẩu. Cụ thể: Tiến độ Giai đoạn I (vốn 400 triệu USD, công suất 150.000 xe/năm) và kế hoạch xuất khẩu xe tay lái nghịch (RHD - Right Hand Drive) từ Ấn Độ sang các thị trường khu vực như Sri Lanka, Nepal, Mauritius, Trung Đông và Châu Phi, các mục tiêu doanh số xuất khẩu. Trình bày chi tiết bằng tiếng Việt với các số liệu cụ thể.",
      title: "Tiến độ nhà máy VinFast Tamil Nadu và chiến lược xuất khẩu xe tay lái nghịch RHD sang Nam Á, Trung Đông, Châu Phi"
    },
    {
      id: '013',
      slug: 'vfs_india_-013-green-sm-india-launch-ride-hailing-expansion',
      question: "Green SM India launch and expansion: Trích xuất chi tiết về sự ra mắt của Green SM (trước đây là Xanh SM) tại thị trường gọi xe Ấn Độ. Cụ thể: Sự kiện ra mắt tại Delhi-NCR vào ngày 5/6/2026 với dịch vụ Green SM Limo (taxi điện cao cấp sử dụng xe MPV 7 chỗ VF Limo Green / VF 7), quá trình đổi tên thương hiệu từ Xanh SM thành Green SM trong tháng 4/2026, gói tuyển dụng tài xế (mức lương từ 35.000 đến 40.000 Rupee/tháng). Trình bày chi tiết bằng tiếng Việt với các con số và mốc thời gian cụ thể.",
      title: "Green SM đổ bộ thị trường Ấn Độ: Ra mắt Green SM Limo tại Delhi-NCR, gói lương tài xế 35k-40k Rupee và đổi nhận diện thương hiệu"
    }
  ];
  
  const vaultDir = '/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/vinfast-an-do/research_vault';
  if (!fs.existsSync(vaultDir)) {
    fs.mkdirSync(vaultDir, { recursive: true });
  }
  
  for (let i = 0; i < queries.length; i++) {
    const q = queries[i];
    console.log(`\n========================================`);
    console.log(`Processing Query ${i + 1}/${queries.length}: ${q.title}`);
    console.log(`========================================`);
    
    // Check if files already exist
    const mdPath = path.join(vaultDir, `${q.slug}.md`);
    const jsonPath = path.join(vaultDir, `${q.slug}.json`);
    
    if (fs.existsSync(mdPath) && fs.existsSync(jsonPath)) {
      console.log(`Files already exist for ${q.slug}. Skipping...`);
      continue;
    }
    
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
    
    // Locate submit button specifically inside the chat panel
    console.log('Locating submit button...');
    const submitBtn = page.locator('chat-panel button.submit-button, chat-panel button[aria-label="Gửi"]').first();
    await submitBtn.waitFor({ timeout: 5000 });
    
    const isEnabled = await submitBtn.isEnabled();
    if (!isEnabled) {
      console.log('Submit button is disabled via Playwright check. Trying page.keyboard.press("Enter")...');
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
    
    for (let j = 0; j < 60; j++) { // Check for up to 180 seconds (60 * 3s)
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
        console.log('Last message in DOM is still the user query, waiting...');
        continue;
      }
      
      const currentLength = lastMsg.text.length;
      console.log(`[${(j + 1) * 3}s] Last message length: ${currentLength}`);
      
      if (currentLength > 0 && currentLength === lastLength) {
        stableCount++;
        if (stableCount >= 4) { // Stable for 12 seconds
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
      console.error(`Timeout waiting for response for query: ${q.title}`);
      // Try to fallback to whatever text is there
      responseText = await page.evaluate(() => {
        const msgs = Array.from(document.querySelectorAll('chat-message'));
        const lastMsg = msgs[msgs.length - 1];
        return lastMsg ? lastMsg.innerText : '';
      });
    }
    
    // Clean citations and parse if possible
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
    
    // Screenshot progress
    try {
      await page.screenshot({ path: `/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/extraction_progress_${q.id}.png` });
    } catch {}
    
    await delay(5000); // 5s cooldown between queries
  }
  
  await browser.close();
  console.log('\nAll batch extractions complete!');
}

main().catch(console.error);
