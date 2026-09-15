# Data Passport — Chương 2: Bài Toán TCO Trên Vai Người Thành Thị

**Episode:** vinfast-co-that-su-re
**Ngày cập nhật:** 2026-06-15
**Tổng số data points:** 14

## Bảng Passport

| Mã | Giá trị | Mô tả | Nguồn | Vị trí | Trích nguyên văn |
|---|---|---|---|---|---|
| DP-01 | 2,4 triệu VNĐ | Chi phí bảo dưỡng định kỳ VF 5 Plus trong 100.000 km | [vf-phu-song-008.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/research_vault/vf-phu-song-008-phan-tich-tiem-nang-doanh-thu-va-dong-tien-dai-han-tu-dich-vu-bao-duong-sac-pin.md) | L128 | "Tổng chi phí bảo dưỡng VF5 trong 100.000 km đạt khoảng 2,4 triệu đồng." |
| DP-02 | 24,7 triệu VNĐ | Chi phí bảo dưỡng định kỳ xe xăng Vios trong 100.000 km | [vf-phu-song-008.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/research_vault/vf-phu-song-008-phan-tich-tiem-nang-doanh-thu-va-dong-tien-dai-han-tu-dich-vu-bao-duong-sac-pin.md) | L128 | derived: "Chênh lệch riêng phần bảo dưỡng định kỳ là 22,3 triệu đồng" (2.4M + 22.3M = 24.7M) |
| DP-03 | 10/02/2029 | Hết hạn ưu đãi miễn phí sạc 3 năm cho xe mua sau 10/02/2026 | [google_ai_audit_02.md](google_ai_audit_02.md) | L74 | "khách hàng mua xe mới được miễn phí tối đa 10 lần sạc/tháng liên tục trong vòng 3 năm (đến hết 10/02/2029)." |
| DP-04 | 6,5 lít/100km | Tiêu hao nhiên liệu trung bình xe xăng hạng B (Vios) | [google_ai_audit_02.md](google_ai_audit_02.md) | L25 | "Nếu một chiếc xe hạng B tiêu thụ trung bình 6,5 lít/100 km" |
| DP-05 | 22.060 VNĐ/lít | Giá xăng RON 95-III Vùng 1 ngày 12/06/2026 | [google_ai_audit_02.md](google_ai_audit_02.md) | L24 | "giá xăng Xăng E10 RON 95-III thực tế tại Vùng 1 đã giảm xuống chỉ còn 22.060 đồng/lít." |
| DP-06 | 1.500 km | Quãng đường di chuyển trung bình một tháng | [vf-phu-song-008.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/research_vault/vf-phu-song-008-phan-tich-tiem-nang-doanh-thu-va-dong-tien-dai-han-tu-dich-vu-bao-duong-sac-pin.md) | L116 | "Tính trung bình quãng đường di chuyển... 1.500km" |
| DP-07 | 529 triệu VND | Giá niêm yết xe điện VinFast VF 5 Plus kèm pin | Quyết định giá bán VinFast | 01/03/2025 | Công bố dừng thuê pin và bán xe kèm pin từ ngày 1/3/2025 |
| DP-08 | 488 triệu VND | Giá niêm yết xe xăng Toyota Vios E CVT | search_web | https://toyota.com.vn | Giá niêm yết chính hãng Toyota Vios E CVT tại Việt Nam |
| DP-09 | 10 lần/tháng | Giới hạn số lần sạc miễn phí V-Green cho xe mua mới từ 10/02/2026 | [google_ai_audit_02.md](google_ai_audit_02.md) | L75 | "Mốc giới hạn 10 lần sạc/tháng là áp dụng cho khách hàng mua xe mới tính từ sau mốc 10/02/2026" |
| DP-10 | 1,5 - 2,5 triệu VNĐ | Chi phí gửi xe đô thị (chung cư & văn phòng) Hà Nội / TP.HCM | [google_ai_audit_02.md](google_ai_audit_02.md) | L58 | "Chi phí cố định như gửi xe ở chung cư/văn phòng tại Hà Nội và TP.HCM dao động từ 1,5 - 2,5 triệu đồng/tháng." |
| DP-11 | 533 triệu VNĐ | Giá lăn bánh VF 5 Plus kèm pin năm 2026 | [google_ai_audit_02.md](google_ai_audit_02.md) | L16 | "chi phí lăn bánh thực tế (bao gồm bảo hiểm, biển số, phí đường bộ cố định) chỉ dao động quanh mốc 533 - 535 triệu đồng" |
| DP-12 | 541 triệu VNĐ | Giá lăn bánh Toyota Vios E CVT ở tỉnh | [google_ai_audit_02.md](google_ai_audit_02.md) | L17 | "tổng giá lăn bánh thực tế của Vios chỉ rơi vào khoảng 540 - 542 triệu đồng." |
| DP-13 | 0 VNĐ | Hóa đơn tiền sạc trạm V-Green hàng tháng của VF 5 Plus (chạy 1.500km) | [google_ai_audit_02.md](google_ai_audit_02.md) | L76 | "người mua mới năm 2026 có chi phí năng lượng bằng 0 đồng" |

## Số liệu CẦN BỔ SUNG (chưa có nguồn)

*Không có.*

## Số liệu TÍNH TOÁN (derived)

| Mã | Phép tính | Từ DP nào | Kết quả |
|---|---|---|---|
| DP-C1 | DP-06 * (DP-04 / 100) * DP-05 | 1.500 * 0.065 * 22.060 | 2.150.850 VNĐ/tháng |
| DP-C2 | ~14 kWh/100km | Tiêu hao điện trung bình VF 5 Plus | [vf-phu-song-008.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-co-that-su-re/research_vault/vf-phu-song-008-phan-tich-tiem-nang-doanh-thu-va-dong-tien-dai-han-tu-dich-vu-bao-duong-sac-pin.md) | xấp xỉ 14 kWh/100km |
