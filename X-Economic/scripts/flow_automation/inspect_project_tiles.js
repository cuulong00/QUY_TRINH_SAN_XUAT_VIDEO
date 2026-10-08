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

        console.log('Reading all tiles from DOM...');
        const tiles = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('[data-tile-id]')).map(card => {
                const textNodes = [];
                const walk = document.createTreeWalker(card, NodeFilter.SHOW_TEXT, null, false);
                let node;
                while (node = walk.nextNode()) {
                    textNodes.push(node.nodeValue.trim());
                }
                
                const hasVideo = !!card.querySelector('video');
                const hasImg = !!card.querySelector('img');
                
                return {
                    id: card.getAttribute('data-tile-id'),
                    hasVideo,
                    hasImg,
                    text: textNodes.filter(Boolean).join(' | ')
                };
            });
        });

        console.log('Tiles found in current project:');
        console.log(JSON.stringify(tiles, null, 2));

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
