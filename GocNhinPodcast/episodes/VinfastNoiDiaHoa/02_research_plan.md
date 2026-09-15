# Kế hoạch Nghiên cứu Sâu — VinFast Nội Địa Hóa

## Bối cảnh Chiến lược (từ Pha 1 Topic Qualification)
- **Champion Angle:** Nghịch lý Chuỗi cung ứng Toàn cầu: Giải mã định kiến "Hàng dán nhãn"
- **Loại chủ đề:** Loại B (phân tích chiến lược doanh nghiệp/quốc gia)
- **Lăng kính:** Kinh tế học chuỗi cung ứng + Sở hữu trí tuệ

## Tài liệu nguồn đã có (3 tệp)
1. `Noidiahoa-gocnhinpodcast.md` — Tổng quan nội địa hóa, chiến lược 3 pha, hệ sinh thái nhà cung ứng
2. `VinfastGocNhinTuconso0.md` — Phân tích "Từ Số Không", bằng sáng chế, so sánh Tesla/BYD
3. `VinfastLamDuocGi_GocNhinPodcast.md` — Chi tiết nhà máy, NCAP, chuỗi cung ứng

## Đánh giá Data Gaps (Lỗ hổng dữ liệu cần bổ sung)

### Gaps nghiêm trọng (PHẢI có trước khi viết)
| # | Data Gap | Tại sao cần | Chương áp dụng |
|---|----------|-------------|----------------|
| 1 | **Số liệu Tesla Shanghai localization mới nhất 2025-2026** — Tài liệu nguồn trích 95% nhưng không rõ nguồn gốc cụ thể, năm nào, phương pháp đo | Hook dựa trên con số này, nếu sai = sụp toàn bộ | Ch.1 |
| 2 | **Chi tiết quy tắc RVC/ATIGA** — Tài liệu nguồn nhắc sơ nhưng chưa có số hiệu cụ thể, phương pháp tính % | Cốt lõi của luận đề "đếm giá trị gia tăng thay vì đếm ốc vít" | Ch.2 |
| 3 | **Báo cáo tài chính VinFast Q1-Q2 2026** — Tình hình lỗ/lãi, doanh số, dòng tiền mới nhất | Counter-thesis cần số liệu tài chính thực tế | Ch.4, Ch.7 |
| 4 | **Chi tiết nhà máy VinES-Gotion Vũng Áng** — Tiến độ xây dựng 2025-2026, công suất thực tế, ngày vận hành | Trụ cột của lộ trình 84% | Ch.6 |
| 5 | **Doanh số VinFast 2025-2026** — Tổng xe bán được, thị phần EV tại VN và toàn cầu | Bối cảnh thị trường thực tế | Ch.3, Ch.7 |
| 6 | **Euro NCAP chi tiết** — VF8 đạt 4 sao, lý do mất 1 sao (cụ thể mục nào bị trừ) | Counter-thesis trung thực | Ch.5 |
| 7 | **BYD doanh số và localization 2025-2026** — Thị phần toàn cầu, số lượng nhà máy ngoài TQ | Đối chiếu công bằng | Ch.4 |

### Gaps bổ trợ (tăng chiều sâu)
| # | Data Gap | Tại sao cần | Chương áp dụng |
|---|----------|-------------|----------------|
| 8 | **Chính sách ưu đãi EV của Việt Nam** — Thuế tiêu thụ đặc biệt, lệ phí trước bạ | Bối cảnh chính sách vĩ mô | Ch.2 |
| 9 | **Lịch sử localization ô tô VN** — Toyota, Hyundai, Thaco đạt bao nhiêu % | So sánh để thấy VinFast vượt trội | Ch.3 |
| 10 | **Chuỗi cung ứng vật liệu pin toàn cầu (Lithium, LFP)** — Giá cả, nguồn cung 2025-2026 | Đánh giá rủi ro lộ trình 84% | Ch.6 |

## Prompt Nạp Nguồn Cấu trúc (cho NotebookLM Deep Research)

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu và nguồn thông tin cho các chủ đề sau:

1. Tỷ lệ nội địa hóa (localization rate) của Tesla Giga Shanghai:
- Tìm các báo cáo chính thống xác nhận tỷ lệ linh kiện nội địa Trung Quốc trong xe Tesla Model 3/Model Y sản xuất tại Shanghai (2023-2026).
- Nguồn từ Global Times, Reuters, SCMP, hoặc báo cáo của UBS, Nikkei.

2. Quy tắc xuất xứ hàng hóa ATIGA (ASEAN Trade in Goods Agreement):
- Định nghĩa chính thức của RVC (Regional Value Content) và phương pháp tính.
- Ngưỡng RVC tối thiểu để được hưởng ưu đãi thuế quan ASEAN.
- So sánh với tiêu chuẩn Rules of Origin của USMCA (Mỹ-Mexico-Canada).

3. Tình hình tài chính và doanh số VinFast 2025-2026:
- Báo cáo tài chính quý gần nhất (doanh thu, lỗ ròng, dòng tiền).
- Tổng doanh số xe bán ra 2024-2025 (toàn cầu và tại Việt Nam).
- Thị phần EV tại thị trường Việt Nam.

4. Nhà máy pin VinES-Gotion tại Vũng Áng, Hà Tĩnh:
- Tiến độ xây dựng, công suất thiết kế (GWh/năm).
- Công nghệ cell LFP (Lithium Iron Phosphate) được chuyển giao.
- Ngày dự kiến vận hành thương mại.

5. BYD - Chiến lược tích hợp dọc và thị phần toàn cầu 2025-2026:
- Doanh số EV toàn cầu, số lượng nhà máy ngoài Trung Quốc.
- Tỷ lệ tự sản xuất linh kiện (vertical integration %).
- Lịch sử 30 năm phát triển pin (từ 1995 đến nay).

6. Euro NCAP - Kết quả đánh giá VinFast VF8:
- Chi tiết điểm số từng hạng mục (Adult, Child, Pedestrian, Safety Assist).
- So sánh với xe cùng phân khúc đạt 5 sao.
- Lý do cụ thể chỉ đạt 4 sao.

7. Lịch sử ngành công nghiệp ô tô Việt Nam và tỷ lệ nội địa hóa:
- Tỷ lệ nội địa hóa của Toyota, Hyundai, Thaco, Honda tại VN (2015-2024).
- Chính sách thuế tiêu thụ đặc biệt và lệ phí trước bạ cho xe điện tại VN.
- Vai trò của VinFast trong hệ sinh thái công nghiệp phụ trợ ô tô VN.

8. Chuỗi cung ứng vật liệu pin toàn cầu:
- Giá Lithium Carbonate 2024-2026 (xu hướng tăng/giảm).
- Ưu thế của công nghệ LFP so với NMC trong bối cảnh giá nguyên liệu.
- Rủi ro chuỗi cung ứng vật liệu thô cho các nhà sản xuất mới.
```

## Danh sách Câu hỏi Trích xuất (Extraction Queries cho Batch to Vault)

| # | Câu hỏi trích xuất | Mục tiêu chương |
|---|---------------------|-----------------|
| 1 | "Dựa trên các nguồn đã nạp, xác nhận chính xác tỷ lệ localization rate của Tesla Giga Shanghai. Con số 95% đến từ nguồn nào? Phương pháp đo là gì? Năm nào?" | Ch.1 |
| 2 | "Giải thích chi tiết cách tính RVC theo ATIGA. Ngưỡng % tối thiểu là bao nhiêu? So sánh với tiêu chuẩn USMCA của Bắc Mỹ." | Ch.2 |
| 3 | "Tổng hợp doanh số VinFast 2024-2025 và tình hình tài chính gần nhất. Lỗ ròng là bao nhiêu? Dòng tiền từ hoạt động kinh doanh?" | Counter-Thesis |
| 4 | "Chi tiết về nhà máy VinES-Gotion Vũng Áng: Công suất, tiến độ, công nghệ LFP, và ảnh hưởng đến tỷ lệ nội địa hóa 84%." | Ch.6 |
| 5 | "So sánh chiến lược chuỗi cung ứng của VinFast vs Tesla vs BYD. Tesla dùng bao nhiêu nhà cung cấp tại TQ? BYD tự sản xuất bao nhiêu %?" | Ch.4 |
| 6 | "Chi tiết kết quả Euro NCAP của VF8: Điểm từng hạng mục, lý do không đạt 5 sao, và so sánh với đối thủ cùng phân khúc." | Ch.5 |
| 7 | "Lịch sử tỷ lệ nội địa hóa ngành ô tô Việt Nam: Toyota, Hyundai, Honda, Thaco đã đạt bao nhiêu % sau bao nhiêu năm hoạt động?" | Ch.2, Ch.3 |
| 8 | "Phân tích rủi ro: VinFast đối mặt với những thách thức gì trong lộ trình đạt 84%? Chuỗi cung ứng Lithium, cạnh tranh BYD/CATL, và rào cản công nghệ." | Ch.6, Ch.7 |
| 9 | "Hệ sinh thái 700 nhà cung ứng nội địa của VinFast: Danh sách các doanh nghiệp phụ trợ chính, sản phẩm cung cấp, và tác động đến nền kinh tế VN." | Ch.3 |
| 10 | "Vụ tai nạn tàu hỏa tại Indonesia liên quan đến VinFast: Chi tiết sự kiện, kết luận của KNKT, và ý nghĩa đối với đánh giá an toàn xe." | Ch.5 |
