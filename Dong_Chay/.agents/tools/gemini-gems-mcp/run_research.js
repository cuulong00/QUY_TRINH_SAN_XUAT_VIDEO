import { chromium } from "patchright";
import * as fs from 'fs';
import * as path from 'path';

const query = process.argv[2];
const gemUrl = process.argv[3] || "https://gemini.google.com/gem/ae781ffc92e7";
const outputFile = process.argv[4];
const browserPort = parseInt(process.argv[5] || "9222", 10);

if (!query) {
  console.error("Usage: node run_research.js <query> [gemUrl] [outputFile] [browserPort]");
  process.exit(1);
}

function logInfo(msg) {
  console.log(`[INFO] ${msg}`);
}

function logError(msg, err) {
  console.error(`[ERROR] ${msg}`, err ? err.stack || err : '');
}

async function run() {
  logInfo(`Connecting to Chrome on port ${browserPort}...`);
  let browser;
  try {
    browser = await chromium.connectOverCDP(`http://127.0.0.1:${browserPort}`);
  } catch (err) {
    logError(`Failed to connect to Chrome. Make sure Chrome is running with --remote-debugging-port=${browserPort}`, err);
    process.exit(1);
  }

  try {
    const context = browser.contexts()[0] || await browser.newContext();
    const page = await context.newPage();
    
    logInfo(`Navigating to Gem URL: ${gemUrl}`);
    await page.goto(gemUrl, { waitUntil: 'load', timeout: 60000 });

    logInfo("Waiting for Gemini input box...");
    const textbox = page.locator('div[role="textbox"]');
    await textbox.waitFor({ state: 'visible', timeout: 30000 });
    
    logInfo("Inputting prompt...");
    await textbox.focus();
    await textbox.fill(query);
    await page.waitForTimeout(500);

    logInfo("Submitting prompt...");
    const sendButton = page.locator('button[aria-label*="Send"], button[aria-label*="Gửi"], button[aria-label*="send"]');
    if (await sendButton.isVisible()) {
      await sendButton.click();
    } else {
      await page.keyboard.press('Enter');
    }

    logInfo("Waiting for response to generate (monitoring Stop button/status)...");
    
    let stopButton = page.locator('button[aria-label*="Stop"], button[aria-label*="Dừng"], button[aria-label*="stop"], button[aria-label*="dừng"]');
    
    try {
      await stopButton.waitFor({ state: 'visible', timeout: 8000 });
      logInfo("Stop button detected. Generating...");
    } catch (e) {
      logInfo("Stop button not detected immediately. Checking text growth...");
    }

    let generationComplete = false;
    let attempts = 0;
    const maxAttempts = 120; // 10 minutes (5s * 120)
    let lastText = "";
    
    while (!generationComplete && attempts < maxAttempts) {
      await page.waitForTimeout(5000);
      attempts++;
      
      const stopVisible = await stopButton.isVisible();
      
      const responses = page.locator('message-content, div.message-content, .model-response');
      const count = await responses.count();
      let currentText = "";
      if (count > 0) {
        currentText = await responses.nth(count - 1).innerText();
      }
      
      logInfo(`Checking stability... Text length: ${currentText.length}. Stop button visible: ${stopVisible}`);
      
      if (!stopVisible && currentText.length > 0 && currentText === lastText) {
        generationComplete = true;
        logInfo("Generation stable and stop button hidden. Finished!");
      }
      
      lastText = currentText;
    }

    if (attempts >= maxAttempts) {
      logInfo("Warning: Timeout reached waiting for response stability.");
    }

    const responses = page.locator('message-content, div.message-content, .model-response');
    const count = await responses.count();
    if (count === 0) {
      throw new Error("Could not find any response elements on the page.");
    }
    
    const finalResponseElement = responses.nth(count - 1);
    const textReport = await finalResponseElement.innerText();
    
    logInfo("Successfully retrieved report.");
    await page.close();

    if (outputFile) {
      const dir = path.dirname(outputFile);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(outputFile, textReport, 'utf8');
      logInfo(`Report saved to ${outputFile}`);
    } else {
      console.log("\n--- REPORT OUTPUT ---");
      console.log(textReport);
      console.log("---------------------\n");
    }

    process.exit(0);

  } catch (err) {
    logError("Error during Gemini Gem automation", err);
    process.exit(1);
  }
}

run();
