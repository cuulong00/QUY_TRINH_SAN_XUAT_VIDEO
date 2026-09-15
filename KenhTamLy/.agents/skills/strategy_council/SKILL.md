---
name: strategy-council
description: "Scientific & Philosophical Strategy Council. Orchestrates collaborative debate between Topic Strategist, Behavioral Psychologist, and Philosophical Auditor to qualify and design video script angles."
---

# Scientific & Philosophical Strategy Council — Hội đồng Chiến lược Khoa học & Triết học

> 🛑 **EXPERT PERSONAS (BẮT BUỘC HÓA THÂN)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC phải dùng tool `view_file` đọc lần lượt 3 tệp Persona của Hội đồng:
> 1. `[KenhTamLy/.agents/personas/the_topic_strategist.md]`
> 2. `[KenhTamLy/.agents/personas/the_behavioral_psychologist.md]`
> 3. `[KenhTamLy/.agents/personas/the_philosophical_auditor.md]`
>
> Nếu bạn chưa nạp đủ cả 3 tệp này trong phiên làm việc, NGHIÊM CẤM tạo output.

## Quy trình Tranh biện Chiến lược 5 Bước
Hội đồng sẽ tiến hành thảo luận chéo theo đúng trình tự sau để tìm ra Góc tiếp cận tối ưu (Champion Angle) cho kịch bản của kênh Đạo & Khoa Học:

### Bước 1: Khởi xướng Góc nhìn Thu hút & Khoảng trống Tâm lý (Pitching)
*   **Tác nhân thực hiện:** `the_topic_strategist`
*   **Hành động:** Phân tích chủ đề thô của người dùng, xác định "khoảng trống tò mò" (curiosity gap) và các điểm chạm tâm lý/nỗi đau thực tế trong cuộc sống hiện đại. Đề xuất ít nhất 3 tiêu đề kịch tính, cuốn hút để thu hút người xem từ giây đầu tiên.

### Bước 2: Grounding Cơ chế Sinh học & Hành vi (Cognitive & Behavioral Grounding)
*   **Tác nhân thực hiện:** `the_behavioral_psychologist`
*   **Hành động:** Phản biện hoặc bổ sung các đề xuất của Strategist bằng cách đưa ra các mô hình khoa học nhận thức, cơ chế sinh học thần kinh liên quan (ví dụ: vai trò của DMN, amygdala, cortisol, dopamine) và các thí nghiệm tâm lý hành vi thực tế đã được công nhận.

### Bước 3: Phản biện Triết lý & Kiểm chứng Ranh giới Khoa học (Auditing)
*   **Tác nhân thực hiện:** `the_philosophical_auditor`
*   **Hành động:** Rà soát tính khách quan và chiều sâu triết lý sống (sự kết hợp giữa tri thức khoa học và triết lý Phật giáo/thiền). Loại bỏ các tuyên bố bịa đặt thí nghiệm, các ranh giới y khoa/trị liệu lâm sàng bị cấm, và kiểm chứng sự thật để bảo vệ uy tín học thuật của kênh.

### Bước 4: Thiết lập Khung tuyến Kịch bản (Trajectory Outline)
*   **Đồng thuận chung:** Hội đồng thống nhất chọn Góc tiếp cận tối ưu nhất (Champion Angle) và phác thảo khung kịch bản gồm 4 Hồi lớn (thường chia thành 7-10 chương):
    *   *Hồi I (Nhập đề):* Hiện tượng/nghịch lý đời sống gây tò mò, chỉ ra nỗi đau hoặc ảo tưởng tâm lý phổ biến.
    *   *Hồi II (Giải mã cơ chế):* Phân tích nguyên nhân sâu xa về mặt sinh học thần kinh, cơ chế tiến hóa hoặc tâm lý học hành vi.
    *   *Hồi III (Đối chiếu & Triết lý):* Lăng kính triết học, góc nhìn tỉnh thức (Mindfulness/Zen) hoặc các thực chứng thực nghiệm khoa học.
    *   *Hồi IV (Giải pháp thực hành):* Đề xuất các bước hành động/rèn luyện cụ thể, dễ thực hiện để người xem ứng dụng và giải phóng bản thân.

### Bước 5: Thiết lập Kế hoạch Nghiên cứu (Research Planning)
*   Hội đồng thiết kế **Prompt nạp nguồn cấu trúc** (dành cho Deep Research) và **Danh sách câu hỏi trích xuất** (Extraction Queries List) bám sát các chương đã phân chia để chuyển giao công việc cho Pha 2 (Data Mining).

---

## Quy chuẩn ghi nhận Nhật ký Đối thoại (Debate Transcript)
Toàn bộ quá trình tranh luận thực tế của Hội đồng phải được ghi lại dưới dạng đoạn hội thoại chat trực tiếp (Direct Dialogue Logs) trong tệp đầu ra `01_topic_qualification.md` theo cấu trúc sau:

```markdown
## 3. Nhật ký Tranh luận của Hội đồng (Detailed Debate Transcript)
*   **[The Topic Strategist]:** "[Ý kiến trực tiếp về CTR, khoảng trống tò mò, kịch bản mở đầu thu hút, nỗi đau tâm lý...]"
*   **[The Behavioral Psychologist]:** "[Phản hồi trực tiếp chỉ ra cơ chế sinh lý, dopamine, cortisol, hoặc các thí nghiệm tâm lý thực chứng liên quan...]"
*   **[The Philosophical Auditor]:** "[Ý kiến phản biện về chiều sâu triết lý, tính chính xác khoa học, ranh giới y tế/trị liệu và các điểm cần làm rõ...]"
*   **[Đồng thuận chung]:** [Tóm tắt kết luận và lựa chọn góc Champion Angle]
```
> ⛔ **CẤM:** Tuyệt đối không được tóm tắt ý kiến dưới dạng mô tả gián tiếp ("Strategist đề xuất... Psychologist đồng ý..."). Bắt buộc phải viết dưới dạng thoại đối đáp trực tiếp đầy cá tính của từng chuyên gia.
