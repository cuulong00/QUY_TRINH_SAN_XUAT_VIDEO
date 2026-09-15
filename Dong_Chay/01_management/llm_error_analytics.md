# SỔ CÁI PHÂN TÍCH & TỐI ƯU HÓA KHUYẾT TẬT LLM (CENTRAL LLM DEFECT ANALYTICS)

> **Kênh:** Dòng Chảy
> **Mục đích tài liệu:** Quản trị tập trung toàn bộ các khuyết tật, lỗi lặp lại và phản hồi từ chối của Người dùng từ tất cả các tập video trong hệ sinh thái **Dòng Chảy**.
> **Cơ chế vận hành:** Tự động tổng hợp dữ liệu từ các tệp `episodes/[slug]/llm_error_log.md` sau mỗi phiên làm việc hoặc sau Pha 16 (Postmortem) để phân tích xu hướng và lập kế hoạch vá System Prompts / Rules định kỳ.

---

## 1. THỐNG KÊ XU HƯỚNG LIÊN TẬP (CROSS-EPISODE METRICS)

| Episode Slug | Tổng Số Lỗi | Format/Syntax | Vocab/Tone | Data Grounding | Logic/Reasoning | Protocol | Human Rejection | Tỷ Lệ Giải Quyết |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *(Chưa có dữ liệu)* | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100% |

---

## 2. BẢNG XẾP HẠNG CÁC "TẬT XẤU" PHỔ BIẾN NHẤT CỦA LLM (TOP RECURRING PATTERNS)

1. **Câu dài vượt giới hạn âm thanh (>150 ký tự):** Mô hình viết câu phức khi phân tích bối cảnh lịch sử/địa chính trị, gây đứt hơi cho TTS.
2. **Trôi dạt từ cấm AI (AI-isms Leakage):** Xuất hiện các cụm từ sáo rỗng như *"đóng vai trò quan trọng"*, *"không thể phủ nhận"*, *"bức tranh toàn cảnh"*.
3. **Ảo giác số liệu hoặc mốc lịch sử (Historical/Data Hallucination):** Nhầm lẫn niên đại, nhân vật, số liệu kiểm toán.
4. **Scaffolding Leakage:** Vô tình in tên block hoặc nhãn phân tích vào kịch bản thành phẩm.
5. **Human Preference Rejection:** Người dùng yêu cầu thay đổi framing kịch bản.

---

## 3. NHẬT KÝ BẢN VÁ HỆ THỐNG ĐÃ ÁP DỤNG (SYSTEMIC PATCH CHANGELOG)

| Ngày Áp Dụng | Mã Lỗi Gốc / Nguồn | Tệp Đã Được Vá | Nội Dung Bản Vá & Răn Đe Bổ Sung | Tác Giả / Người Duyệt |
|:---:|---|---|---|:---:|
| 2026-09-14 | INIT-SYSTEM | `.agents/rules/content-os-pipeline.md` | Bổ sung Giao thức Bắt buộc Ghi Log Lỗi LLM (LLM Defect Logging Mandate) | Trần Tuấn Dương |
| 2026-09-14 | INIT-SYSTEM | `.agents/skills/chapter_writer/SKILL.md` | Tích hợp trạm Post-Write Audit Gate & Revise Gate tự động ghi log lỗi | Trần Tuấn Dương |
