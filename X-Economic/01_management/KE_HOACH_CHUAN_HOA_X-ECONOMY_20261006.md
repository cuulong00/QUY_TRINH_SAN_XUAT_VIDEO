# Kế hoạch chuẩn hóa dự án X-Economic theo quy trình hiện tại (06/10/2026)

Trạng thái: bản nháp chờ user duyệt. Người soạn: Claude (Opus). Chưa sửa file nào của dự án.

## 0. Bối cảnh và nguyên nhân gốc

- Kênh bị tắt kiếm tiền (quyết định "Sử dụng lại nội dung"). User xác nhận 06/10: **nội dung hay; hỏng ở sản xuất**: dùng ảnh tĩnh, video không chau chuốt, tiếng và hình không khớp, quy trình chưa chuẩn.
- Đối chiếu với DNA hiện có của dự án (đã đọc):
  | Lỗi sản xuất | Nằm ở đâu trong X-Economic |
  |---|---|
  | Ảnh tĩnh | `CLAUDE.md`, `.agents/workflows/generate_visual_prompts_plus.md`: trụ cột `INFOGRAPHIC_DATA` là "ảnh tĩnh AI + pan/zoom trong CapCut, không dùng video engine"; Pha 14 "CapCut assembly" |
  | Tiếng và hình không khớp | Phân cảnh lấy `voiceover.md` (toàn bài) làm đầu vào; còn 4 script tự sinh cảnh `fix_scenes.py`, `generate_aligned_scenes.py`, `generate_scene_map.py`, `generate_scenes_raw.py` (Dòng Chảy đã lưu trữ và cấm chúng từ 05/10); không có đối chiếu giờ thật với tiếng đọc |
  | Quy trình chưa chuẩn | Hiến pháp `.agents/AGENTS.md` 64 KB (Antigravity loại hẳn khỏi ngữ cảnh, đo ở Dòng Chảy trước 06/10); không có thẻ pha; DNA nhân đôi ở `.claude/`; registry còn lại slug mẫu và slug của kênh khác |
- Dự án lệch xa các kênh kia: `.agents` giống GocNhinPodcast khoảng 90% nhưng là bản của khoảng 28/09; `00_core` ~67%. Thiếu toàn bộ đợt 29/09 đến 06/10: hiến pháp ngắn, thẻ pha, khung chấm nghệ thuật, kể chuyện theo nhịp, kho vật chứng, tự soi không cho điểm, Hợp đồng I2V nhịp ý.
- Thư mục `X-Economic` bị `.gitignore` (dòng 145–146, ghi "Deprecated Archive … đã thay bằng X-Economics") nên **không có git để quay lại**: phải sao lưu thủ công trước mọi sửa. Còn `X-Economics` (đang trong git, 4 tập, kênh `@X-Economics-b9x`) và `X-Economic_backup`: user chọn chuẩn hóa `X-Economic`.

## 1. Chiến lược: nhân bản khung chung, giữ lớp riêng của kênh, thay phần sản xuất

Ý của user (nhân bản từ kênh sẵn có rồi chỉnh để khác biệt) đúng và rẻ nhất. Em đề xuất chi tiết:

**1a. Lấy Dòng Chảy làm gốc nhân bản, không lấy GocNhinPodcast.** Lý do: lane X-Economy (kinh tế vĩ mô điều tra toàn cầu, địa chính trị, chuỗi cung ứng, thị trường vốn) gần Dòng Chảy hơn. GocNhinPodcast mang bộ máy riêng nặng (hiến chương, sổ M-xx, `kiem_pha.py`, Gem Scout, mã H-x) gắn với doanh nghiệp Việt Nam. Dòng Chảy đã có sẵn đủ: hiến pháp 8,7 KB, 12 thẻ pha, khung chấm, `verify_phase_gate.py`.

**1b. Cắt dự án thành hai lớp.**
- **Lớp khung dùng chung (nhân bản nguyên từ Dòng Chảy, máy làm, gần như không tốn token):** `.agents/skills`, `workflows`, `rules`, `examples`, `phases` (khung), `personas` (khung), `contracts` trỏ về gốc; `00_core`: khung chấm (`narrative_craft_rubric.md`, `quality_rubric.md`, `anti_ai_isms.md` phần cổng), `02_templates`, `03_playbooks`; Hợp đồng I2V và công cụ `VideoProject/.agents/tools/i2v/` dùng chung.
- **Lớp riêng của kênh (KHÔNG ghi đè, giữ bản X-Economic hiện có và sửa tay):** `00_core/channel_bible.md`, `voice_dna.md`, `audience_personas.md`, `content_principles.md`, `financial_boundaries.md` (Lowe v. SEC, phỉ báng doanh nghiệp), `brand_safety_guidelines.md`, `visual_style_guide.md` và `thumbnail_style_guide.md` (Obsidian Midnight Navy `#0A0E17`, Burnished Gold `#D4AF37`, Electric Cyan `#00E5FF`: khác hẳn tông ấm của Dòng Chảy), `profile/`, `01_management/topic_backlog.md`, `readme.md`, phần kênh trong hiến pháp.

**1c. Sự khác biệt giữa các kênh (chống "nội dung lặp"):** ba kênh dùng chung khung nhưng khác ở lớp riêng: ngôn ngữ và thị trường (xem câu hỏi 1), giọng, bảng màu và phong cách hình, loại đề tài, khán giả, ràng buộc pháp lý. Giữ các khác biệt này trong `00_core`, không nhân bản chúng.

## 2. Đại tu phần sản xuất (nguyên nhân gốc, ưu tiên cao nhất)

Thay bản 3 trụ cột cũ bằng quy trình hiện hành của Dòng Chảy, không viết mới:
1. Pha 12 theo Hợp đồng `VideoProject/.agents/contracts/i2v_nhip_y.md`: phân cảnh **theo nhịp ý**, **từng chương** (`chapter_XX.md`, không đọc `voiceover.md`), 5 loại shot (`VIDEO_AI`, `BROLL`, `INFOGRAPHIC_TINH`, `INFOGRAPHIC_DONG`, `BAO_CHI`), sàn B-roll 5 giây.
2. Dựng video bằng công cụ chung `VideoProject/.agents/tools/i2v/` và Hợp đồng `i2v_quy_trinh_dung_video.md`, `i2v_quy_trinh_hyperframes.md`, `i2v_quy_trinh_broll.md`. Hạ ảnh tĩnh xuống mức ngoại lệ, mọi cảnh có chuyển động có chủ đích.
3. **Tiếng và hình khớp bằng giờ thật:** thời gian mỗi cảnh đọc từ file âm thanh thật cộng Whisper tại lúc dựng, kiểm sha256, không bảng giờ chép tay (quyết định đã chốt ở các tập GDP: "đầu vào I2V phải sống"). Thêm một cổng máy: ranh giới cảnh phải rơi đúng vào mốc từ của lời đọc trong ngưỡng cho phép.
4. Gỡ khỏi DNA đang hiệu lực: 4 script tự sinh cảnh (chuyển vào `_archive/`), workflow 3 trụ cột, và các dòng "CapCut, 0đ GPU cloud" ở `CLAUDE.md`, `AGENTS.md`.
5. Thẻ `pha_12_14_san_xuat.md` của X-Economic: lấy bản Dòng Chảy, sửa các chỗ khác kênh (tiếng Anh, bảng màu noir).
6. Thu âm tiếng Anh và dựng phụ đề: cần chọn và kiểm giọng TTS tiếng Anh và hằng số tốc độ đọc tiếng Anh (khác 223–235 từ/phút của tiếng Việt; số này em chưa kiểm, giao agent đo trên giọng thật rồi ghi vào hiến pháp).

## 3. Phần cần sửa tay sau nhân bản (lớp riêng và khác biệt ngôn ngữ)

- **Quy trình hai giai đoạn (nếu giữ tiếng Anh):** Giai đoạn 1 duyệt bản Việt, Giai đoạn 2 dịch sang Anh. Thẻ Pha 7 cần thêm bước dịch và chuẩn "văn nói tiếng Anh". Quy tắc "Viết Câu Cho Tai" cần bản tiếng Anh (hiện đếm theo "tiếng" tiếng Việt, trần 150 ký tự là giới hạn TTS cần kiểm lại với giọng Anh).
- **Hằng số vận hành** (tốc độ đọc, trần chữ mỗi chương, ngân sách từ): tính lại cho tiếng Anh nếu chọn tiếng Anh.
- **Phân loại đề tài A/B/C** của Dòng Chảy (đời sống, doanh nghiệp quốc gia, quy luật lớn): xem lại cho khán giả Mỹ và Anh; bỏ `vietnam_macro_context.md`, thêm bối cảnh vĩ mô Mỹ, Anh, toàn cầu (có sẵn "macro context trước chủ đề" chung cho cả hai kênh, xem `memory`).
- **Persona:** giữ danh sách, sửa phần giọng và khán giả cho khớp X-Economy.
- **Registry:** chuyển registry cũ vào `_archive/`, tạo registry trống theo khuôn Dòng Chảy.
- **Quản lý:** `01_management/master_channel_analytics_audit.md` (là audit của GocNhinPodcast bị chép sang) chuyển đi; bỏ DNA nhân đôi ở `.claude/agents|commands|skills|rules|examples|specialist_map.md` (chỉ giữ `settings.json`, `settings.local.json`), đúng quy tắc "DNA chỉ nằm trong `.agents/`".

## 4. Các bước và chia việc cho agent Antigravity

Mọi bước dưới đây dùng phiếu theo chuẩn hiện hành (một phiếu một file, ngữ cảnh trước, nhiệm vụ sau, quyền sở hữu file rõ). Nên **hai đến ba agent** thay vì một: lỗi dồn việc về một agent đã gặp ở đợt vừa rồi.

| Bước | Việc | Agent | Phụ thuộc |
|---|---|---|---|
| B0 | Sao lưu cả thư mục `X-Economic` (kể cả `.claude/`) vào `/Users/pro16/VideoProject_backup/xe_chuan_hoa_20261006/`; ghi danh sách file. Đã có `X-Economic_backup` (bản cũ hơn) nhưng không thay được | A1 | |
| B1 | Nhân bản lớp khung từ Dòng Chảy theo bản đồ ở mục 1b (bằng lệnh `cp`/`rsync`, không viết lại bằng tay), không đụng lớp riêng; bản đồ file nào thuộc lớp nào ghi vào báo cáo | A1 | B0 |
| B2 | Hiến pháp mới `.agents/AGENTS.md` ≤ 11.000 bytes + `CLAUDE.md` 2 dòng `@` + 12 thẻ pha, từ bản Dòng Chảy, sửa phần kênh; bảng chuyển chỗ các mục của hiến pháp cũ (không mất ràng buộc cứng) | A1 | B1 |
| B3 | Lớp riêng: `channel_bible`, `voice_dna`, `content_principles`, `audience_personas`, `visual_style_guide` giữ và sửa cho nhất quán với khung mới; quy trình tiếng Anh hai giai đoạn trong thẻ Pha 7; hằng số tiếng Anh | A2 | B2 |
| B4 | Phần sản xuất (mục 2): thẻ Pha 12–14, workflow, skill `visual_prompter_plus`, lưu trữ script tự sinh cảnh, cổng khớp giờ, thu âm và phụ đề tiếng Anh | A3 | B2 |
| B5 | Dọn: `.claude/` nhân đôi, registry, audit chép nhầm, `.gitignore` (xem câu hỏi 3), mẫu tập `scripts/new_episode.sh` | A2 | B2 |
| B6 | Kiểm thật: một hội thoại Antigravity mới trong workspace X-Economic, đo `GocNhinPodcast/scripts/kiem_nap.py`; grep link gãy; so khung với Dòng Chảy (chỉ khác lớp riêng) | Claude | B2–B5 |
| B7 | **Phép thử sản xuất:** chọn một tập đã có kịch bản hay (đề xuất `vuong-mua-lpb`, trạng thái `completed`), dựng lại hình và tiếng theo quy trình mới, user nghe xem hình và tiếng khớp | A3 + user | B4 |

## 5. Việc cần user quyết trước khi giao

1. **Hướng kênh khi bật lại: ĐÃ CHỌN 06/10 (user đồng ý hướng A):** tiếng Việt, nhìn kinh tế và kinh tế chính trị thế giới và tác động tới Việt Nam. Việc chọn đề tài là quy trình của user, **không ghi vào DNA**: DNA chỉ mô tả kênh theo hướng tích cực (lane, khán giả, giọng, hình), không có danh sách đề tài cấm, không ghi lịch sử quyết định, không nhắc kênh khác. Hệ quả kỹ thuật: bỏ phần dịch hai giai đoạn và hằng số tiếng Anh vì không còn dùng.
2. **Gốc nhân bản:** đồng ý lấy Dòng Chảy làm gốc (em đề xuất) hay GocNhinPodcast?
3. **Thư mục:** `X-Economic` đang bị git bỏ qua. Em đề xuất đưa vào git (loại `.notebooklm_home`, `.venv_notebooklm`, `credentials`) để có lịch sử và kiểm tra; hai thư mục còn lại (`X-Economics`, `X-Economic_backup`) giữ nguyên, không đụng.
4. **Tập cũ:** lưu trữ registry rồi bắt đầu sạch (đề xuất), hay giữ làm backlog viết lại.
5. **Dựng lại video cũ để xin bật kiếm tiền:** có dựng lại các video đã đăng bằng quy trình mới (thay hình và tiếng khớp) trước khi nộp xét duyệt lại không? Đây là điều có thể quyết định kết quả xét duyệt, em muốn anh cân nhắc.

## 6. Rủi ro

- Nhân bản có thể mang theo thuật ngữ và ví dụ Việt Nam sang kênh tiếng Anh: B3 phải grep `Việt Nam`, `VND`, `ki lô mét`, mã DATA-XX Việt hóa.
- Hằng số tiếng Anh chưa kiểm: phải đo trên giọng thật, không đoán.
- Ba kênh dùng chung khung nên khi sửa khung phải áp đồng nhất (quy tắc 06/10: mọi thay đổi DNA áp cho các kênh trong cùng đợt).
- Chưa nạp xong sẽ lặp lỗi cũ: bước B6 dùng nhật ký thật chứ không tin agent tự khai.

## 7. Hình ảnh cho đề tài kinh tế chính trị (bổ sung 06/10, theo câu hỏi của user)

Nguyên tắc: **cho người xem thấy cơ chế và bằng chứng, không cho xem gương mặt lãnh đạo.** Dùng đúng 5 loại shot của Hợp đồng `i2v_nhip_y.md`, nhưng đổi tỷ trọng:
- `BAO_CHI`: văn bản, nghị định, thông cáo, trích dẫn có nguồn, ảnh chụp thật kèm đoạn nhấn (chính là "vật chứng" của khung chấm).
- `INFOGRAPHIC_DONG`: bản đồ chuyển động (tuyến vận tải, eo biển, dòng thuế quan, dòng vốn), đồ thị theo thời gian, so sánh "lời nói và số liệu". Hình chuyển động có chủ đích thay ảnh tĩnh, vừa là nhận diện "dữ liệu chuyển động" của kênh.
- `BROLL`: địa điểm và hạ tầng, không phải chân dung: cảng, container, nhà máy, trung tâm dữ liệu, trụ sở cơ quan nhìn từ ngoài, phiên họp quay toàn cảnh.
- `VIDEO_AI`: chỉ cho ẩn dụ cơ chế không có người thật; tuyệt đối không dựng video hay ảnh AI của người thật (Quy tắc cách ly an toàn I2V, `visual-asset-safety.md`).
- Phát biểu của lãnh đạo: đoạn ngắn từ nguồn chính thức hoặc có giấy phép, ghi rõ nguồn và mốc thời gian (`NGUON` url và timecode như quy chuẩn B-roll), hoặc thay bằng chữ trích dẫn có nguồn trên nền sạch; hình lưng, bục phát biểu, quốc huy, văn bản thay cho cận mặt.
- Bản đồ: giữ quy tắc bắt buộc Hoàng Sa, Trường Sa, Phú Quốc, Côn Đảo, cấm đường lưỡi bò; bản đồ thế giới có vùng tranh chấp dùng một quy ước thống nhất, ghi chú nguồn bản đồ.
- Pháp lý: mọi cáo buộc dẫn nguồn, phán xét cơ chế không phán xét động cơ cá nhân (`stance_and_judgment.md` §4).

Việc cần làm trong bước B4: quy chuẩn B-roll hiện có (`.agents/rules/broll-production-standard.md`) viết quanh VTV và VNEWS và 5 cụm bối cảnh Việt Nam. Cần phụ lục cho đề tài thế giới: cụm bối cảnh mới (trung tâm tài chính, ngân hàng trung ương và cơ quan nhà nước; cảng và tuyến vận tải; nhà máy bán dẫn và trung tâm dữ liệu; năng lượng; sản xuất ở Trung Quốc) và danh sách nguồn footage quốc tế được phép dùng (cơ quan chính phủ và tổ chức quốc tế công bố tự do, thư viện lưu trữ mở, kho stock có giấy phép). Mỗi nguồn kiểm điều khoản giấy phép trước khi đưa vào danh sách; không dùng lại hình của hãng tin chỉ để lồng tiếng. Lý do: kênh từng bị đánh dấu "sử dụng lại nội dung".
