const puppeteer = require('puppeteer-core');
const path = require('path');

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

        console.log(`Tìm thấy tab Google Flow! URL: ${flowPage.url()}`);
        console.log(`Tiêu đề: ${await flowPage.title()}`);

        // Chụp ảnh màn hình toàn bộ trang và lưu vào thư mục artifacts của session
        const screenshotPath = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/current_flow_screen.png');
        await flowPage.screenshot({ path: screenshotPath, fullPage: false });
        console.log(`Đã chụp và lưu ảnh chụp màn hình tại: ${screenshotPath}`);

        // Quét nhanh các nút nổi bật trên trang hiện tại
        const elements = await flowPage.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button, a, div[role="button"]'));
            return btns.map(b => b.textContent?.trim() || '').filter(t => t.length > 0 && t.length < 50);
        });
        console.log('Các nút bấm hiện có trên màn hình:', elements);

    } catch (error) {
        console.error('Lỗi khi chụp màn hình:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
