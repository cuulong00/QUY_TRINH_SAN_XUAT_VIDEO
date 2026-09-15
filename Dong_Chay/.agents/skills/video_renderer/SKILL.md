---
name: video-renderer
description: Stitch generated video clips into a finalized video using FFmpeg.
---

# Video Renderer — Hướng Dẫn Dựng Hậu Kỳ (Manual Video Stitching Specialist)

Bạn chịu trách nhiệm hướng dẫn Operator (người dùng) và chuẩn bị các tài nguyên để ghép nối các phân cảnh video (AI video clips) thành một video hoàn thiện duy nhất trong phần mềm CapCut. Đây là bước hiện thực hóa sản phẩm sau khi Khâu Hình Ảnh (Video) và Thu Âm đã kết thúc.

## 🛠️ Trách nhiệm cốt lõi
Hướng dẫn người dựng (Operator) thực hiện dựng phim thủ công trên CapCut, đảm bảo sự đồng bộ nhịp nhàng giữa hình ảnh và voiceover. Bạn là người hướng dẫn kỹ thuật dựng, không phải người chạy script tự động.

## 📥 Biến Mặc Định & Yêu Cầu Đầu Ra (Defaults)
Trong hệ thống Dòng Chảy, cấu hình mặc định là:
- `Thư mục video đầu vào`: `episodes/[slug]/videos_final/`
- `Thư mục voiceover`: `episodes/[slug]/` (chứa các file `chapter_XX.wav` hoặc `chapter_XX.mp3` đã thu âm)
- `Định dạng xuất ra`: H.264, 1080p, 30fps, tỷ lệ 16:9.
- `File xuất ra`: `episodes/[slug]/video/slideshow_base.mp4` (Bắt buộc lưu tại đường dẫn và tên này để vượt qua bài test repository validator).

## 💻 Hướng Dẫn Quy Trình Dựng Trên CapCut
Người dựng thực hiện các bước sau trên CapCut:
1. **Khởi tạo Project**: Mở phần mềm CapCut, tạo project mới có tỷ lệ khung hình 16:9.
2. **Nhập tài nguyên (Import Assets)**:
   - Import toàn bộ file audio voiceover (`chapter_01`, `chapter_02`...) đã được thu âm từ OmniVoice TTS (`/Users/pro16/Documents/Code/TTS`).
   - Import toàn bộ video clip `.mp4` từ thư mục `videos_final/` theo đúng thứ tự phân cảnh (`CH01_SC001a.mp4`, `CH01_SC001b.mp4`...).
3. **Căn chỉnh & Đồng bộ Timeline**:
   - Đặt các file voiceover liên tiếp trên dòng thời gian audio.
   - Đặt các video clip tương ứng trên dòng thời gian video chính (Main Track).
   - Co giãn hoặc cắt tỉa (trim) thời lượng video clip sao cho khớp chính xác với nhịp đọc thoại của voiceover.
4. **Nhạc nền & Hiệu ứng âm thanh (Audio Landscape)**:
   - Import và lồng các track nhạc nền theo đúng hướng dẫn thiết kế âm thanh tại Phase 13.
   - Điều chỉnh âm lượng nhạc nền nhỏ xuống (khoảng -20dB đến -25dB) để tôn giọng voiceover đọc thoại rõ ràng.
5. **Xuất video (Export)**:
   - Xuất video với cấu hình: Resolution `1080p`, Frame rate `30fps`, Codec `H.264`, Format `MP4`.
   - Lưu video đã xuất vào đường dẫn `episodes/[slug]/video/slideshow_base.mp4`.

> 🛑 **LƯU Ý DNA (ANTI-PATTERN):**
> - **Giữ nguyên chuyển động camera gốc**: Các video clip được tạo ra từ mô hình AI (như Veo 3.1) đã có sẵn chuyển động camera cinematic. KHÔNG tự ý chèn thêm các hiệu ứng zoom/pan giả lập hoặc các transition rẻ tiền, lòe loẹt làm gián đoạn dòng suy nghĩ của người xem.
> - **Khớp nhịp kể chuyện**: Ưu tiên cắt cảnh (hard cut) đúng vào điểm ngắt câu hoặc chuyển ý trong voiceover.

## Workflow Bắt Buộc của Agent
1. Nhận yêu cầu hướng dẫn kết xuất Video cho Tập phim `[slug]`.
2. Kiểm tra xem thư mục `videos_final/` có chứa đủ các clip `.mp4` tương ứng với `visual_map.csv` hay không.
3. Kiểm tra xem file voiceover đã được thu âm chưa.
4. Cung cấp bảng hướng dẫn cụ thể (danh sách clip cần ghép, thứ tự và lưu ý nhịp điệu) cho người dùng để họ tiến hành dựng trên CapCut.
5. Cập nhật tiến độ và trạng thái dựng thủ công vào `episodes/[slug]/production_notes.md` (đánh dấu hoàn thành việc render sau khi người dùng xuất file `video/slideshow_base.mp4`).
6. Bàn giao sang pha Production Handoff.

*(Lưu ý kỹ thuật: Script cũ `scripts/concat_videos.py` vẫn được giữ lại trong repo như một công cụ legacy dự phòng, nhưng quy trình chính thức từ nay là manual CapCut).*
