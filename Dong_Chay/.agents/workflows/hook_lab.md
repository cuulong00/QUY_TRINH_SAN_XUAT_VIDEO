---
description: >-
  Build the Hook Lab (Phase 4). Requires completed 03_brief.md. MUST be run after
  /build_brief and before /build_outline.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/skills/hook_engine/SKILL.md`
2. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_macro_strategist.md`

NGHIÊM CẤM tạo bất kỳ hook hay output nào nếu chưa hoàn thành việc đọc cả hai file trên.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`.

3. **PHA 4 — PHÒNG THÍ NGHIỆM CÂU MỞ** (nhập tâm hook_engine SKILL đã đọc ở HARD GATE):

   Tạo `episodes/[slug]/04_hook_pack.md` theo đúng quy trình của hook_engine:
   - Tạo 7 góc tiếp cận → 10 câu mở → chọn top 3 → chốt 1 câu mở chính + 5 câu móc giữa
   - Chấm điểm từng câu mở: tò mò / gắn nỗi đau / tín hiệu chiều sâu / giữ chân / đúng kênh

   **4 kiểm tra bắt buộc cho mỗi câu mở trước khi chọn:**

   ```
   ✅ Kiểm tra CHỐNG TỰ ĐÓNG LOOP:
   [ ] Nếu người xem tắt video NGAY SAU câu mở → họ có cảm thấy đã hiểu đủ chưa?
       Nếu CÓ → câu mở tự đóng loop → PHẢI viết lại

   ✅ Kiểm tra TÍNH LIÊN QUAN & TÒ MÒ:
   [ ] Câu mở có khơi gợi sự tò mò mạnh mẽ và thiết lập tính liên quan đến bối cảnh thực tế của người xem hoặc bối cảnh Việt Nam một cách tự nhiên không?

   ✅ Kiểm tra CÂU MÓC GIỮA #1 (mốc ~3:30):
   [ ] Hứa hẹn một mối liên kết thông tin mới hoặc một lớp phân tích logic sâu sắc tiếp theo để giữ chân người nghe, tránh hứa hẹn chung chung.

   ✅ Kiểm tra TRÁNH AI-ISM:
   [ ] Câu mở không dùng các cụm bị cấm trong 00_core/anti_ai_isms.md
   ```

4. Thông báo cho user duyệt Pha 4 trước khi tiếp tục `/build_outline`.