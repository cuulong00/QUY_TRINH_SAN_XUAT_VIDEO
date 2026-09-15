# Oral QA Report — Ngân Hàng Lấy Tiền Đâu Cho 18 Siêu Dự Án?
Ngày QA: 2026-06-25

**Chuyên gia:** The Voice Architect
**Tổng số chương kiểm tra:** 6
**Trạng thái nhịp điệu:** Rất mượt mà, tính nhạc vần tốt.
**Độ dài câu:** 100% câu dưới 135 ký tự (an toàn hơn rất nhiều so với giới hạn cứng 150 ký tự), không gây hụt hơi cho người đọc hay mô hình TTS.

## Kết quả rà soát chi tiết:

### 1. Rút ngắn câu nặng & Cải thiện nhịp thở
- Các câu phức tạp có nhiều mệnh đề phụ hoặc trạng ngữ dài đều đã được chia nhỏ thành các câu staccato đơn giản, có dấu chấm câu rõ ràng.
- Đã sửa từ "ngày mốc một tháng bảy" thành "ngày một tháng bảy" (Chương 3) để câu trôi chảy hơn.
- Đã sửa từ "không phẩy chừng tám điểm phần trăm" thành "không phẩy sáu đến không phẩy tám điểm phần trăm" (Chương 3) để bảo đảm đúng số liệu và đọc không vấp.

### 2. Giảm mật độ từ ngữ hàn lâm
- Các thuật ngữ kỹ thuật khó đều đi kèm các ẩn dụ sinh động và gần gũi với đời sống:
  - Room tín dụng được ẩn dụ hóa là "tấm giấy phép chi tiêu".
  - Chênh lệch kỳ hạn được so sánh với việc "xây nhà dài hạn bằng khoản vay ngắn hạn".
  - Thị trường liên ngân hàng được so sánh với "chợ bán buôn dòng tiền", còn lãi suất vay cá nhân là "giá bán lẻ".
  - Trái phiếu ngân hàng được giải nghĩa là hành động "đi mua thanh khoản dài hạn từ xã hội".

### 3. Voice DNA & Bridge Check
- Mối nối của tất cả các chương đều tuân thủ chặt chẽ **Luật But/Therefore** và tạo được **Subconscious Loop (Vòng lặp tiềm thức)** để lôi cuốn người nghe sang chương tiếp theo mà không sử dụng các từ ngữ transition sáo rỗng.
- Bảo vệ tuyệt đối các câu vàng (Golden Lines) đã đăng ký trong `07_golden_lines.md`.

## Verdict: DUYỆT (Kịch bản sạch, nhịp điệu tối ưu cho lồng tiếng/TTS)
