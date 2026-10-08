const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function run() {
    let browser;
    try {
        console.log('Connecting to Chrome...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        const pages = await browser.pages();
        let flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        if (!flowPage) {
            console.error('Không tìm thấy tab Google Flow nào đang mở.');
            return;
        }

        // 1. Điều hướng thẳng tới URL của Custom Tool để tránh bị lạc ở trang dự án chính
        const toolUrl = 'https://labs.google/fx/tools/flow/project/759075a7-9c26-43f4-8e47-c6a8ef8d5614/tool/bb118cac-48c5-47fb-84f8-aac2a0781bba';
        console.log(`Điều hướng trực tiếp tới Tool URL: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(6000);

        // 2. Bấm nút "Chỉnh sửa" ở trên cùng để vào Edit Mode của tool
        console.log('Đang click nút "Chỉnh sửa" ở trên cùng...');
        const clickedEdit = await flowPage.evaluate(() => {
            const tabs = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = tabs.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                editTab.click();
                return true;
            }
            return false;
        });

        if (!clickedEdit) {
            console.warn('Có thể đã ở sẵn trong chế độ chỉnh sửa.');
        }
        await delay(6000);

        // 3. Định vị chính xác ô chat Tool Builder (bên phải màn hình)
        console.log('Đang định vị ô chat Tool Builder ở nửa bên phải màn hình...');
        const hasFocused = await flowPage.evaluate(() => {
            const editors = Array.from(document.querySelectorAll('div[data-slate-editor="true"][contenteditable="true"]'));
            // Lọc tìm editor nằm ở nửa bên phải màn hình (left > 50% width)
            const toolBuilderEditor = editors.find(el => {
                const rect = el.getBoundingClientRect();
                return rect.left > window.innerWidth * 0.5;
            });

            if (toolBuilderEditor) {
                toolBuilderEditor.focus();
                // Bôi đen toàn bộ để chuẩn bị xóa
                document.execCommand('selectAll', false, null);
                return true;
            }
            return false;
        });

        if (!hasFocused) {
            console.error('Không tìm thấy ô chat Tool Builder ở bên phải màn hình. Vui lòng kiểm tra lại giao diện.');
            await flowPage.screenshot({ path: path.join(__dirname, 'error_no_right_chat.png') });
            await page.close();
            return;
        }

        await delay(500);
        await flowPage.keyboard.press('Backspace');
        await delay(500);

        // Đọc prompt nâng cấp v2
        const promptPath = path.join(__dirname, 'google_flow_advanced_vibe_prompt_v2.md');
        const promptContent = fs.readFileSync(promptPath, 'utf8').trim();

        // 4. Gõ prompt nâng cấp v2 vào ô chat Tool Builder
        console.log('Đang dán prompt v2 vào đúng ô chat Tool Builder...');
        await flowPage.keyboard.type(promptContent, { delay: 0 });
        await delay(4000);

        // 5. Định vị chính xác nút Gửi ("Tạo") của Tool Builder bên phải màn hình
        console.log('Đang tìm nút Gửi của Tool Builder (nút "Tạo" ở bên phải màn hình)...');
        const clickSendSuccess = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            
            // Tìm nút nằm ở bên phải màn hình và chứa chữ "Tạo" hoặc icon arrow_forward (không phải arrow_forward_ios)
            const sendBtn = buttons.find(b => {
                const rect = b.getBoundingClientRect();
                const text = b.textContent?.trim() || '';
                return rect.left > window.innerWidth * 0.5 && 
                       (text.includes('Tạo') || text.includes('Generate') || (text.includes('arrow_forward') && !text.includes('arrow_forward_ios')));
            });

            if (sendBtn) {
                sendBtn.click();
                return { success: true, text: sendBtn.textContent?.trim() };
            }
            return { success: false };
        });

        console.log('Kết quả gửi prompt:', clickSendSuccess);

        if (!clickSendSuccess.success) {
            console.log('Không click được nút gửi, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI bắt đầu cập nhật code (8 giây)...');
        await delay(8000);

        // 6. Theo dõi tiến trình AI của Tool Builder viết code
        let isWorking = true;
        let checkCount = 0;
        const maxChecks = 35; // 35 * 5s = 175s

        while (isWorking && checkCount < maxChecks) {
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                // AI Tool Builder tiếng Việt thường hiển thị "Thinking..." hoặc "Đang cập nhật..." trong panel bên phải
                return bodyText.includes('Thinking…') || bodyText.includes('Working…') || bodyText.includes('Đang xử lý') || bodyText.includes('Đang cập nhật');
            });
            console.log(`AI đang code lại ứng dụng... (Lần kiểm tra ${checkCount}) - Trạng thái: ${isWorking ? 'Đang viết code' : 'Đã hoàn tất'}`);
            await delay(5000);
        }

        console.log('AI đã lập trình nâng cấp xong!');
        await delay(3000);

        // Chụp ảnh màn hình kết quả
        const finalScreenshot = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/final_upgrade_success.png');
        await flowPage.screenshot({ path: finalScreenshot });
        console.log(`Đã lưu ảnh chụp màn hình ứng dụng mới tại: ${finalScreenshot}`);

        // 7. Bấm nút "Xong" để áp dụng code mới và chạy thử giao diện
        console.log('Đang bấm nút "Xong" để lưu và chạy giao diện mới...');
        await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button, a, span'));
            const doneBtn = buttons.find(b => b.textContent?.trim() === 'Xong' || b.textContent?.trim() === 'Done');
            if (doneBtn) {
                doneBtn.click();
            }
        });
        await delay(3000);
        console.log('Hoàn tất quy trình nâng cấp 100%!');

    } catch (error) {
        console.error('Lỗi critical:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
