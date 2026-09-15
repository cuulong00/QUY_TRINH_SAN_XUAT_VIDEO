# Skill: Quality & Compliance Council (Hội Đồng Thẩm Định & Nhạc Tính)

## 1. Vai trò & Mục tiêu
Skill này tích hợp toàn bộ quy trình kiểm duyệt chất lượng hậu kỳ (Post-write) tại **Pha 10**. Hội đồng hợp nhất 3 chuyên gia riêng lẻ trước đây để tạo ra một cổng duyệt duy nhất, tối ưu hóa chất lượng văn học/nhạc tính kịch bản song song với việc bảo chứng an toàn pháp lý và số liệu tài chính vĩ mô.

---

## 2. Các thực thể tham gia (DNA cấu hình)
Hội đồng vận hành 3 subagents (hoặc chuyển vai tuần tự) tương ứng với 3 tệp Persona sẵn có:
1.  **The Data Auditor:** [the_data_auditor.md](file:///Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_data_auditor.md) (Kiểm toán Số liệu).
2.  **The Voice Architect:** [the_voice_architect.md](file:///Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_voice_architect.md) (Kiến trúc sư Giọng nói/TTS).
3.  **The Quality Czar:** [the_quality_czar.md](file:///Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_quality_czar.md) (Giám đốc Chất lượng).

---

## 3. Quy trình Thẩm định & Tối ưu hóa Song song

### Bước 1: Quét song song (Parallel Auditing)
3 Agent cùng đọc bản nháp của tệp `chapter_XX.md` và gắn cờ cảnh báo theo chuyên môn:
*   *Data Auditor* lập danh mục số liệu và gắn cờ cảnh báo (🔴/🟡) các claim thiếu nguồn, bịa đặt hoặc suy diễn vượt phạm vi.
*   *Voice Architect* phát hiện các câu dài > 150 ký tự, các đoạn văn > 4 câu, hoặc các cụm từ khó đọc, hụt hơi gây lỗi TTS.
*   *Quality Czar* tìm kiếm các từ ngữ tabloid bị cấm, từ cự tuyệt AI-isms và lỗi xưng hô không đồng bộ.

### Bước 2: Chấm điểm Chỉ số Chất lượng (Script Quality Metrics)
Hội đồng chấm điểm kịch bản chương (thang điểm 1-10) dựa trên 3 trục tối ưu:
1.  **Novelty Index (Độ tươi mới):** Lập luận bóc tách cơ chế vĩ mô ẩn sâu hay chỉ xào nấu tin tức bề nổi? (Yêu cầu ≥ 8/10).
2.  **Rhythmic Flow (Nhạc tính thoại):** Trộn lẫn câu ngắn/dài tốt không? Đọc lên có tự nhiên và giàu cảm xúc không? (Yêu cầu ≥ 9/10).
3.  **Anchoring Density (Mật độ bằng chứng):** 100% các luận điểm then chốt có phách dẫn nguồn rõ ràng không? (Yêu cầu 10/10).

### Bước 3: Giao thức Tranh biện Thuật ngữ & Nhịp thở (Term-Breath Conflict Resolution)
Đây là chốt chặn quan trọng nhất để giải quyết mâu thuẫn giữa *Nhạc tính* và *An toàn tài chính*:
*   **Tình huống:** Voice Architect muốn chia nhỏ câu dài hoặc thay thế thuật ngữ khó đọc bằng từ gần miệng để tối ưu TTS và nhịp thở.
*   **Ranh giới đỏ:** Nếu việc sửa đổi làm giảm cấp thuật ngữ vĩ mô hoặc bóp méo cơ chế nhân quả kinh tế (Ví dụ: biến *"Thâm dụng vốn lớn"* thành *"Đốt tiền/Lỗ nặng"*, biến *"Tăng trưởng chu kỳ"* thành *"Tăng trưởng thần kỳ"*):
    *   **Data Auditor phát lệnh VETO.**
    *   **Giải pháp bắt buộc:** Hai bên bắt buộc thảo luận để tìm ra phương án tối ưu: Giữ nguyên thuật ngữ vĩ mô chính xác, nhưng thực hiện ngắt câu cơ học bằng dấu chấm hoặc dấu chấm phẩy tại điểm nghỉ hơi tự nhiên để câu đơn dưới 150 ký tự.
    *   *Quality Czar* giám sát để câu viết lại sạch bóng AI-isms và không có biểu cảm cường điệu giả tạo.

---

## 4. Đầu ra Hợp nhất (episodes/[slug]/10_compliance_report.md)
Hội đồng ghi đè trực tiếp các đoạn văn tối ưu vào tệp kịch bản chính thức `chapter_XX.md` và xuất bản một báo cáo compliance duy nhất dưới định dạng sau:

```markdown
# Compliance & Quality Report — [Episode Slug] — Chapter [Số]

## 1. Chỉ số Chất lượng (Quality Metrics)
*   **Novelty Index:** [Điểm/10] — Nhận xét:
*   **Rhythmic Flow:** [Điểm/10] — Nhận xét:
*   **Anchoring Density:** [Điểm/10] — Nhận xét:

## 2. Nhật ký Tranh biện Thuật ngữ & Nhịp thở (Detailed Dialogue Resolution Logs)
> (Ghi lại chi tiết cuộc hội thoại giằng co giữa các chuyên gia khi chỉnh sửa câu thoại nhạy cảm)
*   **[Voice Architect]:** "Tôi cần tách câu gốc này làm đôi và thay cụm từ... cho đỡ hụt hơi."
*   **[Data Auditor]:** "VETO! Việc sửa cụm từ đó làm mất đi bản chất của cơ chế kế toán chéo. Đề xuất: Giữ nguyên từ đó nhưng đặt dấu chấm phẩy nghỉ hơi ở..."
*   **[Quality Czar]:** "Đồng ý với phương án dùng dấu chấm phẩy, tôi sẽ tinh chỉnh lại để từ nối không có cảm giác AI-ism."
*   *Câu gốc:* 
*   *Câu sửa đổi đồng thuận:* (Dưới 150 ký tự, giữ nguyên thuật ngữ chuyên ngành kinh tế học, ngắt câu cơ học)

## 3. Claim Ledger kiểm toán (Bởi Data Auditor)
| # | Tuyên bố trong kịch bản | Phân loại | Nguồn kiểm chứng / Neo tựa | Trạng thái |
|---|-------------------------|-----------|----------------------------|------------|
| 1 | | `verified_data` | | ✅ Duyệt |

## 4. Danh mục Anti-AI & Tabloid đã quét (Bởi Quality Czar)
- [x] Đã quét sạch các từ tabloid bị cấm ("đốt tiền", "cứu trợ", "ván cược").
- [x] Đã dọn dẹp các cụm từ sáo rỗng AI.
- [x] Đã đồng bộ hóa ngôi xưng trong toàn chương.

## 5. Kết luận & Chữ ký Duyệt (Verdict)
*   **Trạng thái kịch bản thoại:** APPROVED (Sẵn sàng sản xuất và thu âm)
*   **Chữ ký duyệt:**
    *   [x] The Data Auditor
    *   [x] The Voice Architect
    *   [x] The Quality Czar
```
