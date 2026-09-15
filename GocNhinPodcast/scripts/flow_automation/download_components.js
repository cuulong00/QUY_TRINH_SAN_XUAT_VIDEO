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
        await flowPage.goto(toolUrl, { waitUntil: 'networkidle2' });
        await delay(6000);

        // Click "Chỉnh sửa" bằng selector CSS
        console.log('2. Click nút "Chỉnh sửa" ở trên cùng...');
        const clickedEdit = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            const editTab = elements.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                const rect = editTab.getBoundingClientRect();
                // Click DOM thô trước
                editTab.click();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (clickedEdit) {
            console.log(`Đã click "Chỉnh sửa" tại tọa độ: (${clickedEdit.x}, ${clickedEdit.y})`);
            // Click chuột vật lý dự phòng
            await flowPage.mouse.click(clickedEdit.x, clickedEdit.y);
            await delay(8000);
        } else {
            console.log('Không thấy nút Chỉnh sửa.');
        }

        // Chụp ảnh màn hình kiểm tra
        await flowPage.screenshot({ path: path.join(__dirname, 'step2_edit_mode.png') });

        // Click tab "Mã"
        console.log('3. Click tab "Mã"...');
        const clickedCode = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button'));
            const codeTab = elements.find(t => t.textContent?.trim() === 'Mã' || t.textContent?.trim() === 'Code');
            if (codeTab) {
                const rect = codeTab.getBoundingClientRect();
                codeTab.click();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (clickedCode) {
            console.log(`Đã click tab "Mã" tại tọa độ: (${clickedCode.x}, ${clickedCode.y})`);
            await flowPage.mouse.click(clickedCode.x, clickedCode.y);
            await delay(8000);
        } else {
            console.log('Không thấy tab Mã.');
        }

        // Chụp ảnh màn hình kiểm tra
        await flowPage.screenshot({ path: path.join(__dirname, 'step3_code_mode.png') });

        // Lấy tất cả text của danh sách tệp bên trái để in ra debug
        const fileListTexts = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('span, div, button'));
            // Lọc các phần tử ở bên trái màn hình
            return elements
                .filter(el => el.getBoundingClientRect().left < window.innerWidth * 0.4 && el.getBoundingClientRect().width > 0)
                .map(el => el.textContent?.trim() || '')
                .filter(t => t.endsWith('.tsx') || t.endsWith('.ts') || t.includes('Sidebar') || t.includes('Monitor') || t.includes('PromptTable'))
                .filter((v, i, a) => a.indexOf(v) === i);
        });
        console.log('Danh sách file thực tế trong DOM:', fileListTexts);

        // Tải 3 file components
        const filesToDownload = ['components/Sidebar.tsx', 'components/Monitor.tsx', 'components/PromptTable.tsx'];
        const outputDir = path.join(__dirname, 'src_download');

        for (const filename of filesToDownload) {
            console.log(`\n--- Đang tải: ${filename} ---`);
            
            // Tìm phần tử bằng cách quét qua danh sách file list text
            const fileCoords = await flowPage.evaluate((fname) => {
                const elements = Array.from(document.querySelectorAll('span, div, button'));
                const fileEl = elements.find(el => {
                    const rect = el.getBoundingClientRect();
                    const text = el.textContent?.trim() || '';
                    return rect.left < window.innerWidth * 0.4 && 
                           (text === fname || text.endsWith(fname) || fname.endsWith(text) || text.includes('Sidebar.tsx') && fname.includes('Sidebar'));
                });

                if (fileEl) {
                    const rect = fileEl.getBoundingClientRect();
                    return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2, text: fileEl.textContent?.trim() };
                }
                return null;
            }, filename);

            if (fileCoords) {
                console.log(`Click file "${filename}" (DOM text: "${fileCoords.text}") tại tọa độ: (${fileCoords.x}, ${fileCoords.y})`);
                await flowPage.mouse.click(fileCoords.x, fileCoords.y);
                await delay(4000); // Chờ code load

                // Lấy code từ thẻ PRE
                const fileContent = await flowPage.evaluate(() => {
                    const pre = document.querySelector('pre.prism-code');
                    return pre ? pre.textContent : null;
                });

                if (fileContent) {
                    const baseName = filename.split('/').pop();
                    const outPath = path.join(outputDir, baseName);
                    fs.writeFileSync(outPath, fileContent, 'utf8');
                    console.log(`Lưu thành công: ${outPath}`);
                } else {
                    console.error(`Không lấy được code của file: ${filename}`);
                }
            } else {
                console.warn(`Không tìm thấy file "${filename}" trong danh sách bên trái.`);
            }
        }

    } catch (error) {
        console.error('Lỗi critical:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
