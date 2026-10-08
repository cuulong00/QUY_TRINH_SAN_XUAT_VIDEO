# episode_workflow.md

Đây là quy trình chuẩn để tạo một video tài chính xuất sắc theo mô hình state-first và one-phase-at-a-time.
Danh sách Pha dưới đây đồng bộ nguyên văn với "Cấu trúc làm việc bắt buộc (16 Pha)" trong `CLAUDE.md` — không định nghĩa lại số pha khác ở đây.

## Pha 0 (tùy chọn) — Qualify Topic
Mục tiêu: biến raw topic thành một góc đủ mạnh để đáng làm video, trước khi dựng Global Vision.
Output: `01_topic_qualification.md`

Tiêu chí qua pha:
- pain đủ cụ thể
- có false belief đủ sắc để bóc
- có ít nhất vài hướng case study / data khả thi
- không cần clickbait hoặc buy/sell advice để hấp dẫn

## Pha 1 — Master Systemic Topography & Global Vision
Mục tiêu: dựng Bàn cờ 4 Tầng + Ma trận 4 Lăng kính + Prompt 5 Phản biện cho toàn tập.
Output: `01_global_vision_synthesis.md`

## Pha 2 — Topographical Deep Research
Mục tiêu: khóa backbone dữ liệu, case study và Contested Data & Trade-offs Ledger trước khi khóa luận điểm.
Output: `02_research_map.md`, `02_research_plan.md`, `02_research_synthesis.md`

Tiêu chí qua pha:
- có verified data đủ dùng
- có case studies đủ mạnh
- claim trung tâm không chỉ dựa vào opinion
- biết chỗ nào còn yếu và phải hạ cấp phát biểu

## Pha 3 — Strategy Brief
Mục tiêu: hiểu đúng người xem và lời hứa insight tài chính.
Output: `03_brief.md`

Tiêu chí qua pha:
- pain tài chính đủ cụ thể
- promise đủ rõ (insight + action plan)
- tone đúng kênh (sắc, logic, có data)
- biết rõ video này không nên drift sang đâu

## Pha 4 — Master Outline Engine
Mục tiêu: khóa xương sống biện chứng Hegel (Thesis → Antithesis [The Devil's Chapter] → Synthesis), nhịp giữ chân và cấu trúc long-form trước khi viết prose.
Output: `07_outline.md`

Tiêu chí qua pha:
- thesis rõ, anti-thesis đủ mạnh, có synthesis
- mỗi chapter có nhiệm vụ phân tích khác nhau, có case study hoặc số liệu phải dùng
- có cao trào phân tích (analytical peaks) và re-hooks tại các điểm chuyển màn kịch bản
- bridge đủ rõ; action plan không bị hòa tan vào các chapter khác

## Pha 5 — Hook Lab
Mục tiêu: chọn một góc khai thác và một hook đủ mạnh.
Output: `04_hook_pack.md`

Tiêu chí qua pha:
- có 1 hook final
- có title direction rõ
- có mini re-hooks đủ dùng cho phần giữa
- title và hook nói cùng một lời hứa

## Pha 6 — Chapter Briefs & Narrative State Tracker
Mục tiêu: biến outline thành brief cụ thể cho từng chapter (20 Trường: dữ liệu + nhịp chuyện + Steelman & Trade-offs) và khởi tạo sổ cái tự sự.
Output: `08_chapter_briefs.md`, `09_narrative_state_tracker.md`

Tiêu chí qua pha:
- mỗi chapter biết rõ role trong toàn video
- biết phải dùng case/data nào
- biết phải tránh lặp gì

## Pha 7 — Chapter Writing
Mục tiêu: viết chương theo state, không drift. Anti-Token Syntax Ban, Steelman 3 nhịp.
Output: `chapter_XX.md`, cập nhật `09_narrative_state_tracker.md`

Sau mỗi chapter phải kiểm:
- có lặp case study cũ không
- có lặp số liệu cũ không
- có advance lập luận không
- bridge có kéo được sang chapter sau không
- có vi phạm financial safety (`00_core/financial_boundaries.md`) không
- có vật chứng, case study hoặc số liệu thực tế làm điểm tựa nhận thức không

## Pha 8 — Merge Voiceover
Mục tiêu: gộp toàn bộ chapter thành một bản voiceover liền mạch.
Output: `voiceover.md`

## Pha 9 — Retention Bridge Audit
Mục tiêu: soi giữ chân, kiểm tra các mốc re-hook và nhịp tụt retention trên bản voiceover hoàn chỉnh.
Output: `retention_bridge_audit.md`

## Pha 10 & 11 — Editorial, Compliance & Dialectical Audit
Mục tiêu: khóa an toàn tài chính/pháp lý, phân loại taxonomy claim, và kiểm định Oral QA + Dialectical Rigor & Bias Audit (25%).
Output: `10_compliance_report.md`

Kiểm:
- disclaimer bắt buộc: "Nội dung chia sẻ luận điểm khách quan, mang tính thảo luận và xây dựng"
- no buy/sell advice, no profit promises, no fabricated stats
- taxonomy đúng 3 lớp: `verified_data` / `market_analysis` / `opinion_commentary`
- câu có dễ đọc, nhịp thở ổn, số liệu dễ nghe qua voiceover
- dialectical rigor: The Devil's Chapter đủ sắc, không thiên vị 1 chiều

## Pha 12 — Visual Storyboard & I2V Prompts / I2V+ Multimodal (chỉ khi có yêu cầu)
Mục tiêu: tạo visual logic theo từng khúc nghĩa của audio.
Output (nhánh Classic I2V): `visual_storyboard_blueprint.md`, `chapter_XX_visual.md`, `prompts_chapter_XX.txt`
Output (nhánh I2V+ Flagship, đang dùng cho các episode gần nhất): `visual_storyboard_blueprint_plus.md`, `chapter_XX_visual_plus.md`, `broll_manifest_chapter_XX.json`, `infographics_manifest_chapter_XX.json`, `prompts_chapter_XX_veo.txt`, `prompts_chapter_XX_infographics.txt`

Nguyên tắc:
- không dùng random footage
- ưu tiên biểu đồ, screen data, case study visuals
- hỗ trợ các đoạn hook và re-hook quan trọng
- đây là bước map logic hình ảnh, chưa phải render video cuối
- TUYỆT ĐỐI CẤM dùng code/script ghép từ khóa tự động để sinh prompt — phải qua suy luận nghệ thuật của LLM (xem `.agents/rules/visual-asset-safety.md`)

## Pha 13 — Audio Landscape (chỉ khi có yêu cầu)
Mục tiêu: thiết kế âm thanh và nhạc nền.
Output: audio direction trong kịch bản và ghi chú sản xuất.

Tiêu chí:
- Nhịp điệu âm nhạc phù hợp từng phân đoạn kể chuyện
- Phân định rõ các điểm drop, khoảng lặng đắt giá

## Pha 14 — Video Rendering & Assembly (chỉ khi có yêu cầu)
Mục tiêu: Dựng hậu kỳ và ghép nối các video clip theo voiceover dựa trên quy trình I2V+ hiện hành.
Input khuyến nghị: `episodes/[slug]/videos/` (thư mục di sản `videos_final/` cho episode cũ)
Output khuyến nghị: `episodes/[slug]/video/slideshow_base.mp4`

Cách thực hiện:
- Nhập (import) toàn bộ video clip `.mp4` từ thư mục `videos/` vào công cụ dựng chuẩn hoặc phần mềm NLE.
- Cắt ghép, căn chỉnh thời lượng từng phân cảnh khớp hoàn hảo với nhịp điệu của file audio đã thu âm.
- Lồng nhạc nền theo sơ đồ Audio Landscape đã thiết lập ở Pha 13.
- Xuất video base hoàn chỉnh với định dạng 1080p, 30fps, codec H.264, tỷ lệ 16:9 và lưu vào đường dẫn `video/slideshow_base.mp4` để phục vụ các bước kiểm tra tiếp theo.

Tiêu chí qua pha:
- Thư mục video có đủ video clip hợp lệ (`.mp4`).
- Căn chỉnh khớp chính xác nhịp kể chuyện và voiceover.
- Xuất thành công ra file `video/slideshow_base.mp4`.
- Nhật ký dựng và thông số được ghi nhận vào `production_notes.md`.
- Biết rõ đây là video base (đã ghép voiceover và nhạc nền cơ bản), chưa phải bản publish cuối nếu cần hiệu chỉnh thêm.

## Pha 15 — Production Handoff
Mục tiêu: bàn giao đầy đủ cho editor / narrator / producer.
Output: `production_notes.md`

Nội dung nên có:
- voice direction
- pacing profile
- asset requests
- packaging notes
- legal / caution notes
- đường dẫn thư mục video final và file slideshow render nếu đã có

## Pha 16 — Postmortem
Mục tiêu: biến episode thành dữ liệu học cho repo.
Output: `postmortem.md`

Sau khi hoàn tất:
- cập nhật `01_management/episode_registry.csv`
- ghi bài học vào `01_management/lessons_learned.md` nếu tồn tại
- nếu pattern đủ mạnh, cập nhật file lõi tương ứng

## Pha 17 (tùy chọn) — Performance Review
Mục tiêu: Đánh giá chỉ số thực tế sau khi video lên sóng để tối ưu hóa kịch bản tiếp theo.
Output: Cập nhật `01_management/performance_benchmarks.md` nếu tồn tại
