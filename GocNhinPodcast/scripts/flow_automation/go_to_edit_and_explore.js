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

        // Đảm bảo đang ở URL của tool
        console.log(`Đang chạy trên tab: ${flowPage.url()}`);

        // Click nút "Chỉnh sửa" ở trên cùng
        console.log('Đang click nút "Chỉnh sửa" ở trên cùng...');
        await flowPage.evaluate(() => {
            const tabs = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = tabs.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                editTab.click();
            }
        });

        console.log('Đang chờ giao diện chỉnh sửa nạp (8 giây)...');
        await delay(8000);

        // Chụp ảnh màn hình Edit Mode
        const screenshotPath = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/edit_mode_screen.png');
        await flowPage.screenshot({ path: screenshotPath });
        console.log(`Đã chụp ảnh màn hình Edit Mode tại: ${screenshotPath}`);

        // In ra danh sách tất cả các placeholder và thuộc tính của các ô input/editor trên trang
        const inputsInfo = await flowPage.evaluate(() => {
            const editors = Array.from(document.querySelectorAll('div[contenteditable="true"], textarea, input'));
            return editors.map(el => ({
                tagName: el.tagName,
                placeholder: el.getAttribute('placeholder') || '',
                className: el.className,
                id: el.id,
                dataSlate: el.getAttribute('data-slate-editor') || '',
                innerTextPreview: el.textContent?.slice(0, 100) || ''
            }));
        });

        console.log('Các ô nhập liệu được tìm thấy:');
        console.log(JSON.stringify(inputsInfo, null, 2));

    } catch (error) {
        console.error('Lỗi khi khám phá Edit Mode:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
