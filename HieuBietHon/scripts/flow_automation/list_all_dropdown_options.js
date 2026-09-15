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

        console.log('Opening settings menu...');
        const settingsBtn = await page.evaluateHandle(() => {
            return Array.from(document.querySelectorAll('button')).find(btn => 
              btn.getAttribute('aria-haspopup') === 'menu' && 
              (btn.innerText && btn.innerText.includes('Banana'))
            );
        });

        if (!settingsBtn) {
            console.log('Settings button not found!');
            return;
        }

        await settingsBtn.asElement().click();
        await new Promise(r => setTimeout(r, 1000));

        console.log('Clicking the model selector dropdown...');
        const dropdownBtn = await page.evaluateHandle(() => {
            return Array.from(document.querySelectorAll('button, [role="button"]')).find(b => 
              b.innerText && b.innerText.includes('Banana') && b.innerText.includes('arrow_drop_down')
            );
        });

        if (!dropdownBtn) {
            console.log('Dropdown button not found!');
            // Close settings
            await page.keyboard.press('Escape');
            return;
        }

        await dropdownBtn.asElement().click();
        await new Promise(r => setTimeout(r, 1000));

        console.log('Listing dropdown options...');
        const options = await page.evaluate(() => {
            // Dropdowns are often rendered in a portal at the body level
            const items = Array.from(document.querySelectorAll('[role="option"], [role="menuitem"], button'));
            return items.map(i => i.innerText).filter(Boolean);
        });

        console.log('Dropdown options:', options);

        // Escape twice to close everything
        await page.keyboard.press('Escape');
        await new Promise(r => setTimeout(r, 500));
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
