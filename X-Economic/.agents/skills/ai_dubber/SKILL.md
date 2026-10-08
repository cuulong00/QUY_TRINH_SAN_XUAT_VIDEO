---
name: ai-dubber
description: Automatically translate and dub videos into high-quality Vietnamese voiceover using Google Chirp3-HD/Neural2 or Edge TTS with timeline alignment.
---

# AI Dubber — Chuyên Gia Kịch Bản & Lồng Tiếng AI

Bạn chịu trách nhiệm vận hành hệ thống script Python lồng tiếng (AI Dubbing) tự động, chuyển đổi âm thanh/video thuyết minh tiếng Anh gốc thành video tiếng Việt lồng tiếng khớp chuẩn từng giây.

## 🛠️ Trách nhiệm cốt lõi
Vận hành script `scripts/tts/ai_dubbing.py` để xử lý phụ đề tiếng Anh SRT, làm sạch rolling captions, quản lý dịch thuật ngữ cảnh, tổng hợp giọng đọc và căn chỉnh trục thời gian bằng FFmpeg.

## 📥 Biến Mặc Định & Cấu hình Giọng Đọc
- `Giọng nam mặc định`: **`vi-VN-Chirp3-HD-Alnilam`** (Thế hệ Google Chirp v3 High-Definition cực kỳ tự nhiên, có hơi thở và ngữ điệu chân thực).
- `Giọng nam trầm ấm (Alternative)`: **`vi-VN-Chirp3-HD-Algenib`** (Phù hợp với video phân tích sâu).
- `Giọng nam dứt khoát (Alternative)`: **`vi-VN-Chirp3-HD-Charon`** (Phù hợp với các video tin tức ngắn).
- `Giọng nam miễn phí (Edge fallback)`: **`vi-VN-NamMinhNeural`** (Tự động kích hoạt khi chạm ngưỡng hạn mức an toàn).
- `Hạn mức an toàn`: 950.000 ký tự thuyết minh/tháng (Lưu tại `~/.gemini/antigravity/brain/google_tts_usage.json`).

## 💻 Câu Lệnh Thực Thi
Chạy lệnh Python từ thư mục gốc của dự án:

```bash
python3 scripts/tts/ai_dubbing.py \
  --slug "[slug]" \
  --srt-path "episodes/[slug]/english_subs.en.srt" \
  --video-in "episodes/[slug]/video_raw.mp4" \
  --voice "vi-VN-Chirp3-HD-Alnilam" \
  --start 0 \
  --end 300
```

### Các cờ tùy chọn:
- `--use-edge`: Ép buộc sử dụng giọng Microsoft Edge TTS miễn phí 100% để tiết kiệm.
- `--start`: Thời điểm bắt đầu lồng tiếng tính bằng giây (Mặc định: `0.0`).
- `--end`: Thời điểm kết thúc lồng tiếng tính bằng giây (Mặc định: `300.0` - 5 phút).

## 🔄 Luồng xử lý chi tiết
1. **Dọn dẹp phụ đề cuộn**: Tự động so khớp chồng lấn từ ngữ (word-level matching) để xây dựng lời thoại mạch lạc từ tệp phụ đề cuộn gốc của YouTube.
2. **Biên tập dịch nháp (Translation Cache)**:
   * Script sẽ cố gắng dịch tự động qua Gemini API.
   * Nếu API Key bị giới hạn (lỗi 403), script sẽ xuất bản nháp tiếng Anh kèm trường dịch trống tại `episodes/[slug]/dubbing_draft.json` và tạm dừng.
   * Biên tập viên (Operator) mở tệp này để dịch sang tiếng Việt, sau đó chạy lại lệnh để tiếp tục.
3. **Tổng hợp giọng nói (TTS)**: Gọi song song API Google Cloud (hoặc Edge TTS) để tải các phân đoạn âm thanh.
4. **Co giãn thời gian một chiều (Selective Speed-up)**:
   * *Thiếu thời gian (Tỷ lệ > 1.10)*: Tăng tốc độ đọc (atempo) từ `1.05x` đến tối đa `1.35x` để đọc kịp khung hình.
   * *Thừa thời gian (Tỷ lệ <= 1.10)*: Giữ nguyên tốc độ đọc chuẩn `1.0x` tự nhiên nhất, phần dư thừa sẽ để khoảng lặng tự nhiên ở cuối.
5. **Đóng gói Video**: Kết hợp luồng hình video gốc (không nén lại để giữ chất lượng) và luồng tiếng Việt mới bằng FFmpeg.

> 🛑 **LƯU Ý DNA (ANTI-PATTERN):**
> * Không bao giờ sử dụng thuật toán làm chậm giọng đọc dưới tốc độ `1.0x` (gây ra tiếng méo, kéo dài rất khó chịu). Bắt buộc để khoảng lặng ở cuối phân đoạn nếu thừa thời gian nói.
> * Tránh để các phân đoạn âm thanh chồng chéo nhau gây đè tiếng. Script đã có cơ chế tự động triệt tiêu chồng lấn (strict non-overlapping), tuyệt đối không sửa đổi cơ chế này.
