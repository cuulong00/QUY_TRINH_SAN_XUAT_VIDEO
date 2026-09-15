/**
 * Diagnostic script: Dump the DOM of the NotebookLM popup overlay
 * Run with: node scripts/dump_overlay_dom.mjs
 */
import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

const NOTEBOOK_URL = 'https://notebooklm.google.com/notebook/bc481255-b22a-43a7-9678-c530fd3357fc';
const PROFILE_DIR = path.join(process.env.HOME || '', 'Library/Application Support/notebooklm-mcp/chrome_profile');

async function main() {
  console.log('🚀 Launching browser...');
  console.log(`  Profile: ${PROFILE_DIR}`);

  const context = await chromium.launchPersistentContext(PROFILE_DIR, {
    headless: false,
    args: [
      '--disable-blink-features=AutomationControlled',
      '--no-sandbox',
    ],
    viewport: { width: 1280, height: 900 },
  });

  const page = context.pages()[0] || await context.newPage();

  console.log('📄 Navigating to notebook...');
  await page.goto(NOTEBOOK_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  console.log('✅ Page loaded');

  // Wait a few seconds for popup to appear
  await page.waitForTimeout(5000);

  // Dump 1: Check for overlay backdrop
  const hasOverlay = await page.locator('.cdk-overlay-backdrop.cdk-overlay-backdrop-showing').isVisible().catch(() => false);
  console.log(`\n🔍 Overlay backdrop visible: ${hasOverlay}`);

  // Dump 2: All content inside cdk-overlay-container
  const overlayHTML = await page.evaluate(() => {
    const container = document.querySelector('.cdk-overlay-container');
    if (!container) return 'NO .cdk-overlay-container found';
    return container.innerHTML;
  });
  
  console.log('\n📋 === OVERLAY CONTAINER HTML ===');
  console.log(overlayHTML.substring(0, 5000));

  // Dump 3: All visible inputs on page
  const inputs = await page.evaluate(() => {
    const allInputs = Array.from(document.querySelectorAll('input, textarea'));
    return allInputs.map(el => ({
      tag: el.tagName,
      type: el.getAttribute('type'),
      placeholder: el.getAttribute('placeholder'),
      class: el.className.substring(0, 80),
      visible: el.offsetParent !== null,
      value: el.value?.substring(0, 50),
    }));
  });
  
  console.log('\n📋 === ALL INPUTS ===');
  console.log(JSON.stringify(inputs, null, 2));

  // Dump 4: All buttons inside overlay pane
  const overlayButtons = await page.evaluate(() => {
    const pane = document.querySelector('.cdk-overlay-pane');
    if (!pane) return 'NO .cdk-overlay-pane found';
    const buttons = Array.from(pane.querySelectorAll('button'));
    return buttons.map(btn => ({
      text: btn.textContent?.trim().substring(0, 100),
      class: btn.className.substring(0, 80),
      ariaLabel: btn.getAttribute('aria-label'),
      disabled: btn.disabled,
    }));
  });
  
  console.log('\n📋 === BUTTONS INSIDE OVERLAY PANE ===');
  console.log(JSON.stringify(overlayButtons, null, 2));

  // Dump 5: The search/input area within overlay
  const searchArea = await page.evaluate(() => {
    const pane = document.querySelector('.cdk-overlay-pane');
    if (!pane) return 'NO .cdk-overlay-pane found';
    
    // Look for the search-related section
    const searchInputs = Array.from(pane.querySelectorAll('input, textarea, [contenteditable]'));
    return searchInputs.map(el => ({
      tag: el.tagName,
      type: el.getAttribute('type'),
      placeholder: el.getAttribute('placeholder'),
      class: el.className.substring(0, 100),
      role: el.getAttribute('role'),
      ariaLabel: el.getAttribute('aria-label'),
      contentEditable: el.getAttribute('contenteditable'),
      value: el.value?.substring(0, 50),
      visible: el.offsetParent !== null,
    }));
  });
  
  console.log('\n📋 === INPUTS INSIDE OVERLAY PANE ===');
  console.log(JSON.stringify(searchArea, null, 2));

  // Save full overlay HTML to file
  const outputPath = path.join(process.cwd(), 'overlay_dump.html');
  fs.writeFileSync(outputPath, overlayHTML);
  console.log(`\n💾 Full overlay HTML saved to: ${outputPath}`);

  // Take screenshot
  const screenshotPath = path.join(process.cwd(), 'overlay_screenshot.png');
  await page.screenshot({ path: screenshotPath });
  console.log(`📸 Screenshot saved to: ${screenshotPath}`);

  // Keep browser open for 10 seconds for manual inspection
  console.log('\n⏳ Keeping browser open for 10s for inspection...');
  await page.waitForTimeout(10000);

  await context.close();
  console.log('✅ Done');
}

main().catch(console.error);
