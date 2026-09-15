# Kế Hoạch Nghiên Cứu Chi Tiết (Research Plan)

**Episode:** pham-nhat-vuong-tinh-than-dan-toc
**Chuyên gia:** The Socio-Economic Researcher (Nhà Nghiên Cứu Xã Hội Học & Chính Sách Công)
**Ngày:** 2026-07-18

---

## 1. THIẾT KẾ CÂU HỎI NGHIÊN CỨU (Research Questions)

### A. Tầng Vĩ Mô: Chính sách "Quán quân quốc gia" (National Champions) và "Sếu đầu đàn"
1. Nghị quyết 68-NQ/TW (tháng 5/2025) và Kết luận Thường trực Chính phủ tháng 9/2024 định hướng gì về vai trò của các tập đoàn tư nhân lớn?
2. Có những ưu đãi, đường băng chính sách hay cơ chế phối hợp PPP nào được thiết kế cho các dự án hạ tầng lớn như đường sắt tốc độ cao VinSpeed, siêu đô thị Olympic, hay mạng lưới trạm sạc điện V-Green?
3. Đâu là các chi phí cơ hội và rủi ro thâm dụng vốn hệ thống khi dồn lực vào một tập đoàn đầu đàn?

### B. Tầng Cơ Cấu & Doanh Nghiệp: Mô hình "Gia đình làm nền tảng"
1. Chi tiết cơ cấu sở hữu pháp lý, tỷ lệ phần trăm cổ phần của Phạm Nhật Vượng, vợ Phạm Thu Hương và hai con trai (Phạm Quân Anh, Phạm Minh Hoàng) tại GSM VN Holding, VinSpace, VinMetal, VSmart Future là gì?
2. Tiến trình IPO của GSM (Xanh SM) được hoạch định ra sao?
3. Sự khác biệt giữa tài sản đại chúng của Vingroup (VIC) và tài sản gia đình tự nắm giữ tại các mảng chiến lược này có thể tạo ra xung đột lợi ích gì cho cổ đông thiểu số?

### C. Tầng Công Nghệ & AI Vật Lý (Physical AI)
1. Tiến trình phát triển của VinRobotics (nhân sự, đối tác Schaeffler, robot Motion 2 tại CES 2026)?
2. Chi tiết kỹ thuật và mô hình hợp tác OEM của xe tự hành cấp độ 4 (Tensor Robocar, Autobrains)?
3. Phân tích chiến lược bác bỏ mảng sản xuất chip bán dẫn của Phạm Nhật Vượng tại ĐHĐCĐ 2026.

### D. Đối Chiếu Lịch Sử & Thể Chế Học Quốc Tế
1. Mô hình gia tộc kiểm soát của Chaebol (Hàn Quốc) và Keiretsu (Nhật Bản) thời kỳ đầu vận hành thế nào? Có những cơ chế giám sát thể chế gì?
2. So sánh mô hình di sản của Ratan Tata (Tata Trusts sở hữu 66%) vs mô hình gia đình thừa kế của Vingroup.

---

## 2. PROMPT NẠP NGUỒN CẤU TRÚC (Structured Ingestion Prompt)

Chúng ta sẽ sử dụng prompt dưới đây để chạy tính năng Deep Research trên NotebookLM nhằm quét và nạp nguồn tài liệu:

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu, báo cáo tài chính, phân tích chính sách và số liệu thực chứng cho các chủ đề sau:

1. Vai trò "Quán quân quốc gia" (National Champions) và "Sếu đầu đàn" của kinh tế tư nhân Việt Nam:
- Nội dung Nghị quyết 68-NQ/TW (tháng 5/2025) về khu vực tư nhân và cuộc họp Thường trực Chính phủ tháng 9/2024 với Vingroup, Thaco, Hòa Phát.
- Các siêu dự án hạ tầng: Đường sắt tốc độ cao VinSpeed (Siemens Mobility), Cầu vượt biển Cần Giờ - Vũng Tàu, Khu đô thị Thể thao Olympic 925.000 tỷ VND và sân vận động Hùng Vương.
- Mạng lưới trạm sạc V-Green phủ 63 tỉnh thành và nguồn vốn đầu tư.

2. Cấu trúc sở hữu và thế hệ kế thừa F2 của gia tộc Phạm Nhật Vượng:
- Tỷ lệ sở hữu và vốn điều lệ tại GSM VN Holding, VinSpace, VinMetal, VSmart Future (V-App).
- Vai trò điều hành của Phạm Quân Anh (VinMetal) và Phạm Minh Hoàng (VSmart Future).
- Tiến trình IPO GSM (Xanh SM) giai đoạn 2026-2028.

3. Công nghệ và AI Vật lý (Physical AI) của Vingroup:
- Sự phát triển của VinRobotics (đối tác Schaeffler), xe tự hành cấp 4 Tensor Robocar (hợp tác Autobrains, chip Nvidia).
- Sovereign Cloud, LLM 420 tỷ token phục vụ Nghị định 53 về an ninh mạng dữ liệu.
- Tuyên bố của Phạm Nhật Vượng về việc không tự sản xuất chip bán dẫn tại ĐHĐCĐ 2026.

4. Mô hình đối sánh quốc tế:
- So sánh Chaebol Hàn Quốc, Keiretsu Nhật Bản, Reliance Industries (Ấn Độ) và mô hình quỹ tín thác Tata Trusts của tập đoàn Tata.
```

---

## 3. DANH SÁCH CÂU HỎI TRÍCH XUẤT (Extraction Queries)

Khi NotebookLM hoàn thành deep research, chúng ta sẽ chạy 9 câu hỏi trích xuất chuyên sâu sau vào thư mục `research_vault/`:

1. **q1_national_champion_policy:** Chính sách "Quán quân quốc gia" của Việt Nam (Nghị quyết 68, họp Chính phủ 2024) và sự định vị dành cho Vingroup.
2. **q2_infrastructure_projects:** Chi tiết quy hoạch, tổng mức đầu tư và vai trò của Vingroup trong các siêu dự án hạ tầng (VinSpeed, cầu Cần Giờ, siêu đô thị Olympic).
3. **q3_family_ownership_structure:** Chi tiết tỷ lệ cổ phần, vốn điều lệ và ban quản trị của gia đình PNV tại GSM VN Holding, VinSpace, VinMetal, VSmart Future.
4. **q4_generational_succession:** Vai trò, vị trí điều hành của thế hệ F2 (Phạm Quân Anh, Phạm Minh Hoàng) và kịch bản chuyển giao di sản.
5. **q5_physical_ai_robotics:** Tiến trình R&D AI vật lý, VinRobotics, đối tác Schaeffler và robot Motion 2.
6. **q6_autonomous_vehicles:** Chi tiết kỹ thuật, đối tác Autobrains và mô hình sản xuất OEM của xe tự hành Tensor Robocar cấp độ 4.
7. **q7_data_sovereignty_cloud:** Mạng lưới dữ liệu, Sovereign Cloud (Nghị định 53), LLM 420 tỷ token và ứng dụng V-App.
8. **q8_semiconductor_strategy:** Phân tích chiến lược từ chối tự làm chip bán dẫn của Phạm Nhật Vượng tại ĐHĐCĐ 2026.
9. **q9_international_comparisons:** Đối chiếu chi tiết thể chế và mô hình di sản của Vingroup với Chaebol Hàn Quốc, Keiretsu Nhật Bản và Tata Trusts.
