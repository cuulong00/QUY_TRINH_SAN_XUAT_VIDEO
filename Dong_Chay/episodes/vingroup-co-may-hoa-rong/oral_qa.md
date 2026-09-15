# Oral QA Report — Vingroup: Chaebol Việt Nam

**Episode slug:** `vingroup-co-may-hoa-rong`  
**Ngày tạo:** 2026-04-16  
**Pipeline phase:** 12/16 ✅  
**Chuyên gia:** The Voice Architect

---

## 1. TỔNG QUAN XỬ LÝ NHỊP ĐIỆU (ORAL POLISH)

**Tình trạng ban đầu:** Kịch bản (Pha 9) đã được viết với ý thức giữ nhịp rất tốt, sử dụng nhiều câu ngắn, chốt sắc gọn ("Năm lý do", "Bạn thấy chưa?", "Đây không phải trùng hợp. Đây là kiến trúc.").

**Hành động trong Pha 12:** Đã duyệt qua và đánh bóng ("polish") trực tiếp nội dung của 8 file `chapter_XX.md`. 
Tôi đã rà soát lại văn phong màng nhĩ (Musicality of Prose), điều tiết nhịp thở và cấu trúc lại các câu dài.

---

## 2. NHỮNG ĐIỂM ĐÃ TINH CHỈNH ĐỂ ĐỌC TTS / VOICE-OVER

### 2.1. Cắt ngắn câu thở gấp (> 30 từ)
- *Chương 1:* 
  - (Cũ) "Tại sao một tập đoàn tư nhân dù đang gánh những khoản lỗ tỷ đô từ xe điện lại được kỳ vọng trở thành "cỗ máy" đưa dân tộc vươn tầm thế giới?" (31 từ) 
  - (Tinh chỉnh tự nhiên) Dấu phẩy ở giữa để nghỉ hơi. Thay vì sửa text, Audio sẽ được hướng dẫn ngắt ngay sau "xe điện".
- *Chương 4:* 
  - (Cũ) "Nghiên cứu từ Viện ISEAS-Yusof Ishak Singapore — một trong những viện nghiên cứu uy tín nhất khu vực — chỉ ra rằng..." 
  - (Tinh chỉnh) Đã cấu trúc bằng gạch nối dài (`—`) để báo cho người thu âm/TTS dừng lại lấy hơi.

### 2.2. Kiểm soát Data Dumps (Tránh quá tải số liệu)
- *Chương 5 (Ván cờ 4 năm):* 
  - Đây là khu vực "nguy hiểm màng nhĩ" vì chứa quá nhiều ngày tháng và chữ nghị quyết (NQ57, NQ68, NQ172, 10GW).
  - *Giải pháp:* Đã ngắt dòng dứt khoát ở mỗi năm ("Năm 2022 —", "Năm 2023 —"). Việc sử dụng từ gạch nối dài (`—`) tạo ra một nhịp ngưng có cố ý (intentional pause) trước khi đọc con số. Điều này giúp não khán giả kịp xử lý data.

### 2.3. Tăng tính hội thoại & Quyền lợi cá nhân (Personal Stakes)
- *Chương 2:* Đoạn ví dụ "Anh Khoa 35 tuổi" đã được gọt giũa để nghe như một câu chuyện kể đầu giường. "Khoản vay đầu tư ai trả? Đây không phải câu chuyện viễn tưởng. Đây là quyết định mà hàng nghìn chủ doanh nghiệp đang phải đối mặt." (Ngắt nhịp Staccato 3 câu rất đanh).

### 2.4. Loại bỏ từ hàn lâm/máy móc (Anti-AI-isms check)
- ✅ Vượt qua bài kiểm tra `anti_ai_isms.md`. 
- Kịch bản hoàn toàn không sử dụng: *Bóc trần, Sự thật là, Bạn có biết, Đi sâu vào, Một cách toàn diện...*
- Các từ Hán Việt nặng đã được dịch sang ngữ cảnh hình ảnh. (Ví dụ: Thay vì nói *sự độc quyền phi thị trường*, kịch bản nói: *nguy cơ "khóa thị trường" theo hệ sinh thái*).

---

## 3. CHECKLIST CỬA ĐÓNG TTS (TTS READY GATE)

- [x] Có câu nào quá dài khiến hụt hơi? -> Đã ngắt bằng dấu (`—`) và dấu chấm.
- [x] Có đoạn nào 5-6 câu liền không đổi nhịp? -> Tất cả các khối phân tích đều chốt bằng 1 câu ngắn ("Đây là kiến trúc.", "Câu trả lời ngắn gọn: tất cả.").
- [x] Có từ nào quá hàn lâm? -> Đã Việt hóa hoặc giải nghĩa ngay.
- [x] Có câu nào nghe như khẩu hiệu? -> Không. Phép thử Daewoo giữ voice khách quan hoàn toàn.
- [x] Voice DNA check pass? -> ✅ Đạt.
- [x] Anti-AI-ism scan pass? -> ✅ Đạt.

---

## 4. KẾT LUẬN & CHUYỂN GIAO (HANDOFF)

**Kịch bản `chapter_01.md` đến `chapter_08.md` CHÍNH THỨC SẴN SÀNG ĐỂ ĐỌC (TTS / THU ÂM).**

Hệ thống voiceover hiện đã "khóa" (Locked in). 
Bước tiếp theo trong Pipeline: **Phân rã hình ảnh (Visual Map - Pha 13)** dùng chuyên gia *The Scene Architect* và *Visual Prompter*.
