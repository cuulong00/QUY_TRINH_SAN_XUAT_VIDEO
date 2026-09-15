---
description: >-
  Build the Strategy Brief (Phase 3). Requires completed 01_topic_qualification.md
  and 02_research_map.md. MUST be run after /deep_research.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt các file sau:

1. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_macro_strategist.md`
2. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_narrative_director.md`
3. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/01_topic_qualification.md`, `episodes/[slug]/02_research_map.md`.

3. **PHA 3 — BẢN CHIẾN LƯỢC (STRATEGY BRIEF):**
   
   Nhập tâm Script Architect (= kết hợp Macro Strategist + Narrative Director).
   
   Tạo `episodes/[slug]/03_brief.md`. File này **BẮT BUỘC** sử dụng dữ liệu cứng đã được thu thập từ `02_research_map.md` (Pha 2) để điền vào phần Neo Số Liệu. Không tự bịa số liệu.

   File `03_brief.md` **BẮT BUỘC** chứa đủ các mục sau (checklist cứng):

   ```
   ✅ Checklist output bắt buộc của Pha 3:
   [ ] Luận đề trung tâm (một câu dao cạo, không phải mô tả chung)
   [ ] Phản đề và cách bẻ gãy phản đề đó
   [ ] Chân dung khán giả — nhân vật đại diện cụ thể (tên, tuổi, hoàn cảnh tài chính)
   [ ] Nỗi đau đa tầng — ít nhất 3 nỗi đau cụ thể
   [ ] Điểm độ sâu chủ đề (Topic Depth Score) — 5 tiêu chí, đã tính tổng
   [ ] Cam kết với khán giả — 3 điều họ sẽ có sau khi xem
   [ ] Hành trình tư duy (Logic Arc) — từng chương có tên và vai trò rõ
   [ ] Neo số liệu — bảng số liệu đã kiểm chứng kèm nguồn (Lấy từ research_vault)
   [ ] Vùng cấm — ít nhất 5 điều KHÔNG làm
   [ ] Dấu vân tay giọng văn — giọng điệu chủ đạo của toàn tập
   ```

   Điều chỉnh ngôn ngữ: Mọi thuật ngữ tiếng Anh phải Việt hóa theo quy tắc trong `00_core/voice_dna.md` (Mục 8).

4. Xác nhận brief đã có đủ: chân dung khán giả, nỗi đau tài chính, cam kết, giọng điệu, neo số liệu thật và vùng cấm (không khuyên mua/bán).

5. Thông báo cho user duyệt Pha 3 trước khi tiếp tục `/hook_lab`.
