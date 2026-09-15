# Walkthrough — Dùng VinFast có thật sự rẻ? (Phase 1 to 11)

Tôi đã hoàn thành toàn bộ kịch bản và báo cáo QA của **Pha 1 đến Pha 11** trong quy trình kịch bản của Content OS.

## Những thay đổi đã thực hiện

### 1. Pha 1 & 2: Topic Qualification & Research Map (Đã duyệt)
- Khởi tạo thư mục và liên kết Master Notebook: `https://notebooklm.google.com/notebook/703f6053-3d8c-4528-ae98-d2d63197e32a`.
- Viết file xác thực chủ đề hoàn chỉnh: [01_topic_qualification.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/01_topic_qualification.md).
- Sao chép `research_vault` thô và biên soạn [02_research_map.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/02_research_map.md) với đầy đủ 8 data points, 5 cơ chế vĩ mô, 2 điểm mù, và các bài học lịch sử Proton/Hyundai.

### 2. Pha 3 & 4: Strategy Brief & Hook Lab (Đã duyệt)
- Biên soạn bản chiến lược phân tích: [03_brief.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/03_brief.md).
- Thiết lập [04_hook_pack.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/04_hook_pack.md) với 3 hook candidates, Data Anchor Matrix và kịch bản Hook + Intro + CTA hoàn chỉnh.

### 3. Pha 5 đến 8: Dàn ý & Tóm tắt chương (Đã duyệt)
- Thiết lập bản đồ luận đề [05_thesis_map.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/05_thesis_map.md) và bản đồ giữ chân [06_retention_map.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/06_retention_map.md).
- Viết dàn ý chi tiết 6 chương [07_outline.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/07_outline.md) và hồ sơ chương chi tiết [08_chapter_briefs.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/08_chapter_briefs.md).

### 4. Pha 9: Viết Chương (Chapter Writing)
- Biên soạn 6 chương kịch bản độc lập: [chapter_01.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_01.md), [chapter_02.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_02.md), [chapter_03.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_03.md), [chapter_04.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_04.md), [chapter_05.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_05.md), và [chapter_06.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/chapter_06.md).
- Thiết lập Hộ chiếu dữ liệu (Data Passport) độc lập cho từng chương để đảm bảo tính an toàn dữ liệu: `data_passport_ch01.md` đến `data_passport_ch06.md`.
- Duy trì tính liên tục toàn cục qua [05_continuity_packet.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/05_continuity_packet.md).
- Khống chế chặt chẽ giới hạn câu dưới 150 ký tự, cấu trúc ngữ pháp đầy đủ và loại bỏ AI-isms.

### 5. Pha 10 & 11: Kiểm tra Biên tập, Pháp lý và Giọng nói (QA Review)
- Xây dựng báo cáo kiểm tra biên tập và pháp lý [editorial_qa.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/editorial_qa.md) (Pha 10) phân loại 19 claims thành `verified_data` và `market_analysis`.
- Xây dựng báo cáo kiểm soát nhịp điệu và ngắt hơi [oral_qa.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/oral_qa.md) (Pha 11) đảm bảo 100% sẵn sàng cho việc thu âm hoặc TTS local trên RunPod GPU.

## Kiểm tra chất lượng (Verification & Compliance)
- Chạy kiểm soát độ dài câu qua kịch bản tự động, 100% câu đạt chuẩn dưới 150 ký tự.
- Khử sạch các dấu gạch ngang dài `—` khỏi phần văn bản.
- Loại bỏ hoàn toàn tiêu đề chương và ghi chú kỹ thuật khỏi các file kịch bản để tránh nhiễu khi đưa vào bộ đọc giọng nói.

## Pha 12: Thu âm & Kiểm tra giọng đọc (Audio Production)
- Đã hoàn thành chạy script `run_production_with_audit.py` trên MacBook kết nối với RunPod GPU.
- Sử dụng giọng thuyết minh Nam chuẩn tự nhiên: `mc_nam_natural_4.8s` (khớp chính xác văn bản).
- Tất cả 6 chương kịch bản (`chapter_01.md` đến `chapter_06.md`) đã được tổng hợp giọng nói và kiểm duyệt tự động thông qua mô hình PhoWhisper-small.
- **Cập nhật (15/06/2026)**: Đã thực hiện thu âm lại riêng **Chương 2** (`chapter_02.md`) để sửa phát âm của ngày tháng (`10/02/2026` -> đọc chuẩn tiếng Việt: *"ngày mười tháng hai năm hai nghìn không trăm hai mươi sáu"*) và đảm bảo giữ nguyên từ tiếng Anh *"Plus"* chuẩn không phiên âm.
- Toàn bộ file âm thanh đầu ra dạng WAV đã được tải về MacBook tại thư mục [audio_v2/](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/):
  - [chapter_01_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_01_v2.wav)
  - [chapter_02_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_02_v2.wav) (Đã sửa lại)
  - [chapter_03_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_03_v2.wav)
  - [chapter_04_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_04_v2.wav)
  - [chapter_05_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_05_v2.wav)
  - [chapter_06_v2.wav](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/audio_v2/chapter_06_v2.wav)
- Tất cả GPU pod trên RunPod (`981jn6vp9yraqo` và pod chạy lại `nj4f76ohzyu1st`) đã được tự động tắt (`EXITED`) ngay sau khi hoàn thành để tránh phát sinh chi phí.

