# Episode Template

Mỗi video là một thư mục riêng dưới `episodes/`.

## Cách tạo nhanh
```bash
bash scripts/new_episode.sh ten-episode
```

## Trình tự dùng file
1. `00_topic_qualification.md`
2. `01_brief.md`
3. `02_research_map.md`
4. `02_hook_pack.md`
5. `03_thesis_map.md`
6. `04_retention_map.md`
7. `04_outline.md`
8. `chapter_briefs.md` (nếu dùng)
9. Viết từng `chapter_XX.md`
10. Sau mỗi chapter, cập nhật `05_continuity_packet.md` và `06_claim_ledger.md`
11. Tạo `final_voiceover.md`
12. Chạy `financial_qa.md`
13. Chạy `oral_qa.md`
14. Tạo `visual_map.csv`
15. Khi đã có thư mục ảnh final, render `video/slideshow_base.mp4`
16. Hoàn tất `production_notes.md`
17. Sau publish hoặc review nội bộ, ghi `postmortem.md`

## Required artifacts
- `00_topic_qualification.md`
- `01_brief.md`
- `02_research_map.md`
- `02_hook_pack.md`
- `03_thesis_map.md`
- `04_retention_map.md`
- `04_outline.md`
- `05_continuity_packet.md`
- `06_claim_ledger.md`
- `chapter_XX.md`
- `final_voiceover.md`
- `financial_qa.md`
- `oral_qa.md`
- `visual_map.csv`
- `production_notes.md`
- `postmortem.md`

## Optional-supported artifacts
- `07_golden_lines.md`
- `chapter_briefs.md`
- `images_final/`
- `video/slideshow_base.mp4`

## Nguyên tắc
- Không viết full script one-shot từ topic thô.
- Mỗi pha chỉ cập nhật đúng file state của pha đó.
- `06_claim_ledger.md` phải dùng taxonomy: `verified_data`, `market_analysis`, `opinion_commentary`.
- Mọi video đều phải có disclaimer: "Đây là nội dung giáo dục, không phải lời khuyên đầu tư".
- Chỉ chạy slideshow render sau khi thư mục ảnh final đã được chốt thứ tự file.
