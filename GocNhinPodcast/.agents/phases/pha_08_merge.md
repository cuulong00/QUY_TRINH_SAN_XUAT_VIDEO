# Thẻ Pha 8: Gộp voiceover

**Mục tiêu.** Gộp các chương đã duyệt thành `voiceover.md` liền mạch: bỏ ý, số, ví dụ trùng; giữ các cú lật đắt; giữ đúng chế độ kết.

## Đọc, theo thứ tự
1. Toàn bộ `chapter_XX.md` đã duyệt; hook đã chọn trong `04_hook_pack.md`.
2. `.agents/rules/final-merge.md` (luật gộp) và `.agents/workflows/merge_voiceover.md`.
3. `00_so_du_kien.md`: đối chiếu mọi con số có mã M, đúng tầng giọng.
4. `00_core/stance_and_judgment.md` §1, §10.
5. Persona: `the_quality_czar.md`.

## Không cần đọc
Brief, outline, vault (trừ khi kiểm một con số).

## Cách làm
- Đọc to toàn bài một lượt. Chỗ nào nhắc lại điều đã nói mà không thêm lớp mới thì cắt.
- Kiểm từng mối nối với khoảng lặng 4 giây giữa hai chương: câu cuối chương trước gài gì, câu đầu chương sau có nhặt đúng thứ đó không (thẻ Pha 7, mục "Cách nghĩ trước khi viết").
- Rà soát cấp bài sau merge theo **Phiếu A** của `00_core/narrative_craft_rubric.md`: kiểm tra toàn bộ tác phẩm sau gộp (câu hỏi kịch tính trung tâm I, cao trào IV-b, gieo/gặt hạt, và tính liền mạch của các cú lật); việc chấm lại Phiếu A sau merge do người khác ngoài người merge thực hiện và ghi nhận vào `11_narrative_craft_scorecard.md`.
- Dòng lưu ý bắt buộc đúng nguyên văn (hiến pháp §3.4); CTA một lần, cuối Chương 2.

## Đầu ra
`voiceover.md`; số từ và số phút ước tính (223 từ/phút).

## Cổng và dừng
Chạy `python3 scripts/kiem_pha.py <slug> --pha 8`; Phiếu A cấp bài sau merge do người khác ngoài người merge chấm đạt chuẩn. Claude đọc lại vault và `research_raw/` tìm dữ kiện bị bỏ sót. User duyệt trước khi sang QA.
