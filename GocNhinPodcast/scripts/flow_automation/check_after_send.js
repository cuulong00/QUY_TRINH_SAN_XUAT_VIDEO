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

        console.log('Listing tiles on dashboard...');
        const tiles = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('[data-tile-id]')).map(card => {
                const textNodes = [];
                const walk = document.createTreeWalker(card, NodeFilter.SHOW_TEXT, null, false);
                let node;
                while (node = walk.nextNode()) {
                    textNodes.push(node.nodeValue.trim());
                }
                const progressNode = textNodes.find(n => /^\d+%$/.test(n));
                const queueNode = textNodes.find(n => n === 'Đang trong hàng đợi' || n === 'In queue');
                
                let status = 'completed/unknown';
                if (queueNode) status = 'queued';
                else if (progressNode) status = `generating (${progressNode})`;
                
                // Check for failure
                const error = textNodes.some(n => n === 'Không thành công' || n === 'Failed');
                if (error) status = 'failed';
                
                return {
                    id: card.getAttribute('data-tile-id'),
                    status: status,
                    text: textNodes.filter(Boolean).slice(0, 3).join(' | ')
                };
            });
        });
        
        console.log('Found tiles:', tiles);

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
