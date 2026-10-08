const puppeteer = require('puppeteer-core');
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
        let page = pages.find(p => p.url().includes('notebooklm.google.com'));
        if (!page) {
            console.log('No active NotebookLM page found, opening one...');
            page = await browser.newPage();
            await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'domcontentloaded' });
            await new Promise(r => setTimeout(r, 8000));
        } else {
            console.log('Found open notebook page:', page.url());
            await page.bringToFront();
        }

        const screenshotPath = '/Users/pro16/.gemini/antigravity-ide/brain/b1580520-fb13-4399-ab9f-f66427ca1149/nblm_current_state.png';
        await page.screenshot({ path: screenshotPath });
        console.log('Screenshot saved to:', screenshotPath);

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
