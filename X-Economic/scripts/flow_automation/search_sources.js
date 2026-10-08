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
            console.log('No active NotebookLM page found.');
            return;
        }

        const sourceTexts = await page.evaluate(() => {
            const elList = Array.from(document.querySelectorAll('.single-source-container, [class*="source-card"], [class*="source-item"]'));
            return elList.map(el => el.innerText || '');
        });

        const keywords = ['indonesia', 'polri', 'police', 'vf 3', 'green sm', 'delhi', 'gensol', 'blusmart', 'tương lai', 'nợ'];
        console.log(`\nAnalyzing ${sourceTexts.length} elements for keywords:`);
        
        const matched = {};
        keywords.forEach(k => matched[k] = []);

        sourceTexts.forEach(text => {
            keywords.forEach(k => {
                if (text.toLowerCase().includes(k)) {
                    matched[k].push(text.replace(/\s+/g, ' ').trim());
                }
            });
        });

        keywords.forEach(k => {
            console.log(`\nKeyword: "${k}" -> Found ${matched[k].length} matches:`);
            matched[k].slice(0, 5).forEach((m, idx) => console.log(`  [${idx+1}] ${m.substring(0, 150)}`));
            if (matched[k].length > 5) console.log(`  ... and ${matched[k].length - 5} more`);
        });

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
