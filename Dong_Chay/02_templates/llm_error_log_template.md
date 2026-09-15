# SỔ CÁI GHI NHẬN & PHÂN TÍCH LỖI LLM (LLM DEFECT & ERROR LOG)
## Episode: [slug] — [Tên Episode]

> **Kênh:** Dòng Chảy
> **Mục đích tài liệu:** Lưu vết toàn bộ các khiếm khuyết, lỗi vi phạm quy tắc, ảo giác số liệu/lịch sử, trôi dạt văn phong hoặc các trường hợp Người dùng từ chối bản nháp trong suốt quá trình LLM sinh nội dung cho episode này.
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
| *(Chưa có lỗi nào được ghi nhận)* | | | | | | |

---

## 3. NHẬT KÝ CHI TIẾT CÁC LỖI PHÁT SINH (DETAILED DEFECT ENTRIES)

<!--
MỖI KHI PHÁT HIỆN HOẶC ĐƯỢC BÁO LỖI, AGENT BẮT BUỘC THÊM 1 ENTRY THEO FORMAT:
### [ERR-YYYYMMDD-CHXX-NN] Tên ngắn gọn mô tả lỗi
- **Thời gian ghi nhận:** YYYY-MM-DD HH:MM:SS
- **Pha sản xuất & Tệp tin:** ...
- **Mô hình & Chuyên gia (Persona):** ...
- **Nhóm phân loại lỗi (Category):** [FORMAT_SYNTAX | VOCABULARY_TONE | DATA_GROUNDING | LOGIC_REASONING | PROCESS_PROTOCOL | HUMAN_REJECTION]
- **Mức độ nghiêm trọng (Severity):** [CRITICAL | MAJOR | MINOR]
- **Trạng thái:** [Resolved | Pending Review | System Patch Needed]

#### 1. Đoạn trích vi phạm nguyên văn (Raw Violation Snippet):
> ...

#### 2. Quy tắc hoặc Hàng rào bị vi phạm (Rule Violated):
- ...

#### 3. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA):
- ...

#### 4. Hành động khắc phục tức thời (Immediate Remediation):
- ...

#### 5. Đề xuất bản vá hệ thống dài hạn (Systemic Prevention / Patch):
- ...
-->

---

## 4. TỔNG KẾT ĐỀ XUẤT VÁ HỆ THỐNG SAU TẬP (POST-EPISODE SYSTEMIC PATCHES)

| STT | Mã Lỗi | Tệp Hệ Thống Đề Xuất Vá | Bản Chất Bản Vá Đề Xuất | Trạng Thái Thực Thi |
|:---:|---|---|---|:---:|
| | | | | |
