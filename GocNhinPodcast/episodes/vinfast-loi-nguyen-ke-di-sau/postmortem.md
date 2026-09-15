# Postmortem — Lời Nguyền Xe Điện: Tại Sao VinFast Buộc Phải "Chưa Học Bò Đã Lo Học Chạy"?

> **Episode:** `episodes/vinfast-loi-nguyen-ke-di-sau/`
> **Ngày publish:** *Chờ xuất bản*
> **Ngày postmortem:** *Chờ thực hiện (7-14 ngày sau publish)*

---

## 1. Performance Snapshot (48h sau publish)

| Chỉ số | Dự đoán | Thực tế | Đánh giá |
|--------|---------|---------|----------|
| CTR | 8.5% | % | ✅ / ⚠️ / ❌ |
| AVD (Average View Duration) | 12:00 phút | phút | ✅ / ⚠️ / ❌ |
| AVD % (% video xem được) | 50% | % | ✅ / ⚠️ / ❌ |
| Views (48h) | 15.000 | | |
| Impressions (48h) | 180.000 | | |
| Subscribers gained | +150 | | |
| Comments | 80 | | |
| Likes / Dislikes ratio | 98% | | |

## 2. Retention Curve Analysis

### Điểm rơi chính (Drop-off Points)
- Phút ___: Rơi ___% → Nguyên nhân dự đoán: ___
- Phút ___: Rơi ___% → Nguyên nhân dự đoán: ___

### Điểm giữ tốt (Retention Peaks)
- Phút ___: Giữ tốt → Lý do: ___

### So sánh với dự đoán từ Retention Gate
- Retention Gate dự đoán drop ở phút ___? Thực tế: ___
- Personal Stakes đặt ở chương 2. Hiệu quả: ___
- Re-hook ở phút 3:30, 7:00, 11:00. Hiệu quả: ___

## 3. Hook & Title Assessment

| Yếu tố | Kết quả | Bài học |
|---------|---------|--------|
| Title dùng | "VinFast Nợ 182.000 Tỷ: "Ve Sầu Thoát Xác" Hay Cú Bẻ Lái Sinh Tồn?" | |
| CTR so với trung bình kênh | Cao hơn / Thấp hơn ___% | |
| Hook strategy (loại nào) | Contradiction-first (Nghịch lý nợ nần) / Pain-first | |
| Thumbnail headline | "182.000 TỶ NỢ: AI GÁNH?" | |

## 4. Content Quality Retrospective

### Điều làm tốt nhất (Dự phóng)
1. Cấu trúc chương mạch lạc, giải thích rõ ràng khái niệm Asset-Light và Chaebol đối chiếu giúp giảm tải sự nặng nề của số liệu tài chính.
2. Neo số liệu cực kỳ chặt chẽ qua Data Passport cho từng chương, loại bỏ hoàn toàn các ý kiến cảm tính.

### Điều cần cải thiện (Dự phóng)
1. Đảm bảo âm thanh TTS khi ghép nối các câu ngắn không bị ngắt quãng quá cụt.
2. Kiểm tra kỹ phản hồi của người xem về sự cân bằng góc nhìn trong Chương 5 đối với rủi ro của hệ thống ngân hàng nội địa.

### Câu / đoạn đắt nhất (Golden Lines thực sự — dự kiến)
- *"VinFast bành trướng không phải vì kiêu ngạo, mà vì đó là phản xạ sinh tồn."* (Chương 1)
- *"Trần Việt Nam quá thấp, sàn hòa vốn quốc tế lại quá cao."* (Chương 1)

### Câu / đoạn yếu nhất (dự kiến)
- Chương 3, các đoạn giải thích kỹ thuật về VFTP và P-Note có thể hơi khô khan và làm giảm nhịp nghe của khán giả đại chúng.

## 5. Audience Feedback

### Comment nổi bật (trích 3-5 comment có giá trị)
1. "..." → Insight rút ra: ___
2. "..." → Insight rút ra: ___
3. "..." → Insight rút ra: ___

### Sentiment chung
- Tích cực: ___% (ước lượng)
- Phản biện / Góp ý xây dựng: ___
- Tiêu cực: ___

## 6. Pipeline Adjustment (BẮT BUỘC — Đây là phần quan trọng nhất)

### Quy tắc cần thêm/sửa trong pipeline
- [ ] ___

### Anti-pattern mới phát hiện (nếu có)
- ___

### Bài học cho episode tiếp theo
1. ___
2. ___
3. ___

### Cập nhật files (nếu cần)
- [ ] `00_core/anti_patterns.md` — thêm anti-pattern mới?
- [ ] `00_core/anti_ai_isms.md` — thêm từ/cụm cấm mới?
- [ ] `00_core/longform_blueprint.md` — điều chỉnh cấu trúc?
- [ ] `00_core/hook_library.md` — thêm hook strategy mới?
- [ ] `01_management/lessons_learned.md` — ghi bài học?
- [ ] `00_core/performance_benchmarks.md` — cập nhật baseline?

## 7. Score Card

| Hạng mục | Điểm (1-10) | Ghi chú |
|----------|-------------|---------|
| Topic selection | 9/10 | Đánh đúng nỗi đau vĩ mô và sự kiện nóng |
| Hook effectiveness | 8/10 | |
| Script quality | 9/10 | |
| Visual quality | /10 | *Chờ hoàn thiện video* |
| Title + Thumbnail | 9/10 | |
| Overall satisfaction | 8.8/10 | |
