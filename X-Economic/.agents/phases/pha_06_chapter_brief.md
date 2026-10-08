# Thẻ Pha 6: Chapter Briefs, Sổ Cái Tự Sự & Thumbnail Brief

**Mục tiêu.** Chuyển hóa dàn ý thành hồ sơ giao việc chi tiết cho từng chương theo **chuẩn 20 trường bắt buộc** (16 trường dữ kiện/lập luận + 4 trường nhịp chuyện kể: `cau_hoi_dieu_tra`, `vat_chung`, `cu_lat`, `chu_the_va_dong_co`). Mỗi chương có chức năng, tọa độ chứng cứ gốc kèm câu trích dẫn nguyên văn, phản biện Steelman và mỏ neo nhân quả. Khởi tạo Sổ cái trạng thái tự sự (`episodes/<slug>/09_narrative_state_tracker.md`) và Thumbnail brief.

## Đọc, theo thứ tự
1. `episodes/<slug>/07_outline.md`, `episodes/<slug>/04_hook_pack.md` (hook đã được user chọn).
2. `episodes/<slug>/02_research_map.md` (Kho vật chứng VC-xx) và `episodes/<slug>/research_vault/`.
3. `.agents/skills/script_architect/SKILL.md` (mục Pha 6).
4. Khuôn: `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md`, `02_templates/episode_template/08_chapter_briefs.md` (khuôn YAML 20 trường), `02_templates/episode_template/09_narrative_state_tracker.md`, `02_templates/episode_template/08_thumbnail_brief.md`.
5. Persona: `.agents/personas/the_narrative_director.md`, `.agents/personas/the_critical_auditor.md`.
6. Thumbnail brief: `.agents/skills/thumbnail_prompter/SKILL.md`, `.agents/personas/the_visual_hook_director.md`.

## Không cần đọc
`episodes/<slug>/01_global_vision_synthesis.md` đầy đủ, toàn bộ vault thô (chỉ mở đúng file/đoạn trích dẫn vào brief).

## Chuyên gia (Persona)
- `.agents/personas/the_narrative_director.md`: Đạo diễn Tự sự & Nhịp chuyện.
- `.agents/personas/the_critical_auditor.md`: Kiểm toán viên Dữ liệu & Phản biện.
- `.agents/personas/the_visual_hook_director.md`: Đạo diễn Thị giác Thumbnail.

## Luật riêng (trỏ bản gốc)
- Điền đủ cấu trúc 20 trường cho từng chương (CH01 đến CHXX) theo `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md`:
  * 4 trường nhịp chuyện: 4a `cau_hoi_dieu_tra`, 4b `vat_chung` (từ kho VC-xx), 4c `cu_lat`, 4d `chu_the_va_dong_co`.
  * Bảng Pointer chứng cứ gốc (Trường 10): Tối thiểu 5 dòng chỉ rõ `Mã Footnote ID + Tên file vault + Trích dẫn nguyên văn (copy, không viết lại) + Dữ kiện & nhịp phục vụ + Đọc / lên hình`.
  * Khóa phản biện Steelman (`steelman_counter_thesis`) và thừa nhận đánh đổi (`admitted_trade_offs`).
- Không nâng độ chắc chắn của dữ kiện (không tự dán nhãn "bất biến" cho con số).
- Đồng bộ Thumbnail Brief với lời hứa của Hook đã chọn.

## Câu tự hỏi
- Người viết chương có thể mở đúng file và đúng dòng trong vault từ bảng pointer không?
- 4 trường nhịp chuyện có giúp chương kể thành một cuộc điều tra hấp dẫn thay vì đọc báo cáo không?
- Danh sách lặp (`forbidden_echoes`) đã chặn những sự kiện và con số đã dùng ở các chương trước chưa?

## Giới hạn
Brief mỗi chương tối đa 400 từ.

## Đầu ra
`episodes/<slug>/08_chapter_briefs.md`, `episodes/<slug>/09_narrative_state_tracker.md`, `episodes/<slug>/08_thumbnail_brief.md`.

## Cổng và dừng
Kiểm tra đủ 20 trường, câu trích dẫn nguyên văn có thật trong vault. User duyệt Chapter Briefs trước khi sang Pha 7.
