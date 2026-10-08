import { debugLog } from './debug-log.js';
import { chromium } from 'patchright';
import fs from 'fs';
import path from 'path';

export const USER_DATA_DIR = '/Users/pro16/Library/Application Support/gemini-gems-mcp/chrome_profile';

// Hàm dọn dẹp các lock files của Chrome để tránh xung đột khi chạy
export function cleanLockFiles() {
  const lockFiles = ['SingletonLock', 'SingletonSocket', 'SingletonCookie'];
  for (const file of lockFiles) {
    const lockPath = path.join(USER_DATA_DIR, file);
    if (fs.existsSync(lockPath)) {
      try {
        fs.unlinkSync(lockPath);
        debugLog(`[Cleaner] Đã xóa lock file: ${file}`);
      } catch (err: any) {
        debugLog(`[Cleaner] Không thể xóa lock file ${file}:`, err.message);
      }
    }
  }
}

// Hàm chạy xác thực thủ công (Headed Mode)
export async function runAuth() {
  cleanLockFiles();
  debugLog('🚀 Đang khởi động trình duyệt Chromium có giao diện...');
  
  const browser = await chromium.launchPersistentContext(USER_DATA_DIR, {
    headless: false,
    viewport: { width: 1280, height: 800 }
  });

  const page = browser.pages()[0] || await browser.newPage();
  debugLog('📌 Đang chuyển hướng đến Gemini...');
  await page.goto('https://gemini.google.com/', { waitUntil: 'domcontentloaded' });

  debugLog('\n==================================================================');
  debugLog('Cửa sổ trình duyệt Chromium đã được mở.');
  debugLog('Hãy thực hiện đăng nhập tài khoản Google của bạn.');
  debugLog('Sau khi đăng nhập thành công và nhìn thấy trang chủ Gemini,');
  debugLog('hãy ĐÓNG CỬA SỔ TRÌNH DUYỆT này để lưu phiên làm việc.');
  debugLog('==================================================================\n');

  await new Promise<void>((resolve) => {
    browser.on('close', () => {
      debugLog('🔌 Trình duyệt đã được đóng. Phiên đăng nhập đã được lưu.');
      resolve();
    });
  });
}

// Hàm gửi truy vấn đến Gem và trích xuất câu trả lời (Headless mặc định)
export async function queryGem(gemUrl: string, prompt: string, headless = true): Promise<string> {
  cleanLockFiles();
  debugLog(`🚀 Đang khởi động trình duyệt (headless: ${headless})...`);
  
  const browser = await chromium.launchPersistentContext(USER_DATA_DIR, {
    headless: headless,
    viewport: { width: 1280, height: 800 }
  });

  const page = await browser.newPage();
  
  try {
    debugLog(`📌 Đang truy cập Gem: ${gemUrl}`);
    await page.goto(gemUrl, { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(3000); // Chờ ổn định nhẹ

    // Kiểm tra xem đã đăng nhập chưa bằng cách tìm avatar hoặc chat box
    const isLoggedIn = await page.evaluate(() => {
      // Nếu thấy nút đăng nhập hoặc nút Sign In thì tức là chưa log
      const loginBtn = document.querySelector('a[href*="login"], a[href*="signin"]');
      return !loginBtn;
    });

    if (!isLoggedIn) {
      throw new Error('Chưa đăng nhập tài khoản Google. Vui lòng chạy lệnh "npm run auth" trước để xác thực!');
    }

    debugLog('💬 Đang định vị ô nhập liệu Chatbox...');
    // Cố gắng tìm ô chat bằng nhiều selector dự phòng
    const chatInputSelectors = [
      'rich-textarea p',
      'div[contenteditable="true"]',
      'textarea[placeholder*="Nhập"]',
      'textarea[placeholder*="Enter"]',
      '[role="textbox"]'
    ];

    let chatInput = null;
    for (const sel of chatInputSelectors) {
      try {
        const el = page.locator(sel).first();
        if (await el.isVisible({ timeout: 2000 })) {
          chatInput = el;
          break;
        }
      } catch (e) {}
    }

    if (!chatInput) {
      // Lưu ảnh màn hình để debug
      const debugPic = path.join(process.cwd(), 'debug_error.png');
      await page.screenshot({ path: debugPic });
      throw new Error(`Không tìm thấy ô nhập liệu của Gemini. Đã lưu ảnh chụp debug tại: ${debugPic}`);
    }

    debugLog('✍️ Đang nhập câu hỏi...');
    await chatInput.click();
    await chatInput.fill(prompt);
    await page.waitForTimeout(1000);

    debugLog('📤 Đang gửi tin nhắn...');
    // Thử nhấn nút gửi trước, nếu không được thì nhấn Enter
    const sendBtnSelectors = [
      'button[aria-label*="Send" i]',
      'button[aria-label*="Gửi" i]',
      'button.send-button',
      '.send-button-container button'
    ];

    let clickedSend = false;
    for (const sel of sendBtnSelectors) {
      try {
        const el = page.locator(sel).first();
        if (await el.isVisible({ timeout: 2000 }) && !(await el.isDisabled())) {
          await el.click();
          clickedSend = true;
          break;
        }
      } catch (e) {}
    }

    if (!clickedSend) {
      await page.keyboard.press('Enter');
      debugLog('  Đã gửi tin nhắn qua phím Enter');
    } else {
      debugLog('✅ Đã click nút gửi thành công');
    }

    debugLog('⏳ Đang chờ phản hồi từ Gemini Gems (tối đa 120s)...');
    
    // Theo dõi phản hồi ổn định (Polling)
    const responseSelectors = [
      'message-content',
      '.message-content',
      '.model-response-text',
      '.response-content'
    ];

    let responseText = '';
    let lastResponse = '';
    let stableCount = 0;
    let attempts = 0;

    while (attempts < 120) {
      await page.waitForTimeout(1000);
      attempts++;

      let currentResponse = '';
      for (const sel of responseSelectors) {
        try {
          const responses = page.locator(sel);
          const count = await responses.count();
          if (count > 0) {
            currentResponse = await responses.nth(count - 1).innerText();
            if (currentResponse && currentResponse.length > 10) {
              break;
            }
          }
        } catch (e) {}
      }

      if (currentResponse) {
        currentResponse = currentResponse.trim();
        const lower = currentResponse.toLowerCase();
        
        // Kiểm tra xem Gemini có đang trong trạng thái sinh chữ (loading/generating) không
        const isGenerating = lower.includes('đang tạo') || 
                             lower.includes('đang xử lý') || 
                             lower.includes('generating') || 
                             currentResponse.endsWith('...');

        if (currentResponse === lastResponse && !isGenerating) {
          stableCount++;
          // Cần ổn định liên tục trong 4 giây để chắc chắn là đã hoàn thành
          if (stableCount >= 4) {
            debugLog(`✅ Đã nhận được câu trả lời hoàn chỉnh! Độ dài: ${currentResponse.length} ký tự.`);
            responseText = currentResponse;
            break;
          }
        } else {
          stableCount = 0;
          lastResponse = currentResponse;
          if (isGenerating) {
            debugLog(`⏳ Gemini đang sinh nội dung... (${currentResponse.length} ký tự)`);
          } else {
            debugLog(`⏳ Phản hồi cập nhật: ${currentResponse.length} ký tự...`);
          }
        }
      } else {
        debugLog('⏳ Đang đợi khung phản hồi xuất hiện...');
      }
    }

    if (!responseText) {
      // Nếu không tìm thấy, lấy toàn bộ văn bản của trang để chẩn đoán
      const bodyText = await page.innerText('body');
      const debugPic = path.join(process.cwd(), 'debug_timeout.png');
      await page.screenshot({ path: debugPic });
      throw new Error(`Timeout hoặc lỗi cào kết quả. Đã chụp màn hình tại ${debugPic}. Preview body: ${bodyText.substring(0, 500)}`);
    }

    return responseText;

  } finally {
    await browser.close();
    debugLog('🔌 Trình duyệt đã được đóng sạch.');
  }
}

// Chạy trực tiếp qua CLI khi gọi `npm run auth`
if (process.argv.includes('--auth')) {
  runAuth().catch(debugLog);
}