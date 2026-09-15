# Remix Differentiation Guide — Kênh GocNhinPodcast

> Hướng dẫn cách biến nội dung tài chính YouTube có sẵn thành kịch bản MỚI, SÁNG TẠO, KHÔNG TRÙNG LẶP — mang đúng giọng và giá trị riêng của kênh GocNhinPodcast.

---

## NGUYÊN TẮC CỐT LÕI

> **Remix ≠ Sao chép. Remix = Lấy dữ liệu gốc → Bổ sung case study + số liệu mới → Viết lại hoàn toàn bằng góc phân tích sắc bén.**

Transcript gốc là **nguyên liệu thô**, KHÔNG PHẢI bản nháp. AI phải:
1. Đọc hiểu nội dung và số liệu gốc
2. Tìm điểm yếu / chỗ phân tích chưa đủ sâu / số liệu lỗi thời
3. Xác định góc phân tích mới + bổ sung dữ liệu xác thực
4. Viết lại hoàn toàn bằng voice GocNhinPodcast — không giữ câu cú, không giữ cấu trúc, không giữ ví dụ

---

## BƯỚC PHÂN TÍCH TRANSCRIPT (Bắt buộc trước khi viết)

### 1. Đọc kỹ → Rút cấu trúc gốc

Sau khi đọc `00_raw_transcript.txt`, lập bảng phân tích:

```markdown
## Phân tích Transcript Gốc

### Chủ đề chính
[Chủ đề tài chính trung tâm của video gốc]

### Luận điểm chính (liệt kê 3-7 ý)
1. [Ý 1]
2. [Ý 2]
...

### Số liệu & dữ liệu được dùng
- [Số liệu nào được trích dẫn? Có nguồn không? Có cập nhật không?]

### Điểm MẠNH (giữ lại cảm hứng)
- [Ý nào phân tích sắc, có dữ liệu thuyết phục]

### Điểm YẾU / THIẾU (cơ hội sáng tạo)
- [Chỗ nào thiếu số liệu, dùng số liệu cũ]
- [Chỗ nào phân tích bề mặt, không đào sâu cơ chế]
- [Chỗ nào thiếu case study thực tế]
- [Chỗ nào thiếu Action Plan cho người xem]

### Đối tượng video gốc vs Đối tượng GocNhinPodcast
- Video gốc hướng tới: [ai? trình độ tài chính nào?]
- GocNhinPodcast hướng tới: người muốn thoát bẫy thu nhập, nhà đầu tư F0, người bị loạn thông tin

### Cấu trúc gốc
- [Tóm tắt cấu trúc: mở bài → thân → kết]
- [Video gốc dài bao nhiêu phút? Bao nhiêu ý chính?]
```

Lưu vào: `episodes/[slug]/01_source_analysis.md`

### 2. Xác định góc khai thác mới (Differentiation)

Áp dụng **ít nhất 2 trong 5 kỹ thuật** dưới đây:

---

## 5 KỸ THUẬT DIFFERENTIATION

### ① Đào sâu bằng dữ liệu (Data Depth)

> Video gốc nói CHUNG CHUNG → GocNhinPodcast bổ sung SỐ LIỆU THẬT + NGUỒN RÕ

**Cách làm:**
- Video gốc: "Lạm phát làm giảm giá trị tiền" → Quá chung
- GocNhinPodcast: "Lạm phát VN trung bình 7% trong 10 năm qua. 100 triệu đồng năm 2014, hôm nay chỉ mua được hàng trị giá 50 triệu. Nếu bạn gửi tiết kiệm lãi 5%, sau thuế 4.75% — bạn đang nghèo đi 2.25% mỗi năm mà không hề biết."
- **Nguyên tắc:** Mỗi luận điểm PHẢI kèm ít nhất 1 con số cụ thể + context rõ ràng

### ② Lật góc nhìn bằng Case Study (Counter-Case)

> Video gốc nói theo hướng A → GocNhinPodcast đưa case study phản bác hoặc bổ sung

**Cách làm:**
- Video gốc: "Đầu tư dài hạn luôn thắng" → hướng tích cực
- GocNhinPodcast: "Người Nhật mua Nikkei năm 1989 phải chờ 34 năm mới hòa vốn. Dài hạn chỉ thắng khi bạn CHỌN ĐÚNG từ đầu — còn không, dài hạn = chôn vốn dài hạn." → bắt đầu từ NGHỊCH LÝ trước, rồi mới dẫn sang framework đúng
- **Nguyên tắc:** Bắt đầu từ chỗ niềm tin sai phổ biến, rồi bóc tách bằng dữ liệu lịch sử

### ③ Thu hẹp đối tượng + Tình huống cụ thể (Niche Down)

> Video gốc nói cho TẤT CẢ → GocNhinPodcast viết cho MỘT NHÓM CỤ THỂ

**Cách làm:**
- Video gốc: "Cách quản lý tài chính cá nhân" → chung cho mọi người
- GocNhinPodcast Option A: "Dành cho dân văn phòng lương 15 củ — tiền đi đâu hết?"
- GocNhinPodcast Option B: "Dành cho người vừa lỡ đu đỉnh — bây giờ nên làm gì?"
- GocNhinPodcast Option C: "Dành cho sinh viên muốn bắt đầu đầu tư với 1 triệu"
- **Nguyên tắc:** Chọn 1 persona cụ thể từ `00_core/audience_personas.md` → viết RIÊNG cho họ

### ④ Thêm tầng tâm lý hành vi (Behavioral Layer)

> Video gốc thiên KỸ THUẬT → GocNhinPodcast thêm TÂM LÝ ĐÁM ĐÔNG + HÀNH VI TÀI CHÍNH

**Cách làm:**
- Video gốc: "Phân tích PE cổ phiếu" → kỹ thuật thuần
- GocNhinPodcast: "Tại sao bạn biết PE cao mà vẫn mua? Vì bạn sợ lỡ cơ hội hơn sợ mất tiền. Đây là FOMO — hiệu ứng tâm lý mà ngành tài chính khai thác hàng ngày. Case study: Năm 2021, PE trung bình crypto lên 500x, nhưng 90% holder vẫn KHÔNG bán — vì não bộ tưởng 'nó còn lên nữa'."
- **Nguyên tắc:** Mỗi phân tích kỹ thuật PHẢI kèm lớp giải thích tâm lý: tại sao biết mà vẫn sai

### ⑤ Stress Test bằng lịch sử (Historical Stress)

> Video gốc chỉ nói HIỆN TẠI → GocNhinPodcast kiểm chứng bằng LỊCH SỬ KHỦNG HOẢNG

**Cách làm:**
- Video gốc: "BĐS là kênh đầu tư an toàn nhất" → chỉ nhìn hiện tại
- GocNhinPodcast: "Năm 2011, BĐS VN giảm 40-60%. Năm 2008, BĐS Mỹ giảm 31% trung bình, một số khu vực giảm 60%. Tháng 9/2023, Evergrande sụp — 300 tỷ USD nợ, hàng triệu căn hộ dang dở. BĐS an toàn? Phụ thuộc vào thời điểm, vị trí, đòn bẩy, và liệu bạn có đang nghe lời môi giới hay đang tự phân tích."
- **Nguyên tắc:** Không bao giờ nói "luôn luôn" — phải stress test mọi khẳng định bằng lịch sử

---

## CHECKLIST CHỐNG TRÙNG LẶP (Bắt buộc kiểm tra)

| # | Câu hỏi | ✅ |
|---|---|---|
| 1 | **Không sao chép câu?** | Không có câu nào giống transcript gốc > 5 từ liên tiếp |
| 2 | **Số liệu mới/bổ sung?** | Có ít nhất 3 số liệu mới mà video gốc KHÔNG có |
| 3 | **Case study mới?** | Tất cả case study đều bổ sung hoặc khác hoàn toàn |
| 4 | **Cấu trúc khác?** | Thứ tự luận điểm, cách mở bài, cách kết khác hoàn toàn |
| 5 | **Góc phân tích khác?** | Có ít nhất 1 insight mà video gốc KHÔNG ĐỀ CẬP |
| 6 | **Action Plan cụ thể hơn?** | Có ít nhất 3 bước hành động cực kỳ cụ thể |
| 7 | **Voice GocNhinPodcast?** | Giọng sắc, có số liệu, không guru, không hứa hẹn |

---

## OUTPUT FILE

Kết quả bước Differentiation lưu vào `episodes/[slug]/01_brief.md` nhưng thêm section:

```markdown
## Nguồn cảm hứng
- Video gốc: [URL]
- Chủ đề gốc: [...]

## Differentiation Strategy
- Kỹ thuật áp dụng: [① Data Depth + ⑤ Historical Stress]
- Góc phân tích mới: [...]
- Đối tượng tập trung: [...]

## Điểm khác biệt chính so với nguồn
1. [...]
2. [...]
3. [...]

## Số liệu & Case Study bổ sung
1. [Số liệu 1 — nguồn]
2. [Case study 1 — context]
```
