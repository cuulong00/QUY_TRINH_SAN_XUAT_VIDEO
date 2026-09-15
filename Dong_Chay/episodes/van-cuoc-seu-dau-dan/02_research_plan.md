# Kế hoạch Nghiên cứu Chuyên sâu (02_research_plan.md)
> **Episode:** Ván Cược Sếu Đầu Đàn (Cỗ Xe Song Mã & Cuộc Đại Phẫu Kinh Tế Việt Nam 2026–2045)  
> **Phương pháp:** NotebookLM Direct RPC Deep Research (`--mode deep` & `--import-all`)  
> **Chuyên gia thực hiện:** The Macro Financial Researcher  

---

## I. MỤC TIÊU NGHIÊN CỨU & KHUNG TUYẾN KỊCH BẢN (TRAJECTORY OUTLINE)

Nghiên cứu tập trung giải mã toàn diện và khách quan cơ chế vận hành của chiến lược "Sếu Đầu Đàn" (National Champions) tại Việt Nam giai đoạn 2026–2045, bao gồm:
1. **Nghị quyết 79-NQ/TW (06/01/2026):** Bản chất thể chế, 9 thành tố tài sản công, tiêu chuẩn OECD, cơ chế bảo vệ cán bộ đổi mới sáng tạo.
2. **7 Tập đoàn Nhà nước then chốt (SOEs):** Vai trò giữ hạ tầng, cơ chế chịu đòn hấp thụ sốc lạm phát (EVN, PVN), điểm nghẽn "bảo toàn vốn" và ngoại lệ Viettel (nhà máy chip 27ha Hòa Lạc).
3. **Khối Tập đoàn Tư nhân Tiên phong:** Hòa Phát (thép ray cao tốc Dung Quất 2), Thaco (toa xe Hyundai Rotem & chuỗi Chu Lai), Vingroup (xe điện toàn cầu, VinSpeed), FPT (bán dẫn, AI).
4. **Cơ học Dòng tiền & Rủi ro Hệ thống:** Áp lực đòn bẩy nợ, bức tường đáo hạn, hiệu ứng chèn lấn tín dụng (Crowding-out) đối với 930.000 SME, bẫy ký sinh địa tô.
5. **Đối sánh Quốc tế:** Chaebol Hàn Quốc (1960–1997), SASAC Trung Quốc (Chu Dung Cơ 1998), Temasek Singapore.
6. **Bản Hợp đồng Thể chế Mới:** "Không bảo hộ, không độc quyền", kỷ luật thị trường, cơ chế cộng sinh kéo đàn.

---

## II. STRUCTURED DEEP RESEARCH INGESTION PROMPT (CHO NOTEBOOKLM)

```text
Nghiên cứu chuyên sâu toàn diện về Chiến lược Sếu Đầu Đàn (National Champions) và Cỗ xe song mã Doanh nghiệp Nhà nước (SOE) - Tập đoàn Tư nhân trong tiến trình phát triển kinh tế Việt Nam 2026-2045:

1. Thể chế & Nghị quyết 79-NQ/TW ngày 06/01/2026 của Bộ Chính trị về phát triển kinh tế nhà nước:
- Nội dung cốt lõi, 9 thành tố cấu thành kinh tế nhà nước, mục tiêu 2030 (1-3 DNNN vào Fortune Global 500, 100% áp dụng quản trị OECD) và tầm nhìn 2045.
- Cơ chế tháo gỡ điểm nghẽn "bảo toàn vốn", phân định rủi ro kinh doanh và vi phạm pháp luật, cơ chế bảo vệ cán bộ dám nghĩ dám làm.

2. Tuyến phòng thủ hạ tầng và năng lượng - 7 Tập đoàn Nhà nước chiến lược (EVN, PVN, Viettel, VNPT, MobiFone, Tân Cảng Sài Gòn, Vietcombank):
- Cơ chế trợ cấp ngầm vĩ mô: Tại sao EVN và Petrolimex phải ghìm giá bán dưới giá thành trong bão giá năng lượng toàn cầu để ổn định CPI và hỗ trợ sản xuất FDI/tư nhân.
- Dự án công nghệ cao quốc doanh: Viettel khởi công nhà máy chế tạo chip bán dẫn đầu tiên 27 ha tại Hòa Lạc (tiến trình 32nm, cung cấp chip IoT, viễn thông, quốc phòng, ô tô).

3. Tuyến tiến công công nghiệp của Khối Tư nhân và Siêu dự án đường sắt 67 tỷ USD:
- Hòa Phát: Nhà máy thép ray cao tốc tại Dung Quất 2 (vốn 14.000 tỷ đồng), chuẩn EN 13674, mục tiêu tự chủ ray 350 km/h từ 2027.
- Thaco: Hợp tác Hyundai Rotem chuyển giao công nghệ toa xe metro và cao tốc, hệ sinh thái 1.200 ha Chu Lai với 35 nhà máy vệ tinh.
- Vingroup: VinFast mở rộng thị trường quốc tế, hạ tầng trạm sạc V-Green, VinSpeed tuyến Hà Nội - Quảng Ninh, Trung tâm Hội chợ Triển lãm Cổ Loa.
- FPT: Đào tạo 50.000 kỹ sư bán dẫn và trung tâm AI.

4. Cơ học dòng tiền, Đòn bẩy tài chính và Rủi ro hệ thống (Counter-Thesis & Stress Test):
- Bẫy "Quá lớn để sụp đổ" (Too Big To Fail), áp lực chi phí lãi vay và cấu trúc kỳ hạn nợ của các đại tập đoàn.
- Hiệu ứng chèn lấn tín dụng (Crowding-out effect): Các siêu dự án hút cạn hạn mức tín dụng dài hạn, khiến 930.000 SME và người dân gặp khó khăn tiếp cận vốn rẻ.
- Bẫy ký sinh địa tô: Rủi ro khi dùng dòng tiền bất động sản để tài trợ công nghiệp công nghệ cao và nguy cơ đóng băng thanh khoản.
- Hiện tượng Policy Capture (Lũng đoạn chính sách) và rào cản ngăn đối thủ mới gia nhập thị trường.

5. Bài học quốc tế đối sánh:
- Hàn Quốc: Kỳ tích Chaebol (Samsung, Hyundai) thời Park Chung-hee bằng tín dụng chỉ định, và mặt tối lũng đoạn chính trị, nợ xấu dẫn đến khủng hoảng tài chính châu Á 1997.
- Trung Quốc: Cải cách "Nắm lớn buông nhỏ" của Chu Dung Cơ (1998), mô hình SASAC quản lý 97 tập đoàn trung ương và sở hữu hỗn hợp.
- Singapore: Mô hình Temasek Holdings - phân tách tuyệt đối giữa sở hữu nhà nước và điều hành thị trường, tỷ suất sinh lời thương mại 14-15%/năm.

6. Cơ chế cộng sinh (Spillover Effect) và Kỷ luật thể chế:
- Cách thức sếu đầu đàn tạo mỏ neo đơn hàng cho doanh nghiệp nhỏ (VinFast với 700 nhà thầu, PTSC với 100 nhà thầu chân đế điện gió, Thaco với 150 bộ linh kiện).
- Nguyên tắc "Không bảo hộ, không độc quyền" theo Nghị quyết 79 để tránh bẫy bao cấp và kích hoạt cơ chế đào thải tự nhiên của thị trường.
```

---

## III. DANH SÁCH 10 CÂU HỎI TRÍCH XUẤT CHUYÊN SÂU (BATCH EXTRACTION QUESTIONS)

1. **Q1 (Nghị quyết 79 & Thể chế):** Phân tích chi tiết nội dung, mục tiêu định lượng (2030, 2045) và cơ chế tháo gỡ điểm nghẽn "bảo toàn vốn" trong Nghị quyết 79-NQ/TW của Bộ Chính trị về kinh tế nhà nước.
2. **Q2 (7 SOEs & Cơ chế Trợ cấp Ngầm):** Giải phẫu vai trò của 7 tập đoàn nhà nước trụ cột (EVN, PVN, Viettel, VCB, Tân Cảng...). Cơ chế gánh lỗ vĩ mô của EVN/PVN để ghìm CPI và hỗ trợ FDI vận hành như thế nào?
3. **Q3 (Viettel & Fab Bán dẫn 32nm):** Thông tin chi tiết về nhà máy chế tạo chip bán dẫn 27ha của Viettel tại Hòa Lạc: quy mô vốn, tiến trình công nghệ (32nm), lộ trình 2026–2030 và vai trò đối với chuỗi tự chủ công nghệ quốc gia.
4. **Q4 (Hòa Phát & Thaco trong Đường sắt 67B USD):** Báo cáo chi tiết về dự án thép ray Hòa Phát Dung Quất 2 (14.000 tỷ) và chuyển giao công nghệ toa xe Thaco - Hyundai Rotem: tiến độ, tiêu chuẩn kỹ thuật (EN 13674) và tỷ lệ nội địa hóa.
5. **Q5 (Vingroup & FPT):** Bức tranh toàn cảnh về chiến lược công nghiệp của Vingroup (xe điện toàn cầu, trạm sạc V-Green, VinSpeed) và FPT (AI, bán dẫn). Áp lực tài chính và dòng tiền vận hành ra sao?
6. **Q6 (Rủi ro Đòn bẩy & Too Big To Fail):** Phân tích rủi ro hệ thống của các siêu tập đoàn tư nhân khi sử dụng đòn bẩy tài chính lớn: cấu trúc nợ, chi phí lãi vay hàng ngày, và bài học domino nếu xảy ra đứt gãy thanh khoản.
7. **Q7 (Hiệu ứng Chèn lấn Tín dụng & 930.000 SME):** Cơ chế chèn lấn tín dụng (Crowding-out) diễn ra như thế nào khi các đại tập đoàn hút room tín dụng ngân hàng? Tác động vi mô tới lãi suất vay, doanh nghiệp nhỏ và người dân?
8. **Q8 (Bẫy Ký sinh Địa tô vs Sản xuất Công nghệ):** Phân tích sự xung đột giữa lợi nhuận ngắn hạn từ đầu cơ bất động sản và chi phí đốt vốn dài hạn của công nghiệp công nghệ cao. Rủi ro khi "lấy đất nuôi công nghệ"?
9. **Q9 (Bài học Quốc tế - Chaebol, SASAC, Temasek):** So sánh đối chiếu 3 mô hình: Chaebol Hàn Quốc (kỳ tích & khủng hoảng 1997), SASAC Trung Quốc (Chu Dung Cơ "Nắm lớn buông nhỏ"), và Temasek Singapore (chuẩn mực thị trường).
10. **Q10 (Cơ chế Cộng sinh & Bản hợp đồng 2045):** Các case study thực tế về sự lan tỏa đơn hàng (VinFast 700 nhà thầu, Thaco 150 bộ linh kiện, PTSC 100 thầu phụ) và ý nghĩa của nguyên tắc "Không bảo hộ, không độc quyền".
