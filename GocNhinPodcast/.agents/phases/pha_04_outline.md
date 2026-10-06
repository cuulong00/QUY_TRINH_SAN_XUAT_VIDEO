# Thẻ Pha 4: Outline biện chứng

**Mục tiêu.** Dựng mạch kể từ chính đề, qua phản đề (Devil's Chapter), tới hợp đề. Mỗi chương có một chức năng rõ và ngân sách từ.

## Đọc, theo thứ tự
1. `00_hien_chuong.md`, `03_brief.md`, `00_bang_gia_thuyet.md`.
2. `.agents/workflows/build_outline.md` (5 trạm) và `.agents/skills/script_architect/SKILL.md` §1 mục 10, §2 "Pha 4".
3. `00_core/longform_blueprint.md` (nhịp dài, re-hook quanh 3:30, luật But/Therefore).
4. `00_core/narrative_craft_rubric.md` (Phiếu A: người khác chấm outline theo 10 chỉ tiêu, người dựng tự soi thêm).
5. Khuôn `02_templates/masterpiece_pipeline/07_outline_template.md`.
6. Persona: `the_dialectic_architect.md`, `the_critical_auditor.md`. Quy chuẩn Devil's Chapter và Steelman 3 nhịp: `.agents/reference/AGENTS_truoc_20261003.md` mục "Thể Chế Hóa Hội Đồng Phản Biện Đa Diện".

## Không cần đọc
Vault, skill viết chương, `00_core` về giọng.

## Cách làm
- **Hình dung cách kể trước khi dựng chương (Cách kể của tập):** Tự trả lời bằng lời của mình (3–6 câu trong `07_outline.md`): điều gì giữ chân khán giả nam 35–40 tới cuối; câu chuyện nên đi theo dạng nào (theo dấu một đồng tiền, giải một câu đố, đặt hai con đường cạnh nhau, đi ngược từ một hệ quả, theo một quyết định qua các bên... — định hướng tư duy, không có khuôn kể chung cho mọi tập, không biến thành bảng chọn máy móc; hạn chế tả cảnh không mang dữ kiện); vì sao dạng ấy hợp chủ đề này hơn các dạng khác; vật chứng nào trong nghiên cứu sẽ gánh câu chuyện. Phiếu A cấp bài sẽ chấm dàn ý theo đúng cách kể này.
- Viết cho mỗi chương một câu "người xem nghĩ X → gặp bằng chứng Y → nghĩ lại thành Z".
- Cắt thứ khán giả không cần (thủ tục, danh sách ngày, liệt kê rào đón); giữ cơ chế, cú lật, nghi ngờ của họ, cái giá.
- Không chép lại số liệu vào outline; trỏ mã M.
- Tự soi theo Phiếu A của `00_core/narrative_craft_rubric.md` trước khi nộp: mỗi chương phải có câu hỏi điều tra, vật chứng/nhân vật, xung đột/cơ chế, cú lật; không biến outline thành bản liệt kê số liệu hay mục lục video.

## Giới hạn
`07_outline.md` tối đa 3.000 từ; tổng ngân sách từ bằng số phút × 223.

## Cổng và dừng
Chạy `python3 scripts/kiem_pha.py <slug> --pha 4`. Phiếu A cấp bài (`00_core/narrative_craft_rubric.md` §4) trên dàn ý do người khác ngoài người dựng outline chấm và đạt mốc ĐẠT (không chỉ tiêu < 3, trung bình ≥ 4,0, I/IV/V ≥ 4) trước khi xin user duyệt; lưu vào `11_narrative_craft_scorecard.md`. Sau khi có outline, Claude đọc lại vault và `research_raw/` để tìm dữ kiện đỡ hoặc bác mà outline bỏ sót. User duyệt outline.
