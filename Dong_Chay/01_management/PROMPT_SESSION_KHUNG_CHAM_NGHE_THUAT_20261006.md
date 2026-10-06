# Prompt mở phiên Claude mới: sửa DNA hai kênh để kịch bản kể chuyện, không đọc báo cáo

Dán toàn bộ nội dung dưới đây vào phiên mới. Thư mục làm việc: `/Users/pro16/Documents/VideoProject/Dong_Chay`.

---

Bạn là Claude, tổng điều phối hai kênh YouTube tài liệu kinh tế chính trị **Dòng Chảy** (`/Users/pro16/Documents/VideoProject/Dong_Chay`) và **GocNhinPodcast** (`/Users/pro16/Documents/VideoProject/GocNhinPodcast`). Hai kênh dùng chung một kiến trúc quy trình 16 pha (DNA nằm trong `.agents/`, `00_core/`, `02_templates/` của mỗi kênh). Phiên này chỉ sửa DNA, không viết tập mới, không sửa tập đã đăng.

## Bối cảnh: chuyện gì đã xảy ra
Ngày 05–06/10/2026, tập `gdp-9-thang-2026-con-so-10-tu-dau` của Dòng Chảy được viết đúng mọi luật dữ liệu (số khớp sổ, câu dưới 150 ký tự, không từ cấm, phản biện steelman) nhưng user kết luận nó **đọc như báo cáo, không phải kể chuyện**. Một phiên Claude trước đã lần gốc rễ và kết luận: lỗi nằm ở thiết kế quy trình, không phải ở nguyên liệu đầu vào. Cụ thể:
1. Outline lấy **điểm dữ liệu** làm đơn vị dựng chương (quota mã DATA-XX, công thức độ dài `D × 35 từ`), nên chương được lắp thành chuỗi "số, giải thích, số".
2. Định nghĩa "viết hay" trong bộ ví dụ chỉ là "câu số có diễn giải", không ai dạy dẫn người nghe đi tìm hay dàn dựng cú lật.
3. Kể chuyện chỉ là lời khuyên, dữ liệu là cổng có đo; người viết tối ưu theo cái được đo.
4. Các lệnh cứng "làm dày bằng số liệu", "lộ trình 3 trạm", "neo nguồn bằng câu dẫn chuẩn" đẩy về lối báo cáo.
5. Brief chương 16 trường toàn hàng dữ liệu, persona chủ đạo định nghĩa kịch bản hay là "tấm bản đồ sắc lạnh", chặng chuyển thể gộp cùng lượt với chặng cơ chế.

Phiên trước đã sửa một phần ở Dòng Chảy (ghi ở `Dong_Chay/.agents/CHANGELOG.md` mục `2026-10-06 · KE-CHUYEN`), rồi thử một "lượt đọc như người nghe" với ba kết luận. User bác: chấm nghệ thuật phải tách thành từng chỉ tiêu như hội đồng kịch bản chuyên nghiệp, và **không chỉ tiêu nào được chấm bằng đếm** (một công cụ đếm số đã bị gỡ vào `/Users/pro16/Documents/VideoProject/.agents/tools/viet/_archive/`, không được hồi sinh). User cũng bác lập luận "đầu vào thiếu cảnh": biến số liệu khô thành chuyện là việc của DNA và người viết.

## Việc của bạn
Thực thi trọn kế hoạch ở **`Dong_Chay/01_management/KE_HOACH_KHUNG_CHAM_NGHE_THUAT_20261006.md`** (9 mục), gồm:
- Mục 1–2: tạo `00_core/narrative_craft_rubric.md` (10 chỉ tiêu, hai cấp bài/chương, hai phiếu mẫu, bảng đối chiếu, mốc ĐẠT, ngân hàng đoạn mẫu); nối vào `quality_rubric.md` (trụ cột K), `chapter_writer`, `compliance_council`, `build_outline`, rules, examples, persona, workflows, khuôn phiếu `11_narrative_craft_scorecard`.
- Mục 8: sửa phần viết còn sót: khuôn brief chương thêm 4 trường (câu hỏi điều tra, vật chứng, cú lật, chủ thể và động cơ), tách lượt chuyển thể, sửa persona (`the_macro_strategist.md` dòng 93, `the_narrative_director.md` Mục 5, rà các persona chủ đạo khác).
- Mục 3: sau khi Dòng Chảy qua test, chuyển theo nghĩa sang GocNhinPodcast **cả hai đợt** (KE-CHUYEN sáng 06/10 và NARRATIVE-CRAFT), vì GocNhinPodcast chưa nhận đợt nào.
- Mục 4: chấm thật tập GDP bằng khung mới, lưu `episodes/gdp-9-thang-2026-con-so-10-tu-dau/11_narrative_craft_scorecard.md`.
- Mục 6: tự chạy 9 test nghiệm thu, báo kết quả từng test.

## Đọc trước khi làm (theo thứ tự, không bỏ)
1. `Dong_Chay/01_management/KE_HOACH_KHUNG_CHAM_NGHE_THUAT_20261006.md` (kế hoạch, kể cả mục 8).
2. `Dong_Chay/01_management/DE_XUAT_KHUNG_CHAM_NGHE_THUAT_KICH_BAN_20261006.md` (10 chỉ tiêu, mốc 1/3/5, nguồn tham chiếu, chấm thử GDP).
3. `Dong_Chay/.agents/CHANGELOG.md` mục KE-CHUYEN (đã sửa gì, file nào, vì sao).
4. `Dong_Chay/00_core/quality_rubric.md`, `00_core/stance_and_judgment.md`, `00_core/anti_ai_isms.md`.
5. `Dong_Chay/.agents/skills/chapter_writer/SKILL.md` (đặc biệt Chặng 1, Chặng 2, Bước 3b, mục "Viết Câu Cho Tai"), `PRE_FLIGHT_GATE.md`, `.agents/skills/compliance_council/SKILL.md`, `.agents/skills/script_architect/SKILL.md`, `.agents/workflows/build_outline.md`, `02_templates/masterpiece_pipeline/08_chapter_briefs_template.md` và `07_outline_template.md`, `.agents/examples/chapter_writer_examples.md`, `.agents/personas/the_narrative_director.md`, `the_macro_strategist.md`, `the_critical_auditor.md`.
6. Tập GDP để lấy mẫu: `episodes/gdp-9-thang-2026-con-so-10-tu-dau/chapter_01.md` đến `chapter_06.md` (bản phát hành), `_thu_dna_ke_chuyen/chapter_03.md` (bản viết lại theo DNA mới, cùng dữ kiện), `08_chapter_briefs.md`, `07_outline.md`.
7. Bộ nhớ của Claude: `/Users/pro16/.claude/projects/-Users-pro16-Documents-VideoProject/memory/prose-judged-by-llm-not-counts.md`, `channels-mirror-process-fixes.md`, `port-architecture-not-episodes.md`, `gocnhinpodcast-dna-single-source.md`, `root-cause-not-speed.md`.

## Quyết định của user (đã chốt)
- Quy trình chấm: đọc trọn không ghi chép → chấm cấp bài (câu hỏi trung tâm, mức cược, gieo và gặt, cao trào, kết) → chấm cấp chương (cú lật, cảnh so với tóm tắt, chủ thể và xung đột, nhịp, câu cho tai, cột "đẩy câu hỏi đi bao xa") → đối chiếu hai cấp → kết luận và lệnh sửa chỉ đích danh chương, chỉ tiêu, câu lỗi. Hai người chấm, Critical Auditor chấm mù. Chấm cấp bài lần đầu ngay sau dàn ý.
- Không chỉ tiêu nào chấm bằng đếm; mọi điểm 4–5 và 1–2 phải trích câu.
- Mốc ĐẠT: không chỉ tiêu nào dưới 3, trung bình ≥ 4,0, ba chỉ tiêu câu hỏi, cú lật, cảnh ≥ 4.

## Điểm user CHƯA chốt (hỏi user trước khi làm phần liên quan, không tự quyết)
1. Đoạn mẫu 5 điểm cho các chỉ tiêu mức cược, giọng, nhịp, câu cho tai, kết: user chỉ tập, hay cho phép dùng mô tả kỹ thuật thay đoạn. Trong khi chờ, ghi `[CHỜ USER CHỌN MẪU]`.
2. Trọng số 20 điểm cho trụ cột K và cách lấy từ các trụ cột khác (đề xuất ở kế hoạch 2.2).
3. Có bắt buộc `11_narrative_craft_scorecard.md` cho mọi tập mới không.
4. Có làm mục 8.4 (Pha 2 thu thêm "kho vật chứng") không.
Hỏi cả bốn trong một tin, rồi làm các phần không phụ thuộc trong lúc chờ.

## Ràng buộc kỹ thuật
- Sao lưu mỗi file trước khi sửa vào `/Users/pro16/VideoProject_backup/khung_cham_nghe_thuat_20261006/<kênh>/<đường dẫn tương đối>`.
- Sửa bằng Edit/Write, không bằng sed cho file nhiều dòng. Không sửa `01_management/episode_registry.csv` bằng Bash (Stop hook chặn).
- DNA chỉ nằm trong `.agents/`, `00_core/`, `02_templates/`; `.claude/` chỉ chứa cấu hình, không tạo skill hay rule ở đó.
- GocNhinPodcast: chuyển theo nghĩa, giữ phần riêng kênh (đề tài Loại A đời sống, persona riêng, tên file riêng); chỉ đọc file framework của kênh kia, không đọc hay chép tập của kênh kia.
- Không chép nguyên văn kịch bản của kênh tham chiếu (Max Fisher, Johnny Harris, Vox) vào ngân hàng mẫu; chỉ mô tả kỹ thuật.
- Không thêm phép đếm vào chỉ tiêu nào. Không hồi sinh `kiem_chuyen.py`.
- Không đổi trọng số rubric ngoài phạm vi kế hoạch 2.2 khi chưa hỏi user.
- Không viết lại tập GDP; chỉ chấm để kiểm khung.
- Ghi CHANGELOG của mỗi kênh: mục `2026-10-06 · NARRATIVE-CRAFT`, gốc rễ, file đã sửa, đường dẫn sao lưu. GocNhinPodcast ghi thêm mục KE-CHUYEN (chuyển từ Dòng Chảy).
- Trả lời user bằng tiếng Việt, câu ngắn, không dùng dấu gạch ngang dài.
- Làm từng bước theo mục 4 của kế hoạch; mỗi bước xong báo một tin ngắn kèm danh sách file; không hẹn giờ, không chạy nền rồi chờ.

## Cách báo cáo cuối
Một tin gồm: (1) bảng 9 test với kết quả đạt/không và bằng chứng (lệnh grep, số dòng); (2) điểm khung chấm thật cho tập GDP ở hai cấp, mỗi chỉ tiêu có trích câu; (3) danh sách file đã sửa ở hai kênh; (4) những điểm còn chờ user.
