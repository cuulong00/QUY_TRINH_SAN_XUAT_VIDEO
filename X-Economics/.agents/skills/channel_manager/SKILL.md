---
name: Channel Management & Analytics
description: Chẩn đoán sức khỏe kênh YouTube, đọc dữ liệu API (AVD, CTR), phân tích Retention Curve và đề xuất chiến lược tối ưu hóa doanh thu/view.
---

# SKILL: Channel Management & Analytics

## Khi nào sử dụng (Trigger Conditions)
- Khi User yêu cầu: "Đánh giá kênh", "Kiểm tra hiện trạng", "Xem video này thế nào", "Bắt bệnh video flop".
- Khi User cân nhắc lịch đăng bài: "Có nên đăng video ngày mai không?", "Khoảng cách đăng video thế nào là tối ưu?".
- Khi xây dựng chiến lược phát triển kênh dài hạn hoặc Audit lại một Postmortem.

## Yêu cầu đầu vào (Inputs)
- Dữ liệu API (Sử dụng `run_command` để chạy các script Python lấy số liệu trực tiếp từ YouTube: `fetch_avd.py`, `fetch_video_stats.py`, v.v.)
- Thông tin về file Kịch bản (`chapter_XX.md`) của video đang được phân tích.
- Baseline Performance (Dữ liệu nền tảng trong `00_core/performance_benchmarks.md`).

## Hướng dẫn cốt lõi (Core Instructions)

### 1. Nguyên tắc chẩn đoán (No Assumptions, Only Data)
- **TUYỆT ĐỐI KHÔNG** dùng cảm tính để khen ngợi video. Luôn đối chiếu với số liệu.
- Mọi đánh giá phải bắt đầu bằng việc kéo dữ liệu thực tế: Views, Likes, Comments, AVD (Average View Duration), Duration, Retention Rate.

### 2. Các bước khám bệnh (The Autopsy Process)
- **Bước 1 (So sánh với Baseline):** Kéo dữ liệu AVD của video và so sánh với mốc KPI > 40% của kênh. Nếu AVD < 30%, video được xếp vào dạng có lỗi cấu trúc.
- **Bước 2 (Giải mã Rớt khán giả - Drop-off):**
  - Nếu Views cực thấp, hãy chẩn đoán *Trần hiển thị (Impressions Ceiling)*: Chủ đề có tính đại chúng không? Title/Thumbnail có quá hàn lâm không?
  - Nếu Views cao nhưng AVD thấp: Tìm hiểu xem kịch bản có bị lỗi "Nhồi nhét lý thuyết" (Data Dumping) hay thiếu Cảm xúc cá nhân (Personal Stakes) ở giữa video không.
- **Bước 3 (Khuyến nghị hành động):** Chỉ đưa ra các Action Plan rõ ràng, cụ thể (ví dụ: cắt video làm Shorts, đổi Title, đổi Hook cho video sau, giữ nhịp đăng bài 5 ngày/video).

### 3. Phân biệt Bản chất Dữ liệu (RPM vs. Views)
- **RPM (Doanh thu/1000 lượt xem):** Luôn nhắc nhở User rằng RPM không phụ thuộc vào tần suất đăng bài, mà phụ thuộc vào ngách (Tài chính vĩ mô) và Độ dài video (Để chèn quảng cáo Mid-roll).
- **Trần hiển thị (Impressions Ceiling):** Giải thích rõ cho User hiểu rằng một video có AVD cao nhưng dung lượng thị trường nhỏ (Niche Topic) thì vẫn sẽ ngừng tăng View ở mức thấp (vd: 15k views). Điều này KHÔNG PHẢI là Flop, mà là đã chạm trần.

## Tích hợp Công cụ (Tool Integrations)
Khi thực thi Skill này, Agent ĐƯỢC PHÉP và ĐƯỢC YÊU CẦU chạy các script Python sau (thông qua `run_command`):
- `python .agents/scripts/youtube_ymyl_scanner.py --handle GocNhin_Podcast`: Quét toàn bộ video trên kênh và xuất Báo cáo Kiểm toán Rủi ro YMYL (`episodes/youtube_ymyl_audit_report.md`).
- `python .agents/scripts/youtube_auto_updater.py`: Đăng nhập Google OAuth2 với vai trò Quản trị kênh và tự động ghi đè/cập nhật Mô tả an toàn YMYL cho toàn bộ video bị gắn cờ.
- `python fetch_avd.py`: Lấy AVD 28 ngày qua của toàn kênh.
- `python fetch_video_stats.py`: Lấy dữ liệu chi tiết của video mới nhất.
*(Lưu ý: Luôn chạy trong môi trường ảo `source venv/bin/activate` nếu cần)*

## Đầu ra mong đợi (Expected Output)
- Một bản chẩn đoán chuyên sâu mang phong thái lạnh lùng, dữ liệu làm gốc.
- Báo cáo kiểm toán rủi ro YMYL chi tiết cho từng video trên kênh kèm theo đoạn văn bản Mô tả sửa lỗi mẫu.
- Không có lời an ủi sáo rỗng. Mọi phân tích phải dẫn tới một bài học hoặc một chiến lược rõ ràng cho tập video tiếp theo.

