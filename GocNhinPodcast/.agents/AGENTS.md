# HIẾN PHÁP GocNhinPodcast (bản 03/10/2026)

File này được Claude Code (`CLAUDE.md` nạp qua `@import`) và Antigravity (tự nạp `.agents/AGENTS.md`) đọc ở mọi phiên. Phải giữ dưới 11.000 bytes, vì quá ngân sách thì Antigravity cắt hoặc bỏ cả file. Bản cũ: `.agents/reference/AGENTS_truoc_20261003.md` (tham khảo, không tự nạp).

## 1. Một thư mục chỉ dẫn duy nhất
- **Mọi chỉ dẫn cho mọi agent, mọi IDE nằm trong `GocNhinPodcast/.agents/`**: hiến pháp này, thẻ pha (`phases/`), skill (`skills/`), persona (`personas/`), workflow (`workflows/`), rule (`rules/`), ví dụ (`examples/`), tham khảo (`reference/`). DNA nội dung dùng chung ở `00_core/`, khuôn ở `02_templates/`.
- `.claude/` chỉ chứa cấu hình Claude Code (quyền, hook). `CLAUDE.md`, `GEMINI.md`, `~/.gemini/GEMINI.md` chỉ được trỏ về đây, không chứa luật riêng. Không tạo skill, rule, persona ở chỗ khác.
- Tự nạp mỗi phiên chỉ có file này (và `rules/orchestration-protocol.md` cho Claude). Mọi file khác chỉ đọc khi **thẻ pha** trỏ tới.

## 2. Kênh và khán giả
- Kênh GocNhinPodcast, `https://www.youtube.com/@GocNhin_Podcast` (có dấu `_`). Lane: kinh tế, công nghiệp, tài chính, địa kinh tế (`00_core/channel_bible.md`).
- Khán giả chính: nam 35–40 tuổi, hiểu biết, phản biện cao. Họ cần cơ chế, nghịch lý, cái giá; không cần nghe lại điều báo đã viết.
- Giọng: người am hiểu nói chuyện bên bàn trà; khách quan là không tô hồng, không bôi đen. Thương hiệu Việt được gọi thẳng tên, nói như người trong nhà (`00_core/stance_and_judgment.md`).

## 3. Ràng buộc cứng (máy kiểm phần đo được bằng `scripts/kiem_pha.py <slug> --pha <n>`)
1. **Dữ kiện có nguồn gốc mở được** (URL + ngày + câu nguyên văn, hoặc `research_vault/`); ghi vào sổ `00_so_du_kien.md` với một trong ba nhãn `verified_data`, `market_analysis`, `opinion_commentary`. Không bịa số, không bịa câu trích. Báo cáo Gem hay NotebookLM tự sinh chỉ là manh mối.
2. **Ranh giới tài chính, pháp lý:** không khuyến nghị mua bán, không dự đoán giá, không phán xét động cơ hay đạo đức (`00_core/financial_boundaries.md`).
3. **Câu thoại** dưới 150 ký tự (trần của máy TTS, không phải mục tiêu viết); không dấu gạch ngang dài `—`; không nhãn khung sườn (`[HOOK]`, `[CTA]`…) trong file thành phẩm.
4. **Dòng lưu ý bắt buộc** trong voiceover: "Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng".
5. **Không dùng script gọi API mô hình ngoài** để viết, dịch, tóm tắt kịch bản hay prompt; không sinh prompt hàng loạt bằng vòng lặp code.
6. **Mỗi lần một pha, dừng ở cổng.** Cổng do user và Claude quyết. Pha 12–14 (hình ảnh, âm thanh, video) và thu âm TTS chỉ chạy khi user yêu cầu.

## 4. Hằng số vận hành (chỉ định nghĩa ở đây)
- Tốc độ đọc 223–235 từ/phút; ngân sách từ = số phút × 223.
- Độ dài mặc định 8–25 phút; dài hơn cần user duyệt. Mỗi chương tối đa 1.050 từ.
- QA đạt khi tổng ≥ 8,5/10 và không trụ cột nào < 7,5 (`compliance_council`). Chất kể chuyện chấm riêng theo `00_core/narrative_craft_rubric.md` (trụ cột K của `00_core/quality_rubric.md`, chấm mù tại `compliance_council` Khóa 6); K không đạt mốc ĐẠT của file đó thì không qua QA dù đạt 8,5.
- CTA đăng ký đúng 1 lần, cuối Chương 2. Mẫu: "Nếu anh chị thấy những phân tích này hữu ích, một lượt đăng ký kênh của anh chị là nguồn động viên rất lớn cho đội ngũ sản xuất."
- Phản đề (Devil's Chapter): mặc định một chương riêng ở cao trào hồi 2.
- Thứ tự chấm: cổng máy, rồi người chấm khác người viết, rồi user. Agent viết không tự cho điểm.

## 5. Cách nạp: theo thẻ pha, không nạp tràn
- Mỗi pha có một **thẻ pha** `.agents/phases/<pha>.md`. Thẻ là cổng vào duy nhất: nói rõ đọc file nào, **phần nào**, theo thứ tự nào, và những gì **không cần đọc**. Đọc thẻ trước khi làm; không đọc tràn ngoài thẻ.
- Dữ kiện đi theo **vị trí nguồn**: mỗi con số trong brief ghi vị trí nguồn gốc; người viết mở đúng chỗ đó, không dựa vào bản diễn giải của pha trước. Pha sau không được nâng độ chắc chắn của một dữ kiện.
- Không dùng chương của tập cũ làm khuôn giọng; giọng lấy từ thẻ pha và `00_core/voice_dna.md`.

| Pha | Việc | Thẻ |
|---|---|---|
| 0 | Chọn đề tài, Gem Scout, hiến chương tập | `phases/pha_00_de_tai.md` |
| 1 | Bản đồ nước đi, giả thuyết cạnh tranh | `phases/pha_01_ban_do.md` |
| 2 | Nghiên cứu sâu (NotebookLM), research map, synthesis | `phases/pha_02_nghien_cuu.md` |
| 3 | Strategy brief | `phases/pha_03_brief.md` |
| 4 | Outline biện chứng | `phases/pha_04_outline.md` |
| 5 | Hook | `phases/pha_05_hook.md` |
| 6 | Chapter briefs, NST, thumbnail brief | `phases/pha_06_chapter_brief.md` |
| 7 | Viết chương | `phases/pha_07_viet_chuong.md` |
| 8 | Gộp voiceover | `phases/pha_08_merge.md` |
| 9–11 | Retention audit, QA biên tập và tuân thủ | `phases/pha_09_11_kiem_dinh.md` |
| 12–14 | Hình ảnh, âm thanh, video (chỉ khi user yêu cầu) | `phases/pha_12_14_san_xuat.md` |
| 15–16 | Bàn giao, postmortem, metadata, Shorts | `phases/pha_15_16_ban_giao.md` |

## 6. Phân vai
- **Claude:** điều phối, phán quyết dữ liệu, chấm, cùng user quyết cổng (`rules/orchestration-protocol.md`, `skills/orchestrator/SKILL.md`).
- **Antigravity:** thực thi theo phiếu giao: web, NotebookLM (engine `scripts/notebooklm_engine/research_run.py`), trình duyệt CDP riêng cho mỗi agent, viết theo thẻ pha. Không tự chuyển pha. Trao đổi qua `_agent_chat/<phòng>/` (`/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`).
- **User:** duyệt cổng, cung cấp số liệu YouTube Studio.
- Sau mỗi pha: cập nhật `01_management/episode_registry.csv` (Claude sửa bằng Edit/Write) và nối thêm một khối vào `episodes/<slug>/00_pipeline_operator_log.md`.

## 7. Luật sửa DNA
1. Một chủ đề, một bản gốc; nơi khác chỉ trỏ tới. Sửa thì sửa bản gốc.
2. Gặp lỗi chất lượng: trước khi thêm luật, hỏi có luật nào gộp hoặc gỡ được không. Ưu tiên nguyên tắc, phép thử và ví dụ thật hơn danh sách cấm.
3. Mọi thay đổi phải kiểm **đường tới agent**: luật có nằm trong thẻ pha hay phiếu giao không. Kiểm bằng nhật ký `scripts/kiem_nap.py <conversationId>`, không tin lời agent tự khai đã đọc.
4. Hiến pháp này giữ dưới 11.000 bytes; thẻ pha mỗi thẻ dưới 1.500 từ. Ghi mọi thay đổi vào `.agents/CHANGELOG.md`.
