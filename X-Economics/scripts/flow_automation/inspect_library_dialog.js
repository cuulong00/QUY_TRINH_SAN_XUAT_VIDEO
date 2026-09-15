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
        const addBtn = await page.evaluateHandle(() => {
            const textbox = document.querySelector('[role="textbox"]');
            if (!textbox) return null;
            const container = textbox.closest('div.sc-26b30722-0, div.sc-c9e4708a-0');
            return container ? container.querySelector('button[aria-haspopup="dialog"]') : null;
        });

        if (!addBtn) {
            console.log('Add Media button not found!');
            return;
        }

        await addBtn.asElement().click();
        await new Promise(r => setTimeout(r, 2000));

        console.log('Inspecting dialog options...');
        const optionsHTML = await page.evaluate(() => {
            const dialog = document.querySelector('[role="dialog"]');
            if (!dialog) return 'Dialog not found';
            
            const options = Array.from(dialog.querySelectorAll('[role="option"]'));
            return options.map(o => ({
                innerText: o.innerText,
                outerHTML: o.outerHTML.substring(0, 1000), // first 1000 chars of HTML
                ariaLabel: o.getAttribute('aria-label'),
                title: o.getAttribute('title')
            }));
        });

        console.log('Options found:');
        console.log(JSON.stringify(optionsHTML, null, 2));

        // Escape to close dialog
        await page.keyboard.press('Escape');

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
