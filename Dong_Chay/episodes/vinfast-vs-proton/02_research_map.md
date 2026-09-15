# 02_research_map.md — Bản Đồ Dữ Liệu Nghiên Cứu Chuyên Sâu

**Episode Slug:** `vinfast-vs-proton`  
**Chủ đề:** Giải mã nghịch lý ngành công nghiệp ô tô Đông Nam Á: Tại sao Proton lụi tàn sau 34 năm bảo hộ, và tại sao VinFast buộc phải dấn thân vào canh bạc quy mô toàn cầu?  
**Research Engine:** Direct RPC NotebookLM Deep Research (`--mode deep`)  
**Master Notebook ID:** `375a51fe-e26a-41e2-bc2b-72b9d694269d`  
**Master Notebook URL:** `https://notebooklm.google.com/notebook/375a51fe-e26a-41e2-bc2b-72b9d694269d`  
**Ngày kiểm toán & cập nhật:** 2026-08-26  

---

## 1. Core Question & Research Goal

*   **Core Question (Câu hỏi trung tâm):** Tại sao một hãng xe quốc dân được Nhà nước bảo bọc bằng thuế quan 300% và bơm hơn 15 tỷ Ringgit suốt 34 năm như Proton lại rơi vào cảnh phải bán mình cho doanh nghiệp Trung Quốc; trong khi một hãng xe tư nhân non trẻ như VinFast lại chấp nhận "đốt" hàng tỷ USD, khai tử xe xăng và vươn ra toàn cầu để giải một bài toán sinh tử về toán học quy mô?
*   **Research Goal (Mục tiêu nghiên cứu):** Bóc trần các quy luật kinh tế học công nghiệp (Quy mô tối thiểu MES, Chi phí cận biên, Bẫy bảo hộ thay thế nhập khẩu ISI, Hiệu ứng mạng lưới hạ tầng) để khán giả hiểu rõ bản chất dòng tiền và chiến lược đằng sau hai số phận đối lập của Proton và VinFast.

---

## 2. Verified Data Candidates (Dữ liệu Đã Kiểm Chứng — Thesis Data)

| STT | Luận điểm & Dữ liệu Định lượng | Mốc thời gian | Nguồn chính thống | Vault Ref Pointer |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Proton đạt đỉnh thị phần 74% nhờ bảo hộ thuế quan 300%:** Năm 1993, Proton chiếm 74% thị trường xe du lịch Malaysia dưới sự bảo hộ của thuế nhập khẩu CBU lên tới 300%, giấy phép APs và độc quyền mua sắm công của chính phủ. | 1985–1993 | MITI Malaysia, ResearchGate (Proton Rise & Fall) | `research_vault/01_proton_birth_protectionism.md#L10-L45` |
| 2 | **Proton mua Lotus với giá £51 triệu bảng nhưng không giải được bài toán quy mô:** Thương vụ thâu tóm hãng xe thể thao Anh Quốc năm 1996 để lấy công nghệ "Handling by Lotus" và phát triển động cơ CamPro thất bại do kỹ thuật siêu xe thủ công không thể chuyển giao sang nền tảng xe đại trà giá rẻ. | 1996–2004 | Báo cáo tài chính DRB-HICOM, Lotus Tech Archives | `research_vault/02_proton_lotus_tech_trap.md#L8-L38` |
| 3 | **Hiệp định AFTA kéo sập Proton, nhận hơn 15 tỷ RM tiền trợ cấp/cứu trợ:** Khi thuế quan nội khối ASEAN giảm về 0–5%, thị phần Proton rơi tự do từ 74% xuống 12.5% (2016). Tổng gói tài trợ, ưu đãi thuế và cho vay ưu đãi của chính phủ lên tới hơn 15.15 tỷ Ringgit (~3.5–4 tỷ USD). | 2000–2016 | Bộ Tài chính Malaysia, Báo cáo Quốc hội Malaysia | `research_vault/03_proton_collapse_afta_geely.md#L12-L50` |
| 4 | **Geely hồi sinh Proton bằng nền tảng có sẵn, đổi lấy quyền tự chủ:** Sau khi Geely mua 49.9% cổ phần (2017), việc đưa nền tảng Geely Boyue (Proton X70, X50) giúp thị phần phục hồi lên 18.7% – 26% (2024–2026), nhưng Proton biến thành xưởng gia công xe tay lái nghịch cho Geely. | 2017–2026 | WardsAuto, Báo cáo Geely Holding, Paultan.org | `research_vault/04_geely_turnaround_proton.md#L15-L48` |
| 5 | **VinFast hoàn thành nhà máy 3.5 tỷ USD trong 21 tháng và khai tử xe xăng:** Mua bản quyền BMW 5-Series/X5 (Lux) và GM (Fadil), nhưng chấp nhận khai tử 100% xe xăng vào đầu năm 2022 để chuyển sang xe thuần điện nhằm tránh chi phí bản quyền vô tận và tiêu chuẩn Euro 6. | 2017–2022 | Vingroup Disclosure, Autocar UK, Paultan | `research_vault/05_vinfast_genesis_ice_pivot.md#L10-L42` |
| 6 | **Tăng trưởng bàn giao xe điện phi mã của VinFast:** Bàn giao xe tăng từ ~35.000 xe (2023) lên 97.399 xe (2024) và đạt kỷ lục 196.919 xe (2025, tăng 102% YoY), chiếm ~36% thị phần xe du lịch Việt Nam. | 2023–2025 | Báo cáo tài chính SEC 6-K VinFast Auto Ltd, PR Newswire | `research_vault/06_vinfast_ev_mechanics_scale.md#L12-L40` |
| 7 | **Hào môn trạm sạc V-GREEN và động cơ hấp thụ GSM:** Mạng lưới 150.000 cổng sạc độc quyền V-GREEN tại 63 tỉnh thành tạo rào cản ngăn BYD/Toyota; hãng taxi Xanh SM hấp thụ 25–28% sản lượng xe, ký thỏa thuận cung ứng 1 triệu ô tô điện (2026–2030). | 2023–2026 | V-GREEN Launch Data, SEC Filings VFS, Green SM | `research_vault/07_gsm_vgreen_domestic_engine.md#L8-L45` |
| 8 | **Mệnh lệnh toán học Quy mô Tối thiểu (MES 200.000 – 500.000 xe):** Chi phí dập khuôn và phần mềm ô tô đòi hỏi sản lượng 200k–500k xe/năm để hòa vốn. Thị trường VN chỉ ~400k xe/năm, buộc VinFast phải mở rộng sang Mỹ, Ấn Độ (Tamil Nadu), Indonesia (Subang) để tránh vết xe đổ Proton. | 2024–2026 | Tutor2u Economics (MES), Kazmaier Analysis | `research_vault/08_vinfast_global_expansion_imperative.md#L15-L55` |
| 9 | **Tái cấu trúc "Nhẹ tài sản" (Asset-Light) tháng 5/2026:** VinFast tách và bán 100% mảng sản xuất cơ khí VFTP cho nhóm nhà đầu tư với giá 530 triệu USD, chuyển giao 7.3 tỷ USD (182.000 tỷ VND) nợ sản xuất, giữ lại R&D, phần mềm và quyền khai thác thương hiệu. | Tháng 5/2026 | SEC Form 6-K (12/05/2026), Investify Corporate Analysis | `research_vault/09_macro_economic_mechanisms_comparison.md#L35-L52` |
| 10 | **Dấu ấn cá nhân và cơ chế "Skin-in-the-game" tuyệt đối:** Tỷ phú Phạm Nhật Vượng cam kết tài trợ không hoàn lại 50.000 tỷ VND (~2 tỷ USD) tiền túi đến 2026 (năm 2025 đã giải ngân 23.000 tỷ), trực tiếp làm CEO điều hành toàn cầu; đối lập với cơ chế bổ nhiệm quan chức luân chuyển theo nhiệm kỳ của Proton không ai chịu trách nhiệm tài sản riêng. | 2024–2026 | Vingroup Disclosures, SEC Filings, Paultan, Báo chí Tài chính | `research_vault/MASTER_SYNTHESIS.md#L45-L75` |

---

## 3. Counter-Thesis Data (Dữ liệu Phản biện & Rủi ro Hệ thống — BẮT BUỘC ≥ 3 POINTS)

| STT | Luận điểm Phản biện / Rủi ro Sắc lạnh | Dữ liệu Định lượng Cụ thể | Mối đe dọa thực tế | Vault Ref Pointer |
| :--- | :--- | :--- | :--- | :--- |
| **CT-01** | **Gánh nặng nợ vay và lỗ ròng bào mòn vốn chủ sở hữu:** VinFast lỗ ròng 97.25 nghìn tỷ VND (~3.9 tỷ USD) năm 2025; lỗ lũy kế chạm 171.6 nghìn tỷ VND khiến vốn chủ sở hữu âm hơn 90 nghìn tỷ VND. Nợ ròng duy trì ở mức 9–11 tỷ USD, phụ thuộc lớn vào các gói tài trợ của Vingroup (cho vay 35k tỷ, chuyển đổi 80k tỷ nợ thành cổ phần ưu đãi) và ông Phạm Nhật Vượng (tài trợ 50k tỷ VND). | Lỗ ròng $3.9B (2025), Vốn chủ âm >90k tỷ VND, Nợ ròng âm $6.485B | Rủi ro thanh khoản và áp lực chi phí vốn đè nặng lên tập đoàn mẹ Vingroup. | `research_vault/10_counter_thesis_systemic_risks.md#L14-L24` |
| **CT-02** | **Sự phụ thuộc vào giao dịch nội bộ và thách thức B2C:** Doanh số bán cho hãng taxi GSM chiếm tới 28% tổng lượng xe bán ra năm 2024. Báo cáo Hunterbrook chỉ ra hơn 90% doanh thu 2023 là giao dịch liên kết. Khi thị trường taxi bão hòa, việc bán lẻ trực tiếp (B2C) gặp khó khăn (đăng ký xe mới tại Mỹ giảm 57% tính đến 10/2025 sau các bài đánh giá tiêu cực của MotorTrend/Car&Driver). | GSM chiếm 28% xe (2024), Đăng ký Mỹ giảm 57% (10/2025) | Bẫy dư thừa công suất khi thị trường dịch vụ đạt ngưỡng bão hòa. | `research_vault/10_counter_thesis_systemic_risks.md#L26-L32` |
| **CT-03** | **Cuộc chiến giá rẻ tàn khốc từ Trung Quốc và vỡ trận tại Thái Lan:** Các hãng xe Trung Quốc chiếm 63% thị phần EV Đông Nam Á (Q2/2025). BYD chiếm 80% thị phần NEV tại Philippines. VinFast buộc phải hoãn kế hoạch ra mắt tại Thái Lan vô thời hạn (8/2024) do không chịu nổi cuộc chiến dìm giá; tại Malaysia bị rào cản CIF RM200.000 đẩy giá VF 5 lên RM300.000 (~$70.000). | Hãng Trung Quốc chiếm 63% EV Đông Nam Á; Hủy ra mắt Thái Lan | Nguy cơ bị chèn ép thị phần ngay trên sân nhà Đông Nam Á. | `research_vault/10_counter_thesis_systemic_risks.md#L34-L40` |
| **CT-04** | **Pháp lý tại Mỹ và rủi ro nhà thầu gia công sau tái cấu trúc:** Bang North Carolina kiện VinFast vi phạm tiến độ nhà máy 4 tỷ USD để đòi lại 1.765 mẫu đất sau khi giảm 80% chỉ tiêu tuyển dụng; Mỹ xóa bỏ trợ cấp thuế $7,500. Sau khi bán xưởng VFTP cho Tường Lai (doanh nghiệp bất động sản thiếu kinh nghiệm ô tô), VinFast phụ thuộc 100% vào đơn vị gia công ngoài. | North Carolina kiện tụng; Bỏ trợ cấp $7,500; Tường Lai nắm 95.5% VFTP | Rủi ro gián đoạn chuỗi cung ứng cơ khí và tổn hại pháp lý quốc tế. | `research_vault/10_counter_thesis_systemic_risks.md#L42-L55` |

---

## 4. Macro Mechanisms (Cơ chế Vĩ mô Vận hành — BẮT BUỘC ≥ 5 CƠ CHẾ)

1. **Cơ chế 1: Quy luật Quy mô Tối thiểu (Minimum Efficient Scale - MES) & Chi phí Cố định (Fixed Cost Dilution):**
   * Trong ngành chế tạo ô tô, chi phí R&D, phần mềm và bộ khuôn dập kim loại (stamping dies) tiêu tốn hàng tỷ USD cố định. Nếu sản lượng dưới 200.000 – 300.000 xe/năm, chi phí cố định phân bổ trên mỗi đầu xe sẽ vượt quá giá bán, đẩy doanh nghiệp vào tình trạng lỗ triền miên. Đây là nguyên nhân gốc rễ khiến Proton không thể tồn tại nếu chỉ dựa vào 33 triệu dân Malaysia, và là lý do VinFast bắt buộc phải tìm kiếm thị trường toàn cầu.
2. **Cơ chế 2: Bẫy Ỷ Lại của Chủ nghĩa Bảo Hộ Thay Thế Nhập Khẩu (Import Substitution Trap):**
   * Khi chính phủ dựng hàng rào thuế quan 300% để che chở một "con cưng quốc gia", thị trường bị biến dạng (người dân chịu giá xe đắt gấp 2–3 lần). Doanh nghiệp nội địa mất động lực nâng cấp công nghệ và tối ưu chất lượng. Khi các hiệp định tự do thương mại (như AFTA/ATIGA) có hiệu lực kéo thuế về 0%, bức tường bảo hộ sụp đổ và doanh nghiệp lập tức bị nuốt chửng bởi đối thủ ngoại.
3. **Cơ chế 3: Cơ chế Nhảy Vọt Công Nghệ (Technology Leapfrogging via EV Reset):**
   * Động cơ đốt trong (ICE) đòi hỏi hơn 100 năm tích lũy bằng sáng chế về luyện kim, dung sai cơ khí hộp số và hệ thống trục khuỷu. Việc chuyển sang xe điện (EV) thay thế động cơ nhiệt bằng motor điện, pin Cell-to-Pack và phần mềm điều khiển, xóa bỏ toàn bộ rào cản IP truyền thống, tạo ra "vạch xuất phát phẳng" cho các doanh nghiệp sinh sau đẻ muộn như VinFast.
4. **Cơ chế 4: Hào Môn Hệ Sinh Thái Nội Địa (Infrastructure Moat & Captive Volume Absorption):**
   * Khi không thể dùng thuế quan bảo hộ, một doanh nghiệp tư nhân có thể xây dựng "bảo hộ phi thuế quan" bằng cách độc quyền mạng lưới hạ tầng sạc (V-GREEN) kết hợp với một đội xe tiêu thụ dịch vụ nội bộ (GSM Taxi). Cơ chế này vừa giải quyết bài toán "con gà - quả trứng" của hạ tầng xe điện, vừa đảm bảo công suất hoạt động tối thiểu cho nhà máy trong giai đoạn đầu.
5. **Cơ chế 5: Tách Rời Bảng Cân Đối & Dịch Chuyển Asset-Light (Balance Sheet De-leveraging):**
   * Chế tạo ô tô truyền thống là ngành công nghiệp "nặng tài sản" (Asset-Heavy) với rủi ro khấu hao nhà xưởng đè bẹp dòng tiền. Bằng cách tách riêng đơn vị gia công cơ khí vật lý (VFTP) để chuyển giao nợ sản xuất sang khối tư nhân và chỉ giữ lại phần "não bộ" (R&D, thương hiệu, bản quyền sở hữu trí tuệ, hệ thống phân phối), công ty niêm yết có thể giải phóng bảng cân đối kế toán để thu hút vốn đầu tư công nghệ cao.
6. **Cơ chế 6: Thể Chế Động Lực & Trách Nhiệm Cá Nhân (Governance Agility & Skin-in-the-game vs. Bureaucratic Inertia):**
   * Doanh nghiệp nhà nước / ủy ban (Proton) tiêu tiền ngân sách nên thiếu áp lực sinh tồn trực tiếp; lãnh đạo theo nhiệm kỳ dễ thỏa hiệp, trì hoãn cải tiến (giữ mẫu 23 năm). Ngược lại, doanh nghiệp tư nhân có người sáng lập "đặt cả danh dự và tài sản lên bàn" (VinFast) tạo ra tốc độ ra quyết định vũ bão (xây xưởng 21 tháng, khai tử xe xăng sau 3 năm, tự tài trợ 50k tỷ VND tiền túi) — biến áp lực sinh tử thành động lực đổi mới không ngừng.

---

## 5. Case Study Candidates

*   **Case 1: Proton Saga & Thương vụ Lotus (1985–2004):** Bài học về ảo tưởng chuyển giao công nghệ. Mua một thương hiệu siêu xe thủ công không thể giúp một hãng xe đại trà tạo ra khung gầm giá rẻ có tính cạnh tranh toàn cầu.
*   **Case 2: Cú Bán Mình Cho Geely (2017):** Proton giữ được việc làm cho công nhân Tanjung Malim nhưng vĩnh viễn mất đi vị thế một thương hiệu tự chủ công nghệ quốc gia, biến thành công xưởng cho Geely thâm nhập ASEAN.
*   **Case 3: Cú Khai Tử Xe Xăng Lịch Sử Của VinFast (2022):** Dũng cảm chấp nhận mất trắng chi phí phát triển dòng xe Lux A/SA để dồn 100% nguồn lực cho xe điện, tránh bẫy chi phí bản quyền động cơ BMW.
*   **Case 4: Mô Hình GSM Taxi & Hào Môn V-GREEN (2023–2026):** Công thức nội địa hóa độc đáo giúp VinFast leo lên top 1 thị trường Việt Nam (36% thị phần) mà không cần sự can thiệp của thuế quan hành chính.
*   **Case 5: Cuộc Tái Cấu Trúc 530 Triệu USD Tháng 5/2026:** VinFast bán mảng sản xuất cơ khí vật lý để trút bỏ 7.3 tỷ USD nợ, chuyển dịch sang mô hình tương tự Apple/Foxconn trong ngành ô tô điện.
*   **Case 6 (Global): Soichiro Honda Chống Lại MITI Nhật Bản (1963):** Nhà sáng lập tư nhân đập bàn phản đối quy hoạch cấm làm ô tô của chính phủ để khai sinh ra đế chế xe hơi Honda độc lập.
*   **Case 7 (Global): Canh Bạc Chung Ju-yung & Hyundai Pony (1975):** Nhà sáng lập Hyundai cược toàn bộ gia tài công ty xây dựng để tự chủ công nghệ ô tô khi bị Ford từ chối hợp tác.
*   **Case 8 (Global): Thảm Họa British Leyland (Anh Quốc 1975):** Quốc hữu hóa ngành ô tô bằng tiền ngân sách (>£11 tỷ), quản trị ủy ban đình công và các mẫu xe lỗi khiến toàn bộ ngành ô tô Anh bị xóa sổ quyền tự chủ.
*   **Case 9 (Global): Bẫy Chi Phí Chìm Concorde & Trabant Đông Đức:** Minh chứng kinh điển về sự thất bại kinh tế khi nhà nước đứng ra làm sản phẩm vì thể diện hoặc kế hoạch hóa thiếu cạnh tranh.

---

## 6. Framework Candidates

*   **Framework 1: Minimum Efficient Scale (MES) Curve:** Đường cong chi phí trung bình dài hạn (LRAC) chứng minh tại sao quy mô sản lượng dưới 200.000 xe/năm là bản án tử cho bất kỳ hãng ô tô nào.
*   **Framework 2: Import-Substitution vs. Export-Oriented Leapfrogging:** Đối chiếu giữa tư duy bảo hộ ao làng (Proton) và tư duy bành trướng quy mô toàn cầu (VinFast).
*   **Framework 3: The 3-Layer Moat Matrix:** Hạ tầng trạm sạc (Physical Moat) + Đội xe GSM (Demand Moat) + Phần mềm điều khiển (Software Moat).
*   **Framework 4: Skin-in-the-game & Agility Matrix:** So sánh cơ chế chịu trách nhiệm và tốc độ phản ứng giữa mô hình "Dự án ủy ban nhà nước" (tiền công, rủi ro phân tán) vs "Canh bạc tư nhân của người sáng lập" (tiền túi, rủi ro tuyệt đối).

---

## 7. Weak Zones & Claims to Avoid

*   ❌ **Cấm suy diễn:** Không quy chụp Proton là "hoàn toàn vô giá trị" (họ đã đào tạo nên thế hệ kỹ sư cơ khí đầu tiên cho Malaysia).
*   ❌ **Cấm tung hô một chiều:** Không ca ngợi VinFast như một câu chuyện cổ tích không tì vết; bắt buộc phải nêu rõ rủi ro nợ vay, lỗ ròng 3.9 tỷ USD và áp lực cạnh tranh nghẹt thở từ BYD/Geely.
*   ❌ **Cấm chạm ranh giới pháp lý:** Không kết luận Vingroup/VinFast "vỡ nợ" hay "phá sản", chỉ trình bày trung thực các con số tài chính công khai từ SEC Form 6-K/20-F.
*   ❌ **Cấm tư duy dân tộc cực đoan:** Không kích động thù ghét thương hiệu đối thủ hay dìm hàng quốc gia láng giềng.

---

## 8. Research Verdict: SUFFICIENT (ĐẠT CHUẨN 100%)

Toàn bộ 10 tệp hồ sơ dữ liệu trong `research_vault/` đã được đối chiếu chéo (cross-verified) từ 100 nguồn tài liệu chính thống, báo cáo học thuật, dữ liệu SEC filings và các phân tích thể chế kinh tế. Đủ điều kiện chuyển sang Pha 3 (Strategy Brief).
