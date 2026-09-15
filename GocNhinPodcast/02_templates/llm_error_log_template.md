# SỔ CÁI GHI NHẬN & PHÂN TÍCH LỖI LLM (LLM DEFECT & ERROR LOG)
## Episode: [slug] — [Tên Episode]

> **Mục đích tài liệu:** Lưu vết toàn bộ các khiếm khuyết, lỗi vi phạm quy tắc, ảo giác số liệu, trôi dạt văn phong hoặc các trường hợp Người dùng từ chối bản nháp trong suốt quá trình LLM sinh nội dung cho episode này.
> **Ý nghĩa:** Cung cấp dữ liệu thực chứng phục vụ khâu Hậu kiểm (Pha 16 - Postmortem) và làm căn cứ định kỳ nâng cấp, vá lỗi cho System Prompts, Skills và Bộ quy tắc vận hành của kênh.

---

## 1. THỐNG KÊ TỔNG QUAN (DEFECT METRICS SUMMARY)

| Nhóm Phân Loại Lỗi (Category) | Mã Phân Loại | Số Lượng Lỗi | Mức Độ Nghiêm Trọng Cao Nhất |
|---|---|:---:|:---:|
| Định dạng, Cú pháp & Kỹ thuật TTS | `[FORMAT_SYNTAX]` | 0 | - |
| Giọng điệu, Từ cấm & Văn phong | `[VOCABULARY_TONE]` | 0 | - |
| Dữ liệu, Trích dẫn & Ảo giác | `[DATA_GROUNDING]` | 0 | - |
| Logic, Lập luận & Cấu trúc | `[LOGIC_REASONING]` | 0 | - |
| Quy trình, Giao thức & Persona | `[PROCESS_PROTOCOL]` | 0 | - |
| Phản hồi & Từ chối từ Người dùng | `[HUMAN_REJECTION]` | 0 | - |
| **TỔNG CỘNG** | | **0** | - |

---

## 2. BẢNG TRA CỨU NHANH CÁC LỖI (DEFECT INDEX)

| Mã Lỗi | Thời Gian | Pha / Tệp Tin | Model & Persona | Nhóm Lỗi | Mức Độ | Trạng Thái Xử Lý |
|---|---|---|---|---|:---:|:---:|
| *[ERR-YYYYMMDD-CHXX-01]* | *YYYY-MM-DD* | *chapter_01.md* | *Gemini 3.8 Flash / the_industrial_economist* | *[FORMAT_SYNTAX]* | *MINOR* | *Resolved* |

---

## 3. NHẬT KÝ CHI TIẾT CÁC LỖI PHÁT SINH (DETAILED DEFECT ENTRIES)

<!--
MỖI KHI PHÁT HIỆN HOẶC ĐƯỢC BÁO LỖI, AGENT BẮT BUỘC THÊM 1 ENTRY THEO KHUNG CHUẨN DƯỚI ĐÂY:
-->

### Template Entry Chuẩn (Dùng để copy khi tạo entry mới):

```markdown
### [ERR-YYYYMMDD-CHXX-NN] [Tên ngắn gọn mô tả bản chất lỗi]

- **Thời gian ghi nhận:** YYYY-MM-DD HH:MM:SS
- **Pha sản xuất & Tệp tin:** [Ví dụ: Pha 7 - chapter_02.md / Pha 4 - 07_outline.md / Pha 6 - 08_chapter_briefs.md]
- **Mô hình & Chuyên gia (Persona):** [Ví dụ: Gemini 3.8 Flash (High) + the_industrial_economist]
- **Nhóm phân loại lỗi (Category):** [FORMAT_SYNTAX | VOCABULARY_TONE | DATA_GROUNDING | LOGIC_REASONING | PROCESS_PROTOCOL | HUMAN_REJECTION]
- **Mức độ nghiêm trọng (Severity):** [CRITICAL (Phế phẩm/vi phạm redline) | MAJOR (Sai lệch cấu trúc/dữ liệu cần viết lại) | MINOR (Lỗi câu từ/format chỉnh nhanh)]
- **Trạng thái:** [Resolved | Pending Review | System Patch Needed]

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> "Trích nguyên văn câu hoặc đoạn văn bản mà LLM đã viết sai hoặc hành vi vi phạm quy trình..."

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- Tên quy tắc: [Ví dụ: Giới hạn câu thoại < 150 ký tự tại SKILL.md / Từ cấm tại 00_core/anti_ai_isms.md / Nguyên tắc Zero-Scaffolding]
- Tệp quy định: [Đường dẫn file rule tương ứng]

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- Tại sao LLM lại tạo ra lỗi này? (Ví dụ: Do ngữ cảnh prompt quá dài khiến mô hình quên câu lệnh tiêu cực; do xung đột giữa Persona muốn phân tích chi tiết và quy định cắt ngắn câu; do User ra lệnh bằng ngôn ngữ tự nhiên không kèm flag...)

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- Đoạn văn bản đã được biên tập lại sạch sẽ / Hành động đã thực hiện để khắc phục:
> "Đoạn văn bản sau khi sửa đạt chuẩn 100%..."

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- Đề xuất cụ thể sửa đổi file nào trong hệ thống để triệt tiêu vĩnh viễn lỗi này:
  * File cần sửa: `[Đường dẫn file]`
  * Nội dung cần thêm/sửa: `[Mô tả câu lệnh hoặc ràng buộc cần bổ sung]`
```

---

## 4. TỔNG KẾT ĐỀ XUẤT VÁ HỆ THỐNG SAU TẬP (POST-EPISODE SYSTEMIC PATCHES)

Sau khi hoàn thành tập video, toàn bộ các đề xuất tại Mục 5 của các lỗi trên sẽ được tổng hợp vào bảng này để chuyển giao cho **Pha 16 (Postmortem)** và cập nhật vào Sổ cái quản trị trung tâm `01_management/llm_error_analytics.md`:

| STT | Mã Lỗi | Tệp Hệ Thống Đề Xuất Vá | Bản Chất Bản Vá Đề Xuất | Trạng Thái Thực Thi |
|:---:|---|---|---|:---:|
| 1 | | | | Chưa áp dụng |
