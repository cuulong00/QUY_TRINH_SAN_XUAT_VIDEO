---
description: BƯỚC BẮT BUỘC để thu âm TTS. Record the final voiceover using VBEE TTS API after script approval (từ chapter_XX.md).
---

# Quy trình Thu âm (Record Voiceover)

> **CẢNH BÁO QUAN TRỌNG VỀ MÔI TRƯỜNG & CHẠY NỀN:**
> - KHÔNG BAO GIỜ dùng lệnh `node` trần, vì môi trường ảo có thể lỗi `command not found`. Bắt buộc dùng đường dẫn tuyệt đối: `/opt/homebrew/bin/node` (hoặc `/usr/local/bin/node`).
> - Script thu âm phải lấy dữ liệu từ API và tải audio, mất 2-5 phút. Bắt buộc đặt `WaitMsBeforeAsync: 2000` (hoặc 5000) khi gọi `run_command` để đẩy tiến trình xuống chạy nền, tránh đứng máy. Dùng `command_status` để kiểm tra tiến độ.

1. Hỏi User `episode slug` nếu chưa biết.
2. Kiểm tra xem các file `episodes/[slug]/chapter_XX.md` đã tồn tại và đã được nghiệm thu (Oral Polish) hay chưa.
3. **Lựa chọn giọng đọc và công cụ (BẮT BUỘC):**
   * **Nếu người dùng không nói gì hoặc yêu cầu chung:** Sử dụng mặc định công cụ **Google Gemini TTS**.
   * **Hiển thị danh sách giọng đọc** cho người dùng chọn trước khi bắt đầu:
     1. **Algenib** (Trầm ấm - Tài liệu - Khuyên dùng)
     2. **Fenrir** (Siêu trầm - Kịch tính)
     3. **Alnilam** (Cân bằng - Giáo dục)
     4. **Puck** (Thân thiện - Trò chuyện)
     5. **Charon** (Trẻ trung - Tin tức nhanh)
   * Chờ người dùng phản hồi lựa chọn giọng đọc (ví dụ: "chọn Algenib" hoặc số "1").
4. **Kích hoạt lệnh thu âm tương ứng:**
   * **Với Google Gemini TTS (Mặc định):**
     Run command:
     ```bash
     ./venv/bin/python3 scripts/tts/gemini_tts_record.py [slug] --voice [tên_giọng_đã_chọn]
     ```
   * **Với VBEE TTS (Chỉ khi người dùng yêu cầu rõ):**
     Run command:
     ```bash
     /opt/homebrew/bin/node scripts/tts/record_episode.js [slug]
     ```
5. Theo dõi đầu ra bằng `command_status` cho đến khi báo cáo kết thúc.
6. Kiểm tra kết quả trong `episodes/[slug]/audio/`. Nếu trong báo cáo có chunk nào bị lỗi (failed), khởi chạy lại lệnh ở Bước 4. (Script sẽ tự động bỏ qua các file đã tải thành công và chỉ thu lại những file bị lỗi).
7. Báo cáo cho User sau khi đảm bảo thư mục audio đã có đủ các file phân đoạn (.wav hoặc .mp3) và `recording_report.json`.
8. Tiến hành nhắc User việc sử dụng FFmpeg để ghép Audio / Video Slideshow ở bước tiếp theo.
