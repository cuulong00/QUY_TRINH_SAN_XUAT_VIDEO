# Thẻ Pha 6: Chapter briefs, sổ cái tự sự, thumbnail brief

**Mục tiêu.** Biến outline thành bản giao việc cho từng chương theo chuẩn 20 trường (16 dữ kiện/lập luận + 4 nhịp chuyện: câu hỏi điều tra, vật chứng, cú lật, chủ thể & động cơ). Mỗi chương có chức năng, dữ kiện kèm **vị trí nguồn gốc**, phản biện cần dựng, câu nối sang chương sau. Người viết Pha 7 chỉ cần brief của chương mình cùng các nguồn được trỏ tới.

## Đọc, theo thứ tự
1. `07_outline.md`, `04_hook_pack.md` (hook đã chọn), `00_so_du_kien.md`.
2. `.agents/skills/script_architect/SKILL.md` §2 "Pha 6".
3. Khuôn `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md`.
4. Persona: `the_narrative_director.md`, `the_critical_auditor.md`.
5. Thumbnail brief: `.agents/skills/thumbnail_prompter/SKILL.md`, `.agents/personas/the_visual_hook_director.md`.

## Không cần đọc
`01_global_vision_synthesis.md` đầy đủ, vault đầy đủ (chỉ mở đoạn nguồn của con số đang đưa vào brief).

## Cách làm
- Điền đủ cấu trúc 20 trường (16 trường dữ kiện/lập luận + 4 trường nhịp chuyện kể: câu hỏi điều tra, vật chứng, cú lật, chủ thể và động cơ).
- Mỗi con số trong brief: mã M, vị trí nguồn gốc (URL kèm đoạn, hoặc `research_vault/<file>`/`research_raw/<file>` kèm dòng), câu trích **chép từ nguồn**, không tự viết lại.
- Không nâng độ chắc chắn của dữ kiện (không "bất biến", không "bắt buộc giữ nguyên" cho một con số).
- Chỉ định một persona chính cho mỗi chương.

## Giới hạn
Brief mỗi chương tối đa 400 từ.

## Đầu ra
`08_chapter_briefs.md`, `09_narrative_state_tracker.md`, `08_thumbnail_brief.md`.

## Cổng và dừng
Chạy `python3 scripts/kiem_pha.py <slug> --pha 6`: câu gốc trong brief phải có trong `research_vault/` hoặc `research_raw/` (`TRICH-KHONG-THAY`). User duyệt.
