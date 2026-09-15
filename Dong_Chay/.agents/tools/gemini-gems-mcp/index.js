import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { chromium } from "patchright";
import * as fs from 'fs';
import * as path from 'path';

// Error logging helper
function logError(msg, err) {
  console.error(`[ERROR] ${msg}`, err ? err.stack || err : '');
}

function logInfo(msg) {
  console.error(`[INFO] ${msg}`);
}

const server = new Server(
  {
    name: "gemini-gems-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler("tools/list", async () => {
  return {
    tools: [
      {
        name: "deep_research_gem",
        description: "Run Deep Research by querying a custom Gemini Gem URL and downloading the response report.",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "The research query / prompt to submit to the Gem."
            },
            gem_url: {
              type: "string",
              description: "The custom Gem URL (e.g. https://gemini.google.com/gem/ae781ffc92e7)."
            },
            browser_port: {
              type: "number",
              description: "The remote debugging port of Chrome. Default is 9222.",
              default: 9222
            },
            output_file: {
              type: "string",
              description: "Optional absolute path to save the markdown report file."
            }
          },
          required: ["query", "gem_url"]
        }
      }
    ]
  };
});

server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name !== "deep_research_gem") {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }

  const { query, gem_url, browser_port = 9222, output_file } = request.params.arguments;

  logInfo(`Connecting to Chrome on port ${browser_port}...`);
  let browser;
  try {
    browser = await chromium.connectOverCDP(`http://127.0.0.1:${browser_port}`);
  } catch (err) {
    logError("Failed to connect to Chrome over CDP. Make sure Chrome is running with --remote-debugging-port=" + browser_port, err);
    return {
      isError: true,
      content: [
        {
          type: "text",
          text: `Error: Could not connect to Chrome on port ${browser_port}. Please make sure you have launched Chrome with the debug port enabled:\n/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=${browser_port}`
        }
      ]
    };
  }

  try {
    const context = browser.contexts()[0] || await browser.newContext();
    const page = await context.newPage();
    
    logInfo(`Navigating to Gem URL: ${gem_url}`);
    await page.goto(gem_url, { waitUntil: 'load', timeout: 60000 });

    logInfo("Waiting for Gemini input box...");
    // Locator for the contenteditable textbox
    const textbox = page.locator('div[role="textbox"]');
    await textbox.waitFor({ state: 'visible', timeout: 30000 });
    
    logInfo("Inputting prompt...");
    await textbox.focus();
    await textbox.fill(query);

    // Wait a brief moment
    await page.waitForTimeout(500);

    logInfo("Submitting prompt...");
    // Find the Send button or press Enter. Pressing Enter is often safer.
    // Let's try clicking the send button first, fallback to pressing Enter.
    const sendButton = page.locator('button[aria-label*="Send"], button[aria-label*="Gửi"], button[aria-label*="send"]');
    if (await sendButton.isVisible()) {
      await sendButton.click();
    } else {
      await page.keyboard.press('Enter');
    }

    logInfo("Waiting for response to generate (monitoring Stop button/status)...");
    
    // Gemini shows a stop button during generation. Wait for it to appear, then disappear.
    // If it's super fast, it might not appear. We handle that.
    let stopButton = page.locator('button[aria-label*="Stop"], button[aria-label*="Dừng"], button[aria-label*="stop"], button[aria-label*="dừng"]');
    
    try {
      await stopButton.waitFor({ state: 'visible', timeout: 8000 });
      logInfo("Stop button detected. Generating...");
    } catch (e) {
      logInfo("Stop button not detected immediately. Checking text growth...");
    }

    // Now wait for the stop button to disappear (detached/hidden)
    // and wait for text content stability.
    let generationComplete = false;
    let attempts = 0;
    const maxAttempts = 60; // 5 minutes (5s * 60)
    let lastText = "";
    
    while (!generationComplete && attempts < maxAttempts) {
      await page.waitForTimeout(5000);
      attempts++;
      
      // Check if stop button is gone
      const stopVisible = await stopButton.isVisible();
      
      // Get the latest response block text
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

    // Extract the final response markdown or text
    const responses = page.locator('message-content, div.message-content, .model-response');
    const count = await responses.count();
    if (count === 0) {
      throw new Error("Could not find any response elements on the page.");
    }
    
    const finalResponseElement = responses.nth(count - 1);
    const textReport = await finalResponseElement.innerText();
    const htmlReport = await finalResponseElement.innerHTML();
    
    logInfo("Successfully retrieved report.");

    // Close the page
    await page.close();

    // If output file specified, write it
    if (output_file) {
      const dir = path.dirname(output_file);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(output_file, textReport, 'utf8');
      logInfo(`Report saved to ${output_file}`);
    }

    return {
      content: [
        {
          type: "text",
          text: textReport
        }
      ]
    };

  } catch (err) {
    logError("Error during Gemini Gem automation", err);
    return {
      isError: true,
      content: [
        {
          type: "text",
          text: `Error during automation: ${err.message}`
        }
      ]
    };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
logInfo("Gemini Gems MCP server running.");
