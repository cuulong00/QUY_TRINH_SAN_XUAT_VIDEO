#!/usr/bin/env python3
"""
Generate Pha 3 to Pha 8b artifacts for:
thai-lan-no-ngap-dau-vet-xe-do-nhat-ban

Includes:
- 03_brief.md
- 04_hook_pack.md
- 05_thesis_map.md
- 06_retention_map.md
- 07_outline.md
- 08_chapter_briefs.md
- 09_narrative_state_tracker.md
"""

import os
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/pro16/Documents/VideoProject/X-Economics")
EPISODE_DIR = WORKSPACE_ROOT / "episodes" / "thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"

brief_content = """# 03_brief.md: Strategy Brief
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản & Bài học Cảnh tỉnh Việt Nam

```yaml
episode_slug: thai-lan-no-ngap-dau-vet-xe-do-nhat-ban
working_title: "Khủng Hoảng Kinh Tế Thái Lan: Nợ Ngập Đầu, Vết Xe Đổ Của Nhật Bản & Bài Học Cảnh Tỉnh Cho Việt Nam"
topic: "Kinh tế chính trị học so sánh, Giải phẫu bẫy nợ hộ gia đình 86% GDP, Khủng hoảng nhân khẩu học, Cú sốc chuyển dịch xe điện và Đối sánh vĩ mô Việt Nam - Thái Lan"

target_duration_min: 25
target_duration_max: 35

audience_primary: "Khán giả quan tâm đến kinh tế vĩ mô, đầu tư, chính sách phát triển, địa chính trị và vị thế kinh tế Việt Nam trong khu vực Đông Nam Á"
audience_secondary: "Giới trẻ đô thị, người lao động đang gánh nợ tiêu dùng/mua nhà, các chủ doanh nghiệp SME quan tâm đến quản trị tài chính và chuỗi cung ứng"
audience_sophistication: "Trung bình đến Nâng cao (Cần giải thích thuật ngữ chuyên môn như Balance Sheet Recession, Liquidity Trap, Smile Curve bằng ngôn ngữ đời thường và phép loại suy sinh động)"

viewer_moment_of_pain: "Chứng kiến một quốc gia láng giềng từng là hình mẫu giàu có, du lịch sầm uất nay rơi vào bế tắc nợ nần, từ đó lo lắng cho tương lai kinh tế cá nhân và đất nước"
core_pain: "Nỗi sợ mắc bẫy nợ tiêu dùng, bẫy thu nhập trung bình và nguy cơ 'chưa giàu đã già' khi cơ hội Dân số Vàng trôi qua"
surface_symptoms: "Lãi suất 1% không ai thèm vay, nợ hộ gia đình ngập đầu 86% GDP, xe điện Trung Quốc tràn ngập, nhà máy linh kiện đóng cửa, giới trẻ gánh nợ BNPL"
deep_cause_hypothesis: "Căn bệnh Suy thoái Bảng cân đối Kế toán (Richard Koo): Tiền lương thực tế đình trệ biến nợ thành vật thay thế thu nhập; già hóa dân số siêu tốc; chuỗi cung ứng cơ khí cũ bị đào thải; chính phủ cạn kiệt dư địa tài khóa"
false_belief_to_break: "Ảo tưởng rằng 'cứ hạ lãi suất bơm tiền rẻ là kinh tế sẽ hồi phục' và 'Thái Lan sa sút giống hệt Nhật Bản' (thực tế Thái Lan nguy hiểm hơn Nhật Bản gấp nhiều lần vì chưa kịp tích lũy của cải)"
emotional_stakes: "Hồi chuông cảnh tỉnh khẩn cấp cho mỗi người dân và nhà hoạch định chính sách Việt Nam trước mốc năm 2036"

desired_transformation: "Từ hoang mang hoặc ngạo nghễ chuyển sang nhận thức tỉnh táo, thấu suốt các quy luật kinh tế vĩ mô, quản trị nợ cá nhân chặt chẽ và nâng cao ý thức tự cường dân tộc"
one_sentence_promise: "Bóc trần toàn bộ sự thật đằng sau cơn sốt lãi suất 1% của Thái Lan, giải mã cơ chế bẫy nợ 86% GDP và rút ra những bài học sống còn cho vận mệnh phát triển của Việt Nam"

why_now: "Ngân hàng Trung ương Thái Lan vừa giữ nguyên lãi suất 1% (cuộc họp thứ 3 liên tiếp), nợ hộ gia đình chạm đỉnh lịch sử, GDP PPP Việt Nam chính thức vượt Thái Lan năm 2026 (IMF), và làn sóng xe điện Trung Quốc đang định hình lại toàn bộ công nghiệp Đông Nam Á"
virality_hypothesis: "Đánh trúng tâm lý so sánh lịch sử 50 năm giữa Việt Nam và Thái Lan, kết hợp giải phẫu nợ cá nhân (chủ đề nóng của Gen Z và Millennials)"
ctr_hypothesis: "Thumbnail 3 tầng chữ tương phản cực mạnh giữa hình ảnh hào nhoáng của Bangkok và con số nợ ngập đầu, tạo cảm giác giật mình phải bấm vào xem ngay"
retention_hypothesis: "Mở đầu bằng nghịch lý 1% chấn động, cài cắm các vòng lặp hồi hộp (Dopamine Drops) qua từng chương từ giải phẫu nợ, bẫy Richard Koo, cú sốc xe điện đến bản đối sánh toàn lực Việt Nam"

tone: "Điềm tĩnh, đanh thép, học thuật nhưng bình dân hóa sâu sắc, giàu tinh thần trách nhiệm và lòng tự hào dân tộc"
narrative_persona: "Nhà phân tích kinh tế vĩ mô và địa chính trị điềm tĩnh, sắc sảo, khách quan, giàu trải nghiệm thực tiễn"

source_policy:
  - "100% số liệu bám sát 30 mỏ neo bất biến (DATA-01 đến DATA-30) trong vault/00_Global_Vision_Synthesis.md"
  - "Nguồn sự thật: Master Notebook 8adfb492-f87a-4b6c-94e1-9f75d454a18b và 10 chuyên đề trong research_vault/"
  - "Tuyệt đối không bịa đặt số liệu thống kê hoặc suy diễn chủ quan ngoài tài liệu nghiên cứu"

success_criteria:
  - "Hook mở đầu đạt độ căng kịch tính cao, giữ chân khán giả qua 60 giây đầu"
  - "Giải thích thuật ngữ BSR và bẫy thanh khoản cực kỳ dễ hiểu bằng ví dụ thực tế"
  - "Cân bằng tuyệt đối: Không hả hê chê bai Thái Lan, không ngạo mạn tự mãn về Việt Nam, nhìn thẳng vào điểm nghẽn của cả hai nước"
  - "Đúc kết bài học tài chính cá nhân và chiến lược quốc gia sâu sắc, truyền cảm hứng hành động"
```
"""

hook_pack_content = """# 04_hook_pack.md: Hook Lab
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản

---

### OPTION 1: THE PARADOX HOOK (Góc nhìn Nghịch lý Vĩ mô — Được Khuyến Nghị)
> **Headline:** "Lãi Suất 1% Nhưng Không Ai Thèm Vay: Bi Kịch Của Một Đất Nước Đang Đi Làm Để Trả Nợ"

* **0:00 – 0:15 (Cú sốc thính giác & thị giác):**  
  *"Một đất nước mà bạn bước chân ra đường là thấy xe hơi nối đuôi nhau, các trung tâm thương mại lộng lẫy bậc nhất Đông Nam Á, và lãi suất ngân hàng vừa hạ xuống mức chỉ 1% — mức rẻ gần như cho không, thấp hơn cả Thụy Sĩ và sắp thấp hơn cả Nhật Bản. Nhưng kỳ lạ thay, không một ai muốn vay tiền!"*
* **0:15 – 0:35 (Vạch trần bóng tối phía sau):**  
  *"Tại sao một nền kinh tế từng được ca ngợi là 'con hổ thứ năm của châu Á', là thủ phủ ô tô của cả khu vực, hôm nay lại rơi vào một cơn sốt lạnh kỳ dị: Tăng trưởng rơi tự do xuống 1,3%, lạm phát đóng băng, và cứ 10 người dân bước ra đường thì có tới gần 9 người đang gánh trên lưng những khoản nợ ngập đầu?"*
* **0:35 – 0:60 (Lời hứa video & Cầu nối giữ chân):**  
  *"Thái Lan đang bước vào vết xe đổ 30 năm mất mát của Nhật Bản, nhưng theo một kịch bản tàn nhẫn hơn gấp ngàn lần: Đó là bi kịch của một quốc gia 'chưa kịp giàu đã già'. Và điều đáng sợ nhất là: Những mầm mống căn bệnh nợ nần mà người Thái đang gánh chịu, lại đang âm thầm xuất hiện ngay tại các đô thị của Việt Nam. Chào mừng quý vị đến với Góc Nhìn Podcast..."*

---

### OPTION 2: THE DEBT DISASTER HOOK (Góc nhìn Giải phẫu Nợ Cá nhân)
> **Headline:** "16 Nghìn Tỷ Baht Nợ Nần: Khi Cả Một Xã Hội Bị Chiếc Thòng Lọng Tài Chính Xiết Cổ"

* **0:00 – 0:15:**  
  *"Bạn có bao giờ tưởng tượng một ngày, bạn kiếm được 10 đồng tiền lương thì có tới 7 đến 8 đồng tự động chảy vào tài khoản ngân hàng để trả nợ gốc và lãi mua nhà, mua xe, thẻ tín dụng và các app mua trước trả sau? Đó không phải là giả định, mà là cuộc sống thực tế của hàng chục triệu người dân Thái Lan ngay lúc này."*
* **0:15 – 0:35:**  
  *"Với tổng số nợ hộ gia đình vượt mốc 16,3 nghìn tỷ Baht — tương đương gần 87% GDP, Thái Lan chính thức trở thành quốc gia nợ nần nhiều nhất trong nhóm các nước thu nhập trung bình trên thế giới. Hơn 52% thanh niên trẻ tuổi đang mắc nợ, và tỷ lệ ngân hàng từ chối cho vay mua xe đã vọt lên tới 70%."*
* **0:35 – 0:60:**  
  *"Khi cả một quốc gia cắm mặt đi làm chỉ để trả lãi, nền kinh tế sẽ chết lâm sàng như thế nào? Tại sao tiền rẻ của Ngân hàng Trung ương lại trở thành vô dụng? Hãy cùng chúng tôi giải phẫu cuộc khủng hoảng nợ chưa từng có này..."*

---

### OPTION 3: THE STRATEGIC RIVALRY HOOK (Góc nhìn Đối sánh Địa chính trị Việt Nam - Thái Lan)
> **Headline:** "Cuộc Đổi Ngôi Lịch Sử: Khi Việt Nam Vượt Mặt Thái Lan Và Bài Học Cảnh Báo Cho Tương Lai"

* **0:00 – 0:25:**  
  *"Năm 2026, Quỹ Tiền tệ Quốc tế IMF vừa công bố một cột mốc lịch sử: Quy mô kinh tế Việt Nam tính theo sức mua tương đương chính thức vượt qua Thái Lan để vươn lên vị trí thứ hai Đông Nam Á. Chúng ta xuất khẩu gấp 1,5 lần Thái Lan, đón nhận làn sóng công nghệ bán dẫn toàn cầu và duy trì tốc độ tăng trưởng gấp 4 lần họ."*
* **0:25 – 0:60:**  
  *"Nhưng trước khi người Việt kịp ăn mừng, hãy nhìn thẳng vào bức tranh bi kịch của người láng giềng: Thái Lan 15 năm trước từng đứng ở vị trí hoàng kim như chúng ta hôm nay, trước khi bị bóp nghẹt bởi nợ tiêu dùng, già hóa dân số và sự sụp đổ của chuỗi sản xuất ô tô. Liệu Việt Nam có tránh được chiếc bẫy thu nhập trung bình đang chực chờ? Câu trả lời sẽ có ngay sau đây."*

---

### 🏆 PHÁN QUYẾT LỰA CHỌN: OPTION 1 (THE PARADOX HOOK)
- **Lý do lựa chọn:** Kết hợp hoàn hảo giữa cú sốc vĩ mô (lãi suất 1%), hình ảnh đời sống gần gũi (nợ ngập đầu) và lời cảnh báo chiến lược cho người xem Việt Nam. Đảm bảo tỷ lệ giữ chân (Retention) tối đa trong 60 giây đầu.
"""

thesis_map_content = """# 05_thesis_map.md: Thesis & Dialectic Map
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản

| Chương | Core Thesis (Luận điểm trọng tâm) | Antithesis (Góc nhìn ngộ nhận / Phản biện) | Synthesis (Bản chất vĩ mô sâu sắc) |
|---|---|---|---|
| **CH01** | Lãi suất 1% thuộc nhóm thấp nhất thế giới nhưng nền kinh tế rơi vào thiểu phát và tăng trưởng chạm đáy 1.3%. | "Cứ hạ lãi suất thật thấp, bơm tiền rẻ ra thị trường là kích thích được tiêu dùng và sản xuất." | Khi cơ thể kinh tế bị nghẽn mạch nợ nần, hạ lãi suất chỉ làm yếu đồng nội tệ chứ không tạo ra tín dụng thực chất (Bẫy thanh khoản). |
| **CH02** | Nợ hộ gia đình 86-90% GDP (~16.3 nghìn tỷ Baht) biến thành chiếc thòng lọng bóp chết sức mua dân sinh. | "Người dân nợ nhiều vì thích mua sắm hoang phí, xài đồ hiệu, chạy theo trào lưu." | Nợ nần là hệ quả của 10 năm tiền lương thực tế đình trệ, kết hợp sự bùng nổ tín dụng tiêu dùng dễ dãi biến nợ thành vật thay thế thu nhập. |
| **CH03** | Khủng hoảng Thái Lan tuân theo lý thuyết Suy thoái Bảng cân đối Kế toán (Richard Koo): Chuyển sang "tối thiểu hóa nợ". | "Ngân hàng thừa tiền thì sớm muộn dòng vốn cũng sẽ tự động chảy vào các dự án kinh doanh mới." | Người dân thắt lưng buộc bụng trả nợ gốc; ngân hàng sợ nợ xấu giữ thanh khoản phòng ngừa; tiền rẻ chỉ nuôi sống các doanh nghiệp thây ma. |
| **CH04** | "Chưa giàu đã già": Thái Lan già hóa với GDP/người $7.200, an sinh yếu, không thể so sánh với Nhật Bản ($30.000). | "Thái Lan đang giống hệt Nhật Bản thời kỳ bong bóng vỡ 1990, chỉ cần kiên nhẫn kích cầu là sẽ qua." | Nhật Bản có kho mỡ dự trữ khổng lồ và chủ nợ toàn cầu; Thái Lan là 'người nghèo mắc bệnh nan y khi bước sang tuổi già', không có của cải để chịu đựng 30 năm. |
| **CH05** | Ngành ô tô 2 triệu xe/năm sụp đổ vì xe điện Trung Quốc gạt bỏ chuỗi cung ứng linh kiện nội địa Tier-2, Tier-3. | "Thái Lan thu hút 4.1 tỷ USD FDI xe điện từ BYD, GWM là thành công lớn trong chuyển đổi xanh." | EV Trung Quốc nhập 100% pin/motor từ đại lục; Thái Lan kẹt ở đáy Smile Curve (R&D chỉ 1.2% GDP), dẫn đến hiện tượng phi công nghiệp hóa sớm. |
| **CH06** | Nợ công 66.1% áp sát trần 70%, gói Digital Wallet 500 tỷ Baht chỉ là giải pháp dân túy bào mòn dự trữ tài khóa. | "Chính phủ phát 10.000 Baht tiền mặt cho mỗi người dân sẽ tạo ra cú hích tổng cầu thần kỳ." | Phát tiền cho người đang nợ ngập đầu thì tiền chảy thẳng vào việc trả nợ hoặc mua hàng giá rẻ Trung Quốc (Temu), không kích thích được sản xuất trong nước. |
| **CH07** | Việt Nam vượt Thái Lan về GDP PPP ($2.025T) nhưng đối mặt bài học cảnh tỉnh: Giá nhà >30 lần thu nhập, nợ hộ gia đình tăng x10. | "Việt Nam đã hoàn toàn vượt qua Thái Lan và không có gì phải lo lắng về mô hình phát triển." | Việt Nam phải chạy đua quyết liệt nâng cao năng suất TFP, kiểm soát nợ tiêu dùng và tự chủ công nghệ trước khi cánh cửa Dân số Vàng khép lại năm 2036. |
"""

retention_map_content = """# 06_retention_map.md: Retention Engineering & Tension Spikes
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản

```
[00:00 - CH01] HOOK: Cơn sốt lạnh 1% ────────► Cú sốc nghịch lý vĩ mô (Tension: 9.5/10)
      │
[04:00 - CH02] GIẢI PHẪU NỢ 86% GDP ────────► Nỗi sợ nợ nần & Thảm cảnh Gen Z (Dopamine Drop #1)
      │
[08:30 - CH03] BẪY RICHARD KOO ─────────────► Giải mã khoa học BSR: Vì sao tiền rẻ vô dụng? (Tension: 8.5/10)
      │
[13:00 - CH04] CHƯA GIÀU ĐÃ GIÀ ────────────► Đối sánh tàn nhẫn Nhật Bản vs Thái Lan (Dopamine Drop #2)
      │
[17:30 - CH05] DETROIT PHƯƠNG ĐÔNG SỤP ĐỔ ──► Cuộc xâm lược của EV Trung Quốc & Smile Curve (Tension: 9.0/10)
      │
[22:00 - CH06] VÍ ĐIỆN TỬ 500 TỶ BAHT ──────► Bế tắc tài khóa & Đòn giáng từ Temu/TikTok Shop (Dopamine Drop #3)
      │
[26:30 - CH07] BÀI HỌC CHO VIỆT NAM ────────► Bức tranh đối sánh tổng lực & Hồi chuông 2036 (Peak Climax: 10/10)
```

### Chiến lược Neo Giữ Khán Giả (Retention Tactics):
1. **0:00 – 1:00 (Hook Anchor):** Sử dụng hình ảnh đối lập cực đoan giữa sự hào nhoáng của Bangkok và mức lãi suất 1% "cho không nhưng không ai thèm vay".
2. **4:00 (Mid-Hook 1):** Công bố số liệu gây sốc: 52% thanh niên 20-35 tuổi mắc nợ, tỷ lệ từ chối vay mua xe vọt lên 70%.
3. **8:30 (Concept Re-hook):** Dùng phép loại suy "Đẩy một sợi dây" để giải thích cặn kẽ thuật ngữ Balance Sheet Recession.
4. **13:00 (Shock Comparison):** Đập tan so sánh với Nhật Bản bằng bảng đối sánh 6 điểm khác biệt chí mạng.
5. **17:30 (Industry Drama):** Kể câu chuyện thực tế về sự phá sản của các nhà máy cơ khí phụ trợ Thái Lan trước làn sóng xe điện BYD giá rẻ.
6. **22:00 (Policy Cliffhanger):** Bóc trần tranh cãi gói Digital Wallet 500 tỷ baht và sự xâm lăng của thương mại điện tử giá rẻ.
7. **26:30 (Climax & National Mirror):** So sánh trực diện Việt Nam vs Thái Lan, chỉ ra 4 mũi nhọn bứt phá và 3 tử huyệt cần phòng ngừa khẩn cấp trước năm 2036.
"""

outline_content = """# 07_outline.md: Master Long-form Outline
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản & Bài học Cảnh tỉnh Việt Nam

---

### PHẦN 1: MỞ ĐẦU & NGHỊCH LÝ VĨ MÔ
#### CH01: Cơn Sốt Lạnh 1% Và Nghịch Lý Con Hổ Đông Nam Á (Thời lượng dự kiến: 4 phút)
- 1.1. Khởi đầu với nghịch lý chấn động: Lãi suất BoT neo ở 1.0%, thấp nhất thế giới, sắp thấp hơn Nhật Bản nhưng không ai vay.
- 1.2. Bức tranh suy kiệt: Tăng trưởng rơi xuống đáy 1.3% (thấp nhất ASEAN), 12 tháng giảm phát liên tiếp, lạm phát tháng 7 chỉ 1.95%.
- 1.3. Lời thú nhận lịch sử từ Ngân hàng Trung ương Thái Lan: Chính sách tiền tệ "gần như đã chạm giới hạn".
- 1.4. Đặt câu hỏi xuyên suốt: Căn bệnh gì đang gặm nhấm nền kinh tế số 2 Đông Nam Á?

---

### PHẦN 2: BẢNG CÂN ĐỐI KẾ TOÁN & CƠ CHẾ NỢ NẦN
#### CH02: Bẫy Nợ Hộ Gia Đình 86% GDP — Khi Cả Quốc Gia Đi Làm Trả Lãi (Thời lượng dự kiến: 4.5 phút)
- 2.1. Quy mô nợ khổng lồ: 16.3 nghìn tỷ Baht (~86% - 87% GDP), tỷ lệ Nợ/Thu nhập (DTI) vọt lên 140% - 150%.
- 2.2. Giải phẫu 4 tầng nợ độc hại:
  * Tầng 1: Vay mua nhà (Mortgage) — nguồn nợ xấu lớn nhất, âm vốn chủ sở hữu.
  * Tầng 2: Vay mua xe (Auto loan) — di chứng trợ thuế 2011, tỷ lệ từ chối vay mua xe vọt lên 70%.
  * Tầng 3: Tín dụng tiêu dùng & BNPL — 52.7% người trẻ mắc nợ, nợ xấu 27%, tài khoản BNPL tăng 99.9%/năm.
  * Tầng 4: Tín dụng đen — lãi suất >20%/tháng, bẫy nợ chồng nợ ở nông thôn.
- 2.3. Hệ quả tàn khốc: Thu nhập khả dụng bị bòn rút, tổng cầu nội địa rơi vào trạng thái đóng băng vĩnh viễn.

#### CH03: Lời Nguyền Richard Koo — Vì Sao Tiền Rẻ Không Thể Cứu Nổi Thái Lan? (Thời lượng dự kiến: 4.5 phút)
- 3.1. Lý thuyết Suy thoái Bảng cân đối Kế toán (Balance Sheet Recession - BSR) của Richard Koo.
- 3.2. Sự chuyển dịch từ pha "Tối đa hóa lợi nhuận" sang "Tối thiểu hóa nợ nần": Người dân thắt lưng buộc bụng trả nợ gốc.
- 3.3. Hiện tượng "Đẩy một sợi dây" (Pushing on a string): Hệ số truyền dẫn lãi suất BoT chỉ đạt 20% - 30%, ngân hàng ôm thanh khoản phòng ngừa.
- 3.4. Rủi ro Doanh nghiệp thây ma (Zombiefication): Tiền rẻ giữ chân các doanh nghiệp năng suất kém, kéo lùi TFP toàn xã hội.

---

### PHẦN 3: NHÂN KHẨU HỌC & CÔNG NGHIỆP CỐT LÕI
#### CH04: "Chưa Giàu Đã Già" — Sự Khác Biệt Tàn Nhẫn Với Nhật Bản (Thời lượng dự kiến: 4.5 phút)
- 4.1. Sự so sánh khập khiễng trên truyền thông quốc tế giữa Nhật Bản 1990 và Thái Lan 2026.
- 4.2. 6 Điểm khác biệt chí mạng:
  * Vị thế thu nhập: Nước giàu (>30.000 USD) vs Nước thu nhập trung bình (7.200 USD).
  * Bản chất nợ: Nợ doanh nghiệp BĐS vs Nợ hộ gia đình tiêu dùng.
  * Không gian tài khóa: Nợ công 200% có dân tài trợ vs Nợ công 66.1% áp sát trần 70%.
  * Hệ thống an sinh: Nhà nước bảo trợ (BGR 0.369) vs Gia đình tự gánh (BGR 0.091, con cái gánh 77.8%).
  * Nhân khẩu học: TFR Thái Lan sụp đổ xuống 0.76 - 1.16, số ca sinh <400.000/năm, dân số giảm từ 67 triệu về 30 triệu.
  * Vị thế quốc tế: Chủ nợ toàn cầu vs Gia công ở đáy Smile Curve.
- 4.3. Kết luận: Thái Lan là bi kịch của "người nghèo mắc bệnh nan y khi bước sang tuổi già".

#### CH05: Cú Sụp Đổ Của "Detroit Đông Nam Á" Trước Xe Điện Trung Quốc (Thời lượng dự kiến: 4.5 phút)
- 5.1. Thời hoàng kim sản xuất 2 triệu ô tô/năm dựa vào chuỗi xe xăng Nhật Bản (Toyota, Isuzu, Honda).
- 5.2. Làn sóng EV Trung Quốc (BYD, GWM, Changan): Giá rẻ hơn 11.8%, chiếm 44% đăng ký mới.
- 5.3. Thảm kịch chuỗi phụ trợ: Xe điện nhập 100% pin/motor từ Trung Quốc $\rightarrow$ Hàng trăm nhà máy linh kiện cơ khí nội địa Tier-2, Tier-3 phá sản.
- 5.4. Bẫy Smile Curve: R&D dậm chân ở 1.2% GDP, sáng chế bản địa chỉ chiếm 10-16% $\rightarrow$ Hiện tượng phi công nghiệp hóa sớm.

---

### PHẦN 4: BẾ TẮC TÀI KHÓA & BÀI HỌC CHO VIỆT NAM
#### CH06: Chiếc Ví Kỹ Thuật Số 500 Tỷ Baht Và Giới Hạn Đỏ Tài Khóa (Thời lượng dự kiến: 4.5 phút)
- 6.1. Nợ công 66.1% áp sát trần pháp lý 70% GDP, dư địa tài khóa khả dụng chỉ còn ~800 tỷ THB.
- 6.2. Tranh cãi gay gắt gói Digital Wallet 500 tỷ Baht (phát 10.000 Baht/người cho 50 triệu dân): Dân túy ngắn hạn vs Kỷ luật tài khóa dài hạn.
- 6.3. Du lịch đuối sức: Chiếm 12-18% GDP nhưng chi tiêu bình quân/khách giảm sút.
- 6.4. Đòn giáng từ thương mại điện tử giá rẻ Trung Quốc (Temu, Shein, TikTok Shop) tràn ngập bóp chết sản xuất bán lẻ trong nước.

#### CH07: Bức Tranh Đối Sánh Việt Nam — Thái Lan & Hồi Chuông Cảnh Tỉnh Tương Lai (Thời lượng dự kiến: 5 phút)
- 7.1. Cuộc đổi ngôi lịch sử: GDP PPP Việt Nam 2026 đạt 2.025 nghìn tỷ USD chính thức vượt Thái Lan (IMF); Xuất khẩu 475 tỷ USD bỏ xa Thái Lan.
- 7.2. 4 Mũi đột phá của Việt Nam: Vận tốc tăng trưởng (7.5% - 8.0%), nam châm FDI công nghệ cao (Samsung, Apple, Nvidia), dư địa nợ công 30% cho kế hoạch 400 tỷ USD đầu tư công hạ tầng, và tinh thần tự chủ của các tập đoàn dân tộc (VinFast, Viettel, FPT, Hòa Phát).
- 7.3. 3 Tử huyệt và bài học cảnh báo đỏ cho Việt Nam:
  * Đưa tỷ lệ Giá nhà / Thu nhập (>30 lần) về vùng an toàn để không bóp nghẹt sức mua người trẻ.
  * Kiểm soát nợ hộ gia đình, khóa trần tín dụng tiêu dùng dễ dãi và triệt phá tín dụng đen.
  * Gia cố đệm dự trữ ngoại hối và nâng cao năng suất lao động trước khi cánh cửa Dân số Vàng khép lại vào năm 2036.
- 7.4. Kết bài: Thông điệp truyền cảm hứng tự cường dân tộc và trách nhiệm phát triển quốc gia.
"""

chapter_briefs_content = """# 08_chapter_briefs.md: Atomic Chapter Briefs
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản

```yaml
chapter_01:
  title: "Cơn Sốt Lạnh 1% Và Nghịch Lý Con Hổ Đông Nam Á"
  target_word_count: 850
  core_thesis: "Lãi suất 1% không cứu nổi nền kinh tế rơi vào thiểu phát và tăng trưởng chạm đáy 1.3%."
  must_include_data: ["DATA-01 (1.0% BoT)", "DATA-02 (GDP 1.3%-1.9%)", "DATA-03 (12 tháng giảm phát)", "DATA-04 (Mục tiêu 2037)"]
  emotional_beat: "Ngỡ ngàng, kịch tính, khơi gợi tò mò khám phá bức màn vĩ mô."

chapter_02:
  title: "Bẫy Nợ Hộ Gia Đình 86% GDP — Khi Cả Quốc Gia Đi Làm Trả Lãi"
  target_word_count: 950
  core_thesis: "Nợ hộ gia đình 16.3 nghìn tỷ Baht biến thành cục máu đông bóp nghẹt thu nhập và sức mua dân sinh."
  must_include_data: ["DATA-05 (85.9%-86.8% GDP)", "DATA-06 (DTI 140%-150%)", "DATA-07 (Từ chối vay xe 70%)", "DATA-08 (Gen Z nợ 52.7%, NPL 27%)", "DATA-09 (Tín dụng đen >20%/tháng)"]
  emotional_beat: "Xót xa, gay gắt, thấu cảm với áp lực mưu sinh của người lao động."

chapter_03:
  title: "Lời Nguyền Richard Koo — Vì Sao Tiền Rẻ Không Thể Cứu Nổi Thái Lan?"
  target_word_count: 950
  core_thesis: "Giải mã lý thuyết Balance Sheet Recession: Chuyển sang tối thiểu hóa nợ, tiền rẻ biến thành đẩy một sợi dây."
  must_include_data: ["DATA-10 (Truyền dẫn 20%-30%)", "DATA-11 (Mô hình ARDL tiêu dùng)", "DATA-12 (Oxford Economics nhận định)"]
  emotional_beat: "Sâu sắc, học thuật đanh thép, thông tuệ."

chapter_04:
  title: "\"Chưa Giàu Đã Già\" — Sự Khác Biệt Tàn Nhẫn Với Nhật Bản"
  target_word_count: 950
  core_thesis: "Thái Lan không có của cải để chịu đựng 30 năm mất mát như Nhật Bản; bi kịch người nghèo mắc bệnh nan y khi vừa già."
  must_include_data: ["DATA-13 (GDP $30.000 vs $7.200)", "DATA-14 (TFR 0.76-1.16)", "DATA-15 (OADR 28.4 lên 56.2)", "DATA-16 (BGR 0.091 vs 0.369, con cái gánh 77.8%)"]
  emotional_beat: "Trầm buồn, cảnh tỉnh, mang sức nặng lịch sử."

chapter_05:
  title: "Cú Sụp Đổ Của \"Detroit Đông Nam Á\" Trước Xe Điện Trung Quốc"
  target_word_count: 950
  core_thesis: "Làn sóng xe điện Trung Quốc phá vỡ chuỗi cung ứng phụ trợ nội địa, đẩy Thái Lan vào bẫy phi công nghiệp hóa sớm."
  must_include_data: ["DATA-17 (Sản lượng 2.0tr xe)", "DATA-18 (EV rẻ hơn 11.8%)", "DATA-19 (EV chiếm 44% xe mới)", "DATA-20 (R&D 1.2% GDP, sáng chế 10%-16%)"]
  emotional_beat: "Kịch tính thương trường, phơi bày sự tàn khốc của chuyển dịch công nghệ."

chapter_06:
  title: "Chiếc Ví Kỹ Thuật Số 500 Tỷ Baht Và Giới Hạn Đỏ Tài Khóa"
  target_word_count: 900
  core_thesis: "Nợ công 66.1% sát trần 70%, gói phát tiền 500 tỷ baht chỉ là giải pháp dân túy ngắn hạn không giải quyết được căn nguyên."
  must_include_data: ["DATA-21 (Nợ công 66.1% / trần 70%)", "DATA-22 (Digital Wallet 500 tỷ Baht)", "DATA-23 (Du lịch 12%-18% GDP suy giảm chi tiêu)"]
  emotional_beat: "Phản biện sắc bén, vạch trần bế tắc chính sách."

chapter_07:
  title: "Bức Tranh Đối Sánh Việt Nam — Thái Lan & Hồi Chuông Cảnh Tỉnh Tương Lai"
  target_word_count: 1100
  core_thesis: "Việt Nam bứt phá vượt qua Thái Lan về quy mô nhưng phải khắc cốt ghi tâm bài học nợ tiêu dùng và cửa sổ Dân số Vàng 2036."
  must_include_data: ["DATA-24 (GDP PPP $2.025T vượt)", "DATA-25 (Tăng trưởng 8.02% vs 1.3%)", "DATA-26 (Xuất khẩu $475B vs $339.6B)", "DATA-27 (Nợ công VN 30% / Đầu tư công $400B)", "DATA-28 (Giá nhà >30 lần / Nợ hộ gia đình VN)", "DATA-29 (Mốc Dân số Vàng 2036)", "DATA-30 (Dự báo CEBR 2035 $994B)"]
  emotional_beat: "Hào hùng, sâu lắng, truyền cảm hứng tự hào và khát vọng tự cường dân tộc."
```
"""

nst_content = """# 09_narrative_state_tracker.md: Narrative State Tracker (NST)
## Đề tài: Khủng hoảng Kinh tế Thái Lan — Nợ ngập đầu, Vết xe đổ của Nhật Bản

```yaml
global_narrative_thread: "Cuộc giải phẫu căn bệnh suy thoái thoái hóa cơ cấu của Thái Lan từ bẫy nợ 86% GDP, lý thuyết Balance Sheet Recession đến hồi chuông cảnh tỉnh cho vận mệnh phát triển của Việt Nam trước năm 2036."

chapter_tracking:
  CH01:
    status: READY_TO_WRITE
    open_loops: ["Tại sao lãi suất 1% lại không ai thèm vay?", "Điều gì đang gặm nhấm nền kinh tế số 2 Đông Nam Á?"]
    seeds_planted: ["Gốc rễ nợ hộ gia đình ngập đầu ẩn sau vẻ hào nhoáng của Bangkok"]
    harvested_seeds: []
    key_entities: ["Bank of Thailand (BoT)", "Don Nakornthab", "World Bank", "IMF"]

  CH02:
    status: PENDING
    open_loops: ["Tại sao người dân lại mắc nợ nhiều đến vậy?", "Cơ cấu 4 tầng nợ đang vận hành ra sao?"]
    seeds_planted: ["Khi cả xã hội nợ nần, hành vi kinh tế thay đổi hoàn toàn theo quy luật BSR"]
    harvested_seeds: ["Gốc rễ nợ hộ gia đình ngập đầu từ CH01"]
    key_entities: ["HSBC", "Aris Dacanay", "BoT", "P-Loans", "Nano Finance", "BNPL"]

  CH03:
    status: PENDING
    open_loops: ["Tại sao tiền rẻ lại biến thành 'đẩy một sợi dây'?", "Doanh nghiệp thây ma xuất hiện như thế nào?"]
    seeds_planted: ["Nhiều người so sánh Thái Lan với Thập niên mất mát của Nhật Bản, nhưng sự thật tàn nhẫn hơn nhiều"]
    harvested_seeds: ["Sự thay đổi hành vi kinh tế sang chế độ 'tối thiểu hóa nợ' từ CH02"]
    key_entities: ["Richard Koo", "Balance Sheet Recession (BSR)", "Oxford Economics", "Louise Loo", "SCB EIC", "Nond Prueksiri"]

  CH04:
    status: PENDING
    open_loops: ["Khác biệt chí mạng giữa Nhật Bản 1990 và Thái Lan 2026 là gì?", "Thảm kịch 'Chưa giàu đã già' sẽ dẫn tới đâu?"]
    seeds_planted: ["Không chỉ tài chính và dân số, trụ cột công nghiệp ô tô 40 năm qua cũng đang sụp đổ"]
    harvested_seeds: ["Sự thật tàn nhẫn về việc Thái Lan không có của cải để chịu đựng như Nhật Bản từ CH03"]
    key_entities: ["Burin Adulwattana", "NESDC", "UNFPA", "Old-Age Dependency Ratio (OADR)", "Sandwich Generation"]

  CH05:
    status: PENDING
    open_loops: ["Vì sao xe điện Trung Quốc lại làm phá sản chuỗi cung ứng nội địa Thái Lan?", "Bẫy Smile Curve là gì?"]
    seeds_planted: ["Khi cả tiêu dùng lẫn công nghiệp đều tê liệt, chính phủ tung gói phát tiền số 500 tỷ baht"]
    harvested_seeds: ["Sự sụp đổ của trụ cột công nghiệp ô tô từ CH04"]
    key_entities: ["Toyota", "Isuzu", "BYD", "Great Wall Motors", "Changan", "Smile Curve", "Tier-2/Tier-3"]

  CH06:
    status: PENDING
    open_loops: ["Tại sao gói Digital Wallet 500 tỷ Baht lại gây tranh cãi gay gắt?", "Hàng giá rẻ Temu/TikTok Shop tàn phá bán lẻ ra sao?"]
    seeds_planted: ["Nhìn sang bi kịch của người láng giềng, Việt Nam đang ở đâu và cần làm gì?"]
    harvested_seeds: ["Gói phát tiền số 500 tỷ baht từ CH05"]
    key_entities: ["Sethaput Suthiwartnarueput", "Digital Wallet 500B", "Public Debt Management Office", "Temu", "Shein"]

  CH07:
    status: PENDING
    open_loops: ["Việt Nam vượt Thái Lan ở những điểm nào?", "Những tử huyệt nào Việt Nam cần phòng vệ khẩn cấp trước 2036?"]
    seeds_planted: ["Thông điệp tự cường dân tộc và trách nhiệm phát triển quốc gia"]
    harvested_seeds: ["So sánh vị thế và rút ra bài học chiến lược cho Việt Nam từ CH06"]
    key_entities: ["IMF WEO 2026", "Nikkei Asia", "CEBR", "VinFast", "Viettel", "FPT", "Hòa Phát", "SBV"]
```
"""

(EPISODE_DIR / "03_brief.md").write_text(brief_content, encoding="utf-8")
(EPISODE_DIR / "04_hook_pack.md").write_text(hook_pack_content, encoding="utf-8")
(EPISODE_DIR / "05_thesis_map.md").write_text(thesis_map_content, encoding="utf-8")
(EPISODE_DIR / "06_retention_map.md").write_text(retention_map_content, encoding="utf-8")
(EPISODE_DIR / "07_outline.md").write_text(outline_content, encoding="utf-8")
(EPISODE_DIR / "08_chapter_briefs.md").write_text(chapter_briefs_content, encoding="utf-8")
(EPISODE_DIR / "09_narrative_state_tracker.md").write_text(nst_content, encoding="utf-8")

print("✓ Đã khởi tạo thành công toàn bộ 7 tệp tin chiến lược (Pha 3 đến Pha 8b)!")
