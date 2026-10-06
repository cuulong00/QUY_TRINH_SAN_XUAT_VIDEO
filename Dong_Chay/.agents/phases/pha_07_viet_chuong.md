# Thẻ Pha 7: Viết chương (Tam đoạn luận 3 nhịp)

**Mục tiêu.** Viết **một** chương (`episodes/<slug>/chapter_XX.md`) đúng chức năng mà brief 20 trường giao, theo cấu trúc Tam đoạn luận 3 nhịp (Chính đề -> Phản đề -> Hợp đề cục bộ), giọng điềm tĩnh, đĩnh đạc, sâu sắc có nghề của Dòng Chảy; dữ kiện đúng nguồn gốc. Viết xong thì dừng chờ duyệt rồi mới viết chương sau.

## Đọc, theo thứ tự (quy trình user chốt: hiểu tổng thể trước, rồi mới chắp bút)
**Bước A. Nhập vai chuyên gia: nạp DNA và skill**
1. Persona chính mà brief chương chỉ định (`.agents/personas/the_narrative_director.md`, `.agents/personas/the_voice_architect.md`), đọc trọn.
2. `.agents/skills/chapter_writer/SKILL.md`, đọc trọn (đặc biệt quy tắc câu thoại viết cho tai nghe, nhịp điệu tự sự, hạn chế tả cảnh theo định nghĩa).
3. `00_core/voice_dna.md`, `00_core/stance_and_judgment.md`, và `00_core/narrative_craft_rubric.md` (Phiếu B: tự soi 6 chỉ tiêu cấp chương, không ghi điểm).

**Bước B. Hiểu bức tranh toàn cảnh của cả tập**
4. `episodes/<slug>/01_global_vision_synthesis.md`: bản đồ hệ thống, các bên, các thị trường, động lực xung đột.
5. `episodes/<slug>/07_outline.md` (toàn bộ): mạch của cả tập, chức năng giải phẫu của chương, nhận gì từ chương trước, trao gì cho chương sau.

**Bước C. Tài liệu của chương này và chương trước**
6. `episodes/<slug>/08_chapter_briefs.md`: brief 20 trường của chương này và của chương ngay trước (đặc biệt 4 trường nhịp chuyện và Trường 10 Pointer chứng cứ gốc).
7. **Vị trí nguồn gốc của dữ kiện:** Với mỗi con số hay sự kiện, **mở vị trí nguồn gốc** theo tọa độ chứng cứ gốc (Pointer trong brief) hoặc `research_vault/`. **Thứ tự tin cậy nguồn:** Văn bản gốc trong `research_raw/` -> `research_vault/` (có thể trích sai) -> sổ claim `episodes/<slug>/10_compliance_report.md` (nếu có). Nguồn gốc nói khác sổ hay vault thì viết theo nguồn gốc và báo Claude. Không có nguồn gốc mở được thì không viết con số hoặc chi tiết đó.
8. Toàn bộ các chương đã viết của tập (từ Chương 1 đến chương trước), đọc liền một mạch để bắt giọng và nhịp. **Khi viết lại một chương, tuyệt đối không mở bản cũ của chính chương đó.**

Nếu file planning (vision, outline) dài quá mức đọc nổi, đó là lỗi của pha trước: báo Claude để rút gọn, **không được bỏ qua** bức tranh toàn cảnh.

## Không cần đọc khi viết
Chương của tập khác (không dùng làm khuôn giọng); bảng điều phối cũ; `00_core/anti_ai_isms.md` đầy đủ (cổng máy kiểm từ cấm; chỉ tra khi cần); cơ chế log lỗi runtime cũ (đã bãi bỏ, sửa trực tiếp).

## Chuyên gia (Persona)
- `.agents/personas/the_narrative_director.md`: Đạo diễn Tự sự & Nhịp chuyện.
- `.agents/personas/the_voice_architect.md`: Kiến trúc sư Thoại Thính giác.

## Luật riêng (trỏ bản gốc)
- Hai lượt viết riêng biệt (`.agents/rules/chapter-writing.md`): Chặng 1 (khung xương cơ chế Tam đoạn luận) in ra chat; Chặng 2 (bảng nhịp chương, rồi mới viết văn) in ra chat. Không viết thẳng từ bảng số liệu của brief.
- Trước khi viết câu đầu tiên, nói được bằng một câu: chương này nằm ở đâu trong mạch của cả tập, và nó đổi điều gì trong đầu người nghe (họ đang nghĩ X, gặp dữ kiện Y, nghĩ lại thành Z).
- Viết cả chương trong một mạch, từ ý của chương, không viết từng đoạn theo dữ kiện của đoạn đó. Mỗi đoạn mở ra từ hệ quả hoặc câu hỏi của đoạn trước. Dữ kiện xuất hiện khi mạch kể cần đến nó.
- Dữ kiện nào đắt nhất của chương? Đặt nó ở đâu để nó tự nói?
- Cụ thể bằng dữ kiện, hạn chế tả cảnh theo định nghĩa (`00_core/narrative_craft_rubric.md` §2): vật chứng có nguồn (văn bản, ngày tháng, công trình, con số đối nghịch) được khuyến khích, không viết câu dựng không khí hay thời tiết rỗng.
- Mối nối: khi dựng phim, giữa hai chương có khoảng 4 giây lặng. Câu cuối chương trước phải để lại một câu hỏi hoặc một sức căng cụ thể. Câu **đầu tiên** của chương này phải nhặt đúng sợi chỉ đó, không mở sang chuyện mới và không dùng câu dẫn sáo mòn ("Như đã nói ở phần trước...", "Ở chương trước ta thấy..."). Câu cuối chương này cũng phải gài sẵn sợi chỉ cho chương sau.
- CTA đăng ký kênh đúng 1 lần duy nhất ở cuối Chương 2, trước câu chuyển tiếp sang Chương 3.

## Tự kiểm trước khi nộp
1. Làm hai phép thử của "Viết Câu Cho Tai" (đọc to; nghe riêng từng đoạn) cho cả chương. Viết lại mọi chỗ vấp, phải nghe lại, hay phải nhớ chương khác mới hiểu. Sửa dù chỉ một đoạn cũng phải mở lại mục đó trước khi sửa và làm lại hai phép thử sau khi sửa.
2. Tự soi bằng Phiếu B (`00_core/narrative_craft_rubric.md`) và in ra chat để tự sửa các câu yếu trước khi nộp; việc tự soi không ghi điểm, không phải điều kiện qua cổng; lưu bảng tự soi câu yếu vào Mục 1 của `episodes/<slug>/11_narrative_craft_scorecard.md` để theo dõi; điều kiện qua cổng Pha 7 là cổng máy `scripts/verify_phase_gate.py` đạt.
3. Mỗi con số đều có mã `DATA-XX` và đã mở nguồn gốc; câu suy luận viết đúng tầng giọng của nhãn (`verified_data`, `market_analysis`, `opinion_commentary`).
4. Không chương nào quá 1.050 từ (vượt ngưỡng kích hoạt phân hạch chương); 100% câu thoại dưới 150 ký tự (chuẩn 100-120 ký tự); tuyệt đối cấm dấu gạch ngang dài em-dash.
5. Chạy `python3 scripts/verify_phase_gate.py <slug> --pha 7`, sửa tới khi ĐẠT.

## Đầu ra và cập nhật
- `episodes/<slug>/chapter_XX.md`: tiêu đề và lời thoại sạch; không ghi chú quy trình, không tả cảnh, không nhãn khung sườn.
- `episodes/<slug>/11_narrative_craft_scorecard.md`: cập nhật bảng tự soi câu yếu Phiếu B của chương vào Mục 1.
- Cập nhật `episodes/<slug>/09_narrative_state_tracker.md`.

## Dừng
Báo Claude qua phiếu: nguyên văn chương, bảng tự soi câu yếu Phiếu B, đầu ra cổng `scripts/verify_phase_gate.py`, danh sách con số kèm vị trí nguồn đã mở. **Không viết chương tiếp theo khi chưa được User duyệt.**
