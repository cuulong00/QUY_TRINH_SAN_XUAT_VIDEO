---
description: Quy trình kiểm toán kịch bản tự động hóa bằng Google Search AI Mode (udm=50) cho kênh Dòng Chảy.
---

# Quy Trình Kiểm Toán Kịch Bản (Google Search AI Mode)

Quy trình này sử dụng công cụ tự động hóa thông qua Google Search ở chế độ AI Overviews trực diện (`udm=50`) để thực hiện kiểm toán toàn diện tính đúng đắn của số liệu vĩ mô, mốc thời gian chính sách, và các cam kết an toàn tài chính trong kịch bản.

## 1. Chuẩn Bị Môi Trường (macOS)
Đảm bảo bạn đã cài đặt các thư viện cần thiết bằng lệnh:
```bash
python3 -m pip install playwright --break-system-packages
python3 -m playwright install chromium
```

## 2. Các Lệnh Thực Thi Chính
Quy trình hỗ trợ chạy tự động qua terminal. Thực hiện lệnh tại thư mục gốc của dự án:

### A. Audit một chương cụ thể (Chế độ Tương tác)
```bash
python3 scripts/tools/google_ai_audit.py episodes/thu-tuong-di-long-thanh --chapter 1
```
*Hệ thống sẽ sao chép nội dung chương vào Clipboard. Bạn chỉ cần dán (Cmd+V) vào giao diện Chrome đã mở, gửi đi, và nhấn Enter ở terminal sau khi AI sinh xong kết quả.*

### B. Audit toàn bộ các chương tự động (Không cần nhấn Enter)
```bash
python3 scripts/tools/google_ai_audit.py episodes/thu-tuong-di-long-thanh --all --auto
```
*Script sẽ tự động dán, gửi và chờ AI Overviews trả về câu trả lời cho từng chương (chương 1 -> chương 7) trong cùng một luồng hội thoại duy nhất.*

### C. Chạy ngầm (Headless Mode)
Nếu không muốn hiển thị giao diện Chromium:
```bash
python3 scripts/tools/google_ai_audit.py episodes/thu-tuong-di-long-thanh --all --auto --headless
```

## 3. Nguyên Lý Hoạt Động Của Hệ Thống Kiểm Toán
*   **Đơn Tab & Đơn Session:** Script chỉ mở trình duyệt đúng một lần và duy trì một tab/session duy nhất. Việc này giúp lưu trữ ngữ cảnh nhất quán giữa các chương và tránh bị Google chặn bot.
*   **Định Vị Chuyên Gia (Setup Prompt):** Script tự động thiết lập vai trò của AI là **Macroeconomic & Financial Auditor** để tập trung đối chiếu internet các báo cáo vĩ mô, dữ liệu doanh nghiệp và chính sách kinh tế mới nhất (2025-2026).
*   **Phạm Vi Kiểm Toán (Focus):** Chỉ tập trung đối chiếu thực tế về số liệu, sự kiện, các kết luận kinh tế và các rủi ro pháp lý/an toàn tài chính thực chất. TUYỆT ĐỐI không đánh giá hay chỉnh sửa kỹ thuật như TTS, độ dài câu thoại hay số lượng ký tự. ĐỒNG THỜI, tuyệt đối tôn trọng và bảo vệ tính nghệ thuật, các so sánh ẩn dụ, nhân hóa kịch tính đặc trưng của kênh Dòng Chảy (như "con cá mập", "cái ao", "rửa xuất xứ", "né thuế", "trận chiến sinh tử"), không tự ý gắn cờ hay đề xuất chỉnh sửa văn phong nếu tính chính xác của dữ liệu và sự thật đã được đảm bảo.
*   **Tự Động Lắng Nghe Văn Bản:** Sử dụng mã JavaScript để theo dõi độ tăng trưởng ký tự phản hồi trên giao diện, nhận diện thời điểm AI sinh chữ xong mà không cần set cứng thời gian chờ.

## 4. Xử Lý Khi Gặp CAPTCHA / Đăng Nhập
*   Nếu Google yêu cầu xác minh CAPTCHA khi bắt đầu, script sẽ dừng và hiển thị cảnh báo đỏ trên terminal.
*   Bạn chỉ cần nhấp chuột giải CAPTCHA ngay trên cửa sổ Chrome vừa xuất hiện.
*   Sau khi giải xong, script sẽ tự động nhận diện và tiếp tục tiến trình audit mà không cần nhấn thêm bất kỳ phím nào ở terminal.

## 5. Kết Quả Đầu Ra
*   Các file kết quả audit chi tiết từng chương: `episodes/[slug]/google_ai_audit_XX.md`.
*   Ảnh chụp màn hình kết quả audit thực tế: `episodes/[slug]/google_ai_audit_final_XX.png`.
*   Báo cáo tổng hợp kiểm toán toàn tập phim: `episodes/[slug]/google_ai_audit_results.md`.

---
*Quy trình này đã được tinh chỉnh hoàn toàn để phục vụ cho các tiêu chuẩn an toàn tài chính và dữ liệu kinh tế vĩ mô của Dòng Chảy.*
