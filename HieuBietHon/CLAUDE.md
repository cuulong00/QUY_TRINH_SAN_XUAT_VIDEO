# HieuBietHon CLI & Agent Operating System

## Cấu trúc làm việc bắt buộc
1. Topic Qualification
2. Data Mining & Verification
3. Strategy Brief
4. Hook Lab
5. Thesis Map
6. Retention Map
7. Outline
8. Chapter Briefs
9. Chapter Writing
10. Editorial & Legal QA
11. Oral QA
12. Visual Map (Chỉ chạy khi có yêu cầu)
13. Audio Landscape (Chỉ chạy khi có yêu cầu)
14. Video Render (CapCut - Manual)
15. Production Handoff
16. Postmortem
17. Performance Review (Thủ công)

## File bắt buộc của mỗi episode
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
- `10_compliance_report.md` (replaces editorial_qa and oral_qa)
- `visual_map.csv`
- `production_notes.md`
- `postmortem.md`

## File hỗ trợ tùy chọn
- `07_golden_lines.md`
- `thư mục ảnh final, ví dụ `images_final/``
- `file output render, ví dụ `video/slideshow_base.mp4``

## Cách làm việc đúng
- Mỗi lần chỉ làm đúng một pha.
- Phải đảm bảo phân loại tài liệu với taxonomy: `verified_data`, `market_analysis`, và `opinion_commentary`.
- Dòng lưu ý nội dung bắt buộc: `Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng`.

## Công cụ Kiểm Chứng (Fact-checking)
- **Chạy tự động đối chiếu Google Search AI Mode (udm=50):**
  ```bash
  python3 scripts/google_ai_audit.py episodes/[slug] --all
  # Hoặc cho 1 chương cụ thể
  python3 scripts/google_ai_audit.py episodes/[slug] --chapter [số_chương]
  ```
  Công cụ sẽ xuất kết quả phản biện ra `google_ai_audit_results.md` và các file chương tương ứng. Sử dụng kết quả này tại **Pha 10 (Editorial QA)** để nới lỏng hoặc thắt chặt các nhận định kinh tế, xã hội trước khi voiceover.
