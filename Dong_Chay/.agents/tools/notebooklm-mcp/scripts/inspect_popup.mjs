/**
 * Script to inspect the Deep Research popup DOM in NotebookLM.
 * Uses the saved auth cookies from notebooklm-mcp.
 */
import { chromium } from 'patchright';
import { readFileSync, existsSync } from 'fs';
import { homedir } from 'os';
import path from 'path';

const NOTEBOOK_URL = 'https://notebooklm.google.com/notebook/bc481255-b22a-43a7-9678-c530fd3357fc?addSource=true';

// Find the chrome profile used by notebooklm-mcp
const profileDir = path.join(homedir(), '.notebooklm-mcp', 'chrome_profile');
const altProfileDir = path.join(homedir(), '.notebooklm-mcp-nodejs', 'chrome_profile');

let userDataDir = profileDir;
if (!existsSync(profileDir) && existsSync(altProfileDir)) {
  userDataDir = altProfileDir;
}

console.log(`Using profile: ${userDataDir}`);
console.log(`Profile exists: ${existsSync(userDataDir)}`);

async function main() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    headless: false,
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'],
    viewport: { width: 1920, height: 1080 },
  });

  const page = await context.newPage();
  console.log('Navigating to notebook...');
  await page.goto(NOTEBOOK_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });

  // Wait for page to stabilize
  await page.waitForTimeout(5000);

  // Take screenshot
  await page.screenshot({ path: '/tmp/nblm_popup_01_initial.png', fullPage: true });
  console.log('Screenshot 1 saved: /tmp/nblm_popup_01_initial.png');

  // Check if there's an overlay
  const overlayHTML = await page.evaluate(() => {
    const overlay = document.querySelector('.cdk-overlay-container');
    if (overlay) return overlay.innerHTML;
    return 'NO OVERLAY FOUND';
  });
  console.log('\n=== CDK OVERLAY CONTAINER HTML ===');
  console.log(overlayHTML);
  console.log('=== END OVERLAY ===\n');

  // Get all dialog/popup elements
  const dialogHTML = await page.evaluate(() => {
    const dialogs = document.querySelectorAll('[role="dialog"], mat-dialog-container, .cdk-overlay-pane');
    const results = [];
    dialogs.forEach((d, i) => {
      results.push(`--- Dialog ${i} ---`);
      results.push(`Tag: ${d.tagName}`);
      results.push(`Classes: ${d.className}`);
      results.push(`Role: ${d.getAttribute('role')}`);
      results.push(`InnerHTML (first 3000 chars): ${d.innerHTML.substring(0, 3000)}`);
    });
    return results.join('\n');
  });
  console.log('\n=== DIALOG ELEMENTS ===');
  console.log(dialogHTML);
  console.log('=== END DIALOGS ===\n');

  // Look for the dropdown (Web / Deep Research switcher)
  const dropdownInfo = await page.evaluate(() => {
    // Find anything that looks like a dropdown trigger
    const triggers = document.querySelectorAll(
      'mat-select, [role="listbox"], [role="combobox"], .mat-mdc-select, button[aria-haspopup], [matMenuTriggerFor], mat-menu, .source-type-selector, [class*="source-type"], [class*="research-type"], [class*="mode-selector"]'
    );
    const results = [];
    triggers.forEach((t, i) => {
      results.push(`--- Trigger ${i} ---`);
      results.push(`Tag: ${t.tagName}`);
      results.push(`Classes: ${t.className}`);
      results.push(`Text: ${t.textContent?.trim().substring(0, 200)}`);
      results.push(`OuterHTML: ${t.outerHTML.substring(0, 1500)}`);
    });
    return results.join('\n') || 'NO DROPDOWN TRIGGERS FOUND';
  });
  console.log('\n=== DROPDOWN TRIGGERS ===');
  console.log(dropdownInfo);
  console.log('=== END DROPDOWN ===\n');

  // Look for input/textarea inside the popup
  const inputInfo = await page.evaluate(() => {
    const overlay = document.querySelector('.cdk-overlay-container');
    if (!overlay) return 'NO OVERLAY';
    const inputs = overlay.querySelectorAll('input, textarea');
    const results = [];
    inputs.forEach((inp, i) => {
      results.push(`--- Input ${i} ---`);
      results.push(`Tag: ${inp.tagName}`);
      results.push(`Type: ${inp.getAttribute('type')}`);
      results.push(`Placeholder: ${inp.getAttribute('placeholder')}`);
      results.push(`AriaLabel: ${inp.getAttribute('aria-label')}`);
      results.push(`Classes: ${inp.className}`);
      results.push(`OuterHTML: ${inp.outerHTML.substring(0, 500)}`);
    });
    return results.join('\n') || 'NO INPUTS IN OVERLAY';
  });
  console.log('\n=== INPUTS IN OVERLAY ===');
  console.log(inputInfo);
  console.log('=== END INPUTS ===\n');

  // Look for buttons inside the popup
  const buttonInfo = await page.evaluate(() => {
    const overlay = document.querySelector('.cdk-overlay-container');
    if (!overlay) return 'NO OVERLAY';
    const buttons = overlay.querySelectorAll('button, [role="button"], .close-button, .mat-icon-button, [mat-icon-button], [matDialogClose]');
    const results = [];
    buttons.forEach((btn, i) => {
      results.push(`--- Button ${i} ---`);
      results.push(`Tag: ${btn.tagName}`);
      results.push(`Text: ${btn.textContent?.trim().substring(0, 200)}`);
      results.push(`AriaLabel: ${btn.getAttribute('aria-label')}`);
      results.push(`Classes: ${btn.className}`);
      results.push(`OuterHTML: ${btn.outerHTML.substring(0, 800)}`);
    });
    return results.join('\n') || 'NO BUTTONS IN OVERLAY';
  });
  console.log('\n=== BUTTONS IN OVERLAY ===');
  console.log(buttonInfo);
  console.log('=== END BUTTONS ===\n');

  // Try to find the "Deep Research" option or dropdown menu items
  const menuItemsInfo = await page.evaluate(() => {
    const allElements = document.querySelectorAll('*');
    const deepResearchEls = [];
    allElements.forEach(el => {
      const text = el.textContent?.trim();
      if (text && (text.includes('Deep Research') || text.includes('Nghiên cứu nhanh') || text.includes('Nghiên cứu sâu'))) {
        if (el.children.length <= 3) { // only leaf-ish nodes
          deepResearchEls.push({
            tag: el.tagName,
            classes: el.className,
            text: text.substring(0, 150),
            outerHTML: el.outerHTML.substring(0, 500),
            role: el.getAttribute('role'),
          });
        }
      }
    });
    return JSON.stringify(deepResearchEls, null, 2);
  });
  console.log('\n=== DEEP RESEARCH RELATED ELEMENTS ===');
  console.log(menuItemsInfo);
  console.log('=== END DEEP RESEARCH ===\n');

  // Now try clicking the dropdown to see options
  // First, try to find and click the "Web" or "Deep Research" dropdown trigger
  const clickableDropdown = await page.evaluate(() => {
    const overlay = document.querySelector('.cdk-overlay-container');
    if (!overlay) return null;
    // Look for mat-select or dropdown-like elements
    const selects = overlay.querySelectorAll('mat-select, [class*="select"], [class*="dropdown"], [class*="menu-trigger"]');
    const results = [];
    selects.forEach((s, i) => {
      results.push({
        index: i,
        tag: s.tagName,
        classes: s.className,
        text: s.textContent?.trim().substring(0, 100),
        outerHTML: s.outerHTML.substring(0, 500),
      });
    });
    return results;
  });
  console.log('\n=== CLICKABLE DROPDOWN CANDIDATES ===');
  console.log(JSON.stringify(clickableDropdown, null, 2));
  console.log('=== END CLICKABLE ===\n');

  // Wait a bit for user to see
  await page.waitForTimeout(3000);

  // Close gracefully
  await context.close();
  console.log('Done! Browser closed.');
}

main().catch(e => {
  console.error('Fatal error:', e);
  process.exit(1);
});
