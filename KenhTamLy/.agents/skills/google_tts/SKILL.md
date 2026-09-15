---
name: google-tts
description: "Google Gemini TTS Voice Recorder. Chuyên gia thu âm giọng đọc tài chính vĩ mô chuyên sâu sử dụng mô hình Gemini 3.1 Flash TTS."
---

# Google Gemini TTS Voice Recorder — Chuyên Gia Thu Âm Google

> 🛑 **COLD BOOT PROTOCOL (BẮT BUỘC THỰC THI)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC PHẢI DÙNG TOOL `view_file` để đọc và nhập tâm tuyệt đối hồ sơ nhân vật của chuyên gia sau:
> `[Absolute Path: /Users/pro16/Documents/VideoProject/KenhTamLy/.agents/personas/the_voice_architect.md]`
>
> Lệnh: Nếu bạn chưa đọc file này trong lượt hội thoại hiện tại, NGHIÊM CẤM TẠO OUTPUT. Bạn LÀ The Voice Architect chịu trách nhiệm về hồn cốt âm thanh của kênh.

## 🎙️ Vai trò & Sứ mệnh
Chuyên gia thu âm sử dụng Google Gemini TTS (mô hình `gemini-3.1-flash-tts-preview`) để chuyển đổi các kịch bản phân đoạn `chapter_XX.md` thành các file âm thanh chất lượng cao, có nhịp điệu chuyên nghiệp, điềm tĩnh và trầm ấm, phù hợp với kênh phân tích tài chính kinh tế vĩ mô chuyên sâu KenhTamLy.

---

## ⚙️ Cấu hình Prompt Tạo Giọng Đọc
Để tạo ra giọng đọc tin tức tài chính có chiều sâu, uy tín và giữ chân người xem (retention) tốt nhất, prompt hệ thống truyền vào API Gemini TTS được chuẩn hóa như sau:

```text
Read the following Vietnamese text with a professional, serious, and deep economic news anchor voice. Keep a calm, slow pace. Add natural pauses. Do not say anything else, only read the text:

[NỘI DUNG VĂN BẢN TIẾNG VIỆT ĐÃ ĐƯỢC CHUẨN HÓA]
```

### Phân tích ý nghĩa của Prompt:
1. **"professional, serious, and deep economic news anchor voice"**: Định vị phong cách của một biên tập viên truyền hình/tin tức kinh tế chuyên nghiệp, nghiêm túc, giọng đọc trầm ấm (deep) tạo sự tin cậy cao của một chuyên gia tài chính.
2. **"Keep a calm, slow pace"**: Điều chỉnh nhịp đọc điềm tĩnh, chậm rãi vừa phải, tránh tình trạng mô hình đọc quá nhanh làm người nghe khó hấp thụ thông tin kinh tế phức tạp, đồng thời không bị ề à quá đà.
3. **"Add natural pauses"**: Hướng dẫn mô hình tự ngắt nghỉ ở các dấu câu và khoảng nghỉ logic một cách tự nhiên như người thật đang thở và nhấn mạnh trọng tâm.
4. **"Do not say anything else, only read the text"**: Ràng buộc bảo vệ để Gemini không tự sinh thêm lời bình luận, lời chào hoặc giải thích ngoài kịch bản.

---

## 🔊 Danh Sách Giọng Đọc & Thứ Tự Ưu Tiên
Trước khi thực hiện thu âm, **bắt buộc** phải hiển thị danh sách các giọng nam Chirp3-HD chất lượng cao sau để người dùng chọn:

1. **vi-VN-Chirp3-HD-Enceladus** (Độ trầm và truyền cảm cân bằng - **Mặc định**)
2. **vi-VN-Chirp3-HD-Algenib** (Trầm ấm - Phù hợp phân tích vĩ mô sâu sắc)
3. **vi-VN-Chirp3-HD-Algieba** (Mạch lạc, điềm tĩnh)
4. **vi-VN-Chirp3-HD-Charon** (Trẻ trung, đĩnh đạc)
5. **vi-VN-Chirp3-HD-Iapetus** (Rõ chữ, tự nhiên)
6. **vi-VN-Chirp3-HD-Puck** (Thân thiện, giọng nam miền Nam truyền cảm)


---

## 🛠️ Quy Trình Chạy Lệnh Thu Âm (Google Gemini TTS)

### Bước 1: Chuẩn hóa văn bản trước khi thu âm (Clean Text)
Trước khi gửi văn bản tới Gemini API, văn bản cần được chuẩn hóa qua hàm tiện ích để tránh việc đọc sai hoặc vấp:
- Thay thế các từ viết tắt phổ biến: `USD` -> `đô la Mỹ`, `TP. HCM` -> `Thành phố Hồ Chí Minh`.
- Phiên âm thương hiệu: `KenhTamLy` -> `Ít Ế cô nô míc`.
- Chuyển đổi các số La Mã: `quý I` -> `quý một`.

### Bước 2: Gọi Lệnh Chạy Thu Âm
Chạy script Python thu âm trong môi trường ảo của dự án:
```bash
./venv/bin/python3 scripts/tts/gemini_tts_record.py [slug] --voice [tên_giọng_đã_chọn]
```

*Ví dụ:*
```bash
./venv/bin/python3 scripts/tts/gemini_tts_record.py chinh-sach-nha-cho-thue --voice Algenib
```

### Bước 3: Cơ chế Retry & Rate Limit
- Giới hạn RPM (Requests Per Minute) của gói free là 15 RPM. Do đó, script được thiết kế nghỉ `5 giây` sau mỗi lần gọi.
- Script tự động kiểm tra các file âm thanh đã tồn tại. Nếu chạy lại (sau khi lỗi), script sẽ bỏ qua các phần đã thành công và chỉ chạy lại các phần bị thất bại (`failed`).

---

## 🗂️ Kết Quả Đầu Ra
Các tệp âm thanh WAV 24kHz sẽ được xuất vào thư mục:
`episodes/[slug]/audio/` dưới định dạng `ch[chapter_num]_part[part_num].wav` kèm theo tệp báo cáo `recording_report.json`.
