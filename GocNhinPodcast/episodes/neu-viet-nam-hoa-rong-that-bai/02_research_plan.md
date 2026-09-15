# 02_research_plan.md

**Episode Slug:** neu-viet-nam-hoa-rong-that-bai
**Notebook URL:** https://notebooklm.google.com/notebook/273397c0-2904-4706-a139-70d4ef045187

---

## 1. Strategic Alignment & Content Strategy (Góc nhìn chiến lược)

### 1.1. Bản chất và Góc nhìn của tập phim
- **Chủ đề chính:** Phân tích hậu quả kinh tế - xã hội nếu Việt Nam thất bại trong mục tiêu trở thành nước phát triển vào năm 2045, từ đó làm sáng tỏ động cơ và tính cấp bách của các chính sách "ép tăng trưởng", tinh gọn bộ máy và tập trung quyền lực hiện nay.
- **Điểm mù của đám đông (Information Gap / Blindspots):** Đa số người dân nhìn thấy chỉ tiêu tăng trưởng kinh tế cao (ví dụ: mục tiêu GDP >10% của Quốc hội cho giai đoạn 2026-2030) hoặc các siêu dự án hạ tầng ($67 tỷ đường sắt tốc độ cao) như những kế hoạch tham vọng mang tính "thành tích". Họ không nhận ra rằng đây là các quyết sách sinh tử bắt buộc để chạy đua với **cửa sổ cơ hội dân số vàng** đang khép lại cực nhanh (chỉ còn khoảng 10-12 năm).
- **Macro-Micro Mapping DNA:**
  - *Vĩ mô:* Bẫy thu nhập trung bình (Middle-Income Trap) và kịch bản già hóa dân số nhanh bậc nhất thế giới. Các cú sốc thuế quan đối ứng toàn cầu (như thuế 20-46% từ Mỹ) và rào cản ESG/GMT làm xói mòn mô hình FDI gia công cũ.
  - *Vi mô:* Đời sống của một người dân trong tương lai "già trước khi giàu": chi phí y tế tăng vọt gấp 7-8 lần, quỹ hưu trí chịu áp lực mất cân đối, người lao động lớn tuổi mất việc làm do công nghệ chế tạo thô sơ bị thay thế, thế hệ trẻ gánh vác tỷ lệ phụ thuộc gấp đôi.
  - *Giải pháp:* Sự thích ứng của chính phủ qua "Nhất thể hóa quyền lực" (Centralized Decision-Making) nhằm giảm chi phí giao dịch nội bộ, loại bỏ tình trạng cát cứ dữ liệu/thẩm quyền, ra quyết định phản ứng nhanh như việc lái xe ở tốc độ cao trên cung đường trơn trượt.

---

## 2. Double-Query Design (Thiết kế câu hỏi hai bước)

### 2.1. Prompt Nạp nguồn Cấu trúc (Structured Ingestion Prompt)
Prompt này sẽ được gửi vào NotebookLM thông qua công cụ `deep_research` để quét web và thu thập tài liệu làm phong phú cơ sở dữ liệu của notebook.

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập và cập nhật đầy đủ thông tin, báo cáo chính thống, số liệu thống kê (giai đoạn 2024-2026) cho các chủ đề sau để lưu vào notebook:

1. Bản chất già hóa dân số và thực trạng tại Việt Nam:
   - Bản chất già hóa dân số là gì và tại sao cả thế giới đều sợ hãi nó (sụt giảm tăng trưởng kinh tế, áp lực tài khóa an sinh xã hội, khủng hoảng y tế toàn cầu).
   - Số liệu GDP đầu người hiện tại (2024-2025) và các mốc ranh giới thu nhập trung bình cao, thu nhập cao theo tiêu chuẩn World Bank.
   - Các nghiên cứu của World Bank, IMF về năng suất lao động Việt Nam và mức đóng góp của TFP (năng suất nhân tố tổng hợp).
   - Tốc độ già hóa dân số Việt Nam: các mốc chuyển đổi dân số già hóa (7% năm 2015) sang dân số già (14% dự báo 2036-2038) và dân số rất già (21% năm 2049-2050). So sánh tốc độ già hóa của Việt Nam với Nhật Bản, Hàn Quốc, Pháp.

2. Case study quốc tế về thành công và thất bại vượt bẫy thu nhập trung bình:
   - Brazil: Phi công nghiệp hóa sớm, thâm hụt tài khóa, bẫy hàng hóa thô (commodity trap).
   - Thái Lan: Già hóa trước khi giàu, bất ổn thể chế và chính trị làm gián đoạn chính sách dài hạn (như Thailand 4.0).
   - Nhóm thất bại (mắc bẫy thu nhập trung bình): 
     - Brazil: Phi công nghiệp hóa sớm, thâm hụt tài khóa, bẫy hàng hóa thô (commodity trap).
     - Thái Lan: Già hóa trước khi giàu, bất ổn thể chế và chính trị làm gián đoạn chính sách dài hạn (như Thailand 4.0).
     - Philippines: Chảy máu chất xám (Brain drain), dựa dẫm vào kiều hối và dịch vụ BPO giá trị thấp, bỏ rơi công nghiệp chế tạo.
   - Nhóm thành công (giàu trước khi già):
     - Hàn Quốc & Đài Loan: Vai trò của nhà nước kiến tạo (Developmental State), đầu tư R&D (Hàn Quốc ~4.8% GDP), phát triển doanh nghiệp mỏ neo dân tộc (Chaebol/TSMC) và viện nghiên cứu ITRI.

3. Áp lực vĩ mô toàn cầu và trong nước năm 2025-2026:
   - Các biến động địa chính trị Trung Đông ảnh hưởng giá năng lượng, cước vận tải logistics đối với Việt Nam.
   - Diễn biến đàm phán thuế đối ứng của Mỹ với Việt Nam (Sắc lệnh 14257 áp thuế 20% và lộ trình đàm phán đưa về 0% theo Sắc lệnh 14346 dựa trên nhập khẩu nông sản/bông từ Mỹ).
   - Khó khăn nội tại của Việt Nam: tắc nghẽn pháp lý bất động sản, rủi ro nợ xấu ngân hàng, sức khỏe suy giảm của doanh nghiệp tư nhân trong nước.

4. Cải cách thể chế và mô hình thích ứng nhanh của Chính phủ Việt Nam:
   - Nghị quyết Quốc hội chốt mục tiêu tăng trưởng GDP bình quân từ 10%/năm trở lên cho giai đoạn 2026-2030.
   - Cuộc cách mạng tinh gọn bộ máy thần tốc: chuyển đổi chính quyền địa phương từ 3 cấp sang 2 cấp (giải thể cấp huyện) trong năm 2025.
   - Phong cách điều hành thực chất, quyết liệt của Thủ tướng Lê Minh Hưng và chiến dịch nâng cao chất lượng cán bộ cơ sở năm 2026.
   - Cơ chế bảo vệ cán bộ dám nghĩ dám làm và Sandbox pháp lý (Regulatory Sandbox) thử nghiệm thể chế.
```

### 2.2. Danh sách Câu hỏi Trích xuất Tối ưu (Optimized Extraction Queries)
Dưới đây là danh sách 10 câu hỏi trích xuất chuyên sâu bám sát tuyến kịch bản, được thiết kế để chạy hàng loạt thông qua `batch_to_vault`. 

1. **[Query 01 - Bản chất già hóa toàn cầu]** "Hãy đóng vai trò chuyên gia nhân khẩu học học thuật. Dựa trên các tài liệu nguồn, hãy trích xuất định nghĩa khoa học và bản chất của hiện tượng già hóa dân số. Giải thích chi tiết tại sao các nền kinh tế phát triển có thu nhập cao (đặc biệt là Nhật Bản, Hàn Quốc, các nước châu Âu - vốn là những quốc gia đã vượt bẫy thu nhập trung bình thành công và giàu trước khi già) đều sợ hãi hiện tượng này. Phân tích cụ thể tác động của nó lên: (a) Tổng cung lao động và sụt giảm GDP dài hạn; (b) Áp lực thâm hụt quỹ hưu trí quốc gia; (c) Sự gia tăng lũy tiến của chi phí y tế và áp lực thuế đè nặng lên lực lượng lao động trẻ."
2. **[Query 02 - Bẫy thu nhập & Già hóa tại VN]** "Hãy đóng vai trò chuyên gia phân tích kinh tế học phát triển. Dựa trên các tài liệu đã nạp, hãy trích xuất toàn bộ dữ liệu định lượng về các mốc chuyển đổi cơ cấu dân số của Việt Nam (2015, 2036-2038, 2049-2050) và so sánh tốc độ già hóa (số năm để tỷ lệ người từ 65 tuổi trở lên tăng từ 7% lên 14%) của Việt Nam với các nước đã giàu trước khi già như Pháp, Nhật Bản, Hàn Quốc. Làm rõ mức GDP đầu người danh nghĩa của Việt Nam tại mốc bắt đầu già hóa (năm 2015) so với các quốc gia trên để chứng minh rủi ro 'chưa giàu đã già'. Đầu ra yêu cầu cấu trúc bảng so sánh chi tiết và dẫn nguồn trích dẫn cụ thể."
3. **[Query 03 - Hậu quả thất bại hóa rồng]** "Dưới góc nhìn xã hội học sắc sảo của một đạo diễn kịch bản tài liệu chuyên sâu, hãy phác họa chi tiết kịch bản xấu nhất (Worst-case scenario) nếu Việt Nam mắc kẹt trong bẫy thu nhập trung bình đến năm 2045 (GDP/đầu người đi ngang ở mức $7,000-$9,000). Hãy bóc tách những hệ lụy cụ thể về: (a) Gánh nặng chi phí y tế và sự bền vững của Quỹ BHXH khi tỷ lệ phụ thuộc tuổi già tăng lên 27.3% vào năm 2040; (b) Sự phân cực của mô hình 'nền kinh tế kép' giữa khối FDI và khối tư nhân nội địa; (c) Bất bình đẳng xã hội và chất lượng sống đô thị suy giảm."
4. **[Query 04 - Thất bại của Thái Lan & Philippines]** "Hãy trích xuất các bài học mắc bẫy thu nhập trung bình từ case study Thái Lan và Philippines. Làm rõ nguyên nhân tại sao Thái Lan bị mắc kẹt ở ngưỡng $7,000-$8,000 GDP/đầu người (tập trung vào mối liên hệ giữa già hóa nhanh trước khi giàu, mất lợi thế chi phí thấp và sự đứt gãy chính sách dài hạn do bất ổn thể chế chính trị). Đối với Philippines, phân tích bẫy kiều hối, chảy máu chất xám (Brain drain) và việc bỏ rơi công nghiệp chế tạo ảnh hưởng thế nào đến năng suất lao động."
5. **[Query 05 - Bài học thành công Hàn Quốc & Đài Loan]** "Hãy trích xuất động lực bứt phá vượt bẫy thu nhập trung bình thành công của Hàn Quốc và Đài Loan trong thập niên 1990. Phân tích chi tiết vai trò của 'Nhà nước kiến tạo phát triển' (Developmental State) trong việc ưu đãi tín dụng gắn liền với hiệu quả xuất khẩu (Hàn Quốc), sự trỗi dậy của các Chaebol nội địa tự chủ công nghệ, tỷ lệ đầu tư R&D (~4.8% GDP), và mô hình Viện ITRI làm mỏ neo công nghệ bán dẫn (Đài Loan)."
6. **[Query 06 - Áp lực vĩ mô & Cơn gió ngược]** "Hãy phân tích chi tiết bối cảnh 'gió ngược' toàn cầu năm 2025-2026 đang ảnh hưởng đến mô hình tăng trưởng của Việt Nam. Trích xuất dữ liệu về: (a) Kịch bản thuế đối ứng của Mỹ dưới chính quyền Trump (từ mức thuế 46% ban đầu xuống mức 20% theo Sắc lệnh 14257 và lộ trình về 0% theo Sắc lệnh 14346); (b) Các rào cản thương mại mới như Thuế tối thiểu toàn cầu (GMT), CBAM của EU; (c) Rủi ro gián đoạn năng lượng (dự trữ xăng dầu chỉ tương đương 25 ngày) khi địa chính trị Trung Đông căng thẳng."
7. **[Query 07 - Điểm nghẽn nội tại]** "Hãy trích xuất các khó khăn nội tại của kinh tế Việt Nam hiện nay, đặc biệt là tình trạng nghẽn thanh khoản và pháp lý thị trường bất động sản lan sang hệ thống ngân hàng (rủi ro nợ xấu). Phân tích sự suy yếu của khu vực doanh nghiệp tư nhân trong nước (kim ngạch xuất khẩu giảm 24.5% trong nửa đầu năm 2026) và khoảng cách công nghệ quá lớn với khối FDI."
8. **[Query 08 - Mệnh lệnh ép tăng trưởng]** "Dựa trên các số liệu toán học vĩ mô, hãy giải thích tại sao Chính phủ Việt Nam bắt buộc phải đặt mục tiêu tăng trưởng GDP bình quân từ 10%/năm trở lên cho giai đoạn 2026-2030. Chứng minh tại sao tăng trưởng cao là 'mệnh lệnh chiến lược' để giải quyết bài toán việc làm (1 triệu người tham gia thị trường lao động mỗi năm), hạ tỷ lệ nợ công/GDP và nợ xấu/GDP bằng cách tăng quy mô mẫu số GDP, và tạo không gian tài khóa đầu tư các dự án hạ tầng nghìn tỷ."
9. **[Query 09 - Nhất thể hóa & Phản ứng nhanh]** "Hãy phân tích mối liên hệ giữa việc 'nhất thể hóa quyền lực' (Centralized decision-making) và năng lực thích ứng nhanh (Agility) của Chính phủ Việt Nam trước các cú sốc toàn cầu. Giải thích cách cơ chế tập trung hóa quyền lực giúp giải quyết các điểm nghẽn hành chính truyền thống: (a) Cát cứ thông tin và thẩm quyền; (b) Tâm lý đùn đẩy trách nhiệm; (c) Quy trình phê duyệt kéo dài. Minh chứng qua các siêu dự án hạ tầng như Đường sắt tốc độ cao Bắc - Nam $67 tỷ và Chiến lược bán dẫn/AI quốc gia."
10. **[Query 10 - Phép ví von Lái xe tốc độ cao]** "Hãy trích xuất và phân tích phép ví von chiến lược 'Lái xe ở tốc độ cao trên cung đường trơn trượt nhiều khúc cua gấp' để mô tả nghệ thuật điều hành vĩ mô của Chính phủ Việt Nam hiện nay. Làm rõ vai trò của hệ thống lái tập trung (nhất thể hóa) giúp phản ứng tức thời, giữ thăng bằng giữa tay lái (định hướng chính trị), chân ga (tài khóa/tiền tệ thúc đẩy tăng trưởng) và chân phanh (ổn định vĩ mô, quản trị lạm phát)."
