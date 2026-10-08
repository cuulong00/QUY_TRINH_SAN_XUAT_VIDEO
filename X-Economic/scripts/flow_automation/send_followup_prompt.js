const puppeteer = require('puppeteer-core');
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
        const flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        if (!flowPage) {
            console.error('Không tìm thấy tab Google Flow nào đang mở.');
            return;
        }

        console.log(`Đang chạy trên tab: ${flowPage.url()}`);

        // Đảm bảo đang ở tab "Chỉnh sửa"
        console.log('Đang click tab "Chỉnh sửa" để mở Tool Builder...');
        await flowPage.evaluate(() => {
            const tabs = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = tabs.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                editTab.click();
            }
        });
        await delay(3000);

        // Định vị ô chat của Tool Builder (thanh bên phải)
        const chatInputSelector = 'div[data-slate-editor="true"][contenteditable="true"]';
        console.log('Đang tìm ô chat Tool Builder...');
        
        try {
            await flowPage.waitForSelector(chatInputSelector, { timeout: 10000 });
        } catch (e) {
            console.error('Không thấy ô chat Tool Builder.');
            return;
        }

        console.log('Đang focus vào ô chat...');
        await flowPage.click(chatInputSelector);
        await delay(500);

        // Xóa nội dung cũ trong ô chat
        await flowPage.keyboard.down('Meta');
        await flowPage.keyboard.press('A');
        await flowPage.keyboard.up('Meta');
        await flowPage.keyboard.press('Backspace');
        await delay(500);

        // Câu lệnh bổ sung yêu cầu hoàn thiện tính năng
        const followupPrompt = "Please update the UI in Sidebar.tsx and App.tsx: Add 'Select Video Model' (Veo 3.1, Veo 3.0) and 'Select Image Model' (Imagen 4, Imagen 3) dropdowns, and add the 'Set Project Destination Folder' button with File System Access API (window.showDirectoryPicker) in the Sidebar setup.";
        
        console.log('Đang gõ câu lệnh bổ sung...');
        await flowPage.keyboard.type(followupPrompt, { delay: 1 });
        await delay(1000);

        // Nhấn nút gửi prompt
        console.log('Đang nhấn nút gửi prompt...');
        const clickedSend = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            // Tìm nút gửi nằm trong phần Tool Builder bên phải
            let sendBtn = buttons.find(b => {
                const text = b.textContent?.trim() || '';
                return text === 'arrow_forward' || text.toLowerCase() === 'submit' || b.querySelector('i')?.textContent === 'arrow_forward';
            });

            if (!sendBtn) {
                sendBtn = buttons.find(b => b.innerHTML.includes('arrow') || b.getAttribute('aria-label')?.toLowerCase().includes('send'));
            }

            // Click nếu nút không disabled
            if (sendBtn && !sendBtn.disabled) {
                sendBtn.click();
                return true;
            }
            return false;
        });

        if (clickedSend) {
            console.log('Đã click nút gửi thành công!');
        } else {
            console.log('Nút gửi bị mờ hoặc không tìm thấy, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI cập nhật code (40 giây)...');
        
        // Chờ 40 giây để AI code lại các dropdown và folder picker
        let checkCount = 0;
        let isWorking = true;
        while (isWorking && checkCount < 8) {
            await delay(5000);
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                return bodyText.includes('Thinking…') || bodyText.includes('Working…') || bodyText.includes('Đang xử lý');
            });
            console.log(`Đang chờ AI lập trình... (Lần kiểm tra ${checkCount})`);
        }

        console.log('AI đã cập nhật xong code mới!');
        await delay(2000);

        // Chụp ảnh màn hình sau khi cập nhật
        const screenshotPath = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/after_followup_screen.png');
        await flowPage.screenshot({ path: screenshotPath });
        console.log(`Đã chụp ảnh màn hình sau cập nhật tại: ${screenshotPath}`);

    } catch (error) {
        console.error('Lỗi khi gửi prompt bổ sung:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
