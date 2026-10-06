---
description: >-
  Build the Strategy Brief (Phase 3). Requires completed 01_topic_qualification.md
  and 02_research_map.md. MUST be run after /deep_research.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt các file sau:

1. `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/personas/the_macro_strategist.md`
2. `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/personas/the_narrative_director.md`
3. `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. **🛑 HARD GATE KIỂM TOÁN THỰC CHỨNG PHA 2 (PROOF-OF-EXECUTION GATE — BẮT BUỘC):**
   Trước khi đọc bất kỳ file nào, Agent BẮT BUỘC chạy script kiểm toán cứng:
   ```bash
   python3 scripts/verify_phase_gate.py --phase 2 --episode [slug]
   ```
   - Nếu script báo **FAIL (Exit Code 1)** $\to$ **DỪNG NGAY LẬP TỨC!** Tuyệt đối CẤM tạo `03_brief.md` hay tự chế brief khi chưa vượt qua kiểm toán Pha 2. Thông báo cho người dùng hoặc quay lại chạy `/deep_research`.
   - Nếu script báo **PASS (Exit Code 0)** $\to$ Được phép chuyển tiếp sang bước 3.

3. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/01_topic_qualification.md`, `episodes/[slug]/02_research_map.md`.

4. **PHA 3 — BẢN CHIẾN LƯỢC (STRATEGY BRIEF):**
   
   Nhập tâm Script Architect (= kết hợp Macro Strategist + Narrative Director).
   
   Tạo `episodes/[slug]/03_brief.md`. File này **BẮT BUỘC** sử dụng dữ liệu cứng đã được thu thập từ `02_research_map.md` (Pha 2) để điền vào phần Neo Số Liệu. Không tự bịa số liệu.

   File `03_brief.md` **BẮT BUỘC** chứa đủ các mục sau (checklist cứng):

   ```
   ✅ Checklist output bắt buộc của Pha 3:
   [ ] Luận đề trung tâm (một câu dao cạo, không phải mô tả chung)
   [ ] Phản đề và cách bẻ gãy phản đề đó
   [ ] Chế độ kết: A (chốt lập trường + điều kiện có thể sai) hoặc B (kết mở có cấu trúc: các cách đọc cạnh tranh + biến số quyết định), kèm lý do chọn — `00_core/stance_and_judgment.md` §1
   [ ] Chân dung khán giả — nhân vật đại diện cụ thể (tên, tuổi, hoàn cảnh tài chính; chỉ dùng nội bộ để định hướng, không đưa nhân vật này vào lời thoại)
   [ ] Nỗi đau đa tầng — các tầng nỗi đau cụ thể gắn với các nhóm chịu tác động
   [ ] Điểm độ sâu chủ đề (Topic Depth Score) — 5 tiêu chí, đã tính tổng
   [ ] Cam kết với khán giả — 3 điều họ sẽ có sau khi xem
   [ ] Hành trình tư duy (Logic Arc) — từng chương có tên và vai trò rõ
   [ ] Neo số liệu — bảng số liệu đã kiểm chứng kèm nguồn (Lấy từ research_vault)
   [ ] Vùng cấm — ít nhất 5 điều KHÔNG làm
   [ ] Dấu vân tay giọng văn — giọng điệu chủ đạo của toàn tập
   ```

   Điều chỉnh ngôn ngữ: Mọi thuật ngữ tiếng Anh phải Việt hóa theo quy tắc trong `00_core/voice_dna.md` (Mục 8).

4. Xác nhận brief đã có đủ: chân dung khán giả, nỗi đau tài chính, cam kết, giọng điệu, neo số liệu thật và vùng cấm (không khuyên mua/bán).

5. Thông báo cho user duyệt Pha 3 trước khi tiếp tục `/build_outline` (Pha 4, Outline-First; Hook Lab là Pha 5, chạy sau khi dàn ý được duyệt).
