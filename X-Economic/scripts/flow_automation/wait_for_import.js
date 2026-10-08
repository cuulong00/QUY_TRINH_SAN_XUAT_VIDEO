const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const delay = ms => new Promise(r => setTimeout(r, ms));

async function main() {
    let browser;
    try {
        console.log('Connecting to existing Chrome via CDP on port 9222...');
        // Wait! The MCP server is running on its own profile, but wait! Does it expose CDP?
        // Ah! The MCP server doesn't expose CDP by default unless we connect to it, or wait!
        // The MCP server's browser instance was launched by patchright. Does it have remote debugging enabled?
        // Let's check if there is an active CDP port on localhost.
        const response = await fetch('http://localhost:9222/json/version').catch(() => null);
        if (!response) {
            console.log('CDP port 9222 is not open. We need to check if there are other ports or launch Chrome with debugging.');
            // Wait, let's check what ports are open.
            // Actually, we can run a Puppeteer script that launches a browser pointing to the same profile path!
            // Let's see: the profile path is '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile'.
            // If the MCP server is currently running, we cannot launch another Puppeteer instance on the same profile
            // because of the profile lock!
            // But wait! If the MCP server is running, we can just write a script that connects to the browser
            // if it was launched with debugging.
            // Let's check if the MCP server has a debugging port.
        }
        
        // Let's run a command to find the remote debugging port of the running Chrome helper/renderer.
        // Wait, did we see any process with --remote-debugging-port in our previous ps aux output?
        // Yes, PID 3553 had --remote-debugging-port=9222, but that was for 'antigravity-browser-profile'.
        // PID 38030 ('notebooklm-mcp/chrome_profile') did NOT have --remote-debugging-port!
        // Oh! If the MCP server's browser does not have remote-debugging-port enabled,
        // then we cannot connect to it via CDP.
        // But wait! If we cannot connect to it via CDP, how can we make the MCP server wait or click it?
        // Ah! If we call `deep_research` again on the MCP server, it will connect to the existing session
        // (if it is still alive), and if it sees the Import button is already visible, or if it waits for it,
        // will it click it?
        // Let's look at `tryClickImport` in `deep-researcher.ts`:
        // Yes! At line 108:
        // const importResult = await this.tryClickImport(sourcesBefore);
        // If it is visible, it clicks it.
        // But wait! In our case, the import button was NOT visible yet because the search was still running (step 2/5).
        // And `deep_research` failed at `switchToDeepResearch()` because it tried to switch to Deep Research mode
        // BEFORE waiting or checking if a research was already in progress!
        // Ah!!!
        // Look at the code in `performDeepResearch`:
        // Line 108: `const importResult = await this.tryClickImport(sourcesBefore);`
        // Line 118: `await this.switchToDeepResearch();`
        // If `tryClickImport` returns null (because the Import button is NOT visible yet since it's still running step 2/5),
        // it goes to `switchToDeepResearch()`.
        // And `switchToDeepResearch()` fails because the research menu trigger is disabled or hidden during active research!
        // That is the bug in the MCP server's `deep_research` tool!
        // If a research is already in progress (e.g. `Đã hoàn tất bước 2/5`), the tool should NOT try to switch to Deep Research mode.
        // Instead, it should wait for the active research to finish (i.e. wait for the Import button to appear),
        // click it, and then proceed!
        // Let's modify `deep-researcher.ts` (or `deep-researcher.js` in dist) to handle this case!
        
    } catch (e) {
        console.error('Error:', e);
    }
}

main();
