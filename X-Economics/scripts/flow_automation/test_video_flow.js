const puppeteer = require('puppeteer-core');
const fs = require('fs');

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
  
  // Check if settings menu is already open
  const isMenuOpen = await page.evaluate(() => {
    return !!document.querySelector('[role="tablist"]');
  });
  
  if (!isMenuOpen) {
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
  } else {
    console.log('[MODEL] Settings menu is already open. Proceeding directly to tab selection.');
  }
  
  const isImageModel = modelName.includes('Banana') || modelName.includes('Imagen');
  
  // Find tab button
  let tabBtn = null;
  let startTime = Date.now();
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
}

async function setBatchSizeToOne(page) {
  const isMenuOpen = await page.evaluate(() => {
    return !!document.querySelector('[role="tablist"]');
  });
  
  if (!isMenuOpen) {
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
    if (!settingsBtn) return;
    await clickNative(page, settingsBtn);
  }
  
  let x1Option = null;
  let startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle(() => {
      return Array.from(document.querySelectorAll('button, [role="tab"], [role="option"]')).find(el => {
        const text = el.innerText ? el.innerText.trim() : '';
        return text === '1x' || text === '1' || text === 'x1';
      });
    });
    x1Option = handle ? handle.asElement() : null;
    if (x1Option) break;
    await delay(300);
  }
  
  if (x1Option) {
    await clickNative(page, x1Option);
    console.log('[BATCH] Batch size set to 1 output.');
  }
  
  await page.keyboard.press('Escape');
  await delay(800);
}

async function setReferenceImageByUrl(page, imageUrl) {
  console.log(`[REF_IMAGE] Selecting reference image by matching URL key...`);
  if (!imageUrl) throw new Error('imageUrl is empty');
  
  const urlObj = new URL(imageUrl, 'https://labs.google');
  const mediaName = urlObj.searchParams.get('name');
  if (!mediaName) throw new Error(`Could not parse media name parameter from URL: ${imageUrl}`);
  
  console.log(`[REF_IMAGE] Looking for media name: ${mediaName}`);
  
  const openDialog = async () => {
    let addBtn = null;
    let startTime = Date.now();
    while (Date.now() - startTime < 5000) {
      const handle = await page.evaluateHandle(() => {
        const textbox = document.querySelector('[role="textbox"]');
        if (!textbox) return null;
        const container = textbox.closest('div.sc-26b30722-0, div.sc-c9e4708a-0');
        return container ? container.querySelector('button[aria-haspopup="dialog"]') : null;
      });
      addBtn = handle ? handle.asElement() : null;
      if (addBtn) break;
      await delay(300);
    }
    if (!addBtn) throw new Error('Could not find Add Media dialog button');
    await clickNative(page, addBtn);
  };
  
  await openDialog();
  
  let optionBtn = null;
  let startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle((nameKey) => {
      const dialog = document.querySelector('[role="dialog"]');
      if (!dialog) return null;
      return Array.from(dialog.querySelectorAll('[role="option"]')).find(o => {
        const img = o.querySelector('img');
        return img && img.src && img.src.includes(nameKey);
      });
    }, mediaName);
    optionBtn = handle ? handle.asElement() : null;
    if (optionBtn) break;
    await delay(300);
  }
  
  if (!optionBtn) {
    await page.keyboard.press('Escape');
    throw new Error(`[REF_IMAGE] Reference image with media name ${mediaName} not found in library.`);
  }
  
  await clickNative(page, optionBtn);
  await delay(800);
  
  const isDialogOpen = await page.evaluate(() => {
    return !!document.querySelector('[role="dialog"]');
  });
  
  if (isDialogOpen) {
    console.log('[REF_IMAGE] Dialog still open. Pressing Escape.');
    await page.keyboard.press('Escape');
  } else {
    console.log('[REF_IMAGE] Dialog closed automatically.');
  }
}

async function insertPromptViaSlate(page, promptText) {
  await delayRandom(600, 1500);
  await page.evaluate((text) => {
    const el = document.querySelector('[role="textbox"][data-slate-editor="true"]');
    if (!el) throw new Error('Prompt textbox not found');
    
    const key = Object.keys(el).find(k => k.startsWith('__reactFiber'));
    if (!key) throw new Error('React Fiber key not found on textbox');
    
    let fiber = el[key];
    let editor = null;
    while (fiber) {
      if (fiber.memoizedProps && fiber.memoizedProps.editor) {
        editor = fiber.memoizedProps.editor;
        break;
      }
      fiber = fiber.return;
    }
    
    if (!editor) throw new Error('Slate editor object not found in Fiber tree');
    
    editor.selection = {
      anchor: { path: [0, 0], offset: 0 },
      focus: { path: [0, 0], offset: editor.children[0].children[0].text.length }
    };
    editor.deleteBackward('character');
    editor.insertText(text);
  }, promptText);
  await delayRandom(800, 1800);
}

async function clickSubmitButton(page) {
  let submitBtn = null;
  let startTime = Date.now();
  while (Date.now() - startTime < 5000) {
    const handle = await page.evaluateHandle(() => {
      return Array.from(document.querySelectorAll('button')).find(btn => 
        btn.innerText && btn.innerText.includes('arrow_forward') && btn.innerText.includes('Tạo')
      );
    });
    submitBtn = handle ? handle.asElement() : null;
    if (submitBtn) break;
    await delay(300);
  }
  if (!submitBtn) throw new Error('Submit button not found');
  await clickNative(page, submitBtn);
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

        const scratchDir = '/Users/pro16/Documents/VideoProject/X-Economics/scratch';
        
        console.log('1. Setting model to Veo 3.1...');
        await setModel(page, 'Veo 3.1 - Lite [Lower Priority]');
        await setBatchSizeToOne(page);
        
        console.log('2. Adding reference image...');
        // Use CH01_SC001 image URL which is generated in state
        const imageUrl = 'https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name=a595d338-3433-4c0b-9999-dcb916203554';
        await setReferenceImageByUrl(page, imageUrl);
        await page.screenshot({ path: `${scratchDir}/test_step_1_ref_added.png` });
        console.log('Screenshot saved: test_step_1_ref_added.png');

        console.log('3. Typing video prompt...');
        const videoPrompt = 'A steady shot showing the orange glow pulsing slowly, preserving the details of the reference image, 8-second continuous documentary video --ar 16:9';
        await insertPromptViaSlate(page, videoPrompt);
        await page.screenshot({ path: `${scratchDir}/test_step_2_prompt_typed.png` });
        console.log('Screenshot saved: test_step_2_prompt_typed.png');

        console.log('4. Clicking submit...');
        await clickSubmitButton(page);
        await page.screenshot({ path: `${scratchDir}/test_step_3_submitted.png` });
        console.log('Screenshot saved: test_step_3_submitted.png');

        console.log('5. Waiting 10 seconds to see state...');
        await delay(10000);
        await page.screenshot({ path: `${scratchDir}/test_step_4_final_state.png` });
        console.log('Screenshot saved: test_step_4_final_state.png');

        console.log('SUCCESS! Test flow completed.');

    } catch (error) {
        console.error('Error during test flow:', error);
    } finally {
        if (browser) {
            browser.disconnect();
        }
    }
}

main();
