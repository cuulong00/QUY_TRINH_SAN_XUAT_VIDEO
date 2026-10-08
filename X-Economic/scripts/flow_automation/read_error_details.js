const puppeteer = require('puppeteer-core');

async function main() {
    let browser;
    try {
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

        const fullErrorText = await page.evaluate(() => {
            const card = document.querySelector('[data-tile-id="fe_id_ad88aedf-a834-4b45-98e7-3054d19d9977"]');
            return card ? card.innerText : 'Card not found';
        });
        
        console.log('--- FULL ERROR TEXT ---');
        console.log(fullErrorText);
        console.log('----------------------');

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
