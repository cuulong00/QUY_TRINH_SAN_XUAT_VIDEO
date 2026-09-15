# Postmortem — [Tên Episode]

> **Episode:** `episodes/[slug]/`
> **Ngày publish:** YYYY-MM-DD
> **Ngày postmortem:** YYYY-MM-DD (chạy sau publish 7-14 ngày)

---

## 1. Performance Snapshot (48h sau publish)

| Chỉ số | Dự đoán | Thực tế | Đánh giá |
|--------|---------|---------|----------|
| CTR | % | % | ✅ / ⚠️ / ❌ |
| AVD (Average View Duration) | phút | phút | ✅ / ⚠️ / ❌ |
| AVD % (% video xem được) | % | % | ✅ / ⚠️ / ❌ |
| Views (48h) | | | |
| Impressions (48h) | | | |
| Subscribers gained | | | |
| Comments | | | |
| Likes / Dislikes ratio | | | |

## 2. Retention Curve Analysis

### Điểm rơi chính (Drop-off Points)
- Phút ___: Rơi ___% → Nguyên nhân dự đoán: ___
- Phút ___: Rơi ___% → Nguyên nhân dự đoán: ___

### Điểm giữ tốt (Retention Peaks)
- Phút ___: Giữ tốt → Lý do: ___

### So sánh với dự đoán từ Retention Gate
- Retention Gate dự đoán drop ở phút ___? Thực tế: ___
- Personal Stakes đặt ở chương ___. Hiệu quả: ___
- Re-hook ở phút ___. Hiệu quả: ___

## 3. Hook & Title Assessment

| Yếu tố | Kết quả | Bài học |
|---------|---------|--------|
| Title dùng | "[title]" | |
| CTR so với trung bình kênh | Cao hơn / Thấp hơn ___% | |
| Hook strategy (loại nào) | Data contrast / Common vs sharper / Pain-first / ... | |
| Thumbnail headline | "[headline]" | |

## 4. Content Quality Retrospective

### Điều làm tốt nhất
1. 
2. 

### Điều cần cải thiện
1. 
2. 

### Câu / đoạn đắt nhất (Golden Lines thực sự — validated bằng retention)
- "_____________" (phút ___: retention giữ / tăng)

### Câu / đoạn yếu nhất (validated bằng retention drop)
- Chương ___, phút ___: retention rơi → nguyên nhân: ___

## 5. Audience Feedback

### Comment nổi bật (trích 3-5 comment có giá trị)
1. "_____________" → Insight rút ra: ___
2. "_____________" → Insight rút ra: ___
3. "_____________" → Insight rút ra: ___

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
| Topic selection | /10 | |
| Hook effectiveness | /10 | |
| Script quality | /10 | |
| Visual quality | /10 | |
| Title + Thumbnail | /10 | |
| Overall satisfaction | /10 | |

---

> **Quy tắc:** Postmortem PHẢI được chạy trong vòng 14 ngày sau publish. Nếu quá 14 ngày, vẫn phải chạy nhưng ghi chú "late postmortem".
> **Cập nhật:** Sau khi hoàn thành postmortem, PHẢI cập nhật `01_management/episode_registry.csv` với cột performance data.
