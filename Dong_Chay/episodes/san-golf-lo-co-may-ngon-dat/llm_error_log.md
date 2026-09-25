# SỔ CÁI GHI NHẬN & PHÂN TÍCH LỖI LLM (LLM DEFECT & ERROR LOG)
## Episode: san-golf-lo-co-may-ngon-dat — Vì Sao 90% Sân Golf Thua Lỗ Nhưng Vẫn Đua Nhau Làm?

> **Kênh:** Dòng Chảy
> **Mục đích:** Lưu vết toàn bộ các khiếm khuyết, lỗi vi phạm quy tắc, ảo giác số liệu/lịch sử, trôi dạt văn phong hoặc phản hồi từ chối từ Người dùng trong quá trình LLM sinh nội dung.
> **Ý nghĩa:** Cung cấp dữ liệu thực chứng cho Pha 16 (Postmortem) và định kỳ tối ưu hóa System Prompts, Skills và Rules.

---

## 1. THỐNG KÊ TỔNG QUAN (DEFECT METRICS SUMMARY)

| Nhóm Phân Loại Lỗi (Category) | Mã Phân Loại | Số Lượng Lỗi | Mức Độ Nghiêm Trọng Cao Nhất |
|---|---|:---:|:---:|
| Định dạng, Cú pháp & Kỹ thuật TTS | `[FORMAT_SYNTAX]` | 1 | MAJOR |
| Giọng điệu, Từ cấm & Văn phong | `[VOCABULARY_TONE]` | 1 | CRITICAL |
| Dữ liệu, Trích dẫn & Ảo giác | `[DATA_GROUNDING]` | 2 | MAJOR |
| Logic, Lập luận & Cấu trúc | `[LOGIC_REASONING]` | 1 | CRITICAL |
| Quy trình, Giao thức & Persona | `[PROCESS_PROTOCOL]` | 0 | - |
| Phản hồi & Từ chối từ Người dùng | `[HUMAN_REJECTION]` | 3 | CRITICAL |
| **TỔNG CỘNG** | | **8** | **CRITICAL** |

---

## 2. BẢNG TRA CỨU NHANH CÁC LỖI (DEFECT INDEX)

| Mã Lỗi | Thời Gian | Pha / Tệp Tin | Model & Persona | Nhóm Lỗi | Mức Độ | Trạng Thái Xử Lý |
|---|---|---|---|---|:---:|:---:|
| `ERR-20260922-USER-01` | 2026-09-22 10:52 | Pha 7 / `chapter_01`–`08.md` | `the_narrative_director` | `[HUMAN_REJECTION]` + `[FORMAT_SYNTAX]` | MAJOR | Resolved |
| `ERR-20260922-USER-02` | 2026-09-22 11:11 | Pha 1, 2, 2.5 / `01_topic`, `02_plan`, `00_GVS` | `the_macro_strategist` | `[HUMAN_REJECTION]` + `[LOGIC_REASONING]` + `[VOCABULARY_TONE]` | CRITICAL | Resolved |
| `ERR-20260922-USER-03` | 2026-09-22 16:32 | Pha 7, 12 / `chapter_01`, `06`, `07` | `the_corporate_finance_analyst` + `the_critical_auditor` | `[HUMAN_REJECTION]` + `[DATA_GROUNDING]` | MAJOR | Resolved |

---

## 3. NHẬT KÝ CHI TIẾT CÁC LỖI PHÁT SINH (DETAILED DEFECT ENTRIES)

### [ERR-20260922-USER-01] Người dùng từ chối định dạng kịch bản "viết mỗi câu một dòng, không phân đoạn" (One-sentence Paragraphs Defect)
- **Thời gian ghi nhận:** 2026-09-22 10:52:00
- **Pha sản xuất & Tệp tin:** Pha 7 / `chapter_01.md` đến `chapter_08.md`, `final_voiceover.md`
- **Mô hình & Chuyên gia (Persona):** `the_narrative_director` + `the_voice_architect`
- **Nhóm phân loại lỗi (Category):** `[HUMAN_REJECTION]` + `[FORMAT_SYNTAX]`
- **Mức độ nghiêm trọng (Severity):** MAJOR
- **Trạng thái:** Resolved

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> Phản hồi của Người dùng: *"tại sao vẫn viết mỗi câu trên 1 dòng thế???"*
> Hiện trạng bản thảo: Cứ sau mỗi câu kết thúc bằng dấu chấm, kịch bản tự động ngắt dòng đôi (`\n\n`), tạo ra hàng trăm dòng đơn câu rời rạc thay vì tổ chức thành các đoạn văn tư duy hoàn chỉnh (2–4 câu/đoạn).

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Quy chuẩn cấu trúc đoạn văn kịch bản (`voiceover_style_guide.md §5` và `Anti-Staccato Mandate`): Kịch bản phải được tổ chức thành các đoạn văn tư duy hoàn chỉnh gồm từ 2 đến 4 câu liên kết cùng một mạch ý.

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- Khi thực thi quy định "siết trần độ dài câu thoại <= 120 ký tự cho mô hình TTS", LLM đã ngộ nhận một cách máy móc rằng mỗi câu thoại phải ngắt dòng đôi (`\n\n`), biến toàn bộ văn bản thành các đoạn văn 1 câu (one-sentence paragraphs).

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Tái cấu trúc toàn bộ 8 chương (`chapter_01.md` đến `chapter_08.md`) thành các đoạn văn tự nhiên (2–4 câu/đoạn), giữ nguyên câu thoại ngắn <= 115 ký tự và nhịp phát thanh chuẩn.
- Đồng bộ hóa toàn bộ sang `final_voiceover.md`.

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Khóa chặt quy tắc cấu trúc đoạn văn (2–4 câu/đoạn) trong `chapter_writer` skill và kiểm toán tự động số câu trung bình mỗi đoạn văn.

---

### [ERR-20260922-USER-02] Người dùng từ chối toàn diện góc nhìn phán xét đạo đức và thiên kiến tiêu cực/thua lỗ (Negative & Moralizing Bias Defect)
- **Thời gian ghi nhận:** 2026-09-22 11:11:29
- **Pha sản xuất & Tệp tin:** Toàn bộ pipeline từ Pha 1 (`01_topic_qualification.md`), Pha 2 (`02_research_plan.md`), Pha 2.5 (`vault/00_Global_Vision_Synthesis.md`) đến các chương kịch bản.
- **Mô hình & Chuyên gia (Persona):** `the_macro_strategist` + `the_content_strategist`
- **Nhóm phân loại lỗi (Category):** `[HUMAN_REJECTION]` + `[LOGIC_REASONING]` + `[VOCABULARY_TONE]`
- **Mức độ nghiêm trọng (Severity):** CRITICAL
- **Trạng thái:** In Progress

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> Phản hồi của Người dùng: *"cách viết của bạn hiện tại có phần phán xét lĩnh vực sân golf đúng không? thay vì phân tích cơ chế, mà ddag đi sâu vào việc nó lỗ thì phải? đi sâu vào case thất bại hơn case thành công à? đại phẫu lại từ file tầm nhìn, file tư duy, và phải làm lại kế hoạch nghiên cứu sâu từ đầu, làm lại từ đầu đi. xóa hết cái gì liên quan đến tầm nhìn cũ để làm lại từ đầu"*

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tôn chỉ kênh Dòng Chảy: Phân tích kinh tế học cơ chế và động lực học hệ thống (First-Principles & Incentives). Tuyệt đối không phán xét đạo đức, không dùng giọng điệu quan tòa đạo đức lên án các chủ thể kinh tế.
- Giao thức Steelmanning & Phản biện Tam diện (Tri-Adversarial Council): Bắt buộc phân tích đa chiều, khách quan, giải phẫu cả cơ chế thành công lẫn nguyên nhân gãy đổ, không được thiên kiến tiêu cực hay sa đà vào các ca thất bại cá biệt.

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- **Lệch pha sang Phán xét Đạo đức (Moralizing Tone):** Sử dụng các từ ngữ định kiến ("cuộc vui xa xỉ", "tấm bình phong trục lợi", "lòng tham đầu cơ") thay vì thuật ngữ kinh tế học khách quan ("chi phí cơ hội của đất", "tối ưu hóa danh mục", "chiết khấu dòng tiền").
- **Thiên kiến Tiêu cực / Ám thị Thua lỗ (Failure Fixation):** Quá tập trung vào 90% sân golf độc lập thua lỗ (PV-Inconess, sụp đổ bong bóng Nhật Bản) mà bỏ qua giải phẫu bản chất của 10% sân golf thành công rực rỡ và các mô hình tạo giá trị thặng dư thực chất trên thế giới (Cụm du lịch golf quốc tế Thái Lan/Đà Nẵng, Tiện ích mỏ neo đô thị, Golf giải trí công nghệ).

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Đại phẫu toàn diện từ gốc:
  1. Tái lập `01_topic_qualification.md` (Pha 1): Thiết lập Bản đồ Không gian Hệ thống đối sánh 3 mô hình (Du lịch quốc tế, Mỏ neo đô thị, và Đầu cơ đòn bẩy); triệt tiêu 100% ngôn ngữ phán xét.
  2. Tái lập `02_research_plan.md` (Pha 2): Thiết kế lại hệ thống truy vấn NotebookLM đa chiều bao quát dữ liệu của cả mô hình thành công lẫn mô hình thất bại.
  3. Tái lập `vault/00_Global_Vision_Synthesis.md` (Pha 2.5): Bản đồ địa hình hiện thực 4 tầng khách quan, cân bằng, tuyệt đối cấm chia chương trước Pha 4.

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cập nhật rào cản kiểm toán trong `compliance_council/SKILL.md` và `anti_ai_isms.md`: Đưa các từ ngữ phán xét đạo đức ("trục lợi", "xa xỉ", "lòng tham", "tấm bình phong") vào Blacklist bắt buộc loại bỏ.


### [ERR-20260922-USER-03] Người dùng yêu cầu hiệu chuẩn 3 chi tiết thực tế: Lao động caddie, Tên thương mại sân Yên Thắng, và Phân hóa thể chế Luật Đất đai 2024
- **Thời gian ghi nhận:** 2026-09-22 16:32:00
- **Pha sản xuất & Tệp tin:** Pha 7 (`chapter_01.md`, `chapter_06.md`, `chapter_07.md`), Pha 8 (`voiceover.md`), Pha 12+ (`visual_plus` & manifests).
- **Mô hình & Chuyên gia (Persona):** `the_corporate_finance_analyst` + `the_critical_auditor` + `the_voice_architect`
- **Nhóm phân loại lỗi (Category):** `[HUMAN_REJECTION]` + `[DATA_GROUNDING]`
- **Mức độ nghiêm trọng (Severity):** MAJOR
- **Trạng thái:** Resolved

#### 1. Đoạn trích vi phạm nguyên văn & Góp ý của Người dùng (Raw Violation Snippet):
> 1. **Chương 7 (Lao động Caddie):** Bản thảo viết *"Họ được đóng bảo hiểm và tiếp cận môi trường làm việc chuyên nghiệp."* -> Nhận định quá màu hồng so với thực tế lao động Việt Nam (caddie ký khoán theo vòng, thu nhập 70-80% từ tip, ít khi có BHXH đầy đủ).
> 2. **Chương 1 (Tên sân golf PV-Inconess):** Bản thảo viết *"chủ sân Yên Thắng"* -> Chưa chuẩn tên thương mại phổ biến nhất là *"sân golf Hoàng Gia (Royal Golf Club) tại hồ Yên Thắng"*.
> 3. **Chương 6 (Luật Đất đai 2024):** Khi nói về tiền thuê đất tăng vọt, thiếu chú thích phân hóa rằng: *"Điều chỉnh trực tiếp và nặng nề nhất đối với các dự án thuê đất trả tiền hàng năm. Dự án đã nộp tiền một lần cho cả vòng đời 50 năm từ trước sẽ không bị điều chỉnh ngay."*

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Quy chuẩn Bám sát Thực chứng & Không lý tưởng hóa (Grounded Labor & Institutional Realism): Không đưa ra các nhận định viễn cảnh thiếu kiểm chứng thực tế về quyền lợi bảo hiểm; phải nêu chính xác tên thương mại nhận diện công chúng; và phải phân hóa rõ đối tượng chịu tác động pháp lý.

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- **Caddie labor:** LLM tổng quát hóa khái niệm "chuyển dịch từ nông nghiệp sang dịch vụ" thành "được đóng bảo hiểm đầy đủ", thiếu nhạy cảm với bản chất hợp đồng giao khoán việc trong ngành golf Việt Nam.
- **Tên thương mại:** LLM dùng tên địa danh hành chính (hồ Yên Thắng) thay vì gắn kèm tên thương mại chính thức đã đăng ký và nổi tiếng trong giới golf (Hoàng Gia / Royal Golf Club).
- **Phân loại tiền thuê đất:** LLM gộp chung "tiền thuê đất tăng gấp 3–5 lần" mà không phân định giữa 2 cơ chế tài chính: thuê đất trả tiền hàng năm (chịu sốc ngay) và thuê đất trả tiền một lần cho cả thời gian thuê (được bảo lưu giá đã nộp).

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- **Chương 1:** Chỉnh câu thoại thành: *"Báo cáo của PV-Inconess, đơn vị sở hữu sân golf Hoàng Gia tại hồ Yên Thắng, ghi nhận lỗ ròng suốt mười hai năm liên tiếp."* (Cập nhật `chapter_01.md`, `voiceover.md`, `chapter_01_visual_plus.md`, `infographics_manifest_chapter_01.json`).
- **Chương 6:** Bổ sung phân hóa pháp lý: Thoại nhấn mạnh cú sốc giáng vào nhóm dự án thuê đất trả tiền hàng năm; trên đồ họa Infographic `CH06_SC016` & `CH06_SC017` thêm ghi chú pháp lý phân định rõ rệt nhóm trả hàng năm vs nộp một lần 50 năm.
- **Chương 7:** Sửa câu thoại thành: *"Nhiều lao động được tiếp cận môi trường dịch vụ chuyên nghiệp, dù thu nhập phần lớn vẫn phụ thuộc vào lượt chơi và tiền tip của khách."* (Cập nhật `chapter_07.md`, `voiceover.md`, `chapter_07_visual_plus.md`, `prompts_chapter_07_veo.txt`).

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Cập nhật vào `.agents/personas/the_corporate_finance_analyst.md`: Khi phân tích chính sách đất đai (Luật Đất đai 2024), luôn tự động phân hóa 2 phương thức trả tiền thuê đất (hàng năm vs một lần).
- Cập nhật vào `00_core/fact_checking_checklist.md`: Khi đề cập đến lao động caddie, luôn gắn liền với cơ chế thu nhập khoán vòng + tip, cấm giả định mặc định có BHXH.

---

## 4. TỔNG KẾT ĐỀ XUẤT VÁ HỆ THỐNG SAU TẬP (POST-EPISODE SYSTEMIC PATCHES)

| STT | Mã Lỗi | Tệp Hệ Thống Đề Xuất Vá | Bản Chất Bản Vá Đề Xuất | Trạng Thái Thực Thi |
|:---:|---|---|---|---|
| 1 | `ERR-20260922-USER-01` | `.agents/skills/chapter_writer/SKILL.md` | Bổ sung kiểm toán tự động tỷ lệ phân đoạn văn tư duy (2–4 câu/đoạn). | Pending |
| 2 | `ERR-20260922-USER-02` | `00_core/anti_ai_isms.md` & `compliance_council/SKILL.md` | Đưa nhóm từ ngữ phán xét đạo đức vào Blacklist bắt buộc quét sạch. | Pending |
| 3 | `ERR-20260922-USER-03` | `.agents/personas/the_corporate_finance_analyst.md` & `fact_checking_checklist.md` | Phân hóa thuê đất hàng năm vs 50 năm; chuẩn hóa bản chất lao động caddie (khoán + tip). | Pending |
