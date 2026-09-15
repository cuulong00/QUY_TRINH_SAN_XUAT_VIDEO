<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/philipines-bi-kich-gia-toc/09_narrative_state_tracker.md
- Activated Persona: The Narrative Director (.agents/personas/the_narrative_director.md) + The Critical Auditor (.agents/personas/the_critical_auditor.md)
- Activated Skill: Script Architect (.agents/skills/script_architect/SKILL.md)
- Source Documents Consulted:
  * episodes/philipines-bi-kich-gia-toc/08_chapter_briefs.md
  * episodes/philipines-bi-kich-gia-toc/07_outline.md
  * episodes/philipines-bi-kich-gia-toc/06_retention_map.md
  * episodes/philipines-bi-kich-gia-toc/05_thesis_map.md
  * episodes/philipines-bi-kich-gia-toc/04_hook_pack.md
  * episodes/philipines-bi-kich-gia-toc/03_brief.md
  * episodes/philipines-bi-kich-gia-toc/vault/00_Global_Vision_Synthesis.md
  * episodes/philipines-bi-kich-gia-toc/research_vault/01_demographic_dividend_vs_poverty_trap.md
- Execution Timestamp: 2026-09-05 23:25
-->

# 09_narrative_state_tracker.md — Bộ Nhớ Trạng Thái Kịch Bản Động (Pha 8b)

> **Tập phim:** Bi Kịch Của Đứa Trẻ Dân Số Vàng: Nhảy Cóc Bỏ Qua Công Nghiệp Hóa, Bẫy Độc Quyền Gia Tộc Và Bài Học Cảnh Tỉnh Cho Việt Nam  
> **Slug:** `philipines-bi-kich-gia-toc`  
> **Mục đích:** Lưu trữ trạng thái lũy tiến của kịch bản qua từng chương thoại; quản lý các vòng lặp tò mò Zeigarnik Loops và kiểm soát việc gieo hạt giống (Seeding) và thu hoạch (Harvesting) giữa các chương kịch bản.  
> **Quy định vận hành:** Chapter Writer bắt buộc phải nạp và cập nhật tệp này sau khi hoàn thành mỗi chương kịch bản sạch (`chapter_XX.md`).  

---

## 1. Factual State Ledger (Sổ Cái Dữ Liệu Đã Sử Dụng)
> *Mục tiêu: Đóng dấu số liệu đã xuất hiện trong kịch bản để triệt tiêu 100% nguy cơ lặp lại số liệu máy móc ở các chương sau.*

| Chương | Số liệu tài chính / Tên pháp lý đã dùng | Đối tượng / Thực thể đề cập | Nguồn kiểm chứng (Vault Ref) | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **Hook (Ch.1)** | Dân số 115 triệu; Tuổi trung vị 25,3; Giá điện đắt gấp 3 Việt Nam; Nhập siêu gạo số 1 thế giới; 75% gạo từ Việt Nam; BPO 40 tỷ USD | Dân số Philippines, Nông nghiệp lúa gạo Việt Nam, BPO | `04_hook_pack.md`, `vault/00:DATA-01,07,09,10,11` | Đã khóa trong Hook |
| **Chương 1** | Dân số 115M, tuổi 25,3; Lao động >63%, tỷ lệ phụ thuộc <50%; 2,5M OFW chính thức, 10M kiều bào; Kiều hối $39,62B (2025, ~9% GDP); H1 2026: $17,15B; 70% kiều hối vào tiêu dùng bán lẻ; Căn bệnh Hà Lan | Sân bay Ninoy Aquino, OFW, Kiều hối BSP, Trung tâm thương mại gia tộc | `research_vault/01:L15-L105`, `06:L15-L50`, `vault/00:DATA-01,DATA-02` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 2** | Chế tạo giảm từ >30% xuống <17% GDP; Đỉnh công nghiệp ở mức $1.700; Việc làm chế tạo <10%; TFP tăng 0,5% - 1%/năm; Chế tạo VN ~25% GDP, xuất khẩu >$400B (gấp >5 lần PH); BPO $40B, 2M lao động tri thức vs 40M lao động phổ thông | Dani Rodrik, Harvard, Chế tạo Việt Nam, BPO, Lao động nông thôn | `research_vault/02:L20-L150`, `10:L20-L55`, `vault/00:DATA-03,DATA-04,DATA-05` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 3** | ~100 gia tộc nắm >70% Quốc hội; Đạo luật EPIRA 2001 (RA 9136) xử lý nợ $16B NPC; Meralco 55% phân phối; Cơ chế chuyển giá trực tiếp (pass-through) than nhập (~60%); Giá điện bán lẻ Manila đỉnh ~15 PHP/kWh (~$0,26 hay >6.500 VND/kWh); Giá điện sản xuất VN ~0,08 USD/kWh (~2.000 VND/kWh, bằng 1/3); Điện chiếm 20-60% chi phí chip/luyện kim; Thuế ngược đẩy lùi FDI (PH chỉ nhận ~1% FDI ASEAN) | Meralco, NPC, Quốc hội Philippines, EVN Việt Nam, Tập đoàn FDI | `research_vault/03:L18-L40`, `04:L12-L120`, `vault/00:DATA-07,DATA-08,DATA-09` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 4** | Viện IRRI Los Baños (Laguna), giống lúa IR8 (1966); USDA dự báo 2026 nhập khẩu kỷ lục 5,2 - 5,7M tấn gạo (số 1 thế giới); 8 tháng đầu 2026 nhập 3,46M tấn (Việt Nam cấp 2,59M tấn ~75%); Đạo luật CARP 1988 phân phối 6M ha, trần 5 ha, cấm chuyển nhượng 10 năm -> manh mún 1-2 ha, ngân hàng từ chối thế chấp -> "landed poor"; Nông dân phơi thóc mặt đường nhựa quốc lộ; Chi phí sản xuất đắt hơn 40% - 50% so với ĐBSCL VN; Lương thực chiếm 55% chi tiêu nhóm nghèo; Lạm phát gạo nông thôn >20%; Giá gạo cam kết 20 peso vỡ trận (thực tế 56-64 peso/kg) | Viện IRRI, Nông dân Philippines, Nông dân ĐBSCL Việt Nam, Đạo luật CARP 1988, Tổng thống Marcos Jr. | `research_vault/05:L10-L75`, `vault/00:DATA-10,DATA-11,DATA-12` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 5** | Bonifacio Global City (BGC) về đêm; Doanh thu BPO $40,3B (2025) tạo việc làm cho gần 2M lao động, vượt kiều hối tiền mặt ($35,63B); BPO không dạy năng lực cơ khí hay chế tạo chip -> thiếu vắng kỹ năng sản xuất vật chất; Cơn địa chấn AI tạo sinh & Voice Agent xử lý 60-80% cuộc gọi Tier-1; IMF cảnh báo 89% công việc văn phòng BPO rủi ro cao; IBPAP Roadmap Refresh 2026 hạ chỉ tiêu xóa sổ 360k-650k việc làm dự kiến; Người trẻ mất việc không thể rút về nhà máy hay đồng ruộng | Bonifacio Global City (BGC), IBPAP, IMF, Lao động BPO Manila | `research_vault/06:L10-L60`, `vault/00:DATA-13,DATA-14,DATA-15,DATA-16` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 6** | Nợ công chạm đỉnh kỷ lục 19,39 nghìn tỷ Peso (~$316B, tăng 53% sau 4 năm); Nợ/GDP đạt 66% (đỉnh 22 năm); Nợ bình quân đầu người tương đương >70 triệu VND (172.005 Peso); Thâm hụt ngân sách kéo dài; Chi trả nợ ngốn >14% thu ngân sách, bóp nghẹt đầu tư công (tăng trưởng Q2 rơi xuống 2,3%); Quỹ Maharlika (RA 11954) rút ép buộc 75 tỷ Peso từ 2 ngân hàng nhà nước (LandBank 50B, DBP 25B); BSP phải cấp nới lỏng đặc biệt (regulatory forbearance); IMF cảnh báo suy yếu an toàn hệ thống ngân hàng; Rủi ro người đóng thuế gánh chịu | Kho bạc Quốc gia (BTr), Tổng thống Marcos Jr., Quỹ Maharlika (MIF), LandBank, DBP, Ngân hàng Trung ương BSP, IMF | `research_vault/07:L10-L65`, `vault/00:DATA-17,DATA-18,DATA-19,DATA-20` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 7** | Liên minh UniTeam tan rã; Hạ viện luận tội Sara Duterte (5/2026, 257 phiếu), Thượng viện mở phiên xử (6/7/2026); Tòa QC RTC phát lệnh bắt Sara Duterte 4/9/2026, bảo lãnh 360k Peso 5/9/2026; Rodrigo Duterte bị bắt 11/3/2025, di lý sang La Haye, xét xử ICC 30/11/2026; Mở rộng 9 căn cứ EDCA cho Mỹ (Cagayan cách Đài Loan ~400km, Balabac Palawan); Tàu tuần duyên Philippines trúng vòi rồng móp méo cabin tại Bãi Cỏ Mây; Hiệp ước MDT 1951 bất lực trước chiến thuật vùng xám | Sara Duterte, Rodrigo Duterte, Ferdinand Marcos Jr., Tòa án ICC La Haye, 9 Căn cứ EDCA, Bãi Cỏ Mây (Ayungin) | `research_vault/08:L10-L75`, `09:L10-L65`, `vault/00:DATA-21,DATA-22,DATA-23,DATA-24` | ✅ ĐÃ HOÀN THÀNH |
| **Chương 8** | Tấm gương đối chiếu 4 lằn ranh đỏ thể chế: (1) Chế tạo duy trì ~25% GDP vs <18%; (2) Giữ vững điều tiết giá điện sản xuất ổn định (~0,08 USD/kWh vs ~0,26 USD/kWh); (3) Tự chủ an ninh lương thực (vùng lúa ĐBSCL) vs nhập siêu kỷ lục; (4) Độc lập chiến lược, Ngoại giao Cây tre và chính sách quốc phòng 4 Không vs tiền đồn rủi ro; Cảnh tỉnh thời gian cửa sổ dân số vàng khép lại trong 2 thập kỷ; Lời kêu gọi thảo luận & Subscribe Dòng Chảy | Toàn thể nhân dân, Công nhân nhà xưởng, Nông dân ĐBSCL, Quốc phòng Việt Nam, Kênh Dòng Chảy | `research_vault/10:L70-L93`, `vault/00:DATA-22,DATA-23,DATA-24` | ✅ ĐÃ HOÀN THÀNH (TOÀN BỘ 8 CHƯƠNG) |

---

## 2. Narrative & Emotional State (Trạng Thái Câu Chuyện & Vòng Lặp Zeigarnik)

* **Tension Level Hiện Tại:** 8.0/10 (Trầm hùng, uy quyền, triết lý, để lại dư âm sâu sắc và trách nhiệm công dân).
* **Active Open Loops (Các vòng lặp tò mò đang mở):**
  - *Không còn vòng lặp mở:* Toàn bộ các câu hỏi lớn và vòng lặp đã được khép lại hoàn hảo bằng Hợp đề biện chứng ở Chương 8.
* **Closed Loops (Các vòng lặp đã đóng):**
  - *[Loop 1 — Đóng ở Ch.1]:* Đã giải mã vì sao 115 triệu dân trẻ nhưng phải xuất khẩu 2,5 triệu lao động.
  - *[Loop 2 — Đóng ở Ch.2]:* Đã giải mã căn bệnh phi công nghiệp hóa sớm theo lý thuyết Dani Rodrik; BPO không thể thay thế nhà xưởng chế tạo cho 40 triệu lao động nông thôn.
  - *[Loop 3 — Đóng ở Ch.3]:* Đã giải mã bức tường vô hình xua đuổi các đại bàng công nghiệp thế giới: Sự thao túng của 100 gia tộc tài phiệt và chiếc thòng lọng giá điện Meralco EPIRA đắt gấp 3 lần Việt Nam.
  - *[Loop 4 — Đóng ở Ch.4]:* Đã giải mã nghịch lý cái nôi Cách mạng Xanh IRRI trở thành con nợ nhập khẩu gạo lớn nhất hành tinh và sự phụ thuộc sống còn vào những cánh đồng miền Tây Việt Nam.
  - *[Loop 5 — Đóng ở Ch.5]:* Đã bóc trần hai mặt của chiếc phao BPO: Lợi thế tiếng Anh rỗng cơ bắp sản xuất và sự đổ vỡ việc làm dưới cơn địa chấn Generative AI.
  - *[Loop 6 — Đóng ở Ch.6]:* Đã giải phẫu quả bom nợ công 19,39 nghìn tỷ Peso và nước cờ mạo hiểm Quỹ Maharlika rút ruột hai ngân hàng nhà nước.
  - *[Loop 7 — Đóng ở Ch.7]:* Đã lột tả sự tan rã của liên minh UniTeam, cuộc thanh trừng nhắm vào gia tộc Duterte và cái bẫy tiền đồn nóng của 9 căn cứ quân sự EDCA.
  - *[Macro Loop Toàn Bài & Loop 8 — Đóng ở Ch.8]:* Đã đúc kết trọn vẹn 4 lằn ranh đỏ thể chế (Công nghiệp chế tạo thực chất ~25% GDP, Hạ tầng năng lượng do nhà nước điều tiết, An ninh lương thực độc lập quy mô lớn, và Độc lập chiến lược Ngoại giao Cây tre 4 Không) làm bài học cảnh tỉnh sống còn và tấm khiên bảo vệ tương lai phát triển của Việt Nam.

---

## 3. Active Seeds & Harvesting Protocol (Gieo Hạt & Thu Hoạch)

* **Hạt giống hình ảnh thị giác (Visual Seeds):**
  - Đã thu hoạch ở Ch.8: "Dây chuyền sản xuất cơ khí, bán dẫn hiện đại tại Bắc Ninh, Hải Phòng", "Những cánh đồng lúa thẳng cánh cò bay tại ĐBSCL", "Người thợ và người nông dân làm việc bền bỉ dưới ánh bình minh vươn mình của đất nước".
* **Hạt giống dữ liệu/Mẫu câu gợi mở (Data Seeds):**
  - Đã đúc kết trọn vẹn: 4 lằn ranh đỏ thể chế và thông điệp triết lý phát triển quốc gia.

---

## 4. Production Completion Status (Trạng Thái Hoàn Thành Pipeline Giai Đoạn 9)

* **Kịch bản thoại sạch 8/8 Chương:**
  - `chapter_01.md`: 49 câu, 100% < 118 ký tự (Đạt chuẩn)
  - `chapter_02.md`: 48 câu, 100% < 111 ký tự (Đạt chuẩn)
  - `chapter_03.md`: 48 câu, 100% < 99 ký tự (Đạt chuẩn)
  - `chapter_04.md`: 45 câu, 100% < 111 ký tự (Đạt chuẩn)
  - `chapter_05.md`: 32 câu, 100% < 104 ký tự (Đạt chuẩn)
  - `chapter_06.md`: 34 câu, 100% < 110 ký tự (Đạt chuẩn)
  - `chapter_07.md`: 32 câu, 100% < 105 ký tự (Đạt chuẩn)
  - `chapter_08.md`: 31 câu, 100% < 114 ký tự (Đạt chuẩn)
* **Tổng kết:** 100% kịch bản 8 chương hoàn toàn là văn bản thoại sạch, không nhãn cues, không tiêu đề kỹ thuật, phân đoạn văn tự nhiên (2-4 câu/đoạn), sẵn sàng chuyển sang Pha 9.7 (Retention Bridge Audit) và Pha 10-11 (Financial & Oral QA).
