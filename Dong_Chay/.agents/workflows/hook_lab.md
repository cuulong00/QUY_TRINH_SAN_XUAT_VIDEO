---
description: >-
  Build the Hook Lab (Phase 5). Requires completed 03_brief.md AND 07_outline.md.
  MUST be run AFTER /build_outline and BEFORE /write_chapter (Outline-First, Hook-Last Protocol).
---

> 📐 Khung đầu ra `04_hook_pack.md`: `02_templates/masterpiece_pipeline/04_hook_pack_template.md`; ví dụ yếu/mạnh: `.agents/examples/hook_engine_examples.md`. Hook đặt câu hỏi và căng thẳng, KHÔNG kết luận trước lập trường của tập (`00_core/stance_and_judgment.md` §8).

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/skills/hook_engine/SKILL.md`
2. `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/personas/the_macro_strategist.md`

NGHIÊM CẤM tạo bất kỳ hook hay output nào nếu chưa hoàn thành việc đọc cả hai file trên.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/07_outline.md`, `episodes/[slug]/01_global_vision_synthesis.md` (hoặc `01_topic_qualification.md` ở tập theo Pha 1 cũ).

3. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo `04_hook_pack.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO 04_hook_pack.md]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Viral Alchemist + The Critical Auditor
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/hook_lab` (`hook_engine/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * `episodes/[slug]/03_brief.md` (Chiến lược & Lời hứa cốt lõi)
   >   * `episodes/[slug]/07_outline.md` (Dàn ý Động ABT & The Grand Payoff)
   >   * `episodes/[slug]/01_global_vision_synthesis.md` (Bức tranh dữ liệu toàn cảnh & Bàn cờ)
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/04_hook_pack.md`
   > - 🛡️ **Rào Cản Kiểm Toán:** Outline-to-Hook Alignment — Hook phải cam kết chính xác những gì Dàn ý sẽ giải quyết, gieo đúng Open Loops, triệt tiêu 100% clickbait hứa hão.
   ```

4. **PHA 5 — PHÒNG THÍ NGHIỆM CÂU MỞ (HOOK LAB - MAY ĐO THEO DÀN Ý)** (nhập tâm hook_engine SKILL đã đọc ở HARD GATE):

   Tạo `episodes/[slug]/04_hook_pack.md` theo đúng quy trình của hook_engine. BẮT BUỘC nhúng khối Provenance Metadata ở đầu tệp:
   ```markdown
   <!--
   DOCUMENT PROVENANCE & EXECUTION LINEAGE:
   - Output Document: episodes/[slug]/04_hook_pack.md
   - Activated Persona: The Viral Alchemist + The Critical Auditor
   - Activated Skill: hook_engine/SKILL.md (/hook_lab)
   - Source Documents Consulted: 03_brief.md, 07_outline.md, 01_global_vision_synthesis.md
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```
   - Viết 3 biến thể Master Hook theo 3 Engine của `hook_engine/SKILL.md` (Chặng 2), mỗi biến thể đủ cấu trúc 30 giây đầu (Chặng 2b: xác nhận cú bấm 0–3 giây, đối nghịch nhìn thấy được, điều được mất + câu hỏi trung tâm; cấm đọc mục lục / lộ trình chặng). Chốt 1 Master Hook, 1 câu re-hook ~3:30, và các câu móc chuyển chương theo đúng số chương của `07_outline.md`.
   - Chấm từng biến thể bằng bảng ở `04_hook_pack_template.md` mục 3 và ba phép thử (tắt tiếng, đặt cạnh thumbnail, tắt sau hook).

   **4 kiểm tra bắt buộc cho mỗi câu mở trước khi chọn:**

   ```
   ✅ Kiểm tra CHỐNG TỰ ĐÓNG LOOP:
   [ ] Nếu người xem tắt video NGAY SAU câu mở → họ có cảm thấy đã hiểu đủ chưa?
       Nếu CÓ → câu mở tự đóng loop → PHẢI viết lại

    ✅ Kiểm tra TÍNH LOGIC & TỰ NHIÊN:
    [ ] Lập luận đi thẳng vào bản chất vấn đề, không cố tình padding hay gò ép stakes cá nhân khi không liên quan.
 
    ✅ Kiểm tra CÂU MÓC GIỮA #1 (mốc ~3:30):
    [ ] Kết nối mở rộng bằng một nghịch lý lớn, bất ngờ hoặc một cú bẻ lái sắc sảo trong dữ liệu để kích hoạt sự chú ý.

   ✅ Kiểm tra TRÁNH AI-ISM:
   [ ] Câu mở không dùng các cụm bị cấm trong 00_core/anti_ai_isms.md

   ✅ Kiểm tra CẤU TRÚC 30 GIÂY ĐẦU (hook_engine Chặng 2b):
   [ ] Câu đầu xác nhận cú bấm (0–3s), cùng chủ thể với tiêu đề và thumbnail
   [ ] Đối nghịch nhìn thấy được bằng dữ kiện thực chứng, không nhãn phán xét
   [ ] Kết bằng câu hỏi trung tâm mở, không lộ đáp án; CẤM đọc mục lục hay lộ trình chặng
   [ ] Đã qua ba phép thử: tắt tiếng, đặt cạnh thumbnail, tắt sau hook
   ```

5. Thông báo cho user duyệt Pha 5 (`04_hook_pack.md`) trước khi tiếp tục **Pha 6: Chapter Briefs (20 Trường - `08_chapter_briefs.md`) & Khởi tạo NST**.