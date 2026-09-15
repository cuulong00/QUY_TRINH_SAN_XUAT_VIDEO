# Gemini Gems MCP Server

Mô hình hóa và kết nối các Gemini Gems của bạn (ví dụ: `https://gemini.google.com/gem/ae781ffc92e7`) vào hệ thống AI Agents hoặc Claude Desktop qua giao thức **Model Context Protocol (MCP)**.

Dự án sử dụng thư viện tự động hóa trình duyệt `patchright` (Playwright đã sửa đổi chống bot) để điều khiển Chrome chạy bằng Profile thực tế, duy trì phiên đăng nhập và truy vấn dữ liệu từ các Gem tùy chỉnh.

## Tính năng
- **Persistent Session Profile:** Không cần lưu cookie thủ công, Playwright tự động duy trì phiên đăng nhập qua thư mục chứa profile riêng tại `~/Library/Application Support/gemini-gems-mcp/chrome_profile`.
- **Chế độ Xác thực Thông minh:** Mở trình duyệt UI để đăng nhập Google thủ công lần đầu, sau đó tự động hóa hoàn toàn ở chế độ ẩn danh (headless).
- **Polling Ổn định:** Tự động lắng nghe và phát hiện trạng thái hoàn thành sinh văn bản của Gemini trước khi thu thập dữ liệu phản hồi.

## Cài đặt & Chuẩn bị

1. **Cài đặt các thư viện Node.js:**
   ```bash
   npm install
   ```

2. **Cài đặt trình duyệt Chromium hỗ trợ bởi Patchright:**
   ```bash
   npx patchright install chromium
   ```

3. **Xác thực tài khoản Google (LƯU Ý QUAN TRỌNG):**
   Bạn bắt buộc phải thực hiện bước này đầu tiên để tạo phiên đăng nhập:
   ```bash
   npm run auth
   ```
   Cửa sổ trình duyệt Chromium sẽ hiện lên. Bạn hãy đăng nhập tài khoản Google của mình, truy cập vào `gemini.google.com` để kiểm tra, sau đó tắt cửa sổ trình duyệt đó đi để lưu lại thông tin phiên (Session).

## Chạy thử nghiệm độc lập
Để test khả năng truy vấn tự động của code:
```bash
npx tsx src/test-query.ts
```
Script sẽ tự động mở trang Gem, điền câu hỏi mẫu, gửi và in kết quả ra màn hình console.

## Cấu hình tích hợp MCP Client

### 1. Claude Desktop
Thêm đoạn cấu hình sau vào tệp `claude_desktop_config.json` (thường nằm ở `~/Library/Application Support/Claude/claude_desktop_config.json` trên macOS):

```json
{
  "mcpServers": {
    "gemini-gems": {
      "command": "node",
      "args": [
        "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/tools/gemini-gems-mcp/dist/index.js"
      ]
    }
  }
}
```

### 2. Sử dụng các Tools được xuất bản qua MCP:
Sau khi khởi động, Server sẽ cung cấp 2 công cụ chính:
- **`gemini_gems_auth`**: Chạy lại trình duyệt có giao diện nếu cookie hết hạn hoặc bạn cần đăng nhập tài khoản khác.
- **`query_gem`**: 
  - `gemUrl` *(Bắt buộc)*: Link của Gem cụ thể (ví dụ: `https://gemini.google.com/gem/ae781ffc92e7`).
  - `prompt` *(Bắt buộc)*: Câu hỏi của bạn.
  - `headless` *(Tùy chọn)*: Mặc định là `true`. Đặt là `false` nếu muốn xem trực tiếp robot thao tác trên trình duyệt.
