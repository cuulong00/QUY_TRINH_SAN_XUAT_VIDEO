# 02_research_plan.md — Kế Hoạch Deep Research Chuyên Sâu (Phiên Bản Mở Rộng Toàn Diện)

> **Mục tiêu:** Nâng cấp toàn diện cơ sở dữ liệu nghiên cứu thông qua hệ thống **Google NotebookLM Deep Research Engine (`--mode deep --import-all`)** để quét sâu các tài liệu chuyên ngành, báo cáo tài chính kiểm toán, kỷ yếu quản trị và các phân tích thể chế về mô hình siêu tập đoàn đa ngành, tốc độ trưởng thành nén thời gian và bánh đà thực chiến của Viettel và Vingroup.

---

## 1. Bản Chỉ Dẫn Ingestion Cấu Trúc (Structured Deep Research Prompt)
*(Dùng cho lệnh `notebooklm source add-research "<Query>" --mode deep --import-all`)*

```text
Nghiên cứu chuyên sâu về mô hình siêu tập đoàn đa ngành, hiện tượng nén thời gian và hệ điều hành thực chiến tại Việt Nam thông qua hai trường hợp điển hình: Tập đoàn Viettel và Tập đoàn Vingroup.

Trọng tâm nghiên cứu chuyên sâu:
1. Tốc độ trưởng thành và hiện tượng "Nén thời gian" (Time-compression phenomenon): 
   - Cơ chế và số liệu chứng minh tốc độ phát triển thần tốc của Viettel: 4 năm (10/2004–10/2008) từ 4.3% lên Top 1 thị phần di động Việt Nam; 15 năm (2009–2024) chuyển dịch từ nhà mạng di động thành tập đoàn công nghệ toàn cầu tự chủ 5G Open RAN lọt Magic Quadrant Gartner, sản xuất chip bán dẫn, radar, khí tài quân sự.
   - Cơ chế và số liệu của Vingroup: 21 tháng xây tổ hợp nhà máy ô tô Cát Hải từ đầm lầy; 5 năm (6/2019–2024) đưa VinFast từ số 0 lên Top 1 toàn thị trường ô tô Việt Nam (>87.000 xe năm 2024); 3 năm (2022–2024) đưa xe điện thuần túy đánh bại toàn bộ các hãng xe xăng truyền thống 30 năm tuổi.
   - So sánh cơ chế "nén thời gian" này với chu kỳ phát triển 30–50 năm của các tập đoàn phương Tây và Chaebol Hàn Quốc (Samsung, Hyundai).
2. Cấu trúc tập đoàn đa ngành và bánh đà hệ sinh thái (Conglomerate Ecosystem Flywheel):
   - Cơ chế trợ lực chéo dòng vốn (cross-financing / cross-subsidization): Dùng dòng tiền mặt khổng lồ từ các mảng "bò sữa" nền tảng (Viễn thông truyền thống của Viettel; Bất động sản dân cư Vinhomes của Vingroup) làm quỹ đầu tư nội bộ tài trợ cho các ngành công nghệ - công nghiệp rủi ro cao, thâm dụng vốn lớn (Thiết bị 5G VHT, Chip; Ô tô điện VinFast, Pin, AI).
   - Cơ chế tự tạo thị trường đầu ra (self-generated demand) và khép kín chuỗi giá trị: Viettel Post (logistics) và Viettel Money (fintech) của Viettel; Hạ tầng trạm sạc V-GREEN, Taxi Xanh SM, Vinmec, Vinschool của Vingroup.
3. Triết lý "Hạ tầng hạng nặng đi trước" (Heavy Infrastructure First):
   - Chiến lược chấp nhận chôn vốn khổng lồ vào hạ tầng vật lý trước khi thị trường bùng nổ: Viettel cắm trạm BTS và kéo cáp quang về từng xã nghèo, biên giới; Vingroup xây dựng mạng lưới hơn 150.000 cổng sạc V-GREEN toàn quốc.
   - Vai trò của hạ tầng như một "con hào kinh tế" (economic moat) tuyệt đối ngăn chặn đối thủ ngoại cạnh tranh.
4. Cỗ máy kỷ luật thực thi triệt để & Bản lĩnh cắt bỏ chi phí chìm:
   - Kỷ luật triệt tiêu sự trì hoãn bàn giấy: Họp nhanh 15–30 phút, báo cáo tối đa 1 trang A4 của Vingroup; Kỷ luật quân đội, không bàn lùi, nhận nhiệm vụ là làm đến cùng của Viettel.
   - Nghệ thuật quản trị chi phí cơ hội và dũng cảm cắt bỏ: Vingroup bán VinMart, đóng Vsmart (12.7% thị phần), dừng xe xăng, tái cấu trúc Asset-light (2026) chuyển giao 182.000 tỷ nợ; Viettel dũng cảm dừng thử nghiệm sai ở cấp xã/huyện ("Dò đá qua sông").
5. Sự hợp tác chiến lược và tương hỗ hệ sinh thái giữa Viettel và Vingroup (2024–2026) trong hạ tầng Cloud AI, siêu máy tính GPU NVIDIA, an ninh mạng và chuyển đổi xanh quốc gia.
```

---

## 2. Danh Sách 12 Chuyên Đề Trích Xuất Chi Tiết (Deep Extraction Roadmap to Vault)

1. **`01_hien_tuong_nen_thoi_gian_va_toc_do_truong_thanh.md`**: Phân tích chi tiết hiện tượng nén thời gian (4 năm của Viettel, 5 năm của VinFast, 21 tháng xây nhà máy) so với chu kỳ 50 năm toàn cầu.
2. **`02_cau_truc_banh_da_he_sinh_thai_da_nganh.md`**: Mổ xẻ cơ chế trợ lực chéo dòng vốn (Cross-Financing) từ Viễn thông/BĐS sang Công nghệ cao (5G/Xe điện) và tự tạo thị trường nội bộ.
3. **`03_triet_ly_ha_tang_hang_nang_di_truoc.md`**: Phân tích con hào kinh tế của hạ tầng vật lý: Mạng lưới trạm BTS/cáp quang Viettel vs. Mạng lưới 150.000 cổng sạc V-GREEN của Vingroup.
4. **`04_co_may_ky_luat_thuc_thi_triet_de.md`**: So sánh cơ chế kỷ luật quân đội "không bàn lùi" và kỷ luật khởi nghiệp hiệu suất "1 trang A4", họp 15 phút.
5. **`05_nghe_thuat_quan_tri_chi_phi_co_hoi_va_cat_bo.md`**: Bài toán bẻ gãy bẫy chi phí chìm: Bán VinMart, đóng Vsmart, dừng xe xăng, Asset-light 2026 vs. Giới hạn thử sai quy mô cấp xã của Viettel.
6. **`06_so_sanh_voi_mo_hinh_chaebol_va_toan_cau.md`**: Đối chiếu mô hình siêu tập đoàn đa ngành Việt Nam với Chaebol Hàn Quốc (Samsung, Hyundai) và Keiretsu Nhật Bản.
7. **`07_su_hop_luc_he_sinh_thai_viettel_vingroup.md`**: Phân tích các thương vụ và thỏa thuận hợp tác chiến lược giữa Viettel và Vingroup (Cloud AI, GPU NVIDIA, trạm sạc, xe điện Xanh SM).
8. **`08_so_lieu_tai_chinh_dinh_luong_toan_dien.md`**: Bảng dữ liệu định lượng về doanh thu, lợi nhuận, quy mô tài sản, đóng góp ngân sách và thị phần của cả 2 tập đoàn giai đoạn 2004–2026.
9. **`09_cac_goc_nhin_phan_bien_va_rui_ro_mo_hinh.md`**: Phân tích rủi ro thâm dụng vốn, rủi ro dàn trải đa ngành, áp lực nợ và thách thức kiệt sức nhân sự (Burnout).
10. **`10_bai_hoc_nen_thoi_gian_cho_ca_nhan.md`**: Chuyển giao Framework "Nén thời gian cá nhân" và "Bánh đà kỹ năng đa nhiệm" cho người đi làm và nhà quản lý.
11. **`11_bai_hoc_quan_tri_ha_tang_va_dong_tien_sme.md`**: Bài học thực chiến cho SME: Cách xây dựng năng lực lõi và quản trị dòng tiền trợ lực chéo.
12. **`12_triet_ly_tro_choi_vo_cuc_va_di_san.md`**: Tầm nhìn quốc gia và ý chí tự lực tự cường Make-in-Vietnam vượt lên trên mục tiêu tài chính thuần túy.
