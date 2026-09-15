const puppeteer = require('puppeteer-core');
const fs = require('fs');

async function main() {
    let browser;
    try {
        console.log('Connecting...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes('labs.google') && p.url().includes('tools/flow'));
        if (!page) {
            console.log('No Flow page found!');
            return;
        }

        console.log('Opening Add Media dialog...');
        const addBtnHandle = await page.evaluateHandle(() => {
            const textbox = document.querySelector('[role="textbox"]');
            if (!textbox) return null;
            const container = textbox.closest('div.sc-26b30722-0, div.sc-c9e4708a-0');
            return container ? container.querySelector('button[aria-haspopup="dialog"]') : null;
        });

        const addBtn = addBtnHandle ? addBtnHandle.asElement() : null;
        if (!addBtn) {
            console.log('Add Media button not found!');
            return;
        }

        await addBtn.click();
        await new Promise(r => setTimeout(r, 2000));

        console.log('Inspecting dialog buttons...');
        const dialogInfo = await page.evaluate(() => {
            const dialog = document.querySelector('[role="dialog"]');
            if (!dialog) return { error: 'Dialog not found' };
            
            const buttons = Array.from(dialog.querySelectorAll('button')).map(btn => ({
                text: btn.innerText || btn.textContent,
                outerHTML: btn.outerHTML
            }));
            
            return {
                buttons,
                outerHTML: dialog.outerHTML.substring(0, 5000)
            };
        });

        fs.writeFileSync('/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/dialog_debug.json', JSON.stringify(dialogInfo, null, 2));
        console.log('Dialog debug info saved to dialog_debug.json');

        // Click first option to see if dialog closes
        console.log('Clicking the first option in dialog...');
        const clickedOption = await page.evaluate(() => {
            const dialog = document.querySelector('[role="dialog"]');
            if (!dialog) return false;
            const option = dialog.querySelector('[role="option"]');
            if (option) {
                option.click();
                return true;
            }
            return false;
        });
        
        await new Promise(r => setTimeout(r, 2000));
        
        const dialogAfterClick = await page.evaluate(() => {
            return !!document.querySelector('[role="dialog"]');
        });
        
        console.log(`Is dialog still open after clicking option? ${dialogAfterClick}`);

        if (dialogAfterClick) {
            // Escape to close
            await page.keyboard.press('Escape');
        }

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
