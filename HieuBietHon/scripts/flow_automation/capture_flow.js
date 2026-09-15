const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

async function main() {
    let browser;
    try {
        console.log('Connecting to existing Chrome via CDP on port 9222...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        console.log('Connected to Chrome!');
        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes('labs.google') && p.url().includes('tools/flow'));
        if (!page) {
            console.log('No active Google Flow page found!');
            return;
        }
        
        console.log('Found open Flow page:', page.url());
        await page.bringToFront();

        const scratchDir = '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch';
        if (!fs.existsSync(scratchDir)) fs.mkdirSync(scratchDir, { recursive: true });
        
        const screenshotPath = path.join(scratchDir, 'flow_state.png');
        await page.screenshot({ path: screenshotPath });
        console.log('Screenshot saved to:', screenshotPath);

        // Inspect the page DOM for the submit button and input box
        const debugInfo = await page.evaluate(() => {
            const textbox = document.querySelector('[role="textbox"]');
            const buttons = Array.from(document.querySelectorAll('button'));
            
            const btnDetails = buttons.map((b, idx) => ({
                index: idx,
                text: b.innerText ? b.innerText.trim().replace(/\n/g, ' ') : '',
                html: b.outerHTML.substring(0, 300),
                disabled: b.disabled || b.getAttribute('aria-disabled') === 'true'
            }));
            
            return {
                textboxExists: !!textbox,
                textboxHtml: textbox ? textbox.outerHTML.substring(0, 300) : null,
                buttonsCount: buttons.length,
                buttons: btnDetails
            };
        });

        fs.writeFileSync(
            path.join(scratchDir, 'flow_dom_debug.json'),
            JSON.stringify(debugInfo, null, 2),
            'utf8'
        );
        console.log('DOM debug info saved to flow_dom_debug.json');

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
