const puppeteer = require('puppeteer-core');

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

        console.log('Locating submit button natively...');
        const submitBtn = await page.evaluateHandle(() => {
            return Array.from(document.querySelectorAll('button')).find(btn => 
              btn.innerText && btn.innerText.includes('arrow_forward') && btn.innerText.includes('Tạo')
            );
        });
        
        const el = submitBtn ? submitBtn.asElement() : null;
        if (!el) {
            console.log('Submit button not found!');
            return;
        }

        console.log('Submit button found. HTML:', await page.evaluate(b => b.outerHTML, el));
        
        // Take screenshot before click
        const scratchDir = '/Users/pro16/Documents/VideoProject/X-Economics/scratch';
        await page.screenshot({ path: `${scratchDir}/before_send_prompt.png` });
        console.log('Screenshot before click saved.');

        console.log('Clicking natively...');
        await el.hover();
        await new Promise(r => setTimeout(r, 200));
        await el.click();
        
        console.log('Clicked! Waiting 5 seconds...');
        await new Promise(r => setTimeout(r, 5000));
        
        await page.screenshot({ path: `${scratchDir}/after_send_prompt.png` });
        console.log('Screenshot after click saved.');

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
