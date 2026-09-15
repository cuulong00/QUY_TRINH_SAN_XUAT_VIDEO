# Data Passport — Chương 3: Cơ Chế Vòng Lặp Công Nghiệp Khép Kín

**Episode:** green-sm-an-do
**Ngày tạo:** 2026-06-09
**Tổng số data points:** 10

## Bảng Passport

| Mã | Giá trị | Mô tả | Nguồn | Vị trí | Trích nguyên văn |
|---|---|---|---|---|---|
| DP-01 | 25/02/2024 | Cột mốc khởi công nhà máy Thoothukudi, Tamil Nadu | `001-vai-tro-...md` | L156 | "Thoothukudi, Tamil Nadu, February 25, 2024 – VinFast, Vietnam's leading electric vehicle manufacturer, officially broke ground on its first integrated electric vehicle (EV) manufacturing facility..." |
| DP-02 | 05/08/2025 | Cột mốc khánh thành nhà máy assembly tại Tamil Nadu | `001-vai-tro-...md` | L164 | "On August 5, 2025, VinFast officially inaugurated the assembly plant..." |
| DP-03 | 01/06/2026 | Ngày xuất xưởng chiếc xe thứ 10.000 tại nhà máy Ấn Độ | `001-vai-tro-...md` | L160 | "...subsequently rolling out its 10,000th vehicle in less than a year of active production... rollout of the 10,000th vehicle from its manufacturing facility in Thoothukudi, Tamil Nadu. The achievement comes less than a year after production began in India." |
| DP-04 | 50.000 xe/năm | Công suất thiết kế ban đầu của nhà máy Ấn Độ | `001-vai-tro-...md` | L148 | "It has an initial production capacity of 50,000 units annually, scalable to 150,000 units." |
| DP-05 | 150.000 xe/năm | Công suất mở rộng tối đa của nhà máy Ấn Độ | `001-vai-tro-...md` | L148 | "It has an initial production capacity of 50,000 units annually, scalable to 150,000 units." |
| DP-06 | 12/2025 | Ký MOU mở rộng giai đoạn 2 đầu tư thêm 500 triệu USD | `001-vai-tro-...md` | L164 | "On December 4, 2025... VinFast is investing an additional $500 million to establish dedicated assembly lines for electric buses and e-scooters..." |
| DP-07 | 15% | Thuế suất nhập khẩu linh kiện/xe ưu đãi của quốc gia | `001-vai-tro-...md` | L120 | "The national EV policy slashes import duties on completely built units (CBUs) from 70-100% to 15% for five years for OEMs that commit a minimum investment of $500 million..." |
| DP-08 | 31/12/2027 | Thời hạn miễn 100% thuế đường bộ của Tamil Nadu | `001-vai-tro-...md` | L168 | "This waiver was previously set to expire but has now been extended until Dec 31, 2027..." |
| DP-09 | 10.900 crore Rupee | Ngân sách của chương trình PM E-DRIVE hỗ trợ xe điện của Ấn Độ | search_web | [URL] | "The PM E-DRIVE scheme has a total budget of ₹10,900 crore and is implemented from October 1, 2024, to March 31, 2028." |
| DP-10 | 01/10/2024 | Ngày chương trình PM E-DRIVE chính thức có hiệu lực thay thế FAME | search_web | [URL] | "The PM E-DRIVE scheme was launched on October 1, 2024, to succeed the FAME-II scheme..." |

## Số liệu CẦN BỔ SUNG (chưa có nguồn)

| Mô tả | Đã tìm ở đâu | Kết quả |
|---|---|---|
| Không có | | |

## Số liệu TÍNH TOÁN (derived)

| Mã | Phép tính | Từ DP nào | Kết quả |
|---|---|---|---|
| DP-C1 | DP-03 / thời gian hoạt động (10 tháng) | 10.000 xe / 300 ngày | Trung bình mỗi ngày xuất xưởng khoảng 33 xe |

---

## Bảng đối chiếu Chapter vs Passport

| Câu trong chapter | Số liệu | Mã passport |
|---|---|---|
| "Tháng 2 năm 2024, VinFast chính thức khởi công..." | 25/02/2024 | DP-01 ✅ |
| "...vào tháng 8 năm 2025, những chiếc xe đầu tiên..." | 05/08/2025 | DP-02 ✅ |
| "Đến ngày 1 tháng 6 năm 2026, nhà máy này chính thức cán mốc xuất xưởng chiếc xe thứ 10.000" | 01/06/2026, 10.000 | DP-03 ✅ |
| "...thuế nhập khẩu đối với ô tô nguyên chiếc dao động từ 70% đến 100%." | 70-100% | DP-07 (tham chiếu CBU) ✅ |
| "...chỉ còn 15% trong vòng năm năm..." | 15% | DP-07 ✅ |
| "...cho các nhà sản xuất cam kết đầu tư tối thiểu 500 triệu USD." | 500 triệu USD | DP-07 ✅ |
| "...bang Tamil Nadu còn miễn 100% thuế đường bộ cho xe điện đến hết năm 2027." | Hết 2027 (31/12/2027) | DP-08 ✅ |
| "Công suất thiết kế ban đầu của nhà máy là 50.000 xe mỗi năm và có thể mở rộng lên tới 150.000 xe." | 50.000 xe/năm, 150.000 xe/năm | DP-04, DP-05 ✅ |
| "Chương trình trợ cấp liên bang PM E-DRIVE trị giá 10.900 crore Rupee..." | 10.900 crore Rupee | DP-09 ✅ |
