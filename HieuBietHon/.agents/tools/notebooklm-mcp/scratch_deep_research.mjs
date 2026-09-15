import { chromium } from 'patchright';

async function runResearch(query) {
  const userDataDir = '/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile';
  console.log(`\n--- Starting Deep Research for: "${query}" ---`);
  console.log('Launching browser with profile:', userDataDir);
  
  const browser = await chromium.launchPersistentContext(userDataDir, {
    headless: true,
    channel: 'chrome'
  });
  const page = await browser.newPage();
  
  await page.goto('https://notebooklm.google.com/notebook/9891a2f0-8e48-445a-a2c4-4b25ee3c3800', { waitUntil: 'networkidle' });
  console.log('Navigated to notebook');
  
  await page.waitForTimeout(5000);
  
  // 1. Click Add source
  console.log('Looking for Add Source button...');
  const addSourceSelectors = [
    'button[aria-label="Add source"]',
    'button[aria-label*="Add source" i]',
    'button:has-text("Thêm nguồn")',
    'button:has-text("Add source")'
  ];
  let found = false;
  for (const selector of addSourceSelectors) {
    try {
      const btn = page.locator(selector).first();
      if (await btn.isVisible({ timeout: 2000 })) {
        console.log('Found Add source:', selector);
        await btn.click({ force: true });
        found = true;
        break;
      }
    } catch {}
  }
  
  if (!found) {
    console.log('Warning: Add source button not found, checking if dialog is already open...');
  }
  
  await page.waitForTimeout(3000);
  
  // 2. Click Deep Research option in panel
  console.log('Looking for Deep Research option...');
  const deepTypeSelectors = [
    'button:has-text("Deep Research")',
    'button:has-text("Nghiên cứu sâu")',
    'button:has-text("Nghiên cứu nhanh")',
    'span:has-text("Deep Research")',
    'span:has-text("Nghiên cứu sâu")',
    'span:has-text("Nghiên cứu nhanh")'
  ];
  let foundDeep = false;
  for (const selector of deepTypeSelectors) {
    try {
      const btn = page.locator(selector).first();
      if (await btn.isVisible({ timeout: 2000 })) {
        console.log('Found Deep Research option:', selector);
        await btn.click({ force: true });
        foundDeep = true;
        break;
      }
    } catch {}
  }
  
  await page.waitForTimeout(3000);
  
  // 3. Type query
  console.log('Looking for textarea...');
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
        console.log('Found textarea:', selector);
        break;
      }
    } catch {}
  }
  
  if (textarea) {
    await textarea.click({ force: true });
    await textarea.fill('');
    await page.waitForTimeout(500);
    await textarea.fill(query);
    await page.waitForTimeout(500);
    await textarea.evaluate((el, q) => {
      el.value = q;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }, query);
    console.log('Typed query');
  } else {
    console.error('Error: Could not find textarea to input research query!');
    await page.screenshot({ path: '/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/deep_research_error.png' });
    await browser.close();
    return false;
  }
  
  await page.waitForTimeout(1000);
  
  // 4. Click Submit
  console.log('Submitting...');
  try {
    const activeElement = await page.evaluate(() => document.activeElement?.tagName);
    if (activeElement === 'TEXTAREA' || activeElement === 'INPUT') {
       console.log('Pressing Enter');
       await page.keyboard.press('Enter');
    }
  } catch {}

  const submitSelectors = [
    '[role="dialog"] button.actions-enter-button',
    '.cdk-overlay-pane button.actions-enter-button',
    '[role="dialog"] button:has-text("Nghiên cứu")',
    '[role="dialog"] button:has-text("Research")',
    'button:has-text("Nghiên cứu nhanh")',
    'button:has-text("Deep Research")'
  ];
  for (const sel of submitSelectors) {
    try {
      const btn = page.locator(sel).first();
      if (await btn.isVisible({ timeout: 1000 })) {
        await btn.click({ force: true });
        console.log('Clicked submit:', sel);
        break;
      }
    } catch {}
  }
  
  console.log('Waiting 15 seconds to ensure research submission is registered...');
  await page.waitForTimeout(15000);
  
  console.log('Taking screenshot for verification...');
  await page.screenshot({ path: `/Users/pro16/Documents/VideoProject/HieuBietHon/scratch/deep_research_submitted_${Date.now()}.png` });
  
  console.log('Closing browser...');
  await browser.close();
  return true;
}

async function main() {
  const queries = [
    "VinFast India strategy, Tamil Nadu plant build progress, export targets, RHD markets Sri Lanka, Nepal, Mauritius, Middle East, Africa",
    "Green SM India Delhi launch June 2026, Green SM Limo Delhi, rebranding of Xanh SM to Green SM in April 2026, ride-hailing expansion in Delhi, Bengaluru",
    "Gensol and BluSmart scandal: Jaggi brothers SEBI ban in April 2025, ED asset attachment in January 2026, diversion of ₹262 crore",
    "Vingroup transferring 182,000 billion VND in factory debt to Công ty Tương Lai in May 2026, leaseback OEM model of VinFast",
    "Indonesian police VF 3 EV deployment: Korlantas Polri modified VF 3s as mobile bases for ETLE drone patrols"
  ];
  
  for (const q of queries) {
    const success = await runResearch(q);
    if (!success) {
      console.log('Failed to submit research for query:', q);
    }
    // Wait between submissions
    await new Promise(resolve => setTimeout(resolve, 5000));
  }
  console.log('All deep research queries submitted!');
}

main().catch(console.error);
