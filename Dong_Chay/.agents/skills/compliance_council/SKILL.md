---
name: compliance-council
description: "Editorial & Compliance Council for Dong Chay. Reviews script safety, legal compliance, oral rhythm, Tri-Adversarial Red Team rigor, and Popperian falsification."
---

# Editorial & Compliance Council — Hội Đồng Thẩm Tra & Phê Duyệt Kiệt Tác Dòng Chảy (Phiên Bản Tư Duy 3.0)

> 🧭 **Phân vai cổng chấm (29/09/2026):** Mỗi khâu chỉ có MỘT cổng PASS/FAIL — Dàn ý: `00_core/retention_gate_checklist.md` (Gate 1) · Kịch bản nháp: `00_core/retention_gate_checklist.md` (Gate 2) · Cả kịch bản (Pha 10–11): `.agents/skills/compliance_council/SKILL.md` (ngưỡng ≥ 8.5/10, không trụ cột nào < 7.5). `00_core/quality_rubric.md` là bộ tiêu chí tham chiếu, không phải cổng riêng.
> **Cổng loại ngay hợp nhất (áp tại đây):** 11 Hard-Fail của `00_core/quality_rubric.md` §4 (điều 11 là chất chuyện, `00_core/narrative_craft_rubric.md`) + các cờ đỏ ở mục 4 dưới đây + 5 câu kiểm lập trường của `00_core/stance_and_judgment.md` §10. Điều kiện trùng nhau giữa các nguồn chỉ tính một lần. Vi phạm bất kỳ điều nào → KHÔNG ĐẠT, dù tổng điểm cao.

> 🎯 **Kiểm lập trường (bắt buộc):** Chấm theo 5 câu hỏi ở `00_core/stance_and_judgment.md` §10 trong trụ cột biện chứng/biên tập. Chế độ A hay B đều hợp lệ; kết lửng lơ mới là lỗi. Nhãn phán xét thay cho dữ kiện, phán xét động cơ hay đạo đức, hoặc lặp "chúng tôi cho rằng" quá 4 lần đều là lỗi phải sửa trước khi đạt ngưỡng.

> 🛑 **EXPERT PERSONAS (BẮT BUỘC HÓA THÂN)**
> Kỹ năng này kích hoạt Hội đồng Thẩm tra Tối cao gồm:
> 1. `the_critical_auditor` (Chủ Tịch Hội Đồng — Giám đốc Thẩm tra Pháp lý, Kỹ thuật & Tài chính Forensic, nắm Veto Power)
> 2. `the_editorial_strategist` (Tổng Biên Tập Chiến Lược — Kiểm toán Sợi chỉ đỏ, Therefore/But, Chống giấu bài ở chương kết)
> 1b. `the_data_auditor` (Kiểm toán số liệu — số này đo cái gì, phương pháp đo có khớp với kết luận không, diễn giải có vượt phạm vi không) · ví dụ yếu/mạnh: `.agents/examples/editorial_qa_examples.md`
> 3. `the_policy_analyst` (Chuyên Gia Thể Chế — Kiểm toán tính chuẩn xác của văn bản luật, số hiệu Nghị định, Thông tư)
> 3b. `the_compliance_editor` (Biên Tập Tuân Thủ — ranh giới Bình luận vs. Tư vấn Đầu tư theo `00_core/financial_boundaries.md`, an toàn thương hiệu theo `00_core/brand_safety_guidelines.md`, taxonomy `verified_data`/`market_analysis`/`opinion_commentary`)
> 4. `the_voice_architect` & `the_quality_czar` (Giám sát Kỷ luật Tai nghe & An toàn TTS trên RunPod GPU)
>
> Nếu chưa nạp đủ các chuyên gia này trong phiên làm việc, NGHIÊM CẤM tạo báo cáo compliance.

---

## 1. SÁU KHÓA KIỂM TOÁN TỐI THƯỢNG (THE 6 IMPERATIVE AUDIT GATES)

Trước khi ký duyệt bất kỳ kịch bản nào của Dòng Chảy, Hội đồng thẩm tra kịch bản qua 6 khóa sinh tử:

### Khóa 1: Zero-Ungrounded-Inference (ZUI — Khóa Chân Lý Thực Chứng)
- **Level 1 (Fact):** 100% số liệu, tên tập đoàn, số hiệu văn bản pháp lý, ngày tháng, dòng tiền tự do (FCF) phải có Footnote ID và trích dẫn gốc trong `research_vault/`. Tuyệt đối CẤM đoán mò các chi phí chưa công bố.
- **Level 2 (Grounded Inference):** Suy diễn sâu bắt buộc phải đi theo công thức:
  $$\text{Tiền đề Thực chứng (Fact)} + \text{Quy luật Khách quan (First Principles)} \Longrightarrow \text{Suy diễn Có căn cứ}$$
- **Level 3 (Speculation):** Tự bịa số liệu kỹ thuật, tự phỏng đoán động cơ cá nhân $\rightarrow$ **ĐÁNH TRƯỢT TỨC THÌ (FAIL)**.

### Khóa 2: Steelmanning & Trade-Offs (Khóa Phản Biện Đối Trọng & Sự Đánh Đổi)
- **Triệt tiêu Bù Nhìn Rơm (Anti-Strawman):** Lập luận của phe phản biện phải được xây dựng ở phiên bản mạnh nhất, sắc bén nhất, có số liệu đối kháng thuyết phục nhất.
- **Tri-Adversarial Red Team Council:** Tra vấn kịch bản qua 3 lăng kính:
  1. *The Market Skeptic:* Bóc trần méo mó phân bổ vốn, bao cấp, doanh nghiệp xác sống, chi phí cơ hội.
  2. *The Institutional Realist:* Ma sát quan liêu, nhóm lợi ích, rủi ro trả đũa thuế quan/thương mại quốc tế.
  3. *The Forensic Cash Auditor:* Dòng tiền tự do FCF âm, nợ ngắn hạn nuôi tài sản dài hạn, điểm hòa vốn viển vông.
- **Khóa Cứng `[THE DEVIL'S CHAPTER]`:** Bắt buộc có 1 chương phản đề độc lập tại cao trào Hồi 2 (50–70% thời lượng).
- **Thừa Nhận Đánh Đổi (`admitted_trade_offs`):** Mọi giải pháp đều phải chỉ rõ cái giá phải trả và chi phí cơ hội; cấm tô hồng giải pháp thần thánh.

### Khóa 3: Single Narrative Spine & Therefore/But (Khóa Sợi Chỉ Đỏ & Nhân Quả)
- Mọi chương có phục vụ việc mổ xẻ Biến cố trung tâm phát nổ ở đầu video không?
- Mạch tự sự có loại trừ hoàn toàn lối kể chuyện ngăn tủ rời rạc ("And Then...") để vận hành bằng động lực nhân quả "Vì vậy..." hoặc "Nhưng..." không?

### Khóa 4: Anti-Burying-The-Lede (Khóa Vị Trí Cao Trào)
- Điểm gãy cấu trúc lớn nhất bắt buộc phải nổ ra ở cao trào Màn 2 (`[THE DEVIL'S CHAPTER]`). Tuyệt đối cấm giấu bí mật kỹ thuật/kinh tế xuống 2 phút cuối của video.

### Khóa 5: Oral Voice & Zero-Scaffolding (Khóa Khẩu Ngữ & Sạch Rác Khung Sườn)
- 100% câu thoại dưới 150 ký tự, đầy đủ chủ - vị, tốc độ nói 223–235 từ/phút (`.agents/AGENTS.md`).
- Gom 2–4 câu thành đoạn văn trôi chảy; cấm ngắt dòng sau mỗi câu đơn lẻ.
- Sạch 100% từ cấm AI (`anti_ai_isms.md`), không có dấu gạch ngang dài (`—`).
- Tuyệt đối không còn nhãn template `[BLOCK X]`, `[HOOK MÔ TẢ]` trong văn bản thành phẩm.
- **Soi và đọc phán dấu hiệu cấu trúc** theo `00_core/anti_ai_isms.md` §3b trên từng chương (bảng "Soi rồi đọc"). Máy liệt kê câu khớp S1–S7 và nhóm yếu; đọc từng câu trong ngữ cảnh: nếu không mang dữ kiện/hệ quả mới hoặc nghe như khuôn máy → trừ trụ cột giọng/nhịp và sửa trong nhật ký sửa đổi. Khi sửa chỉ đổi cách nói, không thêm dữ kiện mới.


### Khóa 6: Narrative Craft, chấm mù hai cấp (viết lại 06/10/2026, đợt NARRATIVE-CRAFT)
Chuẩn chấm: `00_core/narrative_craft_rubric.md` (10 chỉ tiêu, hai cấp, mốc ĐẠT, ngân hàng đoạn mẫu). Người chấm: `the_critical_auditor`.
1. **Chấm mù:** Critical Auditor KHÔNG mở bản tự soi của người viết (Phiếu B trong `11_narrative_craft_scorecard.md`, hay phiếu in trong chat) trước khi nộp phiếu của mình. Khi có nhiều agent, lượt này chạy ở hội thoại khác với người viết.
2. **Đọc trọn cả tập, không ghi chép**, rồi chấm Phiếu A (cấp bài: I, II, III, IV-b, VII cấp bài, X, bảng gieo/gặt), rồi Phiếu B (cấp chương: IV-a, V, VI, VII, VIII, IX, cột "đẩy câu hỏi đi bao xa"). Mọi điểm 4–5 và 1–2 trích câu; không dùng phép đếm (số liệu, câu hỏi, cảnh) thay cho việc đọc.
3. **Đối chiếu với bản tự soi** sau khi đã nộp phiếu: người chấm mù đọc danh sách chỗ yếu của người viết; chỗ nào người viết thấy yếu mà người chấm mù cho 4–5, hoặc ngược lại (người viết không thấy yếu mà chấm mù cho 1–2), thì hai bên đọc lại đúng đoạn đó, ghi điểm thống nhất và lý do. Điểm chính thức là của người chấm mù (hoặc điểm thống nhất sau đối chiếu).
4. **Đối chiếu hai cấp** (`narrative_craft_rubric.md` §5): cấp bài cao, cấp chương thấp → trả về Pha 7 kèm lệnh sửa từng chương; cấp chương cao, cấp bài thấp → trả về Pha 4 sửa dàn ý; cả hai thấp → Pha 4 rồi Pha 7.
5. **Điểm K** (thang 20 của `00_core/quality_rubric.md`) = (trung bình cấp bài + trung bình cấp chương) ÷ 2 × 4, lấy từ kết quả chấm mù chính thức (hoặc điểm thống nhất sau đối chiếu), tuyệt đối không lấy từ bản tự soi của người viết; ghi vào báo cáo. K không đạt mốc ĐẠT thì KHÔNG ĐẠT dù 4 trụ cột ≥ 8,5; Hard-Fail 11 của `quality_rubric.md` §4 áp tại đây.
6. Lưu cả hai phiếu (bản tự soi, bản chấm mù, điểm thống nhất, lệnh sửa) vào `episodes/[slug]/11_narrative_craft_scorecard.md`.
- Lý do: tập `gdp-9-thang-2026-con-so-10-tu-dau` qua đủ Khóa 1 đến 5 mà vẫn đọc như báo cáo; các khóa cũ kiểm dữ liệu, nhân quả và câu chữ, không kiểm chất chuyện.
---

## 2. NGUYÊN LÝ THẨM TRA NÂNG CAO (ADVANCED AUDIT PRINCIPLES)

### A. Tư Duy Bậc Hai & Bậc Ba (Second-Order & Third-Order Thinking)
- Tra vấn kịch bản:
  * Sau 2–3 năm áp dụng chính sách/mô hình này, thị trường sẽ thích nghi và tìm cách né đòn như thế nào?
  * Sau 5 năm, rủi ro hệ thống sẽ tích tụ ở đâu? Ai là người cuối cùng phải trả tiền?

### B. Thước Đo Khả Năng Bác Bỏ Của Popper (Popperian Falsification Heuristic)
- Kiểm tra xem các luận đề chính có điều kiện bác bỏ rõ ràng không: *"Dữ liệu thực tế nào xuất hiện sẽ chứng minh luận điểm này sai?"*
- Nếu một luận đề được diễn giải theo kiểu "thế nào cũng đúng", trốn tránh kiểm chứng thực nghiệm $\rightarrow$ Loại bỏ.

---

## 3. CHỈ SỐ CHẤT LƯỢNG KỊCH BẢN (SCRIPT QUALITY METRICS — 4 TRỤ CỘT)

Hội đồng chấm điểm kịch bản trên thang 10 đối với 4 trụ cột (mỗi tiêu chí 25%):
1. **Novelty & Systemic Insight (25%):** Góc nhìn có phát hiện ra khoảng trống nhận thức mới không? Có bóc tách được bản chất cỗ máy vô hình hay chỉ tóm tắt lại báo chí?
2. **Dialectical Rigor & Tri-Adversarial Red Team (25%):** Có phản biện Steelman mạnh mẽ qua 3 lăng kính Thị trường / Thể chế / Dòng tiền không? Có `[THE DEVIL'S CHAPTER]` không? Đã thừa nhận các đánh đổi sòng phẳng chưa?
3. **Flow, Cadence & Oral Voice (25%):** Câu từ tự nhiên như phim tài liệu điện ảnh, 100% câu < 150 ký tự, nhịp thở TTS trên GPU mượt mà, không dính từ cấm AI.
4. **Data Anchoring Density (25%):** Số liệu định lượng và căn cứ pháp lý chính xác 100%, trích xuất trực tiếp từ Vault, không bịa đặt số liệu.

---

## 4. QUYỀN PHỦ QUYẾT & MƯỜI MỘT CỜ ĐỎ TỬ HUYỆT (VETO POWER & 11 RED FLAGS)

Kiểm toán viên trưởng (`the_critical_auditor`) kích hoạt **Quyền Phủ Quyết Ngay Lập Tức (Veto)** nếu kịch bản vi phạm bất kỳ cờ đỏ nào sau đây:
1. 🚩 Xuất hiện số liệu, thông số kỹ thuật hoặc văn bản pháp lý bịa đặt (không có trong Vault).
2. 🚩 Dùng ngụy biện bù nhìn rơm (Strawman) để hạ thấp phe phản biện.
3. 🚩 Giọng điệu thuyết giáo đạo đức, dạy đời hoặc bưng bô PR cho doanh nghiệp.
4. 🚩 Câu văn phức hợp dài lê thê (> 150 ký tự) gây nghẹt thở khi thu âm TTS.
5. 🚩 Cấu trúc liệt kê ngăn tủ "And Then" không có quan hệ nhân quả Therefore/But.
6. 🚩 Giấu điểm gãy cấu trúc xuống cuối kịch bản (Burying the Lede).
7. 🚩 Xuất hiện cụm từ AI sáo rỗng ("bức tranh toàn cảnh", "không chỉ... mà còn...").
8. 🚩 Rò rỉ nhãn khung sườn template (`[BLOCK X]`, `[HOOK]`) vào kịch bản thành phẩm.
9. 🚩 Vi phạm ranh giới `00_core/financial_boundaries.md` (khuyến nghị mua/bán, dự đoán giá, giọng "phím hàng") hoặc `00_core/brand_safety_guidelines.md`.
10. 🚩 Claim thiếu nhãn taxonomy (`verified_data` / `market_analysis` / `opinion_commentary`) hoặc thiếu dòng lưu ý nội dung bắt buộc.
11. 🚩 Kết lửng lơ, nhãn phán xét thay cho dữ kiện, hoặc phán xét động cơ/đạo đức/nhân cách (`00_core/stance_and_judgment.md` §10).

---

## 5. QUY CHUẨN BÁO CÁO KIỂM DUYỆT (`10_compliance_report.md`)

Báo cáo compliance bắt buộc phải tuân theo cấu trúc sau:

```markdown
# Editorial & Compliance Report — [Slug]

## 1. Điểm số chất lượng (Quality Scores — Thang điểm 10)
* **Novelty & Systemic Insight (25%):** X/10 — [Nhận xét chi tiết]
* **Dialectical Rigor & Tri-Adversarial (25%):** X/10 — [Nhận xét Steelman, 3 lăng kính, [THE DEVIL'S CHAPTER], trade-offs]
* **Flow & Oral Rhythm (25%):** X/10 — [Nhận xét câu < 150 ký tự, nhịp thở TTS, cấm AI-isms]
* **Anchoring Density (25%):** X/10 — [Nhận xét số liệu thực chứng, Footnote ID từ Vault]
* **Narrative Craft (K, Khóa 6, chấm mù):** K = X/20 — Cấp bài TB A.A/5 [ĐẠT/KHÔNG] · Cấp chương TB B.B/5 [ĐẠT/KHÔNG] · Chuyển về: [không / Pha 4 / Pha 7] · Chi tiết: `11_narrative_craft_scorecard.md`
* 🎯 **Tổng Điểm Đánh Giá:** Y.Y/10 — [ĐẠT / KHÔNG ĐẠT (Ngưỡng đạt: ≥ 8.5/10, không có điểm thành phần nào < 7.5, VÀ K đạt mốc ĐẠT của `00_core/narrative_craft_rubric.md`)]

## 2. Sát Hạch Hội Đồng Phản Biện Đa Diện (Tri-Adversarial Red Team Stress-Test)
* **Lăng kính 1 (The Market Skeptic):** [Đạt / Cần sửa — Chi tiết]
* **Lăng kính 2 (The Institutional Realist):** [Đạt / Cần sửa — Chi tiết]
* **Lăng kính 3 (The Forensic Cash Auditor):** [Đạt / Cần sửa — Chi tiết]
* **Kiểm toán [THE DEVIL'S CHAPTER]:** [Xác nhận có chương độc lập tại cao trào Hồi 2]
* **Steelmanning & Admitted Trade-Offs:** [Xác nhận không dùng Strawman, đã thừa nhận đánh đổi]
* 🏁 **Kết Luận Cổng Đa Chiều:** PASS / FAIL

## 3. Rà Soát Mười Một Cờ Đỏ Tử Huyệt (The 11 Red Flags Audit)
| # | Cờ Đỏ | Phát Hiện Vi Phạm | Trạng Thái |
|---|---|---|---|
| 1 | Số liệu / pháp lý bịa đặt | Không | ✅ PASS |
| 2 | Ngụy biện bù nhìn rơm (Strawman) | Không | ✅ PASS |
| 3 | Thuyết giáo đạo đức / PR bưng bô | Không | ✅ PASS |
| 4 | Câu văn > 150 ký tự | Không | ✅ PASS |
| 5 | Cấu trúc ngăn tủ "And Then" | Không | ✅ PASS |
| 6 | Giấu bài ở chương kết | Không | ✅ PASS |
| 7 | Cụm từ AI sáo rỗng | Không | ✅ PASS |
| 8 | Rò rỉ nhãn template `[BLOCK X]` | Không | ✅ PASS |
| 9 | Ranh giới tài chính / an toàn thương hiệu | Không | ✅ PASS |
| 10 | Taxonomy claim & dòng lưu ý nội dung | Không | ✅ PASS |
| 11 | Lập trường (chế độ kết, nhãn phán xét, động cơ) | Không | ✅ PASS |

**Câu bị soi ra theo `00_core/anti_ai_isms.md` §3b:**
| Chương | Câu (trích) | Dấu hiệu | Đọc: Giữ hay Sửa | Lý do | Câu sửa (nếu sửa) |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## 4. Nhật ký Sửa Đổi Trực Tiếp (Direct Revision Log)
| Chương | Câu gốc | Câu sửa đổi | Lý do | Chuyên gia đề xuất |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 5. Phán Quyết Chung Cuộc (Final Verdict)
- **Quyết định:** [PHÊ DUYỆT (PASS) / PHỦ QUYẾT (VETO - YÊU CẦU SỬA)]
- **Chữ ký thẩm định:** The Critical Auditor (Chủ Tịch Hội Đồng)
```
