const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function run() {
    let browser;
    try {
        console.log('Connecting to Chrome via CDP...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        const pages = await browser.pages();
        let flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        const toolUrl = 'https://labs.google/fx/tools/flow/project/759075a7-9c26-43f4-8e47-c6a8ef8d5614/tool/bb118cac-48c5-47fb-84f8-aac2a0781bba';

        if (!flowPage) {
            console.log('Không tìm thấy tab Google Flow nào đang mở. Đang mở tab mới...');
            flowPage = await browser.newPage();
        }

        console.log(`1. Điều hướng tới URL của Tool: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(6000);

        // 2. Chuyển sang tab "Chỉnh sửa" (Edit Mode)
        console.log('2. Click nút "Chỉnh sửa" ở trên cùng...');
        const editTabCoords = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = elements.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                const rect = editTab.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (editTabCoords) {
            await flowPage.mouse.click(editTabCoords.x, editTabCoords.y);
            console.log('Đã click nút "Chỉnh sửa". Chờ 6 giây để giao diện nạp...');
            await delay(6000);
        } else {
            console.warn('Không tìm thấy nút "Chỉnh sửa". Có thể đã ở sẵn Edit Mode.');
        }

        // 3. Đợi cho ô chat của Tool Builder xuất hiện trong DOM
        console.log('3. Chờ ô chat Tool Builder xuất hiện...');
        const chatInputSelector = 'div[data-slate-editor="true"][contenteditable="true"]';
        await flowPage.waitForSelector(chatInputSelector, { timeout: 15000 });

        // Tìm đúng ô chat bên phải bằng tọa độ
        const chatCoords = await flowPage.evaluate(() => {
            const editors = Array.from(document.querySelectorAll('div[data-slate-editor="true"][contenteditable="true"]'));
            const toolBuilderEditor = editors.find(el => el.getBoundingClientRect().left > window.innerWidth * 0.5);
            if (toolBuilderEditor) {
                const rect = toolBuilderEditor.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (!chatCoords) {
            console.error('Không tìm thấy ô chat Tool Builder bên phải màn hình.');
            await flowPage.screenshot({ path: path.join(__dirname, 'error_incremental_chat.png') });
            return;
        }

        console.log(`Click focus vào ô chat Tool Builder tại tọa độ: (${chatCoords.x}, ${chatCoords.y})`);
        await flowPage.mouse.click(chatCoords.x, chatCoords.y);
        await delay(500);

        // Xóa nội dung cũ trong ô chat
        await flowPage.evaluate(() => {
            const editors = Array.from(document.querySelectorAll('div[data-slate-editor="true"][contenteditable="true"]'));
            const toolBuilderEditor = editors.find(el => el.getBoundingClientRect().left > window.innerWidth * 0.5);
            if (toolBuilderEditor) {
                toolBuilderEditor.focus();
                document.execCommand('selectAll', false, null);
            }
        });
        await delay(500);
        await flowPage.keyboard.press('Backspace');
        await delay(500);

        // Lệnh 1: Thêm dropdown chọn model
        const command1 = "Please update the Sidebar.tsx component to add two dropdown selections: 'Select Video Model' (options: Veo 3.1, Veo 3.0) and 'Select Image Model' (options: Imagen 4, Imagen 3, Nano Banana Pro) below the workspace configuration section. Style them with a modern glassmorphic theme to match the UI.";
        
        console.log(`Gửi câu lệnh nâng cấp bước 1: "${command1}"`);
        await flowPage.keyboard.type(command1, { delay: 0 });
        await delay(2000);

        // Click nút gửi ("Tạo") của Tool Builder bên phải
        const sendBtnCoords = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            const sendBtn = buttons.find(b => {
                const rect = b.getBoundingClientRect();
                const text = b.textContent?.trim() || '';
                return rect.left > window.innerWidth * 0.5 && 
                       (text.includes('Tạo') || text.includes('Generate') || (text.includes('arrow_forward') && !text.includes('arrow_forward_ios')));
            });

            if (sendBtn) {
                const rect = sendBtn.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (sendBtnCoords) {
            console.log(`Click gửi tại tọa độ: (${sendBtnCoords.x}, ${sendBtnCoords.y})`);
            await flowPage.mouse.click(sendBtnCoords.x, sendBtnCoords.y);
        } else {
            console.log('Không tìm thấy nút gửi, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI bắt đầu cập nhật code bước 1...');
        await delay(8000);

        let isWorking = true;
        let checkCount = 0;
        const maxChecks = 35;

        while (isWorking && checkCount < maxChecks) {
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                const buttons = Array.from(document.querySelectorAll('button'));
                const hasStopBtn = buttons.some(b => b.textContent?.trim() === 'Dừng' || b.textContent?.trim() === 'Stop');
                return bodyText.includes('Thinking…') || bodyText.includes('Working…') || bodyText.includes('Đang xử lý') || hasStopBtn;
            });
            console.log(`AI đang cập nhật code bước 1... (Lần kiểm tra ${checkCount}) - Trạng thái: ${isWorking ? 'Đang chạy' : 'Đã hoàn tất'}`);
            await delay(5000);
        }

        console.log('AI đã cập nhật xong bước 1!');
        await delay(3000);

        // Chụp ảnh màn hình kết quả bước 1
        const screenshotPath = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/upgrade_step1_success.png');
        await flowPage.screenshot({ path: screenshotPath });
        console.log(`Đã lưu ảnh chụp màn hình kết quả bước 1 tại: ${screenshotPath}`);

        // Bấm nút "Xong" để áp dụng và lưu
        console.log('Bấm nút "Xong" để lưu...');
        const doneBtnCoords = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button, a, span'));
            const doneBtn = buttons.find(b => b.textContent?.trim() === 'Xong' || b.textContent?.trim() === 'Done');
            if (doneBtn) {
                const rect = doneBtn.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (doneBtnCoords) {
            await flowPage.mouse.click(doneBtnCoords.x, doneBtnCoords.y);
            await delay(4000);
            console.log('Đã lưu thành công bước 1!');
        }

    } catch (error) {
        console.error('Lỗi khi nâng cấp bước 1:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
