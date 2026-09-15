# 02_research_plan.md — so-sanh-dong-co-vinfast-tesla-byd

## 📋 Thông tin Episode
- **Episode Slug:** so-sanh-dong-co-vinfast-tesla-byd
- **Tiêu đề dự kiến:** Nghịch Lý Động Cơ Điện: Tesla Đua Công Nghệ, BYD Tối Ưu Giá, VinFast Chọn Độ Bền?
- **Thời gian hiện tại:** Tháng 07/2026

## 🎯 Chỉ thị Freshness & Bám Sát Dữ Liệu Mới Nhất (Bắt buộc)
> ⚠️ **CẬP NHẬT 2025 - 2026:**
> - Toàn bộ quá trình nghiên cứu bắt buộc phải tập trung thu thập dữ liệu mới nhất (đến thời điểm giữa năm 2026).
> - Tránh tuyệt đối các thông số kỹ thuật thế hệ cũ (ví dụ: các thế hệ động cơ Tesla trước 2023, nền tảng e-Platform 3.0 thế hệ cũ của BYD trước khi nâng cấp lên Evo, hoặc thông tin động cơ VF 8 trước phiên bản All-New nâng cấp).
> - Mọi số liệu kỹ thuật, hiệu suất cơ học, và giải pháp tản nhiệt phải ghi rõ dòng xe, đời xe và năm công bố số liệu.

---

## 1. Prompt Nạp Nguồn Cấu Trúc (Structured Ingestion Prompt)
Prompt này sẽ được gửi tới tính năng Deep Research của NotebookLM để quét và thu thập các tài liệu mới nhất:

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web và thu thập tài liệu kỹ thuật mới nhất (giai đoạn 2025-2026) về hệ thống động cơ truyền động của ba nhà sản xuất xe điện: Tesla, BYD và VinFast:

1. Động cơ điện thế hệ mới của Tesla:
- Thiết kế rotor bọc sợi carbon quấn bằng công nghệ AFP (Automated Fiber Placement) trên Model S Plaid. Chi phí sản xuất và khả năng chịu tải cơ học.
- Động cơ đồng bộ thế hệ mới trên Model Y/Model 3 (đặc biệt dòng động cơ 3D6, 4D1/4D3) sử dụng công nghệ dây quấn stator dẹt Hairpin loại bỏ lớp sơn cách điện đầu dây để làm mát trực tiếp bằng dầu.
- Định hướng phát triển động cơ PMSM/SynRM hoàn toàn không sử dụng đất hiếm (rare-earth free) và vật liệu Ferrite nam châm thế hệ mới.

2. Nền tảng e-Platform 3.0 Evo và Super e-Platform mới nhất của BYD:
- Hệ truyền động điện 8-trong-1 (8-in-1 Powertrain): cơ chế hợp nhất vật lý, hiệu suất hệ thống 89-91%, ưu điểm thu gọn thể tích và rủi ro chi phí sửa chữa thay thế.
- Động cơ tốc độ vòng quay cực cao đạt 23.000 RPM (trên Sealion 7) và 30.511 RPM (trên Super e-Platform). 
- Vật liệu thép silic siêu mỏng 0.2mm làm lõi stator, công nghệ lõi liên kết (Bonded Core Technology) không hàn/tán và hệ thống dây quấn Hairpin dẹt 10 lớp.

3. Hệ truyền động và động cơ PMSM mới nhất của VinFast:
- Động cơ PMSM công suất lớn (150kW - 300kW, mô-men xoắn 620Nm trên VF 8 Plus và VF 9).
- Công nghệ dây quấn stator dẹt Hairpin và hướng đi X-pin chuyển giao công nghệ từ Haosen (quy trình uốn đồng, bóc tách laser, hàn laser và tẩm tĩnh điện).
- Cụm động cơ tích hợp 6-trong-1 (mô-tơ, biến tần, hộp số, OBC, DCDC, PDU) trên các mẫu xe VF 8 thế hệ mới (All-New) và VF 9. 
- Vai trò của đối tác cơ khí ZF (Đức) trong thiết kế bánh răng giảm tốc và vòng bi chịu lực của VinFast.

4. Quản lý nhiệt và Động lực học (So sánh đối chiếu):
- Phương pháp làm mát trực tiếp bằng dầu ATF (Tesla và BYD) qua trục rỗng rotor rỗng so với Hệ thống quản lý nhiệt tích hợp ITM (Integrated Thermal Management) bằng dung dịch nước/glycol tuần hoàn kết nối chéo giữa Pin - Động cơ - Cabin - HVAC của VinFast.
- Tác động của trọng lượng xe lên hiệu năng động cơ: Gigacasting của Tesla (Model Y ~1.8 tấn), Cell-to-Body (CTB) của BYD (Sealion 7 ~2.2 tấn), và khung thép cường lực của VinFast (VF 8 ~2.5 tấn).
```

---

## 2. Danh Sách Câu Hỏi Trích Xuất Tối Ưu (Optimized Extraction Queries)

Dưới đây là 8 câu hỏi tương ứng với 8 chương của kịch bản, được thiết kế để trích xuất dữ liệu sạch và chính xác từ NotebookLM:

### ❓ Câu hỏi 1 (Chương 1)
- **Target Chapter:** Chương 1 - Tiếng Rít Ở Tốc Độ 20.000 Vòng/Phút (Mở đầu & Hiện tượng)
- **Nội dung:** Tìm hiểu bối cảnh và trải nghiệm thực tế về âm thanh của động cơ điện (NVH) so với động cơ đốt trong. Tại sao tốc độ vòng quay cao (15.000 - 30.000 RPM) lại là thách thức vật lý cốt lõi của động cơ EV?
- **Ràng buộc:** Ưu tiên dữ liệu từ năm 2024-2026. Chỉ rõ các dòng xe đạt tua máy lớn.

### ❓ Câu hỏi 2 (Chương 2)
- **Target Chapter:** Chương 2 - Thế Kẹt Của Những Khối Nam Châm (Thách thức cơ học)
- **Nội dung:** Giải thích chi tiết lực ly tâm ở tua máy cao ảnh hưởng thế nào đến các khối nam châm vĩnh cửu trong rotor. So sánh các giải pháp giữ nam châm truyền thống (cầu sắt, titanium, inconel) về tổn hao từ thông và dòng điện xoáy (eddy currents).
- **Ràng buộc:** Cấu trúc thông tin dưới dạng mô tả cơ chế vật lý rõ ràng.

### ❓ Câu hỏi 3 (Chương 3)
- **Target Chapter:** Chương 3 - Tesla và Sợi Carbon Giới Hạn Cực Hạn (Công nghệ Tesla)
- **Nội dung:** Trích xuất chi tiết cấu trúc rotor bọc sợi carbon của Tesla (Model S Plaid): công nghệ quấn AFP, áp lực nén cơ học, khe hở không khí (air gap). Phân tích định hướng thiết kế PMSM không sử dụng đất hiếm (rare-earth free) bằng nam châm Ferrite/từ trở đồng bộ (SynRM) của Tesla tính đến năm 2026.
- **Ràng buộc:** Nêu rõ các bằng sáng chế hoặc công bố chính thức từ Tesla.

### ❓ Câu hỏi 4 (Chương 4)
- **Target Chapter:** Chương 4 - BYD và Cú Bắt Tay Tích Hợp "8 Trong 1" (Công nghệ BYD)
- **Nội dung:** Trích xuất thông tin mới nhất về hệ thống truyền động 8-trong-1 trên e-Platform 3.0 Evo của BYD. Làm thế nào động cơ đạt 23.000 RPM và 30.511 RPM? Cấu trúc stator dùng thép silic 0.2mm, lõi liên kết (Bonded Core) và dây quấn Hairpin 10 lớp mang lại mật độ công suất (kW/kg) cụ thể là bao nhiêu?
- **Ràng buộc:** Cung cấp số liệu chính xác về mật độ công suất (ví dụ: 16.4 kW/kg) và hiệu suất toàn bộ hệ thống.

### ❓ Câu hỏi 5 (Chương 5)
- **Target Chapter:** Chương 5 - VinFast và Lực Vặn Cơ Khí Thực Dụng (Công nghệ VinFast)
- **Nội dung:** Trích xuất thông số động cơ PMSM và cụm truyền động 6-trong-1 trên VF 8 thế hệ mới (All-New). Quy trình sản xuất stator Hairpin/X-pin hợp tác với Haosen và ZF hoạt động thế nào? Mô-men xoắn (620Nm) và công suất (300kW) trên bản Plus đóng vai trò gì?
- **Ràng buộc:** Đưa ra thông tin chính thống về dây chuyền sản xuất tại Hải Phòng và ZF.

### ❓ Câu hỏi 6 (Chương 6)
- **Target Chapter:** Chương 6 - Khi Khung Gầm Gánh Nặng Trọng Lực (Trọng lượng & Động lực học)
- **Nội dung:** So sánh trọng lượng bản thân (Curb Weight) của Tesla Model Y, BYD Sealion 7 và VinFast VF 8. Trọng lượng lớn của VF 8 (gần 2.6 tấn) ảnh hưởng thế nào đến mức tiêu hao năng lượng (Wh/km) và yêu cầu mô-men xoắn của động cơ?
- **Ràng buộc:** Lập bảng so sánh 3 dòng xe, bao gồm: Trọng lượng, Công suất động cơ, Mô-men xoắn, Mức tiêu hao năng lượng thực tế theo kiểm định.

### ❓ Câu hỏi 7 (Chương 7)
- **Target Chapter:** Chương 7 - Cuộc Chiến Tản Nhiệt: Dầu ATF vs Hệ Thống ITM (Tản nhiệt)
- **Nội dung:** So sánh cơ chế làm mát bằng dầu trực tiếp (ATF - qua trục rotor rỗng) của Tesla/BYD với Hệ thống quản lý nhiệt tích hợp (ITM) tuần hoàn dung dịch glycol của VinFast. Làm thế nào ITM kết nối động cơ, pin, cabin và HVAC để tối ưu hóa hiệu suất và nâng cao độ bền của xe?
- **Ràng buộc:** Phân tích điểm mạnh và điểm yếu cơ lý của từng phương pháp.

### ❓ Câu hỏi 8 (Chương 8)
- **Target Chapter:** Chương 8 - Lăng Kính Năng Lượng Đằng Sau Mã Lực (Payoff & Framework)
- **Nội dung:** Đưa ra framework so sánh thực tế cho người dùng: Các tiêu chí chọn xe điện dựa trên triết lý thiết kế truyền động (Hiệu suất & Tốc độ tột cùng, Tích hợp & Tiết kiệm chi phí, hay Bền bỉ lâu dài & Chịu tải lớn).
- **Ràng buộc:** Trình bày rõ ràng, dễ hiểu cho người dùng phổ thông.
