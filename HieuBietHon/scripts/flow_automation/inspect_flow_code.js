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
            console.log('Không tìm thấy tab Google Flow. Đang mở tab mới...');
            flowPage = await browser.newPage();
        }

        console.log(`Điều hướng tới URL của Tool: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(5000);

        // Chụp ảnh màn hình hiện tại trước khi click
        await flowPage.screenshot({ path: path.join(__dirname, 'before_inspect_code.png') });

        // Tìm tọa độ nút "Mã" ở trên cùng và click
        console.log('Tìm tọa độ nút "Mã"...');
        const codeTabCoords = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const codeTab = elements.find(t => t.textContent?.trim() === 'Mã' || t.textContent?.trim() === 'Code');
            if (codeTab) {
                const rect = codeTab.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (codeTabCoords) {
            console.log(`Click chuột vào nút "Mã" tại tọa độ: (${codeTabCoords.x}, ${codeTabCoords.y})`);
            await flowPage.mouse.click(codeTabCoords.x, codeTabCoords.y);
            await delay(4000);
        } else {
            console.warn('Không tìm thấy nút "Mã".');
        }

        // Chụp ảnh màn hình tab Mã
        await flowPage.screenshot({ path: path.join(__dirname, 'code_tab_screen.png') });

        // Inspect cấu trúc danh sách file ở bên trái tab Mã để tìm code
        console.log('Đang trích xuất mã nguồn ứng dụng hiện tại từ DOM...');
        const sourceCodeData = await flowPage.evaluate(() => {
            // Thử tìm các phần tử chứa code hoặc tên file
            const fileElements = Array.from(document.querySelectorAll('div, span, button'));
            const files = fileElements
                .map(el => el.textContent?.trim() || '')
                .filter(txt => txt.endsWith('.tsx') || txt.endsWith('.ts') || txt.endsWith('.css') || txt.endsWith('.json'))
                .filter((v, i, a) => a.indexOf(v) === i); // Unique

            // Lấy toàn bộ text của vùng hiển thị code (thường là editor Monaco hoặc thẻ pre/code)
            const codeContainer = document.querySelector('pre, code, .monaco-editor, [role="code"]');
            const visibleCode = codeContainer ? codeContainer.innerText : 'Không tìm thấy container hiển thị code trực tiếp';

            return {
                visibleFiles: files,
                visibleCodeSnippet: visibleCode.substring(0, 3000)
            };
        });

        console.log('Danh sách các file code nhìn thấy trên màn hình:', sourceCodeData.visibleFiles);
        console.log('--- ĐOẠN CODE ĐANG HIỂN THỊ ---');
        console.log(sourceCodeData.visibleCodeSnippet);
        console.log('-------------------------------');

        // Lưu thông tin inspect
        fs.writeFileSync(
            path.join(__dirname, 'inspect_result.json'),
            JSON.stringify(sourceCodeData, null, 2),
            'utf8'
        );

    } catch (error) {
        console.error('Lỗi khi inspect code:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
