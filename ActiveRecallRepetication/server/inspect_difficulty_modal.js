import puppeteer from 'puppeteer-core';

const delay = ms => new Promise(res => setTimeout(res, ms));

const inspect = async () => {
  try {
    const browser = await puppeteer.connect({
      browserURL: 'http://127.0.0.1:9222',
      defaultViewport: null
    });
    
    const pages = await browser.pages();
    const page = pages.find(p => p.url().includes('tak12.com/ex/'));
    
    if (!page) {
      console.error('❌ Could not find any active TAK12 tab in your Chrome browser. Please open a TAK12 practice tab.');
      process.exit(1);
    }
    
    console.log(`📍 Connected to tab: ${page.url()}`);
    
    // Click "Chọn độ khó" button
    console.log('Clicking "Chọn độ khó" button...');
    await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll('button, a'));
      const target = buttons.find(b => b.innerText.trim() === 'Chọn độ khó');
      if (target) {
        target.click();
        return true;
      }
      return false;
    });
    
    await delay(2000);
    
    // Dump HTML of the modal
    const modalHtml = await page.evaluate(() => {
      // Find modal container by looking for common modal classes or headers
      const header = Array.from(document.querySelectorAll('h1, h2, h3, h4, div')).find(el => el.innerText && el.innerText.includes('Chủ điểm:'));
      if (header) {
        // Return parent hierarchy or container
        let parent = header;
        for (let i = 0; i < 5; i++) {
          if (parent.parentElement && (parent.parentElement.classList.contains('modal') || parent.parentElement.classList.contains('dialog') || parent.parentElement.style.position === 'fixed')) {
            parent = parent.parentElement;
            break;
          }
          parent = parent.parentElement || parent;
        }
        return parent.outerHTML;
      }
      return document.body.innerHTML;
    });
    
    console.log('--- Modal HTML Dump ---');
    console.log(modalHtml.slice(0, 5000));
    
    // Let's also print specific inputs inside the modal
    const inputsInfo = await page.evaluate(() => {
      const inputs = Array.from(document.querySelectorAll('input, label, button'));
      return inputs.map(el => ({
        tag: el.tagName,
        type: el.type || '',
        name: el.name || '',
        className: el.className || '',
        id: el.id || '',
        text: el.innerText || el.value || '',
        placeholder: el.placeholder || '',
        onclick: el.getAttribute('onclick') || ''
      }));
    });
    
    console.log('\n--- Interactive Elements inside Modal ---');
    console.log(inputsInfo.filter(el => el.text.includes('Dễ') || el.text.includes('Trung bình') || el.text.includes('Khó') || el.text.includes('Luyện ngay') || el.name || el.type === 'checkbox'));
    
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

inspect();
