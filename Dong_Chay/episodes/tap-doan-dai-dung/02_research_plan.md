# 02_research_plan.md — Kế Hoạch Deep Research Chuyên Sâu

> **Mục tiêu:** Khai thác toàn diện cơ sở dữ liệu nghiên cứu thông qua **Google NotebookLM Deep Research Engine (`--mode deep --import-all`)** để thu thập dữ liệu định lượng, báo cáo tài chính, chứng chỉ công nghệ, dữ liệu kỹ thuật kết cấu thép, hồ sơ các siêu dự án quốc tế (World Cup Lusail, Điện gió ngoài khơi Greater Changhua, Hầm Fehmarnbelt) và các văn kiện đầu tư của Tổ chức Tài chính Quốc tế (IFC) liên quan đến **Tập đoàn Cơ khí Đại Dũng (DDC)**.

---

## 1. Bản Chỉ Dẫn Ingestion Cấu Trúc (Structured Deep Research Ingestion Prompt)
*(Dùng cho lệnh `notebooklm source add-research "<Query>" --mode deep --import-all`)*

```text
Nghiên cứu chuyên sâu toàn diện về Tập đoàn Cơ khí Xây dựng Thương mại Đại Dũng (DaiDung Corporation / DDC) - Vị thế, Năng lực Công nghệ, Hệ sinh thái Sản xuất, Siêu dự án Toàn cầu và Chiến lược Tài chính:

Trọng tâm nghiên cứu chuyên sâu gồm 6 trụ cột chính:

1. Lịch sử phát triển, Cơ cấu tổ chức và Lãnh đạo sáng lập:
   - Quá trình chuyển mình từ xưởng cơ khí tư nhân năm 1995 thành tập đoàn công nghiệp nặng hàng đầu Việt Nam.
   - Chân dung Chủ tịch HĐQT kiêm Tổng Giám đốc Trịnh Tiến Dũng và ban điều hành; vai trò của ông tại Hiệp hội Doanh nghiệp TP.HCM (HUBA), Hội đồng Quản trị PC1 Group.
   - Cơ cấu công ty mẹ - con, các đơn vị thành viên, nhà máy cơ khí, công ty kết cấu thép và đơn vị lắp dựng công trình.

2. Quy mô Vật lý, Hệ thống 6 Cụm Nhà máy 120 Hecta và Công suất Chế tạo:
   - Chi tiết diện tích, công suất, thiết bị của 6 cụm nhà máy: Nhà máy An Hạ / Bình Chánh (TP.HCM), Nhà máy Long An (Đức Hòa), Nhà máy Quảng Ngãi (Dung Quất), Nhà máy Cơ khí Công nghệ cao Đông Xuyên (Vũng Tàu - 10 ha), Dự án Tổ hợp Cơ khí Công nghệ cao Nghi Sơn (Thanh Hóa - 45 ha).
   - Công suất thiết kế hiện tại (500.000 tấn kết cấu thép/năm) và lộ trình mở rộng lên hơn 800.000 tấn/năm đến năm 2030.
   - Năng lực cầu cảng chuyên dụng nước sâu, bãi chế tạo cấu kiện siêu trường siêu trọng (heavy fabrication yards), cẩu trục tải trọng lớn (hàng trăm tấn) phục vụ xuất khẩu đường biển.

3. Năng lực Kỹ thuật Lõi, Hệ thống 33+ Chứng chỉ Toàn cầu và Công nghệ Số hóa (BIM & Robotics):
   - Phân tích chi tiết các chứng chỉ quốc tế cấp cao nhất:
     + AISC (Mỹ) & chứng nhận sơn đặc chủng chống ăn mòn biển SPE (Sophisticated Paint Endorsement).
     + ASME (Mỹ) dấu U, S, R Stamp cho thiết bị áp lực, bồn bể lò hơi công nghiệp.
     + EN 1090-1 EXC4 (Tiêu chuẩn Châu Âu cấp 4 cao nhất cho kết cấu thép chịu lực đặc biệt).
     + H-Grade (Nhật Bản), CWB (Canada), AS/NZS 5131 (Úc/New Zealand), ISO 3834-2 (quản lý chất lượng hàn quốc tế).
   - Công nghệ R&D, chuyển đổi số: Mô hình thông tin công trình BIM (Tekla Structures, Revit), Robot hàn gantry, máy cắt Plasma/Laser Fiber tấm dày, kiểm tra không phá hủy mối hàn NDT (UT, RT, MPI, DPI).
   - Tiêu chuẩn công trình xanh LEED Gold và kiểm kê phát thải carbon (ISO 14064, ISO 14067, EPD, tuân thủ CBAM Châu Âu).

4. Hồ sơ Siêu Dự án Toàn cầu (World-Class Megaprojects Track Record):
   - Gói thầu World Cup 2022 (Qatar): Trúng thầu 80 triệu USD cung cấp hơn 34.000 tấn kết cấu thép cho Sân vận động Lusail Iconic (80.000 chỗ, nơi diễn ra trận Chung kết) và Sân vận động Container 974 (Ras Abu Aboud). Quá trình cạnh tranh quốc tế, kiểm định kỹ thuật và vượt qua rào cản tiêu chuẩn FIFA.
   - Siêu dự án quốc tế khác: Bảo tàng Khoa học Misk Ilmi (Ả Rập Saudi - 52 triệu USD), Bảo tàng Powerhouse Parramatta (Úc - 9.000 tấn thép), Đường hầm xuyên biển Fehmarnbelt (Đan Mạch - Đức), Dự án tại Indonesia, Nhật Bản, Bắc Mỹ.
   - Lĩnh vực Năng lượng Tái tạo & Điện gió Ngoài khơi (Offshore Wind): Chế tạo thùng hút chân không (Suction Buckets) đường kính 14m, cao 16m, nặng 350 tấn/cấu kiện cho dự án Greater Changhua (Đài Loan); Thỏa thuận hợp tác chiến lược với Copenhagen Infrastructure Partners (CIP - Đan Mạch).

5. Siêu Hạ tầng Trọng điểm Trong nước và Chuỗi Giá trị Công nghiệp:
   - Hạng mục kết cấu thép mái nhà ga Cảng hàng không Quốc tế Long Thành.
   - Nhà ga T3 Cảng hàng không Quốc tế Tân Sơn Nhất, Sân bay Quảng Trị.
   - Mái vòm thép Trung tâm Hội chợ Triển lãm Quốc gia (Cổ Loa, Hà Nội - Nhà triển lãm Kim Quy) quy mô 24.000 tấn thép.
   - Khu liên hợp sản xuất gang thép Hòa Phát Dung Quất 1 & 2; các tổ hợp lọc hóa dầu, nhiệt điện, sân vận động trong nước (Hưng Yên, Trống Đồng).

6. Sức mạnh Tài chính, Thương vụ IFC 38 Triệu USD, Lộ trình IPO và Phân tích Rủi ro Ngành:
   - Vốn điều lệ (~2.000 tỷ VND), tăng trưởng doanh thu (mục tiêu 12.000 tỷ VND năm 2026), giá trị hợp đồng ký mới backlog (>6.650 tỷ VND đầu năm 2026).
   - Chi tiết thương vụ Tổ chức Tài chính Quốc tế (IFC - World Bank Group) rót 38 triệu USD vốn lai (quasi-equity) vào tháng 10/2025 và kế hoạch đầu tư 152 triệu USD cho 2 tổ hợp Nghi Sơn và Vũng Tàu.
   - Kế hoạch IPO năm 2026 và tầm nhìn doanh thu 1 tỷ USD trước 2030.
   - So sánh vị thế cạnh tranh với các đối thủ: ATAD Steel, Zamil Steel, BMB Steel, QH Plus, PTSC M&C, Lilama.
   - Phân tích rủi ro & phản biện: Biến động giá nguyên liệu thép cuộn HRC/thép tấm, cước vận tải biển toàn cầu, áp lực thuế carbon CBAM của EU, rủi ro quản trị dòng tiền khi mở rộng quy mô thần tốc.
```

---

## 2. Danh Sách 12 Chuyên Đề Trích Xuất Chi Tiết (Deep Extraction Roadmap to Vault)

1. **`01_ho_so_nang_luc_va_lich_su_phat_trien_dai_dung.md`**: Hành trình 30 năm phát triển, chân dung nhà sáng lập Trịnh Tiến Dũng, cơ cấu tổ chức và triết lý kinh doanh của Tập đoàn Đại Dũng.
2. **`02_he_thong_6_cum_nha_may_120ha_va_cong_suat_san_xuat.md`**: Chi tiết vị trí, diện tích, công suất thiết kế, máy móc thiết bị của 6 cụm nhà máy (TP.HCM, Long An, Quảng Ngãi, Vũng Tàu, Nghi Sơn).
3. **`03_he_thong_33_chung_chi_quoc_te_aisc_asme_en1090.md`**: Mổ xẻ chi tiết kỹ thuật các chứng chỉ quốc tế: AISC SPE, ASME (U, S, R), EN 1090-1 EXC4, H-Grade, CWB, AS/NZS 5131.
4. **`04_cong_nghe_che_tao_bim_robotics_va_kiem_dinh_ndt.md`**: Công nghệ số hóa BIM Tekla, tự động hóa robot hàn, máy cắt CNC Plasma/Laser, quy trình kiểm định không phá hủy NDT (UT, RT, MPI).
5. **`05_sieu_du_an_world_cup_qatar_lusail_va_974.md`**: Toàn cảnh gói thầu 80 triệu USD tại World Cup Qatar 2022: Thách thức kỹ thuật, khối lượng 34.000 tấn thép, quá trình thi công và ý nghĩa lịch sử.
6. **`06_ha_tang_quoc_gia_san_bay_long_thanh_t3_trien_lam_co_loa.md`**: Các công trình biểu tượng quốc gia: Nhà ga Sân bay Long Thành, T3 Tân Sơn Nhất, Mái vòm Nhà triển lãm Kim Quy Cổ Loa (24.000 tấn thép).
7. **`07_nang_luong_tai_tao_dien_gio_ngoai_khoi_changhua_va_cip.md`**: Năng lực điện gió ngoài khơi: Suction Buckets 350 tấn cho dự án Greater Changhua (Đài Loan), hợp tác với CIP Đan Mạch và triển vọng Quy hoạch Điện VIII.
8. **`08_cac_du_an_quoc_te_saudi_uc_chau_au_fehmarnbelt.md`**: Hồ sơ các dự án xuất khẩu tiêu biểu: Bảo tàng Misk Ilmi (Saudi Arabia - $52M), Bảo tàng Powerhouse Parramatta (Úc), Hầm dìm Fehmarnbelt (Đan Mạch - Đức).
9. **`09_thuong_vu_dau_tu_38m_usd_ifc_va_co_cau_tai_chinh.md`**: Chi tiết thương vụ 38 triệu USD vốn lai (quasi-equity) của IFC (World Bank), cơ cấu vốn điều lệ 2.000 tỷ VND, gói đầu tư 152 triệu USD.
10. **`10_ke_hoach_ipo_2026_va_chien_luoc_doanh_thu_ty_do_2030.md`**: Tình hình tài chính, tốc độ tăng trưởng doanh thu (mục tiêu 12.000 tỷ VND 2026), backlog hợp đồng và lộ trình IPO đưa Đại Dũng thành tập đoàn tỷ USD.
11. **`11_phan_tich_doi_thu_va_vi_the_thi_truong_atad_zamil_ptsc.md`**: Ma trận so sánh vị thế cạnh tranh giữa Đại Dũng vs ATAD Steel, Zamil Steel, BMB Steel, PTSC M&C trong và ngoài nước.
12. **`12_rui_ro_gia_thep_bien_loi_nhuan_va_rao_can_cbam_green_steel.md`**: Phân tích rủi ro biến động giá nguyên liệu thép cuộn HRC, chi phí logistics biển, hàng rào thuế carbon EU CBAM, tiêu chuẩn Thép Xanh và bài toán quản trị dòng tiền.

---

## 3. Cơ Chế Kiểm Soát Dữ Liệu Bắt Buộc (Research Control Checklist)

| TT | Hạng Mục Dữ Liệu / Giả Thuyết Bắt Buộc | Chỉ Tiêu Định Lượng & Nguồn Cần Kiểm Chứng | Trạng Thái Vault Ref |
| :---: | :--- | :--- | :--- |
| 1 | **Quy mô mặt bằng & Công suất** | 120 ha, 6 cụm nhà máy, 500.000 tấn/năm hiện tại $\rightarrow$ 800.000 tấn/năm (2030) | Chờ trích xuất Vault |
| 2 | **Dữ liệu World Cup Qatar 2022** | Gói thầu \$80M, 34.000 tấn kết cấu thép (Lusail Iconic + Sân 974) | Chờ trích xuất Vault |
| 3 | **Hồ sơ Chứng chỉ Kỹ thuật** | AISC SPE, ASME (U/S/R), EN 1090-1 EXC4, H-Grade, CWB, AS/NZS 5131, LEED Gold | Chờ trích xuất Vault |
| 4 | **Dự án Điện gió Ngoài khơi** | Suction Buckets (Đường kính 14m, cao 16m, nặng 350 tấn) tại Greater Changhua; thỏa thuận CIP | Chờ trích xuất Vault |
| 5 | **Hạ tầng Trọng điểm Quốc gia** | Sân bay Long Thành, Nhà ga T3 TSN, Mái vòm Triển lãm Cổ Loa (24.000 tấn) | Chờ trích xuất Vault |
| 6 | **Dữ liệu Đầu tư IFC (World Bank)** | 38 triệu USD vốn lai (quasi-equity), tổng gói đầu tư \$152M (Nghi Sơn 45ha + Vũng Tàu 10ha) | Chờ trích xuất Vault |
| 7 | **Chỉ số Tài chính & Mục tiêu IPO** | Vốn điều lệ ~2.000 tỷ VND, Kế hoạch doanh thu 12.000 tỷ VND (2026), Mục tiêu \$1B trước 2030, Kế hoạch IPO 2026 | Chờ trích xuất Vault |
| 8 | **Rủi ro & Điểm mù Phản biện** | Rủi ro biến động giá HRC/thép tấm, chi phí cước biển, áp lực thuế carbon CBAM EU, biên lợi nhuận ròng | Chờ trích xuất Vault |
