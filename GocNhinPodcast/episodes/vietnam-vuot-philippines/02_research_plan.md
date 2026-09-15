# 02_research_plan.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎭 CHUYÊN GIA: Deep Researcher
📋 PHA: 2 — Data Mining & Verification
🎬 EPISODE: vietnam-vuot-philippines (Góc Nhìn Láng Giềng: Vì Sao Báo Philippines Ví Việt Nam Giống Như "Châu Âu"?)
📂 SKILL: deep_researcher/SKILL.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1. Mục tiêu Nghiên cứu & Xác minh
- Đánh giá thực trạng quy mô kinh tế (GDP), cơ cấu kinh tế (doanh nghiệp nhỏ SMEs vs Tập đoàn gia đình tài phiệt), và các trụ cột tăng trưởng của hai quốc gia Việt Nam và Philippines trong giai đoạn 2025–2026.
- Làm rõ bản chất sự ngưỡng mộ của báo chí Philippines đối với hệ thống giao thông công cộng và xe điện nội địa VinFast tại Việt Nam, đồng thời đối sánh với khó khăn trong chương trình hiện đại hóa xe Jeepney tại nước bạn.
- Thu thập và verify các con số để đảm bảo tính khách quan xây dựng (Steelman) cho cả hai quốc gia, tránh phiến diện một chiều.

---

## 2. Prompt Nạp nguồn Cấu trúc (Structured Ingestion Prompt)
```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu và nguồn thông tin cho các chủ đề sau:

1. So sánh quy mô GDP (danh nghĩa và PPP), tốc độ tăng trưởng kinh tế của Việt Nam và Philippines giai đoạn 2025 - 2026. Các điểm nghẽn và động lực tăng trưởng chính của mỗi quốc gia.
2. Sự thâu tóm của các tập đoàn gia đình tài phiệt (Oligopoly như San Miguel Corporation, SM Investments, Ayala Corporation) đối với nền kinh tế Philippines: Tỷ lệ đóng góp doanh thu vào GDP và ảnh hưởng đến khối doanh nghiệp vừa và nhỏ (SMEs).
3. So sánh mô hình tăng trưởng bao trùm (Inclusive Growth) dựa trên SMEs của Việt Nam vs Mô hình tài phiệt của Philippines.
4. Hiện trạng chương trình hiện đại hóa phương tiện giao thông công cộng tại Philippines (PTMP - Public Transport Modernization Program) và việc thay thế xe Jeepney tính đến giữa năm 2026.
5. Sự hiện diện và hoạt động của thương hiệu xe điện VinFast, hãng taxi Xanh GSM tại Philippines sau khi ra mắt vào tháng 5/2024.
```

---

## 3. Danh sách Câu hỏi Trích xuất tối ưu (Optimized Extraction Queries)

- **Target Chapter: Chương 1 & 2**
  - *Query 1:* Joel Ruiz Butuyan trên tờ Inquirer mô tả chi tiết như thế nào về sự thay đổi của TP.HCM sau 15 năm, đặc biệt về hình ảnh xe điện VinFast, hệ thống xe buýt công cộng và năng lượng làm việc tự doanh của người Việt?
- **Target Chapter: Chương 3 & 4**
  - *Query 2:* GDP danh nghĩa và tốc độ tăng trưởng thực tế của Việt Nam và Philippines trong năm 2025 và dự báo cho năm 2026 là bao nhiêu? Cột mốc hoán đổi ngôi vị xảy ra khi nào?
  - *Query 3:* Tỷ lệ đóng góp doanh thu của tập đoàn San Miguel Corporation (SMC) vào GDP Philippines là bao nhiêu? Sự thống trị của các tập đoàn gia đình (SMIC, Ayala, SMC) ảnh hưởng tiêu cực thế nào đến cơ cấu doanh nghiệp vừa và nhỏ (SMEs) tại nước này?
- **Target Chapter: Chương 5 & 6**
  - *Query 4:* VinFast đã triển khai bán các dòng xe nào (VF3, VF5, VF6, VF7, VF9), phát triển dịch vụ taxi Xanh GSM, chương trình cho thuê xe Rentapasada tại Philippines như thế nào tính đến năm 2025–2026?
  - *Query 5:* Chương trình PTMP (Public Transport Modernization Program) và nỗ lực khai tử xe Jeepney truyền thống tại Philippines đang gặp phải những bế tắc gì về mặt tài chính và xã hội tính đến giữa năm 2026?
  - *Query 6:* Các điểm nghẽn hạ tầng thực tế hiện tại của Việt Nam (tiến độ Metro, ô nhiễm, kẹt xe đô thị) là gì để làm cơ sở phản biện (Counter-thesis) cho bài phát biểu "không khác gì châu Âu"?
- **Target Chapter: Chương 7 & 8**
  - *Query 7:* Doanh thu, quy mô nhân sự và tỷ lệ đóng góp GDP của ngành IT-BPM (BPO) và kiều hối (OFW) đối với nền kinh tế Philippines năm 2025-2026 là bao nhiêu?
