const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

async function main() {
    try {
        console.log('Connecting to existing Chrome via CDP on port 9222...');
        const response = await fetch('http://localhost:9222/json/version');
        const data = await response.json();
        const webSocketDebuggerUrl = data.webSocketDebuggerUrl;

        const browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            defaultViewport: null
        });

        console.log('Connected!');
        const pages = await browser.pages();
        // Find existing notebook page or open new
        let page = pages.find(p => p.url().includes('notebooklm.google.com'));
        if (!page) {
            console.log('No NotebookLM page open, opening a new tab...');
            page = await browser.newPage();
            await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'domcontentloaded' });
        } else {
            console.log('Found active NotebookLM page:', page.url());
            // Bring to front
            await page.bringToFront();
        }

        // Wait a bit
        await new Promise(r => setTimeout(r, 3000));

        // Dump button details
        const elementsInfo = await page.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, [role="button"], a, [class*="button"], [id*="button"]'));
            return elements.map(el => {
                return {
                    tagName: el.tagName,
                    text: el.textContent?.trim() || '',
                    id: el.id || '',
                    className: el.className || '',
                    ariaLabel: el.getAttribute('aria-label') || '',
                    outerHTML: el.outerHTML.substring(0, 200)
                };
            });
        });

        console.log(`Found ${elementsInfo.length} button/interactive elements:`);
        fs.writeFileSync(path.join(__dirname, 'dom_buttons.json'), JSON.stringify(elementsInfo, null, 2));
        console.log('Saved to dom_buttons.json');

        // Let's also search for "thêm" or "nguồn" or "add" or "source" across ALL elements
        const matchedElements = await page.evaluate(() => {
            const all = Array.from(document.querySelectorAll('*'));
            return all
                .filter(el => {
                    const txt = el.textContent?.toLowerCase() || '';
                    return (txt.includes('nguồn') || txt.includes('source') || txt.includes('thêm') || txt.includes('add')) && el.children.length === 0;
                })
                .map(el => ({
                    tagName: el.tagName,
                    text: el.textContent?.trim() || '',
                    className: el.className || '',
                    parentTagName: el.parentElement?.tagName || '',
                    parentClassName: el.parentElement?.className || '',
                    parentHTML: el.parentElement?.outerHTML.substring(0, 300)
                }));
        });
        fs.writeFileSync(path.join(__dirname, 'matched_elements.json'), JSON.stringify(matchedElements, null, 2));
        console.log(`Saved ${matchedElements.length} matching text elements to matched_elements.json`);

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e);
    }
}

main();
