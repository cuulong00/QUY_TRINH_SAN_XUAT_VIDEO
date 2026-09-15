---
description: Tự động phân loại và gom video/hình ảnh tải về vào các thư mục ch1, ch2, ch3... theo từng chương.
---

# Quy Trình Tự Động Phân Loại Video Theo Chương (/organize_videos)

Quy trình này nhận đường dẫn thư mục tải về từ người dùng và tự động phân loại toàn bộ file video/ảnh vào các thư mục tương ứng theo cú pháp `ch1`, `ch2`, `ch3`, `ch4`, `ch5`...

---

### CÁC BƯỚC THỰC HIỆN CỦA AGENT:

1. **Xác định đường dẫn thư mục:**
   - Lấy đường dẫn thư mục người dùng cung cấp (ví dụ: `/Users/pro16/Downloads/longgiamvutru` hoặc `~/Downloads/...`).
   - Nếu người dùng chưa cung cấp đường dẫn, hỏi người dùng: *"Vui lòng cung cấp đường dẫn thư mục chứa video cần phân loại."*

2. **Chạy lệnh tự động phân loại:**
   - Thực thi lệnh với `BypassSandbox: true`:
     ```bash
     python3 scripts/tools/organize_chapters.py "<ĐƯỜNG_DẪN_THƯ_MỤC>"
     ```

3. **Báo cáo kết quả:**
   - Hiển thị bảng tổng kết số lượng file video đã được phân chia vào các thư mục `ch1/`, `ch2/`, `ch3/`, `ch4/`, `ch5/`...
   - Cảnh báo nếu có file nào không khớp định dạng để người dùng kiểm tra.
