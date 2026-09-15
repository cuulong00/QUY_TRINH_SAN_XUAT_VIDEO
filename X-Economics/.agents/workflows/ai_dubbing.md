---
description: Tự động lồng tiếng (AI Dubbing) video bằng giọng nam Chirp3-HD/Neural2 hoặc Edge TTS khớp chuẩn trục thời gian từ phụ đề SRT.
---

# Quy trình Lồng tiếng tự động (AI Dubbing)

> **CẢNH BÁO MÔI TRƯỜNG & CHẠY NỀN:**
> - Bắt buộc dùng môi trường Python của dự án: `/Users/pro16/Documents/VideoProject/X-Economics/venv/bin/python3`.
> - Việc gọi API tổng hợp giọng nói và xử lý âm thanh FFmpeg mất 1-3 phút. Bắt buộc đặt `WaitMsBeforeAsync: 5000` (hoặc 10000) khi chạy để đẩy tiến trình xuống chạy nền, tránh đứng máy. Dùng `manage_task` để kiểm tra tiến độ.

1. Xác định `episode slug` hoặc vị trí lưu file phụ đề tiếng Anh SRT cùng video gốc của tập phim.
2. Thu thập các thông tin đầu vào bắt buộc:
   * `--srt-path`: Đường dẫn tới file phụ đề tiếng Anh `.srt` của video.
   * `--video-in`: Đường dẫn tới file video gốc.
   * `--voice`: Giọng đọc Google TTS Chirp3-HD (Mặc định: `vi-VN-Chirp3-HD-Alnilam`).
3. Khởi chạy tiến trình lồng tiếng chạy nền:

```bash
/Users/pro16/Documents/VideoProject/X-Economics/venv/bin/python3 -u scripts/tts/ai_dubbing.py \
  --slug "[slug]" \
  --srt-path "[path_to_srt]" \
  --video-in "[path_to_video]" \
  --voice "vi-VN-Chirp3-HD-Alnilam"
```

4. Theo dõi nhật ký tiến trình bằng `manage_task`.
5. **Duyệt bản dịch nháp (nếu cần)**: 
   * Nếu khóa API Google của bạn bị giới hạn dịch vụ dịch thuật (Gemini 403), script sẽ tạo một file JSON nháp tại `episodes/[slug]/dubbing_draft.json` và dừng lại.
   * Biên tập viên cần mở tệp này, điền các bản dịch tiếng Việt vào trường `text_vi` của mỗi phân đoạn, lưu lại và chạy lại lệnh ở Bước 3.
6. Khi hoàn tất, kiểm tra kết quả lồng tiếng tại:
   * Âm thanh hoàn chỉnh: `episodes/[slug]/dubbed_audio.wav`
   * Video thành phẩm lồng tiếng Việt: `episodes/[slug]/dubbed_video_final.mp4`
7. Bàn giao video thành phẩm cho User kiểm duyệt.
