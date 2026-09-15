<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/phan-con-lai-cua-viet-nam/02_research_plan.md
- Activated Persona: the_socio_economic_researcher (.agents/personas/the_socio_economic_researcher.md)
- Activated Skill: deep_researcher (.agents/skills/deep_researcher/SKILL.md), notebooklm (.agents/skills/notebooklm/SKILL.md)
- Master Notebook ID: 82e43dd0-4ffe-4c76-8dca-c865b5a57b87
- Master Notebook URL: https://notebooklm.google.com/notebook/82e43dd0-4ffe-4c76-8dca-c865b5a57b87
- Execution Timestamp: 2026-09-04 22:08
-->

# Kế Hoạch Nghiên Cứu Sâu (Deep Research Plan)
## Episode: Phương Trình 65% — Bức Tranh Toàn Cảnh Cuộc Cách Mạng Kinh Tế Việt Nam 2024–2045

---

### I. PROMPT NẠP NGUỒN CẤU TRÚC (STRUCTURED DEEP RESEARCH INGESTION PROMPT)
*(Dùng cho lệnh `notebooklm source add-research --mode deep --import-all`)*

```text
Nghiên cứu chuyên sâu về lực lượng lao động phi chính thức và khu vực nông thôn trong bối cảnh cuộc cách mạng kinh tế Việt Nam giai đoạn 2024-2045, bao gồm các chủ đề và dữ liệu thực chứng sau:
1. Báo cáo Điều tra Lao động Việc làm của Tổng cục Thống kê (GSO) và Tổ chức Lao động Quốc tế (ILO) giai đoạn 2023-2026: Tỷ lệ lao động có việc làm phi chính thức (64.6%), quy mô tuyệt đối (~33.5 triệu người), cơ cấu ngành nghề, phân hóa theo vùng nông thôn (>80%) và đô thị, khoảng cách thu nhập giữa khu vực phi chính thức và chính thức.
2. Vai trò kinh tế học của khu vực phi chính thức trong mô hình kinh tế nhị nguyên (Arthur Lewis Dual-Sector Model): Cơ chế trợ giá chi phí sinh hoạt (Cost of living), tái sản xuất sức lao động cho các khu công nghiệp và khối FDI, vai trò chiếc van giảm áp hấp thụ khủng hoảng việc làm.
3. Nút thắt chuỗi cung ứng giữa các tập đoàn lớn (Sếu đầu đàn: Viettel, VinFast, Thaco, Hòa Phát...) và hơn 5.2 triệu hộ kinh doanh cá thể tại Việt Nam: Tỷ lệ nội địa hóa (DVA), tình trạng thiếu chuỗi cung ứng phụ trợ Tier 2, Tier 3, phụ thuộc linh kiện nhập khẩu (70-80%).
4. Cuộc đại phẫu thể chế nông nghiệp: Luật Đất đai 2024 (mở rộng hạn mức tích tụ ruộng đất gấp 15 lần), thực trạng già hóa lao động nông nghiệp (tuổi trung bình nông dân 50-70 tuổi), di cư lao động nông thôn - thành thị, nghịch lý bỏ hoang ruộng đất manh mún, mô hình nông nghiệp công nghệ cao và xuất khẩu nông sản (>55 tỷ USD).
5. Mặt trái của kinh tế nền tảng (Gig Economy): Thực trạng tài xế công nghệ, shipper (Grab, Be, ShopeeFood) núp bóng "hợp đồng hợp tác kinh doanh", thiếu bảo hiểm xã hội, rủi ro việc làm ngõ cụt (dead-end gigs) không tích lũy kỹ năng cho thanh niên.
6. Đồng hồ nhân khẩu học và Luật Bảo hiểm Xã hội 2024 (có hiệu lực từ 01/7/2025): Bước ngoặt Lewis (Lewis Turning Point), tốc độ già hóa dân số nhanh hàng đầu thế giới của Việt Nam, quy định trợ cấp hưu trí xã hội tuổi 75 mức 540.000 đồng/tháng, khoảng trống an sinh 15-20 năm của người cao tuổi.
7. Đại chiến lược hạ tầng và phát triển bao trùm (Inclusive Growth): Tác động của Đề án Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD và 5.000km cao tốc đối với việc phân tán công nghiệp về nông thôn ("ly nông bất ly hương"), Đề án 06 về định danh và an sinh số, bài toán nâng cao năng suất TFP để Việt Nam chạm mốc 15.000 USD vào năm 2045.
```

---

### II. DANH SÁCH 10 CÂU HỎI TRÍCH XUẤT CHUYÊN SÂU (OPTIMIZED EXTRACTION QUERIES CHO `research_vault/`)

* **Query 01 (`vault/01_quy_mo_co_cau_phi_chinh_thuc.md`):**  
  Trích xuất số liệu định lượng chi tiết nhất từ GSO và ILO (2023–2026) về quy mô, tỷ lệ lao động phi chính thức tại Việt Nam (toàn quốc, nông thôn, thành thị), cơ cấu ngành nghề, tỷ lệ có hợp đồng lao động và so sánh thu nhập bình quân giữa lao động phi chính thức và chính thức.

* **Query 02 (`vault/02_co_che_tro_gia_ngam_fdi.md`):**  
  Phân tích cơ chế kinh tế học: Làm thế nào khu vực phi chính thức và nguồn lương thực nông thôn đóng vai trò "trợ giá ngầm" cho chi phí sinh hoạt tại các vành đai công nghiệp, giúp các tập đoàn FDI duy trì mức lương cạnh tranh toàn cầu?

* **Query 03 (`vault/03_nut_that_5_trieu_ho_kinh_doanh.md`):**  
  Thực trạng và số liệu về hơn 5,2 triệu hộ kinh doanh cá thể tại Việt Nam: Tỷ trọng đóng góp GDP, rào cản thể chế khiến họ không thể trở thành nhà cung ứng phụ trợ Tier 2, Tier 3 cho các tập đoàn sếu đầu đàn (VinFast, Viettel, Thaco...), nguyên nhân tỷ lệ nội địa hóa thấp.

* **Query 04 (`vault/04_luat_dat_dai_2024_nong_nghiep.md`):**  
  Phân tích tác động của Luật Đất đai 2024 (mở rộng hạn mức chuyển nhượng đất nông nghiệp gấp 15 lần, cơ chế tích tụ đất): Cơ hội và thách thức trong việc chuyển đổi từ nông nghiệp manh mún sang nông nghiệp công nghệ cao, giải quyết việc làm cho nông dân mất đất.

* **Query 05 (`vault/05_gia_hoa_nong_dan_di_cu.md`):**  
  Dữ liệu và phân tích về tình trạng già hóa lao động nông thôn tại Việt Nam: Độ tuổi trung bình của nông dân, dòng di cư lao động trẻ ra đô thị, hiện tượng làng quê "rút ruột", diện tích ruộng đất bỏ hoang và thách thức duy trì kim ngạch xuất khẩu nông sản 55 tỷ USD.

* **Query 06 (`vault/06_bay_lao_dong_gig_economy.md`):**  
  Thực trạng lao động nền tảng (Grab, Be, ShopeeFood...): Quy mô số lượng tài xế/shipper, bản chất pháp lý "đối tác kinh doanh", tình trạng thiếu hụt BHXH/BHYT, rủi ro bào mòn sức khỏe và bẫy triệt tiêu tích lũy kỹ năng công nghiệp của thanh niên.

* **Query 07 (`vault/07_luat_bhxh_2024_khoang_trong_an_sinh.md`):**  
  Phân tích quy định Trợ cấp hưu trí xã hội trong Luật BHXH 2024 (áp dụng từ 01/7/2025): Điều kiện tuổi 75, mức 540.000 đồng/tháng; Thực trạng hơn 70% người già nông thôn không có lương hưu; Khoảng trống an sinh 15-20 năm giữa tuổi nghỉ làm và tuổi hưởng trợ cấp.

* **Query 08 (`vault/08_buoc_ngoat_lewis_demographic_clock.md`):**  
  Phân tích kinh tế học về Bước ngoặt Lewis (Lewis Turning Point) và tốc độ già hóa dân số của Việt Nam: Khi nguồn lao động giá rẻ cạn kiệt, tại sao Việt Nam đối mặt nguy cơ "chưa giàu đã già" nếu không nâng cấp được năng suất TFP của 65% lao động ở chân tháp?

* **Query 09 (`vault/09_sieu_ha_tang_phi_tap_trung_hoa.md`):**  
  Vai trò của Đề án Đường sắt tốc độ cao Bắc - Nam 67 tỷ USD và hệ thống 5.000 km cao tốc đối với kinh tế nông thôn: Cơ chế "phi tập trung hóa công nghiệp", đưa nhà máy về các tỉnh, giải quyết bài toán "ly nông bất ly hương" thay vì dồn ứ dân số về Hà Nội và TP.HCM.

* **Query 10 (`vault/10_phat_trien_bao_trum_muc_tieu_2045.md`):**  
  Tổng hợp khung chính sách Phát triển bao trùm (Inclusive Growth) để Việt Nam vượt bẫy thu nhập trung bình đạt mốc 15.000 USD vào năm 2045: Ứng dụng Đề án 06, bảo hiểm xã hội số linh hoạt, nâng cấp kỹ năng nghề, bài học thành công từ Đông Á (Hàn Quốc, Đài Loan) và bài học thất bại từ Mỹ Latinh.
