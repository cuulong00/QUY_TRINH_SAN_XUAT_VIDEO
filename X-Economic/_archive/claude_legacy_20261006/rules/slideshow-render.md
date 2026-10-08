# slideshow-render (CapCut - Manual)

Áp dụng cho render phase.

## Preconditions
- Chỉ thực hiện sau khi đã có `visual_map.csv` và thư mục video clips final (`videos_final/`) đã được sắp xếp đúng thứ tự, kèm theo voiceover audio.
- Input khuyến nghị: `episodes/[slug]/videos_final/` (và thư mục di sản `images_final/` nếu có)
- Output khuyến nghị: `episodes/[slug]/video/slideshow_base.mp4`

## Must do
- Thực hiện dựng hậu kỳ thủ công trong CapCut (không chạy script tự động).
- Căn chỉnh khớp chính xác nhịp kể chuyện và voiceover.
- Ghi lại cấu hình xuất (1080p, 30fps, H.264) và trạng thái dựng vào `production_notes.md`.
- Sau khi xuất file thành công vào `video/slideshow_base.mp4`, cập nhật `01_management/episode_registry.csv`.
- Dừng lại để user duyệt video base trước khi handoff.

## Must not do
- Không dựng khi chưa có video clip final và voiceover.
- Không coi video base là bản publish cuối nếu chưa ghép nhạc nền và hiệu chỉnh nâng cao.