const puppeteer = require('puppeteer-core');

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const delayRandom = (min, max) => {
  const ms = Math.floor(Math.random() * (max - min + 1) + min);
  return new Promise((resolve) => setTimeout(resolve, ms));
};

async function clickNative(page, elementHandle) {
  if (!elementHandle) return;
  const el = elementHandle.asElement ? elementHandle.asElement() : elementHandle;
  await el.hover();
  await delayRandom(200, 500);
  await el.click();
  await delay(800);
}

async function setModel(page, modelName) {
  console.log(`[MODEL] Configuring model settings to: ${modelName}...`);
  
  // Find settings button
  let settingsBtn = null;
  let startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle(() => {
      return Array.from(document.querySelectorAll('button')).find(btn => 
        btn.getAttribute('aria-haspopup') === 'menu' && 
        (btn.innerText && (
          btn.innerText.includes('Video') || 
          btn.innerText.includes('Hình ảnh') || 
          btn.innerText.includes('Banana') || 
          btn.innerText.includes('Veo') || 
          btn.innerText.includes('Omni') || 
          btn.innerText.includes('Imagen')
        ))
      );
    });
    settingsBtn = handle ? handle.asElement() : null;
    if (settingsBtn) break;
    await delay(300);
  }
  
  if (!settingsBtn) throw new Error('Settings button not found');
  await clickNative(page, settingsBtn);
  
  const isImageModel = modelName.includes('Banana') || modelName.includes('Imagen');
  
  // Find tab button
  let tabBtn = null;
  startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle((isImage) => {
      return Array.from(document.querySelectorAll('[role="tab"]')).find(t => {
        const text = t.innerText ? t.innerText.replace(/\s+/g, ' ').trim() : '';
        return isImage ? (text.includes('Hình ảnh') && !text.includes('Xem')) : (text.includes('Video') && !text.includes('Xem'));
      });
    }, isImageModel);
    tabBtn = handle ? handle.asElement() : null;
    if (tabBtn) break;
    await delay(300);
  }
  
  if (!tabBtn) throw new Error('Tab button not found');
  await clickNative(page, tabBtn);
  
  // Find model menu dropdown button (specifically matching arrow_drop_down/up to avoid clicking settings button)
  let modelMenuBtn = null;
  startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle(() => {
      return Array.from(document.querySelectorAll('button, [role="button"]')).find(b => 
        b.innerText && 
        (b.innerText.includes('arrow_drop_down') || b.innerText.includes('arrow_drop_up')) &&
        (b.innerText.includes('Veo') || b.innerText.includes('Omni') || b.innerText.includes('Banana') || b.innerText.includes('Imagen'))
      );
    });
    modelMenuBtn = handle ? handle.asElement() : null;
    if (modelMenuBtn) break;
    await delay(300);
  }
  
  if (!modelMenuBtn) throw new Error('Model dropdown button not found');
  await clickNative(page, modelMenuBtn);
  
  // Find option button
  let optionBtn = null;
  startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle((name) => {
      return Array.from(document.querySelectorAll('button, [role="option"], [role="menuitem"]')).find(b => 
        b.innerText && b.innerText.toLowerCase().replace(/\s+/g, '').includes(name.toLowerCase().replace(/\s+/g, ''))
      );
    }, modelName);
    optionBtn = handle ? handle.asElement() : null;
    if (optionBtn) break;
    await delay(300);
  }
  
  if (!optionBtn) {
    await page.keyboard.press('Escape');
    throw new Error(`Model option ${modelName} not found`);
  }
  await clickNative(page, optionBtn);
  
  await page.keyboard.press('Escape');
  await delay(800);
  console.log('[MODEL] Successfully switched model settings!');
}

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

        await setModel(page, '🍌 Nano Banana 2 Lite');

    } catch (error) {
        console.error('Error during model selection:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
