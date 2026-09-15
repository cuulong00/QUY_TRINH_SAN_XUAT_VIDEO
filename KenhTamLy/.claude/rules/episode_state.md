---
description: "Quy tắc state management cho mọi episode dưới episodes/."
---

# Quy tắc State Management cho Episode

## File state bắt buộc của mỗi episode
- `01_brief.md`
- `02_hook_pack.md`
- `03_thesis_map.md`
- `04_outline.md`
- `05_continuity_packet.md`
- `06_claim_ledger.md`
- `07_golden_lines.md`
- `chapter_XX.md`
- `final_voiceover.md`
- `08_thumbnail_brief.md`
- `09_youtube_metadata.md`
- `visual_map.csv`
- `scene_map.json`
- `visual_prompts.md`
- `production_notes.md`

## Production artifacts downstream
- `images_final/`
- `video/slideshow_base.mp4`

## Read-before-write
Trước khi viết hoặc sửa bất kỳ file nào trong `episodes/[slug]/`:
1. Đọc tất cả state files hiện có
2. Nếu đang viết / sửa chapter, đọc tất cả `chapter_*.md` liên quan
3. Xác định pha hiện tại
4. Không viết vượt pha

## Write-then-update
Sau khi viết hoặc revise chapter, bắt buộc cập nhật:
- `05_continuity_packet.md`
- `06_claim_ledger.md`
- `07_golden_lines.md`

## Source of truth by file
- `01_brief.md` = audience, pain, promise, runtime contract
- `02_hook_pack.md` = packaging promise, opening architecture
- `03_thesis_map.md` = thesis, anti-thesis, open loops, payoff requirements
- `04_outline.md` = chapter roles, retention map, chapter budgets
- `chapter_XX.md` = triển khai theo outline
- `final_voiceover.md` = bản merge preservation-first
- `visual_map.csv` = worksheet planning cho visual strategy upstream
- `scene_map.json` = source of truth downstream cho grouping cảnh, `duration_sec`, `visual_summary`, prompt generation, và slideshow render
- `visual_prompts.md` = scene-based image prompt export
- `production_notes.md` = production handoff, image/render notes, và trạng thái vận hành downstream

## Contracts không được phá ở pha sau
- runtime contract từ brief
- packaging promise từ hook pack
- payoff requirements từ thesis map
- chapter roles và target_words từ outline
- visual scene grouping contract từ `scene_map.json`

## Visual grouping contract
- Hook zone: 1 câu = 1 ảnh.
- Các phần khác: tối đa 3 câu = 1 ảnh.
- Không được gộp nếu việc gộp làm mất reveal, contradiction, emotional turn, interpretive pivot, hoặc behavioral reframe.
- `visual_summary` phải giữ trọn linh hồn của tất cả câu đã gộp, không được rơi ý.

## Registry update
Sau mỗi milestone lớn, cập nhật `01_management/episode_registry.csv`.
Nếu học được pattern mới, append vào `01_management/lessons_learned.md`.
