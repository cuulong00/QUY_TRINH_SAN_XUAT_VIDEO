---
description: >-
  Build Master Outline Engine (Phase 4).
  Requires completed 03_brief.md and 01_global_vision_synthesis.md.
  MUST be run after /build_brief and BEFORE /hook_lab (Outline-First, Hook-Last Protocol).
---

> 🧭 **Cổng vào: thẻ `.agents/phases/pha_04_outline.md`**  (và pha_06_chapter_brief cho chapter briefs). Thẻ nói đọc gì và không cần đọc gì; workflow này là tham khảo theo mục.

> 🎯 Dàn ý ghi chế độ kết (A chốt lập trường + điều kiện có thể sai / B kết mở có cấu trúc + biến số quyết định), theo `00_core/stance_and_judgment.md` §1.

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI đọc lần lượt:

1. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_editorial_strategist.md`
2. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_dialectic_architect.md`
3. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_critical_auditor.md`
4. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ outline, thesis map, hay chapter brief nào nếu chưa đọc đủ 4 file trên. (Danh sách khớp Pre-flight và bảng pha Pha 4; kiểm bằng `scripts/kiem_dna.py --persona`.)

---

## Kiểm tra đầu vào bắt buộc

Trước khi bắt đầu, xác nhận các file sau đều đã tồn tại:
- `episodes/[slug]/03_brief.md` ✅
- `episodes/[slug]/02_research_map.md` hoặc `02_research_synthesis.md` ✅
- `episodes/[slug]/01_global_vision_synthesis.md` ✅

Nếu thiếu bất kỳ file nào → DỪNG, thông báo cho user chạy workflow còn thiếu trước.
*(Lưu ý: Theo chuẩn Outline-First Hook-Last, `04_hook_pack.md` sẽ được tạo SAU khi hoàn tất `07_outline.md`).*

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `episodes/[slug]/00_hien_chuong.md` (đề bài khóa, N1–N5, lăng kính đã chọn), `episodes/[slug]/00_bang_gia_thuyet.md` (giả thuyết còn đứng, bằng chứng BÁC còn đứng → Devil's Chapter), `00_core/longform_blueprint.md`, `00_core/voice_dna.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/02_research_synthesis.md`, `episodes/[slug]/01_global_vision_synthesis.md`.

3. Đọc `00_core/reference_stories.md` để tránh dùng lại case study hoặc ẩn dụ cũ.

4. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo bất kỳ file nào (`07_outline.md`, `08_chapter_briefs.md`, `09_narrative_state_tracker.md`), Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO <Tên_File_Đích>]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Editorial Strategist + The Dialectic Architect + The Critical Auditor
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/build_outline` (`script_architect/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * `episodes/[slug]/03_brief.md` (Chiến lược & Lời hứa cốt lõi)
   >   * `episodes/[slug]/01_global_vision_synthesis.md` (Bản đồ Bàn cờ & Tầm nhìn 4 tầng)
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/[Tên_File_Đích]`
   > - 🛡️ **Rào Cản Kiểm Toán:** The Single Spine — 100% các chương phục vụ tháo ngòi biến cố trung tâm; cấu trúc Therefore/But; định vị The Grand Payoff; cấm giấu bài ở chương kết; Orientation Frame khóa cứng cho CH01.
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
   - Source Documents Consulted: 03_brief.md, 01_global_vision_synthesis.md, 02_research_synthesis.md
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```

   #### 🎯 CÁCH KỂ CỦA TẬP — HÌNH DUNG TRƯỚC KHI DỰNG CHƯƠNG (Bắt buộc đầu Pha 4):
   Trước khi bước vào chia chương và tính toán ngân sách, người dựng dàn ý BẮT BUỘC hình dung cách kể riêng cho chủ đề và tự trả lời bằng lời của mình (3–6 câu trong `07_outline.md`):
   - *Với chủ đề này và khán giả nam 35–40 hiểu biết, điều gì làm họ muốn nghe tới cuối?*
   - *Câu chuyện nên đi theo dạng nào?* (Ví dụ chỉ để mở óc, KHÔNG phải danh sách bắt chọn: theo dấu một đồng tiền, giải một câu đố, đặt hai con đường cạnh nhau, đi ngược từ một hệ quả, theo một quyết định qua các bên... Định hướng tư duy, không có khuôn kể chung cho mọi tập; tuyệt đối không biến thành bảng chọn máy móc; tả cảnh không phải là cách mặc định để có giá trị nghệ thuật, hạn chế tả cảnh không mang dữ kiện).
   - *Vì sao dạng ấy hợp chủ đề này hơn các dạng khác?*
   - *Vật chứng nào trong nghiên cứu/sổ dữ kiện sẽ gánh câu chuyện?*
   Phiếu A cấp bài (`00_core/narrative_craft_rubric.md` §4) sẽ chấm dàn ý theo đúng cách kể đã chọn này.

   **QUY TRÌNH KIẾN TRÚC DÀN Ý 5 TRẠM (THE 5-STAGE OUTLINE FORGE):**
   
   #### 🏛️ TRẠM 1: Khóa Quy Mô & Tổng Ngân Sách Toàn Tập (Macro Budget Lock)
   - Đọc kết quả phân loại đề tài từ `03_brief.md` và chạy bảng Topic Depth Score để xác định tập phim thuộc Cấp độ nào trong 4 Cấp độ:
     * **Cấp 1 (Gọn / Nhanh):** 8 – 15 phút ($W_{\text{total}} = 1.800 – 3.300\text{ từ}$ | 4 – 5 chương)
     * **Cấp 2 (Tiêu chuẩn):** 16 – 25 phút ($W_{\text{total}} = 3.500 – 5.500\text{ từ}$ | 6 – 7 chương)
     * **Cấp 3 (Chuyên sâu):** 26 – 35 phút ($W_{\text{total}} = 5.700 – 7.700\text{ từ}$ | 7 – 9 chương)
     * **Cấp 4 (Sử thi / Đại phóng sự):** 36 – 45+ phút ($W_{\text{total}} = 8.000 – 10.000+\text{ từ}$ | 9 – 12 chương)
   - Khóa cứng con số Tổng ngân sách từ $W_{\text{total}}$ dựa trên tốc độ đọc chuẩn thực chứng: **$V = 223\text{ từ/phút}$** (mốc dưới của chuẩn 223–235 trong `.agents/AGENTS.md`).

   #### 🏛️ TRẠM 2: Bản Đồ Nhịp Chuyện (đơn vị dựng chương là NHỊP, không phải điểm dữ liệu)
   > Sửa 06/10/2026: khi đơn vị dựng chương là "điểm dữ liệu" (quota mã DATA-XX, mỗi số một khoản chữ), người viết lắp chương thành chuỗi "số, giải thích, số" và tập phim đọc như báo cáo. Số liệu là bằng chứng phục vụ nhịp, không phải đơn vị cấu thành.
   - Mỗi chương là **một câu hỏi điều tra** mà người xem muốn biết câu trả lời, thường đi qua vài nhịp chuyện (tham chiếu nhịp kể, không phải quota cơ học). Mỗi nhịp mang đúng một chức năng:
     * **Câu hỏi / bí ẩn:** đặt điều người nghe chưa hiểu hoặc một nghịch lý giữa hai sự thật.
     * **Manh mối:** một vật chứng cụ thể (một văn bản, một công trình, một con số đặt cạnh con số khác, một quyết định, một khoảnh khắc có ngày giờ) dẫn người nghe tới gần câu trả lời.
     * **Cú lật:** dữ kiện làm đổi cách hiểu đang có (ví dụ: đặt cách hiểu thông thường trước, đưa dữ kiện làm đổi cách hiểu sau).
     * **Hệ quả:** điều đó có nghĩa gì với câu hỏi lớn của tập, và mở câu hỏi kế tiếp.
   - Mỗi nhịp có **tối đa 1 đến 2 con số chính** để người nghe nhớ. Số còn lại của nhịp đánh dấu "lên hình" (infographic) thay vì đọc. Ghi rõ trong outline: nhịp, chức năng, vật chứng, số chính, số lên hình.
   - Vẫn chia dữ kiện độc quyền cho từng chương để không lặp (mã F hoặc DATA-XX), nhưng mỗi mã phải gắn vào một nhịp cụ thể; mã không gắn được vào nhịp nào thì không đưa vào chương.
   - Ít nhất **một cú lật** trong mỗi chương (trừ chương kết theo chế độ B, nơi cú lật là hai cách đọc), và chương 1 phải gài trước câu hỏi mà một chương sau sẽ lật.
   - Đếm số nhịp ($N_i$) và số mắt xích cơ chế ($M_i$) của mỗi chương để dùng ở Trạm 5.

   #### 🏛️ TRẠM 3: Thiết Kế Sóng Nhịp Điệu, Orientation Frame & Ma Trận Ngân Sách Co Giãn (Pacing Architecture)
   - **ORIENTATION FRAME (Khung Định Hướng 45–60s), sửa 06/10/2026:**
     Trong Chương 1, sau Hook (30–45s), người xem cần nắm được bàn cờ để không lạc. Dành 150–200 từ để:
     1. Định vị các thế lực hoặc bộ phận chính trên bàn cờ, bằng hình ảnh và quan hệ giữa chúng.
     2. Nêu rõ mâu thuẫn ngầm và nghịch lý trung tâm từ `01_global_vision_synthesis.md`, thành một câu hỏi người xem muốn biết đáp án.
     3. **KHÔNG đọc mục lục video** ("hành trình của chúng ta đi qua ba trạm", "trạm đầu là…", "trong video này chúng ta sẽ…"). Người xem biết mình sắp đi đâu nhờ câu hỏi đã được đặt, không nhờ bản liệt kê. Đây là lối báo cáo.
   - **CƠ CHẾ ZOOM IN $\leftrightarrow$ ZOOM OUT:** Phân bổ các điểm neo kéo người xem lên cao nhìn lại bản đồ sau các phân đoạn mổ xẻ kỹ thuật sâu.
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
   - Xương sống đi theo luật "Từ ma trận ra mạch kể" (`.agents/skills/script_architect/SKILL.md` §1 mục 10): chính đề là giả thuyết khán giả tin sẵn, phản đề là các hàng E phân biệt được đưa ra từng cú, hợp đề là giả thuyết còn đứng kèm cái giá và điều kiện sai. Mỗi chương viết được câu "người xem đang nghĩ X, bằng chứng Y làm họ nghĩ lại thành Z".

   #### 🏛️ TRẠM 5: Cổng Thẩm Định Tải Trọng, Lan Can Co Giãn & Phân Hạch (The Safeguard Gate)
   - Tính toán Bộ ba thông số kỹ thuật cho từng chương:
     * $\text{Target\_Words}(i) = W_{\text{total}} \times \% \text{Role\_Weight}(i)$
     * $\text{Floor}(i) = \text{Target\_Words}(i) \times 0.85$ (Sàn tối thiểu: Chống viết nông cạn, cụt ý)
     * $\text{Ceiling}(i) = \text{Target\_Words}(i) \times 1.15$ (Trần tối đa: Chống bành trướng, padding)
   - **Kiểm tra Tải trọng Tối thiểu (Anti-Amputation):**
     * Tính $\text{Min\_Payload\_Budget} = (N_i \times 110\text{ từ}) + (M_i \times 120\text{ từ}) + 80\text{ từ}$, với $N_i$ là số nhịp chuyện (Trạm 2), $M_i$ là số mắt xích cơ chế. Mỗi nhịp cần chỗ để đặt câu hỏi, đưa vật chứng và nói hệ quả; không cấp chữ theo từng con số (công thức cũ $D_i \times 35$ từ đã bỏ ngày 06/10/2026 vì nó biến chương thành chuỗi khoản số liệu).
     * Nếu $\text{Floor}(i) < \text{Min\_Payload\_Budget}$ ➔ nâng $\text{Target}$ hoặc bớt nhịp; CẤM cắt xén cơ chế. Thừa số liệu thì đẩy lên hình, không nhồi vào lời đọc.
   - **Ngoại lệ "người nghe hiểu" (user duyệt 04/10/2026):** Chữ thêm vào để người nghe hiểu ngay khi nghe một lần (giải nghĩa thuật ngữ, nói thẳng kết luận thay vì để người nghe tự suy, gọi tên lại đối tượng, bổ chủ ngữ hoặc tân ngữ còn thiếu) không phải padding. Phần này được phép đẩy chương vượt $\text{Ceiling}(i)$ và đẩy cả tập vượt $W_{\text{total}}$; ghi số mới vào `07_outline.md` và báo user thời lượng mới. Trần 1.050 từ mỗi chương vẫn giữ: chạm trần thì cắt câu lặp ý trước, không cắt phần giải thích; vẫn thiếu chỗ thì tách chương theo quy tắc phân hạch dưới đây.
   - **Kích hoạt Quy tắc Phân hạch Chương (Narrative Fission Protocol):**
     * Ngưỡng trần sinh học thính giác: Bất kể video ở cấp độ nào, không một chương đơn lẻ nào được phép vượt quá **$1.050\text{ từ}$** (~$4.8\text{ phút}$).
     * Nếu tải trọng dữ liệu vượt quá $1.050\text{ từ}$ ➔ **CẤM CẮT XÉN Ý**, bắt buộc **TÁCH ĐÔI CHƯƠNG ĐÓ (Split/Fission)** thành 2 chương độc lập ngay trong Dàn ý (Phần 1: Bế tắc thể chế/chi phí; Phần 2: Cú va chạm cơ khí lõi).
   - **Chấm Phiếu A cấp bài trên `07_outline.md` (thêm 06/10/2026, đợt NARRATIVE-CRAFT):** Người dựng dàn ý tự soi bằng Phiếu A để rà soát câu yếu, không tự cho điểm. Phiếu A chính thức do người khác ngoài người dựng dàn ý (Auditor / Claude / agent khác) chấm mù trước khi xin user duyệt: đọc trọn dàn ý không ghi chép, rồi chấm I Câu hỏi kịch tính trung tâm, II Mức cược, III Gieo và gặt (điền bảng gieo/gặt dự kiến), IV-b Cao trào (vị trí theo % thời lượng), VII Giọng cấp bài (chế độ kết), X Kết và nghĩa, theo `00_core/narrative_craft_rubric.md` §4. Mọi điểm 4–5 và 1–2 trích câu từ dàn ý. Không viết chương trên một dàn ý chưa đạt mốc ĐẠT (§6). Phiếu in trong chat và lưu vào `episodes/[slug]/11_narrative_craft_scorecard.md` (bản chấm mù lưu mục 0b, bản tự soi lưu mục 0a).

   **⛔ KIỂM TRA PHÂN LOẠI CHỦ ĐỀ (HARD GATE TỪ `03_brief.md`):**
   - Mở `episodes/[slug]/03_brief.md` và áp dụng đúng kết quả phân loại (Loại A / B / C):
     * **Loại A (Đời sống chung):** Chương 1 = Hook gắn với đời sống chung / túi tiền; Chương 2 = Điểm chạm đời sống (quyền lợi, việc làm, chi phí); Nhịp tự sự thường xuyên kéo về đời sống thực tế (tham chiếu quanh mỗi 3–4 phút, kiểm bằng câu hỏi đọc trỏ về khung 10 chỉ tiêu: người nghe có còn thấy câu chuyện chạm tới mình không).
     * **Loại B (Doanh nghiệp & Thể chế):** Chương 1 = Sự tò mò trí tuệ & biến cố; Chương 2 = Bài toán doanh nghiệp/quốc gia (cơ chế vận hành, cạnh tranh, thể chế, chuỗi giá trị) và lớp phân tích logic tiếp theo (KHÔNG ép túi tiền cá nhân); Case study tuân thủ trần Q1 (tối đa 2 case study quốc tế, mỗi case ≤ 3 phút, có nguồn trong vault và phục vụ thấu suốt cơ chế, không kể lể xa rời mạch); Nhịp tự sự liên tục đào sâu bài học quản trị và đánh đổi thực tế.
     * **Loại C (Toàn cầu):** Chương 1 = Nghịch lý vĩ mô; Chương 2 = Relevance Anchor; Giữ chân bằng so sánh dữ liệu quốc tế có chọn lọc và liên hệ chiều sâu.

   ```
   ✅ Checklist output bắt buộc của Pha 4 (07_outline.md):
   [ ] Xác định rõ "Cách kể của tập" (3–6 câu hình dung cách kể, lý do chọn, vật chứng gánh câu chuyện, không dùng khuôn máy móc)
   [ ] Xác định rõ Phân cấp Quy mô (Cấp 1 / 2 / 3 / 4) và Tổng ngân sách từ W_total (@ 223 từ/phút, mốc dưới của chuẩn 223–235)
   [ ] Đầy đủ Bản đồ Tổng thể kết nối 100% bằng "Therefore / But" (0% "And Then")
   [ ] Mỗi chương có đủ Bộ ba thông số Kỹ thuật: [Floor – Target – Ceiling]
   [ ] Kiểm toán Tải trọng Nhận thức (Anti-Amputation): Đảm bảo Floor >= Min_Payload_Budget
   [ ] Cao trào Màn 2 phơi bày tử huyệt kỹ thuật / nút thắt bản chất cốt lõi
   [ ] Định vị rõ ràng The Grand Payoff ở Chương kết (Phản tư & Tầm nhìn tương lai)
   [ ] Mỏ neo vật lý từ 03_brief.md xuất hiện làm điểm tựa thị giác
   [ ] Mỗi chương có câu hỏi điều tra và bản đồ nhịp chuyện (tham chiếu thường vài nhịp: câu hỏi / manh mối / cú lật / hệ quả), có ít nhất một chỗ cách hiểu của người nghe đổi đi; mỗi nhịp chọn số chính cần nhớ, số còn lại ghi "lên hình"
   [ ] Mã dữ kiện chia độc quyền cho từng chương và gắn vào nhịp cụ thể; mã không gắn được vào nhịp thì bỏ khỏi chương
   [ ] Chương 1 không đọc mục lục video
   [ ] Phiếu A cấp bài (`00_core/narrative_craft_rubric.md`) do người khác ngoài người dựng dàn ý chấm và đạt mốc ĐẠT trước khi xin user duyệt; đã lưu vào `11_narrative_craft_scorecard.md`
   [ ] Mỗi Key Insight, Causal Exit, câu chốt trỏ mã `M-xx` (sổ dữ kiện) hoặc `E-xx`/`H-x` (bảng giả thuyết); không khẳng định vượt nhãn của mã được trỏ
   [ ] Bằng chứng BÁC còn đứng trong `00_bang_gia_thuyet.md` có chương chứa và dòng "luận điểm đổi gì"; chân đỡ Pha 1 (sổ dữ kiện, mục cuối) còn mặt hoặc có lý do bỏ
   [ ] Tuân thủ Quy tắc Phân hạch (Narrative Fission): Không chương nào vượt trần 1.050 từ
   ```

6. **HUMAN APPROVAL GATE (DÀN Ý):**
   - Thông báo và chờ User duyệt `07_outline.md`.
   - Sau khi User phê duyệt Dàn ý, **TIẾP TỤC CHUYỂN SANG PHA 5: HOOK LAB (`/hook_lab` ➔ `04_hook_pack.md`)**.

7. **PHA 6 — CHAPTER BRIEFS (RESEARCH DOSSIER + NHỊP CHUYỆN — 20 TRƯỜNG BẮT BUỘC):**
   - Sau khi hoàn thành và duyệt `04_hook_pack.md` (Pha 5), tiến hành tạo `episodes/[slug]/08_chapter_briefs.md`.
   - Mỗi chương BẮT BUỘC có đủ **20 trường chuẩn hóa** theo `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md`: 16 trường cũ cộng 4 trường nhịp chuyện thêm 06/10/2026 (`cau_hoi_dieu_tra`, `vat_chung`, `cu_lat`, `chu_the_va_dong_co`), ngang hàng `data_verified`. Brief chỉ có hàng dữ liệu mà thiếu 4 trường này thì chưa đạt.
   - Bảng Pointer chứng cứ gốc (Trường 10) phải có ít nhất 5 dòng trích dẫn nguyên văn ngắn (≤ 15 từ) từ `research_vault/` kèm Mã Footnote ID; mỗi dòng ghi nhịp mà dữ kiện phục vụ và cách dùng (đọc / lên hình).
   - User duyệt `08_chapter_briefs.md` và khởi tạo Sổ cái tự sự NST (`09_narrative_state_tracker.md` - Pha 6b) trước khi bắt đầu viết chương (Pha 7).