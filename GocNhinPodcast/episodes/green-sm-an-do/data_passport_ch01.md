# Data Passport — Chương 1: Mở Đầu — Nghịch Lý Taxi Cước Rẻ Trên Xe Tiền Tỷ

**Episode:** green-sm-an-do
**Ngày tạo:** 2026-06-09
**Tổng số data points:** 9

## Bảng Passport

| Mã | Giá trị | Mô tả | Nguồn | Vị trí | Trích nguyên văn |
|---|---|---|---|---|---|
| DP-01 | 8 Rupee/km | Mức giá cước chào sân của Xanh SM tại Delhi | `001-vai-tro-...md` | L43 | "...launching in Delhi NCR with a starting fair of just 8 rupees per kilometer..." |
| DP-02 | 2.200 đồng | Quy đổi tiền Việt của cước taxi GSM tại Delhi | Derived | DP-01 | Khoảng 2.200 đồng mỗi cây số |
| DP-03 | 2,45 triệu Rupee | Giá bán lẻ của dòng xe VF MPV 7 (Limo Green) | `008-au-la-nhung...md` | L27 | "...VF MPV 7 priced at Rs 24.49 Lakh (~2.45 million Rupees)..." |
| DP-04 | 676 triệu đồng | Quy đổi tiền Việt của giá xe VF MPV 7 | Derived | DP-03 | Khoảng 676 triệu đồng Việt Nam |
| DP-05 | 28 nghìn tỷ đồng | Khoản lỗ ròng kỷ lục của VinFast trong quý 1 năm 2026 | `02_research_map.md` | L24 | "Lỗ ròng 28.1 nghìn tỷ VND (approx. $1.12 billion) trong Q1/2026" |
| DP-06 | 54,51% | Thị phần gọi xe taxi công nghệ của Green SM tại Việt Nam trong Q1/2026 | search_web | [URL] | "Green SM (GSM) chiếm 54,51% thị phần gọi xe taxi công nghệ tại Việt Nam trong quý I/2026" |
| DP-07 | 32.000 Rupee | Thu nhập bình quân đầu người của Ấn Độ | `02_research_map.md` | L8 | "Mức thu nhập bình quân khoảng 32.000 Rupee mỗi tháng..." |
| DP-08 | 13% | Tỷ trọng bàn giao xe của VinFast cho GSM trong Q1/2026 | search_web | [URL] | "Trong quý I năm 2026, doanh số bán xe cho GSM chiếm 13% tổng lượng bàn giao xe ô tô của VinFast" |
| DP-09 | 43,2% | Thị phần xe điện BEV của VinFast tại Philippines đầu năm 2026 | search_web | [URL] | "VinFast chiếm 43,2% thị phần xe điện BEV tại Philippines" |

## Số liệu CẦN BỔ SUNG (chưa có nguồn)

| Mô tả | Đã tìm ở đâu | Kết quả |
|---|---|---|
| Không có | | |

## Số liệu TÍNH TOÁN (derived)

| Mã | Phép tính | Từ DP nào | Kết quả |
|---|---|---|---|
| DP-C1 | DP-01 / cước VN (12.000-15.500) | 2.200 / 14.000 | Rẻ bằng 1/7 so với cước Xanh SM tại Việt Nam |
| DP-C2 | DP-07 * 276 | 32.000 * 276 | Khoảng 8,8 triệu đồng |

---

## Bảng đối chiếu Chapter vs Passport

| Câu trong chapter | Số liệu | Mã passport |
|---|---|---|
| "...mức cước chào sân chỉ 8 Rupee — tương đương khoảng 2.200 đồng..." | 8 Rupee, 2.200 đồng | DP-01, DP-02 ✅ |
| "...lỗ ròng kỷ lục hơn 28 nghìn tỷ đồng chỉ trong quý 1..." | 28 nghìn tỷ đồng | DP-05 ✅ |
| "VF MPV 7 cao cấp, có giá bán lẻ lên tới 2,45 triệu Rupee — quy đổi khoảng 676 triệu đồng Việt Nam." | 2,45 triệu Rupee, 676 triệu đồng | DP-03, DP-04 ✅ |
| "Người dân Ấn Độ có mức thu nhập bình quân khoảng 32.000 Rupee mỗi tháng, tương đương chừng 8,8 triệu đồng..." | 32.000 Rupee, 8,8 triệu đồng | DP-07, DP-C2 ✅ |
| "Green SM đã thâu tóm tới 54,51% thị phần gọi xe công nghệ tại Việt Nam..." | 54,51% | DP-06 ✅ |
| "...chiếm tới 13% tổng lượng xe ô tô bốn bánh bàn giao của VinFast..." | 13% | DP-08 ✅ |
| "...dẫn đầu thị trường xe điện Philippines với 43,2% thị phần..." | 43,2% | DP-09 ✅ |
