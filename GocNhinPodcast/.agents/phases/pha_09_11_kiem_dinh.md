# Thẻ Pha 9–11: Retention audit, QA biên tập và tuân thủ

**Mục tiêu.** Người chấm khác người viết soi voiceover: giữ chân ở đâu rơi, dữ kiện có đúng nguồn và đúng nhãn không, có chạm ranh giới tài chính, pháp lý không, lập luận có thiên lệch không.

## Đọc, theo thứ tự
1. `voiceover.md`, `00_so_du_kien.md`, `00_hien_chuong.md`, `03_brief.md`.
2. Pha 9: `.agents/skills/retention_bridge_audit/SKILL.md`, `00_core/retention_gate_checklist.md`.
3. Pha 10–11: `.agents/skills/compliance_council/SKILL.md`, `00_core/financial_boundaries.md`, `00_core/quality_rubric.md`, `00_core/narrative_craft_rubric.md`.
4. Đối chiếu ngoài: `.agents/workflows/google_ai_audit.md` (`scripts/google_ai_audit.py`, nạp file chương qua nút "Thêm tệp").
5. Persona: `the_critical_auditor.md`, `the_compliance_editor.md`, `the_policy_analyst.md`.

## Cách làm
- Bước 0: chạy `python3 scripts/kiem_pha.py <slug> --pha 8`, dán đầu ra vào báo cáo.
- Với mỗi con số quan trọng: mở vị trí nguồn gốc, đối chiếu câu.
- Chấm mù Khóa 6 Narrative Craft: chấm độc lập Phiếu A (cấp bài) và Phiếu B (từng chương) theo `00_core/narrative_craft_rubric.md`, không xem bản tự soi trước khi nộp; sau khi chấm xong đối chiếu danh sách chỗ yếu của tác giả, chỗ nào người viết thấy yếu mà chấm mù cho 4-5 hoặc ngược lại thì hai bên đọc lại đúng đoạn đó và ghi kết luận; quy đổi ra Điểm Trụ cột K (tối đa 20đ).
- Đọc to những đoạn bị chấm thấp; trả lại chỗ sửa cụ thể, kèm câu đề xuất.

## Đầu ra
`retention_bridge_audit.md`, `10_compliance_report.md` (bảng claim trích từ sổ, bảng điểm 11 trụ cột gồm Trụ cột K), `11_narrative_craft_scorecard.md` (phiên bản audit cuối cùng).

## Cổng và dừng
Đạt khi tổng ≥ 8,5, không trụ cột nào < 7,5 (hiến pháp §4) và K đạt mốc, chấm mù theo `compliance_council` Khóa 6; lưu `11_narrative_craft_scorecard.md`. User duyệt.
