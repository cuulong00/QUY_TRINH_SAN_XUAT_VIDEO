# Kế hoạch Nghiên cứu (Research Plan) - Bức tranh lớn cuộc chiến VinFast vs BYD

## 1. Khung Tuyến Nội Dung (Trajectory Outline)
- Khung tuyến nội dung (outline) chi tiết tại tệp: `trajectory_outline.md`

## 2. Kế hoạch Web Search Căn Bản (Web Search Plan)
**Mục tiêu:** Xác minh các sự kiện, số liệu cập nhật mới nhất (Freshness 2025-2026) về:
- Sức mạnh công nghệ cốt lõi của BYD (Pin Blade, e-Platform 3.0), khả năng tự chủ chuỗi cung ứng từ thâu tóm mỏ khoáng sản (lithium), tự làm chip đến hạm đội tàu chở xe.
- Số liệu về tài chính và các chiến dịch giảm giá (ép giá cực sâu) của BYD bóp nghẹt đối thủ.
- Sự sụp đổ của các hãng xe Nhật tại Thái Lan/Indonesia trước sóng xung kích về giá của BYD.
- Các thỏa thuận BCC của V-Green tại Indonesia (Chargecore, Chargepoint, Amarta Group, CVS).
- Tình hình hoạt động của GSM (Limo Green) tại thị trường Ấn Độ.
- Các dự án điện mặt trời, điện nền của VinEnergo (Philippines, Gia Lai) và vai trò của BESS (đặc biệt là việc tái sử dụng pin xe điện cũ).

## 3. Prompt Nạp nguồn Cấu trúc (Structured Ingestion Prompt Design)
*Sử dụng prompt sau để nạp vào tính năng Deep Research của NotebookLM (1 query duy nhất):*

Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu và nguồn thông tin cho các mảnh ghép sau, đặc biệt chú ý đến các lý thuyết mô hình kinh tế học đằng sau chiến lược của hai hãng:

1. Bức tranh lớn & Sức mạnh Công nghệ - Tài chính khổng lồ của BYD:
- Quy mô doanh thu, lượng tiền mặt dự trữ khổng lồ của BYD năm 2025-2026.
- Sức mạnh công nghệ lõi: Hệ thống pin Blade, nền tảng e-Platform độc quyền, và khả năng tự sản xuất vi mạch (chip).
- **[Lý thuyết Kinh tế] Mô hình Tích hợp dọc (Vertical Integration):** Tìm kiếm minh chứng về *Tích hợp dọc ngược chiều (Backward Integration)* qua việc BYD thâu tóm mỏ Lithium ở châu Phi/Nam Mỹ; và *Tích hợp dọc xuôi chiều (Forward Integration)* qua hạm đội tàu biển tự đóng. Nhờ đó BYD có biên lợi nhuận khổng lồ, tạo ra **Lợi thế nhờ quy mô (Economies of Scale)**.
- **[Lý thuyết Kinh tế] Chiến lược Định giá hủy diệt (Predatory Pricing) / Định giá thâm nhập (Penetration Pricing):** Phân tích cách BYD tận dụng sự tự chủ công nghệ để liên tục phát động chiến tranh giá tàn khốc, đẩy giá xe xuống đáy, bóp nghẹt các đối thủ di sản.
- Triết lý hạ tầng: Mặc dù làm chủ từ A-Z, tại sao BYD kiên quyết đứng ngoài cuộc chơi tự xây dựng trạm sạc công cộng (chuyển rủi ro Capex sang bên thứ ba)?

2. Chiến trường khu vực (Đông Nam Á) & Cứ địa an toàn:
- Dữ liệu thị phần xe điện tại Thái Lan và Indonesia năm 2025-2026. Sự tháo chạy của xe Nhật Bản trước áp lực ép giá tàn khốc của BYD.
- Tính độc quyền của mạng lưới V-Green tại Việt Nam, lý giải theo lý thuyết **Hào hào kinh tế (Economic Moat)**.

3. Các mảnh ghép chiến thuật linh hoạt của VinFast (Micro Tactics):
- **[Lý thuyết Kinh tế] Mô hình Tối giản tài sản (Asset-light Model):** Dữ liệu về mô hình nhượng quyền BCC của V-Green tại Indonesia (xã hội hóa 80% vốn từ đối tác, quy mô 63.000 cổng sạc). Cách mô hình này giải quyết bài toán dòng tiền khổng lồ.
- **[Lý thuyết Kinh tế] Thị trường được bao tiêu (Captive Market):** Chiến lược dùng GSM (Limo Green) thâm nhập Ấn Độ, tạo đầu ra chắc chắn cho nhà máy sản xuất xe và né tránh cuộc chiến giá bán lẻ trực tiếp với BYD.

4. Mảnh ghép "Vòng lặp Năng lượng" từ VinEnergo & Nền Kinh tế tuần hoàn:
- Sự tăng vốn điều lệ của VinEnergo (gần 80.000 tỷ đồng) và các siêu dự án năng lượng: 5GW điện nền tại Philippines, 422MWp điện mặt trời với SunAsia Energy.
- **[Lý thuyết Kinh tế] Mô hình Cán dao & Lưỡi dao (Razor and Blades Business Model) & Hiệu ứng khóa chặt (Lock-in Effect):** Trong cuộc chiến này, chiếc xe điện chỉ là "Cán dao" (phần cứng), còn dòng chảy năng lượng trọn đời của chiếc xe là "Lưỡi dao cạo". Chuỗi giá trị khép kín (VinEnergo -> BESS -> V-Green -> VinFast/GSM) nhằm tối đa hóa **Giá trị vòng đời khách hàng (Customer Lifetime Value - CLV)** và kiểm soát chi phí vận hành trọn đời.
- **[Lý thuyết Kinh tế] Nền kinh tế tuần hoàn (Circular Economy):** Kế hoạch bao tiêu hệ thống pin xe ô tô điện cũ (Second-life EV batteries) của Vingroup để tái sử dụng làm hệ thống lưu trữ điện năng (BESS) cho các nhà máy điện tái tạo và hệ thống trạm sạc của VinEnergo.

## 4. Danh sách Câu hỏi Trích xuất (Batch Extraction Queries List)
*Chạy Batch to Vault sau khi đã nạp đủ nguồn bằng Deep Research:*

1. [Bức tranh lớn & BYD] Hãy cung cấp các số liệu chứng minh sức mạnh công nghệ (Pin Blade, tự chủ chip) của BYD. Áp dụng lý thuyết "Tích hợp dọc" (Vertical Integration - cả ngược và xuôi chiều), hãy phân tích cách BYD thâu tóm chuỗi cung ứng từ mỏ khoáng sản Lithium đến hạm đội chở xe.
2. [Chiến lược Ép giá] BYD đã áp dụng chiến lược "Định giá hủy diệt" (Predatory Pricing) / "Định giá thâm nhập" như thế nào trong giai đoạn 2024-2026? Dựa vào lợi thế "Tích hợp dọc", cấu trúc chi phí của họ chênh lệch bao nhiêu so với các đối thủ để có thể ép giá bóp nghẹt thị trường?
3. [Chiến lược Hạ tầng BYD] Giải thích triết lý đằng sau việc BYD có thể tự chủ từ mỏ quặng đến tàu biển nhưng lại từ chối tự xây dựng hạ tầng trạm sạc (chuyển rủi ro Capex sang bên thứ ba)?
4. [Mặt trận Đông Nam Á] Trước làn sóng "ép giá tận đáy" của BYD tại Thái Lan, Indonesia, các hãng xe Nhật đã sụp đổ ra sao? Nếu VinFast đối đầu trực diện về giá cơ khí với BYD tại đây thì rủi ro là gì?
5. [Chiến thuật V-Green Indonesia] Áp dụng lý thuyết "Mô hình Tối giản tài sản" (Asset-light Model), hãy phân tích cách mô hình BCC của V-Green tại Indonesia (xã hội hóa vốn địa phương) giúp VinFast giải bài toán Capex khổng lồ nhưng vẫn mở rộng thần tốc mạng lưới hạ tầng.
6. [Chiến thuật GSM Ấn Độ] Áp dụng lý thuyết "Thị trường bao tiêu nội bộ" (Captive Market), hãy phân tích vai trò "Con ngựa thành Troy" của hãng taxi GSM tại Ấn Độ giúp VinFast lách qua cuộc chiến giá bán lẻ như thế nào?
7. [Mảnh ghép VinEnergo] Tổng hợp quy mô và chiến lược phát triển toàn cầu của VinEnergo (như các dự án điện nền 5GW tại Philippines, các nước VinFast mở rộng kinh doanh). Năng lượng tái tạo này sẽ hỗ trợ lợi thế cạnh tranh của hệ thống trạm sạc V-Green như thế nào?
8. [Vòng lặp sinh thái & Razor and Blades] Chứng minh luận điểm: BYD dùng "Tích hợp dọc" để kiểm soát giá phần cứng, còn VinFast đang áp dụng mô hình "Cán dao và Lưỡi dao" (Razor and Blades) – dùng chuỗi năng lượng khép kín (VinEnergo -> V-Green -> VinFast) tạo ra "Hiệu ứng khóa chặt" (Lock-in Effect) để kiểm soát trọn đời chi phí vận hành (CLV).
9. [Kinh tế tuần hoàn - Vòng lặp tài chính khép kín] Áp dụng lý thuyết "Kinh tế tuần hoàn" (Circular Economy), hãy phân tích kế hoạch của Vingroup trong việc tạo ra một hệ tuần hoàn tài chính khép kín: Bán xe điện mới -> Cung cấp điện năng di chuyển qua trạm sạc -> Bao tiêu thu hồi hệ thống pin xe điện cũ để làm hệ thống lưu trữ điện năng (BESS) tái tạo. Vòng lặp này tối ưu hóa chi phí cho VinEnergo và gia tăng rào cản xâm nhập như thế nào?
