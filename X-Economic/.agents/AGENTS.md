# HIẾN PHÁP KÊNH X-Economy

File này được Claude Code (`CLAUDE.md` nạp qua `@import`) và Antigravity (tự nạp `.agents/AGENTS.md`) đọc ở mọi phiên. Phải giữ dưới 11.000 bytes, vì quá ngân sách thì Antigravity cắt hoặc bỏ cả file. Bản cũ: `.agents/reference/AGENTS_truoc_20261006.md` (tham khảo, không tự nạp).

## 1. Một thư mục chỉ dẫn duy nhất
- **Mọi chỉ dẫn cho mọi agent, mọi IDE nằm trong `X-Economic/.agents/`**: hiến pháp này, thẻ pha (`phases/`), skill (`skills/`), persona (`personas/`), workflow (`workflows/`), rule (`rules/`), ví dụ (`examples/`), tham khảo (`reference/`). DNA nội dung dùng chung ở `00_core/`, khuôn ở `02_templates/`.
- `.claude/` chỉ chứa cấu hình Claude Code (quyền, hook). `CLAUDE.md`, `GEMINI.md`, `~/.gemini/GEMINI.md` chỉ được trỏ về đây, không chứa luật riêng. Không tạo skill, rule, persona ở chỗ khác.
- Tự nạp mỗi phiên chỉ có file này (và `rules/orchestration-protocol.md` cho Claude). Mọi file khác chỉ đọc khi **thẻ pha** trỏ tới.

## 2. Kênh và khán giả
- Kênh `X-Economy`. Lane: phân tích kinh tế và kinh tế chính trị thế giới (tài chính, vĩ mô, thị trường vốn, chuỗi cung ứng, công nghệ) và tác động tới Việt Nam (`00_core/channel_bible.md`).
- Khán giả chính: người Việt Nam hiểu biết, phản biện cao, thích số liệu. Họ cần nhìn thấy cơ chế ngầm, dòng tiền, xung đột thể chế, chuỗi cung ứng và dữ liệu định lượng; không cần nghe tóm tắt báo chí bề nổi.
- Giọng: điềm tĩnh, có nghề, có một bộ óc đang nghĩ; đặc trưng "người dẫn dữ liệu" (số liệu và biểu đồ là nhân vật chính, nhịp nhanh hơn, cuối tập có chỉ báo để người xem tự theo dõi) (`00_core/voice_dna.md`, `00_core/stance_and_judgment.md`). Phân loại đề tài theo 3 loại (`00_core/content_principles.md` §3: Loại A - đời sống kinh tế; Loại B - bài toán doanh nghiệp/ngành/quốc gia; Loại C - quy luật lớn/thể chế kinh tế toàn cầu).
- Nhận diện thị giác: Obsidian Midnight Navy `#0A0E17`, Burnished Gold `#D4AF37`, Electric Cyan `#00E5FF`, dữ liệu chuyển động (`00_core/visual_style_guide.md`).

## 3. Ràng buộc cứng (máy kiểm phần đo được bằng `scripts/verify_phase_gate.py`)
1. **Dữ kiện có nguồn gốc mở được** (URL + ngày + câu nguyên văn, hoặc `research_vault/`); ghi nhận mã dữ liệu (`DATA-XX`), phân loại taxonomy (`verified_data`, `market_analysis`, `opinion_commentary`). Không bịa số, không bịa câu trích. Báo cáo NotebookLM tự sinh chỉ là manh mối.
2. **Ranh giới tài chính, pháp lý:**
   - Chuẩn mực *Lowe v. SEC (1985)*: phân tích vĩ mô khách quan, phi cá nhân hóa, tuyệt đối không tư vấn mua/bán cổ phiếu, không khuyến nghị đầu tư tài chính (`00_core/financial_boundaries.md`).
   - Phòng vệ phỉ báng doanh nghiệp (*Corporate Libel Protection*): mọi cáo buộc phải dẫn nguồn hồ sơ kiểm toán, báo cáo thường niên, hồ sơ tư pháp hoặc cơ quan quản lý chính thức; phán xét cơ chế không phán xét động cơ hay đạo đức cá nhân (`00_core/brand_safety_guidelines.md`, `00_core/stance_and_judgment.md`).
3. **Câu thoại** dưới 150 ký tự (lý tưởng 100–120 ký tự cho tai nghe); không dấu gạch ngang dài `—` trong voiceover; không nhãn khung sườn template (`[BLOCK X]`, `[HOOK]`, `[CTA]`…) trong file thành phẩm xuất bản (`metadata.md`, `voiceover.md`, `chapter_XX.md`).
4. **Dòng lưu ý bắt buộc** trong voiceover: "Nội dung chia sẻ luận điểm khách quan, mang tính thảo luận và xây dựng. Mọi phân tích không cấu thành khuyến nghị đầu tư tài chính."
5. **Không dùng script gọi API mô hình ngoài** để viết, dịch, tóm tắt kịch bản hay sinh prompt hàng loạt bằng code. Phân cảnh AI tuân thủ nguyên tắc cách ly an toàn I2V (dòng `[VIDEO]` dùng Pure Optical Camera Motion, không tên người thật, không từ khóa chính trị nhạy cảm). Bản đồ Việt Nam bắt buộc đầy đủ Hoàng Sa, Trường Sa, Phú Quốc, Côn Đảo; cấm đường lưỡi bò phi pháp.
6. **Mỗi lần một pha, dừng ở cổng.** Cổng do user và Claude quyết. Pha 12–14 (hình ảnh, âm thanh, video) và thu âm TTS chỉ chạy khi user yêu cầu trực tiếp.

## 4. Hằng số vận hành (chỉ định nghĩa ở đây)
- Tốc độ đọc chuẩn 223–235 từ/phút; ngân sách từ = số phút × 223.
- Độ dài mặc định Cấp 1–2 (8–25 phút); Cấp 3–4 chỉ khi user duyệt riêng. Mỗi chương tối đa 1.050 từ (kích hoạt phân hạch chương nếu quá tải).
- QA đạt khi tổng ≥ 8,5/10 và không trụ cột nào < 7,5 (`compliance_council`). Chất kể chuyện chấm riêng theo `00_core/narrative_craft_rubric.md` (trụ cột K của `00_core/quality_rubric.md`, chấm mù tại `compliance_council` Khóa 6); K không đạt mốc ĐẠT thì không qua QA dù tổng ≥ 8,5.
- CTA đăng ký đúng 1 lần duy nhất, cuối Chương 2, ngay trước Bridge sang Chương 3.
- Phản đề (Devil's Chapter): mặc định 1 chương độc lập ở cao trào Hồi 2 (50–70% thời lượng, chiếm 18–24% ngân sách từ) — Tri-Adversarial Red Team Steelmanning.
- Nghiệm thu từng chương độc lập: viết xong 1 chương dừng chờ user duyệt trước khi sang chương tiếp theo.
- Thứ tự chấm: cổng máy, rồi người chấm khác người viết (chấm mù), rồi user. Tác giả tự soi bằng Phiếu B/Phiếu A để sửa trước khi nộp, không tự cho điểm để qua cổng.

## 5. Cách nạp: theo thẻ pha, không nạp tràn
- Mỗi pha có một **thẻ pha** `.agents/phases/<pha>.md`. Thẻ là cổng vào duy nhất: nói rõ đọc file nào, **phần nào**, theo thứ tự nào, và những gì **không cần đọc**. Đọc thẻ trước khi làm; không đọc tràn ngoài thẻ.
- Dữ kiện đi theo **vị trí nguồn**: mỗi con số trong brief ghi vị trí nguồn gốc; người viết mở đúng chỗ đó, không dựa vào bản diễn giải của pha trước. Pha sau không được nâng độ chắc chắn của một dữ kiện.
- Không dùng chương của tập cũ làm khuôn giọng; giọng lấy từ thẻ pha và `00_core/voice_dna.md`.

| Pha | Việc | Thẻ |
|---|---|---|
| 0 | Đề tài, đánh giá sơ bộ, phân loại chủ đề (A/B/C) | `phases/pha_00_de_tai.md` |
| 1 | Bức tranh lớn (Global Vision: Bàn cờ 4 Tầng + Ma trận 4 Lăng kính) | `phases/pha_01_ban_do.md` |
| 2 | Nghiên cứu sâu (NotebookLM deep research, research map, synthesis) | `phases/pha_02_nghien_cuu.md` |
| 3 | Strategy brief | `phases/pha_03_brief.md` |
| 4 | Dàn ý biện chứng Hegel (Master Outline & Orientation Frame) | `phases/pha_04_outline.md` |
| 5 | Hook Lab (Hook sau khi có dàn ý) | `phases/pha_05_hook.md` |
| 6 | Chapter briefs (20 trường + nhịp chuyện), NST, thumbnail brief | `phases/pha_06_chapter_brief.md` |
| 7 | Viết từng chương (Tam đoạn luận 3 nhịp, tự soi Phiếu B) | `phases/pha_07_viet_chuong.md` |
| 8 | Gộp voiceover hoàn chỉnh | `phases/pha_08_merge.md` |
| 9–11 | Retention audit, QA biên tập, tuân thủ & chấm mù Phiếu A/B | `phases/pha_09_11_kiem_dinh.md` |
| 12–14 | Hình ảnh (I2V/I2V+ nhịp ý), âm thanh, video (chỉ khi có yêu cầu) | `phases/pha_12_14_san_xuat.md` |
| 15–16 | Bàn giao (Production Notes), postmortem, metadata, Shorts | `phases/pha_15_16_ban_giao.md` |

## 6. Phân vai
- **Claude:** điều phối, phán quyết dữ liệu, chấm kiểm định, cùng user quyết cổng (`rules/orchestration-protocol.md`).
- **Antigravity:** thực thi theo phiếu giao: web, NotebookLM (qua `scripts/` hoặc CLI với `BypassSandbox: true`), trình duyệt CDP Canary 9222 riêng, viết theo thẻ pha. Không tự chuyển pha. Trao đổi qua `_agent_chat/<phòng>/` (`/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`).
- **User:** duyệt cổng, cung cấp số liệu YouTube Studio.
- Sau mỗi pha: cập nhật `01_management/episode_registry.csv` (Claude sửa bằng Edit/Write) và nối thêm một khối vào `episodes/<slug>/00_pipeline_operator_log.md`.

## 7. Luật sửa DNA
1. Một chủ đề, một bản gốc; nơi khác chỉ trỏ tới. Sửa thì sửa bản gốc.
2. Gặp lỗi chất lượng: trước khi thêm luật, hỏi có luật nào gộp hoặc gỡ được không. Bãi bỏ việc ghi log khuyết tật runtime (`llm_error_log.md`), sửa dứt điểm trực tiếp vào file đích.
3. Mọi thay đổi phải kiểm **đường tới agent**: luật có nằm trong thẻ pha hay phiếu giao không. Kiểm bằng nhật ký `python3 scripts/kiem_nap.py <conversationId>`, không tin lời agent tự khai đã đọc.
4. Hiến pháp này giữ dưới 11.000 bytes; thẻ pha mỗi thẻ dưới 1.500 từ. Ghi mọi thay đổi vào `.agents/CHANGELOG.md`.
