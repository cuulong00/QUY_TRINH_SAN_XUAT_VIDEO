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

        // Tìm tab đang mở Google Flow
        const pages = await browser.pages();
        let flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        if (!flowPage) {
            console.error('Không tìm thấy tab Google Flow nào đang mở.');
            return;
        }

        // Định vị trực tiếp URL của Custom Tool đã được remix trên tài khoản của người dùng
        const toolUrl = 'https://labs.google/fx/tools/flow/project/759075a7-9c26-43f4-8e47-c6a8ef8d5614/tool/bb118cac-48c5-47fb-84f8-aac2a0781bba';
        console.log(`Điều hướng trực tiếp tới Custom Tool URL: ${toolUrl}`);
        
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(5000); // Chờ trang tool nạp xong hoàn toàn

        // Click nút "Chỉnh sửa" ở trên cùng để vào giao diện lập trình của tool
        console.log('Đang click nút "Chỉnh sửa" để mở Tool Builder...');
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
            console.warn('Không click được nút "Chỉnh sửa" (có thể đã ở chế độ chỉnh sửa rồi).');
        }
        await delay(5000); // Chờ giao diện chỉnh sửa nạp xong

        // Đọc prompt nâng cấp v2
        const promptPath = path.join(__dirname, 'google_flow_advanced_vibe_prompt_v2.md');
        if (!fs.existsSync(promptPath)) {
            console.error('Không tìm thấy file prompt v2.');
            return;
        }
        const promptContent = fs.readFileSync(promptPath, 'utf8').trim();

        // Tìm ô chat Tool Builder (thanh bên phải)
        const chatInputSelector = 'div[data-slate-editor="true"][contenteditable="true"]';
        console.log('Đang tìm ô chat Tool Builder bên phải...');
        await flowPage.waitForSelector(chatInputSelector, { timeout: 10000 });
        
        await flowPage.click(chatInputSelector);
        await delay(500);

        // Xóa sạch nội dung cũ trong ô chat
        console.log('Đang xóa sạch nội dung cũ trong ô chat Tool Builder...');
        await flowPage.evaluate(() => {
            const editor = document.querySelector('div[data-slate-editor="true"][contenteditable="true"]');
            if (editor) {
                editor.focus();
                document.execCommand('selectAll', false, null);
            }
        });
        await delay(500);
        await flowPage.keyboard.press('Backspace');
        await delay(500);

        // Gõ prompt nâng cấp v2
        console.log('Đang gõ prompt nâng cấp v2...');
        await flowPage.keyboard.type(promptContent, { delay: 0 }); // delay = 0 để gõ cực nhanh
        await delay(3000); // Chờ text được nạp và React cập nhật state

        // Định vị và click nút "Tạo" (Gửi) của Tool Builder
        console.log('Đang tìm nút Gửi của Tool Builder (nút "Tạo" hoặc "arrow_forward")...');
        const clickSuccess = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            
            // Tìm nút nằm ở bên phải màn hình (khu vực Tool Builder)
            const rightPanelButtons = buttons.filter(b => {
                const rect = b.getBoundingClientRect();
                return rect.left > window.innerWidth * 0.6 && rect.width > 0 && rect.height > 0;
            });

            // Tìm nút chứa đúng chữ "Tạo" hoặc icon "arrow_forward" (nhưng không phải arrow_forward_ios)
            const sendBtn = rightPanelButtons.find(b => {
                const text = b.textContent?.trim() || '';
                return text.includes('Tạo') || 
                       text.includes('Generate') || 
                       (text.includes('arrow_forward') && !text.includes('arrow_forward_ios'));
            });

            if (sendBtn) {
                sendBtn.click();
                return { success: true, text: sendBtn.textContent?.trim() };
            }
            return { success: false, availableButtons: rightPanelButtons.map(b => b.textContent?.trim()) };
        });

        console.log('Kết quả click nút gửi:', clickSuccess);

        if (!clickSuccess.success) {
            console.log('Không tìm thấy nút gửi, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI bắt đầu lập trình...');
        await delay(8000);

        // Theo dõi tiến trình AI cập nhật code
        let isWorking = true;
        let checkCount = 0;
        const maxChecks = 30; // 30 * 5s = 150s

        while (isWorking && checkCount < maxChecks) {
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                return bodyText.includes('Thinking…') || bodyText.includes('Working…') || bodyText.includes('Đang xử lý') || bodyText.includes('Đang cập nhật');
            });
            console.log(`AI đang cập nhật code... (Lần kiểm tra ${checkCount}) - Trạng thái: ${isWorking ? 'Đang chạy' : 'Đã xong/Chưa chạy'}`);
            
            if (checkCount === 1) {
                await flowPage.screenshot({ path: path.join(__dirname, 'upgrade_in_progress.png') });
            }
            
            await delay(5000);
        }

        console.log('AI đã cập nhật xong code mới cho Custom Tool!');
        await delay(3000);

        // Chụp ảnh màn hình kết quả
        const finalScreenshot = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/final_upgrade_success.png');
        await flowPage.screenshot({ path: finalScreenshot });
        console.log(`Đã chụp ảnh màn hình kết quả tại: ${finalScreenshot}`);

        // Click nút "Xong" để áp dụng giao diện mới
        console.log('Đang click nút "Xong" để chuyển về giao diện ứng dụng chạy thực tế...');
        await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button, a, span'));
            const doneBtn = buttons.find(b => b.textContent?.trim() === 'Xong' || b.textContent?.trim() === 'Done');
            if (doneBtn) {
                doneBtn.click();
            }
        });
        await delay(3000);
        console.log('Hoàn tất quy trình nâng cấp!');

    } catch (error) {
        console.error('Lỗi trong quá trình nâng cấp:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
