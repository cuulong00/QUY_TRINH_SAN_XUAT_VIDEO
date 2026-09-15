# SỔ CÁI GHI NHẬN & PHÂN TÍCH LỖI LLM (LLM DEFECT & ERROR LOG)
## Episode: co-khi-dai-dung — Đặt Đại Dũng Trên Bàn Cân Cơ Khí Nặng Toàn Cầu

> **Mục đích tài liệu:** Lưu vết toàn bộ các khiếm khuyết, lỗi vi phạm quy tắc, ảo giác số liệu, trôi dạt văn phong hoặc các trường hợp Người dùng từ chối bản nháp trong suốt quá trình LLM sinh nội dung cho episode này.
> **Ý nghĩa:** Cung cấp dữ liệu thực chứng phục vụ khâu Hậu kiểm (Pha 16 - Postmortem) và làm căn cứ định kỳ nâng cấp, vá lỗi cho System Prompts, Skills và Bộ quy tắc vận hành của kênh.

---

## 1. THỐNG KÊ TỔNG QUAN (DEFECT METRICS SUMMARY)

| Nhóm Phân Loại Lỗi (Category) | Mã Phân Loại | Số Lượng Lỗi | Mức Độ Nghiêm Trọng Cao Nhất |
|---|---|:---:|:---:|
| Định dạng, Cú pháp & Kỹ thuật TTS | `[FORMAT_SYNTAX]` | 3 | MINOR |
| Giọng điệu, Từ cấm & Văn phong | `[VOCABULARY_TONE]` | 0 | - |
| Dữ liệu, Trích dẫn & Ảo giác | `[DATA_GROUNDING]` | 1 | CRITICAL |
| Logic, Lập luận & Cấu trúc | `[LOGIC_REASONING]` | 0 | - |
| Quy trình, Giao thức & Persona | `[PROCESS_PROTOCOL]` | 0 | - |
| Phản hồi & Từ chối từ Người dùng | `[HUMAN_REJECTION]` | 2 | CRITICAL |
| **TỔNG CỘNG** | | **6** | **CRITICAL** |

---

## 2. BẢNG TRA CỨU NHANH CÁC LỖI (DEFECT INDEX)

| Mã Lỗi | Thời Gian | Pha / Tệp Tin | Model & Persona | Nhóm Lỗi | Mức Độ | Trạng Thái Xử Lý |
|---|---|---|---|---|:---:|:---:|
| `ERR-20260907-PIVOT-01` | 2026-09-07 | Toàn bộ Pipeline nháp cũ | Claude 3.7 Sonnet / The Macro Strategist | `[HUMAN_REJECTION]` | CRITICAL | Resolved |
| `ERR-20260907-CH02-01` | 2026-09-07 | Pha 7 - chapter_02.md | Gemini 3.8 Flash / The Industrial Economist | `[FORMAT_SYNTAX]` | MINOR | Resolved |
| `ERR-20260907-CH05-01` | 2026-09-07 | Pha 7 - chapter_05.md | Gemini 3.8 Flash / The Industrial Economist | `[FORMAT_SYNTAX]` | MINOR | Resolved |
| `ERR-20260907-CH06-01` | 2026-09-07 | Pha 7 - chapter_06.md | Gemini 3.8 Flash / The Policy Analyst | `[FORMAT_SYNTAX]` | MINOR | Resolved |
| `ERR-20260914-GROUNDING-01` | 2026-09-14 | Pha 5 & Pha 7 (Hook, CH01, CH02) | Gemini 3.8 Flash / The Narrative Director | `[DATA_GROUNDING]` + `[HUMAN_REJECTION]` | CRITICAL | Resolved |

---

## 3. NHẬT KÝ CHI TIẾT CÁC LỖI PHÁT SINH (DETAILED DEFECT ENTRIES)

### [ERR-20260907-PIVOT-01] Sai lệch Trọng tâm Chiến lược: Quá tập trung vào Trượt thầu Nội địa

- **Thời gian ghi nhận:** 2026-09-07 10:30:00
- **Pha sản xuất & Tệp tin:** Toàn bộ Pipeline nháp cũ (`03_brief.md`, `07_outline.md`, `chapter_01.md`–`chapter_07.md`)
- **Mô hình & Chuyên gia (Persona):** Claude 3.7 Sonnet + The Macro Strategist
- **Nhóm phân loại lỗi (Category):** `[HUMAN_REJECTION]`
- **Mức độ nghiêm trọng (Severity):** CRITICAL (Phế phẩm do sai lệch định vị đề tài)
- **Trạng thái:** Resolved (Đã xóa sạch bản nháp cũ, cập nhật Bức tranh toàn cảnh 4 tầng và làm lại Dàn ý/Hook)

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> "Dàn ý và kịch bản cũ lấy sự kiện 'Đại Dũng trượt thầu 55% / trượt Gói 4.9 Long Thành' làm biến cố trung tâm xuyên suốt, biến câu chuyện thành một cuộc mổ xẻ tiêu cực về việc thất bại trong nước."

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: Định vị đề tài chuẩn xác, phản ánh đúng bản chất công nghiệp cơ khí nặng; Không bới móc tiểu tiết hay giật gân sai lệch bản chất.
- Tệp quy định: Bức tranh toàn cảnh `vault/00_Global_Vision_Synthesis.md` và phản hồi trực tiếp của Người dùng.

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- LLM bị thu hút bởi số liệu tương phản giật gân (thắng thầu Mỹ >60M USD vs trượt thầu trong nước 55%), dẫn đến việc tự động biến chi tiết trượt thầu thành trục kịch tính chính, trong khi bản chất của việc trượt thầu xây lắp công nội địa chỉ là vấn đề phụ (lệch pha tiêu chuẩn xây dựng dân dụng hỗn hợp).

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Xóa bỏ toàn bộ các tệp nháp cũ vi phạm.
- Cập nhật lại Bức tranh toàn cảnh 4 tầng: Đưa việc trượt thầu về đúng vị trí là một ghi chú khách quan (side-note) ở phần sau để minh chứng doanh nghiệp không phải thần thánh.
- Định vị lại trục chính của video: **Đặt Đại Dũng lên bàn cân cơ khí nặng toàn cầu, khai phóng con hào 33 chứng chỉ G7, dung sai dưới 2mm, phân tích các giới hạn chi phí thực tế (bão giá HRC, Capex cảng nước sâu, thuế CBAM) và trục liên minh công nghiệp dân tộc.**

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cập nhật quy tắc: Khi xây dựng đề tài doanh nghiệp công nghiệp quy mô lớn, luôn đối soát với bàn cân năng lực kỹ thuật cốt lõi toàn cầu trước khi khai thác các số liệu thầu phụ.

---

### [ERR-20260907-CH02-01] Câu dài vượt trần 150 ký tự tại bản nháp Chapter 2

- **Thời gian ghi nhận:** 2026-09-07 13:45:00
- **Pha sản xuất & Tệp tin:** Pha 7 — `chapter_02.md`
- **Mô hình & Chuyên gia (Persona):** Gemini 3.8 Flash + The Industrial Economist
- **Nhóm phân loại lỗi (Category):** `[FORMAT_SYNTAX]`
- **Mức độ nghiêm trọng (Severity):** MINOR (Vi phạm giới hạn câu thoại < 150 ký tự)
- **Trạng thái:** Resolved (Tách câu hoàn chỉnh ngữ pháp < 110 ký tự)

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> 1. "Thế nhưng, trong giới kỹ thuật công nghiệp nặng, quy mô và đẳng cấp của một nhà chế tạo luôn được định lượng bằng hai thước đo không thể che giấu: Diện tích nhà xưởng và công suất gia công hàng năm." (200 ký tự)
> 2. "Trong khi đó, tập đoàn Cimolai của Ý dù chỉ đạt công suất từ 100.000 đến 150.000 tấn, nhưng lại nổi tiếng thế giới về tay nghề thủ công cơ khí độc bản." (152 ký tự)
> 3. "Nếu quý vị thấy những góc nhìn phân tích vĩ mô này hữu ích, một lượt đăng ký kênh và chia sẻ nội dung sẽ là nguồn động viên rất lớn để chúng tôi tiếp tục thực hiện những đề tài chuyên sâu." (190 ký tự)
> 4. "Thế nhưng, để một tập đoàn Mỹ hay Nhật Bản chấp nhận giao phó những công trình huyết mạch, nhà máy của bạn phải vượt qua những bài kiểm tra sinh tử nào?" (153 ký tự)

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: Giới hạn câu thoại dưới 150 ký tự (< 25 từ) để tương thích phát thanh TTS tự nhiên.
- Tệp quy định: `.agents/skills/chapter_writer/SKILL.md` (Mục 4 & Quy tắc Vàng Writing for the Ear).

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- Mô hình ghép mệnh đề giải thích phức tạp có dấu hai chấm và câu kêu gọi Subscribe dài mà chưa tự ngắt câu bằng dấu chấm trước khi xuất tệp.

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Tách các câu dài thành các câu đơn ngắn gọn hoàn chỉnh ngữ pháp, kiểm soát độ dài mỗi câu từ 60 đến 110 ký tự:
> - "Thế nhưng, trong giới công nghiệp nặng, đẳng cấp luôn được định lượng bằng hai thước đo. Đó là diện tích nhà xưởng và công suất gia công hàng năm."
> - "Trong khi đó, tập đoàn Cimolai của Ý chỉ đạt công suất từ 100.000 đến 150.000 tấn. Thế nhưng, họ lại nổi tiếng thế giới về tay nghề thủ công độc bản."
> - "Nếu quý vị thấy phân tích này hữu ích, xin hãy đăng ký kênh. Sự ủng hộ của quý vị là động lực lớn cho đội ngũ sản xuất."
> - "Thế nhưng, để các tập đoàn Mỹ hay Nhật Bản giao phó siêu dự án, nhà máy của bạn phải vượt qua những bài kiểm tra sinh tử nào?"

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cài đặt thêm bước ngắt dấu chấm cho các mẫu câu CTA mặc định dưới 100 ký tự.

---

### [ERR-20260907-CH05-01] Câu ghép dài vượt 150 ký tự tại bản nháp Chapter 5

- **Thời gian ghi nhận:** 2026-09-07 14:00:00
- **Pha sản xuất & Tệp tin:** Pha 7 — `chapter_05.md`
- **Mô hình & Chuyên gia (Persona):** Gemini 3.8 Flash + The Industrial Economist
- **Nhóm phân loại lỗi (Category):** `[FORMAT_SYNTAX]`
- **Mức độ nghiêm trọng (Severity):** MINOR (Vi phạm giới hạn câu thoại < 150 ký tự)
- **Trạng thái:** Resolved (Tách câu hoàn chỉnh cú pháp < 100 ký tự)

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> 1. "Trọng tâm của ván cược này là mở rộng hai cụm nhà máy cận cảng nước sâu: Cụm Nghi Sơn 20 héc-ta tại Thanh Hóa và cụm Đông Xuyên 18 héc-ta tại Vũng Tàu." (153 ký tự)
> 2. "Thế nhưng, khi bước chân vào thị trường toàn cầu giai đoạn 2026, doanh nghiệp lại va phải một bức tường lửa bảo hộ vô hình mới của phương Tây: Thuế carbon biên giới CBAM." (170 ký tự)

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: Giới hạn câu thoại dưới 150 ký tự (< 25 từ) để tương thích phát thanh TTS tự nhiên.
- Tệp quy định: `.agents/skills/chapter_writer/SKILL.md` (Mục 4 & Quy tắc Vàng Writing for the Ear).

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- Mô hình dùng dấu hai chấm để giải thích địa điểm cụ thể và liệt kê tên rào cản thuế quan tạo thành một câu ghép dài trên 150 ký tự.

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Tách thành các câu đơn độc lập hoàn chỉnh ngữ pháp:
> - "Trọng tâm của ván cược này là mở rộng hai cụm nhà máy cận cảng nước sâu. Đó là cụm Nghi Sơn 20 héc-ta tại Thanh Hóa và cụm Đông Xuyên 18 héc-ta tại Vũng Tàu."
> - "Thế nhưng, bước vào thị trường toàn cầu năm 2026, doanh nghiệp lại va phải một bức tường bảo hộ mới. Đó là hàng rào thuế carbon biên giới CBAM của Liên minh Châu Âu."

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Khuyến nghị chia nhỏ các câu có dấu hai chấm giải thích địa danh/chính sách thành hai câu đơn riêng biệt.

---

### [ERR-20260907-CH06-01] Câu dài trên 150 ký tự trong bản nháp Chapter 6

- **Thời gian ghi nhận:** 2026-09-07 14:15:00
- **Pha sản xuất & Tệp tin:** Pha 7 — `chapter_06.md`
- **Mô hình & Chuyên gia (Persona):** Gemini 3.8 Flash + The Policy Analyst
- **Nhóm phân loại lỗi (Category):** `[FORMAT_SYNTAX]`
- **Mức độ nghiêm trọng (Severity):** MINOR (Vi phạm giới hạn câu thoại < 150 ký tự)
- **Trạng thái:** Resolved (Tách câu và tinh gọn mệnh đề < 120 ký tự)

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> 1. "Theo quy định mới, các sản phẩm kết cấu thép nhập khẩu vào Châu Âu nếu không chứng minh được mức phát thải carbon thấp sẽ bị áp mức thuế phạt từ 5% đến 10%." (156 ký tự)
> 2. "Hệ thống số hóa kết hợp cùng các trợ lý tự động hóa akaBot cho phép doanh nghiệp bóc tách chính xác lượng phát thải carbon trên từng tấn kết cấu thép theo thời gian thực." (171 ký tự)
> 3. "Trang bị công nghệ đỉnh cao và đạt chuẩn xanh quốc tế, nhưng chúng ta cần giữ một cái nhìn sòng phẳng: Đại Dũng không phải là một vị thần bất khả chiến bại." (156 ký tự)
> 4. "Điển hình là gói thầu 4.9 xây dựng hệ thống cung cấp nhiên liệu tại Sân bay Long Thành trị giá hơn 3.200 tỷ đồng, hay các gói thầu kho chứa của Đạm Cà Mau." (156 ký tự)
> 5. "Trong khi đó, ở những hạng mục đòi hỏi độ chính xác cơ khí khắt khe nhất như 64 cầu ống lồng sân bay, đối tác Nhật Bản chỉ tin tưởng giao cho Đại Dũng." (152 ký tự)
> 6. "Vì vậy, chúng ta sẽ bước vào chương cuối cùng: Trục liên minh bốn trụ cột công nghiệp dân tộc và sứ mệnh làm chủ đại dự án Đường sắt tốc độ cao 67 tỷ USD." (156 ký tự)

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: Giới hạn câu thoại dưới 150 ký tự (< 25 từ) để tương thích phát thanh TTS tự nhiên.
- Tệp quy định: `.agents/skills/chapter_writer/SKILL.md` (Mục 4 & Quy tắc Vàng Writing for the Ear).

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- Mô hình ghép mệnh đề điều kiện "nếu... thì...", tên đầy đủ của hệ thống phần mềm và liệt kê dự án dẫn tới nhiều câu cận trên 150-170 ký tự.

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Tinh chỉnh và tách câu hoàn chỉnh ngữ pháp < 120 ký tự:
> - "Theo quy định mới, nếu không chứng minh được phát thải thấp, thép nhập vào Châu Âu sẽ bị phạt 5% đến 10%."
> - "Hệ thống số hóa kết hợp cùng akaBot giúp doanh nghiệp bóc tách chính xác lượng carbon trên từng tấn thép theo thời gian thực."
> - "Đạt chuẩn xanh quốc tế, nhưng chúng ta cần nhìn nhận sòng phẳng: Đại Dũng không phải là một vị thần bất khả chiến bại."
> - "Điển hình là gói thầu 4.9 hệ thống nhiên liệu Sân bay Long Thành trị giá 3.200 tỷ, hay các gói kho của Đạm Cà Mau."
> - "Trong khi đó, ở hạng mục cơ khí chính xác đòi hỏi chuẩn G7 như 64 cầu ống lồng sân bay, đối tác Nhật Bản chỉ tin tưởng Đại Dũng."
> - "Vì vậy, chúng ta sẽ bước vào chương cuối cùng. Đó là trục liên minh bốn trụ cột dân tộc và sứ mệnh làm chủ đại dự án Đường sắt tốc độ cao 67 tỷ USD."

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cắt ngắn các danh từ riêng công nghệ (chỉ dùng akaBot thay vì trợ lý tự động hóa akaBot; SAP S/4HANA thay vì hệ thống quản trị nguồn lực doanh nghiệp SAP S/4HANA Cloud...).

---

### [ERR-20260914-GROUNDING-01] Suy diễn danh xưng không có nguồn kiểm chứng: "Top 3 đến Top 5 hành tinh"

- **Thời gian ghi nhận:** 2026-09-14 16:25:00
- **Pha sản xuất & Tệp tin:** Pha 5 (`04_hook_pack.md`), Pha 7 (`chapter_01.md`, `chapter_02.md`), Bức tranh toàn cảnh (`vault/00_Global_Vision_Synthesis.md`)
- **Mô hình & Chuyên gia (Persona):** Gemini 3.8 Flash + The Narrative Director
- **Nhóm phân loại lỗi (Category):** `[DATA_GROUNDING]` + `[HUMAN_REJECTION]`
- **Mức độ nghiêm trọng (Severity):** CRITICAL (Lỗi giật tít suy diễn ngoài đời thực, đe dọa uy tín học thuật của kênh)
- **Trạng thái:** Resolved (Thay thế bằng phân tích so sánh công suất xưởng thực tế 500k tấn vượt các nhà thầu Châu Âu như Severfield 300k, Eversendai 200k và cạnh tranh với Mỹ).

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> "Một doanh nghiệp cơ khí Việt Nam đang sở hữu năng lực chế tạo lọt vào Top ba đến Top năm hành tinh."

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: Giao thức Zero-Ungrounded-Inference (ZUI) — Bắt buộc mọi khẳng định vị thế phải có nguồn đối soát thực chứng công khai; Tuyệt đối cấm phóng đại danh xưng thứ hạng khi ngành không có bảng xếp hạng chính thức.
- Tệp quy định: `00_core/voice_dna.md`, `.agents/skills/chapter_writer/SKILL.md`, phản hồi kiểm chứng trực tiếp của Người dùng.

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- DDC trong thực tế chỉ tuyên bố: Top 1 Việt Nam và mục tiêu chiến lược 2030 là "Top 10 Châu Á". Ngành gia công kết cấu thép toàn cầu mang tính phân mảnh cao và không có bảng xếp hạng xếp hạng chính thức cho các nhà thầu gia công.
- Ở các phiên phân tích trước, mô hình tự làm bài toán so khớp công suất xưởng (500k tấn của DDC so với Schuff 400k, Severfield 300k, Eversendai 200k ngoài Trung Quốc) rồi rút gọn một cách nguy hiểm thành danh xưng tuyệt đối: "Top ba đến Top năm hành tinh". Khán giả khi tra cứu trên mạng không tìm thấy nguồn kiểm chứng sẽ lập tức quy chụp kênh giật tít "ngạo nghễ rởm".

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Thay đổi câu mở đầu Hook theo chỉ đạo của Người dùng: Chuyển từ việc phong danh hiệu mơ hồ sang đối chiếu quy mô thực tế:
> "Có thể bạn sẽ rất bất ngờ khi biết rằng: Giữa một thị trường mà các gã khổng lồ kết cấu thép của Anh, Mỹ hay Nhật Bản đã định hình cả thế kỷ, một doanh nghiệp cơ khí Việt Nam đang vận hành hệ thống nhà xưởng nửa triệu tấn mỗi năm — một năng lực chế tạo đủ sức vượt mặt những nhà thầu hàng đầu châu Âu và bước thẳng vào chuỗi cung ứng siêu trường siêu trọng toàn cầu."
- Tách câu hoàn chỉnh ngữ pháp < 150 ký tự, loại bỏ dấu em-dash (`—`) cho bản voiceover `chapter_01.md`.
- Sửa lại Chương 2: Làm rõ việc so sánh công suất xưởng thuần túy (500.000 tấn vs 300.000 tấn của Severfield Anh, 200.000 tấn của Eversendai), bỏ câu khẳng định "xếp vào Top 3-5".

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cập nhật quy tắc ZUI: Đối với mọi tuyên bố thứ hạng toàn cầu (Top X thế giới), bắt buộc phải trích dẫn tên tổ chức xếp hạng (Fortune, Forbes, ENR, World Steel Association...). Nếu không có tổ chức xếp hạng chính thức, tuyệt đối KHÔNG phong danh hiệu mà phải diễn đạt bằng sự thật so sánh định lượng (Quy mô công suất xưởng, diện tích ha, số lượng chứng chỉ).
