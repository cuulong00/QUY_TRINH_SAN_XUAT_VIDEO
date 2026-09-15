import { queryGem } from './automation.js';

async function test() {
  const gemUrl = 'https://gemini.google.com/gem/ae781ffc92e7';
  const prompt = 'Xin chào, bạn có thể tự giới thiệu ngắn gọn không? Bạn được thiết lập để làm gì?';

  console.log('🧪 Đang chạy thử nghiệm truy vấn Gemini Gem...');
  console.log(`- URL: ${gemUrl}`);
  console.log(`- Prompt: "${prompt}"`);
  console.log('--------------------------------------------------');

  try {
    // Chạy ở chế độ không ẩn danh (headless: false) lần đầu để dễ kiểm tra
    const response = await queryGem(gemUrl, prompt, false);
    console.log('\n🎉 KẾT QUẢ TRẢ VỀ THÀNH CÔNG:');
    console.log(response);
    console.log('--------------------------------------------------');
  } catch (error: any) {
    console.error('\n❌ Thử nghiệm THẤT BẠI:', error.message || error);
  }
}

test();
