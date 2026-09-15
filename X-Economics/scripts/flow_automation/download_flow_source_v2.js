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

        // Click "Chỉnh sửa" bằng chuột vật lý
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

        // Chờ Monaco Editor xuất hiện
        console.log('4. Chờ Monaco Editor xuất hiện...');
        await flowPage.waitForSelector('.monaco-editor', { timeout: 15000 });

        // Tải các file
        const filesToDownload = ['types.ts', 'App.tsx', 'Sidebar.tsx', 'Monitor.tsx', 'PromptTable.tsx'];
        const outputDir = path.join(__dirname, 'src_download');
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        for (const filename of filesToDownload) {
            console.log(`\n--- Đang tải: ${filename} ---`);
            
            // Tìm và click vào tên file ở cột trái
            const fileCoords = await flowPage.evaluate((fname) => {
                const elements = Array.from(document.querySelectorAll('span, div, button'));
                // Lọc tìm phần tử ở nửa bên trái màn hình có chữ trùng với tên file
                const fileEl = elements.find(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.left < window.innerWidth * 0.4 && el.textContent?.trim() === fname;
                });

                if (fileEl) {
                    const rect = fileEl.getBoundingClientRect();
                    return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
                }
                return null;
            }, filename);

            if (fileCoords) {
                console.log(`Click file "${filename}" tại tọa độ: (${fileCoords.x}, ${fileCoords.y})`);
                await flowPage.mouse.click(fileCoords.x, fileCoords.y);
                await delay(2500); // Chờ code load xong

                // Lấy nội dung code từ DOM của Monaco Editor
                const fileContent = await flowPage.evaluate(() => {
                    const editor = document.querySelector('.monaco-editor');
                    if (editor) {
                        const lines = Array.from(editor.querySelectorAll('.view-line'));
                        return lines.map(l => l.textContent || '').join('\n');
                    }
                    return null;
                });

                if (fileContent) {
                    const outPath = path.join(outputDir, filename.replace(/\//g, '_'));
                    fs.writeFileSync(outPath, fileContent, 'utf8');
                    console.log(`Lưu file code thành công: ${outPath}`);
                } else {
                    console.error(`Không thể lấy code của: ${filename}`);
                }
            } else {
                console.warn(`Không tìm thấy file "${filename}" ở danh sách bên trái.`);
            }
        }

        console.log('\nTải mã nguồn thành công!');

    } catch (error) {
        console.error('Lỗi critical:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
