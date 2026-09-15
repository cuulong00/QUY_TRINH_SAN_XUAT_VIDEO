---
description: >-
  DEPRECATED — Bước Final Merge đã bị loại khỏi pipeline.
  Oral polish thực hiện trực tiếp trên từng chapter_XX.md.
  Khi thu âm, đọc tuần tự từ chapter_01 → chapter cuối.
  Không cần file final_voiceover.md.
---

## ⚠️ DEPRECATED

Bước này đã bị loại bỏ khỏi pipeline sản xuất kể từ 2026-04-09.

**Lý do:** Merge là bước cơ học thuần túy (concatenation) không mang lại giá trị. Oral polish thực hiện trực tiếp trên từng `chapter_XX.md`. Thu âm đọc tuần tự từ chapter_01 → chapter cuối.

**Thay thế bằng:**
- Oral Polish: `.agents/skills/oral_polisher/SKILL.md` — chạy trực tiếp trên từng chapter
- QA: `.agents/skills/financial_qa/SKILL.md` — chạy trên tập hợp chapters
