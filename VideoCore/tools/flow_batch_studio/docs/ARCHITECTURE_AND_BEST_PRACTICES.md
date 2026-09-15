# 🏗️ KIẾN TRÚC HỆ THỐNG & KINH NGHIỆM THỰC CHIẾN GOOGLE FLOW

Tài liệu này giải thích chi tiết cơ chế vận hành của ứng dụng **Google Flow Batch Production Engine**, các giải pháp kỹ thuật chống lỗi và những kinh nghiệm quý giá từ cộng đồng nhà làm phim AI.

---

## 1. Cơ Chế Tải File Đích Duy Nhất (Target Deliverable Only)
* **Vấn đề thực tế:** Khi chạy 50–100 cảnh ở chế độ Ảnh + Video, nếu tải cả ảnh lẫn video sẽ làm rác ổ cứng hàng trăm file trung gian và gây quá tải trình duyệt.
* **Giải pháp:**
  - Ở chế độ `Image + Video (Chained)`: Ảnh sinh ra bởi `🍌 Nano Banana 2` được lưu dưới dạng `Blob` tạm trong bộ nhớ RAM. Sau khi truyền `Blob` này vào tham chiếu cho `Veo 3.1`, hệ thống **CHỈ TẢI DUY NHẤT FILE VIDEO (.mp4)**.
  - Ngay sau khi hoàn thành, gọi hàm `URL.revokeObjectURL(imageBlobUrl)` để dọn dẹp RAM, không lưu ảnh xuống đĩa.

---

## 2. Phòng Chống Treo Luồng (Zombie Task) Ở Veo 3.1 Lower Priority
* **Hiện tượng:** Model `Veo 3.1 - Lite [Lower Priority]` chạy trên hàng đợi chia sẻ tài nguyên. Vào giờ cao điểm, request có thể bị kẹt ở trạng thái `Generating...` suốt 15 phút mà không trả về kết quả.
* **Cơ chế Hard Timeout (240s):**
  - Mỗi tác vụ render video được gắn một đồng hồ đếm ngược 240 giây (4 phút).
  - Nếu hết 240s mà không nhận được video, hệ thống tự động ngắt kết nối (`AbortController`), tính là 1 lần lỗi và kích hoạt cơ chế Retry. Luồng được giải phóng ngay lập tức để xử lý cảnh khác.

---

## 3. Cơ Chế Cầu Dao Tự Ngắt (Circuit Breaker khi gặp lỗi 429)
* **Nguy cơ:** Khi chạy song song tối đa 6 luồng, nếu Google trả về mã lỗi `429 Too Many Requests` mà các luồng khác vẫn tiếp tục gửi request, tài khoản sẽ bị khóa tính năng tạo video từ 6–24 tiếng.
* **Hành vi Circuit Breaker:**
  - Khi bất kỳ 1 luồng nào gặp mã 429: Toàn bộ hàng đợi tự động chuyển sang trạng thái **PAUSED (TẠM DỪNG TOÀN DIỆN)** trong 60 giây.
  - Hiển thị đồng hồ đếm ngược hạ nhiệt. Sau 60s, hệ thống mới rón rén kích hoạt lại từng luồng một với độ trễ ngẫu nhiên (Jitter).

---

## 4. Chống Bot Detection Bằng Độ Trễ Ngẫu Nhiên (Staggered Jitter)
* **Nguyên lý:** Nếu 6 luồng được kích hoạt đồng thời hoặc cách nhau đúng một khoảng thời gian cố định (ví dụ 5.0s), hệ thống tường lửa của Google sẽ nhận diện là hành vi bot/script.
* **Giải pháp:** Giữa các lần kích hoạt luồng kế tiếp, hệ thống áp dụng hàm `delayRandom(min, max)` từ 3s đến 8s. Khoảng trễ ngẫu nhiên này mô phỏng hoàn hảo thao tác nhấp chuột của con người.

---

## 5. Tự Động Bỏ Qua Cảnh Đã Có Sẵn (Smart Skip)
* Tích hợp `window.showDirectoryPicker()`.
* Trước khi render một phân cảnh, hệ thống kiểm tra trong thư mục đã có file `CH01_SCXXX.mp4` chưa. Nếu đã có từ phiên trước, hệ thống tự động đánh dấu `Skipped` và chuyển sang cảnh tiếp theo, tiết kiệm 100% chi phí và thời gian.
