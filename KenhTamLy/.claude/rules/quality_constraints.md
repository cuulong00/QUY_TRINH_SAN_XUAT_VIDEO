---
description: "Quy tắc chất lượng câu chữ, an toàn nội dung tâm lý học hành vi, và kỷ luật deliverable cho repo này."
---

# Quy tắc chất lượng & an toàn nội dung

## Chất lượng câu chữ
Ưu tiên:
- dễ nghe
- ít mệnh đề lồng nhau
- giàu nhịp thở
- ấm, sâu, rõ
- giải thích được cơ chế mà vẫn giữ độ người

Tránh:
- giả sâu
- giáo điều
- sáo rỗng
- quá nhiều từ Hán-Việt
- jargon tâm lý học dùng để làm màu
- lặp insight bằng cách đổi chữ

Giọng kênh:
- đồng hành, không lên lớp
- gần gũi, không suồng sã
- sắc mà không lạnh
- sâu mà vẫn rõ
- bắt đầu từ pain và pattern sống, không bắt đầu từ lý thuyết trừu tượng

## An toàn nội dung
Tuyệt đối cấm:
1. Bịa nghiên cứu, thống kê, chuyên gia, hoặc trích dẫn
2. Overclaim quan hệ nhân quả khi dữ liệu chỉ đủ cho tương quan hoặc suy luận mềm
3. Chẩn đoán người xem hoặc gán nhãn bệnh lý một cách bừa bãi
4. Dùng shame, fear, hoặc guilt để ép người nghe ở lại hoặc tin theo luận điểm
5. Hứa quá mức so với script trả được
6. Biến nội dung thành thay thế trị liệu, điều trị, hoặc can thiệp chuyên môn
7. Dùng thuật ngữ thần kinh học / tâm lý học như quyền lực giả

Mọi claim phải được phân loại:
- `evidence_supported`
- `clinically_informed`
- `behavioral_inference`
- `life_observation`
- `reflective_prompt`

Khi không chắc, hạ cấp claim thay vì đoán bừa.

## Safety priorities
### 1. Evidence integrity
- Không dùng câu kiểu “khoa học đã chứng minh” nếu không thật sự có nền đủ chắc.
- Không biến một góc nhìn hợp lý thành chân lý tuyệt đối.
- Phân biệt rõ điều nào là dữ liệu mạnh, điều nào là diễn giải, điều nào là quan sát đời sống.

### 2. Mental health safety
- Không pathologize hành vi bình thường của con người.
- Không nói như thể ai cũng đang có rối loạn.
- Không đổ toàn bộ khó khăn tâm lý cho ý chí yếu.
- Không trivialize trauma, anxiety, depression, burnout, attachment pain.

### 3. Ethical persuasion
- Hook có thể sắc, nhưng không được thao túng.
- Không dùng nỗi xấu hổ của người xem như công cụ câu retention.
- Không tạo false urgency hoặc false binary để ép cảm xúc.

### 4. Everyday applicability
- Insight phải sống được trong đời thường.
- Không được chỉ ném khái niệm mà không mở cơ chế và cảnh đời.
- Nội dung phải giúp người nghe hiểu mình rõ hơn, không chỉ nghe xong thấy “thông minh hơn”.

## Kỷ luật deliverable
- Khi cập nhật file, phải trả lại toàn bộ file.
- Khi kết thúc một pha, phải nêu rõ file nào thay đổi và checkpoint nào đã đạt.
- Khi workflow yêu cầu checkpoint, phải dừng xin user duyệt.

## Review discipline
Trước khi đánh dấu xong:
- continuity không mâu thuẫn
- không evidence overclaiming hoặc pseudo-clinical overreach
- tone khớp channel bible
- script đọc lên được
- state files đã được cập nhật
- không mang mùi văn công nghiệp hoặc template prose
- các đoạn nối có meaning, không chỉ có flow
- không có prompt metadata, workflow labels, reviewer language, hay process language rò vào prose
- không có bridge-by-template hoặc recap/preview kiểu máy

## CẤM LỘ PROMPT METADATA & INDUSTRIAL PHRASING
- Fail ngay nếu prose nghe như đang tóm tắt outline, đọc lại brief, hoặc giải thích cấu trúc thay vì nói với người nghe thật.
- Fail ngay nếu trong prose xuất hiện dấu vết của tên field, nhãn đánh giá, ngôn ngữ điều phối workflow, hoặc các cụm chuyển ý cơ học đã bị cấm trong `00_core/anti_patterns.md`.
- Không được viết như thư ký chuyển outline thành câu. Phải viết như người thật đã tiêu hóa insight rồi mới nói.
- Khi review, luôn tự hỏi:
  - đoạn này nghe như một người thật đang giải thích một cơ chế sống, hay như một hệ thống đang điều phối?
  - nếu bỏ câu nối này đi, ý có mất không? nếu không, đó là rác template
  - có câu nào lộ mùi recap / preview / chapter-management không?

## Chất lượng chiều sâu bắt buộc
- Không được generic empathy opener.
- Không được chỉ mô tả pain mà không đào tới cơ chế.
- Không được chỉ giải thích lý thuyết mà không có cảnh đời.
- Không được đánh đổi chiều sâu để lấy độ mượt rẻ tiền.
- Nội dung phải có cảm giác được viết bởi một người có nội tâm sống, không phải một bộ máy lắp ghép.
