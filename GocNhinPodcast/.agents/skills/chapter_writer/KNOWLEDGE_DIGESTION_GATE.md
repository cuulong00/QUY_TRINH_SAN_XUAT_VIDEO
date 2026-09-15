# ⛔ KNOWLEDGE DIGESTION GATE — Pha Tiêu Hóa Kiến Thức (GATE MỚI — CHỐNG ĐỨT GÃY)

> **NGUYÊN NHÂN GỐC RỄ CỦA LỖI:** Pipeline hiện tại có Gate 2B yêu cầu "đọc toàn bộ tài liệu nguồn", nhưng KHÔNG có bước BẮT BUỘC agent phải CHỨNG MINH đã hiểu. Kết quả: agent đọc → thu thập số liệu → viết ngay. Thiếu bước: đọc → ĐẶT CÂU HỎI PHẢN BIỆN → XÂY MÔ HÌNH TƯ DUY → rồi mới viết.
>
> **Gate này giải quyết chính xác vấn đề đó.**

---

## VỊ TRÍ TRONG PIPELINE

```
Gate 2B (Đọc Source Materials) 
    ↓
⭐ KNOWLEDGE DIGESTION GATE (GATE MỚI — file này)
    ↓
Gate 3 (Continuity Check)
    ↓
Gate 4 (Emotional Arc)
    ↓
Viết
```

Gate này nằm GIỮA việc đọc tài liệu (Gate 2B) và việc kiểm tra mạch logic (Gate 3).

---

## CÁCH THỰC THI

Sau khi đọc TOÀN BỘ tài liệu nghiên cứu gốc ở Gate 2B, agent PHẢI hoàn thành **4 bài kiểm tra** dưới đây TRƯỚC KHI tiếp tục. Kết quả phải được GHI RA (không được chỉ "nghĩ trong đầu").

---

### BÀI 1: "Tôi hiểu gì?" — Knowledge Model Statement (≤ 200 từ)

Agent phải viết ra một đoạn văn NGẮN (≤ 200 từ) tóm tắt:

1. **Bản chất vấn đề** (KHÔNG phải liệt kê số liệu, mà là cơ chế vận hành)
2. **Các bên liên quan** và vai trò thực sự của từng bên
3. **Điều mà nhận thức phổ biến SAI** về vấn đề này
4. **Lý do sâu xa** (WHY behind the WHY)

> **Ví dụ SAI (data dump):** "GDP 2025 đạt 8%, FDI 27,6 tỷ, xuất khẩu 900 tỷ."
> **Ví dụ ĐÚNG (knowledge model):** "VN đang thực hiện Đổi mới 2.0 — lần đầu tiên thiết kế kinh tế bằng tư duy kiến trúc thay vì ứng biến. DNNN không phải gánh nặng mà là công cụ chiến lược cho lĩnh vực tư nhân không làm được. Nhận thức phổ biến sai: tưởng nhà nước nghèo nên cần tư nhân thay thế. Thực tế: tư nhân là ĐỘNG LỰC CHÍNH theo thiết kế, không phải người thay thế bất đắc dĩ."

**Nếu agent không viết được đoạn này → CHỨNG TỎ chưa hiểu. DỪNG LẠI, đọc lại tài liệu.**

---

### BÀI 2: "Tôi sẽ sai ở đâu?" — 5 Câu Hỏi Phản Biện Bắt Buộc

Agent phải tự đặt VÀ tự trả lời 5 câu hỏi theo format:

| # | Câu hỏi phản biện | Câu trả lời (từ tài liệu, có source) |
|---|---|---|
| 1 | Nhận định nào trong tài liệu có thể KHÔNG ĐÚNG hoặc bị phóng đại? | (trả lời + source) |
| 2 | Số liệu nào trong tài liệu CẦN KIỂM CHỨNG thêm? | (trả lời + source hoặc [CẦN VERIFY]) |
| 3 | Bối cảnh nào mà tài liệu KHÔNG NÓI ĐẾN nhưng ảnh hưởng đến kết luận? | (trả lời) |
| 4 | **[Bẫy Nhị Nguyên]** Tôi có đang "chọn phe" thay vì phân tích sự đánh đổi (Trade-off) không? | (trả lời: Xác định rõ doanh nghiệp/quốc gia phải hy sinh gì) |
| 5 | **[Hindsight Bias]** Nếu phân tích quá khứ, tôi có đang lấy kết quả hiện tại để phán xét quyết định lúc đó không? | (trả lời: Nêu bối cảnh thông tin tại thời điểm ra quyết định) |

> **Tại sao phải làm bài này:** Đọc tài liệu mà không đặt câu hỏi phản biện = chỉ copy-paste. Agent phải chứng minh đã TƯ DUY PHẢN BIỆN với chính dữ liệu mình vừa nạp. Đặc biệt phải tránh tuyệt đối Bẫy Nhị Nguyên và Tư duy Vuốt đuôi.

---

### BÀI 3: "Tôi không được viết gì?" — Bảng Cấm Cụ Thể

Agent phải liệt kê TỐI THIỂU 3 câu/framing mà agent DỄ VIẾT SAI dựa trên bối cảnh episode:

| # | Câu/Framing SAI (dễ mắc) | TẠI SAO SAI (bản chất) | Cách viết ĐÚNG |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

> **Lưu ý:** Bảng này phải được điền DỰA TRÊN bối cảnh episode ĐANG VIẾT, không copy ví dụ từ episode khác.

---

### BÀI 4: "Chuyên gia sẽ nói gì?" — Expert Lens Test

Agent phải trả lời:

> "Nếu một chuyên gia kinh tế VN (ví dụ: TS. Nguyễn Đức Kiên, TS. Trần Đình Thiên, hoặc PGS. Phạm Thế Anh) đọc chapter tôi sắp viết, họ sẽ phản bác điểm nào?"

Liệt kê tối thiểu 2 điểm có thể bị phản bác + cách xử lý:

| # | Điểm có thể bị phản bác | Cách xử lý trong kịch bản |
|---|---|---|
| 1 | | |
| 2 | | |

---

## QUY TẮC THỰC THI

1. **PHẢI hoàn thành cả 4 bài** trước khi viết. Không có ngoại lệ.
2. **PHẢI ghi ra kết quả** — không được "nghĩ trong đầu". Ghi vào response hoặc vào file scratch.
3. **Nếu Bài 1 viết không được** → chưa hiểu, đọc lại tài liệu.
4. **Nếu Bài 2 không đặt được câu hỏi phản biện** → đang tin 100% không phản biện = nguy hiểm.
5. **Nếu Bài 3 không liệt kê được cái sai** → không biết giới hạn = sẽ viết sai.
6. **Nếu Bài 4 không tìm được điểm phản bác** → thiếu chiều sâu.

---

## KẾT NỐI VỚI CÁC GATE KHÁC

- Gate này BỔ SUNG cho Gate 2B, KHÔNG thay thế.
- Gate 2B = đọc. Gate này = chứng minh đã hiểu.
- Sau Gate này → tiếp tục Gate 3 (Continuity) → Gate 4 (Emotional Arc) → Gate 5 → Gate 6 → Viết.

---

## LỊCH SỬ VÁ LỖI

| Ngày | Vấn đề | Giải pháp |
|---|---|---|
| 2026-05-10 | Agent đọc tài liệu → viết ngay → viết sai bản chất kinh tế VN. Tài liệu research bị lãng phí. | Tạo Knowledge Digestion Gate: buộc agent CHỨNG MINH đã hiểu trước khi viết. |
