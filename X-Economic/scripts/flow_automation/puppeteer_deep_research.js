const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function runResearch(page, query) {
    console.log(`\n--- Starting Deep Research for: "${query}" ---`);
    try {
        console.log('Navigating to NotebookLM...');
        await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'domcontentloaded' });
        await delay(5000);
        
        // Click Add source
        console.log('Looking for Add Source button...');
        await page.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const addBtn = btns.find(b => {
                const txt = b.textContent?.toLowerCase() || '';
                const aria = b.getAttribute('aria-label')?.toLowerCase() || '';
                return txt.includes('add source') || txt.includes('thêm nguồn') || aria.includes('add source') || aria.includes('thêm nguồn');
            });
            if (addBtn) addBtn.click();
        });
        await delay(3000);
        
        // Click Deep Research
        console.log('Looking for Deep Research option...');
        await page.evaluate(() => {
            const elements = Array.from(document.querySelectorAll('button, span, div'));
            const el = elements.find(b => {
                const txt = b.textContent?.toLowerCase() || '';
                return txt.includes('deep research') || txt.includes('nghiên cứu sâu') || txt.includes('nghiên cứu nhanh');
            });
            if (el) el.click();
        });
        await delay(3000);
        
        // Type query
        console.log('Entering query...');
        const textareaSelector = 'textarea[placeholder*="Research"], textarea[placeholder*="nghiên cứu" i], textarea[placeholder*="nhanh"], .cdk-overlay-pane textarea';
        await page.waitForSelector(textareaSelector, { timeout: 8000 });
        await page.click(textareaSelector);
        
        // Clear and type
        await page.keyboard.down('Meta');
        await page.keyboard.press('A');
        await page.keyboard.up('Meta');
        await page.keyboard.press('Backspace');
        await page.keyboard.type(query, { delay: 1 });
        await delay(1000);
        
        // Click Submit
        console.log('Clicking Submit button...');
        await page.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('.cdk-overlay-pane button, [role="dialog"] button, button.actions-enter-button'));
            const submitBtn = btns.find(b => {
                const txt = b.textContent?.toLowerCase() || '';
                return txt.includes('nghiên cứu') || txt.includes('research') || b.classList.contains('actions-enter-button');
            });
            if (submitBtn) {
                submitBtn.click();
            } else {
                // Try pressing enter
                console.log('Submit button not found, will press Enter key.');
            }
        });
        
        // Try pressing Enter key as backup
        await page.keyboard.press('Enter');
        
        console.log('Waiting 15 seconds to ensure research submission is registered...');
        await delay(15000);
        console.log('Research submitted.');
        return true;
    } catch (err) {
        console.error('Error during research submission:', err.message);
        // Take debug screenshot
        try {
            await page.screenshot({ path: path.join(__dirname, `debug_research_error_${Date.now()}.png`) });
        } catch (screenshotErr) {
            console.error('Failed to take screenshot:', screenshotErr.message);
        }
        return false;
    }
}

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
        
        const queries = [
            "VinFast India strategy, Tamil Nadu plant build progress, export targets, RHD markets Sri Lanka, Nepal, Mauritius, Middle East, Africa",
            "Green SM India Delhi launch June 2026, Green SM Limo Delhi, rebranding of Xanh SM to Green SM in April 2026, ride-hailing expansion in Delhi, Bengaluru",
            "Gensol and BluSmart scandal: Jaggi brothers SEBI ban in April 2025, ED asset attachment in January 2026, diversion of ₹262 crore",
            "Vingroup transferring 182,000 billion VND in factory debt to Công ty Tương Lai in May 2026, leaseback OEM model of VinFast",
            "Indonesian police VF 3 EV deployment: Korlantas Polri modified VF 3s as mobile bases for ETLE drone patrols"
        ];
        
        for (let i = 0; i < queries.length; i++) {
            const query = queries[i];
            console.log(`\n--- Query ${i + 1}/${queries.length} ---`);
            const success = await runResearch(page, query);
            if (!success) {
                console.error(`Failed at query: ${query}`);
            }
            await delay(3000);
        }
        
        console.log('\nAll research submissions finished! Closing tab...');
        await page.close();
        
    } catch (error) {
        console.error('CRITICAL ERROR during automation:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
