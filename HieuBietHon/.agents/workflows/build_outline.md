---
description: >-
  Build Thesis Map, Retention Map, Outline, and Chapter Briefs (Phases 5-8).
  Requires completed 03_brief.md and 04_hook_pack.md.
  MUST be run after /hook_lab and before /write_chapter.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/personas/the_macro_strategist.md`
2. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/personas/the_narrative_director.md`
3. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/skills/script_architect/SKILL.md`

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
   - Chương 1 = Hook + Open Loop (gắn với TÚI TIỀN người xem)
   - **Chương 2 = QUYỀN LỢI CÁ NHÂN** — BẮT BUỘC, NGHIÊM CẤM case study nước ngoài
   - Chương 3+ = Phân tích + Re-hook mỗi 3-4 phút kéo về đời sống cá nhân

   **Cấu trúc theo Loại B (phân tích chiến lược doanh nghiệp/quốc gia):**
   - Chương 1 = Hook + Open Loop (gắn với SỰ TÒ MÒ TRÍ TUỆ hoặc bài học chiến lược)
   - **Chương 2 = Lớp phân tích logic tiếp theo** (KHÔNG ép Personal Stakes thành 1 chương riêng)
   - Personal Stakes được dệt vào qua câu Zoom-In rải đều mỗi 3-4 phút xuyên suốt video
   - Ví dụ Zoom-In: "Nếu bạn đang cân nhắc mua xe VinFast, con số này cho thấy..."

   **Cấu trúc theo Loại C (documentary toàn cầu):**
   - Chương 1 = Hook + Open Loop (gắn với nghịch lý trí tuệ)
   - **Chương 2 = Relevance Anchor** — tại sao VN/khán giả nên quan tâm
   - Giữ chân bằng Data Shock + Comparison mỗi 4 phút, KHÔNG ép túi tiền
   - Cho phép đến 3 case study quốc tế

   **NGHIÊM CẤM trong dàn ý (áp dụng cho MỌI loại):**
   - Đoạn hơn 3 phút chỉ có phân tích/lý thuyết không có data shock, zoom-in, hoặc loại suy đời thường
   - Câu mở tự đóng loop (câu chuyện hoàn chỉnh ở Chương 1)

   ```
   ✅ Checklist output bắt buộc của Pha 7:
   [ ] Chương 2 rõ ràng là Quyền Lợi Cá Nhân, không phải lý thuyết
   [ ] Có móc giữ tại đúng vị trí (~3:30 và ~11:00)
   [ ] Cú sốc dữ liệu mới xuất hiện tại ~7:00
   [ ] Không quá 2 case study quốc tế
   [ ] Câu mở để ngỏ, không hoàn chỉnh
   ```

7. **PHA 7b — CỬA KIỂM TRA GIỮ CHÂN (BẮT BUỘC trước khi làm Pha 8):**
   - Chạy Retention Checkpoint từ `00_core/retention_gate_checklist.md`.
   - Nếu dàn ý không đạt ≥ 8/10 tiêu chí → PHẢI sửa dàn ý trước khi sang bước tiếp.
   - **🛑 YÊU CẦU DUYỆT (CHUNKING GATE):** Tạm dừng luồng làm việc tại đây. Xuất bản `07_outline.md` và Yêu cầu user duyệt Dàn ý (Pha 5-7) TRƯỚC KHI tạo Chapter Briefs (Pha 8). NGHIÊM CẤM làm tiếp Pha 8 nếu user chưa duyệt Dàn ý. Điều này giúp giảm tải bộ nhớ (Context Window) cho AI.

8. **PHA 8 — TÓM LƯỢC TỪNG CHƯƠNG (Chỉ thực hiện SAU KHI user đã duyệt Dàn ý):**
   - Tạo `episodes/[slug]/08_chapter_briefs.md`.
   - Mỗi chương **BẮT BUỘC** có đủ 11 trường theo Script Architect SKILL: `purpose`, `chapter_thesis`, `editorial_perspective`, `data_verified`, `counter_argument`, `personal_stakes_dimension`, `key_insight`, `chapter_signature`, `personal_angle`, `research_vault_insights`, `counter_thesis_data`.
   - **Tóm lược Chương 2:** Định hướng rõ ràng việc đi từ logic nghịch lý ở Chương 1 sang phân tích sâu chiến lược/dòng vốn. Cho phép mở rộng sáng tạo, không gò ép stakes cá nhân khiên cưỡng. Có thể đưa vào các case study hoặc dữ liệu quốc tế để tăng sức nặng lập luận nếu thật sự cần thiết.
   - KHÔNG bao giờ hướng dẫn người viết dùng câu chuyển tiếp cơ học (`bridge_to_next`, `bridge_out`). Chuyển ý phải đến từ luồng logic dữ liệu.

   ```
   ✅ Checklist output bắt buộc của Pha 8:
   [ ] Mỗi chương có đủ 12 trường trong tóm lược
   [ ] Mỗi chương có chapter_signature (dấu vân tay giọng văn) khác nhau
   [ ] Không có chương nào thiếu data_verified
   [ ] Tóm lược Chương 2 có ghi lệnh cấm case study nước ngoài
   ```

9. Sau khi tạo xong Pha 8, yêu cầu user duyệt `08_chapter_briefs.md` trước khi bắt đầu viết chương bất kỳ (Pha 9).