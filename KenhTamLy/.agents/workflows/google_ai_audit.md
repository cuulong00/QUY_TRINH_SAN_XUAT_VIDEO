---
description: Tự động chạy công cụ đối chiếu, kiểm chứng kịch bản qua chế độ Google Search AI Mode (udm=50)
---
1. Xác định thư mục của episode cần kiểm chứng (ví dụ: `episodes/vinfast-co-that-su-re`).
2. Xác minh xem người dùng muốn kiểm chứng toàn bộ kịch bản hay chỉ một chương cụ thể.
3. **Quy tắc Thiết lập Query Động (CRITICAL RULE):**
   - **TUYỆT ĐỐI CẤM** viết cứng (hardcode) nội dung query thiết lập ban đầu (`setup_prompt`) trong script cho mọi kịch bản video.
   - Script chạy audit bắt buộc phải tự động đọc và trích xuất thông tin chủ đề (`raw_topic`) và tóm tắt chủ đề từ file `01_topic_qualification.md` hoặc `03_brief.md` của chính episode đó để gửi bối cảnh chuẩn xác cho Google AI Search Mode SGE.
   - Nếu không có file mô tả, bắt buộc phải fallback về query tổng quan mở (generic open query) chứ không được chứa các từ khóa cụ thể của một kịch bản khác (tránh context bias).
4. Chạy công cụ audit qua Playwright:
   - Toàn bộ kịch bản: `python3 scripts/google_ai_audit.py episodes/[slug] --all`
   - Chỉ một chương: `python3 scripts/google_ai_audit.py episodes/[slug] --chapter [số_chương]`
5. Khi trình duyệt khởi chạy:
   - Nếu xuất hiện CAPTCHA của Google hoặc yêu cầu đăng nhập tài khoản Google, hãy tạm dừng và nhắc người dùng tự giải quyết trực quan trên màn hình.
   - Script sẽ tự động lắng nghe và tiếp tục khi ô nhập liệu SGE "Hỏi thêm" xuất hiện.
6. Sau khi hoàn thành, kiểm tra các tệp báo cáo được tạo ra tại thư mục episode:
   - `google_ai_audit_results.md` (Báo cáo tổng hợp)
   - `google_ai_audit_XX.md` (Báo cáo chi tiết từng chương)
   - `google_ai_audit_XX.png` (Ảnh chụp màn hình đối chiếu)
7. Sử dụng thông tin phản biện của AI Mode để hướng dẫn người dùng chỉnh sửa các số liệu bị sai lệch hoặc cập nhật các quy định pháp luật mới nhất vào kịch bản trước khi thực hiện thu âm.

