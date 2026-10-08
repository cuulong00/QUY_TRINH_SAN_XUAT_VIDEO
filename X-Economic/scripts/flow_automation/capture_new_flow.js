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

        console.log('Capturing new flow state...');
        const scratchDir = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch';
        await page.screenshot({ path: `${scratchDir}/new_flow_state.png` });
        console.log('Screenshot saved to new_flow_state.png');

        // Extract DOM nodes
        const domData = await page.evaluate(() => {
            const buttons = Array.from(document.querySelectorAll('button')).map(btn => ({
                text: btn.innerText,
                disabled: btn.disabled,
                ariaDisabled: btn.getAttribute('aria-disabled'),
                outerHTML: btn.outerHTML
            }));
            const textboxes = Array.from(document.querySelectorAll('[role="textbox"]')).map(tb => ({
                outerHTML: tb.outerHTML,
                innerText: tb.innerText
            }));
            return {
                url: window.location.href,
                buttons,
                textboxes
            };
        });

        fs.writeFileSync(`${scratchDir}/new_flow_dom.json`, JSON.stringify(domData, null, 2));
        console.log('DOM data saved to new_flow_dom.json');

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
