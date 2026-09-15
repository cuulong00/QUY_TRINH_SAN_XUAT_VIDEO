# Kế Hoạch Deep Research Chuyên Sâu & Khung Truy Vấn Trích Xuất Dữ Liệu
> **Tập phim:** VinFast Tách Mảng Sản Xuất – Bước Ngoặt Asset-Light & Lộ Trình Hòa Vốn 2027  
> **Mã thư mục:** `episodes/Vinfast-sap-co-lai`  
> **Chuyên gia:** The Socio-Economic Researcher  
> **Trọng tâm nghiên cứu theo yêu cầu chỉ đạo:** Bóc tách sâu sắc toàn bộ cấu phần của một chiếc xe ô tô VinFast ở 2 mốc thời điểm: **TRƯỚC KHI TÁCH MẢNG SẢN XUẤT** (khi hợp nhất A-Z) và **Ở THỜI ĐIỂM HIỆN TẠI (SAU KHI TÁCH MẢNG SẢN XUẤT)**, đi kèm số liệu kiểm toán tài chính thực chứng mới nhất (2024 - 2026).

---

## 1. PROMPT NẠP NGUỒN CẤU TRÚC (STRUCTURED INGESTION PROMPT - CHẠY DEEP RESEARCH TRÊN NOTEBOOKLM)

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web, tài liệu kỹ thuật và các hồ sơ pháp lý nộp SEC để thu thập đầy đủ nguồn thông tin, số liệu thực chứng mới nhất (2024-2026) cho các chủ đề trọng tâm sau:

1. BÓC TÁCH CẤU PHẦN CHIẾC XE VINFAST TRƯỚC VÀ SAU KHI TÁCH MẢNG SẢN XUẤT:
   - Thời điểm TRƯỚC KHI tách mảng sản xuất (trước tháng 05/2026): Cấu phần chiếc xe VinFast bao gồm những gì dưới sự quản lý trực tiếp của VinFast Auto Ltd? (Hạ tầng 500 ha nhà máy Hải Phòng, xưởng dập vỏ khung thép Schuler, xưởng hàn robot ABB/KUKA, xưởng sơn Eisenmann, nhà máy sản xuất pin VinES, cùng toàn bộ phần mềm ADAS, BMS, AI cockpit và thương hiệu).
   - Thời điểm HIỆN TẠI (sau tháng 05/2026): Cấu phần chiếc xe VinFast được chia tách ranh giới sở hữu như thế nào giữa 2 pháp nhân?
     + VinFast Auto (VFVN) còn nắm giữ những cấu phần nào? (Toàn bộ bộ não IP, phần mềm ADAS/AI, BMS, thuật toán quản lý pin, thiết kế kiểu dáng Pininfarina, thương hiệu VinFast, hợp đồng nhà cung cấp Tier-1 toàn cầu, mạng lưới phân phối toàn cầu).
     + VFTP (Công ty Tương Lai / Nhóm nhà đầu tư) tiếp nhận những cấu phần nào? (Toàn bộ phần thể xác cơ khí: nhà máy dập/sơn/hàn Hải Phòng, Hà Tĩnh, hạ tầng công nghiệp nặng, cổ phần VinEG và gánh khoản nợ tài chính 182.000 tỷ VNĐ).
   - So sánh trực tiếp sự thay đổi về quyền sở hữu, chi phí phân bổ và ranh giới tài sản trên một chiếc xe giữa 2 thời điểm.

2. BÁO CÁO TÀI CHÍNH & DOANH SỐ KIỂM TOÁN MỚI NHẤT (2024 - 2026):
   - Doanh thu hợp nhất, lỗ ròng (Net Loss), và biên lợi nhuận gộp (Gross Margin) năm 2024 và năm 2025:
     + Năm 2024: Doanh thu 44.019,6 tỷ VNĐ (1,81 tỷ USD), Lỗ ròng 77.354,9 tỷ VNĐ (3,18 tỷ USD), Biên lợi nhuận gộp -57,4%.
     + Năm 2025: Doanh thu 90.427,6 tỷ VNĐ (3,6 tỷ USD - tăng 105,4%), Lỗ ròng 97.245,7 tỷ VNĐ (3,9 tỷ USD - tăng 25,7%), Biên lợi nhuận gộp -42,5% (Q4/2025 đạt -39,9%).
   - Số lượng xe ô tô điện bàn giao: 97.399 xe (2024), 196.919 xe (2025 - tăng 102%), và 115.916 xe (nửa đầu năm 2026 tại VN).
   - Mục tiêu ~300.000 xe năm 2026 và lộ trình đạt điểm hòa vốn tại Việt Nam vào năm 2027.

3. HỒ SƠ SEC FORM 6-K THƯƠNG VỤ TÁCH MẢNG SẢN XUẤT (THÁNG 05/2026):
   - Thương vụ chuyển nhượng 100% cổ phần VFTP cho nhóm Công ty Tương Lai (vốn 122.000 tỷ VNĐ) giá 530 triệu USD (13.309,6 tỷ VNĐ).
   - Việc chuyển giao toàn bộ khoản nợ ròng 182.000 tỷ VNĐ (~7,2 tỷ USD) sang cho VFTP và bên mua.
   - Cơ chế Hợp đồng gia công (Tolling Fee agreement): VinFast trả phí gia công biến đổi cho VFTP trên mỗi chiếc xe hoàn chỉnh xuất xưởng.

4. BÓC TÁCH TỶ LỆ % BILL OF MATERIALS (BOM) & ĐỐI TÁC TIER-1:
   - Tỷ lệ % chi phí linh kiện cấu thành xe: Pin & BMS (30-40%), Chip/ADAS (18-22%), Thiết kế & IP (10-15%), Gia công khung vỏ (25-30%).
   - Mạng lưới Tier-1: NVIDIA (DRIVE Hyperion 10 cho L4 Robotaxi), Qualcomm (Snapdragon Cockpit), VinAI (DOMS, ASVM, MirrorSense), Bosch, ZF, CATL, Gotion High-Tech, StoreDot (pin sạc siêu nhanh 4-5 phút), ProLogium (pin thể rắn).

5. KẾ TOÁN KHẤU HAO CỐ ĐỊNH & PHƯƠNG TRÌNH CÂN BẰNG TƯƠNG LAI 2026-2030:
   - Cái bẫy trích khấu hao tài sản cố định (Fixed Cost Depreciation Trap) trước tái cấu trúc khi công suất nhà máy Hải Phòng chạy <40%.
   - Công thức tính Giá vốn (COGS) trước vs. sau tái cấu trúc.
   - Bức tranh tương lai 2026-2030: Chuyển dịch B2C cá nhân, nhà máy Tamil Nadu (Ấn Độ) & Subang (Indonesia), trạm sạc V-GREEN, và 2 kịch bản tài chính sinh tử (Win-Win vs. Stress Scenario).
```

---

## 2. DANH SÁCH 15 CÂU HỎI TRÍCH XUẤT CHI TIẾT (EXTRACTION QUERIES - CHẠY BATCH TO VAULT)

1. **Câu 1 (Bóc tách Cấu phần Linh kiện BOM trước vs sau tách):** Bóc tách chi tiết cấu phần chiếc xe ô tô VinFast ở 2 mốc thời gian: Trước khi tách mảng sản xuất (VinFast Auto hợp nhất quản lý từ nhà máy 500ha Hải Phòng, robot hàn, xưởng sơn, pin VinES đến IP/phần mềm) và Thời điểm Hiện tại sau khi tách mảng sản xuất (VinFast Auto/VFVN giữ IP, phần mềm ADAS/BMS, thương hiệu, hợp đồng Tier-1; VFTP/Công ty Tương Lai nhận lại tổ hợp nhà máy Hải Phòng/Hà Tĩnh, gia công cơ khí). So sánh tỷ lệ % chi phí BOM (Pin 30-40%, Chip 18-22%, IP 10-15%, Khung vỏ 25-30%).
2. **Câu 2 (Dữ liệu Tài chính & Doanh số Kiểm toán 2024-2026):** Tóm tắt dữ liệu tài chính & doanh số mới nhất của VinFast giai đoạn 2024-2026: doanh thu hợp nhất năm 2025 (90.427,6 tỷ VNĐ / 3,6 tỷ USD), lỗ ròng 2024 (77.354,9 tỷ VNĐ), lỗ ròng 2025 (97.245,7 tỷ VNĐ / 3,9 tỷ USD), sản lượng bàn giao 196.919 ô tô điện năm 2025, 115.916 ô tô điện H1/2026, diễn biến biên lợi nhuận gộp (-57,4% năm 2024, -42,5% năm 2025, -39,9% Q4/2025), mục tiêu 300.000 xe năm 2026 và mốc hòa vốn tại VN năm 2027.
3. **Câu 3 (Hồ sơ SEC Tái cấu trúc Form 6-K):** Chi tiết hồ sơ nộp SEC (Form 6-K Ex-99.1 tháng 05/2026) về thương vụ tái cấu trúc mảng sản xuất: việc tách VFTP thành VFVN (Soft Assets) và VFTP (Hard Assets), thương vụ nhượng cổ phần 530 triệu USD cho Công ty Tương Lai.
4. **Câu 4 (Ranh giới Tài sản SEC VFVN vs VFTP):** Phân định ranh giới tài sản SEC: VinFast (VFVN) giữ trọn vẹn những tài sản vô hình/IP nào (ADAS, BMS, kiểu dáng thiết kế, thương hiệu, hợp đồng nhà cung cấp Tier-1)? VFTP (Công ty Tương Lai) nhận lại những nhà máy, máy móc dập/sơn/hàn và khoản nợ vay 182.000 tỷ VNĐ nào?
5. **Câu 5 (Cơ chế Phí gia công Tolling Fee):** Cơ chế hợp đồng gia công (Tolling agreement) & phí gia công lắp ráp: VinFast trả phí cho VFTP theo công thức nào? Việc này biến chi phí khấu hao cố định thành chi phí biến đổi ra sao?
6. **Câu 6 (Bẫy Khấu hao Cố định & Hạ điểm Hòa vốn):** Giải thích cơ chế trích khấu hao nhà máy (Depreciation) và chi phí cố định trước tái cấu trúc, và cơ chế phí gia công biến đổi sau tái cấu trúc. Tách mảng sản xuất có làm VinFast không cần đầu tư thêm nhà máy tại VN nữa không và nguồn vốn tương lai dồn vào đâu?
7. **Câu 7 (Tác động P&L & Công thức COGS):** Tác động chi tiết đến Báo cáo Kết quả Kinh doanh (P&L & Gross Margin): So sánh công thức tính Giá vốn hàng bán (COGS) chiếc xe VinFast trước và sau khi tách nhà máy. Phân tích vì sao biên lợi nhuận gộp cải thiện từ -57,4% (2024) lên -42,5% (2025) và -39,9% (Q4/2025) và tiến tới dương.
8. **Câu 8 (Mạng lưới Nhà cung cấp Tier-1):** Mạng lưới nhà cung cấp Tier-1 & Chuỗi cung ứng toàn cầu: Danh sách các đối tác linh kiện, chip, pin của VinFast (Qualcomm, NVIDIA, Bosch, ZF, CATL, Gotion, StoreDot, ProLogium). VinFast tự làm phần nào, mua ngoài phần nào?
9. **Câu 9 (Giải mã Bản chất Tái cấu trúc Nội bộ):** Giải mã bản chất tái cấu trúc nội bộ "tay trái sang tay phải" giữa VinFast Auto Ltd (niêm yết NASDAQ) và Công ty Tương Lai / Tập đoàn Vingroup. Mục tiêu đưa VinFast Auto thành doanh nghiệp Asset-Light là gì?
10. **Câu 10 (Ai gánh khoản nợ 182k tỷ):** Ai thực sự gánh khoản nợ 182.000 tỷ VNĐ? Công ty Tương Lai lấy tiền đâu trả nợ ngân hàng? Vai trò phí gia công thu từ VinFast và tài sản bảo lãnh của tỷ phú Phạm Nhật Vượng và Tập đoàn Vingroup.
11. **Câu 11 (Rủi ro Giá giao dịch liên kết Transfer Pricing):** Phân tích rủi ro giá giao dịch liên kết (Transfer Pricing) giữa VinFast Auto và VFTP dưới góc nhìn kiểm toán độc lập và cơ quan quản lý SEC / Thuế Việt Nam.
12. **Câu 12 (Tỷ lệ Phụ thuộc Taxi GSM vs B2C):** Tỷ lệ phụ thuộc doanh số vào GSM trong giai đoạn 2024-2026 là bao nhiêu? Phép thử chuyển dịch từ bán taxi dịch vụ sang người tiêu dùng cá nhân (B2C) diễn ra như thế nào?
13. **Câu 13 (Bản đồ R&D & AI/ADAS):** Chi tiết bản đồ R&D công nghệ & hợp tác phần mềm lái tự động ADAS/AI với Qualcomm, NVIDIA, VinAI, Autobrains. VinFast nắm giữ độc quyền những phần mềm nào?
14. **Câu 14 (Bản chất Nền móng & Thời điểm Tách):** Phân tích bản chất nền móng & đỉnh điểm rủi ro: VinFast đã hoàn thành xong móng nhà máy chưa? Vì sao lại chọn thời điểm giữa năm 2026 để thực hiện tách mảng sản xuất?
15. **Câu 15 (Bức tranh 2026-2030 & 2 Kịch bản Sinh tử):** Bức tranh tương lai 2026-2030: 4 Trụ cột chiến lược (Đua quy mô 300k xe, Chuyển dịch B2C & Nhà máy Ấn Độ/Indo, Hào sâu V-GREEN, Phương trình cân bằng dòng tiền nội bộ) và 2 kịch bản tài chính sinh tử (Win-Win vs. Stress Scenario).
