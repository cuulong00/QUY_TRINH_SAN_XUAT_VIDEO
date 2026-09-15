---
description: >-
  Build Thesis Map, Retention Map, Outline, and Chapter Briefs (Phases 5-8).
  Requires completed 03_brief.md and 04_hook_pack.md.
  MUST be run after /hook_lab and before /write_chapter.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_macro_strategist.md`
2. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_narrative_director.md`
3. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ outline, thesis map, hay chapter brief nào nếu chưa đọc đủ 3 file trên.

---

## Kiểm tra đầu vào bắt buộc

Trước khi bắt đầu, xác nhận các file sau đều đã tồn tại:
- `episodes/[slug]/03_brief.md` ✅
- `episodes/[slug]/02_research_map.md` ✅
- `episodes/[slug]/04_hook_pack.md` ✅

Nếu thiếu bất kỳ file nào → DỪNG, thông báo cho user chạy workflow còn thiếu trước.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/longform_blueprint.md`, `00_core/voice_dna.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/02_research_map.md`, `episodes/[slug]/04_hook_pack.md`.

3. Đọc `00_core/reference_stories.md` để tránh dùng lại case study hoặc ẩn dụ cũ.

4. **PHA 5 — BẢN ĐỒ LUẬN ĐỀ:**
   - Tạo `episodes/[slug]/05_thesis_map.md` — vạch rõ luận điểm logic trung tâm và hành trình phân tích.

5. **PHA 6 — BẢN ĐỒ GIỮ CHÂN:**
   - Tạo `episodes/[slug]/06_retention_map.md` — lên kịch bản micro-hook, câu hỏi bỏ ngỏ, và điểm căng thẳng cao xuyên suốt video.
   - **BẮT BUỘC lên kế hoạch:** Móc giữ #1 tại ~3:30 | Cú sốc dữ liệu mới tại ~7:00 | Móc giữ #3 tại ~11:00.

6. **PHA 7 — DÀN Ý (6–8 chương):**
   - Tạo `episodes/[slug]/07_outline.md` theo `00_core/longform_blueprint.md`.

   **⛔ KIỂM TRA PHÂN LOẠI CHỦ ĐỀ (HARD GATE TRƯỚC KHI DỰNG OUTLINE):**
   - Mở `episodes/[slug]/03_brief.md` và tìm mục `## Phân Loại Chủ Đề`.
   - Nếu CHƯA CÓ mục này → DỪNG, chạy Topic Type Classification Gate trong `script_architect/SKILL.md` và ghi kết quả vào `03_brief.md` trước.
   - Đọc kết quả phân loại (Loại A / B / C) và áp dụng cấu trúc tương ứng:

    **Cấu trúc theo Loại A (ảnh hưởng trực tiếp túi tiền):**
    - Chương 1 = Hook + Open Loop (kích hoạt sự tò mò và tính liên quan thực tế)
    - Chương 2 = Relevance Anchor (kết nối logic vĩ mô với bối cảnh đời sống thực tế một cách tự nhiên)
    - Chương 3+ = Giải mã cơ chế + Dữ liệu thực tế + Tương tác tự nhiên

    **Cấu trúc theo Loại B (phân tích chiến lược doanh nghiệp/quốc gia) & Loại C (documentary toàn cầu):**
    - Chương 1 = Hook + Open Loop (gắn với nghịch lý vĩ mô hoặc bài học chiến lược)
    - Chương 2 = Lớp phân tích logic tiếp theo (đi sâu làm rõ nguyên nhân hoặc thiết lập bối cảnh)
    - Chương 3+ = Giải mã cơ chế + Soi chiếu tương quan + Case study trong/ngoài nước linh hoạt

   **NGHIÊM CẤM trong dàn ý (áp dụng cho MỌI loại):**
   - Đoạn hơn 3 phút chỉ có phân tích/lý thuyết không có data shock, zoom-in, hoặc loại suy đời thường
   - Câu mở tự đóng loop (câu chuyện hoàn chỉnh ở Chương 1)

   ```
    ✅ Checklist output bắt buộc của Pha 7:
    [ ] Chương 2 giải quyết lớp phân tích tiếp theo hoặc tạo liên hệ thực tế một cách logic
    [ ] Có các điểm neo giữ chân (Re-hook tại mốc ~3:30, Data Shock tại ~7:00, Re-hook tại ~11:00 nếu cần)
    [ ] Số lượng và thời lượng các case study được tối ưu hóa cho lập luận, tránh dàn trải
    [ ] Câu mở (Hook) mở loop rõ ràng, kích thích tò mò
    ```

7. **PHA 7b — CỬA KIỂM TRA GIỮ CHÂN (BẮT BUỘC trước khi làm Pha 8):**
   - Chạy Retention Checkpoint từ `00_core/retention_gate_checklist.md`.
   - Nếu dàn ý không đạt ≥ 8/10 tiêu chí → PHẢI sửa dàn ý trước khi sang bước tiếp.

8. **PHA 8 — TÓM LƯỢC TỪNG CHƯƠNG:**
   - Tạo `episodes/[slug]/08_chapter_briefs.md`.
    - Mỗi chương **BẮT BUỘC** có đủ các trường nội dung cốt lõi của Script Architect SKILL: `purpose`, `chapter_thesis`, `editorial_perspective`, `data_verified`, `counter_argument`, `key_insight`, `chapter_signature`, `target_words`, `research_vault_insights`, `counter_thesis_data`.
    - **Tóm lược Chương 2:** Định rõ cách tiếp cận tiếp theo sau Hook, liên hệ thực tiễn một cách tự nhiên và logic với bối cảnh khán giả hoặc Việt Nam nếu cần thiết.
    - KHÔNG bao giờ hướng dẫn người viết dùng câu chuyển tiếp cơ học (`bridge_to_next`, `bridge_out`). Chuyển ý phải đến từ luồng logic dữ liệu.

    ```
    ✅ Checklist output bắt buộc của Pha 8:
    [ ] Mỗi chương có đủ các trường thông tin cốt lõi trong tóm lược
    [ ] Mỗi chương có chapter_signature (dấu vân tay giọng văn) rõ nét
    [ ] Không có chương nào thiếu data_verified (mọi luận điểm phải dựa trên dữ liệu đã xác thực)
    ```

8b. **KHỞI TẠO NARRATIVE STATE TRACKER (NST):**
    - Tạo tệp `episodes/[slug]/09_narrative_state_tracker.md` bằng cách sao chép cấu trúc từ tệp template `02_templates/episode_template/09_narrative_state_tracker.md`.
    - Tệp này sẽ đóng vai trò bộ nhớ trạng thái động lưu trữ dữ liệu và sự liên kết giữa các chương kịch bản trong suốt Pha 9.

9. Yêu cầu user duyệt toàn bộ cấu trúc vĩ mô (Pha 5–8) trước khi bắt đầu viết chương bất kỳ.