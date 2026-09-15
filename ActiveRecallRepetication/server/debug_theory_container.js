import puppeteer from 'puppeteer-core';

async function run() {
  console.log('🔌 Connecting...');
  const browser = await puppeteer.connect({
    browserURL: 'http://127.0.0.1:9222',
    defaultViewport: null
  });
  
  const page = await browser.newPage();
  const url = 'https://tak12.com/ex/165/tong-on-tieng-viet-vao-6/luyen-theo-chuyen-de/t/803/tu-loai-danh-tu-dong-tu-tinh-tu-dai-tu-ket-tu?from=/ex/165/tong-on-tieng-viet-vao-6/luyen-theo-chuyen-de';
  await page.goto(url, { waitUntil: 'networkidle2' });
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  const ancestors = await page.evaluate(() => {
    const headings = Array.from(document.querySelectorAll('*')).filter(el => el.innerText && el.innerText.trim() === 'DANH TỪ:');
    if (headings.length === 0) return [];
    
    const list = [];
    let curr = headings[0].parentElement;
    while (curr && curr !== document.body) {
      list.push({
        tagName: curr.tagName,
        className: curr.className,
        id: curr.id,
        attributes: Array.from(curr.attributes).map(attr => `${attr.name}="${attr.value}"`)
      });
      curr = curr.parentElement;
    }
    return list;
  });
  
  console.log('Ancestors of theory heading:', ancestors);
  
  // Let's also print the selector for the theory tab pane
  const tabPaneInfo = await page.evaluate(() => {
    // Look for elements with "Tóm tắt lý thuyết"
    // Let's see if there is an element with class tab, pane, active, etc.
    const panes = Array.from(document.querySelectorAll('.tab, .pane, [class*="tab"], [class*="pane"]'));
    return panes.map(p => ({
      tagName: p.tagName,
      className: p.className,
      id: p.id,
      textSnippet: p.innerText ? p.innerText.slice(0, 100).trim() : ''
    })).filter(p => p.textSnippet.length > 0);
  });
  
  console.log('Tab Panes:', tabPaneInfo);
  
  await page.close();
  process.exit(0);
}

run();
