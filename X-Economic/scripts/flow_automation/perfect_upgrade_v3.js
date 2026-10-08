const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function run() {
    let browser;
    try {
        console.log('Connecting to Chrome via CDP 9222...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        const pages = await browser.pages();
        let flowPage = pages.find(p => p.url().includes('labs.google/fx/tools/flow'));

        if (!flowPage) {
            console.error('Không tìm thấy tab Google Flow nào đang mở.');
            return;
        }

        const toolUrl = 'https://labs.google/fx/tools/flow/project/759075a7-9c26-43f4-8e47-c6a8ef8d5614/tool/bb118cac-48c5-47fb-84f8-aac2a0781bba';
        console.log(`1. Điều hướng tab tới Tool URL: ${toolUrl}`);
        await flowPage.goto(toolUrl, { waitUntil: 'domcontentloaded' });
        await delay(6000);

        // 2. Định vị tọa độ nút "Chỉnh sửa" ở trên cùng và click bằng chuột vật lý
        console.log('2. Tìm tọa độ nút "Chỉnh sửa"...');
        const editTabCoords = await flowPage.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, a, div[role="button"], span'));
            // Tìm đúng nút có chữ "Chỉnh sửa"
            const editTab = elements.find(t => t.textContent?.trim() === 'Chỉnh sửa');
            if (editTab) {
                const rect = editTab.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (editTabCoords) {
            console.log(`Click chuột vật lý vào nút "Chỉnh sửa" tại tọa độ: (${editTabCoords.x}, ${editTabCoords.y})`);
            await flowPage.mouse.click(editTabCoords.x, editTabCoords.y);
            await delay(6000); // Chờ giao diện chỉnh sửa nạp
        } else {
            console.warn('Không tìm thấy nút "Chỉnh sửa". Có thể đã ở trong Edit Mode.');
        }

        // 3. Định vị ô chat Tool Builder bên phải màn hình
        console.log('3. Tìm tọa độ ô chat Tool Builder bên phải...');
        const chatCoords = await flowPage.evaluate(() => {
            const editors = Array.from(document.querySelectorAll('div[data-slate-editor="true"][contenteditable="true"]'));
            // Lọc tìm editor ở nửa bên phải màn hình
            const toolBuilderEditor = editors.find(el => {
                const rect = el.getBoundingClientRect();
                return rect.left > window.innerWidth * 0.5;
            });

            if (toolBuilderEditor) {
                const rect = toolBuilderEditor.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
            }
            return null;
        });

        if (!chatCoords) {
            console.error('LỖI: Không tìm thấy ô chat Tool Builder bên phải màn hình.');
            await flowPage.screenshot({ path: path.join(__dirname, 'error_find_right_chat.png') });
            return;
        }

        console.log(`Click chuột vào ô chat Tool Builder tại tọa độ: (${chatCoords.x}, ${chatCoords.y})`);
        await flowPage.mouse.click(chatCoords.x, chatCoords.y);
        await delay(500);

        // Xóa nội dung cũ trong ô chat bằng selectAll + Backspace
        console.log('Đang xóa nội dung cũ trong ô chat...');
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

        // Đọc prompt nâng cấp v2
        const promptPath = path.join(__dirname, 'google_flow_advanced_vibe_prompt_v2.md');
        const promptContent = fs.readFileSync(promptPath, 'utf8').trim();

        // 4. Gõ prompt v2
        console.log('4. Gõ prompt nâng cấp v2 vào ô chat...');
        await flowPage.keyboard.type(promptContent, { delay: 0 });
        await delay(4000); // Đợi text nạp xong

        // 5. Định vị nút Gửi ("Tạo") của Tool Builder bên phải và click bằng chuột vật lý
        console.log('5. Tìm tọa độ nút Gửi ("Tạo") bên phải...');
        const sendBtnCoords = await flowPage.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            
            // Tìm nút ở bên phải màn hình chứa chữ "Tạo" hoặc icon arrow_forward (không phải arrow_forward_ios)
            const sendBtn = buttons.find(b => {
                const rect = b.getBoundingClientRect();
                const text = b.textContent?.trim() || '';
                return rect.left > window.innerWidth * 0.5 && 
                       (text.includes('Tạo') || text.includes('Generate') || (text.includes('arrow_forward') && !text.includes('arrow_forward_ios')));
            });

            if (sendBtn) {
                const rect = sendBtn.getBoundingClientRect();
                return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2, text: sendBtn.textContent?.trim() };
            }
            return null;
        });

        if (sendBtnCoords) {
            console.log(`Click chuột vào nút Gửi ("${sendBtnCoords.text}") tại tọa độ: (${sendBtnCoords.x}, ${sendBtnCoords.y})`);
            await flowPage.mouse.click(sendBtnCoords.x, sendBtnCoords.y);
        } else {
            console.log('Không tìm thấy nút gửi bằng tọa độ, giả lập nhấn phím Enter...');
            await flowPage.keyboard.press('Enter');
        }

        console.log('Đang chờ AI bắt đầu cập nhật code...');
        await delay(8000);

        // 6. Theo dõi tiến trình AI lập trình
        let isWorking = true;
        let checkCount = 0;
        const maxChecks = 35; // 35 * 5s = 175s

        while (isWorking && checkCount < maxChecks) {
            checkCount++;
            isWorking = await flowPage.evaluate(() => {
                const bodyText = document.body.innerText;
                // AI Tool Builder tiếng Việt thường hiển thị "Thinking..." hoặc "Đang cập nhật..." trong panel bên phải
                // Ngoài ra, khi đang cập nhật thì có nút "Dừng" (Stop) hiển thị.
                const buttons = Array.from(document.querySelectorAll('button'));
                const hasStopBtn = buttons.some(b => b.textContent?.trim() === 'Dừng' || b.textContent?.trim() === 'Stop');
                
                return bodyText.includes('Thinking…') || 
                       bodyText.includes('Working…') || 
                       bodyText.includes('Đang xử lý') || 
                       bodyText.includes('Đang cập nhật') ||
                       hasStopBtn;
            });
            console.log(`AI đang cập nhật code... (Lần kiểm tra ${checkCount}) - Trạng thái: ${isWorking ? 'Đang chạy' : 'Đã hoàn tất'}`);
            
            if (checkCount === 1) {
                await flowPage.screenshot({ path: path.join(__dirname, 'actual_upgrade_progress.png') });
            }
            
            await delay(5000);
        }

        console.log('AI đã lập trình nâng cấp xong!');
        await delay(3000);

        // Chụp ảnh màn hình Edit Mode hoàn thành
        const completeEditScreenshot = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/edit_complete_screen.png');
        await flowPage.screenshot({ path: completeEditScreenshot });
        console.log(`Đã lưu ảnh màn hình Edit Mode hoàn thành tại: ${completeEditScreenshot}`);

        // 7. Click nút "Xong" bằng chuột vật lý để lưu và chạy giao diện mới
        console.log('7. Tìm tọa độ nút "Xong" để lưu...');
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
            console.log(`Click chuột vào nút "Xong" tại tọa độ: (${doneBtnCoords.x}, ${doneBtnCoords.y})`);
            await flowPage.mouse.click(doneBtnCoords.x, doneBtnCoords.y);
            await delay(4000);
        } else {
            console.warn('Không tìm thấy nút "Xong" bằng tọa độ.');
        }

        // Chụp ảnh màn hình Tool Mode sau cùng
        const finalScreenshot = path.resolve('/Users/pro16/.gemini/antigravity/brain/98676974-b36c-4473-904a-ca038cc18ff4/final_tool_v2_success.png');
        await flowPage.screenshot({ path: finalScreenshot });
        console.log(`Đã lưu ảnh màn hình giao diện ứng dụng v2 mới tại: ${finalScreenshot}`);
        console.log('Hoàn tất quy trình nâng cấp 100%!');

    } catch (error) {
        console.error('Lỗi critical:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
