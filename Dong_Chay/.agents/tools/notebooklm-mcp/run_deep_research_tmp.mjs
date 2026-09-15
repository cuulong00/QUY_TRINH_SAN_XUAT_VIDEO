import { chromium } from 'patchright';
import fs from 'fs';
import { DeepResearcher } from './dist/content/deep-researcher.js';

const notebookUrl = "https://notebooklm.google.com/notebook/f6296b14-a456-47e9-b24a-a5a2b3a7dc9b";
const profileDir = "/Users/pro16/Library/Application Support/notebooklm-mcp/chrome_profile";

// Search for the state.json in different paths
const statePaths = [
  "/Users/pro16/Library/Application Support/notebooklm-mcp/accounts/default/browser_state/state.json",
  "/Users/pro16/Library/Application Support/notebooklm-mcp/accounts/default/state.json",
  "/Users/pro16/Library/Application Support/notebooklm-mcp/browser_state/state.json"
];

async function run() {
  console.log("🚀 Launching Chrome in headless mode...");
  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    viewport: { width: 1920, height: 1080 },
    args: [
      '--disable-blink-features=AutomationControlled',
      '--disable-dev-shm-usage',
      '--no-sandbox',
    ]
  });

  // Inject cookies from the first existing state.json
  let injected = false;
  for (const statePath of statePaths) {
    if (fs.existsSync(statePath)) {
      try {
        const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));
        if (state && Array.isArray(state.cookies) && state.cookies.length > 0) {
          await context.addCookies(state.cookies);
          console.log(`✅ Manually injected ${state.cookies.length} cookies from: ${statePath}`);
          injected = true;
          break;
        }
      } catch (err) {
        console.warn(`⚠️ Failed to inject cookies from ${statePath}: ${err}`);
      }
    }
  }

  if (!injected) {
    console.warn("⚠️ No valid state.json found to inject cookies!");
  }

  const page = await context.newPage();
  console.log(`🌐 Navigating to: ${notebookUrl}`);
  await page.goto(notebookUrl);
  await page.waitForTimeout(5000); // Wait for initial load

  // Instantiate DeepResearcher and execute
  console.log("🔬 Instantiating DeepResearcher...");
  const researcher = new DeepResearcher(page);

  const query = 'Định hướng chiến lược "doanh nghiệp kiến tạo" hoặc "doanh nghiệp kiến tạo nền tảng phát triển cho tương lai" của Vingroup được công bố tại Đại hội đồng cổ đông thường niên 2026. Tìm các bài viết, phân tích, tin tức chính thống giải thích về định nghĩa này và các trụ cột đi kèm như VinFast, VinSpeed, VinEnergo.';
  
  console.log(`🚀 Starting Deep Research with query: "${query}"`);
  const result = await researcher.performDeepResearch({
    query,
    timeoutMs: 300000 // 5 minutes
  });

  console.log("\n======================================\nRESULT:\n");
  console.log(JSON.stringify(result, null, 2));
  console.log("\n======================================\n");

  await context.close();
}

run().catch(err => console.error("❌ Fatal error:", err));
