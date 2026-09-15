---
description: >-
  Build the Hook Lab (Phase 5). Requires completed 03_brief.md AND 07_outline.md.
  MUST be run AFTER /build_outline and BEFORE /write_chapter (Outline-First, Hook-Last Protocol).
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/hook_engine/SKILL.md`
2. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_macro_strategist.md`

NGHIÊM CẤM tạo bất kỳ hook hay output nào nếu chưa hoàn thành việc đọc cả hai file trên.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/07_outline.md`, `episodes/[slug]/vault/00_Global_Vision_Synthesis.md`.

3. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo `04_hook_pack.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO 04_hook_pack.md]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Viral Alchemist + The Critical Auditor
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/hook_lab` (`hook_engine/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * `episodes/[slug]/03_brief.md` (Chiến lược & Lời hứa cốt lõi)
   >   * `episodes/[slug]/07_outline.md` (Dàn ý Động ABT & The Grand Payoff)
   >   * `episodes/[slug]/vault/00_Global_Vision_Synthesis.md` (Bức tranh dữ liệu toàn cảnh)
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
   - Source Documents Consulted: 03_brief.md, 07_outline.md, vault/00_Global_Vision_Synthesis.md
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```
   - Tạo 7 góc tiếp cận → 10 câu mở → chọn top 3 → chốt 1 câu mở chính + 5 câu móc giữa
   - Chấm điểm từng câu mở: tò mò / gắn nỗi đau / tín hiệu chiều sâu / giữ chân / đúng kênh

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
   ```

5. Thông báo cho user duyệt Pha 5 (`04_hook_pack.md`) trước khi tiếp tục **Pha 6: Chapter Briefs (16 Trường - `08_chapter_briefs.md`) & Khởi tạo NST**.