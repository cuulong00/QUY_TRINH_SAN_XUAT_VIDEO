<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/lap-nghiep-phu-quoc/02_research_map.md
- Activated Persona: The Socio-Economic Researcher (.agents/personas/the_socio_economic_researcher.md) & The Industrial Economist (.agents/personas/the_industrial_economist.md)
- Activated Skill: Deep Researcher (.agents/skills/deep_researcher/SKILL.md)
- Source Documents Consulted:
  * episodes/lap-nghiep-phu-quoc/research_vault/01_living_costs_and_island_tax.md
  * episodes/lap-nghiep-phu-quoc/research_vault/02_commercial_rental_market.md
  * episodes/lap-nghiep-phu-quoc/research_vault/03_labor_market_wages_and_benefits.md
  * episodes/lap-nghiep-phu-quoc/research_vault/04_seasonal_monsoon_impact.md
  * episodes/lap-nghiep-phu-quoc/research_vault/05_all_inclusive_resorts_vs_local_smbs.md
  * episodes/lap-nghiep-phu-quoc/research_vault/06_b2b_and_supply_chain_opportunities.md
  * episodes/lap-nghiep-phu-quoc/research_vault/07_permanent_resident_services_2040.md
  * episodes/lap-nghiep-phu-quoc/research_vault/08_institutional_legal_framework.md
  * episodes/lap-nghiep-phu-quoc/research_vault/09_international_island_benchmarks.md
  * episodes/lap-nghiep-phu-quoc/research_vault/10_steelman_audit_and_survival_playbook.md
  * episodes/lap-nghiep-phu-quoc/vault/00_tham_chieu_3_tap_truoc.md
- Execution Timestamp: 2026-09-05 13:40
-->

# 02_research_map.md — BẢN ĐỒ NGHIÊN CỨU CHUYÊN SÂU (RESEARCH MAP)
## TẬP PHIM: BÀI TOÁN LẬP NGHIỆP & SINH SỐNG TẠI ĐẶC KHU PHÚ QUỐC 2026
### (Khảo sát Thực chứng: Chi phí ngầm, Cơn ác mộng Mùa mưa, Sàng lọc Thị trường và Lằn ranh An toàn YMYL)

> **Cơ quan Nghiên cứu:** Hội đồng Nghiên cứu Kinh tế Xã hội & Chiến lược Kịch bản (Góc Nhìn Podcast)  
> **Phương pháp:** Direct RPC Ingestion (63 nguồn tài liệu chuẩn mực đã nhập) & Batch Extraction qua Google NotebookLM Engine (`b14b9d2f-6f32-491a-b7dd-c5638817dc71`)  
> **Cập nhật dữ liệu:** Tháng 09/2026 (Số liệu thực chứng 2025–2026, hướng tới APEC 2027 và Quy hoạch 2040)

---

## 1. MỤC LỤC TỔNG QUAN TỌA ĐỘ KHO TÀI LIỆU (VAULT INDEX — 10 CHUYÊN ĐỀ)

| Mã Vault | Tên Chuyên Đề Nghiên Cứu Thực Chứng | File Lưu Trữ (`research_vault/`) | Quy mô Dữ liệu |
| :--- | :--- | :--- | :---: |
| `VAULT_PQ_01` | Chi phí sinh hoạt, giá thuê trọ & Chỉ số "Thuế hải đảo" (Island Tax) 2025–2026 | [`01_living_costs_and_island_tax.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/01_living_costs_and_island_tax.md) | 15.280 bytes |
| `VAULT_PQ_02` | Thị trường thuê mặt bằng kinh doanh, kiot & shophouse trục ĐT.975 | [`02_commercial_rental_market.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/02_commercial_rental_market.md) | 14.159 bytes |
| `VAULT_PQ_03` | Cơ cấu thị trường lao động, thang lương & chế độ đãi ngộ resort 4-5 sao | [`03_labor_market_wages_and_benefits.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/03_labor_market_wages_and_benefits.md) | 15.214 bytes |
| `VAULT_PQ_04` | Cơn ác mộng mùa mưa (Gió mùa Tây Nam) & Rủi ro đứt gãy dòng tiền F&B/Homestay | [`04_seasonal_monsoon_impact.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/04_seasonal_monsoon_impact.md) | 9.236 bytes |
| `VAULT_PQ_05` | Sự thống trị của Integrated Resorts (Hệ sinh thái khép kín) & Bẫy hoa hồng taxi | [`05_all_inclusive_resorts_vs_local_smbs.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/05_all_inclusive_resorts_vs_local_smbs.md) | 11.186 bytes |
| `VAULT_PQ_06` | Cơ hội lập nghiệp chuỗi cung ứng B2B & Dịch vụ phụ trợ cho các tổ hợp nghỉ dưỡng 5 sao | [`06_b2b_and_supply_chain_opportunities.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/06_b2b_and_supply_chain_opportunities.md) | 11.762 bytes |
| `VAULT_PQ_07` | Đón đầu Quy hoạch 700.000 dân thường trú 2040 — Cơ hội dịch vụ đô thị & An cư | [`07_permanent_resident_services_2040.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/07_permanent_resident_services_2040.md) | 14.128 bytes |
| `VAULT_PQ_08` | Khung pháp lý Đặc khu Phú Quốc, Nghị quyết 41/2026/QH16, FTZ & Bảng giá đất 2026 | [`08_institutional_legal_framework.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/08_institutional_legal_framework.md) | 18.830 bytes |
| `VAULT_PQ_09` | Bài học quốc tế về lập nghiệp hải đảo — Jeju (Hàn Quốc), Bali (Indonesia), Okinawa & Phuket | [`09_international_island_benchmarks.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/09_international_island_benchmarks.md) | 11.122 bytes |
| `VAULT_PQ_10` | Phản biện đối lập mạnh nhất (Steelman Audit) & Cẩm nang kỷ luật sinh tồn tại đảo | [`10_steelman_audit_and_survival_playbook.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/10_steelman_audit_and_survival_playbook.md) | 15.307 bytes |

---

## 2. BẢNG MỎ NEO DỮ LIỆU THỰC CHỨNG ĐỊNH LƯỢNG (FACT-BASED DATA ANCHORS)

| # | Luận điểm & Chỉ số Cốt lõi | Con số Định lượng Thực chứng | Căn cứ Pháp lý & Khảo sát Thực tế | Tọa độ Vault (`research_vault/`) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Chi phí Thuê trọ Lao động:** Phân hóa sâu sắc giữa phòng cơ bản và phòng tiện nghi. | • **1,4 – 2,5 triệu đồng/tháng** (Phòng 18-24m² tại An Thới, Dương Tơ).<br>• **3,0 – 5,5 triệu đồng/tháng** (Phòng full nội thất tại Dương Đông). | Báo cáo thị trường lưu trú Phú Quốc 2026; Phongtro123, Homedy. | [`01_living_costs_and_island_tax.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/01_living_costs_and_island_tax.md) |
| **2** | **"Thuế Hải Đảo" (Island Tax):** Chi phí logistics đa phương thức đẩy giá vốn hàng bán. | • Logistics đội giá vốn (COGS) lên **15% – 25%** so với đất liền.<br>• Ngân sách tối thiểu: **7 – 10 triệu/tháng** (độc thân), **18 – 25 triệu/tháng** (gia đình 3 người). | Khảo sát chuỗi cung ứng phà Rạch Giá/Hà Tiên – Bãi Vòng; Vận tải An Pha. | [`01_living_costs_and_island_tax.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/01_living_costs_and_island_tax.md) |
| **3** | **Rào cản Thuê Mặt bằng Kinh doanh:** Tiền cọc lớn và chi phí mặt tiền trục chính. | • Kiot/quán nhỏ: **5 – 15 triệu đồng/tháng**.<br>• Shophouse hoàn thiện trục ĐT.975: **60 – 80 triệu đồng/tháng**.<br>• Đặt cọc: **1 – 6 tháng**, thanh toán: **3 – 6 tháng/lần**. | Dữ liệu Batdongsan.com.vn, CafeF 2026; Khảo sát ĐT.975 và Dương Đông. | [`02_commercial_rental_market.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/02_commercial_rental_market.md) |
| **4** | **Thang lương & Phúc lợi Resort 4-5 sao:** Cơ cấu thu nhập và giá trị của gói bao ăn ở. | • Lao động phổ thông: **7 – 12 triệu/tháng**.<br>• Chuyên môn/Giám sát: **12 – 20 triệu/tháng**.<br>• Quản lý cấp trung - cao: **25 – 60+ triệu/tháng**.<br>• Gói bao ăn ở (ký túc xá) tương đương **3 – 5 triệu đồng/tháng**. | Báo cáo khảo sát CareerLink & Hoteljob Phú Quốc (Tháng 08/2026). | [`03_labor_market_wages_and_benefits.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/03_labor_market_wages_and_benefits.md) |
| **5** | **Khát khao Nhân sự Đa ngôn ngữ:** Lợi thế cạnh tranh vượt bậc của tiếng ngoại. | • Nhân sự thông thạo tiếng Hàn, Trung, Nga, Anh có mức lương cao hơn **30% – 50%** so với nhân sự đơn ngữ.<br>• Tỷ lệ khách ngoại chiếm hơn **50%** cơ cấu khách 2026. | Sở Du lịch Kiên Giang / An Giang; Báo Lao Động (2026). | [`03_labor_market_wages_and_benefits.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/03_labor_market_wages_and_benefits.md) |
| **6** | **Cơn ác mộng Mùa mưa (Tháng 5 - Tháng 10):** Đứt gãy dòng tiền mùa gió Tây Nam. | • Doanh thu dịch vụ du lịch ngoài trời sụt giảm **50% – 70%**.<br>• Tàu cao tốc và tour đảo ngừng hoạt động trung bình **15 – 30 ngày/mùa**.<br>• Hơn **60%** quán cà phê/homestay tự phát đóng cửa sau 1 mùa mưa. | Dữ liệu khí tượng thủy văn Phú Quốc; Khảo sát thực địa Rooty Trip. | [`04_seasonal_monsoon_impact.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/04_seasonal_monsoon_impact.md) |
| **7** | **Bẫy Hoa hồng Taxi & Hệ sinh thái Khép kín:** Khách tour trọn gói không ra ngoài. | • Các quán ăn độc lập phải trích chiết khấu **20% – 40%** cho tài xế taxi / hướng dẫn viên.<br>• Các đại tổ hợp (Grand World, Sun World) giữ khách tiêu dùng khép kín **80%** ngân sách tour. | Báo Thanh Niên, Diễn đàn Doanh nghiệp Phú Quốc 2026. | [`05_all_inclusive_resorts_vs_local_smbs.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/05_all_inclusive_resorts_vs_local_smbs.md) |
| **8** | **Mỏ neo Thể chế Đặc khu & Giá đất 2026:** Bảng giá đất mới sát thị trường đẩy chi phí. | • Nghị quyết 202/2025/QH15 & Nghị quyết 1654/NQ-UBTVQH15 lập Đặc khu Phú Quốc.<br>• Nghị quyết số 41/2026/QH16 tháo gỡ vướng mắc 21 dự án APEC 2027.<br>• Bảng giá đất 2026 làm chi phí đầu vào thuê đất tăng **20% – 35%**. | LuatVietnam; Cổng thông tin Chính phủ; Báo Đầu Tư (09/2026). | [`08_institutional_legal_framework.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/08_institutional_legal_framework.md) |
| **9** | **Quy hoạch Đô thị Thường trú 2040:** Dư địa dịch vụ phục vụ 700.000 dân. | • Quy mô dân số tăng từ **150.000 dân hiện tại lên 700.000 dân** năm 2040 (theo QĐ 150/QĐ-TTg).<br>• Thiếu hụt nghiêm trọng trường mầm non chất lượng cao, phòng khám đa khoa gia đình. | Quyết định 150/QĐ-TTg của Thủ tướng Chính phủ; Ban Quản lý Khu kinh tế. | [`07_permanent_resident_services_2040.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/07_permanent_resident_services_2040.md) |
| **10** | **Kỷ luật Sinh tồn Hải đảo (Survival Playbook):** Quy tắc quản trị vốn bắt buộc. | • Bắt buộc chuẩn bị vốn lưu động dự phòng bù lỗ tối thiểu **6 – 9 tháng** (trọn vẹn 1 mùa mưa).<br>• Lựa chọn địa bàn theo mùa: Bờ Tây (hoàng hôn mùa khô) vs Bờ Đông (yên sóng mùa mưa). | Nghiên cứu tổng hợp từ bài học đảo Jeju (Hàn Quốc) và Bali (Indonesia). | [`10_steelman_audit_and_survival_playbook.md`](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/lap-nghiep-phu-quoc/research_vault/10_steelman_audit_and_survival_playbook.md) |

---

## 3. MA TRẬN PHẢN BIỆN ĐỐI LẬP (STEELMAN DIALECTICAL MATRIX)

| Luận Điểm Màu Hồng (The Illusion) | Thực Tế Khắc Nghiệt Kiểm Toán Được (The Harsh Reality) | Đòn Bẩy Thích Ứng Sống Còn (The Survival Strategy) |
| :--- | :--- | :--- |
| *"Phú Quốc đón 8 triệu khách, mở quán gì cũng đông khách và hốt bạc."* | Hơn 70% khách quốc tế đi tour trọn gói, ăn - ở - chơi khép kín trong các Integrated Resorts. Quán ngoài phố không có khách nếu không chiết khấu 30% cho taxi. | Chuyển dịch mô hình: Không tranh giành khách lẻ vãng lai; tập trung làm chuỗi cung ứng B2B (thực phẩm, giặt ủi, bảo trì) hoặc phục vụ dân cư thường trú. |
| *"Ra đảo làm việc vừa có thu nhập cao vừa được sống chill ngắm hoàng hôn mỗi ngày."* | Chi phí sinh hoạt đắt hơn đất liền 20-30%, đời sống văn hóa hạn chế, ốm đau nặng phải chuyển viện đất liền; áp lực ca kíp mùa cao điểm 12-14 tiếng/ngày. | Nhắm vào các doanh nghiệp bao ăn ở trọn gói (ký túc xá); trang bị ngoại ngữ để bước vào nhóm quản lý hoặc chuyên môn kỹ thuật hưởng service charge cao. |
| *"Cứ mở quán đẹp, thuê mặt bằng trung tâm rồi dòng tiền sẽ tự xoay vòng từ tháng đầu."* | Tiền cọc 3-6 tháng, tiền thuê trả trước nửa năm ngốn sạch vốn; mùa mưa kéo dài 5 tháng vắng khách khiến 60-80% mô hình tự phát phá sản sau 12 tháng. | Tuân thủ tuyệt đối quy tắc vốn dự phòng 6-9 tháng; phân bổ dòng tiền chống chọi qua trọn vẹn một mùa mưa gió Tây Nam trước khi tính đến lợi nhuận. |
| *"Lập nghiệp ở Phú Quốc chỉ có con đường làm du lịch, khách sạn hoặc nhà hàng."* | Thị trường du lịch đại trà đã bão hòa và bị thống trị bởi các tập đoàn lớn; cạnh tranh giá khốc liệt dẫn đến giảm chất lượng dịch vụ. | Đón đầu quy hoạch 700.000 dân đến 2040: Khởi nghiệp trong các ngành dịch vụ đô thị thiết yếu (giáo dục mầm non, ngoại ngữ, y tế tư nhân, bán lẻ tiện ích). |

---

## 4. BẢNG KIỂM TOÁN AN TOÀN NỘI DUNG YMYL (YOUTUBE MONETIZATION COMPLIANCE)

* [x] **Quy tắc 1 — Không lời khuyên đầu tư/chỉ đạo hành vi:** Toàn bộ dữ liệu được trình bày dưới góc độ báo cáo nghiên cứu kinh tế học đô thị và khảo sát thị trường lao động. Không xuất hiện câu lệnh: "Bạn nên đầu tư...", "Hãy mua ngay...".
* [x] **Quy tắc 2 — Tính trung lập & Tôn trọng sự thật (No Defamation):** Không nêu đích danh các cơ sở kinh doanh nhỏ lẻ để bôi nhọ; dùng thuật ngữ kinh tế học ("chi phí trung gian", "hoa hồng môi giới", "chi phí logistics vận tải biển") thay cho ngôn từ kích động ("chặt chém", "lừa đảo").
* [x] **Quy tắc 3 — Cân bằng hai chiều (Steelman Standard):** Khẳng định tiềm năng to lớn của Đặc khu Phú Quốc và APEC 2027, đồng thời chỉ rõ rào cản chi phí và chu kỳ mùa mưa để người xem có bức tranh toàn cảnh khách quan.
* [x] **Quy tắc 4 — Tuyên bố miễn trừ trách nhiệm (Legal Disclaimer):** Đã tích hợp sẵn nội dung miễn trừ trách nhiệm ở đầu kịch bản nhằm bảo vệ kênh 100% trước bộ lọc kiểm duyệt của YouTube.
