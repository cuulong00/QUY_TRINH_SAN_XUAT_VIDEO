# Retention Gate Checklist — Cổng Chặn Tự Động

> 🧭 **Phân vai cổng chấm (29/09/2026):** Mỗi khâu chỉ có MỘT cổng PASS/FAIL — Dàn ý: `00_core/retention_gate_checklist.md` (Gate 1 / Gate D1) · Từng chương: `00_core/chapter_quality_standard.md` · Cả kịch bản (Pha 10–11): `.agents/skills/compliance_council/SKILL.md` (ngưỡng ≥ 8.5/10, không trụ cột nào < 7.5).
> File này là **cổng chính thức cấp dàn ý** (Gate 1 / Gate D1) và cổng Ch.2 (Gate 2). Người chấm khác agent viết; chạy `scripts/kiem_pha.py --pha 4` trước và đính đầu ra (Q11).

> File này là CỔNG CHẶN bắt buộc trong pipeline sản xuất.
> Được chạy 2 lần: sau Outline (Gate 1) và sau viết Ch.2 (Gate 2).
> Nếu KHÔNG ĐẠT → PHẢI sửa trước khi tiếp tục.

---

## GATE 1: Sau Outline (trước khi tạo Chapter Briefs)

Outline được đánh giá bằng bảng câu hỏi đọc duyệt sau (tham chiếu Phiếu A `00_core/narrative_craft_rubric.md`):

- [ ] **1.** Ch.1 kết bằng câu hỏi HỞ liên quan quyền lợi/mối quan tâm trực tiếp của khán giả (Loại A: túi tiền/sinh kế; Loại B: bài toán quản trị/quy luật sinh tồn ngành; Loại C: nghịch lý tri thức/mâu thuẫn dữ liệu)? (Không tự đóng loop)
- [ ] **2.** Ch.2 = Stakes & Relevance Anchor ("Điều này liên quan đến bạn/thị trường/cuộc chơi ra sao?" — Loại A: Personal Stakes túi tiền; Loại B: bài toán doanh nghiệp/quốc gia (cơ chế vận hành, cạnh tranh, thể chế, chuỗi giá trị); Loại C: Mâu thuẫn cấu trúc vĩ mô — KHÔNG biến thành bài giảng lý thuyết giáo điều)
- [ ] **3.** Open Loop ở Hook liên quan trực tiếp đến stakes cốt lõi của đề tài (Loại A: túi tiền/việc làm; Loại B: bài toán kinh doanh/thách thức chiến lược; Loại C: nghịch lý lịch sử/địa chính trị)?
- [ ] **4.** Có Re-hook hoặc cú mở vấn đề mới tại mốc chuyển nhịp (tham chiếu nhịp ~3:30 hoặc cuối Hồi 1) giữ chân khán giả?
- [ ] **5.** Có manh mối, dữ kiện hoặc nghịch lý MỚI tại khúc chuyển giao sang Hồi 2 (tham chiếu nhịp ~7:00)?
- [ ] **6.** Tổng case study quốc tế đạt trần Q1 (Loại A/B tối đa 2 case, Loại C tối đa 3 case, mỗi case ≤ 3 phút; quyết định nội dung của user ngày 02/10/2026)? Mỗi case gắn chặt vào việc làm sáng tỏ luận điểm và có nguồn trong vault (theo `content_principles.md` §5).
- [ ] **7.** Phân cấp độ dài bám sát 4 Cấp độ Thời lượng (Cấp 1: 8–15m; Cấp 2: 16–25m; Cấp 3: 26–35m; Cấp 4: 36–45+m, theo `.agents/rules/content-os-pipeline.md`; mặc định Cấp 1–2 theo `.agents/AGENTS.md`), bố trí Re-hook & manh mối/dữ kiện mới tại các khúc chuyển màn để duy trì nhịp chú ý?
- [ ] **8.** Không có đoạn kéo dài (tham chiếu > 3 phút) chỉ phân tích/framework khô khan mà không có mỏ neo thực tế (stakes / data / drama)?
- [ ] **9.** Mỗi chương có bridge tạo chuyển động (logical data flow / narrative bridge)?
- [ ] **10.** Outro kết đúng chế độ đã chọn (`00_core/stance_and_judgment.md` §1)? Chế độ A nói thẳng lập trường kèm điều kiện có thể sai; chế độ B trao các cách đọc cạnh tranh, biến số quyết định rồi đặt câu hỏi mở nhắm đúng biến số đó. Câu hỏi mở là một phần lập luận, không phải lời xin bình luận (CTA duy nhất nằm cuối Chương 2).

### Điều kiện PASS:
- Vượt qua kiểm định chất lượng theo Phiếu A (`00_core/narrative_craft_rubric.md`) do người khác ngoài người dựng dàn ý chấm, thỏa mãn các câu hỏi trên → PASS → Tiếp tục tạo Chapter Briefs
- Chưa thỏa mãn các câu hỏi cốt lõi hoặc dưới ngưỡng chất lượng Phiếu A → FAIL → Sửa outline và chạy lại Gate 1

### Tiêu chí KHÔNG ĐƯỢC vi phạm (Hard-fail):
- Tiêu chí #1 (Anti-Completion) — Nếu fail → outline bị reject ngay
- Tiêu chí #2 (Ch.2 = Stakes & Relevance Anchor) — Nếu fail → outline bị reject ngay
- Tiêu chí #6 (Trần case study Q1) - Nếu quá số case hoặc mỗi case > 3 phút → phải cắt bớt trước khi tiếp

---

## GATE 2: Sau viết Ch.2 (trước khi viết Ch.3)

Ch.2 đã viết PHẢI đạt **TẤT CẢ 5/5** tiêu chí sau:

- [ ] **1.** Có mỏ neo lợi ích/sự liên quan trực tiếp:
  - *Loại A (Đời sống/Chính sách dân sinh):* Có liên hệ rõ tới đời sống chung (thu nhập, việc làm, chi phí, khoản vay) bằng lăng kính phổ quát ("chúng ta", "người lao động"); không ép số câu "của bạn", không bịa nhân vật cá nhân.
  - *Loại B (Doanh nghiệp/Kinh tế ngành):* Có phân tích rõ bài toán cơ chế của doanh nghiệp/quốc gia (cạnh tranh, thể chế, chuỗi giá trị, đánh đổi chiến lược); chi phí, dòng tiền chỉ khi đề tài là tài chính (WO-00 Q10).
  - *Loại C (Tài liệu/Địa chính trị/Lịch sử):* Có mâu thuẫn dữ liệu hoặc liên hệ trực tiếp đến vị thế kinh tế - xã hội của Việt Nam.
- [ ] **2.** Có ít nhất 1 Zoom In (ví dụ cụ thể, tình huống thực tế hoặc dữ liệu bóc tách vi mô)?
- [ ] **3.** KHÔNG sa đà vào liệt kê case study quốc tế xa lạ rời rạc?
- [ ] **4.** KHÔNG có bài giảng lý thuyết/framework thuần túy giáo điều (Developmental State, Meritocratic Bureaucracy...) mà thiếu mỏ neo dữ liệu thực tiễn?
- [ ] **5.** Người xem sau khi nghe Ch.2 có CẢM THẤY BỊ CUỐN VÀO CUỘC CHƠI (thấy quyền lợi của mình, bài toán kinh doanh của mình, hoặc sự tò mò bức thiết) không?

### Điều kiện PASS:
- 5/5 → PASS → Tiếp tục viết Ch.3
- < 5/5 → FAIL → Sửa Ch.2 và chạy lại Gate 2

---

## BẰNG CHỨNG VÌ SAO GATE NÀY CẦN THIẾT

| Video | Drop-off | Nguyên nhân |
|-------|----------|-------------|
| `nhat-the-hoa-quyen-luc` (25 phút) | ~phút 5 | Ch.2 = "63 tỉnh thành, chi phí giao dịch" (bài giảng hành chính) |
| `to-lam-tap-can-binh` (16:19, CTR 7.5%) | 5:22 | Ch.2 = "TQ GDP 5%, CPI 0%, PPI -2.6%" (bài giảng kinh tế TQ) |

**Cả 2 video đều chết ở phút 5 vì Chapter 2 "phản bội" lời hứa Stakes & Relevance Anchor của Chapter 1.**

Gate này đảm bảo điều đó KHÔNG BAO GIỜ xảy ra nữa.

---

## GATE D: Nhánh Documentary (Loại C — Chỉ dùng khi brief xác nhận Loại C)

> ⚠️ **Khi nào dùng Gate D thay Gate 1+2?**
> Khi `03_brief.md` xác định rõ đây là video Loại C (documentary toàn cầu / so sánh quốc gia / phân tích xu hướng dài hạn) VÀ persona chính là Persona 5 (tò mò trí tuệ).
> Gate D KHÔNG áp dụng cho Loại A hoặc Loại B. Nếu nghi ngờ, dùng Gate 1+2 tiêu chuẩn.

### Gate D1: Sau Outline (trước Chapter Briefs)

Outline được đánh giá bằng bảng câu hỏi đọc duyệt sau (tham chiếu Phiếu A `00_core/narrative_craft_rubric.md`):

- [ ] **1.** Ch.1 kết bằng câu hỏi HỞ (nghịch lý trí tuệ hoặc mâu thuẫn dữ liệu — KHÔNG bắt buộc túi tiền)
- [ ] **2.** Ch.2 = Relevance Anchor? (Tại sao điều này QUAN TRỌNG với khán giả — có thể là financial, intellectual, hoặc cultural stakes)
- [ ] **3.** Có manh mối, so sánh hoặc nghịch lý MỚI tại mốc chuyển nhịp đầu tiên (tham chiếu nhịp ~3:30)?
- [ ] **4.** Có manh mối hoặc dữ kiện bất ngờ MỚI tại mốc chuyển giao sang Hồi 2 (tham chiếu nhịp ~7:00)?
- [ ] **5.** Phân cấp độ dài bám sát 4 Cấp độ Thời lượng (Cấp 1: 8–15m; Cấp 2: 16–25m; Cấp 3: 26–35m; Cấp 4: 36–45+m), bố trí Re-hook & manh mối mới tại các khúc chuyển màn để bảo vệ mạch chú ý?
- [ ] **6.** Không có đoạn kéo dài (tham chiếu > 4 phút) chỉ phân tích mà không có manh mối mới, comparison, hoặc case study?
- [ ] **7.** Mỗi chương có mạch vận động kịch tính và logic nhân quả rõ ràng (But/Therefore) thay vì liệt kê phẳng?
- [ ] **8.** Outro kết đúng chế độ đã chọn (`00_core/stance_and_judgment.md` §1)? Chế độ A nói thẳng lập trường kèm điều kiện có thể sai; chế độ B trao các cách đọc cạnh tranh, biến số quyết định rồi đặt câu hỏi mở nhắm đúng biến số đó. Câu hỏi mở là một phần lập luận, không phải lời xin bình luận (CTA duy nhất nằm cuối Chương 2).
- [ ] **9.** Có ít nhất 1 điểm nối về VN / đời sống VN (nếu chủ đề là quốc tế)?

### Điều kiện PASS:
- Vượt qua kiểm định chất lượng theo Phiếu A (`00_core/narrative_craft_rubric.md`), thỏa mãn các câu hỏi trên → PASS → Tiếp tục tạo Chapter Briefs
- Chưa thỏa mãn các câu hỏi cốt lõi hoặc dưới ngưỡng chất lượng Phiếu A → FAIL → Sửa outline

### Tiêu chí KHÔNG ĐƯỢC vi phạm (Hard-fail):
- Tiêu chí #1 (Anti-Completion) — Hook phải mở loop
- Tiêu chí #6 (Tránh phân tích thuần kéo dài) — Phải có manh mối/comparison đối chứng

### Gate D2: Sau Ch.2 (trước Ch.3)

Ch.2 PHẢI đạt **TẤT CẢ 4/4**:

- [ ] **1.** Có ít nhất 1 data point hoặc comparison khiến khán giả nghĩ "mình chưa biết điều này"?
- [ ] **2.** Có ít nhất 1 câu nối về VN hoặc đời sống người Việt (nếu chủ đề quốc tế)?
- [ ] **3.** KHÔNG phải bài giảng thuần túy — phải có góc nhìn riêng, nhận định, hoặc narrative?
- [ ] **4.** Sau khi nghe Ch.2, khán giả có MUỐN nghe tiếp không? Có gì chưa được giải đáp?

### Điều kiện PASS:
- 4/4 → PASS → Viết Ch.3
- < 4/4 → FAIL → Sửa Ch.2

