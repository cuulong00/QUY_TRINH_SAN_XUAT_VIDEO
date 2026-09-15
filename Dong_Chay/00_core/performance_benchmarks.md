 # Performance Benchmarks — Dòng Chảy

> **Mục đích:** File này là nguồn sự thật DUY NHẤT cho baseline performance của kênh. Mọi postmortem và planning đều so sánh với file này.
> **Cập nhật:** Mỗi 10 episodes hoặc mỗi khi có sự thay đổi lớn về performance.

---

## 1. Baseline Metrics (CẬP NHẬT: 2026-05-20)

> **Trạng thái hiện tại:** ĐÃ CÓ BASELINE ĐẦU TIÊN (Dựa trên 10 videos gần nhất)

| Chỉ số | Baseline hiện tại | Mục tiêu | Ghi chú |
|--------|-------------------|----------|---------|
| CTR trung bình | ~4.5% | > 5% | Kênh mới: CTR 4-6% là đạt chuẩn |
| AVD trung bình | 5 phút 18 giây | > 6 phút | Trung bình toàn kênh bao gồm cả Shorts |
| AVD % trung bình (Long) | ~45% | > 40% | Video dài giữ chân từ 40% - 59.5% |
| Views/48h trung bình | ~3,500 views | > 5,000 views | |
| Subscriber conversion | ~1.5% | > 2% per video | |
| Comment rate | ~0.8% | > 1% of views | Cần tối ưu bằng Comment Hook ở Outro |

## 2. Retention Curve Patterns (Rút ra từ postmortems)

### Pattern đã xác nhận
- **Độ dài ngọt ngào (Length Sweet Spot):** Các video dài từ **8 - 12 phút** đạt tỷ lệ giữ chân xuất sắc từ **49% - 59.5%** (evidence: `indonesia-quan-tri-300m`, `vinfast-ban-nha-may-530m`). Các video dài từ 17 - 20 phút dễ bị hụt hơi trừ khi có kịch tính đối đầu cao.
- **Drop phút 5 (Lỗi Data Dumping):** Xảy ra khi Ch.2 không có Personal Stakes, nhồi nhét lý thuyết. Khán giả bỏ đi vì không thấy lợi ích sát sườn (evidence: `walmart-quyen-luc`, `nhat-the-hoa-quyen-luc`, `to-lam-tap-can-binh`).
- **Giữ chân kỷ lục (Personal Stakes Hook):** Đột ngột bẻ lái một vấn đề vĩ mô khô khan thành áp lực tài chính trực tiếp đè lên thu nhập của người xem (ví dụ: lương 15 triệu/tháng). Điều này kích hoạt tâm lý sinh tồn (evidence: `cach-mang-vi-the` đạt AVD 8:51).
- **Lỗi Đề tài Trừu tượng (Abstract/Happiness Flop):** Các chủ đề thiếu "wallet stakes" thực tế (như chỉ số hạnh phúc, GDP lý thuyết) bị người xem bỏ qua hoặc rơi rớt giữ chân nghiêm trọng (evidence: `vietnam-hanh-phuc-hon-trung-quoc` tụt xuống 38.4%).
- **Geopolitical Drama (Kịch tính địa chính trị):** Dùng để bù đắp khi chủ đề thiếu Personal Stakes. Khai thác sự đối đầu (Vn vs Trung Quốc/Ấn Độ) để kích thích lòng tự hào quốc gia (evidence: `vinfast-an-do` short đạt 107.4% retention).
- **Lỗi Hypothetical Stakes:** Bắt người xem Việt Nam tưởng tượng lợi ích/rủi ro ở một quốc gia khác (Mexico) mà không có sợi dây liên kết nào về xuất khẩu hay việc làm nội địa. Gây chạm trần hiển thị và rớt khán giả thảm hại.
- **Geopolitical Drama (Kịch tính địa chính trị):** Dùng để bù đắp khi chủ đề thiếu Personal Stakes. Khai thác sự đối đầu (Vn vs Trung Quốc/Ấn Độ) để kích thích lòng tự hào quốc gia (evidence: `vinfast-an-do`).

### Ngưỡng nguy hiểm
- Nếu retention rơi > 15% trong 1 phút → có đoạn "chết"
- Nếu AVD < 30% → cấu trúc video có vấn đề nghiêm trọng
- Nếu CTR < 3% → title/thumbnail cần redesign

## 3. Title & Thumbnail Performance

### Title patterns hoạt động tốt
| Pattern | Ví dụ | CTR trung bình |
|---------|-------|----------------|
| [THU THẬP DỮ LIỆU] | | |

### Title patterns hoạt động kém
| Pattern | Ví dụ | CTR trung bình | Lý do |
|---------|-------|----------------|-------|
| Thuật ngữ chuyên gia | "Nhất Thể Hóa Quyền Lực" | Thấp | Khán giả không search |

### Thumbnail patterns
| Pattern | CTR | Ghi chú |
|---------|-----|---------|
| [THU THẬP DỮ LIỆU] | | |

## 4. Content Category Performance

| Loại nội dung | Số episodes | AVD trung bình | CTR trung bình | Ghi chú |
|---------------|-------------|----------------|----------------|---------|
| Loại A (tài chính cá nhân) | [ĐẾM] | | | |
| Loại B (chiến lược doanh nghiệp/quốc gia) | [ĐẾM] | | | |
| Loại C (documentary toàn cầu) | [ĐẾM] | | | |

## 5. Hook Strategy Performance

| Hook strategy | Lần dùng | CTR trung bình | Retention phút 1 | Hiệu quả |
|---------------|----------|----------------|-------------------|----------|
| Data contrast | [ĐẾM] | | | |
| Common vs sharper reading | [ĐẾM] | | | |
| Quiet expert question | [ĐẾM] | | | |
| Persona pain + structure | [ĐẾM] | | | |
| Historical mirror | [ĐẾM] | | | |

## 6. Quy tắc cập nhật

1. Sau mỗi postmortem → cập nhật các bảng trên
2. Sau mỗi 10 episodes → tính lại baseline trung bình
3. Khi phát hiện pattern mới (tốt hoặc xấu) → thêm vào Section 2 hoặc 3
4. Khi baseline thay đổi > 20% → review toàn bộ pipeline xem cần điều chỉnh gì
