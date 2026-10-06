# Thẻ Pha 7: Viết chương

**Mục tiêu.** Viết **một** chương (`episodes/<slug>/chapter_XX.md`) đúng chức năng mà brief giao, bằng giọng người am hiểu nói chuyện thật, dữ kiện đúng nguồn gốc. Viết xong thì dừng chờ duyệt rồi mới viết chương sau.

## Đọc, theo thứ tự (quy trình user chốt: hiểu tổng thể trước, rồi mới chắp bút)
**Bước A. Nhập vai chuyên gia: nạp DNA và skill**
1. Persona chính mà brief chương chỉ định (`.agents/personas/`), đọc trọn.
2. `.agents/skills/chapter_writer/SKILL.md`, đọc trọn (đặc biệt "Quy Tắc Vàng: Viết Câu Cho Tai", "Quy tắc đặc biệt theo vị trí", "CHƯƠNG KẾT" nếu là chương kết).
3. `00_core/voice_dna.md`, `00_core/stance_and_judgment.md`, và `00_core/narrative_craft_rubric.md` (Phiếu B: tự soi 10 chỉ tiêu).

**Bước B. Hiểu bức tranh toàn cảnh của cả tập**
4. `00_hien_chuong.md` (toàn bộ): đề bài, chỉ đạo user, điều đã loại, lăng kính, chế độ kết.
5. `01_global_vision_synthesis.md`: bản đồ hệ thống, các bên, các thị trường, giả thuyết.
6. `00_bang_gia_thuyet.md`: giả thuyết còn đứng, bằng chứng đỡ và bác.
7. `07_outline.md` (toàn bộ): mạch của cả tập, chương này đứng ở đâu, nhận gì từ chương trước, trao gì cho chương sau.

**Bước C. Tài liệu của chương này và chương trước**
8. `08_chapter_briefs.md`: brief của chương này và của chương ngay trước.
9. `00_so_du_kien.md`: các hàng M chương này dùng. Với mỗi con số, **mở vị trí nguồn gốc**, đọc đúng câu gốc chứa con số. Thứ tự tin cậy: văn bản gốc trong `research_raw/`, rồi `research_vault/` (có thể trích sai), rồi sổ. Nguồn gốc nói khác sổ hay vault thì viết theo nguồn gốc và báo Claude. Không có nguồn thì không viết con số đó.
10. Toàn bộ các chương đã viết của tập (`chapter_01.md` đến chương trước), đọc liền một mạch để bắt giọng và nhịp. Khi viết lại một chương, không mở bản cũ của chính chương đó.

Nếu file planning (vision, outline) dài quá mức đọc nổi, đó là lỗi của pha trước: báo Claude để rút gọn, **không được bỏ qua** bức tranh toàn cảnh.

## Không cần đọc khi viết
Chương của tập khác (không dùng làm khuôn giọng), bảng điều phối cũ, `00_core/anti_ai_isms.md` đầy đủ (cổng máy kiểm từ cấm; chỉ tra khi cần).

- Hai lượt viết riêng biệt (`chapter_writer/SKILL.md` Bước 1): Chặng 1 (khung xương cơ chế) in ra chat; Chặng 2 (bảng nhịp chương, rồi mới viết văn) in ra chat. Không viết thẳng từ bảng số liệu của brief.
- Trước khi viết câu đầu tiên, nói được bằng một câu: chương này nằm ở đâu trong mạch của cả tập, và nó đổi điều gì trong đầu người nghe (họ đang nghĩ X, gặp dữ kiện Y, nghĩ lại thành Z).
- Viết cả chương trong một mạch, từ ý của chương, không viết từng đoạn theo dữ kiện của đoạn đó. Mỗi đoạn mở ra từ hệ quả hoặc câu hỏi của đoạn trước. Dữ kiện xuất hiện khi mạch kể cần đến nó.
- Dữ kiện nào đắt nhất của chương? Đặt nó ở đâu để nó tự nói?
- Mối nối: khi dựng phim, giữa hai chương có khoảng 4 giây lặng. Câu cuối chương trước phải để lại một câu hỏi hoặc một sức căng cụ thể. Câu **đầu tiên** của chương này phải nhặt đúng sợi chỉ đó, không mở sang chuyện mới và không dùng câu dẫn ("Giờ quay lại…", "Ghép tất cả lại…", "phải kể lại…"). Câu cuối chương này cũng phải gài sẵn sợi chỉ cho chương sau. CTA ở Chương 2 đặt trước câu chuyển, không đặt sau.

## Tự kiểm trước khi nộp
1. Làm hai phép thử của "Viết Câu Cho Tai" (đọc to; nghe riêng từng đoạn) cho cả chương. Viết lại mọi chỗ vấp, phải nghe lại, hay phải nhớ chương khác mới hiểu. **Sửa dù chỉ một đoạn cũng phải mở lại mục đó trước khi sửa và làm lại hai phép thử sau khi sửa.**
2. Tự soi bằng Phiếu B (`00_core/narrative_craft_rubric.md`) và in ra chat để tự sửa các câu yếu trước khi nộp; việc tự soi không phải điều kiện qua cổng và điểm tự soi không tính vào điểm K; lưu kết quả tự soi vào Mục 1 của `11_narrative_craft_scorecard.md` để theo dõi; điều kiện qua cổng Pha 7 là cổng máy `kiem_pha.py` đạt.
3. Mỗi con số đều có hàng M và đã mở nguồn gốc; câu suy luận viết đúng tầng giọng của nhãn.
4. Không chương nào quá 1.050 từ; CTA chỉ ở cuối Chương 2 (hiến pháp §4).
5. Chạy `python3 scripts/kiem_pha.py <slug> --pha 7`, sửa tới khi ĐẠT.

## Đầu ra và cập nhật
- `chapter_XX.md`: tiêu đề và lời thoại sạch; không ghi chú quy trình, không tả cảnh, không nhãn khung.
- `11_narrative_craft_scorecard.md`: cập nhật bảng tự soi Phiếu B của chương vào Mục 1.
- Thêm hàng mới vào `00_so_du_kien.md` nếu dùng mắt xích mới (kèm vị trí nguồn); cập nhật `09_narrative_state_tracker.md`.

## Dừng
Báo Claude qua phiếu: nguyên văn chương, bảng tự soi Phiếu B, đầu ra cổng `kiem_pha.py`, danh sách con số kèm vị trí nguồn đã mở. **Không viết chương tiếp theo khi chưa được duyệt.**
