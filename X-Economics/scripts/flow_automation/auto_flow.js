const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function run() {
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

        // Read the prompts
        const promptsPath = path.join(__dirname, '..', '..', 'episodes', 'hon-loan-trump-2', 'flow_veo3_prompts_all.txt');
        const content = fs.readFileSync(promptsPath, 'utf8');
        const allPrompts = content.split('\n\n').map(p => p.trim()).filter(p => p);
        
        // Take just the first 3 prompts for the test
        const testPrompts = allPrompts.slice(0, 3);

        const page = await browser.newPage();
        
        // Grant clipboard read/write permissions
        await browser.defaultBrowserContext().overridePermissions('https://labs.google', ['clipboard-read', 'clipboard-write']);

        for (let i = 0; i < testPrompts.length; i++) {
            const prompt = testPrompts[i];
            console.log(`\n--- Processing Prompt ${i + 1}/3 ---`);
            
            console.log('Loading Flow Home...');
            await page.goto('https://labs.google/fx/vi/tools/flow', { waitUntil: 'domcontentloaded' });
            await delay(4000);

            // 1. Create New Project (if present)
            await page.evaluate(() => {
                const btns = Array.from(document.querySelectorAll('button'));
                const newProject = btns.find(b => {
                    const txt = b.textContent?.toLowerCase() || '';
                    return txt.includes('dự án mới') || txt.includes('new project') || txt.includes('create with flow');
                });
                if (newProject) {
                    newProject.click();
                }
            });
            await delay(3000);

            // 2. Ensure Model is set to Nano Banana Pro and Outputs = 1
            console.log('Setting model to Nano Banana Pro and output to 1...');
            await page.evaluate(async () => {
                const buttons = Array.from(document.querySelectorAll('button'));
                const modelBtn = buttons.find(b => b.textContent && b.textContent.toLowerCase().includes('nano banana'));
                if (modelBtn) {
                    modelBtn.click();
                    await new Promise(r => setTimeout(r, 1000));
                    
                    // Look for 'x1' or '1'
                    const menuItems = Array.from(document.querySelectorAll('div[role="option"], div[role="menuitem"], button'));
                    const x1Option = menuItems.find(el => el.textContent === '1' || el.textContent === 'x1');
                    if (x1Option) x1Option.click();
                    
                    await new Promise(r => setTimeout(r, 500));
                    document.body.click(); // Close menu
                }
            });
            await delay(1000);

            // 3. Type Prompt via Clipboard
            console.log('Entering prompt...');
            const editorSelector = 'div[data-slate-editor="true"][contenteditable="true"], textarea[placeholder*="tạo gì"]';
            await page.waitForSelector(editorSelector, { timeout: 10000 });
            await page.click(editorSelector);
            
            // Clear existing if any
            await page.keyboard.down('Meta');
            await page.keyboard.press('A');
            await page.keyboard.up('Meta');
            await page.keyboard.press('Backspace');
            await delay(200);

            // Inject payload using keyboard
            await page.keyboard.type(prompt, { delay: 1 });
            await delay(1000);

            // 4. Click Generate
            console.log('Clicking Generate...');
            const clickGenerate = await page.evaluate(() => {
                const btns = Array.from(document.querySelectorAll('button'));
                
                // Priority 1: Match the exact Google Material icon "arrow_forward"
                let sendBtn = btns.find(b => {
                    const icons = Array.from(b.querySelectorAll('i'));
                    return icons.some(i => i.textContent.trim() === 'arrow_forward');
                });
                
                // Priority 2: Match the visually hidden span text exact "Tạo"
                if (!sendBtn) {
                    sendBtn = btns.find(b => {
                        const spans = Array.from(b.querySelectorAll('span'));
                        return spans.some(s => s.textContent.trim() === 'Tạo');
                    });
                }
                
                if (sendBtn && !sendBtn.disabled) {
                    sendBtn.click();
                    return true;
                }
                return false;
            });
            
            if (!clickGenerate) {
                console.error('Failed to find or click generate button!');
                continue;
            }

            // 5. Wait for generation to complete
            console.log('Waiting for generation (may take up to 120s)...');
            try {
                // Catch any immediate SPA navigation side-effects that destroy the Execution Context
                try {
                    await page.waitForNavigation({ waitUntil: 'domcontentloaded', timeout: 5000 });
                } catch (navErr) {
                    // Ignore timeout if it doesn't navigate
                }

                // Wait until the "Tải xuống" button appears in the DOM
                await page.waitForFunction(() => {
                    const btns = Array.from(document.querySelectorAll('button'));
                    return btns.some(b => b.textContent && (b.textContent.includes('Tải xuống') || b.textContent.toLowerCase().includes('download')));
                }, { timeout: 120000, polling: 3000 });
                console.log('Generation completed!');
            } catch (err) {
                console.log('Timeout/Error waiting for generation to finish:', err.message);
                await page.screenshot({ path: path.join(__dirname, `debug_flow_p${i}.png`) });
                continue;
            }
            await delay(2000);

            // 6. Click Download
            console.log('Clicking Download...');
            await page.evaluate(() => {
                const btns = Array.from(document.querySelectorAll('button'));
                const downloadBtn = btns.find(b => b.textContent && (b.textContent.includes('Tải xuống') || b.textContent.toLowerCase().includes('download')));
                if (downloadBtn) downloadBtn.click();
            });

            console.log('Download initiated. Waiting 5 seconds before next iteration...');
            await delay(7000); 
        }

        console.log('\n--- Script completed successfully! ---');
        
        // Clean up: close the automation page so the user doesn't end up with 10 tabs
        await page.close();

    } catch (error) {
        console.error('CRITICAL ERROR during automation:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

run();
