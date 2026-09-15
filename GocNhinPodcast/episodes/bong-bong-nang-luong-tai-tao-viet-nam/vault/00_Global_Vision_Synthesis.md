<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/bong-bong-nang-luong-tai-tao-viet-nam/vault/00_Global_Vision_Synthesis.md
- Activated Persona: The Macro Strategist (.agents/personas/the_macro_strategist.md) + The Industrial Economist (.agents/personas/the_industrial_economist.md) + The Policy Analyst (.agents/personas/the_policy_analyst.md) + The Critical Auditor (.agents/personas/the_critical_auditor.md)
- Activated Skill: script_architect (.agents/skills/script_architect/SKILL.md)
- Source Documents Consulted:
  * episodes/bong-bong-nang-luong-tai-tao-viet-nam/01_topic_qualification.md
  * Báo cáo IRENA, BloombergNEF về khủng hoảng thừa công suất quang điện Trung Quốc (1.200 GW vs 500 GW)
  * Quyết định áp thuế chống lẩn tránh AD/CVD của Bộ Thương mại Hoa Kỳ (US DOC) đối với pin mặt trời Đông Nam Á (2024-2026)
  * Báo cáo tài chính Longi Green Energy, Jinko Solar, Trina Solar (Giai đoạn lỗ ròng 2024-2026)
  * Quyết định 11/2017/QĐ-TTg, Kết luận 1027/KL-TTCP, Quy hoạch điện VIII (QĐ 500/QĐ-TTg)
- Execution Timestamp: 2026-09-04 22:00
-->

# BỨC TRANH TOÀN CẢNH: CAN BẠC NĂNG LƯỢNG TÁI TẠO & CUỘC SINH TỒN CÔNG NGHIỆP XANH CỦA VIỆT NAM
*(Macro Global Vision Synthesis & 4-Tier Modular Blueprint — Phiên bản Mở rộng Đối sánh Trung Quốc)*

---

## TẦNG 1: META-INSTRUCTIONS & MACRO GUARDRAILS

```yaml
meta_framework:
  episode_slug: "bong-bong-nang-luong-tai-tao-viet-nam"
  working_title: "Can Bạc Năng Lượng Tái Tạo & Cuộc Sinh Tồn Công Nghiệp Xanh Của Việt Nam"
  runtime_target: "25 - 30 phút (khoảng 4.500 - 5.200 từ thoại)"
  primary_persona: "The Macro Strategist + The Industrial Economist"
  supervising_auditor: "The Critical Auditor + The Policy Analyst"
  
narrative_spine:
  inciting_incident: "Mùa hè năm 2023, miền Bắc cắt điện luân phiên làm gián đoạn các khu công nghiệp FDI, phơi bày nghịch lý: Việt Nam sở hữu công suất điện mặt trời số 1 Đông Nam Á nhưng vẫn đối mặt với rủi ro an ninh năng lượng."
  macro_undercurrent: "Năng lượng tái tạo là VÉ THÔNG HÀNH SINH TỒN của cả nền kinh tế Việt Nam trên bàn cờ Net Zero toàn cầu (hàng rào thuế carbon CBAM, giữ chân dòng vốn FDI bán dẫn/AI/Apple/Samsung). Nhưng cuộc đua này bị biến dạng bởi cơn sốt giá FIT và đòn bẩy nợ."
  comparative_axis: "Sự đối lập bản chất giữa chiếc bẫy của Trung Quốc và chiếc bẫy của Việt Nam: Trung Quốc mắc kẹt ở THƯỢNG NGUỒN CHẾ TẠO (dư thừa công suất 1.200 GW, bẫy nội quyển tự sát và thuế quan phương Tây); Việt Nam mắc kẹt ở HẠ NGUỒN TRUYỀN TẢI (nhập khẩu thiết bị rẻ của TQ để xí dự án ăn giá FIT, dẫn tới vỡ trận lưới điện và nợ trái phiếu)."
  grand_payoff: "Các cú sốc nghẽn lưới, dự án đắp chiếu và thanh tra không phải là dấu chấm hết, mà là cơn đau chuyển dạ tất yếu để Việt Nam thoát khỏi bẫy bao cấp sơ khai, chuyển sang mô hình công nghiệp xanh thực chất: Cơ chế DPPA sòng phẳng và Quy hoạch điện VIII."

guardrails_and_blacklist:
  blacklisted_framing:
    - CẤM đánh đồng khủng hoảng năng lượng tái tạo của Việt Nam với Trung Quốc. Trung Quốc thừa nhà máy sản xuất tấm pin (Overcapacity); Việt Nam thừa công suất phát cục bộ nhưng thiếu đường dây truyền tải và thiếu nguồn điện nền.
    - CẤM bỏ qua mối quan hệ nhân quả cộng sinh: Chính sự sụp đổ giá tấm pin của Trung Quốc là 'ngòi nổ' giúp các tập đoàn tư nhân Việt Nam có thể xây dựng thần tốc các trang trại nghìn tỷ để ăn giá FIT 9,35 cents.
    - CẤM nhìn nhận cuộc cạnh tranh năng lượng một chiều: Phải làm rõ thế kẹt của Việt Nam trong cuộc chiến thương mại Mỹ - Trung (vừa là nơi tiêu thụ thiết bị Trung Quốc, vừa là trạm trung chuyển bị Mỹ áp thuế chống lẩn tránh AD/CVD).
```

---

## TẦNG 2: GLOBAL ASCII ARCHITECTURE & MA TRẬN ĐỐI SÁNH TRUNG QUỐC — VIỆT NAM

### 1. Ma Trận Đối Sánh Chi Tiết: Hai Cỗ Máy — Hai Chiếc Bẫy

| Tiêu Chí Phân Tích | TRUNG QUỐC (The Manufacturing Giant) | VIỆT NAM (The Downstream Deployer) |
|---|---|---|
| **Vị trí Chuỗi Giá Trị** | **Thượng nguồn & Trung nguồn cốt lõi** (Kiểm soát 80–90% nguồn cung Polysilicon, Ingot, Wafer, Cell, Module toàn cầu). | **Hạ nguồn & Lắp ráp gia công** (Nhập khẩu 100% tế bào quang điện/tấm pin từ TQ để lắp trang trại điện hoặc làm trạm gia công xuất khẩu). |
| **Bản chất Sự Dư Thừa** | **Dư thừa NĂNG LỰC SẢN XUẤT CÔNG NGHIỆP** (1.200 GW công suất chế tạo vs ~500–600 GW nhu cầu toàn cầu). | **Dư thừa CÔNG SUẤT PHÁT ĐIỆN CỤC BỘ** (Thừa điện mặt trời tại Ninh Thuận/Bình Thuận vào giờ trưa nhưng thiếu điện giờ cao điểm tối). |
| **Nguyên Nhân Gốc Rễ** | **Chủ nghĩa tư bản nhà nước phi tập trung**: Chính quyền các tỉnh đua nhau cấp đất 0 đồng, ưu đãi thuế, ép ngân hàng cho vay để lấy chỉ số GDP địa phương. | **Thiết kế chính sách giá FIT kiểu vách đá**: Mức giá cố định quá hời (9,35 cents neo USD 20 năm) kích hoạt tâm lý xí đất, chạy đua đóng điện trước hạn chót. |
| **Chiếc Bẫy Mắc Kẹt Lớn Nhất** | **1. Bẫy Nội quyển (Involution - 内卷):** Cuộc chiến hạ giá tự sát ép các ông lớn (Longi) bán lỗ dưới giá thành.<br>**2. Bẫy Địa chính trị:** Mỹ/EU áp thuế AD/CVD chặn đường xuất khẩu thặng dư. | **1. Bẫy Hạ tầng Truyền tải:** Lưới điện không đuổi kịp pin mặt trời $\rightarrow$ Lệnh cắt giảm phát (Curtailment) 30–50%.<br>**2. Bẫy Kỳ hạn nợ:** Trái phiếu 2–4 năm tài trợ cho tài sản 20 năm. |
| **Hậu Quả Tài Chính** | Hàng chục hãng quang điện phá sản; các tập đoàn đầu ngành lỗ hàng trăm triệu USD; chính phủ phải áp thuế tiêu thụ để ép đóng cửa nhà máy yếu. | 85 dự án chuyển tiếp đắp chiếu; doanh nghiệp năng lượng tư nhân mất thanh khoản nợ trái phiếu; EVN gánh lỗ vì mua điện giá cao; chuyển nhượng dự án cho ngoại. |
| **Lối Thoát Chiến Lược** | Chuyển dịch chuỗi cung ứng ra nước ngoài (Đông Nam Á, Trung Đông) + Thúc đẩy thị trường lưu trữ BESS + Đặt chuẩn kỹ thuật cao loại bỏ công nghệ cũ. | Chấm dứt bao cấp FIT + Chuyển sang đấu thầu cạnh tranh + Ban hành cơ chế DPPA để phục vụ trực tiếp các tập đoàn FDI xuất khẩu (Samsung, Foxconn). |

### 2. Sơ Đồ Chuỗi Giá Trị & Mối Quan Hệ Cộng Sinh Giữa TQ và VN

```
[TRUNG QUỐC: BÙNG NỔ CÔNG SUẤT CHẾ TẠO]
- Chính quyền địa phương trợ cấp ồ ạt
- Công suất module vọt lên 1.200 GW/năm
- Dẫn tới CUỘC CHIẾN HẠ GIÁ "NỘI QUYỂN" (Giá tấm pin giảm >70%)
                │
                │ (Xuất khẩu thiết bị giá rẻ mạt)
                ▼
[VIỆT NAM: CƠN SAY ĐẦU TƯ TRANG TRẠI HẠ NGUỒN (2018 - 2020)]
- Quyết định 11/2017: Giá FIT 9,35 cents neo USD 20 năm
- Thiết bị nhập từ TQ rẻ đột biến ➔ Biên lợi nhuận (IRR) vọt lên 15-20%+
- Các đại gia tư nhân đua nhau dùng đòn bẩy trái phiếu gom đất làm dự án
                │
                │ (Bức tường giới hạn vật lý đập lại)
                ▼
[HAI BẢN KẾT TOÁN — HAI NỖI ĐAU KHÁC NHAU]
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│           TRUNG QUỐC BỊ KẸT:          │   │           VIỆT NAM BỊ KẸT:            │
│ - Tấm pin bán lỗ dưới giá thành       │   │ - Đường dây 220/500kV nghẽn mạch      │
│ - Longi, Jinko báo lỗ ròng kỷ lục     │   │ - EVN cắt giảm phát 30-50% (A0)       │
│ - Mỹ áp thuế AD/CVD chặn đường sang ĐNA│   │ - 85 dự án chuyển tiếp đắp chiếu      │
│ - Bị phương Tây tố 'xuất khẩu thặng dư'│  │ - Vỡ nợ kỹ thuật trái phiếu nghìn tỷ  │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```

---

## TẦNG 3: ATOMIC CHAPTER BLUEPRINTS (CH01 ĐẾN CH07)

### [CH01]: NGHỊCH LÝ GIỮA TRƯA NẮNG & BẢN CAM KẾT SINH TỒN COP26
* **THESIS:** Đợt mất điện mùa hè 2023 không đơn thuần là sự cố kỹ thuật, mà là phát súng báo hiệu sự va chạm giữa cam kết Net Zero toàn cầu và năng lực chịu đựng của hệ thống điện quốc gia.
* **CONTEXT & CONSTRAINTS:** Bối cảnh Thủ tướng tuyên bố cam kết Net Zero 2050 tại COP26. Việt Nam là một trong những nền kinh tế có độ mở thương mại lớn nhất thế giới (~200% GDP), mọi biến động xanh của quốc tế đều dội thẳng vào nội địa.
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-01`: Tổng công suất năng lượng tái tạo (gió + mặt trời) Việt Nam vượt 21.000 MW, chiếm hơn 27% tổng công suất đặt toàn hệ thống.
  - `DATA-02`: Đợt thiếu điện miền Bắc (tháng 5–6/2023) làm gián đoạn sản xuất tại các KCN Bắc Ninh, Bắc Giang; thiếu hụt đỉnh điểm 1.600 – 4.900 MW công suất khả dụng.
  - `DATA-03`: Cam kết Net Zero 2050 của Việt Nam tại COP26 và gói hỗ trợ JETP trị giá 15,5 tỷ USD từ Nhóm IPG.
* **DIALECTIC OPPOSITION:** Dư luận hỏi tại sao thừa điện mặt trời ở phía Nam mà không đưa ra Bắc cứu nguy $\longleftrightarrow$ Thực tế kỹ thuật: Khoảng cách truyền tải 1.500 km vượt quá giới hạn đường dây hiện hữu, và điện mặt trời biến mất vào đúng giờ cao điểm tối (18h–22h).
* **NARRATIVE BRIDGE:** 
  - *Harvest:* Khởi đi từ nghịch lý chiếc quạt nan mất điện và cam kết vĩ mô tại Glasgow.
  - *Seed:* Tại sao Việt Nam lại phải tự trói mình vào một cam kết khắt khe như vậy? Câu trả lời nằm ở chiếc thòng lọng thuế quan quốc tế.
* **VOICEOVER TONE:** Trầm tĩnh, mang tầm vóc địa kinh tế toàn cầu (Geopolitical Gravity).
* **COMPLIANCE & TERMINOLOGY:** Chuẩn xác: Cam kết Net Zero; Đối tác Chuyển dịch Năng lượng Công bằng (JETP); Độ mở thương mại (Trade-to-GDP ratio).

---

### [CH02]: HÀNG RÀO THUẾ CARBON & BÀI HỌC "NỘI QUYỂN" TỪ TRUNG QUỐC
* **THESIS:** Trong khi Việt Nam chạy đua làm điện sạch để vượt qua hàng rào thuế carbon CBAM và giữ chân FDI, thì nhìn sang biên giới, cỗ máy năng lượng tái tạo Trung Quốc đang tự giam mình trong chiếc bẫy "nội quyển" và thừa mứa công suất kinh hoàng.
* **CONTEXT & CONSTRAINTS:** Cơ chế CBAM của EU bắt đầu áp dụng; yêu cầu chuỗi cung ứng RE100 (Apple, Samsung, Lego). Đồng thời phân tích cuộc khủng hoảng thừa công suất quang điện tại Trung Quốc (1.200 GW công suất vs 500 GW nhu cầu).
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-04`: Cơ chế CBAM của EU đánh thuế carbon lên các ngành xuất khẩu chủ lực (thép, nhôm, xi măng...).
  - `DATA-05`: Công suất sản xuất pin mặt trời của Trung Quốc đạt ~1.200 GW/năm, kiểm soát >80% chuỗi cung ứng toàn cầu; giá module sụt giảm xuống mức kỷ lục ~0,10 USD/W.
  - `DATA-06`: Biểu tượng quang điện Trung Quốc — Longi Green Energy — ghi nhận lỗ ròng 3,68 tỷ NDT trong nửa đầu năm 2026 do cuộc chiến dìm giá tự sát (*neijuan*).
* **DIALECTIC OPPOSITION:** Trung Quốc làm chủ công nghệ và thừa mứa thiết bị $\longleftrightarrow$ Nhưng mắc kẹt vì không ai hấp thụ hết lượng hàng khổng lồ đó khi Mỹ và Châu Âu dựng hàng rào thuế quan bảo hộ; doanh nghiệp Trung Quốc buộc phải "xuất khẩu thặng dư" và dìm giá rẻ mạt ra thế giới.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Phơi bày hai thái cực: Một bên khát điện sạch để xuất khẩu (VN), một bên thừa mứa thiết bị đến mức tự hủy hoại lợi nhuận (TQ).
  - *Seed:* Chính cơn khủng hoảng thừa và làn sóng xả hàng giá rẻ của Trung Quốc đã trở thành "mồi lửa" thổi bùng cơn sốt điện mặt trời tại Việt Nam.
* **VOICEOVER TONE:** So sánh sắc lạnh, tầm nhìn địa kinh tế công nghiệp (Comparative Industrial Forensics).
* **COMPLIANCE & TERMINOLOGY:** CBAM; RE100; Bẫy Nội quyển (Involution / Neijuan - 内卷); Dư thừa công suất (Overcapacity).

---

### [CH03]: MỎ VÀNG 9,35 CENTS — CƠN SAY NGHÌN TỶ VÀ NGHỆ THUẬT XÍ ĐẤT
* **THESIS:** Nhờ tấm pin Trung Quốc giảm giá sốc, mức giá FIT 9,35 cents của Quyết định 11/2017 bất ngờ biến thành một "cỗ máy in tiền phi rủi ro", kích hoạt làn sóng đầu cơ và đòn bẩy nợ của các tập đoàn tư nhân.
* **CONTEXT & CONSTRAINTS:** Quyết định 11/2017/QĐ-TTg ra đời khi các đại dự án nhiệt điện than bị đình trệ. Các tập đoàn tư nhân nhập khẩu ồ ạt thiết bị giá rẻ của Trung Quốc về lắp đặt thần tốc.
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-07`: Giá FIT 1 cho điện mặt trời: 9,35 US cents/kWh (~2.086 đ/kWh), neo USD trong 20 năm, cam kết bao tiêu 100%.
  - `DATA-08`: Công suất điện mặt trời Việt Nam tăng vọt từ <100 MW lên hơn 16.500 MW trong chưa đầy 3 năm (2018–2020), phá vỡ toàn bộ quy hoạch nguồn điện.
  - `DATA-09`: Tỷ lệ đòn bẩy nợ mạo hiểm: Doanh nghiệp chỉ bỏ 15–20% vốn chủ sở hữu, còn lại 80–85% là vay ngân hàng và phát hành trái phiếu doanh nghiệp với lãi suất 10–11,5%/năm.
* **DIALECTIC OPPOSITION:** Doanh nghiệp vẽ ra bảng tính Excel với IRR 15–20% dựa trên giả định EVN sẽ mua hết 100% điện phát ra $\longleftrightarrow$ Họ nhắm mắt làm ngơ trước điều khoản PPA mẫu: EVN có quyền giảm phát nếu lưới quá tải mà không phải bồi thường một đồng nào.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Bóc trần cơn say tài chính được nuôi dưỡng bởi thiết bị giá rẻ Trung Quốc và chính sách giá FIT.
  - *Seed:* Nhưng khi hàng trăm trang trại mọc lên như nấm, bức tường vật lý không thể vượt qua đã đập thẳng vào mặt các nhà đầu tư.
* **VOICEOVER TONE:** Kịch tính, phơi bày cỗ máy dòng tiền (Investigative Financial Noir).
* **COMPLIANCE & TERMINOLOGY:** Cơ chế giá FIT (Feed-in Tariff); Hợp đồng mua bán điện mẫu (Standard PPA); Đòn bẩy tài chính (Leverage).

---

### [CH04]: VỠ TRẬN HẠ TẦNG — SỰ KHÁC BIỆT GIỮA KẸT LƯỚI VÀ THỪA HÀNG
* **THESIS:** Sự va chạm khốc liệt giữa tốc độ xây dựng thần tốc của nguồn phát và độ trễ giải phóng mặt bằng của đường dây truyền tải đã đẩy hệ thống điện Việt Nam vào thảm cảnh cắt giảm công suất (Curtailment).
* **CONTEXT & CONSTRAINTS:** Điểm nóng Ninh Thuận, Bình Thuận, Tây Nguyên (2019–2021). So sánh: Trung Quốc kẹt vì không bán được tấm pin ra thế giới; Việt Nam kẹt vì pin lắp xong không thể phát điện lên lưới.
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-10`: Bất đối xứng vật lý: Xây trang trại điện mặt trời mất 6–9 tháng; xây đường dây 220kV/500kV mất 3–5 năm.
  - `DATA-11`: Trung tâm Điều độ A0 buộc phải ra lệnh cắt giảm phát điện (Curtailment) từ 30% đến 50% công suất tại nhiều dự án để chống nổ biến áp và sập lưới điện quốc gia.
  - `DATA-12`: Hệ số phụ tải (Capacity Factor) của điện mặt trời chỉ đạt 15–20%, đòi hỏi hệ thống phải duy trì nguồn nhiệt điện than/khí chạy dự phòng quay (Spinning Reserve) tốn kém.
  - `DATA-26`: Hiện tượng Đường cong con vịt (Duck Curve) tại Việt Nam: Chênh lệch phụ tải ròng giữa trưa nắng và giờ cao điểm tối (17h30–20h) lên tới 4.000 – 6.000 MW, phơi bày giới hạn của điện mặt trời khi thiếu hệ thống pin lưu trữ BESS.
  - `DATA-27`: Đường dây 500kV Mạch 3 Quảng Trạch - Phố Nối (hoàn thành 8/2024): Nâng công suất truyền tải Bắc - Trung từ 2.200 MW lên 5.000 MW, nhưng chưa thể giải tỏa hoàn toàn cho các vựa NLTT Nam Trung Bộ do nút thắt 500kV Ninh Thuận - Bình Thuận.
* **DIALECTIC OPPOSITION:** Chủ đầu tư khóc ròng vì tiền đầu tư bỏ ra 100% nhưng chỉ thu về 50–70% doanh thu $\longleftrightarrow$ Cơ quan điều độ không có lựa chọn nào khác vì an ninh lưới điện quốc gia là tối thượng.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Phơi bày mâu thuẫn vật lý cơ học.
  - *Seed:* Bị giảm phát 50% đã là thảm họa, nhưng với những dự án trượt hạn FIT dù chỉ 24 giờ, chiếc bẫy tài chính thực sự mới sập xuống.
* **VOICEOVER TONE:** Xung đột gay gắt, cơ học, số liệu đanh thép (Mechanistic Climax).
* **COMPLIANCE & TERMINOLOGY:** Cắt giảm công suất phát (Curtailment); Nghẽn mạch truyền tải (Grid Bottleneck); Dự phòng quay (Spinning Reserve); Đường cong con vịt (Duck Curve).

---

### [CH05]: CHIẾC BẪY TÀI CHÍNH & VẾT SẸO 85 DỰ ÁN CHUYỂN TIẾP
* **THESIS:** Thiết kế chính sách kiểu "vách đá" và sự lệch pha kỳ hạn nợ trái phiếu đã biến hàng chục nghìn tỷ đồng tài sản thành phế tích phơi sương, kích hoạt cuộc thanh tra chấn chỉnh kỷ cương quy hoạch.
* **CONTEXT & CONSTRAINTS:** Hạn chót đóng điện điện gió (31/10/2021). Nhóm 85 dự án chuyển tiếp trượt hạn COD. Khủng hoảng thị trường trái phiếu sau vụ việc Vạn Thịnh Phát (cuối 2022).
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-13`: Nhóm 85 dự án năng lượng tái tạo chuyển tiếp (tổng công suất 4.736 MW, chủ yếu điện gió) trượt hạn COD, đắp chiếu chờ cơ chế suốt hơn 2 năm.
  - `DATA-14`: Khung giá phát điện chuyển tiếp (Quyết định 21/QĐ-BCT) thấp hơn 21% – 29% so với giá FIT cũ (điện mặt trời mặt đất trần 1.184,9 đ/kWh vs FIT 1 ~2.086 đ/kWh; điện gió trên đất liền trần 1.587,12 đ/kWh).
  - `DATA-15`: Kết luận thanh tra số 1027/KL-TTCP: Chỉ ra 54 dự án (>10.500 MW) được bổ sung riêng lẻ vào Quy hoạch điện VII điều chỉnh thiếu căn cứ pháp lý tổng thể; chuyển 154 dự án có vướng mắc sang cơ quan điều tra rà soát.
  - `DATA-16`: Chiếc bẫy lệch pha kỳ hạn: Trái phiếu kỳ hạn 2–4 năm (lãi suất 10–11,5%) đè bẹp dòng tiền của các dự án có chu kỳ hoàn vốn 15–20 năm, khiến các tập đoàn tư nhân (Trung Nam, BCG Energy) phải khất nợ trái phiếu.
  - `DATA-24`: Biến cố nợ trái phiếu Trung Nam Đắk Lắk 1: Chậm thanh toán gốc và lãi cho 3 lô trái phiếu với tổng giá trị lưu hành lên tới 2.540 tỷ đồng; công bố thông tin bất thường tại HNX và lãnh đạo tập đoàn bị tạm hoãn xuất cảnh do nợ thuế.
  - `DATA-25`: Tranh chấp nghiệm thu COD 172 MW Trung Nam Thuận Nam: Dự án 450 MW tại Ninh Thuận bị dừng huy động phần công suất 172 MW do chưa có khung giá và chưa đủ điều kiện theo Kết luận 1027/KL-TTCP, đẩy dự án vào bế tắc tài chính.
* **DIALECTIC OPPOSITION:** Doanh nghiệp xin cứu trợ để tránh phá sản $\longleftrightarrow$ Nhà nước kiên quyết siết chặt kỷ cương: Không thể dùng tiền điện của toàn dân để bảo lãnh cho những dự án chậm tiến độ và phê duyệt sai quy trình.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Nút thắt pháp lý và tài chính nghẹt thở.
  - *Seed:* Giữa vòng vây nợ nần và thanh tra, các tập đoàn tư nhân Việt Nam tìm đường thoát hiểm bằng cách nào? Một bàn cờ chuyển giao tài sản quốc tế bắt đầu xoay vần.
* **VOICEOVER TONE:** Lạnh lùng, soi xét pháp lý và kiểm toán tài chính (Forensic & Analytical).
* **COMPLIANCE & TERMINOLOGY:** Dự án chuyển tiếp (Transitional Projects); Lệch pha kỳ hạn nợ (Maturity Mismatch); Kết luận thanh tra 1027/KL-TTCP.

---

### [CH06]: BÀN CỜ M&A NGOẠI & CUỘC CHIẾN THUẾ QUAN BỌC LÓT
* **THESIS:** Làn sóng các tập đoàn quốc tế thâu tóm dự án năng lượng sạch tại Việt Nam phơi bày sự thay thế của dòng vốn dài hạn giá rẻ; đồng thời phản ánh thế kẹt của Việt Nam trong cuộc chiến thuế quan năng lượng Mỹ - Trung.
* **CONTEXT & CONSTRAINTS:** Làn sóng M&A từ Thái Lan (B.Grimm, Super Energy), Philippines (ACEN), Singapore (Sembcorp). Cùng lúc đó, Bộ Thương mại Hoa Kỳ (DOC) điều tra và áp thuế chống lẩn tránh (AD/CVD) lên pin mặt trời sản xuất tại Việt Nam.
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-17`: B.Grimm Power nâng sở hữu lên 96,25% tại cụm dự án điện mặt trời Dầu Tiếng (Tây Ninh - 420 MW) và mua 80% dự án Hòa Hội (Phú Yên).
  - `DATA-18`: Super Energy thâu tóm 9 dự án điện mặt trời (837 MW) rồi sang tay cho tập đoàn ACEN (Philippines) để tái cơ cấu danh mục.
  - `DATA-19`: Chênh lệch chi phí vốn (WACC): Doanh nghiệp nội gánh lãi suất vay 10%–12%/năm; các tập đoàn quốc tế tiếp cận nguồn vốn xanh toàn cầu với chi phí chỉ 3%–5%/năm.
  - `DATA-20`: Tháng 4/2025 và kéo dài sang 2026, Bộ Thương mại Mỹ (DOC) hoàn tất áp thuế chống bán phá giá và chống trợ cấp (AD/CVD) đối với pin mặt trời nhập khẩu từ Việt Nam, Malaysia, Thái Lan, Campuchia vì bị coi là 'trạm trung chuyển lẩn tránh thuế' của các nhà sản xuất Trung Quốc.
* **DIALECTIC OPPOSITION:** Lo ngại mất an ninh năng lượng vào tay doanh nghiệp ngoại $\longleftrightarrow$ Thực tế thị trường: Doanh nghiệp nội buộc phải bán để giải tỏa áp lực nợ trái phiếu; khối ngoại có năng lực tài chính và chi phí vốn rẻ hơn để vận hành dài hạn.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Làm rõ cuộc tái cơ cấu nguồn lực và thế kẹt địa chính trị.
  - *Seed:* Cơn sốt hoang dã đã kết thúc. Một thị trường năng lượng xanh của Việt Nam trong thập niên tới sẽ được thiết kế lại theo luật chơi nào để vừa đáp ứng Net Zero, vừa không lặp lại bi kịch bong bóng?
* **VOICEOVER TONE:** Sâu sắc, nhìn nhận thực tế địa kinh tế (Strategic & Objective).
* **COMPLIANCE & TERMINOLOGY:** M&A năng lượng; Thuế chống lẩn tránh (Anti-circumvention / AD/CVD); Chi phí sử dụng vốn bình quân (WACC).

---

### [CH07]: KỶ NGUYÊN THỰC CHẤT — BẢN THIẾT KẾ MỚI CỦA NỀN KINH TẾ XANH
* **THESIS:** Chấm dứt bao cấp FIT không phải là thất bại, mà là bước trưởng thành tất yếu để đưa năng lượng sạch Việt Nam hòa nhịp vào nền kinh tế thị trường sòng phẳng: Cơ chế DPPA phục vụ xuất khẩu, Quy hoạch điện VIII và bài toán chuyển dịch công bằng.
* **CONTEXT & CONSTRAINTS:** Nghị định 57/2025/NĐ-CP (ban hành ngày 03/03/2025 thay thế NĐ 80/2024); Quyết định 21/2025/QĐ-TTg (Phân loại Xanh); Quy hoạch điện VIII điều chỉnh.
* **IMMUTABLE DATA ANCHORS:**
  - `DATA-21`: Nghị định 80/2024/NĐ-CP và Nghị định 57/2025/NĐ-CP chính thức thiết lập hành lang pháp lý mua bán điện trực tiếp (DPPA): Cho phép nhà phát điện NLTT bán điện cho khách hàng lớn qua lưới điện quốc gia hoặc qua đường dây kết nối riêng.
  - `DATA-22`: Thỏa thuận DPPA đầu tiên: Dự án Điện mặt trời TTC Đức Huệ 2 (Long An, 49 MWp) ký kết hợp tác bán điện sạch và chuyển giao chứng chỉ I-REC trực tiếp cho Samsung Electronics Việt Nam (Thái Nguyên).
  - `DATA-23`: Quy hoạch điện VIII đặt mục tiêu đến năm 2030 nâng tỷ lệ năng lượng tái tạo lên 30,9% – 39,2%; ưu tiên phát triển hệ thống pin tích năng BESS và điện gió ngoài khơi gắn với các tập đoàn nhà nước (PVN, EVN).
  - `DATA-28`: Nghị định số 57/2025/NĐ-CP (ngày 03/03/2025): Hoàn thiện công thức thanh toán hợp đồng chênh lệch (CfD) qua thị trường điện giao ngay và quy định chi tiết biểu phí dịch vụ hệ thống điện (wheeling charges: truyền tải, phân phối, điều độ, phụ trợ).
  - `DATA-29`: Quyết định số 21/2025/QĐ-TTg về Phân loại Xanh Quốc gia (Green Taxonomy): Ban hành bộ tiêu chí kỹ thuật chuẩn mực để các ngân hàng mở rộng tín dụng xanh và các tổ chức quốc tế giải ngân gói hỗ trợ JETP 15,5 tỷ USD.
  - `DATA-30`: Chứng chỉ năng lượng tái tạo I-REC: Vũ khí chiến lược giúp các doanh nghiệp FDI (Samsung, Lego, Apple) hợp thức hóa mục tiêu RE100 và giúp hàng hóa Việt Nam né thuế carbon CBAM của Liên minh Châu Âu khi cơ chế tài chính bắt đầu thực thi từ 01/01/2026.
* **DIALECTIC OPPOSITION:** Doanh nghiệp không còn dựa dẫm vào giá bao cấp của nhà nước $\longleftrightarrow$ Doanh nghiệp xuất khẩu muốn né thuế CBAM phải tự trả tiền mua điện sạch theo giá thị trường; người dân được bảo vệ giá điện sinh hoạt thông qua nguồn điện nền ổn định.
* **NARRATIVE BRIDGE:**
  - *Harvest:* Giải tỏa hoàn toàn các nghịch lý từ đầu video.
  - *Grand Ending:* Một thông điệp đúc kết đắt giá: Bài học từ cơn say năng lượng tái tạo của Việt Nam và sự mắc kẹt của Trung Quốc cho thấy, không có con đường tắt nào dẫn tới thịnh vượng xanh. Chỉ khi năng lượng sạch được gắn trực tiếp vào chuỗi giá trị sản xuất thực và bài toán chi phí sòng phẳng, cuộc chuyển dịch Net Zero mới thực sự trở thành động cơ cất cánh của quốc gia.
* **VOICEOVER TONE:** Đĩnh đạc, triết lý, truyền cảm hứng phát triển bền vững (Visionary & Philosophic Noir).
* **COMPLIANCE & TERMINOLOGY:** Mua bán điện trực tiếp (Direct Power Purchase Agreement - DPPA); Hợp đồng kỳ hạn chênh lệch (CfD); Phân loại Xanh (Green Taxonomy); Quy hoạch điện VIII (PDP8).

---

## TẦNG 4: IMMUTABLE DATA VAULT (BẢNG TRA CỨU SỐ LIỆU VĨ MÔ ĐỐI SÁNH)

| Mã ID | Tên Chỉ Số / Sự Kiện Thực Chứng | Giá Trị Kiểm Chứng | Nguồn Tài Liệu Gốc | Chương Áp Dụng |
|---|---|---|---|:---:|
| `DATA-01` | Công suất NLTT Việt Nam | >21.000 MW (chiếm ~27% tổng công suất hệ thống) | Báo cáo Cục Điện lực & NLTT, Bộ Công Thương | CH01 |
| `DATA-02` | Thiệt hại thiếu điện miền Bắc 2023 | Hụt đỉnh điểm 1.600 – 4.900 MW công suất khả dụng | Báo cáo vận hành Trung tâm Điều độ A0 (T6/2023) | CH01 |
| `DATA-03` | Cam kết Net Zero & Gói JETP | Net Zero 2050 (COP26); Gói JETP 15,5 tỷ USD | Tuyên bố chính trị JETP Việt Nam & Nhóm IPG | CH01 |
| `DATA-04` | Thuế carbon CBAM của EU | Quy định EU 2023/956; áp thuế 6 ngành thâm dụng phát thải | Cổng thông tin Ủy ban Châu Âu (EC) | CH02 |
| `DATA-05` | Công suất quang điện Trung Quốc | ~1.200 GW/năm (gấp đôi nhu cầu toàn cầu); giá sụt còn ~0,10 $/W | Báo cáo BloombergNEF, Wood Mackenzie 2025–2026 | CH02 |
| `DATA-06` | Khoản lỗ của Longi Green Energy | Lỗ ròng 3,68 tỷ NDT trong nửa đầu năm 2026 (sau lỗ 6,4 tỷ 2025) | Báo cáo tài chính bán niên Longi Green Energy | CH02 |
| `DATA-07` | Mức giá FIT 1 điện mặt trời VN | 9,35 US cents/kWh (~2.086 đ/kWh), neo USD trong 20 năm | Quyết định số 11/2017/QĐ-TTg của Thủ tướng Chính phủ | CH03 |
| `DATA-08` | Tốc độ tăng trưởng ĐMT tại VN | Từ <100 MW lên >16.500 MW trong 3 năm (2018–2020) | Báo cáo tổng kết Tập đoàn Điện lực Việt Nam (EVN) | CH03 |
| `DATA-09` | Tỷ lệ đòn bẩy nợ của DN NLTT VN | Vốn chủ 15–20%, vốn vay nợ (ngân hàng + trái phiếu) 80–85% | Báo cáo thị trường trái phiếu FiinGroup, FiinRatings | CH03 |
| `DATA-10` | Bất đối xứng tiến độ Trạm vs Lưới | Trạm phát: 6–9 tháng; Đường dây truyền tải: 3–5 năm | Báo cáo Tổng công ty Truyền tải điện QG (EVNNPT) | CH04 |
| `DATA-11` | Tỷ lệ cắt giảm phát (Curtailment) | Cắt giảm 30% – 50% sản lượng tại Ninh Thuận, Bình Thuận | Báo cáo vận hành Trung tâm Điều độ A0 | CH04 |
| `DATA-12` | Hệ số phụ tải (Capacity Factor) ĐMT | Đạt 15% – 20% (chỉ phát điện ban ngày) | Báo cáo kỹ thuật Viện Năng lượng Việt Nam | CH04 |
| `DATA-13` | Quy mô 85 dự án chuyển tiếp | 85 dự án, tổng công suất 4.736 MW (chủ yếu là điện gió) | Báo cáo Bộ Công Thương gửi Thủ tướng Chính phủ | CH05 |
| `DATA-14` | Khung giá phát điện chuyển tiếp | Thấp hơn FIT 21% – 29% (Mặt đất trần 1.184,9 đ/kWh; Gió 1.587,1 đ/kWh) | Quyết định 21/QĐ-BCT của Bộ Công Thương | CH05 |
| `DATA-15` | Kết luận sai phạm quy hoạch TTCP | 54 dự án (>10.500 MW) bổ sung thiếu căn cứ; rà soát 154 dự án | Kết luận thanh tra số 1027/KL-TTCP | CH05 |
| `DATA-16` | Lệch pha kỳ hạn nợ trái phiếu | Trái phiếu 2–4 năm (lãi 10–11,5%) vs Hoàn vốn 15–20 năm | Bản cáo bạch phát hành trái phiếu các DN năng lượng | CH05 |
| `DATA-17` | B.Grimm Power thâu tóm ĐMT VN | Nâng sở hữu 96,25% Dầu Tiếng (Tây Ninh), mua 80% Hòa Hội (Phú Yên) | Báo cáo thường niên B.Grimm Power (SET Thái Lan) | CH06 |
| `DATA-18` | Super Energy sang tay cho ACEN | Chuyển nhượng 9 dự án ĐMT (837 MW) cho ACEN (Philippines) | Báo cáo công bố thông tin Sở GDCK Thái Lan (SET) | CH06 |
| `DATA-19` | Chênh lệch chi phí vốn (WACC) | Doanh nghiệp VN: 10%–12%/năm vs Quỹ ngoại: 3%–5%/năm | Báo cáo phân tích ngân hàng đầu tư quốc tế | CH06 |
| `DATA-20` | Mỹ áp thuế chống lẩn tránh AD/CVD | Thuế AD/CVD đối với pin mặt trời từ VN, Thái Lan, Malaysia | Quyết định điều tra Bộ Thương mại Hoa Kỳ (US DOC 2024-2026)| CH06 |
| `DATA-21` | Khung pháp lý cơ chế DPPA | Nghị định 80/2024/NĐ-CP & Nghị định 57/2025/NĐ-CP | Cổng thông tin điện tử Chính phủ | CH07 |
| `DATA-22` | Giao dịch DPPA đầu tiên qua lưới | TTC Đức Huệ 2 (Long An) ➔ Samsung Thái Nguyên (T6/2026) | EVN / Báo Đầu Tư | CH07 |
| `DATA-23` | Mục tiêu cơ cấu nguồn PDP8 | Tỷ lệ NLTT đạt 30,9% – 39,2% đến năm 2030; phát triển BESS | Quyết định số 500/QĐ-TTg phê duyệt Quy hoạch điện VIII | CH07 |
| `DATA-24` | Vỡ nợ trái phiếu Trung Nam Đắk Lắk 1 | Chậm trả lãi 3 lô trái phiếu tổng giá trị 2.540 tỷ đồng | Công bố thông tin Sở Giao dịch Chứng khoán Hà Nội (HNX) | CH05 |
| `DATA-25` | Đình chỉ huy động 172 MW Thuận Nam | Dừng huy động 172 MW do chưa có cơ chế giá và vướng TTCP | Báo cáo EVN và Kết luận Thanh tra 1027/KL-TTCP | CH05 |
| `DATA-26` | Đường cong con vịt (Duck Curve) VN | Chênh lệch phụ tải ròng trưa - tối đạt 4.000 – 6.000 MW | Báo cáo điều độ vận hành hệ thống điện A0/NSMO | CH04 |
| `DATA-27` | Đường dây 500kV Mạch 3 | Nâng truyền tải Bắc - Trung lên 5.000 MW (khánh thành 8/2024) | Ban Quản lý dự án các công trình điện miền Trung (CPMB)| CH04 |
| `DATA-28` | Nghị định DPPA mới 57/2025/NĐ-CP | Thay thế NĐ 80/2024, chuẩn hóa công thức CfD và wheeling fee | Ban hành ngày 03/03/2025 của Chính phủ | CH07 |
| `DATA-29` | Tiêu chuẩn Phân loại Xanh QG | Quyết định số 21/2025/QĐ-TTg về Green Taxonomy | Cổng thông tin điện tử Chính phủ (2025) | CH07 |
| `DATA-30` | Chuyển giao chứng chỉ I-REC | Samsung nhận I-REC từ dự án NLTT Việt Nam để đạt chuẩn RE100 | Báo cáo phát triển bền vững Samsung Electronics | CH07 |
