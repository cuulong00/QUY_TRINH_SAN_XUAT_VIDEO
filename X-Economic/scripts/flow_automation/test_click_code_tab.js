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
            flowPage = await browser.newPage();
        }

        console.log(`Điều hướng tới URL: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(5000);

        // Click "Chỉnh sửa"
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
            console.log('Chờ 6 giây...');
            await delay(6000);
        }

        // Tìm tất cả phần tử trong DOM có text liên quan đến "Mã", "Xem trước", "Code", "Preview"
        const candidates = await flowPage.evaluate(() => {
            const allElements = Array.from(document.querySelectorAll('*'));
            return allElements
                .map(el => {
                    const text = el.textContent?.trim() || '';
                    const rect = el.getBoundingClientRect();
                    return {
                        tagName: el.tagName,
                        text: text.substring(0, 100),
                        id: el.id,
                        className: el.className,
                        rect: { left: rect.left, top: rect.top, width: rect.width, height: rect.height }
                    };
                })
                .filter(c => {
                    const t = c.text.toLowerCase();
                    return (t === 'mã' || t === 'code' || t === 'xem trước' || t === 'preview') && c.rect.width > 0;
                });
        });

        console.log('Các phần tử khả nghi tìm thấy:');
        console.log(JSON.stringify(candidates, null, 2));

    } catch (error) {
        console.error('Lỗi:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
