# Research Plan — VinfastLamDuocGi

## 1. Structured Ingestion Prompt (Nạp nguồn)
Sử dụng Prompt sau để nạp nguồn bằng công cụ `deep_research`:

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu và nguồn thông tin mới nhất (2025-2026) cho các chủ đề sau:

1. Bức tranh tỷ lệ nội địa hóa 60% đến 84% của VinFast tính đến 2026:
- Chi tiết cấu trúc 60% hiện tại gồm những gì (khung vỏ, dập, hàn, sơn, động cơ điện, hệ thống ADAS/phần mềm).
- Dự án nhà máy cell pin LFP VinES kết hợp với Gotion tại Hà Tĩnh: quy mô, tỷ lệ đóng góp vào mốc 84% nội địa hóa, tiến độ sản xuất thực tế.
- Báo cáo kết quả thử nghiệm an toàn ASEAN NCAP 5 sao của VinFast tại Indonesia hoặc các nước khác và các đánh giá về chất lượng lắp ráp.

2. So sánh cấu trúc chuỗi cung ứng và quyền tự chủ công nghệ xe điện (VinFast vs Tesla vs BYD):
- Module Pin (Heart): Blade Battery của BYD (tự chủ khép kín) vs Tesla (liên doanh Panasonic/mua ngoài) vs VinFast (bắt đầu mua cell/pack, nay tiến lên tự sản xuất cell với đối tác).
- Module Khung gầm & Phần cứng (Body): BYD đúc nguyên khối vs Tesla Gigacasting vs VinFast tự dập, hàn, sơn 100% tại xưởng ở Hải Phòng.
- Module Phần mềm/ADAS (Brain): Tesla FSD khép kín vs BYD đang phát triển vs VinFast tự chủ lõi từ hệ sinh thái Vantix/VinAI và kết hợp đối tác phần cứng.
- Phân tích mô hình "Tích hợp lai" (Hybrid Integration) của VinFast trong việc thu hút vốn FDI chuỗi cung ứng về Việt Nam để làm chủ công nghệ thay vì mua đứt bán đoạn.

3. Tác động kinh tế vĩ mô (Spillover Effect) và Doanh số 2026:
- Hiệu ứng lan tỏa của chuỗi cung ứng VinFast tới các doanh nghiệp vừa và nhỏ (SME) vệ tinh tại Việt Nam (có ví dụ doanh nghiệp thực tế).
- Tác động giữ lại thặng dư GDP của ngành công nghiệp ô tô/cơ khí thay vì lắp ráp đơn thuần.
- Số liệu bán hàng và kỷ lục giao xe vượt mốc 115.000 xe của VinFast trong 6 tháng đầu năm 2026 (chi tiết các mẫu Limo Green, VF3, VF5).
```

## 2. Extraction Queries List (Trích xuất Dữ liệu)
Danh sách các câu hỏi sẽ được trích xuất bằng công cụ `batch_to_vault` sau khi nạp nguồn:

*   **Q1 [Chương 1]:** Cập nhật kết quả đánh giá an toàn ASEAN NCAP 5 sao của VinFast (như tại Indonesia) được truyền thông như thế nào, và dữ liệu thực tế nào phản bác lại định kiến "xe Tàu dán nhãn kém chất lượng"? (Bắt buộc dùng số liệu 2025-2026)
*   **Q2 [Chương 2]:** Trình bày nguyên nhân vĩ mô khiến ngành công nghiệp ô tô Việt Nam trong 30 năm trước chỉ dừng ở mức nội địa hóa 10-20% và thất bại trong việc vươn lên chuỗi giá trị toàn cầu.
*   **Q3 [Chương 3]:** Bóc tách chi tiết 60% giá trị nội địa hóa hiện tại của VinFast. Các xưởng dập, hàn, sơn tại Hải Phòng, hệ thống động cơ điện và hệ thống VCU đóng góp tỷ trọng như thế nào vào con số 60% này?
*   **Q4 [Chương 4-5]:** Phân tích chi tiết dự án nhà máy cell pin LFP VinES - Gotion tại Vũng Áng (Hà Tĩnh). Dự án này quyết định thế nào đến mốc 84% nội địa hóa và quyền tự chủ sinh tử của VinFast?
*   **Q5 [Chương 6]:** Phân tích đối chiếu Module Pin và Module Khung gầm giữa 3 mô hình chiến lược: Tích hợp dọc tuyệt đối (BYD), Tối ưu bằng Gigacasting/Mua ngoài (Tesla) và mô hình hiện tại của VinFast. Ưu nhược điểm của mỗi bên là gì?
*   **Q6 [Chương 7]:** So sánh quyền tự chủ công nghệ phần mềm và ADAS: Cách Tesla phát triển FSD khép kín khác biệt thế nào với cách VinFast làm chủ phần lõi từ VinAI/Vantix và tích hợp đối tác phần cứng?
*   **Q7 [Chương 7]:** Làm rõ mô hình "Tích hợp lai" của VinFast: Họ đã dùng chính sách và lợi thế nào để ép các nhà cung cấp FDI toàn cầu chuyển giao công nghệ và đặt xưởng tại Việt Nam thay vì chỉ mua linh kiện lắp ráp?
*   **Q8 [Chương 8]:** Thống kê số lượng/tên doanh nghiệp SME vệ tinh Việt Nam đang tham gia chuỗi cung ứng VinFast. Hiệu ứng lan tỏa (Spillover Effect) này đóng góp gì vào việc giữ lại thặng dư GDP so với trước đây?
*   **Q9 [Chương 9]:** Bóc tách kỷ lục doanh số giao 115.000 xe của VinFast trong 6 tháng đầu năm 2026. Tỷ trọng các mẫu xe bình dân (VF3, VF5, Limo Green) phản ánh điều gì về mức độ chấp nhận của thị trường nội địa?
