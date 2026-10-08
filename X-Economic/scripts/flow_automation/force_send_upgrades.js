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
        const flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        if (!flowPage) {
            console.error('Không tìm thấy tab Google Flow nào đang mở.');
            return;
        }

        console.log(`Đang chạy trên tab: ${flowPage.url()}`);

        // Bước 1: Click nút "Chỉnh sửa" ở trên cùng để chắc chắn hiển thị Tool Builder
        console.log('Đang click nút "Chỉnh sửa"...');
        await flowPage.evaluate(() => {
            const tabs = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = tabs.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                editTab.click();
            }
        });
        await delay(5000);

        // Đọc prompt nâng cấp v2
        const promptPath = path.join(__dirname, 'google_flow_advanced_vibe_prompt_v2.md');
        if (!fs.existsSync(promptPath)) {
            console.error('Không tìm thấy file prompt v2.');
            return;
        }
        const promptContent = fs.readFileSync(promptPath, 'utf8').trim();

        // Bước 2: Focus vào ô chat Tool Builder
        const chatInputSelector = 'div[data-slate-editor="true"][contenteditable="true"]';
        console.log('Đang tìm ô chat Tool Builder...');
        await flowPage.waitForSelector(chatInputSelector, { timeout: 10000 });
        
        await flowPage.click(chatInputSelector);
        await delay(500);

        // Bước 3: Xóa sạch nội dung cũ bằng selectAll và Backspace để đồng bộ React state
        console.log('Đang xóa sạch nội dung cũ trong ô chat...');
        await flowPage.evaluate(() => {
            const editor = document.querySelector('div[data-slate-editor="true"][contenteditable="true"]');
            if (editor) {
                editor.focus();
                // Bôi đen toàn bộ text trong editor
                document.execCommand('selectAll', false, null);
            }
        });
        await delay(500);
        await flowPage.keyboard.press('Backspace');
        await delay(500);

        // Bước 4: Gõ prompt v2
        console.log('Đang gõ prompt nâng cấp v2 vào ô chat...');
        await flowPage.keyboard.type(promptContent, { delay: 0 }); // delay = 0 để gõ cực nhanh
        await delay(3000); // Chờ text được nạp xong và React kích hoạt nút gửi

        // Bước 5: Định vị và click nút Gửi của Tool Builder (nút nằm ở góc phải bên dưới)
        console.log('Đang tìm nút Gửi của Tool Builder (nút "Tạo" hoặc "arrow_forward")...');
        const clickSuccess = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            
            // Tìm nút nằm ở bên phải màn hình
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
                return { success: true, text: sendBtn.textContent?.trim(), className: sendBtn.className };
            }
            return { success: false, availableButtons: rightPanelButtons.map(b => b.textContent?.trim()) };
        });

        console.log('Kết quả click nút gửi:', clickSuccess);

        if (!clickSuccess.success) {
            console.log('Không tìm thấy nút gửi bằng tọa độ, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI bắt đầu lập trình...');
        await delay(8000);

        // Bước 6: Theo dõi tiến trình lập trình của AI
        let isWorking = true;
        let checkCount = 0;
        const maxChecks = 30; // 30 * 5s = 150s

        while (isWorking && checkCount < maxChecks) {
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                return bodyText.includes('Thinking…') || bodyText.includes('Working…') || bodyText.includes('Đang xử lý') || bodyText.includes('Đang cập nhật');
            });
            console.log(`AI đang lập trình... (Lần kiểm tra ${checkCount}) - Trạng thái: ${isWorking ? 'Đang chạy' : 'Đã dừng/Chưa chạy'}`);
            
            // Chụp ảnh màn hình tiến trình ở lần kiểm tra đầu tiên hoặc khi AI bắt đầu chạy để debug
            if (checkCount === 1 || (checkCount === 2 && isWorking)) {
                await flowPage.screenshot({ path: path.join(__dirname, `progess_check_${checkCount}.png`) });
            }
            
            await delay(5000);
        }

        console.log('AI đã lập trình xong!');
        await delay(3000);

        // Chụp ảnh màn hình kết quả cuối cùng
        const finalScreenshot = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/final_upgrade_success.png');
        await flowPage.screenshot({ path: finalScreenshot });
        console.log(`Đã chụp ảnh màn hình kết quả tại: ${finalScreenshot}`);

        // Click nút "Xong" (Done) ở góc phải trên cùng để lưu và chạy ứng dụng
        console.log('Đang click nút "Xong" để áp dụng giao diện mới...');
        await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button, a, span'));
            const doneBtn = buttons.find(b => b.textContent?.trim() === 'Xong' || b.textContent?.trim() === 'Done');
            if (doneBtn) {
                doneBtn.click();
            }
        });
        await delay(3000);

    } catch (error) {
        console.error('Lỗi khi nâng cấp:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
