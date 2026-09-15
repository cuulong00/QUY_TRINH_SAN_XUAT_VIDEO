# Giao Thức Viết Kịch Bản Chống Trượt Ý (Anti-Drift Writing Protocol)

Tài liệu này là **"Vòng kim cô" (Bộ quy tắc bắt buộc)** áp dụng cho trợ lý AI (LLM) mỗi khi được yêu cầu chắp bút viết bất kỳ chương nào của kịch bản. Trước khi viết bài, AI bắt buộc phải đối chiếu và tuân thủ tuyệt đối 4 nguyên tắc sau:

## 1. Nguyên Tắc Cuốn Chiếu (Cấm Viết Một Mạch)
- **Luật:** Không bao giờ tự ý viết toàn bộ 6 chương cùng lúc.
- **Thực thi:** Chỉ viết duy nhất 1 chương được yêu cầu (không gò bó độ dài, viết cho đến khi diễn đạt đủ độ sâu và cảm xúc). Phải chờ User đọc, nhận xét, và cấp quyền "Duyệt" thì mới được phép chuyển sang viết chương tiếp theo.

## 2. Cổng Nạp Bối Cảnh (Context Priming Gate)
Trước khi thả phím viết một chương mới, AI bắt buộc phải:
- **Nạp DNA và Skill Chuyên Gia:** Đọc lại các quy tắc cốt lõi của kênh (Channel DNA trong `AGENTS.md`) và hướng dẫn kỹ năng chuyên gia tại `.agents/skills/chapter_writer/SKILL.md` để đồng bộ đúng tư duy, giọng điệu của một Đạo diễn Kịch bản Kinh tế Chính trị.
- **Đọc lại Toàn bộ Kho Nghiên Cứu:** Quét lại các tệp tài liệu trong thư mục `vault/` (đặc biệt là `bao-cao-phan-bien.md` hoặc các báo cáo về Malaysia/ICOR) để bơm đầy số liệu, bằng chứng lịch sử và chiều sâu vĩ mô vào bộ nhớ. Tuyệt đối cấm viết suông thiếu thực chứng.
- **Đọc lại** `implementation_plan.md` để nhớ vị trí của chương đó trong tổng thể chiến lược.
- **Đọc lại** bảng "Từ Điển Ví Von" trong `nguyen-tac-cot-loi-kich-ban.md` để đảm bảo sử dụng ít nhất 1-2 hình ảnh đắt giá (như "máy chạy bộ", "cỗ xe hành chính", "lỡ chuyến tàu") vào đúng ngữ cảnh.
- **Đọc lại** nội dung của chương liền kề trước đó (nếu có) để khớp nối mượt mà nhịp điệu và cảm xúc.

## 3. Luật Ngôn Ngữ & Nhịp Điệu Âm Nhạc (Spoken-Word Rhythm)
- **Tư duy:** Đây không phải bài báo hay văn bản hành chính. Đây là một bài diễn thuyết (Monologue) phát ra từ miệng con người.
- **Kỹ thuật Nhịp điệu (Sentence Variation):** Tuyệt đối cấm viết toàn bộ các câu sàn sàn giống nhau. Phải thiết kế câu như một bản nhạc:
  - **Dòng chảy (Flow):** Dùng những câu dài khoảng 15-25 từ để giải thích bối cảnh, lướt êm và dẫn dắt logic.
  - **Nhát dao (Punchline):** Bất ngờ chèn vào những câu cực ngắn (chỉ 4-8 từ) để ghim chặt cảm xúc, tạo điểm ngắt nghỉ sắc lẹm (Ví dụ: *"Nhưng không."*, *"Đó là sự tự sát."*, *"Họ đã lỡ tàu."*).
- **Cấm:** Cấm sử dụng các câu ghép nhồi nhét quá nhiều mệnh đề rườm rà khiến người đọc voice-over bị tắt thở.

## 4. Tự Phản Biện (Red-Teaming)
Ngay khi xuất ra bản thảo của một chương, AI **không được phép coi đó là hoàn hảo**. Ở cuối mỗi bản thảo, AI bắt buộc phải thêm một phần **[Tự Bắt Bệnh]**:
- Đóng vai một khán giả cực kỳ khó tính và soi mói.
- Tự chỉ ra ít nhất 1-2 điểm trong đoạn văn vừa viết có nguy cơ bị sáo rỗng, hơi dài dòng, hoặc xưng hô chưa đủ uy lực.
- Đề xuất sẵn 1 phương án sửa đổi "cay nghiệt" và sắc bén hơn để User lựa chọn.
