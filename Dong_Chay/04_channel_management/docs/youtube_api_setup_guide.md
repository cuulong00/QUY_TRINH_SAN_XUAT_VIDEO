# Hướng dẫn Thiết lập YouTube API cho Dòng Chảy Content OS

Để tôi có thể tự động hóa việc đọc bình luận, kéo dữ liệu phân tích và quản lý kênh, bạn cần cấp thông tin xác thực (Credentials). Hãy làm theo các bước sau, quá trình này mất khoảng 5 phút.

### Bước 1: Tạo dự án Google Cloud
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2. Đăng nhập bằng tài khoản Google quản lý kênh YouTube Dòng Chảy.
3. Nhấp vào menu **chọn dự án** ở góc trên cùng bên trái (bên phải logo Google Cloud), chọn **New Project** (Dự án mới).
4. Đặt tên dự án là `Dòng Chảy-Manager` (hoặc tên bất kỳ) và nhấp **Create**.
5. Đợi một lát để Google tạo dự án. Sau đó, nhấp vào menu chọn dự án lần nữa và **chọn đúng dự án bạn vừa tạo**.

### Bước 2: Bật YouTube APIs
1. Mở menu thanh điều hướng bên trái ☰ > **APIs & Services** > **Library**.
2. Tại ô tìm kiếm, nhập `YouTube Data API v3`. Nhấp vào kết quả và chọn **Enable** (Bật).
3. Quay lại tab Library, tiếp tục tìm `YouTube Analytics API`. Nhấp vào kết quả và chọn **Enable** (Bật).

### Bước 3: Thiết lập Màn hình đồng ý OAuth (OAuth Consent Screen)
*Lưu ý: Đây là màn hình sẽ hiện ra để hỏi bạn có đồng ý cấp quyền cho ứng dụng hay không.*
1. Mở menu bên trái > **APIs & Services** > **OAuth consent screen**.
2. Chọn loại User Type là **External** (Bên ngoài) và bấm **Create**.
3. Điền các thông tin cơ bản bắt buộc:
   - **App name:** `Dòng Chảy Manager`
   - **User support email:** (Chọn email của bạn từ menu thả xuống)
   - **Developer contact information:** (Nhập email của bạn)
4. Bấm **Save and Continue** cho phần *App information*, *Scopes* (bỏ qua không cần điền thêm).
5. Tới phần **Test users** (Người dùng thử nghiệm): Nhấp **+ Add Users** và nhập **chính xác email quản lý kênh YouTube của bạn** vào đây. Đây là bước rất quan trọng để cấp phép.
6. Bấm **Save and Continue** cho đến hết.

### Bước 4: Tạo Tệp thông tin xác thực (Credentials)
1. Ở menu bên trái, nhấp vào tab **Credentials**.
2. Nhấp vào **+ Create Credentials** ở phía trên cùng màn hình, chọn **OAuth client ID**.
3. Ở mục **Application type**, hãy chọn **Desktop app** (Ứng dụng dành cho máy tính để bàn).
4. Ở mục Name, bạn có thể để nguyên hoặc đặt là `Antigravity Python App`, sau đó nhấp **Create**.
5. Một hộp thoại sẽ hiện lên báo thành công. Nhấp vào nút **Download JSON** (biểu tượng tải xuống) để tải tệp thông tin xác thực về máy.
6. Đổi tên tệp vừa tải về thành: `credentials.json`.

### Bước 5: Đưa vào Content OS
1. Bạn hãy copy tệp `credentials.json` đó và dán thẳng vào thư mục gốc dự án của chúng ta tại đường dẫn:
   `/Users/pro16/Documents/VideoProject/Dòng Chảy/credentials.json`
2. Sau khi đã chép tệp xong, hãy quay lại chat và báo cho tôi biết là **"Đã làm xong"**.

Sau khi bạn hoàn tất, tôi sẽ viết một đoạn mã Python ngắn để kiểm tra kết nối và kéo thử 5 bình luận mới nhất về cho bạn xem!
