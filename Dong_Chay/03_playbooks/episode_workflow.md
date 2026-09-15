# episode_workflow.md

Đây là quy trình chuẩn để tạo một video tài chính xuất sắc theo mô hình state-first và one-phase-at-a-time.

## Pha 1 — Topic Qualification
Mục tiêu: biến raw topic thành một góc đủ mạnh để đáng làm video.
Output: `01_topic_qualification.md`

Tiêu chí qua pha:
- pain đủ cụ thể
- có false belief đủ sắc để bóc
- có ít nhất vài hướng case study / data khả thi
- không cần clickbait hoặc buy/sell advice để hấp dẫn

## Pha 2 — Data Mining & Verification
Mục tiêu: khóa backbone dữ liệu và case study trước khi khóa luận điểm.
Output: `02_research_map.md`, khởi tạo `10_claim_ledger.md`

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

## Pha 4 — Hook Lab
Mục tiêu: chọn một góc khai thác và một hook đủ mạnh.
Output: `04_hook_pack.md`

Tiêu chí qua pha:
- có 1 hook final
- có title direction rõ
- có mini re-hooks đủ dùng cho phần giữa
- title và hook nói cùng một lời hứa

## Pha 5 — Thesis Map
Mục tiêu: khóa xương sống phân tích trước khi dựng retention và outline.
Output: `05_thesis_map.md`

Tiêu chí qua pha:
- thesis rõ
- anti-thesis đủ mạnh
- 3 open loops rõ
- sub-claims map được sang data / case / framework

## Pha 6 — Retention Map
Mục tiêu: thiết kế nhịp giữ người xem trước khi viết prose.
Output: `06_retention_map.md`

Tiêu chí qua pha:
- có ít nhất 2 analytical peaks
- có các re-hooks ở vùng dễ tụt retention
- biết đoạn nào cần tăng nhịp và đoạn nào cần nghỉ

## Pha 7 — Outline
Mục tiêu: khóa cấu trúc long-form trước khi viết.
Output: `07_outline.md`

Tiêu chí qua pha:
- mỗi chapter có nhiệm vụ phân tích khác nhau
- mỗi chapter có case study hoặc số liệu phải dùng
- bridge đủ rõ
- action plan không bị hòa tan vào các chapter khác

## Pha 8 — Chapter Briefs
Mục tiêu: biến outline thành brief cụ thể cho từng chapter.
Output: `08_chapter_briefs.md` đồng thời cập nhật `09_continuity_packet.md`

Tiêu chí qua pha:
- mỗi chapter biết rõ role trong toàn video
- biết phải dùng case/data nào
- biết phải tránh lặp gì

## Pha 9 — Chapter Writing
Mục tiêu: viết chương theo state, không drift.
Output: `chapter_XX.md`, cập nhật `09_continuity_packet.md`, `10_claim_ledger.md`

Sau mỗi chapter phải kiểm:
- có lặp case study cũ không
- có lặp số liệu cũ không
- có advance lập luận không
- bridge có kéo được sang chapter sau không
- có vi phạm financial safety không
- có ít nhất 1 case study hoặc số liệu thực tế không

## Pha 10 — Financial QA
Mục tiêu: khóa an toàn tài chính và độ trung thực của claim.
Output: `financial_qa.md`

Kiểm:
- disclaimer
- no buy/sell advice
- no profit promises
- no fabricated stats
- claim taxonomy đúng

## Pha 11 — Oral QA
Mục tiêu: đảm bảo script nghe được và có lực qua voice over.
Output: `oral_qa.md`

Kiểm:
- câu có dễ đọc không
- nhịp thở có ổn không
- số liệu có dễ nghe không
- phần giữa có đều đều quá không
- ending có đủ lực không

## Pha 12 — Visual Map
Mục tiêu: tạo visual logic theo từng khúc nghĩa của audio.
Output: `visual_map.csv`

Nguyên tắc:
- không dùng random footage
- ưu tiên biểu đồ, screen data, case study visuals
- hỗ trợ các đoạn hook và re-hook quan trọng
- đây là bước map logic hình ảnh, chưa phải render video cuối

## Pha 13 — Audio Landscape
Mục tiêu: thiết kế âm thanh và nhạc nền.
Output: audio direction trong kịch bản và ghi chú sản xuất.

Tiêu chí:
- Nhịp điệu âm nhạc phù hợp từng phân đoạn kể chuyện
- Phân định rõ các điểm drop, khoảng lặng đắt giá

## Pha 14 — Video Render (CapCut Stitching - Manual)
Mục tiêu: Dựng hậu kỳ và ghép nối các video clip thủ công trong phần mềm CapCut theo voiceover.
Input khuyến nghị: `episodes/[slug]/videos_final/`
Output khuyến nghị: `episodes/[slug]/video/slideshow_base.mp4`

Cách thực hiện:
- Nhập (import) toàn bộ video clip `.mp4` từ thư mục `videos_final/` vào CapCut.
- Cắt ghép, căn chỉnh thời lượng từng phân cảnh khớp hoàn hảo với nhịp điệu của file voiceover đã thu âm.
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
- đường dẫn thư mục ảnh final và file slideshow render nếu đã có

## Pha 16 — Postmortem
Mục tiêu: biến episode thành dữ liệu học cho repo.
Output: `postmortem.md`

Sau khi hoàn tất:
- cập nhật `01_management/episode_registry.csv`
- ghi bài học vào `01_management/lessons_learned.md`
- nếu pattern đủ mạnh, cập nhật file lõi tương ứng

## Pha 17 — Performance Review
Mục tiêu: Đánh giá chỉ số thực tế sau khi video lên sóng để tối ưu hóa kịch bản tiếp theo.
Output: Cập nhật `01_management/performance_benchmarks.md`
