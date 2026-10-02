---
name: compliance-council
description: "Editorial & Compliance Council. Reviews script safety, legal compliance, oral rhythm, Tri-Adversarial Red Team rigor, and Popperian falsification."
---

# Editorial & Compliance Council — Hội Đồng Thẩm Tra & Phê Duyệt Kiệt Tác (Phiên Bản Tư Duy 3.0)

> 🧭 **Phân vai cổng chấm (29/09/2026):** Mỗi khâu chỉ có MỘT cổng PASS/FAIL — Dàn ý: `00_core/retention_gate_checklist.md` (Gate 1 / Gate D1) · Từng chương: `00_core/chapter_quality_standard.md` · Cả kịch bản (Pha 10–11): `.agents/skills/compliance_council/SKILL.md` (ngưỡng ≥ 8.5/10, không trụ cột nào < 7.5).
> **Cổng loại ngay hợp nhất (áp tại đây):** 10 Hard-Fail của `00_core/quality_rubric.md` §4 + 5 Hard-Fail Gates của `00_core/masterpiece_quality_standard.md` §4 + 5 câu kiểm lập trường của `00_core/stance_and_judgment.md` §10. Điều kiện trùng nhau giữa các nguồn chỉ tính một lần. Vi phạm bất kỳ điều nào → KHÔNG ĐẠT, dù tổng điểm cao.

> 🎯 **Kiểm lập trường (bắt buộc):** Chấm theo 5 câu hỏi ở `00_core/stance_and_judgment.md` §10 trong trụ cột biện chứng/biên tập. Chế độ A hay B đều hợp lệ; kết lửng lơ mới là lỗi. Nhãn phán xét thay cho dữ kiện, phán xét động cơ hay đạo đức, hoặc lặp "chúng tôi cho rằng" quá 4 lần đều là lỗi phải sửa trước khi đạt ngưỡng.

> 🛑 **EXPERT PERSONAS (BẮT BUỘC HÓA THÂN)**
> Kỹ năng này kích hoạt Hội đồng Thẩm tra Tối cao gồm:
> 1. `the_critical_auditor` (Chủ Tịch Hội Đồng — Giám đốc Thẩm tra Pháp lý, Kỹ thuật & Tài chính Forensic, nắm Veto Power)
> 1b. `the_data_auditor` (Kiểm toán số liệu — số này đo cái gì, phương pháp đo có khớp với kết luận không, diễn giải có vượt phạm vi không; claim `⛔ UNVERIFIED` bị loại) · ví dụ yếu/mạnh: `.agents/examples/editorial_qa_examples.md`
> 2. `the_editorial_strategist` (Tổng Biên Tập Chiến Lược — Kiểm toán Sợi chỉ đỏ, Therefore/But, Chống giấu bài ở chương kết)
> 3. `the_policy_analyst` (Chuyên Gia Thể Chế — Kiểm toán tính chuẩn xác của văn bản luật, số hiệu Nghị định, Thông tư)
> 4. `the_compliance_editor` (Biên Tập Tuân Thủ — Kiểm toán ranh giới Bình luận vs. Tư vấn Đầu tư theo `00_core/financial_boundaries.md`, taxonomy `verified_data`/`market_analysis`/`opinion_commentary`)
> 5. `the_voice_architect` & `the_quality_czar` (Giám sát Kỷ luật Tai nghe & An toàn TTS)
>
> Nếu chưa nạp đủ các chuyên gia này trong phiên làm việc, NGHIÊM CẤM tạo báo cáo compliance.

---

## 1. NĂM KHÓA KIỂM TOÁN TỐI THƯỢNG (THE 5 IMPERATIVE AUDIT GATES)

Trước khi ký duyệt bất kỳ kịch bản nào, Hội đồng thẩm tra kịch bản qua 5 khóa sinh tử:

### Khóa 1: Zero-Ungrounded-Inference (ZUI — Khóa Chân Lý Thực Chứng)
- **Level 1 (Fact):** 100% số liệu, tên tập đoàn, số hiệu Nghị định, Thông tư, ngày tháng phải có Footnote ID và trích dẫn gốc trong `research_vault/`. Tuyệt đối CẤM đoán mò các chi phí chưa công bố.
- **Level 2 (Grounded Inference):** Suy diễn sâu bắt buộc phải đi theo công thức:
  $$\text{Tiền đề Thực chứng (Fact)} + \text{Quy luật Khách quan (First Principles)} \Longrightarrow \text{Suy diễn Có căn cứ}$$
- **Level 3 (Speculation):** Tự bịa số liệu kỹ thuật, tự phỏng đoán động cơ cá nhân $\rightarrow$ **ĐÁNH TRƯỢT TỨC THÌ (FAIL)**.

### Khóa 2: Steelmanning, Trade-Offs & Symmetric Parity (Khóa Đối Xứng & Sự Đánh Đổi)
- **Triệt tiêu Bù Nhìn Rơm (Anti-Strawman):** Lập luận của phe phản biện phải được xây dựng ở phiên bản mạnh nhất, sắc bén nhất, có số liệu đối kháng thuyết phục nhất.
- **Hội đồng Phản biện Đa diện:** tra vấn kịch bản qua các lăng kính **đã chọn trong hiến chương tập** (tối thiểu 2); kiểm thêm: lăng kính dòng tiền có bị bật cho đề tài không phải tài chính không. danh mục lăng kính và điều kiện bật lăng kính dòng tiền: `.agents/AGENTS.md` mục "Thể Chế Hóa Hội Đồng Phản Biện Đa Diện" (bản gốc duy nhất, WO-00 Q10).
- **Bàn Cân Đối Xứng 1-1 (Symmetric Parity):** Khi đề tài so sánh hoặc đối kháng đa thực thể, kiểm toán viên bắt buộc đối soát để bảo đảm độ sâu dữ kiện, cơ chế và tử huyệt của cả hai bên đều được mổ xẻ ngang nhau (BCTC, cơ cấu nợ chỉ khi đề tài là tài chính). Cấm tình trạng một bên là nhân vật chính đa chiều, bên kia là bù nhìn hời hợt.
- **Khóa Cứng `[THE DEVIL'S CHAPTER]`:** Bắt buộc có 1 chương phản đề độc lập tại cao trào Hồi 2 (50–70% thời lượng).
- **Thừa Nhận Đánh Đổi (`admitted_trade_offs`):** Mọi giải pháp đều phải chỉ rõ cái giá phải trả và chi phí cơ hội; cấm tô hồng giải pháp thần thánh.

### Khóa 3: Single Narrative Spine & Kinetic Pacing (Khóa Sợi Chỉ Đỏ & Động Lực Học Tự Sự)
- 100% các chương phải phục vụ Biến cố trung tâm phát nổ ở đầu video.
- 0% cấu trúc "And Then" (kể chuyện ngăn tủ) hoặc niên biểu hành chính chán ngắt ("Năm 2015... Ba năm sau..."). 
- Mọi chuyển đoạn phải có động lực nhân quả "Vì vậy..." [THEREFORE] hoặc "Nhưng..." [BUT]. Phân cảnh phải bắt đầu bằng năng lượng động của áp lực hoặc nghịch lý.

### Khóa 4: Anti-Burying-The-Lede & Organic Integrity (Khóa Cao Trào & Tính Toàn Vẹn Hữu Cơ)
- Điểm gãy cấu trúc lớn nhất bắt buộc phải nổ ra ở cao trào Màn 2 (`[THE DEVIL'S CHAPTER]`). Tuyệt đối cấm giấu bí mật kỹ thuật/kinh tế xuống 2 phút cuối của video.
- **Chống Vá Víu Đối Phó (Anti-Patchwork Compliance):** Khi tiếp nhận phản hồi hiệu đính, cấm chèn cơ học một câu trả bài vào đầu đoạn làm vỡ nhịp thở. Đoạn văn phải được tái cấu trúc hữu cơ như một cơ thể sống thống nhất.

### Khóa 5: Oral Voice, Authentic Gravitas & Zero-Scaffolding (Khóa Khẩu Ngữ, Điềm Đạm & Sạch Khung Sườn)
- 100% câu thoại dưới 150 ký tự, đầy đủ chủ - vị, tốc độ nói 223–235 từ/phút (`.agents/AGENTS.md`), âm sắc đàm thoại điềm tĩnh như ngồi uống trà.
- Gom 2–4 câu thành đoạn văn trôi chảy; cấm ngắt dòng sau mỗi câu đơn lẻ.
- **Khử Sạch Melodrama & Lạm Phát Tính Từ:** Tuyệt đối loại bỏ các tính từ giật gân rẻ tiền (`nghiệt ngã, rúng động, cuộc chơi, kinh hoàng, sốc`). Độ kịch tính phải đến từ sự thật trần trụi và quy luật kinh tế khách quan.
- Tuyệt đối không còn nhãn template `[BLOCK X]`, `[HOOK MÔ TẢ]` trong văn bản thành phẩm.
- **Đếm dấu hiệu cấu trúc** theo `00_core/anti_ai_isms.md` §3b trên từng chương (bảng "Đếm khi chấm"). Vượt ngưỡng ở S1, S2 hoặc có S3/S4/S6/S7 → trừ trụ cột Flow và ghi vào nhật ký sửa đổi. Khi sửa chỉ đổi cách nói, không thêm dữ kiện mới.

---

## 2. NGUYÊN LÝ THẨM TRA NÂNG CAO (ADVANCED AUDIT PRINCIPLES)

### A. Tư Duy Bậc Hai & Bậc Ba (Second-Order & Third-Order Thinking)
- Tra vấn kịch bản:
  * Sau 2–3 năm áp dụng chính sách/mô hình này, thị trường sẽ thích nghi và tìm cách né đòn như thế nào?
  * Sau 5 năm, rủi ro hệ thống sẽ tích tụ ở đâu? Ai là người cuối cùng phải trả tiền?

### B. Thước Đo Khả Năng Bác Bỏ Của Popper (Popperian Falsification Heuristic)
- Kiểm tra xem các luận đề chính có điều kiện bác bỏ rõ ràng không: *"Dữ liệu thực tế nào xuất hiện sẽ chứng minh luận điểm này sai?"*
- Nếu một luận đề được diễn giải theo kiểu "thế nào cũng đúng", trốn tránh kiểm chứng thực nghiệm $\rightarrow$ Loại bỏ.

### C. Khám Nghiệm Sự Giả Tạo & Lạm Phát Tính Từ (Inauthenticity & Adjective Inflation Detector)
- Tra vấn độ kịch tính: Kịch tính này xuất phát từ sức nén của các con số đối lập và sự va đập thể chế, hay do người viết đang cố gắng "diễn trò", gào thét bằng các tính từ melodrama?
- Tước bỏ toàn bộ tính từ cảm thán để thử thách xem luận điểm có còn đứng vững bằng sự thật hay không.

### D. Thước Đo Cân Bằng Bàn Cờ Đối Xứng (Symmetric Parity Metric)
- Soi chiếu độ dày của dữ liệu: Khi hai đối thủ hoặc hai mô hình được đem ra so sánh, số dữ kiện có nguồn, số cơ chế được bóc tách và mức độ đào sâu nguyên nhân gốc rễ của bên thứ hai có ngang bằng bên thứ nhất không? (Chỉ số tài chính chỉ là một loại dữ kiện, không bắt buộc.)

### E. Kiểm Toán Tính Liền Mạch Tiến Hóa Thời Gian (Temporal & Chronological Integrity)
- Quét các mốc thời gian: Có hiện tượng "gộp thời gian giả tạo" (ghép các sự kiện cách nhau nhiều năm thành "cùng thời điểm") để tạo kịch tính rẻ tiền không?
- Niên biểu lịch sử có bị lạm dụng như một bản báo cáo hành chính chán ngắt không?

---

## 3. CHỈ SỐ CHẤT LƯỢNG KỊCH BẢN (SCRIPT QUALITY METRICS — 4 TRỤ CỘT)

Hội đồng chấm điểm kịch bản trên thang 10 đối với 4 trụ cột (mỗi tiêu chí 25%):
1. **Novelty & Systemic Insight (25%):** Góc nhìn có phát hiện ra khoảng trống nhận thức mới không? Có bóc tách được bản chất cỗ máy vô hình hay chỉ tóm tắt lại báo chí?
2. **Dialectical Rigor & Symmetric Parity (25%):** Có phản biện Steelman mạnh mẽ qua các lăng kính đã chọn trong hiến chương tập không (tối thiểu 2)? Có `[THE DEVIL'S CHAPTER]` không? Đã thừa nhận các đánh đổi sòng phẳng chưa? Cán cân đối xứng giữa các chủ thể có đạt 1-1 không?
3. **Flow, Cadence & Authentic Gravitas (25%):** Câu từ tự nhiên như ngồi uống trà, 100% câu < 150 ký tự, nhịp thở TTS mượt mà, khử sạch melodrama giật gân và từ cấm AI.
4. **Data Anchoring Density & Temporal Integrity (25%):** Số liệu định lượng và căn cứ pháp lý chính xác 100%, trích xuất trực tiếp từ Vault, logic thời gian trung thực, không bịa đặt số liệu.

---

## 4. QUYỀN PHỦ QUYẾT & MƯỜI CỜ ĐỎ TỬ HUYỆT (VETO POWER & 10 RED FLAGS)

Kiểm toán viên trưởng (`the_critical_auditor`) kích hoạt **Quyền Phủ Quyết Ngay Lập Tức (Veto)** nếu kịch bản vi phạm bất kỳ cờ đỏ nào sau đây:
1. 🚩 Xuất hiện số liệu, thông số kỹ thuật hoặc văn bản pháp lý bịa đặt (không có trong Vault).
2. 🚩 Dùng ngụy biện bù nhìn rơm (Strawman) để hạ thấp phe phản biện.
3. 🚩 Giọng điệu thuyết giáo đạo đức, dạy đời hoặc bưng bô PR cho doanh nghiệp.
4. 🚩 Lạm phát tính từ, melodrama giật gân rẻ tiền (`nghiệt ngã, rúng động, cuộc chơi, kinh hoàng, ván cược sinh tử`).
5. 🚩 Mù lòa bất đối xứng: cán cân phân tích bị lệch, biến một bên thành đạo cụ minh họa sơ sài.
6. 🚩 Bóp méo niên biểu (gộp sự kiện cách nhau nhiều năm thành "cùng lúc") hoặc mở màn bằng niên biểu hành chính chán ngắt.
7. 🚩 Sửa đổi chắp vá đối phó (nhét câu trả bài cơ học làm vỡ tính hữu cơ của đoạn văn).
8. 🚩 Câu văn phức hợp dài lê thê (> 150 ký tự) gây nghẹt thở khi thu âm TTS.
9. 🚩 Cấu trúc liệt kê ngăn tủ "And Then" không có quan hệ nhân quả Therefore/But.
10. 🚩 Rò rỉ nhãn khung sườn template (`[BLOCK X]`, `[HOOK]`) vào kịch bản thành phẩm.
11. 🚩 Vi phạm ranh giới `00_core/financial_boundaries.md`: khuyến nghị mua/bán tài sản tài chính cụ thể, dự đoán giá, hoặc giọng điệu "phím hàng".
12. 🚩 Claim thiếu nhãn taxonomy (`verified_data` / `market_analysis` / `opinion_commentary`) hoặc thiếu dòng lưu ý nội dung bắt buộc.

---

## 5. QUY CHUẨN BÁO CÁO KIỂM DUYỆT (`10_compliance_report.md`)

Báo cáo compliance bắt buộc phải tuân theo cấu trúc sau:

```markdown
# Editorial & Compliance Report — [Slug]

## 1. Điểm số chất lượng (Quality Scores — Thang điểm 10)
* **Novelty & Systemic Insight (25%):** X/10 — [Nhận xét chi tiết]
* **Dialectical Rigor & Symmetric Parity (25%):** X/10 — [Nhận xét Steelman, các lăng kính đã chọn trong hiến chương, [THE DEVIL'S CHAPTER], trade-offs, đối xứng 1-1]
* **Flow, Cadence & Authentic Gravitas (25%):** X/10 — [Nhận xét câu < 150 ký tự, nhịp thở TTS, sạch melodrama & AI-isms]
* **Anchoring Density & Temporal Integrity (25%):** X/10 — [Nhận xét số liệu thực chứng, logic thời gian, Footnote ID từ Vault]
* 🎯 **Tổng Điểm Đánh Giá:** Y.Y/10 — [ĐẠT / KHÔNG ĐẠT (Ngưỡng đạt: ≥ 8.5/10 và không có điểm thành phần nào < 7.5)]

## 2. Sát Hạch Hội Đồng Phản Biện Đa Diện (Tri-Adversarial Red Team Stress-Test)
* **Lăng kính đã chọn (liệt kê theo hiến chương tập, tối thiểu 2):** [Tên lăng kính — Đạt / Cần sửa — Chi tiết], ...
* **Kiểm lăng kính dòng tiền:** [Có bật không; nếu bật, đề tài có phải doanh nghiệp/thị trường vốn và luận điểm có xoay quanh sức khỏe tài chính không]
* **Kiểm toán [THE DEVIL'S CHAPTER]:** [Xác nhận có chương độc lập tại cao trào Hồi 2]
* **Steelmanning & Admitted Trade-Offs:** [Xác nhận không dùng Strawman, đã thừa nhận đánh đổi]
* **Symmetric Parity Check:** [Xác nhận độ sâu phân tích 1-1 giữa các chủ thể]
* 🏁 **Kết Luận Cổng Đa Chiều:** PASS / FAIL

## 3. Rà Soát Mười Cờ Đỏ Tử Huyệt (The 10 Red Flags Audit)
| # | Cờ Đỏ | Phát Hiện Vi Phạm | Trạng Thái |
|---|---|---|---|
| 1 | Số liệu / pháp lý bịa đặt | Không | ✅ PASS |
| 2 | Ngụy biện bù nhìn rơm (Strawman) | Không | ✅ PASS |
| 3 | Thuyết giáo đạo đức / PR bưng bô | Không | ✅ PASS |
| 4 | Lạm phát tính từ / Melodrama rẻ tiền | Không | ✅ PASS |
| 5 | Mù lòa bất đối xứng (Parity Failure) | Không | ✅ PASS |
| 6 | Bóp méo niên biểu / Niên biểu hành chính | Không | ✅ PASS |
| 7 | Sửa chữa chắp vá đối phó (Patchwork) | Không | ✅ PASS |
| 8 | Câu văn > 150 ký tự | Không | ✅ PASS |
| 9 | Cấu trúc ngăn tủ "And Then" | Không | ✅ PASS |
| 10 | Rò rỉ nhãn template `[BLOCK X]` | Không | ✅ PASS |

**Đếm dấu hiệu cấu trúc (`00_core/anti_ai_isms.md` §3b):**
| Chương | S1 không phải X mà là Y (≤2) | S2 câu chốt rỗng | S3/S4/S6/S7 | Đoạn có ≥2 dấu hiệu yếu | Trạng thái |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ✅ / ❌ |

## 4. Nhật ký Sửa Đổi Trực Tiếp Hữu Cơ (Organic Revision Log)
| Chương | Đoạn gốc | Đoạn tái cấu trúc hữu cơ | Lý do nhận thức | Chuyên gia đề xuất |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 5. Phán Quyết Chung Cuộc (Final Verdict)
- **Quyết định:** [PHÊ DUYỆT (PASS) / PHỦ QUYẾT (VETO - YÊU CẦU SỬA)]
- **Chữ ký thẩm định:** The Critical Auditor (Chủ Tịch Hội Đồng)
```
