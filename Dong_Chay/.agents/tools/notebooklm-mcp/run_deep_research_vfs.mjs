import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const notebookUrl = "https://notebooklm.google.com/notebook/a31c4014-b6cc-4645-bc03-7814539fd4ba";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

const queries = [
  // 1. Vĩ mô quốc tế - Định giá kỳ vọng và Tư bản định giá
  "corporate governance valuation based capitalism how founders get rich from loss making startups",
  
  // 2. Vĩ mô quốc tế - Cơ chế thế chấp cổ phiếu vay tiêu dùng tránh thuế
  "buy borrow die tax planning strategy stock backed loans billionaires collateral margin call risks",
  
  // 3. Case study thế giới - WeWork và Adam Neumann
  "Adam Neumann WeWork exit package SoftBank payout litigation settlement 2021 amount",
  
  // 4. Case study thế giới - Uber và Travis Kalanick
  "Travis Kalanick Uber stock sales post IPO lock up expiration 2019 cash out amount",
  
  // 5. Vĩ mô Việt Nam - Mối quan hệ tài chính và dòng vốn chéo trong hệ sinh thái Vingroup
  "Vingroup Vinhomes tài trợ VinFast cam kết Phạm Nhật Vượng giải ngân mới nhất 2025 2026",
  
  // 6. Số liệu VinFast Q1/2026 mới nhất
  "VinFast báo cáo tài chính quý 1 2026 doanh thu lỗ thuần bàn giao xe SEC filings"
];

async function run() {
  console.log("🚀 Khởi chạy trình duyệt Playwright ở chế độ hiển thị (headless: false)...");
  
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: false, // Hiển thị trình duyệt để người dùng nhìn thấy và kiểm soát
    viewport: { width: 1366, height: 768 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-first-run',
      '--no-default-browser-check',
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  });

  const page = await context.newPage();
  console.log(`🌐 Đang mở Notebook: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(8000);

  // Hàm đếm số nguồn hiện có trong Notebook
  async function countSources() {
    try {
      const c1 = await page.locator('.single-source-container').count();
      const c2 = await page.locator('input.mdc-checkbox__native-control').count();
      const checkboxCount = c2 > 0 ? c2 - 1 : 0;
      return Math.max(c1, checkboxCount);
    } catch {
      return 0;
    }
  }

  // Hàm tắt các popup đè màn hình
  async function dismissOverlays() {
    try {
      const closeBtn = page.locator('button.close-button, button[aria-label="Đóng"], button[aria-label="Close"]').filter({ visible: true }).first();
      if (await closeBtn.isVisible()) {
        await closeBtn.click({ force: true });
        console.log("  ✅ Đã đóng popup overlay");
        await page.waitForTimeout(1000);
      }
    } catch (e) {}

    try {
      const backdrop = page.locator('.cdk-overlay-backdrop').filter({ visible: true }).first();
      if (await backdrop.isVisible()) {
        await page.keyboard.press('Escape');
        console.log("  ✅ Đã nhấn Escape để tắt backdrop");
        await page.waitForTimeout(1000);
      }
    } catch (e) {}
  }

  // Hàm kiểm tra và click nút Import nếu có tìm kiếm cũ chưa nạp
  async function handlePendingImport() {
    await dismissOverlays();
    
    const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
    const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa"), button:has-text("Clear")').filter({ visible: true }).first();
    
    if (await importBtn.isVisible()) {
      console.log("  ✅ Phát hiện nút Nhập (Import) chưa nạp! Đang click...");
      await importBtn.click({ force: true });
      await page.waitForTimeout(10000);
    }

    if (await deleteBtn.isVisible()) {
      console.log("  🧹 Đang dọn dẹp panel tìm kiếm cũ...");
      await deleteBtn.click({ force: true });
      await page.waitForTimeout(3000);
    }
  }

  await dismissOverlays();
  await handlePendingImport();

  let sourcesBefore = await countSources();
  console.log(`📊 Số lượng nguồn ban đầu: ${sourcesBefore}`);

  // Thực thi tuần tự từng câu query theo đúng kế hoạch
  for (let idx = 0; idx < queries.length; idx++) {
    const query = queries[idx];
    console.log(`\n======================================`);
    console.log(`📝 THỰC THI QUERY ${idx + 1}/${queries.length}: "${query}"`);
    console.log(`======================================`);

    try {
      console.log("  🔄 Refresh lại trang để có slate sạch...");
      await page.reload();
      await page.waitForTimeout(10000);
      await dismissOverlays();
      await handlePendingImport();

      // 1. Chuyển sang chế độ Deep Research
      const trigger = page.locator('button.corpus-select.researcher-menu-trigger, button.corpus-select:has-text("Nghiên cứu nhanh"), button.corpus-select:has-text("Nghiên cứu sâu"), button.corpus-select:has-text("Deep Research"), button.corpus-select:has(mat-icon:has-text("search_spark"))').filter({ visible: true }).first();
      if (await trigger.isVisible()) {
        const text = await trigger.textContent();
        if (!text.includes('Deep Research') && !text.includes('Nghiên cứu sâu')) {
          console.log("  🔄 Đang click chuyển đổi sang chế độ Nghiên cứu sâu (Deep Research)...");
          await trigger.click({ force: true });
          await page.waitForTimeout(2000);

          const deepOption = page.locator('.cdk-overlay-pane button.research-option-deep-research, .cdk-overlay-pane button:has-text("Deep Research"), .cdk-overlay-pane button:has-text("Nghiên cứu sâu")').filter({ visible: true }).first();
          if (await deepOption.isVisible()) {
            await deepOption.click({ force: true });
            await page.waitForTimeout(2000);
            console.log(`  ✅ Đã chuyển sang chế độ Deep Research: "${await trigger.textContent()}"`);
          } else {
            console.log("  ⚠️ Không tìm thấy nút Deep Research trong danh sách tùy chọn");
          }
        } else {
          console.log("  ✅ Đã ở sẵn trong chế độ Deep Research");
        }
      } else {
        console.log("  ⚠️ Không thấy nút trigger chế độ, thử click qua nút Thêm nguồn (Add source)...");
        const addSourceBtn = page.locator('button:has-text("Thêm nguồn"), button:has-text("Add source")').filter({ visible: true }).first();
        if (await addSourceBtn.isVisible()) {
          await addSourceBtn.click({ force: true });
          await page.waitForTimeout(2000);
          const deepOption = page.locator('button.research-option-deep-research, button:has-text("Deep Research"), button:has-text("Nghiên cứu sâu")').filter({ visible: true }).first();
          if (await deepOption.isVisible()) {
            await deepOption.click({ force: true });
            await page.waitForTimeout(2000);
          }
        }
      }

      // 2. Điền query vào textarea
      const textarea = page.locator('textarea.query-box-textarea, textarea[aria-label*="Khám phá nguồn" i], textarea[aria-label*="Discover sources" i]').filter({ visible: true }).first();
      if (!(await textarea.isVisible())) {
        throw new Error("Không tìm thấy textarea để nhập câu hỏi!");
      }

      const isDisabled = await textarea.isDisabled();
      if (isDisabled) {
        console.log("  ⚠️ Textarea đang bị khóa! Thử dọn dẹp panel tìm kiếm cũ...");
        const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa")').filter({ visible: true }).first();
        if (await deleteBtn.isVisible()) {
          await deleteBtn.click({ force: true });
          await page.waitForTimeout(3000);
        }
        if (await textarea.isDisabled()) {
          throw new Error("Textarea vẫn bị khóa sau khi dọn dẹp!");
        }
      }

      console.log("  ⌨️  Đang điền câu truy vấn...");
      await textarea.click({ force: true });
      await textarea.fill(query);
      await page.waitForTimeout(1000);

      // 3. Submit tìm kiếm
      console.log("  📤 Gửi yêu cầu tìm kiếm...");
      const submitBtn = page.locator('button.actions-enter-button, button[aria-label="Gửi"], button[aria-label="Submit"]').filter({ visible: true }).first();
      if (await submitBtn.isVisible() && !(await submitBtn.isDisabled())) {
        await submitBtn.click({ force: true });
      } else {
        await page.keyboard.press('Enter');
      }
      await page.waitForTimeout(6000);

      // 4. Đợi quá trình Deep Research hoàn thành (Tối đa 10 phút)
      console.log("  ⏳ Đang chờ quá trình Deep Research hoàn tất trên Google (tối đa 10 phút)...");
      const startTime = Date.now();
      const timeoutMs = 600000;
      let querySuccess = false;
      let progressLog = "";

      while (Date.now() - startTime < timeoutMs) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        
        // Kiểm tra xem đã hoàn thành chưa
        const isCompletedText = await page.locator('text="Đã hoàn tất Deep Research!", text="Deep Research completed!"').count() > 0;
        const importBtn = page.locator('button.source-discovery-completed-action-import-button, button:has-text("Nhập"), button:has-text("Import")').filter({ visible: true }).first();
        const isImportVisible = await importBtn.isVisible();
        
        // Chỉ số đang chạy
        const hasProgress = await page.locator('mat-progress-bar, [role="progressbar"], mat-progress-spinner, [class*="spinner"]').count() > 0;
        const isRunningText = await page.locator('text="Đang phân tích kết quả...", text="Analyzing results..."').count() > 0;

        if ((isCompletedText || isImportVisible) && !hasProgress && !isRunningText) {
          console.log(`  ✅ Hoàn tất tìm kiếm sau ${elapsed}s! Đang nhấn Nhập (Import)...`);
          
          if (isImportVisible) {
            await importBtn.click({ force: true });
            await page.waitForTimeout(12000); // Đợi nạp nguồn vào Notebook
          }

          const deleteBtn = page.locator('button.source-discovery-completed-action-delete-button, button:has-text("Xoá"), button:has-text("Xóa")').filter({ visible: true }).first();
          if (await deleteBtn.isVisible()) {
            console.log("  🧹 Dọn dẹp panel tìm kiếm...");
            await deleteBtn.click({ force: true });
            await page.waitForTimeout(3000);
          }

          const newCount = await countSources();
          console.log(`  📊 Cập nhật số lượng nguồn: ${newCount} (đã thêm được ${newCount - sourcesBefore} nguồn)`);
          sourcesBefore = newCount;
          querySuccess = true;
          break;
        }

        const status = (hasProgress || isRunningText) ? `Đang tìm kiếm & phân tích... (${elapsed}s)` : `Đang xử lý... (${elapsed}s)`;
        if (status !== progressLog) {
          console.log(`    ${status}`);
          progressLog = status;
        }

        await page.waitForTimeout(5000);
      }

      if (!querySuccess) {
        throw new Error("Quá trình tìm kiếm của NotebookLM bị timeout!");
      }

      console.log(`  ✅ Hoàn tất query ${idx + 1}!`);

    } catch (queryErr) {
      console.error(`  ❌ Lỗi xảy ra ở query ${idx + 1}:`, queryErr.message);
    }
  }

  const finalSources = await countSources();
  console.log(`\n🎉 ĐÃ HOÀN TẤT TOÀN BỘ 6 TRUY VẤN DEEP RESEARCH!`);
  console.log(`📊 Tổng số nguồn hiện có trong Notebook: ${finalSources}`);

  console.log("🔒 Đóng trình duyệt...");
  await context.close();
}

run().catch(err => {
  console.error("❌ Lỗi uncaught trong main runner:", err);
});
