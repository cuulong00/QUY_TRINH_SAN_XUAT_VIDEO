---
description: >-
  Chapter writing phase workflow. Relies on the specialist craft method in
  .agents/skills/chapter_writer/SKILL.md and rules in .agents/rules/content-os-pipeline.md.
---

Chapter writing workflow only.

Canonical sources for this phase:
- `.agents/skills/chapter_writer/SKILL.md` — specialist judgment, persona, and writing craft
- `.agents/rules/content-os-pipeline.md` — consolidated rules and pipeline controls
- `00_core/voiceover_style_guide.md` & `00_core/voice_dna.md` — tone, style, and vocabulary DNA

Reminder:
- Write exactly one chapter at a time.
- Read the minimum working set first: `03_brief.md`, `07_outline.md`, `08_chapter_briefs.md`, `09_narrative_state_tracker.md`, `10_compliance_report.md` (nếu có).
- Read the immediately previous `chapter_*.md` when a bridge or local continuity depends on exact wording.
- Run Chặng 1 (khung xương cơ chế) and Chặng 2 (bảng nhịp chương, rồi văn) as two separate passes, each printed to chat (`chapter_writer/SKILL.md` Bước 1).
- Before submitting, self-inspect the chapter with **Phiếu B** of `00_core/narrative_craft_rubric.md` (`chapter_writer/SKILL.md` Bước 3b) to spot weak lines and revise: ghi chỉ tiêu yếu, trích câu, vì sao, câu sửa; không cho điểm, không ghi ĐẠT; tự soi không phải điều kiện lưu và không tính vào điểm K; điều kiện qua cổng là chấm mù ở Pha 10 (`compliance_council` Khóa 6); chép bảng tự soi vào mục 1 của `episodes/[slug]/11_narrative_craft_scorecard.md`.
- Run the Post-write compliance check by invoking the **Quality & Compliance Council** (`compliance_council/SKILL.md`) to review, debate, and polish the drafted chapter.
- Update `09_narrative_state_tracker.md`, `10_compliance_report.md` (which replaces `financial_qa` and `oral_qa` reports), and `01_management/episode_registry.csv`.
- Do not bypass the chapter workflow by drafting final merge prose in chat.
