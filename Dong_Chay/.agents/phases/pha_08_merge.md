# Thẻ Pha 8: Gộp voiceover hoàn chỉnh

**Mục tiêu.** Gộp toàn bộ các chương đã duyệt và Master Hook thành `episodes/<slug>/voiceover.md` liền mạch: loại bỏ triệt để các ý, số liệu, case study trùng lặp; bảo tồn các cú lật đắt giá; giữ đúng chế độ kết (A/B); không nhãn khung sườn template.

## Đọc, theo thứ tự
1. Toàn bộ các file `episodes/<slug>/chapter_XX.md` đã được duyệt; Master Hook đã được chọn trong `episodes/<slug>/04_hook_pack.md`.
2. `.agents/rules/final-merge.md` (luật gộp) và `.agents/workflows/merge_voiceover.md`.
3. Dữ liệu nguồn: kiểm tra mọi con số có mã `DATA-XX`, giữ đúng tầng giọng theo taxonomy (`verified_data`, `market_analysis`, `opinion_commentary`).
4. `00_core/stance_and_judgment.md` (chế độ kết luận A/B).
5. Persona: `.agents/personas/the_quality_czar.md`, `.agents/personas/the_voice_architect.md`.

## Không cần đọc
Brief, outline, toàn bộ kho vault thô (trừ trường hợp kiểm tra lại một con số bị nghi vấn).

## Chuyên gia (Persona)
- `.agents/personas/the_quality_czar.md`: Tổng Giám sát Chất lượng.
- `.agents/personas/the_voice_architect.md`: Kiến trúc sư Thoại Thính giác.

## Cách làm & Luật riêng (trỏ bản gốc)
- Đọc to toàn bài một lượt. Chỗ nào nhắc lại điều đã nói mà không mở thêm lớp phân tích mới thì dứt khoát cắt bỏ.
- Kiểm tra từng mối nối với khoảng lặng 4 giây giữa hai chương: câu cuối chương trước gài câu hỏi gì, câu đầu chương sau có nhặt đúng sợi chỉ đó không (thẻ Pha 7).
- Rà soát cấp bài sau merge theo **Phiếu A** của `00_core/narrative_craft_rubric.md`: kiểm tra toàn bộ tác phẩm sau gộp (câu hỏi kịch tính trung tâm I, cao trào IV-b, gieo/gặt hạt giống, và tính liền mạch của các cú lật); việc chấm lại Phiếu A sau merge do người khác ngoài người merge thực hiện và ghi nhận vào `episodes/<slug>/11_narrative_craft_scorecard.md`.
- Dòng lưu ý bắt buộc xuất hiện đúng nguyên văn: "Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng" (hiến pháp §3.4).
- CTA đăng ký kênh đúng 1 lần duy nhất, ở cuối Chương 2, trước khi bước sang Chương 3.
- Giữ đúng chế độ kết đã chọn (`00_core/stance_and_judgment.md`): Chế độ A giữ lập trường chính vững chãi; Chế độ B giữ đủ khung kết mở đa chiều; khi gộp không làm mềm thành câu lửng lơ và không cộng dồn các cụm rào đón.
- Kiểm kê ngân sách: Đảm bảo độ lệch tổng số từ thực tế so với mục tiêu trong `episodes/<slug>/07_outline.md` nằm trong biên độ dung sai cho phép (+- 10%).

## Đầu ra
- `episodes/<slug>/voiceover.md`: văn bản thoại sạch hoàn chỉnh 100%, không nhãn khung sườn, không tả cảnh, không metadata vận hành.
- Thống kê tổng số từ thực tế và thời lượng ước tính (tốc độ đọc chuẩn 223-235 từ/phút).

## Cổng và dừng
Chạy `python3 scripts/verify_phase_gate.py <slug> --pha 8`; Phiếu A cấp bài sau merge do người khác ngoài người merge chấm đạt chuẩn. Claude đọc lại vault và `research_raw/` tìm dữ kiện bị bỏ sót. User duyệt voiceover trước khi chuyển sang QA kiểm định.
