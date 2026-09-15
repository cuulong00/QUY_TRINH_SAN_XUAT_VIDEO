# SỔ CÁI PHÂN TÍCH & TỐI ƯU HÓA KHUYẾT TẬT LLM (CENTRAL LLM DEFECT ANALYTICS)

> **Mục đích tài liệu:** Quản trị tập trung toàn bộ các khuyết tật, lỗi lặp lại và phản hồi từ chối của Người dùng từ tất cả các tập video trong hệ sinh thái **GocNhinPodcast**.
> **Cơ chế vận hành:** Tự động tổng hợp dữ liệu từ các tệp `episodes/[slug]/llm_error_log.md` sau mỗi phiên làm việc hoặc sau Pha 16 (Postmortem) để phân tích xu hướng và lập kế hoạch vá System Prompts / Rules định kỳ.

---

## 1. THỐNG KÊ XU HƯỚNG LIÊN TẬP (CROSS-EPISODE METRICS)

| Episode Slug | Tổng Số Lỗi | Format/Syntax | Vocab/Tone | Data Grounding | Logic/Reasoning | Protocol | Human Rejection | Tỷ Lệ Giải Quyết |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `kinh-te-hoc-tam-linh` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100% |

---

## 2. BẢNG XẾP HẠNG CÁC "TẬT XẤU" PHỔ BIẾN NHẤT CỦA LLM (TOP RECURRING PATTERNS)

1. **Câu dài vượt giới hạn âm thanh (>150 ký tự):** Mô hình có xu hướng viết câu phức ghép mệnh đề quan hệ khi phân tích vĩ mô, gây đứt hơi cho TTS.
2. **Trôi dạt từ cấm AI (AI-isms Leakage):** Xuất hiện các cụm từ sáo rỗng như *"đóng vai trò quan trọng"*, *"không thể phủ nhận"*, *"bức tranh toàn cảnh"* khi mô hình cố gắng liên kết ý.
3. **Cắt xén cơ chế kỹ thuật (Mechanism Amputation):** Khi bị ép trần số từ (Floor/Ceiling), LLM có xu hướng cắt bỏ các bước logic của cơ chế kinh tế/vật lý thay vì viết cô đọng câu chữ.
4. **Scaffolding Leakage:** Vô tình in tên block hoặc nhãn phân tích vào văn bản thành phẩm xuất bản.
5. **Human Preference Rejection:** Người dùng yêu cầu thay đổi framing do LLM diễn giải quá tiêu cực hoặc quá thiên lệch mà thiếu tính biện chứng đa chiều.

---

## 3. NHẬT KÝ BẢN VÁ HỆ THỐNG ĐÃ ÁP DỤNG (SYSTEMIC PATCH CHANGELOG)

| Ngày Áp Dụng | Mã Lỗi Gốc / Nguồn | Tệp Đã Được Vá | Nội Dung Bản Vá & Răn Đe Bổ Sung | Tác Giả / Người Duyệt |
|:---:|---|---|---|:---:|
| 2026-09-14 | INIT-SYSTEM | `.agents/rules/content-os-pipeline.md` | Bổ sung Giao thức Bắt buộc Ghi Log Lỗi LLM (LLM Defect Logging Mandate) | Trần Tuấn Dương |
| 2026-09-14 | INIT-SYSTEM | `.agents/skills/chapter_writer/SKILL.md` | Tích hợp trạm Post-Write Audit Gate & Revise Gate tự động ghi log lỗi | Trần Tuấn Dương |
