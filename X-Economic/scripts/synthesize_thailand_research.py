#!/usr/bin/env python3
"""
Generate 01_topic_qualification.md, 02_research_map.md, and 02_research_synthesis.md
for episode: thai-lan-no-ngap-dau-vet-xe-do-nhat-ban.
"""

import os
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast")
EPISODE_DIR = WORKSPACE_ROOT / "episodes" / "thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"

topic_qualification_content = """# Pha 1: Topic Qualification & Strategic Angle Review
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu & Vết xe đổ của Nhật Bản

### 1. Thẩm định Tiềm năng Nội dung (Socio-Political Strategy Council)
- **Tên Kênh:** GocNhinPodcast (YouTube Handle: `@GocNhin_Podcast`)
- **Định vị Chủ đề:** Phân tích vĩ mô, kinh tế chính trị so sánh (Comparative Macroeconomics & Development Economics).
- **Core Hook:** Thái Lan từng là "con hổ kinh tế" đi trước cả Đông Nam Á, là hình mẫu công nghiệp hóa và du lịch mà cả khu vực ngưỡng mộ. Nhưng hôm nay, Thái Lan đang rơi vào một thảm kịch kinh tế chưa từng có: **Lãi suất chính sách chỉ 1% (thấp kỷ lục, sắp thấp hơn cả Nhật Bản), nhưng không ai thèm vay tiền; nợ hộ gia đình cán mốc 86-90% GDP bóp nghẹt toàn bộ sức mua; dân số già hóa siêu tốc với tỷ lệ sinh sụp đổ; thủ phủ ô tô "Detroit Đông Nam Á" lung lay trước làn sóng xe điện Trung Quốc; và nguy cơ "Nhật Bản hóa" biến Thái Lan thành quốc gia "chưa kịp giàu đã già" đầu tiên tại châu Á.**

### 2. Tranh luận Đa chiều (Debate Matrix)
- **Viral Alchemist (Góc nhìn Kích thích Tò mò & Chấn động):**
  * Tấn công thẳng vào cú sốc tâm lý: Tại sao một đất nước giàu có, du lịch sầm uất, xe hơi chạy đầy đường như Thái Lan lại đang "nợ ngập đầu" và đứng trước nguy cơ mất trắng 30 năm tương lai?
  * Sự so sánh trực diện với Nhật Bản: Nhật Bản mất mát 30 năm khi đã là siêu cường kinh tế giàu có thế giới. Còn Thái Lan lại đang sao chép toàn bộ căn bệnh của Nhật Bản khi thu nhập bình quân đầu người mới chỉ bằng 1/4 Nhật Bản!
- **Policy Analyst (Góc nhìn Nhà Kinh tế Học & Chính sách):**
  * Sử dụng khung lý thuyết **Suy thoái Bảng cân đối Kế toán (Balance Sheet Recession)** của Richard Koo để giải thích tại sao chính sách tiền tệ lãi suất 1% bị vô hiệu hóa hoàn toàn (Bẫy thanh khoản).
  * Phân tích sự đứt gãy giữa 3 tầng nợ: Nợ hộ gia đình (86% GDP) $\rightarrow$ Nợ doanh nghiệp thây ma (Zombiefication) $\rightarrow$ Nợ công kịch trần (66-70% GDP).
  * Bóc tách sự sụp đổ của chuỗi cung ứng linh kiện xe xăng truyền thống trước xe điện Trung Quốc và bế tắc của các gói kích thích tiêu dùng ngắn hạn (Digital Wallet).
- **Critical Auditor (Góc nhìn Phản biện & Tuân thủ An toàn):**
  * Cần giữ vững tính khách quan báo chí kinh tế, dựa 100% vào số liệu thực chứng từ Bank of Thailand (BoT), World Bank, IMF, HSBC, Oxford Economics.
  * Không phán xét tiêu cực văn hóa hay thể chế chính trị Thái Lan; tập trung thuần túy vào các quy luật kinh tế học, cơ cấu nhân khẩu học và bài học chiến lược chuyển dịch công nghệ.
- **People's Lens (Góc nhìn Đời sống & Đồng cảm Xã hội):**
  * Đặt câu hỏi thực tế: Tại sao người dân Thái Lan thu nhập 15.000 - 20.000 THB/tháng lại gánh tới 3-4 khoản nợ (mua nhà, mua xe, thẻ tín dụng, BNPL và tín dụng đen)?
  * Nỗi đau của "Thế hệ bánh mì kẹp" (Sandwich Generation): Vừa phải gánh nợ cá nhân, vừa phải chu cấp tới 78% chi phí sinh hoạt cho cha mẹ già trong bối cảnh hệ thống lương hưu công không đủ sống.

### 3. Phán quyết Chiến lược (Council Verdict)
- **Quyết định:** DUYỆT 100% TRIỂN KHAI VÀO PRODUCTION.
- **Tiềm năng Đón nhận:** Cực kỳ cao, chạm đúng mối quan tâm về bẫy nợ tiêu dùng, bài học phát triển kinh tế cho Việt Nam, và hiện tượng "Nhật Bản hóa" đang được quan tâm toàn cầu.
"""

research_map_content = """# Pha 2: Research Map & Master Source Registry
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu & Vết xe đổ của Nhật Bản

### 1. Master Notebook Metadata
- **Master Notebook Name:** `[GÓC NHÌN PODCAST] Khủng hoảng Kinh tế Thái Lan - Vết xe đổ của Nhật Bản`
- **Master Notebook ID:** `8adfb492-f87a-4b6c-94e1-9f75d454a18b`
- **Master Notebook URL:** `https://notebooklm.google.com/notebook/8adfb492-f87a-4b6c-94e1-9f75d454a18b`
- **Tổng số Nguồn Dữ liệu Học thuật Nạp qua Deep Research:** 133 nguồn (Nghiên cứu sâu `--mode deep` đa tầng).

---

### 2. Cấu trúc Cây Dữ liệu Vault (Research Vault Registry)

| File Vault | Chủ đề Chuyên sâu | Mỏ neo Dữ liệu Cốt lõi (Data Anchors) |
|---|---|---|
| `01_no_ho_gia_dinh_va_bay_thanh_khoan.md` | Nợ hộ gia đình, Lãi suất 1% & Bẫy thanh khoản | - Nợ hộ gia đình: **85,9% - 86,8% GDP** (~**16,3 nghìn tỷ THB**), cao nhất nhóm Upper-Middle Income.<br>- Lãi suất BoT: **1,0%** (thấp thứ 2 thế giới sau Thụy Sĩ).<br>- Tỷ lệ từ chối vay mua ô tô: **70%**.<br>- Tài khoản BNPL tăng **99,9%/năm** (lên 5 triệu TK); Nhóm 20-35 tuổi nợ **52,7%**, NPL **27%**.<br>- Trần lãi suất: P-Loans (25%), Nano Finance (33%), Pico Finance (36%), Tín dụng đen (**>20%/tháng**). |
| `02_nhat_ban_hoa_va_suy_thoai_bctc.md` | Hiện tượng "Nhật Bản hóa" & Lý thuyết BSR Richard Koo | - Giảm phát **12 tháng liên tiếp**; Tăng trưởng quanh **2%**.<br>- Đối sánh Nhật Bản vs Thái Lan: Nhật Bản (GDP/người > **30.000 USD**, nợ doanh nghiệp, thặng dư tài sản ròng lớn nhất TG); Thái Lan (GDP/người chỉ **~7.000 USD**, nợ hộ gia đình bóp nghẹt cầu, nợ công **66,1% GDP** sát trần 70%).<br>- Hiện tượng Doanh nghiệp thây ma (Zombiefication). |
| `03_nhan_khau_hoc_chua_giau_da_gia.md` | Khủng hoảng Nhân khẩu học "Chưa giàu đã già" | - Tổng tỷ suất sinh TFR chạm đáy lịch sử: **0,76 - 1,16**.<br>- Số ca sinh sụt giảm dưới **400.000 trẻ/năm**.<br>- Tỷ lệ phụ thuộc người già (OADR) tăng từ **28,4** lên **56,2** vào năm 2040.<br>- Lực lượng lao động suy giảm **1,0%/năm**; Dự báo dân số giảm từ **67 triệu xuống 30 triệu** trong 50 năm.<br>- An sinh xã hội: Con cái chu cấp **77,8%** chi phí người già (Bẫy Sandwich Generation). |
| `04_khung_hoang_detroit_dong_nam_a_va_xe_dien.md` | Cú sụp đổ của "Detroit Đông Nam Á" & Làn sóng EV TQ | - Từng sản xuất **2 triệu xe/năm** (Toyota, Isuzu, Honda).<br>- Xe điện Trung Quốc (BYD, GWM, Changan) chiếm lĩnh thị phần, giá rẻ hơn xe xăng **11,8%**.<br>- Chuỗi cung ứng phụ trợ Tier-2, Tier-3 Thái Lan bị gạt khỏi chuỗi EV (nhập khẩu pin/motor từ TQ) $\rightarrow$ Phá sản hàng loạt.<br>- R&D chỉ chiếm **1,2% GDP**, kẹt ở đáy "Đường cong nụ cười" (Smile Curve). |
| `05_be_tac_tai_khoa_va_dong_luc_du_lich.md` | Bế tắc Tài khóa & Động lực Du lịch suy yếu | - Nợ công: **66,1% GDP** (tiến sát trần an toàn **70%**), dư địa chỉ còn ~800 tỷ THB.<br>- Gói phát tiền số Digital Wallet **500 tỷ THB** (10.000 THB/người) gây lo ngại bào mòn không gian tài khóa.<br>- Du lịch (12-18% GDP) phục hồi số lượng nhưng chi tiêu bình quân giảm; hàng giá rẻ TMĐT Trung Quốc (Temu, Shein, TikTok Shop) tràn ngập bóp chết sản xuất nội địa. |
| `06_bai_hoc_canh_tinh_cho_viet_nam.md` | Bài học Cảnh tỉnh Chiến lược cho Việt Nam | - Nhận diện sớm rủi ro nợ tiêu dùng cá nhân & tín dụng đen.<br>- Tận dụng tối đa "Cửa sổ Dân số Vàng" (dự kiến kết thúc quanh 2036).<br>- Tự chủ công nghệ lõi & chuỗi cung ứng thay vì thuần túy gia công FDI.<br>- Tránh bẫy thu nhập trung bình bằng nâng cao năng suất TFP. |
"""

research_synthesis_content = """# Pha 2: Báo cáo Tổng hợp Nghiên cứu Sâu (Research Synthesis)
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản & Bài học Cảnh tỉnh Đông Nam Á

---

## 1. Bản chất Khủng hoảng: Khi "Con Hổ Châu Á" Mắc Bẫy Bảng Cân Đối Kế Toán

Thái Lan từng là ngọn cờ đầu trong làn sóng công nghiệp hóa Đông Nam Á thập niên 1980–1990, được ca ngợi là "Con hổ thứ năm của châu Á" và "Detroit của phương Đông". Tuy nhiên, bước sang năm 2026, quốc gia 67 triệu dân này đang trở thành tâm điểm của một cuộc khủng hoảng vĩ mô trầm trọng: **Hiện tượng "Nhật Bản hóa" (Japanification) xảy ra tại một nền kinh tế đang phát triển.**

Khác với các cuộc khủng hoảng tài chính truyền thống bắt nguồn từ tỷ giá hay thâm hụt cán cân thanh toán ngoại hối (như Khủng hoảng Tom Yum Goong 1997), cuộc khủng hoảng hiện tại của Thái Lan là một **căn bệnh thoái hóa cơ cấu nội tại (Structural Degenerative Crisis)**.

### Sơ đồ Cơ chế Lan truyền Bẫy Bảng Cân Đối Kế Toán (Richard Koo Framework)

```
[NỢ HỘ GIA ĐÌNH 86-90% GDP] ───► [CHUYỂN SANG CHẾ ĐỘ "TỐI THIỂU HÓA NỢ"]
              │                                      │
              ▼                                      ▼
[THẮT LƯNG BUỘC BỤNG TRẢ NỢ] ◄──── [TỪ CHỐI VAY MỚI DÙ LÃI SUẤT 1%]
              │                                      │
              ▼                                      ▼
[TỔNG CẦU NỘI ĐỊA TÊ LIỆT] ──────► [DOANH NGHIỆP CẮT GIẢM ĐẦU TƯ]
              │                                      │
              ▼                                      ▼
[GIẢM PHÁT / THIỂU PHÁT KÉO DÀI] ◄── [BẪY TĂNG TRƯỞNG TRÌ TRỆ 1-2%]
              │
              ▼
[NỢ CÔNG ÁP SÁT TRẦN 70% GDP ── KHÔNG CÒN DƯ ĐỊA TÀI KHÓA ĐỂ CỨU CẦU]
```

---

## 2. 5 Trụ Cột Giải Mã Khủng Hoảng Kinh Tế Thái Lan

### Trụ cột 1: Bẫy Nợ Hộ Gia Đình (86-90% GDP) & Bẫy Thanh Khoản (Lãi suất 1%)
- **Mức nợ kỷ lục:** Tỷ lệ nợ hộ gia đình Thái Lan đạt **85,9% - 86,8% GDP** (tương đương **16,3 nghìn tỷ THB**), cao nhất trong số các quốc gia thu nhập trung bình cao toàn cầu (theo HSBC).
- **Cơ cấu nợ đa tầng độc hại:**
  * Vay mua nhà (Mortgage) là nguồn nợ xấu lớn nhất.
  * Vay mua xe (Auto loan) từng bùng nổ từ chính sách hoàn thuế xe đầu tiên (2011-2013), nay để lại di chứng nặng nề với tỷ lệ ngân hàng từ chối cho vay mua xe lên tới **70%**.
  * Bùng nổ tín dụng tiêu dùng vi mô & Mua trước trả sau (BNPL): Tài khoản BNPL tăng trưởng phi mã **99,9%/năm** (đạt gần 5 triệu tài khoản). Đáng báo động, nhóm người trẻ 20–35 tuổi chiếm **52,7%** tổng số người mắc nợ và có tỷ lệ nợ xấu lên đến **27%**.
  * Tầng nợ đen (Loan Sharks): Lãi suất vượt **20%/tháng**, bổ sung thêm trung bình 100.000 - 200.000 THB nợ cho mỗi hộ gia đình nông thôn không có tài sản thế chấp.
- **Sự vô hiệu hóa của chính sách tiền tệ (Monetary Transmission Failure):**
  * Ngân hàng Trung ương Thái Lan (BoT) giữ lãi suất sàn ở mức **1,0%** (thấp thứ 2 thế giới, chỉ trên Thụy Sĩ). Nhiều dự báo Thái Lan sẽ sớm có lãi suất thấp hơn cả Nhật Bản.
  * Tuy nhiên, việc hạ lãi suất không kích thích được vay mượn. Theo lý thuyết của Richard Koo, nền kinh tế đã rơi vào **Pha Yin (Suy thoái Bảng cân đối Kế toán)**: Người dân và doanh nghiệp dùng mọi đồng tiền kiếm được để trả nợ cũ thay vì vay mới để chi tiêu hoặc mở rộng sản xuất. Trợ lý Thống đốc BoT Don Nakornthab thừa nhận: Chính sách tiền tệ "gần như đã chạm giới hạn".

---

### Trụ cột 2: Nghịch lý "Chưa Giàu Đã Già" — Sự Khác biệt Chí Mạng với Nhật Bản
Khi người ta so sánh Thái Lan với "Thập niên mất mát" của Nhật Bản, có một sự thật tàn nhẫn về cấu trúc nội tại:

| Chỉ số Đối sánh | Nhật Bản (1990s) | Thái Lan (Hiện tại 2026) |
|---|---|---|
| **GDP bình quân đầu người** | **> 30.000 USD** (Nước giàu phát triển) | **~ 7.000 - 7.500 USD** (Mắc kẹt ở thu nhập trung bình) |
| **Bản chất Nợ gây BSR** | Nợ doanh nghiệp bất động sản (Hộ gia đình tiết kiệm cao) | Nợ hộ gia đình tiêu dùng (Bóp chết trực tiếp sức mua dân sinh) |
| **Không gian Tài khóa** | Rộng rãi (Dân giàu cho chính phủ vay nợ công 200% GDP) | Kiệt quệ (Nợ công **66,1%**, sát trần pháp lý **70% GDP**) |
| **Vị thế Quốc tế** | Quốc gia chủ nợ lớn nhất thế giới, làm chủ công nghệ nguồn | Gia công ở đáy Smile Curve, thặng dư mỏng manh |
| **Hệ thống An sinh** | Nhà nước bảo trợ an sinh toàn diện (BGR = 0,369) | Dựa vào gia đình (BGR = 0,091). Con cái gánh **77,8%** chi phí |
| **Tỷ suất sinh (TFR)** | Giảm từ tốn | Sụp đổ lịch sử xuống **0,76 - 1,16** (<400.000 trẻ/năm) |

> 📌 **Kết luận then chốt:** Nhật Bản mất mát 30 năm với tư cách một **"người giàu có nhiều của cải tích lũy và sức đề kháng cao"**. Còn Thái Lan đang đối mặt với thảm kịch của một **"người nghèo bị bệnh mãn tính khi vừa bước sang tuổi già"**.

---

### Trụ cột 3: Cú Sụp Đổ Của "Detroit Đông Nam Á" Trước Xe Điện Trung Quốc
- **Thời hoàng kim:** Thái Lan từng xây dựng thành công cụm công nghiệp ô tô sản lượng 2 triệu xe/năm, phụ thuộc hoàn toàn vào hệ sinh thái xe động cơ đốt trong (ICE) của các hãng Nhật Bản (Toyota, Isuzu, Honda, Nissan).
- **Cú đấm kép từ làn sóng EV Trung Quốc:**
  * Các hãng xe điện Trung Quốc (BYD, Great Wall Motors, Changan, Neta) đổ bộ ồ ạt, tung chiến dịch giảm giá khiến xe điện rẻ hơn xe xăng truyền thống khoảng **11,8%**.
  * **Thảm kịch linh kiện phụ trợ:** Khác với xe Nhật Bản sử dụng tới 70-80% linh kiện nội địa Thái Lan, các hãng xe điện Trung Quốc nhập khẩu trực tiếp các bộ phận giá trị cao nhất (Pin, Động cơ điện, Chip điều khiển) từ chuỗi cung ứng chính quốc Trung Quốc.
  * Hàng trăm nhà máy phụ trợ cơ khí, dập kim loại, đúc linh kiện cấp Tier-2, Tier-3 của Thái Lan phá sản hoặc đóng cửa hàng loạt.
  * Thái Lan bị kẹt ở đáy **"Đường cong nụ cười" (Smile Curve)**: Không làm chủ thiết kế, không sở hữu công nghệ pin, R&D chỉ chiếm **1,2% GDP**, dẫn đến hiện tượng **Phi công nghiệp hóa sớm (Premature De-industrialization)**.

---

### Trụ cột 4: Bế Tắc Tài Khóa & Động Lực Tăng Trưởng Truyền Thống Suy Kiệt
- **Nợ công áp sát giới hạn đỏ:** Nợ công đạt **66,1% GDP**, trần luật định là **70% GDP**. Dư địa tài khóa khả dụng chỉ còn khoảng 800 tỷ THB, khiến chính phủ không thể tung ra các gói giải cứu quy mô lớn.
- **Tranh cãi Gói Phát tiền số Digital Wallet (500 tỷ THB):** Đề xuất phát 10.000 THB cho mỗi người dân bị các nhà kinh tế học và Thống đốc BoT Sethaput Suthiwartnarueput phản đối kịch liệt vì chỉ giải quyết triệu chứng tiêu dùng ngắn hạn trong vài tháng nhưng để lại di chứng nợ công nặng nề cho ngân sách quốc gia.
- **Trụ cột Du lịch đuối sức:** Du lịch chiếm 12-18% GDP dù đón lượng khách đông nhưng chi tiêu bình quân trên mỗi đầu khách giảm sút rõ rệt.
- **Bị cạnh tranh bóp nghẹt:** Hàng hóa giá rẻ Trung Quốc qua thương mại điện tử (Temu, Shein, TikTok Shop) tràn ngập khiến các doanh nghiệp sản xuất tiêu dùng nội địa Thái Lan tê liệt.

---

### Trụ cột 5: Bài Học Cảnh Tỉnh Chiến Lược Đối Với Việt Nam
1. **Kiểm soát chặt chẽ đòn bẩy nợ tiêu dùng và bong bóng tài sản:** Không để nợ hộ gia đình vượt quá ngưỡng an toàn 60-70% GDP; siết chặt các hình thức tín dụng đen, cho vay ngang hàng (P2P), BNPL không kiểm soát.
2. **Chạy đua với "Cửa sổ Dân số Vàng":** Thời kỳ dân số vàng của Việt Nam dự kiến sẽ khép lại vào khoảng năm 2036. Việt Nam phải hoàn thành công nghiệp hóa và bứt phá thu nhập bình quân trước khi bước vào giai đoạn siêu già hóa như Thái Lan.
3. **Chuyển từ "Gia công FDI" sang "Làm chủ Công nghệ Nguồn":** Bài học xe điện Thái Lan cho thấy nếu chỉ dừng lại ở lắp ráp thuê cho nước ngoài mà không xây dựng được các doanh nghiệp dân tộc dẫn dắt và chuỗi cung ứng nội địa tự chủ, nền công nghiệp sẽ lập tức sụp đổ khi công nghệ chuyển giao thế hệ.
4. **Nâng cao Năng suất Nhân tố Tổng hợp (TFP):** Động lực tăng trưởng tương lai không thể dựa mãi vào thâm dụng lao động giá rẻ hay bơm tín dụng bất động sản, mà bắt buộc phải dựa vào kinh tế số, công nghệ cao và cải cách thể chế.

---

## 3. Khung Lập Luận Kịch Bản Podcast Đề Xuất (7 Chương Chuẩn)

- **CH01: Cơn Sốt Lạnh 1% và Nghịch Lý Con Hổ Đông Nam Á** (Hook bùng nổ, đối lập giữa hào nhoáng bên ngoài và căn bệnh tê liệt tín dụng bên trong).
- **CH02: Bẫy Nợ Hộ Gia Đình — Khi Cả Quốc Gia Đi Làm Để Trả Lãi** (Phân tích nợ 86-90% GDP, BNPL, thế hệ trẻ kẹt nợ).
- **CH03: Lời Nguyền Richard Koo — Vì Sao Tiền Rẻ Không Thể Cứu Nổi Thái Lan?** (Giải thích cơ chế BSR và bẫy thanh khoản một cách đời thường, hấp dẫn).
- **CH04: "Chưa Giàu Đã Già" — Sự Khác Biệt Tàn Nhẫn Với Nhật Bản** (So sánh đối đầu giữa Nhật Bản 1990 vs Thái Lan 2026).
- **CH05: Detroit Phương Đông Sụp Đổ — Khi Xe Điện Trung Quốc Quét Sạch Giấc Mơ Công Nghiệp** (Cú sốc xe điện, chuỗi cung ứng nội địa phá sản).
- **CH06: Chiếc Ví Kỹ Thuật Số 500 Tỷ Baht và Giới Hạn Đỏ Tài Khóa** (Bế tắc chính sách, nợ công 70%, du lịch đuối sức).
- **CH07: Hồi Chuông Cảnh Tỉnh Cho Việt Nam — Chạy Đua Trước Khi Cánh Cửa Khép Lại** (Bài học đúc kết chiến lược, thông điệp tự cường dân tộc).
"""

# Ghi các tệp tin
(EPISODE_DIR / "01_topic_qualification.md").write_text(topic_qualification_content, encoding="utf-8")
(EPISODE_DIR / "02_research_map.md").write_text(research_map_content, encoding="utf-8")
(EPISODE_DIR / "02_research_synthesis.md").write_text(research_synthesis_content, encoding="utf-8")

print("✓ Đã tổng hợp thành công 01_topic_qualification.md, 02_research_map.md, 02_research_synthesis.md!")
