# Thẻ Pha 9–11: Retention audit, QA biên tập, tuân thủ & chấm mù Narrative Craft

**Mục tiêu.** Người chấm khác người viết soi toàn bộ voiceover: giữ chân ở đâu rơi (Pha 9), dữ kiện có đúng nguồn gốc và taxonomy không, có chạm ranh giới tài chính hay an toàn thương hiệu không (Pha 10), chấm mù chất chuyện theo khung 10 chỉ tiêu hai cấp để xác lập Điểm Trụ cột K của kịch bản (Pha 11).

## Đọc, theo thứ tự
1. `episodes/<slug>/voiceover.md`, `episodes/<slug>/01_global_vision_synthesis.md`, `episodes/<slug>/03_brief.md`, `episodes/<slug>/07_outline.md`.
2. Pha 9 (Giữ chân): `.agents/skills/retention_bridge_audit/SKILL.md`, `00_core/retention_gate_checklist.md`.
3. Pha 10–11 (Tuân thủ & Chất lượng): `.agents/skills/compliance_council/SKILL.md`, `00_core/financial_boundaries.md`, `00_core/brand_safety_guidelines.md`, `00_core/quality_rubric.md`, `00_core/narrative_craft_rubric.md`.
4. Persona: `.agents/personas/the_critical_auditor.md`, `.agents/personas/the_compliance_editor.md`, `.agents/personas/the_policy_analyst.md`.

## Không cần đọc
Prompt hình ảnh, tài nguyên video, các bản nháp chương cũ đã bỏ.

## Chuyên gia (Persona)
- `.agents/personas/the_critical_auditor.md`: Chủ tịch Hội đồng Kiểm định, Phản biện Tri-Adversarial Red Team.
- `.agents/personas/the_compliance_editor.md`: Biên tập viên Tuân thủ & An toàn Thương hiệu.
- `.agents/personas/the_policy_analyst.md`: Chuyên gia Phân tích Thể chế & Kinh tế vĩ mô.

## Cách làm & 6 Khóa thẩm định bắt buộc
- **Bước 0 (Cổng máy):** Chạy `python3 scripts/verify_phase_gate.py <slug> --pha 8`, dán đầu ra vào báo cáo.
- **Khóa 1 (Dữ kiện & Bằng chứng):** Mở vị trí nguồn gốc của mọi con số quan trọng, kiểm tra mã `DATA-XX`, đối chiếu câu gốc trong `research_vault/` hoặc `research_raw/`. Đảm bảo không có số vô căn cứ, không suy diễn vượt nhãn.
- **Khóa 2 (Ranh giới Tài chính & An toàn Thương hiệu):** Đối soát theo `00_core/financial_boundaries.md` và `00_core/brand_safety_guidelines.md` (không tư vấn đầu tư, không phán xét đạo đức, không dùng từ ngữ kích động).
- **Khóa 3 (Giữ chân & Nhịp điệu Thính giác):** Thực hiện kiểm toán theo `00_core/retention_gate_checklist.md`. Đọc to các đoạn nghi chùng nhịp; trả lại chỗ sửa cụ thể kèm câu đề xuất.
- **Khóa 4 (Thiên lệch & Devil's Chapter):** Kiểm tra tính khách quan của lập luận; thẩm định chương phản đề Devil's Chapter có đủ sức nặng Steelman không.
- **Khóa 5 (Kỷ luật Ngôn ngữ):** 100% câu dưới 150 ký tự; tuyệt đối không có dấu gạch ngang dài em-dash; khử sạch từ cấm AI (`00_core/anti_ai_isms.md`).
- **Khóa 6 (Chất Chuyện Narrative Craft & Điểm Trụ cột K):**
  * Critical Auditor chấm mù độc lập Phiếu A (cấp bài) và Phiếu B (từng chương) theo `00_core/narrative_craft_rubric.md`, tuyệt đối không xem bản tự soi trước khi nộp.
  * Mọi điểm 4-5 và 1-2 bắt buộc trích câu dẫn chứng cụ thể; không dùng phép đếm máy móc để cho điểm.
  * Sau khi chấm xong, đối chiếu với danh sách chỗ yếu của tác giả; chỗ nào tác giả thấy yếu mà người chấm mù cho 4-5 hoặc ngược lại thì hai bên đọc lại đúng đoạn đó và ghi kết luận.
  * Điểm chấm mù chính thức là căn cứ tính Điểm Trụ cột K (tối đa 20 điểm) của `00_core/quality_rubric.md`.

## Công cụ kiểm chứng độc lập (Fact-checking với Google AI)
Chạy tự động đối chiếu qua Google Search AI Mode (dùng ở Pha 10, Editorial QA):
```bash
python3 scripts/google_ai_audit.py episodes/<slug> --all
# Hoặc cho 1 chương cụ thể:
python3 scripts/google_ai_audit.py episodes/<slug> --chapter <số_chương>
```
- Công cụ xuất kết quả phản biện ra `episodes/<slug>/google_ai_audit_results.md`. Sử dụng kết quả này tại **Pha 10 (Editorial QA)** để nới lỏng hoặc thắt chặt các nhận định kinh tế, xã hội trước khi voiceover.
- **Quy tắc thao tác trên Google AI Mode:** Bắt buộc sử dụng tính năng **"Thêm tệp" (nút +)** để nạp file .md từng chương, không dán văn bản dài trực tiếp vào ô chat. Việc import file giúp Gemini tiếp nhận trọn vẹn ngữ cảnh tài liệu, không bị cắt bớt nội dung và trả về báo cáo phân tích chuyên sâu đầy đủ nhất.

## Đầu ra
- `episodes/<slug>/retention_bridge_audit.md` (Pha 9).
- `episodes/<slug>/10_compliance_report.md` (Bảng claim đối soát, bảng điểm 11 trụ cột gồm Trụ cột K).
- `episodes/<slug>/11_narrative_craft_scorecard.md` (Phiên bản audit chính thức của Critical Auditor).
- `episodes/<slug>/google_ai_audit_results.md` (Kết quả phản biện độc lập của Google AI).

## Cổng và dừng
Đạt khi tổng điểm QA >= 8,5/10, không trụ cột nào < 7,5/10 (hiến pháp §4) và Trụ cột K đạt mốc ĐẠT (không chỉ tiêu nào < 3, trung bình >= 4,0, IV-a Cú lật và V Vật chứng không cùng <= 2); lưu `episodes/<slug>/11_narrative_craft_scorecard.md`. User duyệt trước khi chuyển sang giai đoạn sản xuất.
