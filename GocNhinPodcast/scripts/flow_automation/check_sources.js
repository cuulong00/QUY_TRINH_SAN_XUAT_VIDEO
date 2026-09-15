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
        const page = await browser.newPage();
        
        console.log('Navigating to NotebookLM...');
        await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'domcontentloaded' });
        await new Promise(r => setTimeout(r, 8000)); // wait for sources to load
        
        const sources = await page.evaluate(() => {
            // Find all source items
            const sourceElements = Array.from(document.querySelectorAll('.single-source-container, [class*="source-card"], [class*="source-item"]'));
            return sourceElements.map(el => el.textContent?.trim() || '');
        });
        
        console.log(`\nFound ${sources.length} sources:`);
        sources.forEach((s, i) => {
            if (i < 20 || i >= sources.length - 10) {
                console.log(`- [${i+1}] ${s.substring(0, 100)}`);
            } else if (i === 20) {
                console.log(`... [skipped ${sources.length - 30} sources] ...`);
            }
        });

        // Let's also check if there is an active Deep Research query running or an Import button visible
        const pageText = await page.evaluate(() => document.body.innerText);
        const importVisible = await page.evaluate(() => {
            const btn = document.querySelector('button.source-discovery-completed-action-import-button');
            return btn ? btn.outerHTML : null;
        });

        console.log('\n--- Page State ---');
        console.log('Import button visible:', !!importVisible);
        if (importVisible) console.log('Import button HTML:', importVisible);
        
        const hasStepText = pageText.includes('hoàn tất bước') || pageText.includes('completed step') || pageText.includes('bước') || pageText.includes('Deep Research');
        console.log('Deep Research text present in body:', hasStepText);

        await page.close();
    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
