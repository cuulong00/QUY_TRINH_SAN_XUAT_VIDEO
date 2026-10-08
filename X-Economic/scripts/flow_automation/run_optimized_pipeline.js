const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const http = require('http');
const https = require('https');
const { URL } = require('url');

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const delayRandom = (min, max) => {
  const ms = Math.floor(Math.random() * (max - min + 1) + min);
  return new Promise((resolve) => setTimeout(resolve, ms));
};

let lastSubmitTime = 0;

async function enforceCooldown() {
  const elapsed = Date.now() - lastSubmitTime;
  if (elapsed < 25000) {
    const waitTime = 25000 - elapsed;
    console.log(`[COOLDOWN] Waiting ${Math.ceil(waitTime / 1000)}s before next submission to prevent bot detection...`);
    await delay(waitTime);
  }
}

async function getWebSocketUrl() {
  return new Promise((resolve, reject) => {
    http.get('http://127.0.0.1:9222/json/version', (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        try {
          const info = JSON.parse(data);
          resolve(info.webSocketDebuggerUrl);
        } catch (err) {
          reject(new Error('Failed to parse debugging info: ' + err.message));
        }
      });
    }).on('error', (err) => {
      reject(new Error('Could not connect to browser on port 9222: ' + err.message));
    });
  });
}

async function downloadFile(url, destPath, cookieHeader) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(destPath);
    const parsed = new URL(url);
    
    const options = {
      hostname: parsed.hostname,
      path: parsed.pathname + parsed.search,
      headers: {}
    };
    
    if (parsed.hostname.includes('labs.google') && cookieHeader) {
      options.headers['Cookie'] = cookieHeader;
    }
    
    const protocol = parsed.protocol === 'https:' ? https : http;
    
    protocol.get(options, (response) => {
      if (response.statusCode === 307 || response.statusCode === 302 || response.statusCode === 301) {
        const redirectUrl = response.headers.location;
        downloadFile(redirectUrl, destPath, cookieHeader).then(resolve).catch(reject);
        return;
      }
      
      if (response.statusCode !== 200 && response.statusCode !== 206) {
        reject(new Error(`Failed to download file, status code: ${response.statusCode}`));
        return;
      }
      
      response.pipe(file);
      
      file.on('finish', () => {
        file.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(destPath, () => {});
      reject(err);
    });
  });
}

function parsePrompts(imagePath, videoPath) {
  const imgContent = fs.readFileSync(imagePath, 'utf8');
  const vidContent = fs.readFileSync(videoPath, 'utf8');
  
  const imgLines = imgContent.split('\n').map(l => l.trim()).filter(Boolean);
  const vidLines = vidContent.split('\n').map(l => l.trim()).filter(Boolean);
  
  const scenes = {};
  
  for (const line of imgLines) {
    const match = line.match(/^(CH\d{2}_SC\d{3}):\s*(.*)$/);
    if (match) {
      const [_, sceneId, prompt] = match;
      if (!scenes[sceneId]) scenes[sceneId] = { id: sceneId };
      scenes[sceneId].imagePrompt = prompt;
    }
  }
  
  for (const line of vidLines) {
    const match = line.match(/^(CH\d{2}_SC\d{3}):\s*(.*)$/);
    if (match) {
      const [_, sceneId, prompt] = match;
      if (!scenes[sceneId]) scenes[sceneId] = { id: sceneId };
      scenes[sceneId].videoPrompt = prompt;
    }
  }
  
  return Object.values(scenes).sort((a, b) => a.id.localeCompare(b.id));
}

function cleanVideoPrompt(prompt) {
  if (!prompt) return '';
  const match = prompt.match(/^@[^\s]+\s*(?:->|=>|-)\s*(.*)$/);
  return match ? match[1].trim() : prompt.trim();
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

// 100% Native Mouse Hover and Click simulation using Puppeteer
async function clickNative(page, elementHandle) {
  if (!elementHandle) return;
  const el = elementHandle.asElement ? elementHandle.asElement() : elementHandle;
  await el.hover();
  await delayRandom(200, 500); // natural hover response delay
  await el.click();
  await delay(800); // wait for UI transition after click
}

async function setModel(page, modelName) {
  console.log(`[MODEL] Configuring model settings to: ${modelName}...`);
  
  const alreadySelected = await page.evaluate((targetModel) => {
    const settingsBtn = Array.from(document.querySelectorAll('button')).find(btn => 
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
    if (!settingsBtn) return false;
    
    const cleanTarget = targetModel.replace(/[🍌\s\-\[\]]/g, '').toLowerCase();
    const cleanCurrent = settingsBtn.innerText.replace(/[🍌\s\-\[\]]/g, '').toLowerCase();
    
    return cleanCurrent.includes(cleanTarget) || cleanTarget.includes(cleanCurrent);
  }, modelName);
  
  if (alreadySelected) {
    console.log(`[MODEL] Model ${modelName} is already selected. Skipping configuration.`);
    return;
  }
  
  // Find settings button with retry polling
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
  
  // Find tab button with retry polling
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
  
  // Find model menu dropdown button with retry polling
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
  
  // Find option button with retry polling
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
  
  let x1Option = null;
  startTime = Date.now();
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
  
  // click settings button again to close
  await clickNative(page, settingsBtn);
  await delay(800);
}

async function setReferenceImageByUrl(page, imageUrl) {
  console.log(`[REF_IMAGE] Selecting reference image by matching URL key...`);
  if (!imageUrl) throw new Error('imageUrl is empty');
  
  // Extract the "name=..." parameter from the imageUrl
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
  
  // Find the option element whose img src contains the mediaName
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
    console.log(`[REF_IMAGE] Image not found on first page. Scrolling library dialog...`);
    await page.evaluate(() => {
      const dialog = document.querySelector('[role="dialog"]');
      if (dialog) {
        const scrollable = dialog.querySelector('div[style*="overflow"]');
        if (scrollable) scrollable.scrollTop = scrollable.scrollHeight;
      }
    });
    await delay(1500);
    
    const handle = await page.evaluateHandle((nameKey) => {
      const dialog = document.querySelector('[role="dialog"]');
      if (!dialog) return null;
      return Array.from(dialog.querySelectorAll('[role="option"]')).find(o => {
        const img = o.querySelector('img');
        return img && img.src && img.src.includes(nameKey);
      });
    }, mediaName);
    optionBtn = handle ? handle.asElement() : null;
  }
  
  if (!optionBtn) {
    await page.keyboard.press('Escape');
    throw new Error(`[REF_IMAGE] Reference image with media name ${mediaName} not found in library.`);
  }
  
  await clickNative(page, optionBtn);
  await delay(800);
  
  // Check if dialog is still open (some Google Flow updates close the dialog immediately on option click)
  const isDialogOpen = await page.evaluate(() => {
    return !!document.querySelector('[role="dialog"]');
  });
  
  if (isDialogOpen) {
    console.log('[REF_IMAGE] Dialog still open after selection. Clicking confirm button...');
    let confirmBtn = null;
    startTime = Date.now();
    while (Date.now() - startTime < 5000) {
      const handle = await page.evaluateHandle(() => {
        const dialog = document.querySelector('[role="dialog"]');
        if (!dialog) return null;
        return Array.from(dialog.querySelectorAll('button')).find(btn => 
          btn.textContent && (
            btn.textContent.includes('Thêm') || 
            btn.textContent.includes('Add') || 
            btn.textContent.includes('Xong') || 
            btn.textContent.includes('Confirm')
          )
        );
      });
      confirmBtn = handle ? handle.asElement() : null;
      if (confirmBtn) break;
      await delay(300);
    }
    
    if (confirmBtn) {
      await clickNative(page, confirmBtn);
      await delay(1200);
    } else {
      console.warn('[REF_IMAGE] Confirm button not found but dialog is open. Pressing Escape.');
      await page.keyboard.press('Escape');
    }
  } else {
    console.log('[REF_IMAGE] Dialog closed automatically after selecting option.');
  }
}

async function clearReferenceImages(page) {
  await page.evaluate(() => {
    const textbox = document.querySelector('[role="textbox"]');
    if (!textbox) return;
    const container = textbox.closest('div.sc-26b30722-0, div.sc-c9e4708a-0');
    if (!container) return;
    
    const cancelButtons = Array.from(container.querySelectorAll('button')).filter(btn => {
      const text = btn.innerText || '';
      return text.toLowerCase().includes('cancel');
    });
    
    for (const btn of cancelButtons) {
      btn.click();
    }
  });
  await delay(800);
}

async function downloadDirectAsset(page, mediaUrl, outputPath) {
  const parsedUrl = new URL(page.url());
  const absoluteMediaUrl = new URL(mediaUrl, parsedUrl.origin).toString();
  
  const cookies = await page.cookies();
  const cookieHeader = cookies.map(c => `${c.name}=${c.value}`).join('; ');
  
  await downloadFile(absoluteMediaUrl, outputPath, cookieHeader);
}

async function getExistingTileIds(page) {
  return await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[data-tile-id]')).map(el => el.getAttribute('data-tile-id'));
  });
}

async function getNewTileId(page, oldTileIds) {
  const startTime = Date.now();
  while ((Date.now() - startTime) < 20000) {
    const newId = await page.evaluate((oldIds) => {
      const currentTiles = Array.from(document.querySelectorAll('[data-tile-id]'));
      const newTile = currentTiles.find(el => !oldIds.includes(el.getAttribute('data-tile-id')));
      return newTile ? newTile.getAttribute('data-tile-id') : '';
    }, oldTileIds);
    if (newId) return newId;
    await delay(500);
  }
  return null;
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
  
  if (!submitBtn) {
    throw new Error('Could not find submit button');
  }
  
  await clickNative(page, submitBtn);
}

async function checkTileStatus(page, tileId) {
  return await page.evaluate((id) => {
    const card = document.querySelector(`[data-tile-id="${id}"]`);
    if (!card) return { type: 'waiting' };
    
    const isElementVisible = (el) => {
      let parent = el;
      while (parent && parent !== card) {
        const style = window.getComputedStyle(parent);
        if (style.opacity === '0' || style.display === 'none' || style.visibility === 'hidden') {
          return false;
        }
        parent = parent.parentElement;
      }
      return true;
    };
    
    const allDivs = Array.from(card.querySelectorAll('div'));
    const errorDiv = allDivs.find(d => d.innerText && (d.innerText === 'Không thành công' || d.innerText === 'Failed'));
    if (errorDiv && isElementVisible(errorDiv)) {
      return { type: 'failed', text: card.innerText };
    }
    
    const textNodes = [];
    const walk = document.createTreeWalker(card, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while (node = walk.nextNode()) {
      textNodes.push(node.nodeValue.trim());
    }
    
    const queueNode = textNodes.find(n => n === 'Đang trong hàng đợi' || n === 'In queue');
    if (queueNode && isElementVisible(card.querySelector('.sc-be9184ba-0') || card)) {
      return { type: 'queued' };
    }
    
    const progressNode = textNodes.find(n => /^\d+%$/.test(n));
    if (progressNode && isElementVisible(card.querySelector('.sc-be9184ba-0') || card)) {
      return { type: 'generating', progress: parseInt(progressNode) };
    }
    
    const video = card.querySelector('video');
    if (video && video.src && video.src.includes('getMediaUrlRedirect')) {
      return { type: 'complete', url: video.src };
    }
    
    const img = card.querySelector('img');
    if (img && img.src && img.src.includes('getMediaUrlRedirect')) {
      return { type: 'complete', url: img.src };
    }
    
    return { type: 'unknown', text: textNodes.join(' | ') };
  }, tileId);
}

// Mutex lock for browser UI interaction
let browserLock = false;
async function acquireLock() {
  while (browserLock) {
    await delay(100);
  }
  browserLock = true;
}
function releaseLock() {
  browserLock = false;
}

function loadState(statePath) {
  if (fs.existsSync(statePath)) {
    try {
      return JSON.parse(fs.readFileSync(statePath, 'utf8'));
    } catch (err) {
      console.error('Failed to parse generation state file:', err.message);
    }
  }
  return {};
}

function saveState(statePath, scenesState) {
  const stateObj = {};
  for (const s of scenesState) {
    stateObj[s.scene.id] = {
      imageStatus: s.state === 'PENDING_IMAGE' ? 'PENDING' : 
                   (s.state === 'GENERATING_IMAGE' ? 'GENERATING' : 'COMPLETED'),
      imageTileId: s.imageTileId,
      imageUrl: s.imageUrl,
      videoStatus: s.state === 'COMPLETED' ? 'COMPLETED' : 
                   (s.state === 'GENERATING_VIDEO' ? 'GENERATING' : 'PENDING'),
      videoTileId: s.videoTileId
    };
  }
  fs.writeFileSync(statePath, JSON.stringify(stateObj, null, 2), 'utf8');
}

async function main() {
  const args = process.argv.slice(2);
  const episodeIndex = args.indexOf('--episode');
  const limitIndex = args.indexOf('--limit');
  const concurrencyIndex = args.indexOf('--concurrency');
  const isNewProject = args.includes('--new-project');
  const isDryRun = args.includes('--dry-run');
  
  if (episodeIndex === -1 || !args[episodeIndex + 1]) {
    console.error('Usage: node run_optimized_pipeline.js --episode <slug> [--limit <num>] [--concurrency <num>] [--new-project] [--dry-run]');
    process.exit(1);
  }
  
  const slug = args[episodeIndex + 1];
  const limit = limitIndex !== -1 && args[limitIndex + 1] ? parseInt(args[limitIndex + 1]) : Infinity;
  const maxConcurrent = concurrencyIndex !== -1 && args[concurrencyIndex + 1] ? parseInt(args[concurrencyIndex + 1]) : 6;
  
  const episodeDir = path.join(__dirname, '..', '..', 'episodes', slug);
  const imagePromptsPath = path.join(episodeDir, 'image_prompts.txt');
  const videoPromptsPath = path.join(episodeDir, 'video_prompts.txt');
  const statePath = path.join(episodeDir, 'generation_state.json');
  const videosDir = path.join(episodeDir, 'videos');
  
  if (!fs.existsSync(videosDir)) fs.mkdirSync(videosDir, { recursive: true });
  
  console.log(`[INIT] Starting optimized generation pipeline (NO IMAGE DOWNLOAD) for episode: ${slug}`);
  console.log(`[INIT] Image Prompts: ${imagePromptsPath}`);
  console.log(`[INIT] Video Prompts: ${videoPromptsPath}`);
  console.log(`[INIT] State Logger: ${statePath}`);
  console.log(`[INIT] Max Concurrent Requests: ${maxConcurrent}`);
  
  const scenes = parsePrompts(imagePromptsPath, videoPromptsPath);
  console.log(`[INIT] Parsed ${scenes.length} total scenes.`);
  
  const savedState = loadState(statePath);
  
  const scenesState = scenes.map(s => {
    const videoPath = path.join(videosDir, `${s.id}.mp4`);
    const saved = savedState[s.id] || {};
    
    let state = 'PENDING_IMAGE';
    
    if (fs.existsSync(videoPath)) {
      state = 'COMPLETED';
    } else if (saved.videoStatus === 'COMPLETED') {
      state = 'PENDING_VIDEO';
    } else if (saved.imageStatus === 'COMPLETED') {
      state = 'PENDING_VIDEO';
    }
    
    return {
      scene: s,
      state: state,
      videoPath,
      imageTileId: saved.imageTileId || null,
      imageUrl: saved.imageUrl || null,
      videoTileId: saved.videoTileId || null,
      imageFailCount: 0,
      videoFailCount: 0
    };
  });
  
  saveState(statePath, scenesState);
  
  if (isDryRun) {
    console.log('\n--- DRY RUN SUMMARY ---');
    let count = 0;
    for (const s of scenesState) {
      if (count >= limit) break;
      console.log(`Scene: ${s.scene.id} [Current State: ${s.state}]`);
      console.log(`  - Image: ${s.scene.imagePrompt ? 'Yes' : 'No'}`);
      console.log(`  - Video: ${s.scene.videoPrompt ? 'Yes' : 'No'}`);
      count++;
    }
    console.log('-----------------------\n');
    process.exit(0);
  }
  
  let wsUrl;
  try {
    wsUrl = await getWebSocketUrl();
  } catch (err) {
    console.error('Fatal Error:', err.message);
    console.error('Ensure Chrome is running with remote debugging at port 9222.');
    process.exit(1);
  }
  
  console.log('[BROWSER] Connecting to Chrome debugger...');
  const browser = await puppeteer.connect({
    browserWSEndpoint: wsUrl,
    defaultViewport: null
  });
  
  const pages = await browser.pages();
  let page = pages.find(p => p.url().includes('labs.google') && p.url().includes('tools/flow'));
  
  if (page) {
    console.log(`[BROWSER] Found active Google Flow tab: ${page.url()}`);
    await page.bringToFront();
    if (isNewProject) {
      console.log('[BROWSER] --new-project flag detected. Navigating to Flow Home to create a new project...');
      await page.goto('https://labs.google/fx/vi/tools/flow', { waitUntil: 'domcontentloaded' });
      await delay(5000);
    }
  } else {
    console.log('[BROWSER] Google Flow tab not found. Opening a new tab...');
    page = await browser.newPage();
    await page.goto('https://labs.google/fx/vi/tools/flow', { waitUntil: 'domcontentloaded' });
    await delay(5000);
  }
  
  const currentUrl = page.url();
  if (currentUrl.endsWith('/tools/flow') || currentUrl.endsWith('/tools/flow/')) {
    console.log('[BROWSER] On Flow Home. Creating a new project...');
    const created = await page.evaluate(async () => {
      const btns = Array.from(document.querySelectorAll('button'));
      const newProject = btns.find(b => {
          const txt = b.textContent?.toLowerCase() || '';
          return txt.includes('dự án mới') || txt.includes('new project') || txt.includes('create with flow');
      });
      if (newProject) {
          newProject.click();
          return true;
      }
      return false;
    });
    
    if (created) {
      console.log('[BROWSER] Clicked New Project button. Waiting 5s for redirection...');
      await delay(5000);
      console.log(`[BROWSER] New project loaded: ${page.url()}`);
    } else {
      console.warn('[BROWSER] New Project button not found or could not be clicked!');
    }
  }
  
  await browser.defaultBrowserContext().overridePermissions('https://labs.google', ['clipboard-read', 'clipboard-write']);
  
  const activeImages = () => scenesState.filter(s => s.state === 'GENERATING_IMAGE').length;
  const activeVideos = () => scenesState.filter(s => s.state === 'GENERATING_VIDEO').length;
  const activeTotal = () => activeImages() + activeVideos();
  
  let pipelineFinished = false;
  let countSubmitted = 0;
  
  console.log('\n[START] Starting pipelined generation worker loop...');
  
  while (!pipelineFinished) {
    // 1. Process active generations statuses
    const activeImageScenes = scenesState.filter(s => s.state === 'GENERATING_IMAGE');
    const activeVideoScenes = scenesState.filter(s => s.state === 'GENERATING_VIDEO');
    
    // Check generating images
    for (const s of activeImageScenes) {
      const status = await checkTileStatus(page, s.imageTileId);
      if (status.type === 'complete') {
        console.log(`\n[COMPLETE] Image ready on Flow for ${s.scene.id}! URL: ${status.url}`);
        s.state = 'PENDING_VIDEO';
        s.imageTileId = null;
        s.imageUrl = status.url;
        saveState(statePath, scenesState);
      } else if (status.type === 'failed') {
        console.error(`\n[FAILED] Image generation failed on Flow for ${s.scene.id}`);
        s.imageFailCount++;
        s.state = s.imageFailCount > 10 ? 'FAILED' : 'PENDING_IMAGE'; // Try up to 10 times to persist through maintenance
        s.imageTileId = null;
        saveState(statePath, scenesState);
      }
    }
    
    // Check generating videos
    for (const s of activeVideoScenes) {
      const status = await checkTileStatus(page, s.videoTileId);
      if (status.type === 'complete') {
        console.log(`\n[COMPLETE] Video ready for ${s.scene.id}! Downloading...`);
        try {
          await downloadDirectAsset(page, status.url, s.videoPath);
          s.state = 'COMPLETED';
          s.videoTileId = null;
          saveState(statePath, scenesState);
        } catch (err) {
          console.error(`\n[ERROR] Failed downloading video for ${s.scene.id}:`, err.message);
          s.state = 'PENDING_VIDEO'; // retry
          s.videoTileId = null;
        }
      } else if (status.type === 'failed') {
        console.error(`\n[FAILED] Video generation failed on Flow for ${s.scene.id}`);
        s.videoFailCount++;
        s.state = s.videoFailCount > 10 ? 'FAILED' : 'PENDING_VIDEO'; // Try up to 10 times
        s.videoTileId = null;
        saveState(statePath, scenesState);
      }
    }
    
    // 2. Submit new jobs if slots are available
    if (!browserLock && countSubmitted < limit) {
      // Prioritize video submissions
      const nextVideo = scenesState.find(s => s.state === 'PENDING_VIDEO');
      if (nextVideo && activeTotal() < maxConcurrent) {
        await acquireLock();
        try {
          console.log(`\n[PIPELINE] Submitting Video for scene ${nextVideo.scene.id}...`);
          const existingTileIds = await getExistingTileIds(page);
          
          await setModel(page, 'Veo 3.1 - Lite [Lower Priority]');
          await setBatchSizeToOne(page);
          await clearReferenceImages(page);
          
          // Select reference image from project library using matching URL
          await setReferenceImageByUrl(page, nextVideo.imageUrl);
          
          const videoPromptClean = cleanVideoPrompt(nextVideo.scene.videoPrompt);
          console.log(`[PROMPT] Video prompt: "${videoPromptClean}"`);
          
          await insertPromptViaSlate(page, videoPromptClean);
          await delay(1200); // Wait for slate binding
          
          await enforceCooldown();
          await clickSubmitButton(page);
          lastSubmitTime = Date.now();
          
          const newTileId = await getNewTileId(page, existingTileIds);
          if (newTileId) {
            nextVideo.videoTileId = newTileId;
            nextVideo.state = 'GENERATING_VIDEO';
            console.log(`[SUBMIT] Submitted Video! Tile ID: ${newTileId}`);
            countSubmitted++;
            saveState(statePath, scenesState);
          } else {
            console.error(`[ERROR] Timeout waiting for new video tile for ${nextVideo.scene.id}`);
          }
        } catch (err) {
          console.error(`[ERROR] Submission error for video ${nextVideo.scene.id}:`, err.message);
        } finally {
          releaseLock();
          await delay(2000);
        }
      }
      
      // Submit new image generations
      const nextImage = scenesState.find(s => s.state === 'PENDING_IMAGE');
      if (nextImage && activeTotal() < maxConcurrent && countSubmitted < limit) {
        await acquireLock();
        try {
          console.log(`\n[PIPELINE] Submitting Image for scene ${nextImage.scene.id}...`);
          const existingTileIds = await getExistingTileIds(page);
          
          // Using Banana 2 Lite as requested by user to check for error rate improvement
          await setModel(page, '🍌 Nano Banana 2 Lite');
          await setBatchSizeToOne(page);
          await clearReferenceImages(page);
          
          console.log(`[PROMPT] Image prompt: "${nextImage.scene.imagePrompt}"`);
          await insertPromptViaSlate(page, nextImage.scene.imagePrompt);
          await delay(1200); // Wait for slate binding
          
          await enforceCooldown();
          await clickSubmitButton(page);
          lastSubmitTime = Date.now();
          
          const newTileId = await getNewTileId(page, existingTileIds);
          if (newTileId) {
            nextImage.imageTileId = newTileId;
            nextImage.state = 'GENERATING_IMAGE';
            console.log(`[SUBMIT] Submitted Image! Tile ID: ${newTileId}`);
            countSubmitted++;
            saveState(statePath, scenesState);
          } else {
            console.error(`[ERROR] Timeout waiting for new image tile for ${nextImage.scene.id}`);
          }
        } catch (err) {
          console.error(`[ERROR] Submission error for image ${nextImage.scene.id}:`, err.message);
        } finally {
          releaseLock();
          await delay(2000);
        }
      }
    }
    
    // 3. Print ongoing status dashboard
    const completedCount = scenesState.filter(s => s.state === 'COMPLETED').length;
    const failedCount = scenesState.filter(s => s.state === 'FAILED').length;
    const pendingCount = scenesState.filter(s => s.state === 'PENDING_IMAGE' || s.state === 'PENDING_VIDEO').length;
    
    process.stdout.write(
      `Progress: ${completedCount}/${scenesState.length} complete, ${failedCount} failed, ${pendingCount} pending | ` +
      `Active: ${activeImages()} images, ${activeVideos()} videos (Total: ${activeTotal()}/${maxConcurrent})\r`
    );
    
    const allDone = scenesState.every(s => s.state === 'COMPLETED' || s.state === 'FAILED');
    const limitReachedAndDone = (countSubmitted >= limit && activeImages() === 0 && activeVideos() === 0);
    
    if (allDone || limitReachedAndDone) {
      pipelineFinished = true;
      console.log('\n');
    } else {
      await delay(5000);
    }
  }
  
  await browser.disconnect();
  console.log('\n[DONE] Pipeline completed successfully!');
}

main().catch(err => {
  console.error('\n[FATAL ERROR] Pipeline terminated:', err);
  process.exit(1);
});
