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

        console.log('Opening settings menu...');
        // Find settings button
        const settingsBtn = await page.evaluateHandle(() => {
            return Array.from(document.querySelectorAll('button')).find(btn => 
              btn.getAttribute('aria-haspopup') === 'menu' && 
              (btn.innerText && (
                btn.innerText.includes('Video') || 
                btn.innerText.includes('Hình ảnh') || 
                btn.innerText.includes('Banana') || 
                btn.innerText.includes('Veo') || 
                btn.innerText.includes('Omni') || 
                btn.innerText.includes('Imagen')
              ))
            );
        });

        if (!settingsBtn) {
            console.log('Settings button not found!');
            return;
        }

        const el = settingsBtn.asElement();
        await el.hover();
        await new Promise(r => setTimeout(r, 200));
        await el.click();
        await new Promise(r => setTimeout(r, 1000));

        console.log('Switching to Image tab in settings (just in case)...');
        await page.evaluate(() => {
            const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
            const imageTab = tabs.find(t => t.innerText && t.innerText.includes('Hình ảnh') && !t.innerText.includes('Xem'));
            if (imageTab) imageTab.click();
        });
        await new Promise(r => setTimeout(r, 1000));

        console.log('Clicking model dropdown menu...');
        await page.evaluate(() => {
            const dropdown = Array.from(document.querySelectorAll('button, [role="button"]')).find(b => 
              b.innerText && (b.innerText.includes('Veo') || b.innerText.includes('Omni') || b.innerText.includes('Banana') || b.innerText.includes('Imagen'))
            );
            if (dropdown) dropdown.click();
        });
        await new Promise(r => setTimeout(r, 1000));

        console.log('Listing available image models in menu...');
        const models = await page.evaluate(() => {
            const options = Array.from(document.querySelectorAll('[role="option"], [role="menuitem"], button'));
            return options.map(o => o.innerText).filter(Boolean);
        });

        console.log('Models found:', models);

        // Escape to close settings
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
