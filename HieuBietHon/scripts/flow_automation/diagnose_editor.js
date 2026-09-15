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

        console.log('Diagnosing Slate Editor...');
        const result = await page.evaluate(() => {
            const el = document.querySelector('[role="textbox"][data-slate-editor="true"]');
            if (!el) return 'Textbox not found';
            
            // Focus it
            el.focus();
            
            const key = Object.keys(el).find(k => k.startsWith('__reactFiber'));
            if (!key) return 'React Fiber key not found';
            
            let fiber = el[key];
            let editor = null;
            while (fiber) {
              if (fiber.memoizedProps && fiber.memoizedProps.editor) {
                editor = fiber.memoizedProps.editor;
                break;
              }
              fiber = fiber.return;
            }
            
            if (!editor) return 'Editor not found in Fiber';
            
            // Log editor children
            const initialChildren = JSON.stringify(editor.children);
            
            // Try inserting text
            try {
                editor.selection = {
                  anchor: { path: [0, 0], offset: 0 },
                  focus: { path: [0, 0], offset: editor.children[0].children[0].text.length }
                };
                editor.deleteBackward('character');
                editor.insertText("HELLO_DIAGNOSTIC_WORLD");
            } catch (err) {
                return 'Error inserting: ' + err.message;
            }
            
            return {
                initialChildren,
                afterChildren: JSON.stringify(editor.children),
                innerText: el.innerText
            };
        });

        console.log('Result:', result);

    } catch (error) {
        console.error('Error:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
