# Kế hoạch Nghiên cứu: Phân tích Quy mô Thị trường & Chiến lược Ma trận của VinFast

## 1. Structured Ingestion Prompt (Prompt Nạp Nguồn - Dùng cho Deep Research cào dữ liệu)
**Lệnh tìm kiếm gốc:**
"Tìm kiếm, trích xuất và tổng hợp các báo cáo thị trường, nghiên cứu vĩ mô uy tín (ưu tiên McKinsey, BMI, VAMA, World Bank, BloombergNEF) về ngành công nghiệp ô tô, xe máy và xe điện (EV) tại Việt Nam, Đông Nam Á (đặc biệt là Indonesia, Philippines) và Ấn Độ giai đoạn 2023-2026. 
Trọng tâm tìm kiếm phải bao phủ 7 góc tiếp cận sau:
1. **Dung lượng thị trường (Market Sizing):** Tổng lượng xe máy đang lưu hành, doanh số bán xe máy/xe máy điện hàng năm, dư địa thị trường ô tô (tỷ lệ sở hữu ô tô/1.000 dân) tại Việt Nam so sánh với các thị trường trọng điểm: Indonesia, Philippines, và Ấn Độ.
2. **Điểm bùng phát hành vi (Motorization):** Động lực kinh tế thúc đẩy tầng lớp trung lưu chuyển đổi từ xe máy sang ô tô cỡ nhỏ (Mini Car, A-SUV). Mức độ nhạy cảm về giá của người tiêu dùng tại các quốc gia đang phát triển này khi ra quyết định mua xe lần đầu.
3. **Cảnh quan Cạnh tranh (Sự đổ bộ của xe điện Trung Quốc):** Tốc độ thâm nhập, chiến lược định giá và thị phần của các hãng xe Trung Quốc (BYD, Wuling, Chery, GAC) tại các thị trường trên.
4. **Hạ tầng Trạm sạc (Infrastructure Moat):** Vai trò của trạm sạc công cộng trong quyết định mua EV. Rào cản phát triển trạm sạc và chính sách trợ cấp của chính phủ tại Indonesia, Philippines, Ấn Độ.
5. **Tác động của Xe dịch vụ (Ride-hailing Impact):** Vai trò của các hãng taxi/gọi xe công nghệ trong việc thúc đẩy và giáo dục thị trường EV. Đồng thời, tìm kiếm các rủi ro về pha loãng thương hiệu (Brand Dilution) hoặc Tự ăn thịt đồng loại (Cannibalization).
6. **Sự "Ngủ đông" của Hãng xe Truyền thống:** Phân tích sự chậm nhịp hoặc chiến lược cố thủ với xe Hybrid của các gã khổng lồ (Toyota, Hyundai, Honda) trong phân khúc thuần điện (BEV) tại Đông Nam Á.
7. **Chu kỳ Vòng đời Sản phẩm (Replacement Cycle):** Thời gian trung bình một người dùng giữ xe trước khi đổi mới (5-7 năm). Tác động của việc "mua xe đầu tiên" đến việc khóa tệp khách hàng trong dài hạn.

## 2. Optimized Extraction Queries (Danh sách Câu hỏi Trích xuất Tối ưu)
*(Tất cả các câu hỏi dưới đây đều đính kèm lệnh kiểm toán cứng: "Ưu tiên dữ liệu mới nhất (2024-2026). Bỏ qua dữ liệu cũ trước 2023 trừ khi cần so sánh lịch sử. Trình bày dưới dạng báo cáo chuyên nghiệp: tiêu đề H2/H3, gạch đầu dòng, bảng biểu. TUYỆT ĐỐI KHÔNG trích xuất văn bản rác, nút share mạng xã hội, hoặc boilerplate website. Chỉ giữ phần lõi nội dung.")*

1. **[Target Chapter 1 & 2] Quy mô mỏ neo xe máy:** Trích xuất dữ liệu về tổng số lượng xe máy đang lưu hành và doanh số bán hàng năm tại Việt Nam. Dữ liệu này chứng minh điều gì về chiến lược "khóa đáy" (phủ xe máy điện Evo/Feliz và VF 3) của VinFast? (Lệnh kiểm toán cứng kèm theo)
2. **[Target Chapter 1] Dư địa chuyển dịch:** Lập bảng so sánh tỷ lệ sở hữu ô tô trên 1.000 dân của Việt Nam so với Thái Lan, Indonesia và Malaysia. Dựa trên GDP per capita hiện tại, dư địa này giải thích thế nào cho chiến thuật rải thảm mọi phân khúc của VinFast? (Lệnh kiểm toán cứng kèm theo)
3. **[Target Chapter 3] Tâm lý học giá cả (Decoy Effect):** Phân tích sự nhạy cảm về giá của người tiêu dùng ô tô lần đầu tại Việt Nam. Việc đặt giá VF 3, VF 5, VF 6 sát nhau chênh lệch 100-200 triệu tận dụng hiệu ứng mỏ neo như thế nào để ép khách hàng "cố thêm chút nữa" thay vì mua xe ngoại? (Lệnh kiểm toán cứng kèm theo)
4. **[Target Chapter 4] Rủi ro dẫm chân phân khúc:** Trích xuất các phân tích về sự chồng chéo tập khách hàng khi định giá xe dịch vụ (Xanh SM) quá sát với xe cá nhân tại thị trường Đông Nam Á. Điều này tàn phá "tín hiệu địa vị" của người mua xe cá nhân như thế nào? (Lệnh kiểm toán cứng kèm theo)
5. **[Target Chapter 7] Chiến lược Tiếm quyền:** Dựa trên các số liệu vĩ mô đã trích xuất, hãy chứng minh bằng dữ liệu rằng: Việc VinFast tung ra 15 mẫu xe, chịu lỗ hàng tỷ USD là một chiến thuật bắt buộc theo mô hình "Spatial Preemption" (Tiếm quyền không gian) để chặn đứng làn sóng xe điện giá rẻ từ Trung Quốc (BYD, Wuling) tại Đông Nam Á. (Lệnh kiểm toán cứng kèm theo)
6. **[Target Bổ trợ: Thị trường Quốc tế] Chiến lược Nhân bản (Indonesia, Philippines, Ấn Độ):** Trích xuất các dữ liệu vĩ mô (quy mô thị trường, thói quen đi xe máy, chính sách trợ cấp, rào cản trạm sạc) tại 3 thị trường: Indonesia, Philippines và Ấn Độ. Sự tương đồng về nhân khẩu học và thói quen tiêu dùng ở các quốc gia này chứng minh thế nào cho khả năng VinFast có thể "rập khuôn" thành công chiến lược khóa đáy (dùng VF 3, VF 5) từ Việt Nam sang các thị trường này? (Lệnh kiểm toán cứng kèm theo)
7. **[Target Ch2 & Ch7] Khoảng trống "Ngủ đông" & Chu kỳ Vòng đời:** Trích xuất các phân tích về sự chậm nhịp hoặc chuyển hướng sang xe lai (Hybrid) của các gã khổng lồ truyền thống (Toyota, Hyundai). Kết hợp với dữ liệu về vòng đời sở hữu một chiếc ô tô trung bình (từ 5-7 năm), hãy chứng minh: Chiến dịch "vơ vét thị phần" thần tốc của VinFast chính là nước cờ lợi dụng Cửa sổ thời gian (Window of Opportunity) này để khóa chặt khách hàng, tước đoạt cơ hội bán hàng của các hãng truyền thống trong suốt một thập kỷ tiếp theo? (Lệnh kiểm toán cứng kèm theo)

## 3. Master Synthesis Prompt (Prompt Tổng Hợp Bức Tranh Toàn Cảnh)
*(Sau khi NotebookLM đã đọc xong toàn bộ báo cáo vĩ mô, chiến lược giá và tài liệu đối thủ, hãy copy-paste toàn bộ nội dung dưới đây vào ô chat của NotebookLM)*

**Lệnh tổng hợp:**
"Dựa trên toàn bộ kho tài liệu đã được nạp vào, hãy đóng vai một Chuyên gia Chiến lược Vĩ mô và Cố vấn Địa chính trị Kinh tế để viết một Báo cáo Tổng hợp (Master Synthesis Report) phân tích chiến lược 'Lấy thịt đè người' (phủ kín ma trận sản phẩm) của VinFast.

Nhiệm vụ của bạn là ghép nối mọi mảnh ghép rời rạc về dữ liệu thị trường, tâm lý học hành vi, chính sách và đối thủ thành một bức tranh nhân quả liền mạch, logic và sinh động. Báo cáo của bạn phải chứng minh được rằng: Cuộc càn quét tung ra 15 mẫu xe và chịu lỗ hàng tỷ USD không phải là sự ngông cuồng, mà là một ván cờ 'Tất tay' mang tính sinh tử, được cấu thành từ 4 trục lõi sau:

1. **Trục Thị trường & Dịch biến:** Kết nối sự tương đồng giữa Việt Nam và Đông Nam Á/Ấn Độ. Hãy phác họa quy mô khổng lồ của 'kỷ nguyên xe máy' đang tiến tới điểm bùng phát chuyển lên ô tô, và giải thích tại sao việc dùng VF 3, VF 5 để 'khóa đáy' thị trường là phát súng vơ vét khách hàng hoàn hảo nhất.
2. **Trục Cạnh tranh & Cửa sổ Thời gian:** Phân tích sự giao thoa lợi ích giữa hai khoảnh khắc: Sự 'ngủ đông' của các gã khổng lồ truyền thống (Toyota, Hyundai bám víu Hybrid) và Chu kỳ vòng đời 5-7 năm của ô tô. Tại sao việc 'bắt cóc' thế hệ mua xe đầu tiên ngay lúc này sẽ khóa chặt cửa quay lại của các hãng Nhật/Hàn?
3. **Trục Phòng ngự & Tiếm quyền Không gian:** Mô tả cách VinFast dùng hào nước 'Trạm sạc V-Green' kết hợp với mật độ phủ sóng dày đặc của 'Xanh SM' (Mere Exposure Effect) để tạo ra bức tường lửa. Bức tường này đè bẹp sự hoài nghi của người dùng nội địa và chặn đứng cuộc đổ bộ của làn sóng xe điện giá rẻ Trung Quốc (BYD, Wuling) như thế nào?
4. **Trục Tâm lý & Giá cả:** Đưa các lý thuyết kinh tế học hành vi (Hiệu ứng Chim mồi - Decoy Effect, Quán tính lựa chọn) vào để phân tích ma trận giá hẹp của VF 3, VF 5, VF 6. Phân tích cách định giá này thao túng tâm lý 'cố thêm chút nữa' của người mua, bẻ gãy mọi nỗ lực so sánh với xe ngoại.

**Yêu cầu văn phong & Khống chế:** 
- KHÔNG liệt kê số liệu thô một cách máy móc, khô khan.
- Giọng văn mang tính điện ảnh, sắc bén, sử dụng các ngôn từ chiến lược (ví dụ: 'cửa sổ thời gian', 'hào quang phòng thủ', 'vơ vét thị phần', 'bắt cóc', 'ngủ đông').
- Cấu trúc chặt chẽ: Phải có sự dẫn dắt nhân quả liên tục từ việc Môi trường vĩ mô -> Thấu hiểu tâm lý -> Ra quyết định sản phẩm -> Bức tử đối thủ."
