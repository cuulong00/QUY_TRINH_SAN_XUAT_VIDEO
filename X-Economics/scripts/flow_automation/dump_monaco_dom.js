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
            console.log('Mở tab mới...');
            flowPage = await browser.newPage();
        }

        console.log(`1. Điều hướng tới URL: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(5000);

        // Click "Chỉnh sửa" bằng chuột vật lý để vào Edit Mode
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
            console.log('Đã click "Chỉnh sửa". Chờ 6 giây...');
            await delay(6000);
        }

        // Click tab "Mã"
        console.log('3. Click tab "Mã" để mở trình xem code...');
        const codeTabCoords = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button'));
            const codeTab = elements.find(t => t.textContent?.trim() === 'Mã' || t.textContent?.trim() === 'Code');
            if (codeTab) {
                const rect = codeTab.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (codeTabCoords) {
            await flowPage.mouse.click(codeTabCoords.x, codeTabCoords.y);
            console.log('Đã click tab "Mã". Chờ 4 giây...');
            await delay(4000);
        } else {
            console.error('LỖI: Không tìm thấy nút "Mã". Dừng script.');
            return;
        }

        // Chờ editor load
        await delay(3000);

        // Dump toàn bộ DOM của trang tab Mã để xem Monaco Editor được render ra sao
        const domDump = await flowPage.evaluate(() => {
            // Lấy tất cả elements chứa văn bản
            return Array.from(document.querySelectorAll('.view-line, pre, code, textarea, [class*="editor"]'))
                .map(el => ({
                    tagName: el.tagName,
                    className: el.className,
                    text: el.textContent?.trim() || '',
                    id: el.id,
                    html: el.outerHTML.substring(0, 500)
                }));
        });

        fs.writeFileSync(
            path.join(__dirname, 'monaco_dom_dump.json'),
            JSON.stringify(domDump, null, 2),
            'utf8'
        );
        console.log('Đã dump DOM tab Mã xong!');

    } catch (error) {
        console.error('Lỗi khi dump Monaco editor DOM:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
