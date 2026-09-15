# ⛔ PRE-FLIGHT VERIFICATION GATE & CLAIM-TO-SOURCE LEDGER

> 🛑 **NGUYÊN TẮC VẬN HÀNH BẮT BUỘC (ZUI PROTOCOL):**
> 1. **Triệt tiêu Kiểm toán Ngầm Hình thức:** Nghiêm cấm hoàn toàn hành vi "tự kiểm tra trong đầu rồi tick xanh `✅ ĐẠT`". LLM không được tự cấp phép cho mình mà phải phơi bày chứng cứ kiểm toán minh bạch ra trước mắt người dùng.
> 2. **Giao thức 2 Bước Bắt buộc TRƯỚC KHI tạo tệp `chapter_XX.md`:**
>    - **Bước 1:** In hộp Pre-Flight Log chuẩn hóa ra màn hình chat.
>    - **Bước 2:** In **Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger)** ra màn hình chat. Chỉ khi bảng này hợp lệ 100% (không có suy diễn vô căn cứ, không có số liệu bịa đặt), Agent mới được phép gọi tool tạo tệp kịch bản.

---

## BƯỚC 1: HỘP PRE-FLIGHT LOG CHUẨN HÓA

```markdown
> 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG VIẾT chapter_XX.md]**
> - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** [Persona được chỉ định trong 08_chapter_briefs.md] + The Narrative Director (Khóa Khẩu Ngữ Oral Voice)
> - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/write_chapter` (`chapter_writer/SKILL.md`)
> - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
>   * `vault/00_Global_Vision_Synthesis.md` (Tầm nhìn tổng thể & Mỏ neo số liệu)
>   * `episodes/[slug]/08_chapter_briefs.md` (Brief chi tiết của Chương XX)
>   * `episodes/[slug]/09_narrative_state_tracker.md` (Vòng lặp nhận thức, Hạt giống chuyển tiếp)
>   * `episodes/[slug]/chapter_01.md` đến `chapter_XX-1.md` (Toàn bộ kịch bản thoại sạch các chương trước để giữ nhịp, chống lặp)
> - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/chapter_XX.md` (Văn bản thoại sạch 100%, câu < 150 ký tự, không nhúng log vận hành)
> - 🛡️ **Rào Cản Kiểm Toán First-Principles:** Giao thức ZUI (Zero-Ungrounded-Inference) — Bảng đối soát chứng cứ công khai.
```

---

## BƯỚC 2: BẢNG ĐỐI SOÁT CHỨNG CỨ CÔNG KHAI (CLAIM-TO-SOURCE VERIFICATION LEDGER)

Trước khi viết bất kỳ đoạn thoại nào, Agent phải lập bảng phân tích toàn bộ các luận điểm (Claims) dự kiến viết:

```markdown
### 📋 BẢNG ĐỐI SOÁT CHỨNG CỨ CÔNG KHAI (CLAIM-TO-SOURCE VERIFICATION LEDGER) — CHƯƠNG XX

| Đoạn Dự Kiến | Luận Điểm Cốt Lõi (Core Claim) | Phân Loại (FACT / GROUNDED_INFERENCE) | Mã Footnote & Nguồn Vault | Trích Dẫn Gốc (≤ 15 từ) Hoặc Công Thức Logic | Kiểm Toán ZUI (Xác Nhận Không Bịa Đặt) |
|---|---|---|---|---|---|
| Đoạn 1 | [Luận điểm 1] | FACT | `[Footnote X]` - `[Tên file vault]` | `"..."` | ✅ Khớp 100% số liệu gốc |
| Đoạn 2 | [Luận điểm 2] | GROUNDED_INFERENCE | Fact + Quy luật chi phí | Tiền đề: Footnote Y + Công thức Khấu hao T/V | ✅ Logic nhân quả vững chắc, không PR |
| Đoạn 3 | [Luận điểm 3] | FACT | `[Footnote Z]` - `[Tên file vault]` | `"..."` | ✅ Đúng tên riêng & thông số |
| ... | ... | ... | ... | ... | ... |
```

### 3 CẤP ĐỘ PHÂN LOẠI BẮT BUỘC (ZUI TAXONOMY):
1. **CẤP ĐỘ 1 — FACT (Sự thật thực chứng):** 
   - 100% số liệu, tên tập đoàn, mốc thời gian, quyết định chính sách phải có Footnote ID và trích dẫn ngắn (≤ 15 từ) từ `research_vault/`.
   - Tuyệt đối CẤM đoán mò các chi phí chưa công bố. Nếu nguồn không nêu rõ số tiền $\rightarrow$ bắt buộc phân tích bản chất định tính.
2. **CẤP ĐỘ 2 — GROUNDED INFERENCE (Suy diễn có căn cứ — Được phép & Khuyến khích):**
   - Mọi phân tích sâu bắt buộc phải đi theo cấu trúc:
     $$\text{Tiền đề Thực chứng (Fact)} + \text{Quy luật Khách quan (First Principles / Công thức)} \Longrightarrow \text{Suy diễn Có căn cứ}$$
   - Bắt buộc giải thích được cơ chế kinh tế/vật lý rõ ràng (như bài toán điểm hòa vốn, chi phí biến đổi vs cố định, rào cản thuế quan).
3. **CẤP ĐỘ 3 — FORBIDDEN SPECULATION (Suy diễn vô căn cứ — CẤM TUYỆT ĐỐI):**
   - Cấm bịa đặt thông số máy móc (như máy ép 2.500T), tự phỏng đoán biên lợi nhuận hay động cơ nội bộ mà không có BCTC.
   - Cấm dùng ngôn từ cảm tính giật gân hoặc ca ngợi PR ("quyết định dũng cảm", "thảm họa cận kề").
   - Bất kỳ luận điểm nào thuộc Cấp độ 3 đều bị cấm đưa vào kịch bản!

---

## CÁC TIÊU CHUẨN KỸ THUẬT VĂN BẢN THOẠI (OUTPUT DELIVERABLE)

Sau khi Bảng Đối Soát trên được thiết lập, Agent tiến hành xuất kịch bản sạch vào tệp `episodes/[slug]/chapter_XX.md` thỏa mãn 100% các tiêu chuẩn:
1. **Văn bản sạch 100%:** Không nhúng log, không nhúng bảng biểu, không chèn ghi chú hình ảnh (Visual cues).
2. **Kỷ luật Tai nghe (Ear Constraints):** 100% câu thoại dưới 150 ký tự (khoảng 20-25 từ), cú pháp trọn vẹn chủ - vị, không dấu gạch ngang dài (`—`), không từ cấm AI (`anti_ai_isms.md`).
3. **Phân đoạn văn bản (Paragraph Pacing):** Gom từ 2 đến 4 câu ngắn thành một đoạn văn hoàn chỉnh. Tuyệt đối CẤM ngắt dòng sau mỗi câu đơn độc làm nát vụn văn bản.
4. **Văn phong Bên Tách Trà:** Điềm tĩnh, khách quan, tri thức, tự sự điện ảnh (Cinematic Editorial Noir).
