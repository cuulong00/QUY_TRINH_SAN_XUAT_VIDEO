<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/bay-mat-ngot-kinh-te-nen-tang/02_research_plan.md
- Master Notebook ID: 7069c72d-fe15-436c-9c21-57ac114117ec (Account: duongtt84@gmail.com)
- Methodology: Modular Multi-Query Ingestion Protocol (Phân Hạch Đa Tầng 5 Trụ Cột Độc Lập)
- Activated Personas: 
  * The Macro Strategist (.agents/personas/the_macro_strategist.md)
  * The Industrial Economist (.agents/personas/the_industrial_economist.md)
  * The Policy Analyst (.agents/personas/the_policy_analyst.md)
  * The Critical Auditor (.agents/personas/the_critical_auditor.md)
- Activated Skills: 
  * Deep Researcher (.agents/skills/deep_researcher/SKILL.md)
  * NotebookLM Librarian (.agents/skills/notebooklm_librarian/SKILL.md)
- Execution Timestamp: 2026-09-13 22:15
-->

# KẾ HOẠCH TÁI THIẾT DEEP RESEARCH TRÊN NOTEBOOKLM (02_RESEARCH_PLAN.MD)
## ĐỀ TÀI: BẢN CHẤT KINH TẾ HỌC CỐT LÕI CỦA KINH TẾ NỀN TẢNG (PLATFORM ECONOMY & MULTI-SIDED MARKETS)

---

## 🎯 I. MỤC TIÊU CHIẾN LƯỢC & NGUYÊN TẮC THIẾT KẾ BỨC TRANH TOÀN CẢNH

### 1. Bắt Bệnh Lỗ Hổng Nghiên Cứu Cũ
- **Hạn chế đã nhận diện:** Đợt nghiên cứu trước dùng một prompt duy nhất chứa quá nhiều từ khóa địa phương (*Grab đình công, Shopee tăng phí, kho Pingxiang, QĐ 01/2025*), khiến Google Deep Crawler kéo về 48 nguồn thì có tới 95% là báo chí thời sự Việt Nam. Hệ quả là kịch bản bị kéo lệch thành một bài phóng sự "kể khổ cục bộ", thiếu chiều sâu học thuật và mất đi tính phổ quát của cỗ máy kinh tế toàn cầu.
- **Tư duy tái thiết First-Principles:** 
  - Tên gọi chung của mô hình: **Kinh tế Nền tảng (Platform Economy)** / **Thị trường Đa diện (Multi-Sided Platforms - MSP)** / **Chủ nghĩa Tư bản Nền tảng (Platform Capitalism)**.
  - Trọng tâm tối thượng: **Giải phẫu Bản chất Kinh tế học, Kỹ nghệ Thao túng Hành vi, và Cơ chế Thu tô Số**.
  - Định vị các thị trường: Mỹ (Uber, Amazon), Trung Quốc (Meituan, Pinduoduo, Douyin) hay Đông Nam Á / Việt Nam (Grab, Shopee, TikTok Shop) **chỉ là những phòng thí nghiệm thực chứng (Empirical Case Studies)** phản chiếu cùng một quy luật vận hành của cỗ máy.

---

## 🧭 II. BỘ 5 PROMPTS NẠP NGUỒN PHÂN HẠCH CHUYÊN SÂU (TARGETED MODULAR INGESTION PROMPTS)

*Mỗi prompt dưới đây được nạp tuần tự vào Master Notebook duy nhất (`7069c72d-fe15-436c-9c21-57ac114117ec`) với cờ `--mode deep --import-all` để cào sâu 40–80 nguồn tài liệu quốc tế và học thuật.*

```
                                    ┌──────────────────────────────────────────────────────────┐
                                    │    MASTER NOTEBOOK: 7069c72d-fe15-436c-9c21-57ac114117ec │
                                    └────────────────────────────┬─────────────────────────────┘
                                                                 │
         ┌───────────────────────┬───────────────────────┼───────────────────────┬───────────────────────┐
         ▼                       ▼                       ▼                       ▼                       ▼
   [TRỤ CỘT 1]             [TRỤ CỘT 2]             [TRỤ CỘT 3]             [TRỤ CỘT 4]             [TRỤ CỘT 5]
Lý Thuyết Kinh Tế Học    Nguyên Mẫu Mỹ:         Nguyên Mẫu TQ:          Xung Đột Tam Giác       Bàn Cờ Thể Chế
Thị Trường Đa Diện       ZIRP Blitzscaling      Chuyên Chế Thuật Toán   Cấu Trúc & Phản Kháng   Toàn Cầu & Lát Cắt
(Tirole, Srnicek,        đến Siêu Thu Tô        & Chuỗi F2C Khép Kín    (Platform vs Partners   Thực Nghiệm
Doctorow, Zuboff)        (Uber & Amazon)        (Meituan & Temu/Douyin) vs Consumers)           Đông Nam Á / VN
```

---

### 📌 PROMPT 1: LÝ THUYẾT KINH TẾ HỌC NỀN TẢNG & QUY LUẬT THỊ TRƯỜNG ĐA DIỆN (FOUNDATIONAL THEORIES)

* **Mục tiêu nghiên cứu:** Xây dựng khung lý thuyết kinh tế học bất biến giải thích bản chất vận hành của mọi nền tảng số.
* **Nội dung Prompt nạp vào NotebookLM:**
```text
Nghiên cứu học thuật và kinh tế học chuyên sâu về Bản chất của Kinh tế Nền tảng (Platform Economy), Thị trường Đa diện (Multi-Sided Platforms - MSP / Two-Sided Markets), và Chủ nghĩa Tư bản Nền tảng (Platform Capitalism):

1. LÝ THUYẾT THỊ TRƯỜNG ĐA DIỆN (Jean Tirole - Nobel Kinh tế 2014 & Rochet):
   - Cơ chế Định giá Bất đối xứng (Asymmetric Pricing) và Trợ giá chéo (Cross-subsidization): Tại sao nền tảng chấp nhận bán dưới giá thành biên (P < MC) ở một phía để thu hút bên kia?
   - Hiệu ứng Mạng lưới Đa chiều (Cross-side Network Externalities): Động lực đạt tới "Điểm tới hạn" (Critical Mass) và thế độc quyền tự nhiên (Winner-Takes-All).
   - Chi phí chuyển đổi (Switching Costs) và hiệu ứng khóa chặt nhận thức/hành vi (Cognitive & Economic Lock-in).

2. CHỦ NGHĨA TƯ BẢN THU TÔ SỐ (Nick Srnicek - "Platform Capitalism"):
   - Định nghĩa các loại nền tảng: Lean platforms, Advertising platforms, Cloud platforms.
   - Bản chất của việc tư nhân hóa hạ tầng giao dịch công cộng và trích xuất địa tô số (Digital Rent Extraction) thay vì tạo ra của cải vật chất mới.

3. CHU KỲ SUY THOÁI NỀN TẢNG (Cory Doctorow - Lý thuyết "Enshittification"):
   - 3 giai đoạn suy thoái tự nhiên của mọi nền tảng độc quyền: (1) Hào phóng với người dùng để gom traffic -> (2) Hào phóng với đối tác kinh doanh/lao động để gom nguồn cung -> (3) Vắt kiệt cả hai phía để tối đa hóa thặng dư cho cổ đông nền tảng.

4. KỸ NGHỆ THAO TÚNG HÀNH VI (Shoshana Zuboff - "The Age of Surveillance Capitalism"):
   - Khai thác Thặng dư Hành vi (Behavioral Surplus) và Định hình Thói quen (Habit Formation / Conditioning): Cách nền tảng biến các tiện ích số thành phản xạ sinh học không thể từ bỏ của xã hội.
```

---

### 📌 PROMPT 2: NGUYÊN MẪU PHƯƠNG TÂY — TỪ BỮA TIỆC TIỀN RẺ (ZIRP) ĐẾN CUỘC SIẾT NỢ PHỐ WALL (THE US ARCHETYPE)

* **Mục tiêu nghiên cứu:** Cung cấp bằng chứng thực nghiệm quốc tế từ cái nôi Thung lũng Silicon: Cách thức Uber và Amazon đã mở đường cho cỗ máy thu tô toàn cầu.
* **Nội dung Prompt nạp vào NotebookLM:**
```text
Nghiên cứu kinh tế và kiểm toán thực chứng về sự chuyển dịch mô hình kinh doanh của các gã khổng lồ nền tảng Mỹ (Uber, Lyft, Amazon Marketplace) từ thời kỳ tiền rẻ đến áp lực IPO Phố Wall:

1. NGUYÊN MẪU GỌI XE (UBER & LYFT):
   - Kỷ nguyên tiền rẻ (Zero Interest-Rate Policy - ZIRP 2008-2021): Chiến lược Blitzscaling đốt hàng chục tỷ USD từ SoftBank Vision Fund, Sequoia; trợ giá tới 50% chi phí mỗi cuốc xe để tiêu diệt taxi truyền thống.
   - Cú bẻ lái sau IPO và lãi suất tăng (2022-2026): Áp lực tạo dòng tiền dương (Positive Free Cash Flow & Adjusted EBITDA) từ cổ đông Phố Wall.
   - Cơ chế siết thu nhập: Tỷ lệ trích thu (Take Rate) tăng từ 20% lên 35%-45%; thuật toán định giá động (Surge Pricing) và định giá phân biệt cá nhân hóa; bóc tách cuộc chiến phân loại lao động (California Proposition 22).

2. NGUYÊN MẪU THƯƠNG MẠI ĐIỆN TỬ (AMAZON MARKETPLACE):
   - Chuyên khảo "Amazon's Antitrust Paradox" (Lina Khan - Yale Law Journal 2017): Cách nền tảng dùng giá rẻ để trốn tránh luật chống độc quyền truyền thống.
   - Vụ kiện chống độc quyền của FTC chống lại Amazon (2023): Bằng chứng Amazon trích thu hơn 50% doanh thu của người bán thông qua ma trận phí (Phí hoa hồng, Phí kho vận FBA bắt buộc, Phí quảng cáo bắt buộc Pay-to-Play).
   - Sự suy đồi thuật toán tìm kiếm: Quảng cáo trả tiền chèn ép các kết quả tìm kiếm tự nhiên hữu cơ (Organic results degradation).
```

---

### 📌 PROMPT 3: NGUYÊN MẪU TRUNG QUỐC — CHUYÊN CHẾ THUẬT TOÁN & CỖ MÁY CHUỖI CUNG ỨNG F2C (THE CHINA ARCHETYPE)

* **Mục tiêu nghiên cứu:** Mổ xẻ cỗ máy kiểm soát lao động cực hạn bằng AI và mô hình Logistics F2C đè bẹp các tầng nấc phân phối.
* **Nội dung Prompt nạp vào NotebookLM:**
```text
Nghiên cứu chuyên sâu về mô hình kinh tế nền tảng và quản trị thuật toán tại Trung Quốc (Meituan, Alibaba/Taobao, Pinduoduo/Temu, Douyin):

1. QUẢN TRỊ THUẬT TOÁN CỰC ĐOAN (MEITUAN & ELE.ME):
   - Báo cáo điều tra chấn động "Tài xế giao hàng bị mắc kẹt trong hệ thống" (Delivery Drivers, Stuck in the System - Tạp chí Nhân vật Renwu 2020): Cách thuật toán AI liên tục nén thời gian giao hàng từng phút, biến shipper thành con quay sinh học.
   - Đòn trừng phạt chống độc quyền của Cơ quan Quản lý Thị trường Trung Quốc (SAMR 2021): Xử phạt Alibaba 2,8 tỷ USD, Meituan 530 triệu USD vì hành vi ép buộc "Chọn 1 trong 2" (二选一) và lệnh buộc đóng an sinh xã hội cho người giao hàng.

2. CÔNG XƯỞNG TOÀN CẦU VÀ CHUỖI F2C (PINDUODUO / TEMU & DOUYIN/TIKTOK SHOP):
   - Mô hình Factory-to-Consumer (F2C / M2C): Tận dụng quy mô công nghiệp tỷ dân ( = C_var + (T+E)/V$) để bán hàng thẳng từ xưởng tới tay người tiêu dùng toàn cầu, xóa sổ các tầng nấc bán buôn truyền thống.
   - Cơ chế bóp nghẹt nhà sản xuất: Thuật toán ép hạ giá tự động, chính sách "hoàn tiền không cần trả hàng" (Returnless Refund) đẩy toàn bộ rủi ro cho xưởng.
   - Thương mại nội dung (Shoppertainment) trên Douyin/TikTok: Thuật toán bóp reach hữu cơ để ép người bán mua traffic trả phí, vòng quay đào thải KOC/Creator.
```

---

### 📌 PROMPT 4: ĐỘNG LỰC HỌC VA CHẠM TAM GIÁC & PHẢN ỨNG XÃ HỘI (THE TRIPARTITE CLASH)

* **Mục tiêu nghiên cứu:** Giải phẫu cuộc chiến quyền lợi giữa 3 đỉnh tam giác (Nền tảng $\leftrightarrow$ Nhà cung ứng/Lao động $\leftrightarrow$ Người tiêu dùng) và các chiến thuật phản kháng sinh tồn.
* **Nội dung Prompt nạp vào NotebookLM:**
```text
Phân tích kinh tế học và xã hội học về Sự Va Chạm Tam Giác Cấu Trúc (The Tripartite Structural Clash) trong nền kinh tế nền tảng:

1. NỀN TẢNG VS. NHÀ CUNG ỨNG / LAO ĐỘNG (THE SUPPLY SIDE):
   - Khái niệm "Nông nô kỹ thuật số" (Digital Sharecropping) và "Giai cấp bấp bênh" (The Precariat - Guy Standing).
   - Sự bất đối xứng tài sản cố định: Lao động/Tiểu thương gánh toàn bộ chi phí tài sản suy hao (xe cộ, xăng dầu, điện thoại, tồn kho) trong khi nền tảng sở hữu phần mềm nhẹ và dữ liệu vô hình.
   - Bẫy nợ tài chính và chi phí chìm (Sunk Cost Trap): Vay nợ ngân hàng mua ô tô/xe máy chạy app; đầu tư kho bãi khiến người tham gia không thể rút lui.

2. NỀN TẢNG VS. NGƯỜI TIÊU DÙNG (THE DEMAND SIDE):
   - Tù nhân hành vi: Khi các giải pháp thay thế ngoài đời thực (xe ôm truyền thống, sạp chợ dân sinh) bị triệt tiêu, người tiêu dùng trở thành con tin bị phân biệt giá (Price Discrimination), gánh thêm phụ phí nền tảng và chất lượng dịch vụ suy giảm.

3. XUNG ĐỘT NGANG GIỮA BÊN CUNG VÀ BÊN CẦU:
   - Cơ chế "chuyển lửa" của nền tảng: Nền tảng giấu mình sau thuật toán hộp đen, biến mâu thuẫn thành xung đột trực tiếp giữa tài xế và khách (hủy chuyến, xin tip), giữa chủ shop và người mua (bom hàng, tráo hàng trả lại).

4. CHIẾN TRANH DU KÍCH VÀ PHẢN KHÁNG SINH TỒN:
   - Các đợt đình công tắt app, đặt cuốc xe ma (Ghost Bookings) tại London, New York, Jakarta, Hà Nội.
   - Làn sóng di cư về "Ao riêng" (Private Domain Migration): Người bán lách thuật toán kéo khách về kênh cá nhân (WhatsApp, Zalo, Website D2C) để thoát vòng kiềm tỏa phí sàn.
```

---

### 📌 PROMPT 5: BÀN CỜ THỂ CHẾ TOÀN CẦU & LÁT CẮT THỰC NGHIỆM ĐÔNG NAM Á / VIỆT NAM (GLOBAL REGULATORY & SEA/VN CRUCIBLE)

* **Mục tiêu nghiên cứu:** Đối sánh các khung can thiệp pháp lý trên thế giới và phân tích Đông Nam Á / Việt Nam như một chiến trường thử nghiệm nơi hội tụ cả hai làn sóng phương Tây và phương Bắc.
* **Nội dung Prompt nạp vào NotebookLM:**
```text
Nghiên cứu so sánh về các phản ứng thể chế toàn cầu và Lát cắt thực nghiệm tại Đông Nam Á & Việt Nam:

1. CÁC KHUNG PHÁP LÝ ĐIỀU TIẾT QUỐC TẾ:
   - Liên minh Châu Âu (EU): Đạo luật Thị trường Số (Digital Markets Act - DMA) kiểm soát các "Người gác cổng" (Gatekeepers); Chỉ thị Lao động Nền tảng (Platform Work Directive) đảo ngược nghĩa vụ chứng minh quan hệ lao động (presumption of employment).
   - Indonesia: Quy định số 27/2026 áp trần hoa hồng xe công nghệ tối đa 8%; lệnh cấm giao dịch thương mại trực tiếp trên mạng xã hội năm 2023 buộc TikTok Shop phải mua lại Tokopedia.

2. ĐÔNG NAM Á & VIỆT NAM — NƠI HỘI LƯU CỦA HAI CỖ MÁY:
   - Sự du nhập của mô hình gọi xe phương Tây (Grab thâu tóm Uber, Gojek rút lui tạo thế độc quyền) kết hợp với mô hình TMĐT/Live-commerce phương Bắc (Shopee và TikTok Shop chiếm 97% GMV).
   - Lỗ hổng thể chế lao động: Hơn 300.000 tài xế bị xếp vào Hợp đồng Hợp tác Kinh doanh (BCC), không có BHXH bắt buộc hay quyền thương lượng tập thể.
   - Đòn tấn công chuỗi cung ứng biên giới: Cụm kho ngoại quan Bằng Tường (Pingxiang) cách biên giới 9km với 4-5 triệu đơn/ngày; chính sách chấm dứt miễn thuế VAT hàng dưới 1 triệu VNĐ (QĐ 01/2025/QĐ-TTg) và dự thảo hạ trần miễn thuế nhập khẩu xuống 100.000 VNĐ.
```

---

## 🔬 III. DANH SÁCH 10 CÂU HỎI TRÍCH XUẤT CHUYÊN SÂU (OPTIMIZED EXTRACTION QUERIES)

*Sau khi nạp xong 5 prompts vào Master Notebook, hệ thống sẽ thực hiện Batch Extraction ra 10 file Markdown trong `research_vault/`:*

| Mã Vault | Tiêu Đề Trích Xuất | Bản Chất Câu Hỏi & Trọng Tâm Dữ Liệu Cần Khai Thác |
|---|---|---|
| `001_MSP` | **Kinh tế học Thị trường Đa diện & Bẫy Khóa Hành Vi** | Phân tích lý thuyết Tirole về định giá bất đối xứng, trợ giá chéo  < MC$, cơ chế tạo phản xạ sinh học và bẫy chi phí chuyển đổi. |
| `002_ENSHIT` | **Quy luật Suy thoái Enshittification & Trích xuất Địa tô** | Mổ xẻ 3 giai đoạn của Cory Doctorow và phân tích bản chất việc tư nhân hóa hạ tầng công cộng thành khâu siêu trung gian thu tô. |
| `003_UBER_AMZN` | **Nguyên mẫu Mỹ: Từ Tiền Rẻ ZIRP Đến Cuộc Siết Nợ Phố Wall** | Dữ liệu tài chính Uber đốt 32 tỷ USD, tỷ lệ take rate tăng từ 20% lên 40%; Vụ kiện FTC vs Amazon bóc trần trích thu >50% doanh thu người bán. |
| `004_MEITUAN_AI` | **Nguyên mẫu Trung Quốc: Chuyên Chế Thuật Toán Giao Vận** | Báo cáo điều tra 2020 về shipper Meituan; án phạt SAMR 530 triệu USD; cơ chế thuật toán nén thời gian và trò chơi hóa (gamification). |
| `005_F2C_SUPPLY` | **Chuỗi Cung Ứng F2C & Cơn Bão Hàng Xưởng Biên Giới** | Phương trình quy mô công nghiệp tỷ dân; cơ chế kho Pingxiang 4-5 triệu đơn/ngày; chính sách hoàn tiền không trả hàng đè bẹp tiểu thương nội địa. |
| `006_PRECARIAT` | **Giai cấp Bấp bênh & Bẫy Chi Phí Chìm của Lao Động** | Khái niệm The Precariat của Guy Standing; bất đối xứng tài sản (lao động ôm nợ mua xe/kho hàng, app ôm phần mềm); đơn giá cước thực tế và unit economics tài xế. |
| `007_SELLER_FEE` | **Ma Trận Phí Sàn TMĐT & Sự Biến Chất của Creator** | Phân tích cơ cấu phí cố định, phí xử lý thanh toán, phí hạ tầng, phí voucher; việc bóp reach hữu cơ ép mua ads và cắt giảm hoa hồng KOC. |
| `008_TRIPARTITE` | **Giải Phẫu Cuộc Xung Đột Tam Giác: Nền Tảng - Đối Tác - Khách Hàng** | Nền tảng chia để trị, đẩy mâu thuẫn thành xung đột ngang giữa tài xế - khách và shop - người mua; thuật toán định giá phân biệt người dùng. |
| `009_RESISTANCE` | **Chiến Tranh Du Kích & Làn Sóng Di Cư Về "Ao Riêng"** | Các hình thức phản kháng: đình công tắt app, cuốc xe ma, kẹp mã QR vào kiện hàng, dùng tiếng lóng livestream, rút lui về Private Domain (Zalo/D2C). |
| `010_REGULATION` | **Bàn Cờ Can Thiệp Thể Chế: Từ Quốc Tế Đến Việt Nam** | So sánh EU DMA, EU Platform Directive, Indonesia trần phí 8% vs Lỗ hổng Hợp đồng BCC Việt Nam, chính sách thuế VAT hàng nhập khẩu giá trị nhỏ. |

---

## 🛠️ IV. LỘ TRÌNH THỰC THI KỸ THUẬT (EXECUTION RUNBOOK)

1. **Bước 1 (Vệ sinh Notebook):** 
   - Chạy lệnh `notebooklm source clean -n 7069c72d-fe15-436c-9c21-57ac114117ec -y` để dọn sạch 6 nguồn lỗi.
2. **Bước 2 (Nạp nguồn phân hạch):**
   - Kích hoạt tuần tự 5 lệnh `notebooklm source add-research` tương ứng với 5 Prompts ở Mục II (`BypassSandbox: true`, `--mode deep`, `--import-all`, `--timeout 1800`).
3. **Bước 3 (Trích xuất đa tầng):**
   - Chạy vòng lặp trích xuất 10 câu hỏi ở Mục III bằng `notebooklm ask` lưu vào `episodes/bay-mat-ngot-kinh-te-nen-tang/research_vault/`.
4. **Bước 4 (Tái thiết Bức Tranh Toàn Cảnh & Bản Đồ Dữ Liệu):**
   - Cập nhật toàn diện `02_research_map.md` (bổ sung data points quốc tế Uber, Amazon, Meituan, EU, Indonesia).
   - Tái lập `vault/00_Global_Vision_Synthesis.md` (Pha 2.5) theo đúng Khung 4 Tầng Phổ Quát, lấy lý thuyết kinh tế học hệ thống làm gốc rễ bất biến.