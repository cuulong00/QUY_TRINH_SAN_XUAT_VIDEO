# 02_research_plan.md — Kế Hoạch Deep Research Chuyên Sâu

> **Mục tiêu:** Khai thác toàn diện cơ sở dữ liệu nghiên cứu thông qua **Google NotebookLM Deep Research Engine (`--mode deep --import-all`)** để thu thập dữ liệu định lượng, quy hoạch quốc gia, số liệu cảng biển quốc tế, phân tích chiến lược của các hãng tàu hàng đầu (MSC, Maersk, CMA CGM) và các bài toán kinh tế - địa chính trị đằng sau làn sóng xây dựng siêu cảng biển tại Việt Nam.

---

## 1. Bản Chỉ Dẫn Ingestion Cấu Trúc (Structured Deep Research Ingestion Prompt)
*(Dùng cho lệnh `notebooklm source add-research "<Query>" --mode deep --import-all`)*

```text
Nghiên cứu chuyên sâu toàn diện về chiến lược phát triển hệ thống siêu cảng biển nước sâu và cảng trung chuyển quốc tế của Việt Nam (Why is Vietnam building massive mega-ports?):

Trọng tâm nghiên cứu chuyên sâu gồm 6 trụ cột chính:
1. Động lực kinh tế vĩ mô và Quy hoạch cảng biển quốc gia 2021-2030, tầm nhìn 2050 (Quyết định 1579/QĐ-TTg):
   - Tốc độ tăng trưởng kim ngạch xuất nhập khẩu của Việt Nam (vượt 730–800 tỷ USD), tỷ trọng xuất nhập khẩu/GDP >160-180% (độ mở kinh tế hàng đầu thế giới).
   - Áp lực từ làn sóng dịch chuyển chuỗi cung ứng sản xuất toàn cầu (China+1, Samsung, Foxconn, Apple, Pegatron, BYD, Lego).
   - Mục tiêu năng lực thông qua hệ thống cảng biển: từ 1,14 tỷ đến 1,42 tỷ tấn hàng hóa và 38–47 triệu TEU vào năm 2030.

2. Bài toán chi phí logistics và Lợi thế tàu mẹ trực tiếp (Direct Calls):
   - Phân tích gánh nặng chi phí logistics của Việt Nam: chiếm 16.8% – 18% GDP (so với mức trung bình thế giới 10.7%, Singapore ~8%, Trung Quốc ~14%).
   - Cơ chế kinh tế của tuyến tàu mẹ trực tiếp (Direct mother vessel calls): Tiết kiệm $150 – $300/TEU và rút ngắn 3–5 ngày thời gian vận chuyển đi Bờ Tây/Bờ Đông Hoa Kỳ và Châu Âu so với việc phải dùng tàu gom (feeder) trung chuyển qua Singapore, Hong Kong hay Tanjung Pelepas.
   - Nhu cầu tiếp nhận các siêu tàu container thế hệ mới trọng tải 18.000 – 24.000 TEU (trọng tải đến 250.000 DWT).

3. Dự án Cảng trung chuyển quốc tế Cần Giờ và Ván cược của Tập đoàn Hàng hải MSC:
   - Quy mô vốn đầu tư gần 5 tỷ USD (~129.000 tỷ VNĐ), diện tích 571 ha, chiều dài cầu cảng 7.5 km, công suất tối đa dự kiến 16.9 triệu TEU vào năm 2047.
   - Cơ cấu liên danh: MSC/TIL (Terminal Investment Limited) nắm 49%, VIMC nắm 36%, Cảng Sài Gòn nắm 15%.
   - Chiến lược của MSC: Vì sao hãng tàu lớn nhất thế giới (nắm gần 20% thị phần đội tàu container toàn cầu) chọn Cần Giờ làm "căn cứ điểm" trung chuyển khu vực? Mối liên hệ giữa đội tàu mẹ MSC và nguồn hàng trung chuyển quốc tế (dự kiến chiếm 75–80% sản lượng Cần Giờ).

4. Bản đồ chiến trường hàng hải khu vực & Cuộc đối đầu với Singapore, Malaysia:
   - So sánh năng lực, chi phí, vị trí địa lý với Cảng Tuas (Singapore - siêu cảng 20 tỷ USD, công suất 65 triệu TEU), Port of Tanjung Pelepas (PTP) và Port Klang (Malaysia), Laem Chabang (Thái Lan).
   - Khả năng cạnh tranh nguồn hàng trung chuyển quốc tế: Liệu Việt Nam có thể thu hút nguồn hàng ngoại khối (từ Campuchia, Thái Lan, Philippines, miền Nam Trung Quốc) hay chỉ gom hàng nội địa?
   - Tác động của các dự án địa kinh tế trong khu vực: Kênh đào Funan Techo (Campuchia), đề xuất Landbridge eo đất Kra (Thái Lan).

5. Cấu trúc các cụm cảng trọng điểm Việt Nam và Mối quan hệ tương hỗ / cạnh tranh:
   - Cụm cảng phía Nam: Mối quan hệ giữa Cần Giờ và Cái Mép - Thị Vải (Bà Rịa - Vũng Tàu). Liệu có xảy ra tình trạng "giẫm chân nhau" làm loãng thị phần hay bổ trợ hình thành siêu cụm cảng (super-hub)? Tình trạng di dời và giảm tải cho cảng sông nội thành TP.HCM (Cát Lái, Hiệp Phước).
   - Cụm cảng phía Bắc: Vai trò của Cảng nước sâu Lạch Huyện (Hải Phòng), các bến 1-2, 3-4, 5-6 và cụm cảng Nam Đồ Sơn đối với tam giác kinh tế Hà Nội - Hải Phòng - Quảng Ninh.
   - Cụm cảng miền Trung: Quy hoạch cảng Liên Chiểu (Đà Nẵng), Vân Phong (Khánh Hòa), Quy Nhơn.

6. Các nút thắt hạ tầng, Rủi ro dư thừa công suất và Tranh cãi môi trường:
   - Điểm nghẽn hạ tầng sau cảng (Hinterland connectivity): Sự thiếu hụt hệ thống đường sắt kết nối trực tiếp vào cảng biển; 80% hàng hóa Cái Mép phải phụ thuộc vào sà lan thủy nội địa và đường bộ cao tốc Biên Hòa - Vũng Tàu, Vành đai 3, Vành đai 4.
   - Tranh cãi bảo tồn môi trường: Tác động của dự án Cần Giờ đối với Khu dự trữ sinh quyển Rừng ngập mặn Cần Giờ (UNESCO), bài toán nạo vét luồng hàng hải, bồi lắng và xói lở bờ biển.
   - Xu hướng Chuyển đổi Xanh (Green Port) và Tự động hóa (Smart Port) theo quy chuẩn phát thải ròng bằng 0 (Net Zero 2050) và quy định IMO.
```

---

## 2. Danh Sách 12 Chuyên Đề Trích Xuất Chi Tiết (Deep Extraction Roadmap to Vault)

1. **`01_dong_luc_vi_mo_va_quy_hoach_1579.md`**: Tổng quan động lực kinh tế vĩ mo, kim ngạch XNK, độ mở kinh tế, phân tích chi tiết Quyết định 1579/QĐ-TTg về quy hoạch hệ thống cảng biển quốc gia.
2. **`02_bai_toan_chi_phi_logistics_gdp.md`**: Bóc trần gánh nặng chi phí logistics (16.8%–18% GDP), so sánh quốc tế, cơ chế dòng tiền và bài toán tiết kiệm chi phí qua tuyến tàu mẹ trực tiếp (Direct Calls).
3. **`03_cuoc_chien_cang_trung_chuyen_quoc_te_singapore_malaysia.md`**: Phân tích vị thế trung chuyển quốc tế, đối chiếu với Siêu cảng Tuas (Singapore), Tanjung Pelepas & Port Klang (Malaysia), Laem Chabang (Thái Lan).
4. **`04_lien_minh_hang_tau_va_van_co_msc_can_gio.md`**: Giải mã chiến lược của MSC và TIL, cơ cấu vốn 5 tỷ USD tại Cần Giờ, quyền lực của các liên minh hàng hải toàn cầu (Gemini, Ocean Alliance, MSC Standalone).
5. **`05_cai_mep_thi_vai_va_nghich_ly_ao_tu_nuoc_sau.md`**: Thực trạng cụm cảng nước sâu Cái Mép - Thị Vải, sản lượng hàng hóa, khả năng đón siêu tàu 24.000 TEU, so sánh chức năng giữa Cái Mép và Cần Giờ.
6. **`06_lach_huyen_hai_phong_va_cuc_tang_truong_mien_bac.md`**: Vai trò của cụm cảng Lạch Huyện (Hải Phòng), tiến độ các bến 1 đến 6, phục vụ xuất khẩu công nghệ cao (Samsung, Pegatron, Foxconn) miền Bắc.
7. **`07_lan_song_dich_chuyen_fdi_china_plus_one.md`**: Tác động của làn sóng chuyển dịch chuỗi cung ứng sản xuất toàn cầu sang Việt Nam lên nhu cầu hạ tầng hàng hải và logistics.
8. **`08_ket_noi_ha_tang_sau_cang_duong_sat_va_thuy_noi_dia.md`**: Mổ xẻ điểm nghẽn hạ tầng giao thông sau cảng (Hinterland), tỷ lệ sà lan đường thủy vs đường bộ, dự án đường sắt kết nối cảng biển.
9. **`09_bai_toan_moi_truong_va_rung_ngap_man_can_gio.md`**: Phân tích các đánh giá tác động môi trường (ĐTM), tranh cãi về Khu dự trữ sinh quyển Rừng ngập mặn Cần Giờ (UNESCO) và giải pháp giảm thiểu tác động.
10. **`10_rui_ro_du_thua_cong_suat_va_phan_manh_thi_phan.md`**: Phân tích nguy cơ dư thừa công suất cảng, cạnh tranh hạ giá cước, kịch bản phân chia luồng hàng và các rủi ro đầu tư.
11. **`11_chuyen_doi_cang_xanh_va_tu_dong_hoa_smart_port.md`**: Xu hướng cảng thông minh, cẩu tự động, số hóa thủ tục hải quan, cảng xanh giảm phát thải carbon theo cam kết Net Zero 2050.
12. **`12_tong_hop_so_lieu_dinh_luong_va_so_sanh_quoc_te.md`**: Bảng dữ liệu định lượng tổng hợp toàn diện: Số liệu vốn đầu tư, công suất TEU, chiều sâu luồng, chi phí bốc dỡ, thị phần hãng tàu và chỉ số LPI của Việt Nam vs khu vực.
