# Production Notes — Bàn Giao Thành Phẩm Sẵn Sàng Xuất Bản

**Episode slug:** `vingroup-co-may-hoa-rong`
**Ngày bàn giao:** 2026-04-16

---

Tập phim này đã vượt qua toàn bộ 15 vòng kiểm duyệt biên tập nghiêm ngặt (Editorial Quality Gates). Dưới đây là biên bản bàn giao thành phẩm để tiến hành đóng gói Media và Xuất bản trên kênh YouTube.

## 1. Định hướng Giọng đọc (Voice Direction cho TTS/Human Narrator)
- **Mood chính:** Bình tĩnh, sắc lạnh, giọng phim tài liệu điều tra (Investigative Documentary). Không phán xét, không chọn phe ủng hộ hay phản đối.
- **Năng lượng:** Âm lượng đều đặn, hạ giọng ở những câu chốt hạ (VD: "Đây không phải trùng hợp. Đây là kiến trúc.").
- **Tempo:** Trung bình chậm. Ngắt nghỉ dứt khoát tại các dấu gạch nối (—) để tạo độ nghèn trước những thông tin nặng (VD: "Lịch sử không chỉ có Samsung. Lịch sử còn có Daewoo.").

## 2. Pacing Profile (Nhịp điệu hình ảnh toàn tập)
- Hook (Chương 1): Cực nhanh. 1 câu thoại = 1 cảnh (SC001-SC004). Mục tiêu là nhồi nhét visual vào mắt khán giả để chống trôi.
- Thân bài (Từ Chương 2): Chậm và chắc. Mạch cảm xúc kéo dãn sang nhịp độ "Historical review".
- Phân mảnh (Scene Parsing): Đã xuất 41 Prompts tĩnh theo chuẩn Modern Comic Book. Các Layer hình ảnh được đảo góc Focus tiên tục (Wide → Close-up → Low Angle). File: `image_prompts.txt` + `scene_timing_map.json`.

## 3. Pronunciation Watchlist (Từ khóa đọc cẩn thận)
- **Chaebol:** Đọc là "Che-bôn" (âm Hàn Quốc) hoặc "Chai-bôn" nếu tuỳ chỉnh TTS, cần nhất quán từ đầu đến cuối.
- **Keiretsu:** Đối ứng với "Kê-rết-sư".
- **Zaibatsu:** Đối ứng với "Dai-bát-sư".
- **Temasek:** Đọc gọn "Tê-ma-sếch".

## 4. Trạng thái Đóng Gói
- [x] **Kịch bản (Voiceover text):** Hoàn thiện và lưu tại `chapter_01.md` đến `chapter_08.md`. Đã đi qua The Voice Architect làm Oral QA.
- [x] **Thumbnail Direction:** Lưu tại `08_thumbnail_brief.md`. Typography "TẠI SAO LẠI LÀ VINGROUP?" 2 dòng cực đậm, ghép trên nền 2 nhân vật chân dung tỷ phú + lãnh đạo tối cao.
- [x] **SEO Meta Data:** Đã sẵn sàng tại `09_youtube_metadata.md` (Gồm Title SEO, Description CTA, Hashtags, Tags và **Comment ghim bắt buộc**).
- [x] **Báo cáo Render Video:** Đã render slideshow base từ thư mục ảnh `/Users/pro16/Downloads/vingroup` ra `episodes/vingroup-co-may-hoa-rong/video/slideshow_base.mp4` bằng `scripts/slideshow_video`, dùng `scene_timing_map.json`, `fps 30`, `transition 1s`, `seed 42`. Thời lượng đầu ra: 365 giây (~6 phút 05 giây). Trạng thái: completed.

## 5. Cảnh báo Pháp lý & An Toàn Tiền Tệ (Legal & Disclaimer)
- **Status:** **PASS** (100% tuân thủ `financial_boundaries.md`).
- Đây là video cực kỳ nhạy cảm liên quan đến các mã tài sản lớn trên sàn giao dịch và các cơ cấu chính sách của Đảng/Nhà Nước.
- TUYỆT ĐỐI không thay đổi bất kỳ câu chữ nào ở phần Disclaimer đầu chương 1 và kết chương 8.
- Kịch bản bóc tách dựa trên cấu trúc vĩ mô toàn cầu, không kích động, không có ý định bơm xả cổ phiếu VIC/VHM/VFS.

---

**→ END OF PHASE 15 AUTOMATION.** 
*Mọi quy trình của The AI System đã kết thúc xuất sắc. Chỉ chờ lệnh Manual Render từ Đạo Diễn Nhân Sự.*
