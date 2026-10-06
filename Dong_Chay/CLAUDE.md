# Dòng Chảy CLI & Agent Operating System

## Nguồn DNA duy nhất: `.agents/`
Toàn bộ DNA của kênh (persona, skill, workflow, rule, ví dụ) nằm DUY NHẤT trong `.agents/`, dùng chung cho Claude Code và Antigravity. `.claude/` chỉ chứa cấu hình Claude Code (`settings.json`: quyền và hook), không chứa DNA. Không tạo skill, agent, rule hay command trong `.claude/`.
- Làm một pha: mở `.agents/workflows/<pha>.md` và `.agents/skills/<skill>/SKILL.md` tương ứng, cùng persona trong `.agents/personas/`.
- Lập trường và nhận định: `00_core/stance_and_judgment.md`.

## Rule nạp mỗi phiên
@.agents/rules/orchestration-protocol.md
@.agents/rules/episodes-general.md
@.agents/rules/operator-visibility.md
@.agents/rules/editorial-quality.md
@.agents/rules/chapter-writing.md
@.agents/rules/claim-ledger.md
@.agents/rules/final-merge.md
@.agents/rules/visual-asset-safety.md
@.agents/rules/slideshow-render.md

## Cấu trúc làm việc bắt buộc (16 Pha Tư Duy Hệ Thống & Biện Chứng Đa Chiều)
1. Master Systemic Topography & Global Vision (`01_global_vision_synthesis.md` — Bàn cờ 4 Tầng + Ma trận 4 Lăng kính + Prompt 5 Phản biện)
2. Topographical Deep Research (`02_research_map.md` & `02_research_synthesis.md` — Contested Data & Trade-offs Ledger)
3. Strategy Brief (`03_brief.md`)
4. Master Outline Engine (`07_outline.md` — Biện chứng Hegel: Thesis ➔ Antithesis [The Devil's Chapter] ➔ Synthesis)
5. Hook Lab (`04_hook_pack.md` - Hook Sau)
6. Chapter Briefs (20 Trường: dữ liệu + nhịp chuyện + Steelman & Trade-offs) & NST (`08_chapter_briefs.md` & `09_narrative_state_tracker.md`)
7. Chapter Writing (`chapter_XX.md` — Anti-Token Syntax Ban, Steelman 3 nhịp)
8. Merge Voiceover (`voiceover.md`)
9. Retention Bridge Audit (`retention_bridge_audit.md`)
10 & 11. Editorial, Compliance & Dialectical Audit (`10_compliance_report.md` — Term-Breath + Dialectical Rigor & Bias Audit 25%)
12. Visual Storyboard & I2V Prompts / I2V+ Multimodal (Pha 12A/B/C hoặc 12+A/B/C — Chỉ khi có yêu cầu)
13. Audio Landscape (Chỉ khi có yêu cầu)
14. Batch Video Production (Chỉ khi có yêu cầu)
15. Production Handoff (`production_notes.md`)
16. Postmortem (`postmortem.md`)

## File bắt buộc của mỗi episode
- `01_global_vision_synthesis.md` (Pha 1 — Bản đồ Bàn cờ 4 Tầng + Ma trận 4 Lăng kính + Prompt 5 Phản biện)
- `02_research_map.md` & `02_research_synthesis.md` (Pha 2 — Contested Data & Trade-offs)
- `03_brief.md` (Pha 3 — Strategy Brief)
- `07_outline.md` (Pha 4 — Master Outline Biện Chứng Hegel & The Devil's Chapter)
- `04_hook_pack.md` (Pha 5 — Hook Lab)
- `08_chapter_briefs.md` (Pha 6 — Chapter Briefs 20 Trường + Steelman)
- `09_narrative_state_tracker.md` (Pha 6b — Sổ cái tự sự)
- `chapter_XX.md` (Pha 7 — Kịch bản thoại sạch, Steelman 3 nhịp)
- `voiceover.md` (Pha 8 — Gộp toàn bài)
- `retention_bridge_audit.md` (Pha 9 — Soi giữ chân)
- `10_compliance_report.md` (Pha 10 & 11 — Compliance, Oral & Dialectical Bias Audit)
- `11_narrative_craft_scorecard.md` (Pha 4, 7, 10 — Phiếu chấm nghệ thuật kịch bản theo `00_core/narrative_craft_rubric.md`; bắt buộc với tập mới từ 06/10/2026, tập đã đăng không bổ sung)
- `visual_storyboard_blueprint.md` / `visual_storyboard_blueprint_plus.md` (Pha 12 — Khi yêu cầu)
- `production_notes.md` (Pha 15 — Bàn giao)
- `postmortem.md` (Pha 16 — Rút kinh nghiệm)

## File hỗ trợ tùy chọn
- `07_golden_lines.md`
- `08_thumbnail_brief.md`
- thư mục tư liệu, video clips final (`footages/`, `videos/`)

## Cách làm việc đúng
- Mỗi lần chỉ làm đúng một pha.
- Phải đảm bảo phân loại tài liệu với taxonomy: `verified_data`, `market_analysis`, và `opinion_commentary` (do `the_compliance_editor` giám sát tại Pha 10 & 11).
- Dòng lưu ý nội dung bắt buộc: `Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng`.
- Ranh giới nội dung tài chính (cấm khuyến nghị mua/bán, dự đoán giá...): xem `00_core/financial_boundaries.md`.

## Nguồn Sự Thật Duy Nhất (Single Source of Truth)
- Định vị kênh: **Dự án video tài liệu phân tích dòng chảy lịch sử, địa chính trị, kinh tế chính trị và sự hưng vong của các thể chế**. Xem `00_core/channel_bible.md`.
- Toàn bộ hằng số vận hành (tốc độ đọc 223–235 từ/phút, ngưỡng QA ≥8.5/không trụ cột nào <7.5, độ dài mặc định Cấp 1-2, vị trí CTA cuối Chương 2) được hiến định tại `.agents/AGENTS.md` mục "Chuẩn Vận Hành Kỹ Thuật" — dùng chung cho cả Claude Code và Antigravity. Không định nghĩa lại số khác ở bất kỳ đâu.
- Bộ chuyên gia lõi mới: `the_capital_markets_analyst` (thị trường vốn/dòng tiền doanh nghiệp, kích hoạt khi chủ thể thuộc Hình thái 5 — Doanh nghiệp/Thị trường vốn) và `the_compliance_editor` (ranh giới tư vấn đầu tư/phỉ báng/an toàn thương hiệu, Pha 10 & 11).

## Công cụ Kiểm Chứng (Fact-checking)
- **Chạy tự động đối chiếu Google Search AI Mode (udm=50):**
  ```bash
  python3 scripts/google_ai_audit.py episodes/[slug] --all
  # Hoặc cho 1 chương cụ thể
  python3 scripts/google_ai_audit.py episodes/[slug] --chapter [số_chương]
  ```
  Công cụ sẽ xuất kết quả phản biện ra `google_ai_audit_results.md` và các file chương tương ứng. Sử dụng kết quả này tại **Pha 10 (Editorial QA)** để nới lỏng hoặc thắt chặt các nhận định kinh tế, xã hội trước khi voiceover.
  - **Quy tắc thao tác trên Google AI Mode:** BẮT BUỘC sử dụng tính năng **"Thêm tệp" (Import file .md từng chương)** qua nút `+` thay vì copy-paste trực tiếp văn bản dài vào ô chat. Việc import file giúp Gemini tiếp nhận trọn vẹn ngữ cảnh tài liệu, không bị cắt bớt nội dung và trả về báo cáo phân tích chuyên sâu đầy đủ nhất.
