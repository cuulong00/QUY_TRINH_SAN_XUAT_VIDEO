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
- **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
  TRƯỚC KHI tạo `chapter_XX.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
  ```markdown
  > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG VIẾT chapter_XX.md]**
  > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** [Persona được chỉ định trong 08_chapter_briefs.md] + The Narrative Director (Khóa Khẩu Ngữ Oral Voice)
  > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/write_chapter` (`chapter_writer/SKILL.md`)
  > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Full Working Context):**
  >   * `vault/00_Global_Vision_Synthesis.md` (Tầm nhìn tổng thể & Mỏ neo số liệu)
  >   * `episodes/[slug]/08_chapter_briefs.md` (Brief chi tiết của Chương XX)
  >   * `episodes/[slug]/09_narrative_state_tracker.md` (Vòng lặp nhận thức, Hạt giống chuyển tiếp)
  >   * `episodes/[slug]/chapter_01.md` đến `chapter_XX-1.md` (Toàn bộ kịch bản thoại sạch các chương trước để giữ nhịp, chống lặp)
  > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/chapter_XX.md` (Văn bản thoại sạch 100%, câu < 150 ký tự, không nhúng log vận hành)
  > - 🛡️ **Rào Cản Kiểm Toán:** 5 Gates ngầm trong Thinking (Data ZUI, Continuity, Oral Voice, Math < 150 ký tự/câu, Paragraph Integrity $S/P \ge 1.8$ - CẤM ngắt dòng sau mỗi câu).
  ```
- **KỶ LUẬT PHÂN ĐOẠN VĂN XUÔI (PARAGRAPH INTEGRITY GATE):**
  * Kịch bản thoại PHẢI được viết thành các đoạn văn hoàn chỉnh (2-4 câu/đoạn).
  * TUYỆT ĐỐI CẤM xuống dòng `\n\n` sau mỗi câu đơn lẻ.
  * Tỷ lệ $S/P = \text{Số câu} / \text{Số đoạn} \ge 1.8$. Nếu $S/P < 1.5$ ➔ Từ chối nghiệm thu.
- Run the Post-write compliance check by invoking the **Quality & Compliance Council** (`compliance_council/SKILL.md`) to review, debate, and polish the drafted chapter.
- Update `09_narrative_state_tracker.md`, `10_compliance_report.md` (which replaces `financial_qa` and `oral_qa` reports), and `01_management/episode_registry.csv`.
- Do not bypass the chapter workflow by drafting final merge prose in chat.
