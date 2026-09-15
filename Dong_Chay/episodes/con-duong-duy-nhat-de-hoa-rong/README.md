# Episode Template

Mỗi video là một thư mục riêng dưới `episodes/`.

## Cách tạo nhanh
```bash
bash scripts/new_episode.sh ten-episode
```

## Trình tự dùng file
1. `01_topic_qualification.md`
2. `02_research_map.md`
3. `03_brief.md`
4. `04_hook_pack.md`
5. `05_thesis_map.md`
6. `06_retention_map.md`
7. `07_outline.md`
8. `08_chapter_briefs.md`
9. Viết từng `chapter_XX.md`
10. Sau mỗi chapter, cập nhật `09_narrative_state_tracker.md` và `10_claim_ledger.md`
11. Chạy `financial_qa.md`
12. Chạy `oral_qa.md`
13. Tạo `visual_map.csv`
14. Khi đã có thư mục ảnh final, render `video/slideshow_base.mp4`
15. Hoàn tất `production_notes.md`
16. Sau publish hoặc review nội bộ, ghi `postmortem.md`

## Required artifacts
- `01_topic_qualification.md`
- `02_research_map.md`
- `03_brief.md`
- `04_hook_pack.md`
- `05_thesis_map.md`
- `06_retention_map.md`
- `07_outline.md`
- `08_chapter_briefs.md`
- `09_narrative_state_tracker.md`
- `10_claim_ledger.md`
- `chapter_XX.md`
- `financial_qa.md`
- `oral_qa.md`
- `visual_map.csv`
- `production_notes.md`
- `postmortem.md`

## Optional-supported artifacts
- `07_golden_lines.md`
- `images_final/`
- `video/slideshow_base.mp4`

## Nguyên tắc
- Không viết full script one-shot từ topic thô.
- Mỗi pha chỉ cập nhật đúng file state của pha đó.
- `10_claim_ledger.md` phải dùng taxonomy: `verified_data`, `market_analysis`, `opinion_commentary`.
- Mọi video đều phải có disclaimer: "Đây là nội dung giáo dục, không phải lời khuyên đầu tư".
- Chỉ chạy slideshow render sau khi thư mục ảnh final đã được chốt thứ tự file.
