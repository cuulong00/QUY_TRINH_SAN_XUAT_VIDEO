const puppeteer = require('puppeteer-core');

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
            await new Promise(r => setTimeout(r, 6000));
        } else {
            console.log('Found open notebook page:', page.url());
            await page.bringToFront();
        }

        const accountInfo = await page.evaluate(() => {
            // Let's find Google account avatar button or profile element
            const avatar = document.querySelector('a[href*="SignOutOptions"], [aria-label*="Google Account"], [aria-label*="Tài khoản Google"], [class*="gb_A"], [class*="gb_B"], img[src*="googleusercontent"]');
            
            return {
                avatarHTML: avatar ? avatar.outerHTML : null,
                ariaLabel: avatar ? avatar.getAttribute('aria-label') : null,
                src: avatar && avatar.tagName === 'IMG' ? avatar.src : (avatar ? avatar.querySelector('img')?.src : null),
                href: avatar ? avatar.getAttribute('href') : null
            };
        });

        console.log('\nAccount Element info:', JSON.stringify(accountInfo, null, 2));

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
