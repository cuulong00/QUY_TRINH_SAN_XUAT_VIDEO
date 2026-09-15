import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

async function run() {
  console.log("🚀 Launching browser to search on Bing...");
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  const query = 'Vingroup "doanh nghiệp kiến tạo" ĐHĐCĐ 2026';
  console.log(`🔍 Searching Bing for: "${query}"`);
  await page.goto(`https://www.bing.com/search?q=${encodeURIComponent(query)}`);
  await page.waitForTimeout(3000);

  // Extract Bing search results
  const results = await page.evaluate(() => {
    const items = [];
    const elements = document.querySelectorAll('li.b_algo');
    elements.forEach(el => {
      const titleEl = el.querySelector('h2 a');
      const snippetEl = el.querySelector('.b_caption p, .b_snippet p, p');
      if (titleEl) {
        items.push({
          title: titleEl.innerText,
          url: titleEl.href,
          snippet: snippetEl ? snippetEl.innerText : ''
        });
      }
    });
    return items;
  });

  console.log(`📊 Found ${results.length} search results on Bing.`);
  
  if (results.length === 0) {
    console.log("⚠️ No results found on Bing. Taking screenshot for debug...");
    await page.screenshot({ path: 'bing_debug.png' });
    console.log("📸 Saved screenshot to bing_debug.png");
  }

  // Format into a research document
  let docContent = `# BÁO CÁO NGHIÊN CỨU BỔ SUNG: ĐỊNH HƯỚNG "DOANH NGHIỆP KIẾN TẠO" CỦA VINGROUP TẠI ĐHĐCĐ 2026\n\n`;
  docContent += `*Ngày thu thập tài liệu: 18/07/2026*\n`;
  docContent += `*Nguồn tra cứu: Bing Search (Tin tức chính thống về ĐHĐCĐ 2026)*\n\n`;
  docContent += `## I. Các nguồn tin thu thập được\n\n`;

  for (let i = 0; i < Math.min(results.length, 5); i++) {
    const res = results[i];
    docContent += `### Nguồn ${i + 1}: ${res.title}\n`;
    docContent += `- **Đường dẫn:** ${res.url}\n`;
    docContent += `- **Tóm tắt tin tức:** ${res.snippet}\n\n`;
    
    // Attempt to crawl the content of the top 2 articles
    if (i < 2) {
      try {
        console.log(`🌐 Crawling article content: ${res.url}`);
        const articlePage = await context.newPage();
        await articlePage.goto(res.url, { timeout: 15000, waitUntil: 'domcontentloaded' });
        await articlePage.waitForTimeout(3000);
        const bodyText = await articlePage.evaluate(() => {
          const scripts = document.querySelectorAll('script, style, iframe, header, footer, nav, ads');
          scripts.forEach(s => s.remove());
          return document.body.innerText.substring(0, 3000); // Grab first 3000 chars of core content
        });
        docContent += `#### Nội dung chi tiết trích lục:\n\`\`\`text\n${bodyText}\n\`\`\`\n\n`;
        await articlePage.close();
      } catch (err) {
        console.log(`⚠️ Failed to crawl details for ${res.url}: ${err.message}`);
      }
    }
  }

  const targetPath = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/vingroup-van-cuoc-dia-chinh-tri/research_vault/009-vingroup-dinh-huong-doanh-nghiep-kien-tao-dhdcd-2026.md";
  fs.writeFileSync(targetPath, docContent);
  console.log(`✅ Saved research document to: ${targetPath}`);

  await browser.close();
}

run().catch(err => console.error(err));
