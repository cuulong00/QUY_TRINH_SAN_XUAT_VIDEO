<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/sieu-cong-trinh-va-bat-com/02_research_plan.md
- Activated Persona: The Socio-Economic Researcher (.agents/personas/the_socio_economic_researcher.md) + The Policy Analyst (.agents/personas/the_policy_analyst.md) + The Industrial Economist (.agents/personas/the_industrial_economist.md)
- Activated Skill: deep-researcher (.agents/skills/deep_researcher/SKILL.md)
- Source Documents Consulted:
  * episodes/sieu-cong-trinh-va-bat-com/01_topic_qualification.md
- Execution Timestamp: 2026-09-11 22:42
-->

# 02_research_plan.md — Kế Hoạch Nghiên Cứu Chuyên Sâu (Deep Research Plan)

## 1. Mục Tiêu & Phạm Vi Nghiên Cứu
* **Đề tài:** Siêu Công Trình Và Bát Cơm Của Bạn: Tấm Vé Hóa Rồng Hay Gánh Nợ Trăm Năm?
* **Mã tập:** `sieu-cong-trinh-va-bat-com`
* **Công cụ cốt lõi:** Direct RPC NotebookLM Engine (`.venv_notebooklm/bin/notebooklm`, `BypassSandbox: true`).
* **Tiêu chuẩn chất lượng:**
  * Bắt buộc sử dụng `--mode deep` và `--import-all`.
  * Quét nạp tối thiểu 20–30 nguồn học thuật, báo cáo bộ ngành (GTVT, KH&ĐT, Tài chính, NHNN), báo cáo tổ chức quốc tế (World Bank, ADB, IMF) và dữ liệu thực chứng 2024–2026.
  * Hoàn thành Batch Extraction 12 chuyên đề vào `research_vault/`.

---

## 2. Hệ Thống 5 Khối Prompt Nạp Nguồn Cấu Trúc (5 Modular Deep Research Prompts)

### 🔹 Khối 1: Địa Kinh Tế Không Gian & "Ly Nông Bất Ly Hương" (Spatial Economics & Decentralization)
```text
Nghiên cứu kinh tế học không gian (Spatial Economics) và tác động của hạ tầng giao thông kết nối liên vùng tại Việt Nam (hệ thống cao tốc Bắc - Nam, các tuyến vành đai đô thị Hà Nội/TP.HCM, cụm cao tốc miền Tây ĐBSCL):
1. Sự thay đổi về thời gian di chuyển, chi phí vận tải liên tỉnh và sự hình thành các hành lang kinh tế mới dọc tuyến.
2. Hiện tượng "ly nông bất ly hương": Tác động của hạ tầng trong việc đưa các khu công nghiệp, cụm công nghiệp về các địa phương nghèo (miền Trung, Tây Nguyên, ĐBSCL), tạo việc làm phi nông nghiệp tại chỗ cho lao động nông thôn, hạn chế làn sóng di cư tự phát lên các siêu đô thị.
3. Phân tích rủi ro kinh tế không gian: Hiện tượng "hiệu ứng hút chân không" (Straw Effect) - khi hạ tầng kết nối nhanh vô tình hút cạn nhân lực, dòng vốn từ các tỉnh nhỏ về đại đô thị trung tâm nếu địa phương không có chiến lược phát triển công nghiệp nội tại.
```

### 🔹 Khối 2: Chuỗi Giá Trị Toàn Cầu & Nâng Cấp Đẳng Cấp "Bát Cơm" (Global Value Chain & Escaping Middle-Income Trap)
```text
Nghiên cứu mối quan hệ giữa hạ tầng chiến lược và năng lực cạnh tranh quốc gia trong việc thu hút dòng vốn FDI chất lượng cao và phát triển công nghiệp phụ trợ tại Việt Nam:
1. Vai trò của Sân bay Quốc tế Long Thành (16 tỷ USD), Cảng trung chuyển quốc tế Cần Giờ, Cảng Lạch Huyện đối với chuỗi cung ứng công nghệ cao (bán dẫn, điện tử, dược phẩm, AI).
2. Phân tích chi phí logistics Việt Nam (hiện ở mức 16-17% GDP): Các điểm nghẽn hạ tầng đa phương thức (đường sắt - đường bộ - cảng biển), tác động của việc giảm chi phí logistics xuống 10-12% GDP đến biên lợi nhuận của doanh nghiệp xuất khẩu và sức cạnh tranh của hàng hóa Việt Nam trên thị trường quốc tế.
3. Tỷ lệ nội địa hóa (DVA) và sự tham gia của các tập đoàn công nghiệp trong nước (thép, cơ khí, xây dựng, công nghệ số) vào các gói thầu siêu dự án: Cơ chế chuyển giao công nghệ hay nguy cơ biến thành "thị trường tiêu thụ máy móc, công nghệ chìa khóa trao tay" cho các nhà thầu ngoại.
```

### 🔹 Khối 3: Hạ Tầng An Ninh Sống Còn (Năng Lượng Nền, Nước Ngọt & Sinh Thái)
```text
Nghiên cứu về hạ tầng năng lượng và sinh thái nền tảng tại Việt Nam giai đoạn 2024-2035:
1. Vai trò của Đường dây 500kV mạch 3 (Quảng Trạch - Phố Nối) trong việc cân đối an ninh năng lượng quốc gia, bài học kinh nghiệm từ cuộc khủng hoảng thiếu điện sản xuất tại miền Bắc mùa hè năm 2023.
2. Quy hoạch Điện VIII, bài toán vốn cho chuyển dịch năng lượng xanh, và chiến lược tái khởi động các dự án Điện hạt nhân (Ninh Thuận 1 và 2) để đảm bảo nguồn điện nền (Baseload Power) phục vụ công nghiệp bán dẫn và trung tâm dữ liệu AI.
3. Các siêu dự án hạ tầng thủy lợi, hồ trữ nước ngọt và cống ngăn mặn tại Đồng bằng sông Cửu Long nhằm ứng phó với biến đổi khí hậu, nước biển dâng và tác động thủy văn từ các dự án thượng nguồn sông Mekong (như Kênh đào Phù Nam Techo của Campuchia).
```

### 🔹 Khối 4: Cơ Chế Tài Khóa, Tiền Tệ & Bảng Cân Đối Quốc Gia (Fiscal & Monetary Transmission)
```text
Nghiên cứu cơ chế tài chính vĩ mô của chiến dịch đầu tư công quy mô lớn tại Việt Nam:
1. Chu trình tiền tệ: Cơ chế giải ngân vốn Kho bạc Nhà nước sang hệ thống ngân hàng thương mại, hệ số nhân tiền tệ (Money Multiplier), cung tiền M2, thanh khoản hệ thống, vòng quay của tiền (Velocity of Money) và nguy cơ lạm phát (lạm phát chi phí đẩy vs lạm phát cầu kéo).
2. Bảng cân đối nợ công và bội chi ngân sách: Đánh giá phương án huy động vốn cho Tuyến đường sắt tốc độ cao Bắc - Nam (67,34 tỷ USD), áp lực trần nợ công, nghĩa vụ trả nợ trực tiếp hàng năm, và rủi ro chi phí bù lỗ vận hành/bảo trì (O&M) sau năm 2035.
3. Cơ chế thu hồi giá trị gia tăng từ đất đai (Land Value Capture) thông qua mô hình phát triển đô thị định hướng giao thông (TOD) quanh các nhà ga, nút giao để tạo nguồn thu bền vững bù đắp chi phí đầu tư công.
```

### 🔹 Khối 5: Lăng Kính Đời Sống Vi Mô & Bài Học Lịch Sử Đối Chiếu (Street-Level Reality & Global Lessons)
```text
Nghiên cứu tác động vi mô của siêu công trình đến đời sống người dân thường và bài học quốc tế:
1. Bát cơm vi mô: Sự phân hóa giàu nghèo qua Hiệu ứng Cantillon (giới đầu cơ đất đai ven dự án vs người lao động trẻ chịu giá nhà tăng phi mã); cú sốc thiếu cát san lấp đẩy giá vật liệu xây dựng dân dụng tăng 50-150%; sinh kế bền vững của nông dân sau khi nhận tiền đền bù đất.
2. So sánh lịch sử: Bài học thành công từ Cao tốc Gyeongbu (Hàn Quốc 1970), Shinkansen (Nhật Bản 1964) và hệ thống cao tốc liên bang Eisenhower (Mỹ thập niên 1950) vs Các bài học cảnh báo về nợ nần và "voi trắng" hạ tầng (Sri Lanka, Hy Lạp 2004, và bài học nợ 850 tỷ USD của China Railway).
3. Điều kiện cần và đủ về thể chế để một quốc gia biến siêu công trình thành đòn bẩy thịnh vượng thay vì chiếc bẫy nợ nần thế hệ.
```

### 🔹 Khối 6: Nghịch Lý Vận Tải Hàng Hóa vs Hành Khách & Phân Phối Thu Nhập Ngược (Freight vs Passenger Dilemma & Regressive Redistribution)
```text
Nghiên cứu phản biện về cơ cấu vận tải của Dự án Đường sắt tốc độ cao Bắc - Nam (67,34 tỷ USD) và tác động kinh tế học xã hội:
1. So sánh cơ cấu vận tải: Tuyến 350km/h thiết kế chủ yếu chở khách (và hàng nhẹ khi cần), nâng cấp tuyến hiện hữu khổ 1.000mm chở hàng. Đánh giá mức độ giải quyết chiếc thòng lọng chi phí logistics hàng hóa 16.8% GDP (vận tải đường bộ gánh 77-80% container, hàng nông sản nặng). Liệu đường sắt cao tốc có giúp hạ giá thành nông sản và thực phẩm dân sinh hay chỉ phục vụ nhu cầu đi lại của hành khách?
2. Khả năng chi trả (Affordability) và độ co giãn cầu theo giá (Price Elasticity of Demand): Giá vé dự kiến bằng khoảng 75% vé máy bay (~1.5 - 1.8 triệu VNĐ). So sánh với thu nhập bình quân của người lao động (6-8 triệu VNĐ/tháng). Tỷ lệ người dân có khả năng tiếp cận thường xuyên.
3. Nguy cơ phân phối thu nhập ngược (Regressive Redistribution): Khi tuyến đường sắt phải bù lỗ vận hành/bảo trì (O&M) hơn 1 tỷ USD/năm từ ngân sách nhà nước (nguồn thu từ thuế toàn dân, gồm cả thuế VAT người nghèo đóng), liệu có xảy ra nghịch lý "người nghèo đóng thuế trợ giá vé cho tầng lớp trung lưu và khá giả đi tàu cao tốc"?
```

### 🔹 Khối 7: Bẫy Đội Vốn, Thiên Kiến Lạc Quan & Rủi Ro Thể Chế (Cost Overruns, Optimism Bias & Megaproject Governance - Bent Flyvbjerg)
```text
Nghiên cứu lý thuyết kinh tế học siêu dự án (Megaprojects) của Giáo sư Bent Flyvbjerg (Đại học Oxford) và bài học thực tiễn tại Việt Nam:
1. Thống kê toàn cầu của Bent Flyvbjerg về "Luật sắt của các siêu dự án" (The Iron Law of Megaprojects: Over budget, over time, under benefits over and over again): 90% siêu dự án bị đội vốn, đường sắt vượt dự toán trung bình 44.7%, lượng khách thực tế thấp hơn 51.4% so với dự báo tiền khả thi.
2. Kiểm toán thực chứng các dự án đường sắt đô thị (Metro) tại Việt Nam: Cát Linh - Hà Đông, Nhổn - Ga Hà Nội, Bến Thành - Suối Tiên (mức độ đội vốn 50-100%, thời gian chậm tiến độ 5-10 năm, nguyên nhân gốc rễ: vướng giải phóng mặt bằng, thay đổi thiết kế, tranh chấp hợp đồng nhà thầu quốc tế EPC, chi phí lãi vay trong thời gian xây dựng IDC).
3. Kịch bản ứng phó rủi ro cho tuyến 67,34 tỷ USD: Nếu dự án bị đội vốn 30-50% (lên 90-100 tỷ USD) hoặc chậm 5 năm, áp lực nợ công, tỷ lệ trả nợ trực tiếp của Chính phủ (vượt trần 25% thu NSNN) và rủi ro tỷ giá (Currency Mismatch khi nhập khẩu công nghệ tàu/tín hiệu bằng ngoại tệ) sẽ ảnh hưởng thế nào đến an toàn tài chính quốc gia?
```

### 🔹 Khối 8: Chi Phí Cơ Hội An Sinh Xã Hội & Hệ Lụy Môi Trường Sinh Thái (Social Infrastructure Crowding-Out & Ecological Externalities)
```text
Nghiên cứu về chi phí cơ hội và ngoại ứng tiêu cực của chiến dịch đầu tư hạ tầng giao thông quy mô lớn tại Việt Nam:
1. Sự chèn ép ngân sách xã hội (Crowding-out of Social Capital): Khi bội chi ngân sách đẩy lên 4.2% - 5% GDP để dồn lực cho hạ tầng cứng (bê tông, sắt thép), ngân sách chi thường xuyên và đầu tư cho hạ tầng mềm (y tế cơ sở, bệnh viện công, trường học công lập, nhà ở xã hội, quỹ an sinh, đào tạo nghề) chịu áp lực cắt giảm hoặc tăng chậm như thế nào? Phân tích sự đánh đổi chi phí cơ hội đối với chất lượng cuộc sống thực tế của người dân.
2. Hệ lụy môi trường sinh thái của cơn đói cát san lấp: Khai thác hàng chục triệu m³ cát sông tại Đồng bằng sông Cửu Long làm hạ thấp đáy sông Tiền, sông Hậu 2-3m, kích hoạt sạt lở bờ sông làm mất nhà cửa, sụt lún đất và kéo mặn xâm nhập sâu hơn vào nội đồng.
3. Rào cản kỹ thuật của việc dùng cát biển thay thế: Nguy cơ ăn mòn cốt thép bê tông, ngấm mặn phá hủy tầng nước ngầm và đất canh tác nông nghiệp xung quanh nếu quy trình xử lý rửa mặn không đạt tiêu chuẩn nghiêm ngặt.
```

---

## 3. Danh Sách 15 Câu Hỏi Trích Xuất Chuyên Sâu (Batch Extraction to Vault)

| STT | File Đích (`research_vault/`) | Câu Hỏi Trích Xuất (Extraction Query) |
|---|---|---|
| 1 | `01_market_making_public_goods.md` | *Bản chất kinh tế học của Hàng hóa công cộng (Public Goods): Tại sao khu vực tư nhân không thể đầu tư các đại hạ tầng mạng lưới? Cơ chế "vốn mồi" và tích lũy tư bản cố định cho quốc gia?* |
| 2 | `02_spatial_economics_decentralization.md` | *Kinh tế học không gian và sự dịch chuyển việc làm: Hạ tầng cao tốc và vành đai giúp phân bổ lại lực lượng lao động thế nào? Hiện tượng 'ly nông bất ly hương' và nguy cơ 'hiệu ứng hút chân không' (Straw Effect)?* |
| 3 | `03_middle_income_trap_fdi_upgrading.md` | *Siêu hạ tầng và bài toán thoát bẫy thu nhập trung bình: Sân bay Long Thành, siêu cảng Cần Giờ/Lạch Huyện đáp ứng những tiêu chuẩn sống còn nào của các tập đoàn bán dẫn, AI và công nghệ cao?* |
| 4 | `04_energy_lifeline_500kv_nuclear.md` | *An ninh năng lượng nền tảng: Đánh giá bài học mất điện mùa hè 2023, vai trò của Đường dây 500kV mạch 3 và chiến lược tái khởi động Điện hạt nhân Ninh Thuận trong việc bảo vệ sản xuất công nghiệp?* |
| 5 | `05_mekong_water_security_phunam.md` | *An ninh nguồn nước và sinh thái Đồng bằng sông Cửu Long: Các siêu dự án cống ngăn mặn, hồ trữ ngọt ứng phó thế nào trước biến đổi khí hậu và tác động của Kênh đào Phù Nam Techo?* |
| 6 | `06_logistics_reduction_16pct_gdp.md` | *Giải phẫu chi phí logistics 16.8% GDP: Tỷ trọng vận tải đường bộ, cấu thành logistics trong giá gạo, rau củ và hàng tiêu dùng; tác động của việc giảm logistics xuống 12% GDP đến giá cả sinh hoạt?* |
| 7 | `07_money_multiplier_m2_liquidity.md` | *Cơ chế truyền dẫn tiền tệ: 700.000 - 800.000 tỷ vốn Kho bạc giải ngân tác động ra sao đến thanh khoản Big 4, hệ số nhân tiền (m), cung tiền M2, lãi suất và rủi ro lạm phát?* |
| 8 | `08_fiscal_debt_railway_67b.md` | *Hồ sơ tài chính Đường sắt tốc độ cao 67.34 tỷ USD: Phương án phân kỳ vốn, tác động đến trần nợ công 60% GDP, nghĩa vụ trả nợ trực tiếp và bài toán bù lỗ vận hành/bảo trì (O&M) sau năm 2035?* |
| 9 | `09_cantillon_effect_land_inequality.md` | *Hiệu ứng Cantillon và bất bình đẳng tài sản: Dòng tiền đền bù đất và hạ tầng mới kích hoạt sốt đất ven đô thế nào? Tác động đến giá thuê trọ, chi phí mua nhà của người lao động trẻ?* |
| 10 | `10_sand_crisis_civil_construction.md` | *Khủng hoảng cát san lấp và vật liệu xây dựng: Nhu cầu đột biến từ các tuyến cao tốc đẩy giá cát, đá tăng 50-150% tác động thế nào đến xây dựng dân dụng và đời sống người dân?* |
| 11 | `11_tod_land_value_capture.md` | *Mô hình phát triển đô thị TOD: Cơ chế thể chế và pháp lý để Nhà nước thu hồi địa tô chênh lệch quanh các nhà ga đường sắt và nút giao cao tốc bù đắp chi phí đầu tư?* |
| 12 | `12_global_precedents_gyeongbu_vs_debt.md` | *Bài học lịch sử quốc tế: Kỳ tích Cao tốc Gyeongbu (Hàn Quốc) và Shinkansen (Nhật Bản) vs Cạm bẫy vỡ nợ Sri Lanka, Hy Lạp và khoản nợ 850 tỷ USD của China Railway?* |
| 13 | `13_freight_vs_passenger_railway_dilemma.md` | *Nghịch lý vận tải hàng hóa vs hành khách của Đường sắt 67 tỷ USD: Tuyến 350km/h chỉ chở khách có giải quyết được chi phí logistics hàng hóa 16.8% GDP? Khả năng chi trả vé tàu và nguy cơ phân phối thu nhập ngược (thuế người nghèo bù lỗ cho người giàu)?* |
| 14 | `14_cost_overruns_optimism_bias_flyvbjerg.md` | *Bẫy đội vốn và thiên kiến lạc quan theo lý thuyết Bent Flyvbjerg: Bài học đội vốn 50-100% của các tuyến Metro tại Việt Nam; kịch bản tài khóa dự phòng nếu dự án 67 tỷ USD đội vốn lên 90-100 tỷ USD và chậm tiến độ?* |
| 15 | `15_social_infrastructure_crowding_out.md` | *Chi phí cơ hội hạ tầng xã hội và hệ lụy sinh thái: Sự chèn ép ngân sách y tế, giáo dục khi dồn lực cho bê tông sắt thép; tác động hạ thấp đáy sông 2-3m, sạt lở bờ sông ĐBSCL do khai thác cát và rủi ro từ cát biển chưa rửa mặn triệt để?* |
