/**
 * Direct test of Deep Research v3
 * Uses the compiled dist/content/deep-researcher.js directly
 */
import { chromium } from 'patchright';
import path from 'path';
import fs from 'fs';

const NOTEBOOK_URL = 'https://notebooklm.google.com/notebook/bc481255-b22a-43a7-9678-c530fd3357fc';
const PROFILE_DIR = path.join(process.env.HOME || '', 'Library/Application Support/notebooklm-mcp/chrome_profile');

async function main() {
  console.log('🚀 Launching browser...');

  const context = await chromium.launchPersistentContext(PROFILE_DIR, {
    headless: false,
    args: ['--disable-blink-features=AutomationControlled', '--no-sandbox'],
    viewport: { width: 1280, height: 900 },
  });

  const page = context.pages()[0] || await context.newPage();

  console.log('📄 Navigating to notebook...');
  await page.goto(NOTEBOOK_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  console.log('✅ Page loaded, waiting for popup...');
  await page.waitForTimeout(5000);

  // Import our compiled deep researcher
  const { DeepResearcher } = await import('../dist/content/deep-researcher.js');
  const researcher = new DeepResearcher(page);

  // We will run the research in the background so we can take a screenshot during it
  console.log('🔬 Starting Deep Research...');
  const researchPromise = researcher.performDeepResearch({
    query: 'VinFast financial reports funding sources Phạm Nhật Vượng Vingroup capital 2024 2025 2026',
    timeoutMs: 600000, // 10 minutes timeout for real research
  });

  // Wait 15 seconds after starting to see what's on the screen
  await page.waitForTimeout(15000);
  
  const screenshotPath = path.join(process.cwd(), 'post_submit_screenshot.png');
  await page.screenshot({ path: screenshotPath });
  console.log(`📸 Screenshot taken during research: ${screenshotPath}`);

  const result = await researchPromise;

  console.log('\n📋 Result:', JSON.stringify(result, null, 2));

  // Keep browser open for inspection
  console.log('\n⏳ Browser stays open for 10s...');
  await page.waitForTimeout(10000);
  await context.close();
}

main().catch(console.error);
