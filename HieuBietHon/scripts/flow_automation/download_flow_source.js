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

        console.log(`1. Điều hướng tới URL của Tool: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(6000);

        // Click "Chỉnh sửa" bằng chuột vật lý để vào Edit Mode
        console.log('2. Chuyển sang tab Chỉnh sửa...');
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
        }

        // Chờ danh sách file xuất hiện (ví dụ tìm phần tử chứa text App.tsx ở bên trái)
        console.log('3. Chờ danh sách file xuất hiện...');
        await flowPage.waitForFunction(() => {
            return Array.from(document.querySelectorAll('*')).some(el => el.textContent?.trim() === 'App.tsx');
        }, { timeout: 15000 });

        // Danh sách các file cần tải
        const targetFiles = ['types.ts', 'App.tsx', 'components/Sidebar.tsx', 'components/Monitor.tsx', 'components/PromptTable.tsx'];
        const outputDir = path.join(__dirname, 'src_download');
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        for (const filename of targetFiles) {
            console.log(`\n--- Tải file: ${filename} ---`);
            
            // Tìm và click vào tên file ở danh sách bên trái bằng tọa độ
            const fileCoords = await flowPage.evaluate((fname) => {
                // Tách phần tên file cuối cùng (ví dụ components/Sidebar.tsx -> Sidebar.tsx)
                const baseName = fname.split('/').pop();
                const elements = Array.from(document.querySelectorAll('span, div, button'));
                
                // Lọc tìm phần tử ở nửa bên trái màn hình có chữ trùng với baseName
                const fileEl = elements.find(el => {
                    const rect = el.getBoundingClientRect();
                    return rect.left < window.innerWidth * 0.4 && el.textContent?.trim() === baseName;
                });

                if (fileEl) {
                    const rect = fileEl.getBoundingClientRect();
                    return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
                }
                return null;
            }, filename);

            if (fileCoords) {
                console.log(`Click chuột vật lý vào file "${filename}" tại tọa độ: (${fileCoords.x}, ${fileCoords.y})`);
                await flowPage.mouse.click(fileCoords.x, fileCoords.y);
                await delay(3000); // Chờ code nạp vào Monaco Editor

                // Lấy nội dung code từ Monaco Editor
                const fileContent = await flowPage.evaluate(() => {
                    // Trích xuất qua Monaco API nếu có
                    if (window.monaco && window.monaco.editor) {
                        const models = window.monaco.editor.getModels();
                        if (models && models.length > 0) {
                            // Trả về model đang active hoặc model khớp với URI/tên
                            return models[0].getValue();
                        }
                    }
                    // Fallback: Lấy text từ container Monaco
                    const editorContainer = document.querySelector('.monaco-editor');
                    if (editorContainer) {
                        // Monaco hiển thị text qua class view-line
                        const lines = Array.from(editorContainer.querySelectorAll('.view-line'));
                        if (lines.length > 0) {
                            return lines.map(l => l.textContent || '').join('\n');
                        }
                        return editorContainer.innerText;
                    }
                    return null;
                });

                if (fileContent) {
                    const outPath = path.join(outputDir, filename.replace(/\//g, '_'));
                    fs.writeFileSync(outPath, fileContent, 'utf8');
                    console.log(`Đã tải và lưu file code thành công tại: ${outPath}`);
                } else {
                    console.error(`Không thể trích xuất nội dung code của file: ${filename}`);
                }
            } else {
                console.warn(`Không tìm thấy file: ${filename} trong danh sách bên trái.`);
            }
        }

        console.log('\nĐã tải xong toàn bộ mã nguồn khảo sát!');

    } catch (error) {
        console.error('Lỗi khi tải mã nguồn:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
