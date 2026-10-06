# Kế hoạch chi tiết: Khung chấm nghệ thuật kịch bản (để Opus thực thi)

Soạn: Claude (Fable), 06/10/2026. Trạng thái: user duyệt nguyên tắc, chờ thực thi. Người thực thi: Opus. Người chấm kết quả: Claude bằng các test ở mục 6, không chấm bằng cảm nhận.

## 0. Đọc trước khi làm (bắt buộc, theo thứ tự)
1. `Dong_Chay/01_management/DE_XUAT_KHUNG_CHAM_NGHE_THUAT_KICH_BAN_20261006.md` (10 chỉ tiêu, mốc đạt, chấm thử tập GDP).
2. `Dong_Chay/.agents/CHANGELOG.md` mục `2026-10-06 · KE-CHUYEN` (những gì đã sửa sáng nay và vì sao; kế hoạch này THAY phần "Lượt đọc như người nghe" của đợt đó).
3. `Dong_Chay/00_core/quality_rubric.md` (rubric 10 tiêu chí hiện có, thang 110) và `Dong_Chay/00_core/stance_and_judgment.md`.
4. `Dong_Chay/.agents/skills/chapter_writer/SKILL.md` Bước 3b, `Dong_Chay/.agents/skills/compliance_council/SKILL.md` Khóa 6.
5. Bộ nhớ: `/Users/pro16/.claude/projects/-Users-pro16-Documents-VideoProject/memory/prose-judged-by-llm-not-counts.md`, `channels-mirror-process-fixes.md`, `port-architecture-not-episodes.md`.

Quy tắc chung của đợt: không chỉ tiêu nào chấm bằng đếm; mọi điểm 4–5 và 1–2 phải trích câu; sao lưu mỗi file trước khi sửa vào `/Users/pro16/VideoProject_backup/khung_cham_nghe_thuat_20261006/<kênh>/<đường dẫn>`; không sửa tập đã đăng; không chép tập của kênh này sang kênh kia.

## 1. Quy trình chấm (chốt với user 06/10)
Thứ tự: **đọc trọn → chấm cả bài → chấm từng chương → đối chiếu hai cấp → kết luận và lệnh sửa.** Hai người chấm: người viết tự chấm sau Pha 7; Critical Auditor chấm mù ở Pha 10 (không xem bản tự chấm); lệch > 1 điểm ở chỉ tiêu nào thì đọc lại cùng nhau chỗ đó. Chấm cấp bài lần đầu ngay sau dàn ý (Pha 4), chỉ 5 chỉ tiêu cấp bài; không đạt thì không viết chương.

Chia chỉ tiêu theo cấp:
- **Cấp bài (5):** I Câu hỏi kịch tính trung tâm · II Mức cược · III Gieo và gặt · IV-b Cao trào (cú lật lớn nhất, vị trí 50–70%) · X Kết và nghĩa.
- **Cấp chương (5 + 1 cột):** IV-a Cú lật trong chương · V Cảnh so với tóm tắt · VI Chủ thể và xung đột · VIII Nhịp · IX Câu cho tai · cột "chương này đẩy câu hỏi trung tâm đi bao xa" (1–5).
- VII Giọng và lập trường chấm ở cả hai cấp (cấp chương: có nhận định không; cấp bài: nhận định có nhất quán và đúng chế độ kết không).

Mốc ĐẠT: không chỉ tiêu nào dưới 3; trung bình ≥ 4,0; I, IV, V ≥ 4.

## 2. Sản phẩm cần tạo (Dòng Chảy trước)

### 2.1 File chuẩn mới: `Dong_Chay/00_core/narrative_craft_rubric.md`
Nội dung bắt buộc, theo thứ tự:
1. Mục đích, phạm vi (áp cho `07_outline.md` ở cấp bài; `chapter_XX.md` ở cả hai cấp; `voiceover.md` chấm lại cấp bài sau merge).
2. Bảng 10 chỉ tiêu: tên, câu hỏi chấm, mốc mô tả cho điểm 1 / 3 / 5 (lấy từ đề xuất, viết lại cho gọn, không đổi nghĩa), cấp áp dụng.
3. Quy trình 5 bước ở mục 1, kèm quy định "đọc trọn không ghi chép".
4. **Hai phiếu mẫu** (markdown bảng): Phiếu A cấp bài (5 chỉ tiêu + VII + bảng gieo/gặt: hạt, chương gieo, chương gặt, trạng thái); Phiếu B cấp chương (một dòng mỗi chương: 5 chỉ tiêu + VII + cột đẩy câu hỏi; mỗi ô = điểm + trích câu ≤ 25 từ).
5. Bảng đối chiếu hai cấp và cách đọc: bài cao chương thấp → lỗi ở viết chương; chương cao bài thấp → lỗi ở dàn ý; ghi rõ chuyển về pha nào.
6. Mốc ĐẠT và mẫu "lệnh sửa" (chương, chỉ tiêu, câu lỗi, một câu viết lại mẫu).
7. **Ngân hàng đoạn mẫu**: với mỗi chỉ tiêu, một đoạn 5 điểm và một đoạn 1 điểm. Đoạn 1 điểm lấy từ tập GDP (bản phát hành `episodes/gdp-9-thang-2026-con-so-10-tu-dau/chapter_0X.md`). Đoạn 5 điểm: dùng `episodes/gdp-9-thang-2026-con-so-10-tu-dau/chapter_04.md` đoạn "hàng chờ giải thể" cho III/IV; `_thu_dna_ke_chuyen/chapter_03.md` cho V; các chỉ tiêu còn thiếu mẫu 5 điểm thì ghi `[CHỜ USER CHỌN MẪU]` kèm mô tả loại đoạn cần tìm, không bịa đoạn từ kênh tham chiếu (không chép lời Max Fisher/Johnny Harris; chỉ mô tả kỹ thuật).
8. Dòng "Không chỉ tiêu nào chấm bằng đếm" và lý do (bộ nhớ `prose-judged-by-llm-not-counts`).

### 2.2 Sửa `Dong_Chay/00_core/quality_rubric.md`
- Thêm trụ cột **K. Narrative Craft** trỏ về `narrative_craft_rubric.md`; trọng số đề xuất 20 điểm, lấy từ: I (12→8), E (10→6), D (12→8), J (5→3), tổng vẫn 110. Ghi rõ K là điều kiện cứng: K dưới mốc ĐẠT thì tập không qua Pha 10 dù tổng điểm cao.
- Mục 4 Hard-Fail: thêm "Cấp bài không đạt I hoặc X; cấp chương có chương nào IV-a, V cùng ≤ 2".
- Mục 5 phiếu chấm nhanh: thêm hai dòng tổng K cấp bài, K cấp chương.
- Mục 9 Retention Checkpoint: thêm "chạy Phiếu A cấp bài trên outline".

### 2.3 Sửa `Dong_Chay/.agents/skills/chapter_writer/SKILL.md`
- Thay toàn bộ Bước 3b "Lượt đọc như người nghe" bằng **Bước 3b: Tự chấm theo `narrative_craft_rubric.md`**: người viết chạy Phiếu B cho chương vừa viết và cập nhật Phiếu A (dòng gieo/gặt). In phiếu trong chat, không ghi vào `chapter_XX.md`. Chỉ lưu khi chương đạt mốc.
- Bảng tự kiểm 5 dòng: dòng "Kể chuyện" trỏ về Phiếu B.
- Tiêu chí 9, 10 trong bảng 10 tiêu chí: gộp thành một tiêu chí "Narrative Craft (Phiếu B đạt mốc)".
- Giữ nguyên Chặng 2 bước 0 (bảng nhịp chương) vì đó là công cụ viết, không phải công cụ chấm.

### 2.4 Sửa `Dong_Chay/.agents/skills/compliance_council/SKILL.md`
- Khóa 6 viết lại: Critical Auditor chấm mù Phiếu A + Phiếu B, không xem bản tự chấm; đối chiếu hai cấp; lệch > 1 điểm thì đọc lại cùng người viết; kết luận chuyển về Pha 4 hay Pha 7 theo bảng đối chiếu.
- Điểm K đưa vào tổng rubric.

### 2.5 Sửa `Dong_Chay/.agents/workflows/build_outline.md`
- Trạm 5 hoặc Cổng duyệt dàn ý: thêm "Chấm Phiếu A cấp bài trên `07_outline.md` (I, II, III, IV-b, X). Không đạt thì sửa dàn ý trước khi xin duyệt."
- Checklist cuối: thêm dòng tương ứng.

### 2.6 Sửa `Dong_Chay/.agents/rules/chapter-writing.md`, `rules/editorial-quality.md`
- Thay câu "Lượt đọc như người nghe" bằng "Phiếu B cấp chương theo `00_core/narrative_craft_rubric.md`".
- `editorial-quality.md` mục Review questions: thêm 3 câu từ chỉ tiêu IV, V, VI.

### 2.7 Sửa `Dong_Chay/.agents/examples/chapter_writer_examples.md`
- Mục "Chương mạnh phải có gì" 6–8: thay dòng 8 bằng "Phiếu B đạt mốc"; thêm chú thích Pair 6–8 là mẫu 1/5 điểm cho chỉ tiêu III, IV, V.

### 2.8 Sửa persona `Dong_Chay/.agents/personas/the_critical_auditor.md`
- Thêm nhiệm vụ "chấm mù narrative craft" và cấm xem bản tự chấm trước khi chấm.

### 2.9 Workflow `Dong_Chay/.agents/workflows/write_chapter.md` (nếu có bước tương ứng) và `revise_chapter.md`
- Thêm bước tự chấm Phiếu B; lệnh sửa chương phải nêu chỉ tiêu và câu lỗi.

### 2.10 Khuôn `Dong_Chay/02_templates/masterpiece_pipeline/`
- Tạo `11_narrative_craft_scorecard_template.md` (Phiếu A + B rỗng) để mỗi tập lưu kết quả chấm ở `episodes/[slug]/11_narrative_craft_scorecard.md`; thêm vào `02_templates/episode_template/README.md` và danh sách file của `CLAUDE.md` (mục file hỗ trợ tùy chọn, không bắt buộc với tập đã đăng).

### 2.11 CHANGELOG
- Mục mới `2026-10-06 · NARRATIVE-CRAFT`, ghi: thay "Lượt đọc như người nghe" bằng khung 10 chỉ tiêu hai cấp; liệt kê file sửa; đường dẫn sao lưu.

## 3. GocNhinPodcast (làm sau khi Dòng Chảy qua test mục 6)
Nguyên tắc: chuyển theo nghĩa, giữ phần riêng kênh (Loại A đời sống, "chúng tôi cho rằng", persona của GN). Chỉ đụng framework, không đụng `episodes/`.
Danh sách file đối ứng (đã kiểm tồn tại): `GocNhinPodcast/00_core/quality_rubric.md`, `00_core/longform_blueprint.md`, `00_core/retention_gate_checklist.md`, `.agents/workflows/build_outline.md`, `.agents/skills/chapter_writer/SKILL.md`, `.agents/skills/compliance_council/SKILL.md`, `.agents/skills/script_architect/SKILL.md`, `.agents/examples/chapter_writer_examples.md`, personas tương ứng, CHANGELOG của GN.
Ngoài khung chấm, GN còn **chưa nhận đợt KE-CHUYEN sáng 06/10** (build_outline vẫn `D × 35 từ`, quota DATA-XX, "lộ trình 3 trạm"; chapter_writer vẫn "làm dày bằng số liệu"; ví dụ chỉ 5 cặp). Chuyển cả hai đợt trong một lần, theo đúng danh sách file của CHANGELOG Dòng Chảy mục KE-CHUYEN và mục NARRATIVE-CRAFT. Ngân hàng đoạn mẫu của GN lấy từ `gsm-chau-au-v4/chapter_04.md` (5 điểm cho I, IV, VI) và `tai-xe-grab-tat-app-vs-gsm/chapter_02.md`, `green-sm-an-do/chapter_07.md` (1 điểm cho V, VIII).

## 4. Thứ tự thực thi và ước lượng
| Bước | Việc | Phụ thuộc |
|---|---|---|
| 1 | Sao lưu; viết `narrative_craft_rubric.md` (2.1) | — |
| 2 | Sửa rubric tổng (2.2) | 1 |
| 3 | Sửa chapter_writer, compliance_council, build_outline, rules, examples, persona, workflows, khuôn (2.3–2.10) | 1 |
| 4 | Chấm thật tập GDP bằng khung mới, lưu `episodes/gdp-9-thang-2026-con-so-10-tu-dau/11_narrative_craft_scorecard.md` | 1 |
| 5 | CHANGELOG (2.11) | 2–4 |
| 6 | Chuyển sang GocNhinPodcast (3) | 5 và test mục 6 đạt |
Không hẹn giờ, không chạy nền; mỗi bước xong báo một tin kèm danh sách file.

## 5. Không làm
- Không viết lại tập GDP (chỉ chấm để kiểm khung).
- Không thêm phép đếm nào vào bất kỳ chỉ tiêu; không hồi sinh `kiem_chuyen.py`.
- Không chép nguyên văn kịch bản kênh tham chiếu vào ngân hàng mẫu.
- Không đổi trọng số rubric ngoài phạm vi 2.2 khi chưa hỏi user.
- Không sửa `AGENTS.md` ngoài một dòng trỏ tới `narrative_craft_rubric.md` ở mục chuẩn chất lượng.

## 6. Test nghiệm thu (Claude chạy)
1. `grep -rn "Lượt đọc như người nghe" Dong_Chay/.agents Dong_Chay/00_core` chỉ còn trong CHANGELOG.
2. `grep -rn "narrative_craft_rubric" Dong_Chay` xuất hiện ở: quality_rubric, chapter_writer SKILL, compliance_council, build_outline, chapter-writing rule, editorial-quality rule, critical_auditor persona, CLAUDE.md hoặc README khuôn.
3. `narrative_craft_rubric.md` có đủ: 10 chỉ tiêu × mốc 1/3/5, Phiếu A, Phiếu B, bảng đối chiếu, mốc ĐẠT, ngân hàng mẫu (mỗi chỉ tiêu có đoạn 1 điểm; đoạn 5 điểm hoặc `[CHỜ USER CHỌN MẪU]`), không có từ "đếm" theo nghĩa chấm.
4. Tổng điểm rubric vẫn 110; K có trong Hard-Fail.
5. `11_narrative_craft_scorecard.md` của tập GDP: mọi ô điểm 4–5 và 1–2 có trích câu; kết luận chỉ ra cú lật/cảnh/chủ thể là chỗ hỏng (khớp chấm thử trong đề xuất, lệch ≤ 1 điểm mỗi chỉ tiêu; nếu lệch hơn, Opus phải ghi lý do).
6. Một lượt chấm mù giả lập: Claude chấm lại chương 3 GDP bằng Phiếu B, so với bản của Opus, lệch ≤ 1 điểm mỗi chỉ tiêu.
7. Với GN: diff `build_outline.md` và `chapter_writer/SKILL.md` của hai kênh chỉ khác ở phần riêng kênh (loại đề tài, persona, tên file), không khác ở nguyên tắc.

## 7. Điểm còn chờ user
- Chọn đoạn mẫu 5 điểm cho các chỉ tiêu II, VII, VIII, IX, X (hoặc cho phép dùng mô tả kỹ thuật thay đoạn).
- Trọng số 20 điểm cho K và cách lấy từ các trụ cột khác (2.2).
- Có bắt buộc file `11_narrative_craft_scorecard.md` cho mọi tập mới không.

## 8. Phần viết: chỗ nào trong DNA sinh ra nội dung báo cáo (bổ sung 06/10, sau câu hỏi của user)

Chuỗi tạo ra một chương: Pha 2 nghiên cứu → Pha 4 outline → Pha 6 brief chương → Pha 7 viết (Chặng 1 cơ chế, Chặng 2 chuyển thể) → tự kiểm. Lỗi báo cáo sinh ra ở từng mắt xích, và mắt xích sau khuếch đại mắt xích trước.

| # | Mắt xích | Cơ chế gây báo cáo (file, dòng) | Trạng thái |
|---|---|---|---|
| W1 | Pha 4 outline | Đơn vị dựng chương là điểm dữ liệu: quota DATA-XX, công thức chữ `D × 35 từ`, khuôn buộc "giải mã đủ quota Data Anchors" (`workflows/build_outline.md` Trạm 2, 5; `07_outline_template.md`) | **ĐÃ SỬA 06/10** sang bản đồ nhịp chuyện |
| W2 | Pha 4 outline | Lệnh "lộ trình 3 trạm" trong Orientation Frame (`build_outline.md`, `07_outline_template.md`, `AGENTS.md`, `content-os-pipeline.md`, `quality_rubric.md`, `longform_blueprint.md`) | **ĐÃ SỬA 06/10** |
| W3 | Pha 6 brief chương | Khuôn 16 trường toàn là hàng dữ liệu: trường 4 `data_verified`, trường 8 `chapter_signature` đòi "mật độ dữ liệu", trường 10 bảng pointer ≥ 5 dòng "Data Point Cốt Lõi + con số" (`08_chapter_briefs_template.md` dòng 39–43; `script_architect/SKILL.md` Pha 6). Không trường nào là nhịp chuyện, cú lật, vật chứng, chủ thể muốn gì. Người viết nhận một bảng số kèm lệnh "đủ quota" thì lắp bảng số thành văn | **CHƯA SỬA** → việc 8.1 |
| W4 | Pha 7 Chặng 1 | "Vault mining để LÀM DÀY", "neo nguồn bằng câu dẫn chuẩn", "thêm data gốc" là cách mở rộng đầu tiên, tự kiểm "tất cả data anchors đã xuất hiện?" (`chapter_writer/SKILL.md`, `PRE_FLIGHT_GATE.md`) | **ĐÃ SỬA 06/10** |
| W5 | Pha 7 Chặng 2 | Chuyển thể không có sản phẩm riêng; gộp vào cùng lượt với Chặng 1 nên chặng có cổng đo (Chặng 1) chiếm hết | **ĐÃ SỬA 06/10** (bảng nhịp chương, bước 0) nhưng vẫn cùng một người cùng một lượt → việc 8.2 |
| W6 | Ví dụ mẫu | 5 cặp chỉ dạy "câu số có diễn giải" (`examples/chapter_writer_examples.md`) | **ĐÃ SỬA 06/10** (Pair 6–8) |
| W7 | Persona | `the_narrative_director.md` có Mô hình 1 "Scene Anchoring (Michael Lewis, Ira Glass)" nhưng Mục 5 "Quy trình chấp bút 3 bước" không có bước nào bắt tìm cảnh; `the_macro_strategist.md` định nghĩa kịch bản hay là "tấm bản đồ sắc lạnh" (dòng 93) → người viết hóa thân vào persona chủ đạo (macro strategist) thì viết bản đồ, không viết chuyện | **CHƯA SỬA** → việc 8.3 |
| W8 | Pha 2 nghiên cứu | `deep_researcher` và sổ dữ kiện chỉ thu con số, câu trích, URL; không thu cảnh, quyết định có ngày giờ, chi tiết đắt. Không phải nguyên nhân (DNA phải biến số thành chuyện), nhưng là chỗ rẻ nhất để chuẩn bị vật chứng cho chỉ tiêu V | **CHƯA SỬA** → việc 8.4 (tùy chọn) |
| W9 | Tự kiểm | Chỉ những gì có thước đo mới được kiểm (trần từ, 150 ký tự, từ cấm, số khớp sổ); chất chuyện không có cổng | **Khung chấm mục 1–2 giải quyết** |

### Việc bổ sung vào kế hoạch (Opus làm cùng đợt)
- **8.1 Khuôn brief chương** (`02_templates/masterpiece_pipeline/08_chapter_briefs_template.md`, `script_architect/SKILL.md` Pha 6): thêm 4 trường bắt buộc ngang hàng `data_verified`: `cau_hoi_dieu_tra` (câu hỏi người nghe muốn biết ở chương này), `vat_chung` (2–3 chi tiết có thật, có nguồn: văn bản, công trình, quyết định có ngày, con số đặt cạnh con số), `cu_lat` (cách hiểu cũ → dữ kiện làm đổi), `chu_the_va_dong_co` (ai muốn gì, bị cản gì). Trường 8 `chapter_signature` bỏ cụm "mật độ dữ liệu", thay bằng "nhịp: chỗ chậm, chỗ nhanh". Bảng pointer giữ, nhưng đổi tiêu đề cột "Data Point Cốt Lõi" thành "Dữ kiện và nhịp nó phục vụ"; mỗi dòng ghi thêm cột "đọc / lên hình".
- **8.2 Tách lượt chuyển thể**: trong `chapter_writer/SKILL.md`, Chặng 2 chạy ở một lượt riêng sau khi Chặng 1 đã ra "khung xương cơ chế + bảng nhịp" (in ra chat). Khi có nhiều agent: Chặng 1 do persona chuyên môn, Chặng 2 do Narrative Director trong hội thoại khác. Khi một mình: bắt buộc in bảng nhịp, rồi mới viết văn; không viết thẳng từ bảng số.
- **8.3 Persona**: `the_narrative_director.md` Mục 5 thêm bước "tìm cảnh và vật chứng trước khi viết câu đầu"; `the_macro_strategist.md` dòng 93 sửa định nghĩa: bản đồ là thứ người xem *nhận ra* sau khi đi qua câu chuyện, không phải thứ được đọc cho nghe. Rà các persona chủ đạo khác (`the_policy_analyst`, `the_macro_economist`, `the_critical_auditor`) xem có câu định nghĩa "kịch bản hay = phân tích/bản đồ" tương tự không; có thì sửa cùng cách.
- **8.4 (tùy chọn, user quyết) Pha 2**: thêm vào `deep_researcher/SKILL.md` một đầu ra "kho vật chứng" bên cạnh sổ dữ kiện: mỗi mục là một cảnh, quyết định, văn bản, khoảnh khắc có ngày giờ và nguồn, gắn với câu hỏi của Pha 1. Không bắt buộc với tập đang chạy.
- Test thêm: (8) brief chương của một tập thử (dùng GDP chương 3) viết lại theo khuôn mới phải điền được đủ 4 trường từ vault hiện có; (9) diff persona chỉ đổi đúng các câu nêu trên.
