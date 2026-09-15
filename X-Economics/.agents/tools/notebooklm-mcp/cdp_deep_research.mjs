import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

// Helper to wait
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Helper to take a screenshot and save it
async function takeScreenshot(page, name) {
  const screenshotPath = `/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch/${name}_${Date.now()}.png`;
  try {
    await page.screenshot({ path: screenshotPath });
    console.log(`[Screenshot] Saved: ${screenshotPath}`);
  } catch (err) {
    console.error(`[Screenshot] Failed to save screenshot: ${err.message}`);
  }
}

// Find or open the NotebookLM tab
async function getNotebookPage(browser) {
  const notebookId = '9891a2f0-8e48-445a-a2c4-4b25ee3c3800';
  let page;
  
  for (const ctx of browser.contexts()) {
    const found = ctx.pages().find(p => p.url().includes(notebookId));
    if (found) {
      page = found;
      console.log('Reusing existing NotebookLM tab:', page.url());
      break;
    }
  }
  
  if (!page) {
    console.log('NotebookLM tab not found. Opening a new tab...');
    // Create page on the first context
    const contexts = browser.contexts();
    if (contexts.length === 0) {
      throw new Error('No active browser contexts found!');
    }
    page = await contexts[0].newPage();
    await page.goto(`https://notebooklm.google.com/notebook/${notebookId}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
    console.log('Navigated, waiting for page to load main elements...');
    try {
      await page.waitForSelector('button[aria-label="Add source"], button:has-text("Thêm nguồn"), button:has-text("Add source")', { timeout: 30000 });
      console.log('Opened NotebookLM tab successfully (Add Source button is visible).');
    } catch (e) {
      console.log('Timeout waiting for Add Source button, but continuing anyway...');
    }
  }
  
  await page.bringToFront();
  return page;
}

// Click the Import/Nhập button if it is visible, and wait for it to disappear
async function clickImportIfPresent(page) {
  const importButtons = [
    page.locator('button:has-text("+ Nhập")'),
    page.locator('button:has-text("Nhập")'),
    page.locator('button:has-text("+ Import")'),
    page.locator('button:has-text("Import")')
  ];

  for (const locator of importButtons) {
    try {
      if (await locator.isVisible({ timeout: 2000 })) {
        console.log('Found Import/Nhập button. Clicking...');
        await locator.click({ force: true });
        console.log('Clicked Import/Nhập. Waiting 10 seconds for import to process...');
        await delay(10000);
        
        // Wait for the card to disappear from the sidebar
        console.log('Waiting for the completed research card to disappear...');
        const cardSelectors = [
          'text=Đã hoàn tất Deep Research!',
          'text=Đã hoàn tất Nghiên cứu nhanh!',
          'text=Deep Research complete',
          'text=Fast Research complete'
        ];
        
        for (let j = 0; j < 8; j++) { // Wait up to 40s
          let cardVisible = false;
          for (const selector of cardSelectors) {
            if (await page.locator(selector).first().isVisible({ timeout: 1000 })) {
              cardVisible = true;
              break;
            }
          }
          if (!cardVisible) {
            console.log('Completed card disappeared successfully.');
            break;
          }
          console.log(`Completed card is still visible, waiting 5s... (attempt ${j + 1}/8)`);
          await delay(5000);
        }
        return true;
      }
    } catch {}
  }
  return false;
}

// Wait for the Deep Research progress/spinner to finish and show the Import button
async function waitForResearchToComplete(page, maxWaitMins = 10) {
  console.log('Waiting for Deep Research to complete...');
  const checkInterval = 10000; // 10 seconds
  const maxIterations = (maxWaitMins * 60 * 1000) / checkInterval;
  
  for (let i = 0; i < maxIterations; i++) {
    // Check if Import button is visible
    const imported = await clickImportIfPresent(page);
    if (imported) {
      console.log('Deep Research completed and imported successfully.');
      return true;
    }
    
    // Check if there's any active spinner or "Planning" text
    const spinnerTexts = [
      'Vui lòng ở lại trang này',
      'Please stay on this page'
    ];
    
    let isRunning = false;
    for (const text of spinnerTexts) {
      if (await page.locator(`text=${text}`).first().isVisible({ timeout: 1000 })) {
        isRunning = true;
        break;
      }
    }
    
    if (isRunning) {
      console.log(`[Status] Research is in progress... (elapsed: ${((i * checkInterval) / 1000).toFixed(0)}s)`);
    } else {
      console.log('[Status] No active spinner detected. Checking if we need to check again...');
    }
    
    await delay(checkInterval);
  }
  
  console.error('Timeout: Deep Research did not complete within the maximum wait time.');
  await takeScreenshot(page, 'deep_research_timeout');
  return false;
}

// Submit a new Deep Research query (Robust non-recursive implementation)
async function submitQuery(page, query) {
  console.log(`\n--- Submitting Query: "${query}" ---`);
  
  for (let attempt = 1; attempt <= 5; attempt++) {
    console.log(`Submission attempt ${attempt}/5...`);
    
    // First, check if there's a modal open. Dismiss it by pressing Escape.
    await page.keyboard.press('Escape');
    await delay(1000);
    await page.keyboard.press('Escape');
    await delay(2000);
    
    // Click "Add source" (Thêm nguồn)
    console.log('Looking for Add Source / Thêm nguồn button...');
    let foundAddSource = false;
    const addSourceSelectors = [
      'button[aria-label="Add source"]',
      'button[aria-label*="Add source" i]',
      'button:has-text("Thêm nguồn")',
      'button:has-text("Add source")'
    ];
    for (const selector of addSourceSelectors) {
      try {
        const btn = page.locator(selector).first();
        if (await btn.isVisible({ timeout: 2000 })) {
          await btn.click({ force: true });
          console.log('Clicked Add Source.');
          foundAddSource = true;
          break;
        }
      } catch {}
    }
    
    await delay(2000);
    
    // Click "Deep Research" / "Nghiên cứu nhanh"
    console.log('Looking for Deep Research option...');
    let foundDeep = false;
    const deepTypeSelectors = [
      'button:has-text("Deep Research")',
      'button:has-text("Nghiên cứu sâu")',
      'button:has-text("Nghiên cứu nhanh")',
      'span:has-text("Deep Research")',
      'span:has-text("Nghiên cứu sâu")',
      'span:has-text("Nghiên cứu nhanh")'
    ];
    for (const selector of deepTypeSelectors) {
      try {
        const btn = page.locator(selector).first();
        if (await btn.isVisible({ timeout: 2000 })) {
          await btn.click({ force: true });
          console.log('Clicked Deep Research option.');
          foundDeep = true;
          break;
        }
      } catch {}
    }
    
    if (!foundDeep) {
      console.log('Deep Research option not found, retrying...');
      continue;
    }
    
    await delay(2000);
    
    // Look for textarea
    console.log('Looking for input textarea...');
    const inputSelectors = [
      '[role="dialog"] textarea',
      '.cdk-overlay-pane textarea',
      '.mat-mdc-dialog-container textarea',
      'textarea[placeholder*="Research"]',
      'textarea[placeholder*="nghiên cứu" i]',
      'textarea[placeholder*="nhanh"]',
      'input[placeholder*="Research"]'
    ];
    let textarea;
    for (const selector of inputSelectors) {
      try {
        const el = page.locator(selector).first();
        if (await el.isVisible({ timeout: 2000 })) {
          textarea = el;
          console.log('Found textarea.');
          break;
        }
      } catch {}
    }
    
    if (!textarea) {
      console.log('Textarea not found, retrying...');
      continue;
    }
    
    const isDisabled = await textarea.getAttribute('disabled');
    const isReadOnly = await textarea.getAttribute('readonly');
    
    if (isDisabled || isReadOnly) {
      console.log('Textarea is disabled. Dismissing dialog to clean up...');
      await page.keyboard.press('Escape');
      await delay(2000);
      
      // Check for pending import
      const imported = await clickImportIfPresent(page);
      if (imported) {
        console.log('Import triggered. Waiting 15s before next attempt...');
        await delay(15000);
      } else {
        console.log('No pending import found, checking if background research is running...');
        const completed = await waitForResearchToComplete(page, 3); // Wait up to 3 minutes
        if (completed) {
          console.log('Background research finished and imported. Waiting 10s...');
          await delay(10000);
        } else {
          console.log('No active/completed research found, but input is still disabled. Waiting 15s...');
          await delay(15000);
        }
      }
      continue;
    }
    
    // Input is enabled! Type query
    await textarea.click({ force: true });
    await textarea.fill('');
    await delay(500);
    await textarea.fill(query);
    await delay(500);
    await textarea.evaluate((el, q) => {
      el.value = q;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }, query);
    
    console.log('Query typed successfully. Submitting...');
    await takeScreenshot(page, `query_typed_${attempt}`);
    
    // Click Submit
    const submitSelectors = [
      '[role="dialog"] button.actions-enter-button',
      '.cdk-overlay-pane button.actions-enter-button',
      '[role="dialog"] button:has-text("Nghiên cứu")',
      '[role="dialog"] button:has-text("Research")',
      'button:has-text("Nghiên cứu nhanh")',
      'button:has-text("Deep Research")'
    ];
    
    let submitted = false;
    for (const sel of submitSelectors) {
      try {
        const btn = page.locator(sel).first();
        if (await btn.isVisible({ timeout: 1000 }) && !(await btn.getAttribute('disabled'))) {
          await btn.click({ force: true });
          console.log('Clicked submit button.');
          submitted = true;
          break;
        }
      } catch {}
    }
    
    if (!submitted) {
      console.log('Submit button not clickable, trying Enter key...');
      await textarea.focus();
      await page.keyboard.press('Enter');
      submitted = true;
    }
    
    console.log('Waiting 15 seconds to let the submission register...');
    await delay(15000);
    await takeScreenshot(page, 'after_submit');
    return true;
  }
  
  console.error('Failed to submit query after 5 attempts.');
  return false;
}

async function main() {
  console.log('Connecting to existing Chrome via CDP on port 9222...');
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  console.log('Connected successfully!');
  
  try {
    const page = await getNotebookPage(browser);
    
    // List of queries to run
    const queries = [
      "Gensol and BluSmart scandal: Jaggi brothers SEBI ban in April 2025, ED asset attachment in January 2026, diversion of ₹262 crore",
      "Vingroup transferring 182,000 billion VND in factory debt to Công ty Tương Lai in May 2026, leaseback OEM model of VinFast",
      "Indonesian police VF 3 EV deployment: Korlantas Polri modified VF 3s as mobile bases for ETLE drone patrols"
    ];
    
    // First, check if there's any pending research result waiting to be imported
    console.log('Checking for any leftover pending imports...');
    await clickImportIfPresent(page);
    
    // Check if a research is already running in background
    console.log('Checking if a research is already running in background...');
    const spinnerTexts = ['Vui lòng ở lại trang này', 'Please stay on this page'];
    let running = false;
    for (const text of spinnerTexts) {
      if (await page.locator(`text=${text}`).first().isVisible({ timeout: 1000 })) {
        running = true;
        break;
      }
    }
    if (running) {
      console.log('A background research is already running. Waiting for it to finish first...');
      await waitForResearchToComplete(page, 10);
    }
    
    // Execute all queries sequentially
    for (let i = 0; i < queries.length; i++) {
      const q = queries[i];
      console.log(`\n========================================`);
      console.log(`Processing query ${i + 1}/${queries.length}`);
      console.log(`========================================`);
      
      const success = await submitQuery(page, q);
      if (!success) {
        console.error(`Failed to submit query: "${q}". Aborting remaining queries.`);
        break;
      }
      
      const completed = await waitForResearchToComplete(page, 12); // Wait up to 12 minutes
      if (!completed) {
        console.error(`Failed to complete research for query: "${q}". Aborting remaining queries.`);
        break;
      }
      
      console.log(`Query ${i + 1} completed and imported successfully.`);
      await delay(5000); // 5s cooling down
    }
    
    console.log('\n--- Deep Research Execution Finished ---');
    await takeScreenshot(page, 'final_state');
    
  } catch (err) {
    console.error('Fatal error in main script execution:', err);
  } finally {
    await browser.close();
    console.log('CDP connection closed.');
  }
}

main().catch(console.error);
