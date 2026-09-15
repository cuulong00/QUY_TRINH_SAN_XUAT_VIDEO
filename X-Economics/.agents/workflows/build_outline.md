---
description: >-
  Build Master Outline Engine (Phase 4).
  Requires completed 03_brief.md and vault/00_Global_Vision_Synthesis.md.
  MUST be run after /build_brief and BEFORE /hook_lab (Outline-First, Hook-Last Protocol).
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_macro_strategist.md`
2. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_narrative_director.md`
3. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ outline, thesis map, hay chapter brief nào nếu chưa đọc đủ 3 file trên.

---

## Kiểm tra đầu vào bắt buộc

Trước khi bắt đầu, xác nhận các file sau đều đã tồn tại:
- `episodes/[slug]/03_brief.md` ✅
- `episodes/[slug]/02_research_map.md` hoặc `02_research_synthesis.md` ✅
- `episodes/[slug]/vault/00_Global_Vision_Synthesis.md` ✅

Nếu thiếu bất kỳ file nào → DỪNG, thông báo cho user chạy workflow còn thiếu trước.
*(Lưu ý: Theo chuẩn Outline-First Hook-Last, `04_hook_pack.md` sẽ được tạo SAU khi hoàn tất `07_outline.md`).*

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/longform_blueprint.md`, `00_core/voice_dna.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/02_research_synthesis.md`, `episodes/[slug]/vault/00_Global_Vision_Synthesis.md`.

3. Đọc `00_core/reference_stories.md` để tránh dùng lại case study hoặc ẩn dụ cũ.

4. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo bất kỳ file nào (`07_outline.md`, `08_chapter_briefs.md`, `09_narrative_state_tracker.md`), Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO <Tên_File_Đích>]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Editorial Strategist + The Dialectic Architect + The Critical Auditor
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/build_outline` (`script_architect/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * `episodes/[slug]/03_brief.md` (Chiến lược & Lời hứa cốt lõi)
   >   * `episodes/[slug]/vault/00_Global_Vision_Synthesis.md` (Mỏ neo dữ liệu & Tầm nhìn 4 tầng)
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/[Tên_File_Đích]`
   > - 🛡️ **Rào Cản Kiểm Toán:** The Single Spine — 100% các chương phục vụ tháo ngòi biến cố trung tâm; cấu trúc Therefore/But; định vị The Grand Payoff; cấm giấu bài ở chương kết.
   ```
   Đồng thời BẮT BUỘC nhúng khối `DOCUMENT PROVENANCE & EXECUTION LINEAGE` ở đầu mỗi file markdown được tạo ra.

5. **PHA 4 — MASTER OUTLINE ENGINE (`episodes/[slug]/07_outline.md`):**
   Nhập tâm Script Architect (kết hợp `the_editorial_strategist` + `the_dialectic_architect` + `the_critical_auditor`).
   
   Tạo `episodes/[slug]/07_outline.md` theo cấu trúc Masterpiece ABT tương ứng với Cấp độ Thời lượng đã chọn (theo `02_templates/masterpiece_pipeline/07_outline_template.md`).
   BẮT BUỘC nhúng khối Provenance Metadata ở đầu tệp:
   ```markdown
   <!--
   DOCUMENT PROVENANCE & EXECUTION LINEAGE:
   - Output Document: episodes/[slug]/07_outline.md
   - Activated Persona: The Editorial Strategist + The Dialectic Architect + The Critical Auditor
   - Activated Skill: script_architect/SKILL.md (/build_outline)
   - Source Documents Consulted: 03_brief.md, vault/00_Global_Vision_Synthesis.md, 02_research_synthesis.md
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```

   **QUY TRÌNH KIẾN TRÚC DÀN Ý 5 TRẠM (THE 5-STAGE OUTLINE FORGE):**
   
   #### 🏛️ TRẠM 1: Khóa Quy Mô & Tổng Ngân Sách Toàn Tập (Macro Budget Lock)
   - Đọc kết quả phân loại đề tài từ `03_brief.md` và chạy bảng Topic Depth Score để xác định tập phim thuộc Cấp độ nào trong 4 Cấp độ:
     * **Cấp 1 (Gọn / Nhanh):** 8 – 15 phút ($W_{\text{total}} = 1.800 – 3.300\text{ từ}$ | 4 – 5 chương)
     * **Cấp 2 (Tiêu chuẩn):** 16 – 25 phút ($W_{\text{total}} = 3.500 – 5.500\text{ từ}$ | 6 – 7 chương)
     * **Cấp 3 (Chuyên sâu):** 26 – 35 phút ($W_{\text{total}} = 5.700 – 7.700\text{ từ}$ | 7 – 9 chương)
     * **Cấp 4 (Sử thi / Đại phóng sự):** 36 – 45+ phút ($W_{\text{total}} = 8.000 – 10.000+\text{ từ}$ | 9 – 12 chương)
   - Khóa cứng con số Tổng ngân sách từ $W_{\text{total}}$ dựa trên tốc độ đọc chuẩn thực chứng: **$V = 220\text{ từ/phút}$**.

   #### 🏛️ TRẠM 2: Quy Hoạch Lãnh Thổ Dữ Liệu & Kiểm Kê Tải Trọng (Payload Accounting)
   - Bổ quả cam dữ liệu `vault/00_Global_Vision_Synthesis.md` và `research_vault/` thành các phần độc quyền, cấp quota mã `DATA-XX` không trùng lặp cho từng chương.
   - Kiểm kê số lượng mỏ neo thực chứng ($D_i$) và số mắt xích cơ chế First-Principles ($M_i$) của mỗi chương.

   #### 🏛️ TRẠM 3: Thiết Kế Sóng Nhịp Điệu Đa Tầng & Ma Trận Ngân Sách Co Giãn (Pacing Architecture)
   - Áp dụng Ma trận Tỷ trọng Vai trò tương ứng với Cấp độ thời lượng:
     * **Cấp 2 (7 Hồi chuẩn - Đối xứng chuông quanh Đỉnh Màn 2):**
       CH01 (10% | ~440 từ) ➔ CH02 (13% | ~570 từ) ➔ CH03 (15% | ~660 từ) ➔ **CH04: ĐỈNH LÕI (24% | ~1.050 từ trần)** ➔ CH05 (15% | ~660 từ) ➔ CH06 (13% | ~570 từ) ➔ CH07 (10% | ~440 từ).
     * **Cấp 1 (5 Hồi tốc chiến):** CH01 (12%) ➔ CH02 (22%) ➔ **CH03: ĐỈNH (30%)** ➔ CH04 (22%) ➔ CH05 (14%).
     * **Cấp 4 (Sóng kép 10 Hồi):** Vòng 1 (CH01-CH05 có Đỉnh CH04: 18%) + Vòng 2 (CH06-CH10 có Đỉnh CH08: 18%), các chương khác dao động 7% - 11%.

   #### 🏛️ TRẠM 4: Đúc Xương Sống Nhân Quả (The Causal Spine Forge)
   - Viết chuỗi các câu liên kết 100% bằng "Therefore / But" (0% "And Then") tích hợp trực tiếp Logic Arc (Thesis) và Tension Arc (Retention) vào thẳng `07_outline.md`.
   - Thỏa mãn 3 rào cản kiểm toán:
     1. *The Single Spine Test:* 100% các chương đều trực tiếp quay quanh việc mổ xẻ Biến cố trung tâm phát nổ ở CH01.
     2. *Anti-Burying-The-Lede Test:* Nút thắt bản chất cốt lõi bắt buộc nổ ra ở Đỉnh cao trào Màn 2, cấm giấu bài ở chương kết.
     3. *The Russian Doll Test:* Mỗi chương tháo gỡ một lớp vỏ bề mặt để làm lộ ra tầng nghịch lý sâu hơn.

   #### 🏛️ TRẠM 5: Cổng Thẩm Định Tải Trọng, Lan Can Co Giãn & Phân Hạch (The Safeguard Gate)
   - Tính toán Bộ ba thông số kỹ thuật cho từng chương:
     * $\text{Target\_Words}(i) = W_{\text{total}} \times \% \text{Role\_Weight}(i)$
     * $\text{Floor}(i) = \text{Target\_Words}(i) \times 0.85$ (Sàn tối thiểu: Chống viết nông cạn, cụt ý)
     * $\text{Ceiling}(i) = \text{Target\_Words}(i) \times 1.15$ (Trần tối đa: Chống bành trướng, padding)
   - **Kiểm tra Tải trọng Tối thiểu (Anti-Amputation):**
     * Tính $\text{Min\_Payload\_Budget} = (D_i \times 35\text{ từ}) + (M_i \times 160\text{ từ}) + 80\text{ từ}$.
     * Nếu $\text{Floor}(i) < \text{Min\_Payload\_Budget}$ ➔ BẮT BUỘC nâng $\text{Target}$ lên tương ứng, CẤM cắt xén cơ chế hoặc số liệu để ép dung lượng!
   - **Kích hoạt Quy tắc Phân hạch Chương (Narrative Fission Protocol):**
     * Ngưỡng trần sinh học thính giác: Bất kể video ở cấp độ nào, không một chương đơn lẻ nào được phép vượt quá **$1.050\text{ từ}$** (~$4.8\text{ phút}$).
     * Nếu tải trọng dữ liệu vượt quá $1.050\text{ từ}$ ➔ **CẤM CẮT XÉN Ý**, bắt buộc **TÁCH ĐÔI CHƯƠNG ĐÓ (Split/Fission)** thành 2 chương độc lập ngay trong Dàn ý (Phần 1: Bế tắc thể chế/chi phí; Phần 2: Cú va chạm cơ khí lõi).

   **⛔ KIỂM TRA PHÂN LOẠI CHỦ ĐỀ (HARD GATE TỪ `03_brief.md`):**
   - Mở `episodes/[slug]/03_brief.md` và áp dụng đúng kết quả phân loại (Loại A / B / C):
     * **Loại A (Túi tiền cá nhân):** Chương 1 = Hook gắn với túi tiền; Chương 2 = Quyền lợi cá nhân; Re-hook mỗi 3-4 phút kéo về đời sống cá nhân.
     * **Loại B (Doanh nghiệp & Thể chế):** Chương 1 = Sự tò mò trí tuệ & biến cố; Chương 2 = Cơ chế chi phí và lớp phân tích logic tiếp theo (KHÔNG ép túi tiền cá nhân); Giới hạn đúng 1 Case Study quốc tế điển hình; Zoom-in bài học quản trị rải đều mỗi 3-4 phút.
     * **Loại C (Toàn cầu):** Chương 1 = Nghịch lý vĩ mô; Chương 2 = Relevance Anchor; Giữ chân bằng so sánh dữ liệu quốc tế (tối đa 3 case study).

   ```
   ✅ Checklist output bắt buộc của Pha 4 (07_outline.md):
   [ ] Xác định rõ Phân cấp Quy mô (Cấp 1 / 2 / 3 / 4) và Tổng ngân sách từ W_total (@ 220 WPM)
   [ ] Đầy đủ Bản đồ Tổng thể kết nối 100% bằng "Therefore / But" (0% "And Then")
   [ ] Mỗi chương có đủ Bộ ba thông số Kỹ thuật: [Floor – Target – Ceiling]
   [ ] Kiểm toán Tải trọng Nhận thức (Anti-Amputation): Đảm bảo Floor >= Min_Payload_Budget
   [ ] Cao trào Màn 2 phơi bày tử huyệt kỹ thuật / nút thắt bản chất cốt lõi
   [ ] Định vị rõ ràng The Grand Payoff ở Chương kết (Phản tư & Tầm nhìn tương lai)
   [ ] Mỏ neo vật lý từ 03_brief.md xuất hiện làm điểm tựa thị giác
   [ ] Quota mã DATA-XX phân bổ độc quyền cho từng chương, không trùng lặp
   [ ] Tuân thủ Quy tắc Phân hạch (Narrative Fission): Không chương nào vượt trần 1.050 từ
   ```

6. **HUMAN APPROVAL GATE (DÀN Ý):**
   - Thông báo và chờ User duyệt `07_outline.md`.
   - Sau khi User phê duyệt Dàn ý, **TIẾP TỤC CHUYỂN SANG PHA 5: HOOK LAB (`/hook_lab` ➔ `04_hook_pack.md`)**.

7. **PHA 6 — CHAPTER BRIEFS (RESEARCH DOSSIER — 16 TRƯỜNG BẮT BUỘC):**
   - Sau khi hoàn thành và duyệt `04_hook_pack.md` (Pha 5), tiến hành tạo `episodes/[slug]/08_chapter_briefs.md`.
   - Mỗi chương BẮT BUỘC có đủ **16 trường chuẩn hóa** theo `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md` (bổ sung Trường 15 `forbidden_echoes` và Trường 16 `perspective_shift_anchor`).
   - Bảng Pointer chứng cứ gốc (Trường 10) phải có ít nhất 5 dòng trích dẫn nguyên văn ngắn (≤ 15 từ) từ `research_vault/` kèm Mã Footnote ID.
   - User duyệt `08_chapter_briefs.md` và khởi tạo Sổ cái tự sự NST (`09_narrative_state_tracker.md` - Pha 6b) trước khi bắt đầu viết chương (Pha 7).