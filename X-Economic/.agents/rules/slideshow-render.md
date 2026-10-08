# slideshow-render (dựng video từ clip)

Áp dụng cho khâu ghép clip thành video chương và video tập. **Đường chuẩn là quy trình dựng I2V+** ở `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_dung_video.md` (render lô infographic, ghép chương `ghep_chuong.py`, ghép tập `ghep_tap_phim.py`, nền động). Dựng thủ công trên phần mềm dựng phim chuyên nghiệp (NLE) chỉ còn là đường dự phòng khi công cụ chuẩn lỗi.

## Preconditions
- Có `chapter_XX_manifest.json` (xuất từ `kiem_nhip.py`), audio `audio/chapter_XX.wav` và Whisper mới hơn `chapter_XX.md`, và các clip final của chương (infographic, báo chí, broll, video AI).
- Tập có `nen_dong.json` (một tập một màu nền) nếu dùng nền động.

## Must do
- Chạy bốn lệnh theo quy trình chuẩn; mỗi lệnh đồng bộ, in `KET_QUA:`, đọc audio trực tiếp và in sha256.
- Xuất `episodes/[slug]/video/` (ví dụ `CHxx_full.mp4`, `tap_phim_hoan_chinh.mp4`, `muc_luc_chuong.txt`); ghi cấu hình xuất (1080p, 30 fps, CRF 18, H.264) và trạng thái vào `production_notes.md`.
- Sau khi xuất thành công, cập nhật `01_management/episode_registry.csv` (bằng Edit/Write) và dừng cho user duyệt video base trước khi handoff.
- Dọn file trung gian theo mục 8 của quy trình chuẩn sau khi user duyệt.

## Must not do
- Không dựng khi chưa có clip final và voiceover.
- Không `sleep`, không chạy nền rồi chờ, không tự đổi màu nền giữa các chương của một tập.
- Không coi video base là bản publish cuối nếu chưa ghép nhạc nền và hiệu chỉnh nâng cao.
- Dùng phần mềm dựng phim NLE (đường dự phòng) thì ghi rõ lý do vào `production_notes.md`.
