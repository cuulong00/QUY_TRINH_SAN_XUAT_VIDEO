# Hướng Dẫn Kỹ Thuật: Tạo & Lấy Never-Expiring Page Access Token

Để script có thể upload video dài và đăng bài tự động mà không bao giờ bị hết hạn token giữa chừng, anh cần tạo một **Never-Expiring Page Access Token** theo các bước sau:

---

## 🛠️ Bước 1: Tạo Meta App (Nếu chưa có)
1. Truy cập [developers.facebook.com](https://developers.facebook.com).
2. Vào **My Apps** > **Create App**.
3. Chọn Loại ứng dụng: **Business** (Doanh nghiệp).
4. Đặt tên App (ví dụ: `ContentDistributionSystem`) và nhấn **Create App**.

---

## 🛠️ Bước 2: Tạo User Token có đủ quyền tại Graph API Explorer
1. Truy cập công cụ [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Tại mục **Meta App**, chọn App anh vừa tạo ở Bước 1.
3. Tại mục **User or Page**, chọn **User Token**.
4. Tại mục **Add a Permission**, thêm các quyền bắt buộc sau:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `publish_video`
5. Nhấn **Generate Access Token** và đăng nhập cấp quyền cho tài khoản Facebook quản trị Fanpage.

---

## 🛠️ Bước 3: Đổi thành Long-Lived User Token (60 ngày)
Chạy lệnh sau trong Terminal (thay thế các giá trị tương ứng):
```bash
curl -X GET "https://graph.facebook.com/v20.0/oauth/access_token?\
grant_type=fb_exchange_token&\
client_id={YOUR_APP_ID}&\
client_secret={YOUR_APP_SECRET}&\
fb_exchange_token={SHORT_LIVED_USER_TOKEN}"
```
Kết quả trả về một JSON có trường `access_token` (đây là Long-Lived User Token có hạn 60 ngày).

---

## 🛠️ Bước 4: Lấy Never-Expiring Page Access Token (Vĩnh viễn)
Dùng Long-Lived User Token vừa lấy ở Bước 3 để gọi endpoint lấy danh sách Page:
```bash
curl -X GET "https://graph.facebook.com/v20.0/me/accounts?access_token={LONG_LIVED_USER_TOKEN}"
```
Kết quả trả về danh sách các Fanpage anh quản trị:
```json
{
  "data": [
    {
      "access_token": "EAA...", // <-- ĐÂY LÀ TOKEN VĨNH VIỄN CỦA FANPAGE!
      "category": "Podcast",
      "name": "Góc Nhìn Đa Chiều",
      "id": "123456789012345"    // <-- ĐÂY LÀ FB_PAGE_ID
    }
  ]
}
```
> [!IMPORTANT]
> Token lấy từ endpoint `/me/accounts` bằng một Long-Lived User Token sẽ **KHÔNG BAO GIỜ HẾT HẠN** (Never Expire), trừ khi anh đổi mật khẩu tài khoản cá nhân hoặc tự thu hồi quyền của App!

---

## 🛠️ Bước 5: Cấu hình vào file `.env`
Điền 2 giá trị vào `/Users/pro16/Documents/VideoProject/FacebookChannel/.env`:
```ini
FB_PAGE_ID=123456789012345
FB_PAGE_ACCESS_TOKEN=EAA...
FB_API_VERSION=v20.0
FB_UPLOAD_CHUNK_SIZE_MB=8
```
Sau đó kiểm tra lại bằng:
```bash
python scripts/check_page.py
```
