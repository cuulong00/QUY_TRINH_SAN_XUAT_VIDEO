import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const notebookUrl = "https://notebooklm.google.com/notebook/48518ca4-8f89-4411-9a41-8d94e22b2166";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";
const outputDir = "/Users/pro16/Documents/VideoProject/Dòng Chảy/episodes/vinhomes-ngung-quy-dat/research_vault";

const extractionQuestions = [
  {
    fileName: "001_vinhomes_land_fund.md",
    question: "Hãy trích xuất chi tiết số liệu và phân tích về quỹ đất 29.500 ha của Vinhomes tại Việt Nam. Quỹ đất này tập trung ở những phân khúc nào, vị trí địa lý ra sao, và khả năng phát triển trong vòng bao nhiêu năm tới (5-7 năm)? Những đại dự án trọng điểm nào đang và sắp triển khai (như Vinhomes Royal Island, Vinhomes Cổ Loa, Vinhomes Wonder Park...)? Vì sao ban lãnh đạo Vinhomes tự tin tuyên bố quỹ đất hiện tại 'đã đủ'?"
  },
  {
    fileName: "002_financial_target_2026.md",
    question: "Hãy phân tích chi tiết kế hoạch tài chính năm 2026 của Vinhomes với mục tiêu doanh thu 250.000 tỷ đồng và lợi nhuận sau thuế 50.000 tỷ đồng. Những động lực tăng trưởng cốt lõi nào giúp Vinhomes tự tin đạt được con số kỷ lục này? Tiến độ triển khai và ghi nhận doanh thu từ các dự án BĐS tại Việt Nam đóng góp vào mục tiêu này ra sao?"
  },
  {
    fileName: "003_congo_megacity.md",
    question: "Hãy trích xuất toàn bộ thông tin chi tiết về dự án đại đô thị 6.300 ha của Vingroup tại Kinshasa, Cộng hòa Dân chủ Congo. Dự án này có quy hoạch như thế nào, nằm ở khu vực nào ven sông? Cơ chế chính phủ Congo cấp đất miễn phí cho Vingroup hoạt động ra sao? Các thông tin pháp lý về việc thành lập Vingroup DRC Holding S.A.R.L. vào tháng 12/2025?"
  },
  {
    fileName: "004_financial_support_vinfast.md",
    question: "Hãy phân tích chi tiết về cơ cấu nợ, chi phí lãi vay, đòn bẩy tài chính của Vinhomes và áp lực dòng tiền hỗ trợ VinFast/Vingroup. Báo cáo tài chính cho thấy Vinhomes đang hỗ trợ tài chính cho VinFast dưới các hình thức nào (cho vay, bảo lãnh, đầu tư chéo)? Mức độ rủi ro lan truyền (risk transmission) trong hệ sinh thái Vingroup là bao nhiêu?"
  },
  {
    fileName: "005_congo_green_mobility.md",
    question: "Hãy trích xuất chi tiết chiến lược chuyển đổi xanh của Vingroup và VinFast/GSM tại Cộng hòa Dân chủ Congo. Thỏa thuận về hành lang giao thông xanh Kinshasa - Brazzaville, cam kết chuyển đổi 300.000 phương tiện xanh, việc độc quyền xây dựng hạ tầng trạm sạc và vận hành xe buýt điện, taxi điện của GSM được triển khai thế nào?"
  },
  {
    fileName: "006_congo_macro_risks.md",
    question: "Hãy đánh giá chi tiết các rủi ro vĩ mô, pháp lý, an ninh và bất ổn chính trị tại Cộng hòa Dân chủ Congo (DRC) mà Vingroup phải đối mặt khi đầu tư đại dự án. Bối cảnh kinh tế Kinshasa, biến động GDP, lạm phát, và rủi ro chủ quyền ảnh hưởng thế nào đến tính khả thi của dự án?"
  },
  {
    fileName: "007_historical_analogs.md",
    question: "Hãy cung cấp các case study hoặc mô hình đối sánh quốc tế tương đương về việc các tập đoàn gia đình quy mô lớn (như các Chaebol Hàn Quốc hay Keiretsu Nhật Bản) sử dụng đòn bẩy tài chính từ mảng kinh doanh cốt lõi (như BĐS, công nghiệp truyền thống) để tài trợ cho các canh bạc công nghệ hoặc ngành công nghiệp mới (như xe điện, bán dẫn). Những bài học thành công hoặc thất bại xương máu là gì?"
  },
  {
    fileName: "008_strategic_verdict.md",
    question: "Hãy tổng hợp phân tích bản án chiến lược (Strategic Verdict): Mối liên hệ logic giữa việc Vinhomes tuyên bố dừng mở rộng quỹ đất tại Việt Nam (nhường sân cho doanh nghiệp khác nhưng thực chất là tối ưu hóa dòng tiền mặt) và việc dồn lực tài chính để gánh vác VinFast cũng như thực hiện canh bạc lớn tại Congo. Ý đồ chiến lược thực sự của tỷ phú Phạm Nhật Vượng đằng sau nước cờ này là gì?"
  }
];

async function clearChat(page) {
  try {
    console.log("  🧹 Clearing chat history for a clean session...");
    const menuBtn = page.locator('.chat-header-buttons button').last();
    if (await menuBtn.isVisible()) {
      await menuBtn.click({ force: true });
      await page.waitForTimeout(1000);
      
      const clearOption = page.locator('.cdk-overlay-pane button:has-text("Xoá nhật ký"), .cdk-overlay-pane button:has-text("Clear chat"), button:has-text("Xoá nhật ký trò chuyện")').first();
      if (await clearOption.isVisible()) {
        await clearOption.click({ force: true });
        await page.waitForTimeout(1500);
        
        // Click nút xác nhận xóa trong popup dialog
        const confirmBtn = page.locator('mat-dialog-container button:has-text("Xoá"), mat-dialog-container button:has-text("Xóa"), mat-dialog-container button:has-text("Delete"), button:has-text("Xoá")').filter({ visible: true }).first();
        if (await confirmBtn.isVisible()) {
          await confirmBtn.click({ force: true });
          console.log("    ✅ Chat history cleared via confirmation dialog!");
          await page.waitForTimeout(3000); // Đợi panel chat làm sạch hoàn toàn
        } else {
          console.log("    ✅ Chat history cleared (no confirmation dialog appeared)!");
        }
      } else {
        console.log("    ⚠️ Clear options not found in menu!");
        await page.keyboard.press('Escape');
      }
    } else {
      console.log("    ⚠️ Chat menu button is not visible!");
    }
  } catch (err) {
    console.error("    ❌ Error in clearChat helper:", err.message);
  }
}

async function run() {
  console.log("🚀 Initializing output directory...");
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
    console.log(`  ✅ Created directory: ${outputDir}`);
  }

  console.log("🚀 Launching Chrome browser with persistent profile...");
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
  
  console.log(`🌐 Navigating to NotebookLM: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(15000); // Chờ tải xong trang ban đầu

  // Tắt popup/overlay nếu có lúc bắt đầu
  try {
    const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').filter({ visible: true }).first();
    if (await closeBtn.isVisible()) {
      await closeBtn.click({ force: true });
      console.log("  ✅ Closed popup overlay");
      await page.waitForTimeout(1000);
    }
  } catch (e) {}

  for (let idx = 0; idx < extractionQuestions.length; idx++) {
    const item = extractionQuestions[idx];
    const filePath = path.join(outputDir, item.fileName);

    console.log(`\n======================================`);
    console.log(`📝 Question ${idx + 1}/${extractionQuestions.length}: [${item.fileName}]`);
    console.log(`======================================`);

    // Kiểm tra xem file đã được trích xuất thành công trước đó chưa (resume logic)
    // Để cho an toàn, ta chỉ skip nếu file > 2500 bytes (chắc chắn là file kết quả đầy đủ, không phải file suy nghĩ ngắn 1200 bytes)
    if (fs.existsSync(filePath)) {
      const stats = fs.statSync(filePath);
      if (stats.size > 2500) {
        console.log(`  ⏭️ File ${item.fileName} already exists with size ${stats.size} bytes. Skipping!`);
        continue;
      } else {
        console.log(`  ⚠️ File ${item.fileName} is too small or invalid (${stats.size} bytes). Re-extracting...`);
      }
    }

    try {
      // 1. Dọn dẹp cuộc trò chuyện cũ để bắt đầu sạch
      await clearChat(page);

      const pairSelector = '.chat-message-pair';
      const countBefore = await page.locator(pairSelector).count();
      console.log(`  📊 Chat pairs after clear: ${countBefore}`);

      // Tìm textarea chat
      const chatInput = page.locator('textarea.query-box-input').filter({ visible: true }).first();
      if (!(await chatInput.isVisible())) {
        throw new Error("Chat input textarea is not visible!");
      }

      console.log("  ⌨️ Typing question...");
      await chatInput.click({ force: true });
      await chatInput.fill(item.question);
      await page.waitForTimeout(1000);

      console.log("  📤 Sending question...");
      await page.keyboard.press('Enter');
      
      // Chờ cặp tin nhắn mới xuất hiện (phải tăng thêm 1)
      console.log("  ⏳ Waiting for AI to start responding (new pair)...");
      let countAfter = countBefore;
      const startWaitBubble = Date.now();
      const targetCount = countBefore + 1;

      while (countAfter < targetCount && Date.now() - startWaitBubble < 25000) {
        await page.waitForTimeout(1000);
        countAfter = await page.locator(pairSelector).count();
      }

      if (countAfter < targetCount) {
        throw new Error("Failed to detect new chat message pair after sending!");
      }

      console.log(`  📊 New chat pair appeared! Total pairs: ${countAfter}`);

      console.log("  ⏳ Waiting for AI response to stabilize (timeout 8 minutes)...");
      const startTime = Date.now();
      const timeoutMs = 480000;
      let lastText = "";
      let stableCount = 0;
      let responseText = "";

      while (Date.now() - startTime < timeoutMs) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        
        // Sử dụng page.evaluate() để lấy text thô tức thời của phần tử cuối cùng
        // Tránh hoàn toàn cơ chế actionability block gây timeout của Playwright
        let currentText = await page.evaluate(() => {
          const pairs = document.querySelectorAll('.chat-message-pair');
          if (pairs.length === 0) return "";
          const lastPair = pairs[pairs.length - 1];
          return lastPair.textContent || lastPair.innerText || "";
        });

        // Kiểm tra xem text có thay đổi nội dung không
        // Độ dài tối thiểu phải lớn hơn độ dài câu hỏi gốc ít nhất 800 ký tự
        const minLength = item.question.length + 800;
        
        if (currentText.length > minLength && currentText === lastText) {
          stableCount++;
          if (stableCount >= 6) { // Ổn định trong 6 chu kỳ (18 giây)
            console.log(`  ✅ Response completed and stabilized after ${elapsed}s!`);
            // Cắt bỏ phần câu hỏi của user ở đầu tin nhắn
            responseText = currentText.replace(item.question, "").trim();
            break;
          }
        } else {
          stableCount = 0;
          lastText = currentText;
        }

        if (elapsed % 15 === 0) {
          console.log(`    Status: Generating... (${elapsed}s), Total text length: ${currentText.length}`);
        }

        await page.waitForTimeout(3000);
      }

      if (!responseText) {
        // Fallback: lấy nội dung cuối cùng
        const currentText = await page.evaluate(() => {
          const pairs = document.querySelectorAll('.chat-message-pair');
          if (pairs.length === 0) return "";
          const lastPair = pairs[pairs.length - 1];
          return lastPair.textContent || lastPair.innerText || "";
        });
        responseText = currentText ? currentText.replace(item.question, "").trim() : "";
        if (responseText.length < 200) {
          throw new Error("Response content is too short or empty!");
        }
        console.log(`  ⚠️ Saved response via fallback (length: ${responseText.length})`);
      }

      // Lưu kết quả vào file markdown
      const fileContent = `# ${item.fileName}\n\n## Question\n${item.question}\n\n## Extract Content\n\n${responseText}\n`;
      fs.writeFileSync(filePath, fileContent, 'utf-8');
      console.log(`  💾 Saved response to ${filePath} (${fileContent.length} bytes)`);

      // Đợi thêm vài giây trước khi hỏi câu tiếp theo
      await page.waitForTimeout(5000);

    } catch (err) {
      console.error(`  ❌ Error extracting question ${idx + 1}:`, err.message);
      try {
        const screenshotErrPath = path.join(outputDir, `error_extract_question_${idx+1}.png`);
        await page.screenshot({ path: screenshotErrPath });
        console.log(`  📸 Saved error screenshot to ${screenshotErrPath}`);
      } catch (screenshotErr) {
        console.error("  ⚠️ Failed to take error screenshot:", screenshotErr.message);
      }
    }
  }

  console.log("\n🔒 Closing context...");
  await context.close();
  console.log("🎉 All extractions finished successfully!");
}

run().catch(err => {
  console.error("❌ Uncaught error in main extraction runner:", err);
});
