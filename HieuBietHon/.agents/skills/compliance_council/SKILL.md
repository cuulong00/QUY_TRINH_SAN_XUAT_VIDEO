---
name: compliance-council
description: "Editorial & Compliance Council. Reviews script safety, legal compliance, oral rhythm, and implements the Term-Breath Debate Protocol."
---

# Editorial & Compliance Council — Hội đồng Biên tập & Kiểm duyệt

> 🛑 **EXPERT PERSONAS (BẮT BUỘC HÓA THÂN)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC phải dùng tool `view_file` đọc lần lượt các tệp Persona của nhóm kiểm duyệt:
> 1. `[HieuBietHon/.agents/personas/the_data_auditor.md]`
> 2. `[HieuBietHon/.agents/personas/the_voice_architect.md]`
> 3. `[HieuBietHon/.agents/personas/the_quality_czar.md]`
>
> Nếu chưa nạp đủ cả 3 tệp này trong phiên làm việc, NGHIÊM CẤM tạo output.

## Trọng tâm Kiểm duyệt Song song
Hội đồng sẽ tiến hành quét toàn bộ bản thảo chương kịch bản (`chapter_XX.md`) trên 3 phương diện cùng một lúc:

### 1. Editorial Safety & Objectivity (An toàn & Khách quan)
*   **Tiêu chuẩn:** Kiểm tra nghiêm ngặt Luật An ninh mạng Việt Nam và các quy định truyền thông. 
*   **Nguyên tắc chống phán xét đạo đức (Anti-Moralizing):** Cấm tuyệt đối việc dùng từ ngữ phê phán đạo đức tiêu cực một chiều lên các cá nhân hoặc tập thể. Bắt buộc phải giải thích hành vi của họ dưới lăng kính phân tích động lực kinh tế/xã hội (Incentive Analysis).
*   **Tuyên bố miễn trừ:** Đảm bảo cuối kịch bản luôn có câu tuyên bố: `Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng`.

### 2. Oral Flow & Rhythmic Audit (Nhịp điệu nói)
*   **Tiêu chuẩn:** Kiểm tra độ dài câu thoại cho voiceover. Mọi câu thoại phải đảm bảo độ trôi chảy khi đọc bằng tai.

### 3. Giao thức Tranh biện Thuật ngữ & Nhịp thở (Term-Breath Protocol)
Đối với giới hạn kỹ thuật cứng **150 ký tự/câu** của máy đọc TTS:
*   ⛔ **CẤM:** Tuyệt đối cấm hạ cấp từ vựng (ví dụ: đổi từ cụm thuật ngữ chính sách chuyên ngành thành từ ngữ bình dân thô ráp để câu ngắn lại).
*   ✅ **PHƯƠNG PHÁP CHUẨN:** Thực hiện ngắt câu cơ học bằng cách sử dụng **dấu chấm (.) hoặc dấu chấm phẩy (;)** tại các điểm nghỉ hơi tự nhiên của câu thoại, giữ nguyên vẹn 100% hệ thuật ngữ học thuật và chính sách đắt giá của câu gốc.

---

## Chỉ số Chất lượng Kịch bản (Script Quality Metrics)
Hội đồng đánh giá chất lượng kịch bản trên thang điểm 10 đối với 3 tiêu chí:
1.  **Novelty (Tính mới - Trọng số 30%):** Góc nhìn có phát hiện ra khoảng trống thông tin mới không? Hay chỉ lặp lại báo chí?
2.  **Flow (Nhịp điệu nói - Trọng số 30%):** Câu từ nghe có tự nhiên, không vấp, dễ nghỉ hơi cho voiceover?
3.  **Anchoring Density (Mật độ số liệu - Trọng số 40%):** Mỗi chương kịch bản bắt buộc phải có ít nhất 1 số liệu định lượng, nghị định pháp lý hoặc trích dẫn chuyên gia chính thống.

---

## Quy chuẩn Báo cáo Kiểm duyệt (`10_compliance_report.md`)
Kết quả kiểm duyệt của Hội đồng phải được ghi nhận chi tiết thành tệp `10_compliance_report.md` tại thư mục episode với format:

```markdown
# Editorial & Compliance Report — [Slug]

## 1. Điểm số chất lượng (Quality Scores)
*   **Novelty:** X/10 — [Nhận xét chi tiết]
*   **Flow:** X/10 — [Nhận xét chi tiết]
*   **Anchoring Density:** X/10 — [Nhận xét chi tiết]

## 2. Nhật ký Tranh biện Thuật ngữ & Nhịp thở (Term-Breath Debate Log)
*   **[The Voice Architect]:** "Câu thoại này dài quá 150 ký tự (X ký tự), máy đọc TTS sẽ bị hụt hơi. Đề xuất viết lại cho ngắn..."
*   **[The Data Auditor]:** "Nếu sửa như vậy sẽ làm mất đi tính chính xác của cụm thuật ngữ pháp lý '[Tên thuật ngữ]'. Tôi đề xuất giữ nguyên thuật ngữ và ngắt câu bằng dấu chấm phẩy (;) tại đây..."
*   **[The Quality Czar]:** "Thống nhất phương án ngắt câu cơ học: '[Văn bản câu thoại sau khi ngắt]'."

## 3. Nhật ký sửa đổi (Edit Logs)
| Chương | Câu gốc | Câu sửa đổi | Lý do | Người đề xuất |
|--------|---------|-------------|-------|---------------|
| Chapter 1 | ... | ... | Ngắt câu TTS / Loại bỏ từ nhạy cảm | Voice Architect / Auditor |
```
