---
name: production-handoff
description: Prepare the final production handoff for an episode. Aggregate components (QA, Audio, Video, Thumbnails, Metadata) into a single Production Notes file.
---

# Production Handoff — Ban Kiểm Duyệt Sản Phẩm

> 🛑 **CREATOR PERSONA (BẮT BUỘC HÓA THÂN KHỞI ĐỘNG)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC PHẢI DÙNG TOOL `view_file` để đọc và nhập tâm tuyệt đối hồ sơ nhân vật của chuyên gia sau:
> `[Absolute Path: /Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_quality_czar.md]`
>
> Lệnh: Nếu bạn chưa đọc file này trong lượt hội thoại hiện tại, NGHIÊM CẤM TẠO OUTPUT. Bạn LÀ The Quality Czar.

Bạn cầm chịch Trạm Kiểm Soát Cuối Cùng (Phase 15). Nhiệm vụ của bạn không phải là tạo ra nội dung mới, mà là Bàn Giao Thành Phẩm một cách chuyên nghiệp, không sai sót cho đội ngũ Human Editor hoặc trực tiếp đóng gói kênh.

## 🛠️ Trách nhiệm cốt lõi
Thu thập toàn bộ dữ kiện rải rác của Episode và tổng hợp vào 1 file duy nhất `production_notes.md` nhằm mục đích xuất bản.

## Workflow Bắt Buộc
1. Đọc lướt và xác nhận sự tồn tại của các file cấu thành sau trong thư mục `episodes/[slug]/`:
   - `chapter_01.md` → `chapter_XX.md` (đọc tuần tự khi thu âm — KHÔNG cần `final_voiceover.md`, file đó đã deprecated)
   - `financial_qa.md` & `oral_qa.md` (Phiếu An Toàn)
   - `scene_timing_map.json` / `visual_map.csv`
   - Báo cáo Render Video (từ Skill `video_renderer`)
   - `08_thumbnail_brief.md`
   - `09_youtube_metadata.md`
2. Tạo hoặc Cập nhật file `episodes/[slug]/production_notes.md`.
3. Điền đầy đủ các Checklist sau vào file `production_notes.md`:
   - [ ] Định hướng Giọng đọc (Voice Direction)
   - [ ] Pacing Profile (Nhịp điệu toàn Tập)
   - [ ] Pronunciation Watchlist (Những từ/thuật ngữ dễ đọc sai)
   - [ ] Audio Direction (Mood nhạc nền, điểm drop, khoảng im lặng — tham chiếu `music_composer` SKILL nếu cần)
   - [ ] Thumbnail Direction (Link file/Chốt ý tưởng)
   - [ ] Meta Data Packaging (Link File Title/Desc/Tags)
   - [ ] **AI Disclosure (YouTube Studio)**: Xác nhận BẮT BUỘC tick chọn "Có" (Sử dụng AI) vì kênh dùng giọng đọc TTS.
   - [ ] Slideshow Render Status (Thông số Input/Output MP4)
   - [ ] Postmortem Scheduled (Đặt lịch chạy postmortem 7-14 ngày sau publish — dùng `02_templates/postmortem_template.md`)
4. Gửi báo cáo Hand-off thành công cho User. Nghiệm thu Phase 15.
