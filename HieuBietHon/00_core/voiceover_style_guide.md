# voiceover_style_guide.md

## 1. Mục tiêu của file này
File này giúp mọi bản script trở thành **lời thoại nghe được**, không chỉ là văn bản đọc đẹp.

Với kênh tài chính, voice over phải truyền được 4 thứ cùng lúc:
- độ rõ của lập luận,
- sức nặng của dữ liệu,
- độ tin cậy của người nói,
- và nhịp nghe đủ sống để người xem đi hết video.

Script tốt không chỉ “mượt”.
Script tốt phải nghe như có một người thật đang nghĩ, đang chọn câu, đang có chính kiến.

## 2. Nguyên tắc cốt lõi
Script phải được viết cho **tai nghe**.
Điều đó có nghĩa là:
- câu cần có nhịp thở,
- dữ liệu phải đi kèm diễn giải,
- đoạn phải có điểm chuyển ý rõ,
- từ ngữ phải gần miệng người nói,
- và quan trọng hơn cả: giọng nói phải có **calibre của người hiểu vấn đề**.

## 3. Giọng đọc mục tiêu
Giọng đọc mà script hướng đến là:
- bình tĩnh nhưng sắc,
- tự tin nhưng không tự cao,
- có chính kiến nhưng biết phân biệt đâu là data, đâu là analysis, đâu là opinion,
- không giật tít, không dạy đời, không lên lớp,
- nghe như một nhà phân tích lâu năm đang giải thích cho người thông minh nhưng không chuyên sâu đúng mảng đó.

Không phải:
- MC đọc bản tin,
- giáo sư giảng bài,
- KOL bán niềm tin,
- YouTuber giữ retention bằng drama.

## 4. Quy tắc câu văn
### Nên làm
- ưu tiên câu ngắn đến trung bình, BẮT BUỘC giữ độ dài dưới 150 ký tự (khoảng 20-25 từ) cho mỗi câu để tương thích tối ưu với hệ thống GPU RunPod TTS local.
- một câu chủ yếu mang một ý chính duy nhất,
- dùng câu cực ngắn để chốt sau một đoạn phân tích,
- đan xen câu có độ dài không đều nhau (câu cực ngắn 3-5 từ kết hợp câu trung bình 10-15 từ) để tạo nhịp thở tự nhiên của con người,
- chủ động ngắt câu bằng dấu chấm (.) và dấu phẩy (,) dưới 150 ký tự để làm mốc nghỉ hơi tự nhiên cho AI, tránh choppy.
- sau dữ liệu phải có một câu “so what?”.

### Tránh
- câu dài quá 150 ký tự, câu nhiều tầng mệnh đề phụ gây attention drift (trôi bộ nhớ) và nghẽn bộ nhớ GPU RunPod.
- liệt kê quá nhiều số liệu liên tiếp,
- câu quá cân đối, quá “đẹp công nghiệp”,
- câu nghe như mẫu prompt viết sẵn,
- câu announce-importance kiểu “đây là phần quan trọng nhất”.

Ví dụ chưa tốt:
> Theo số liệu của Tổng cục Thống kê, chỉ số giá tiêu dùng CPI năm 2024 tăng trung bình 3.63% so với cùng kỳ năm trước, trong khi lãi suất tiết kiệm bình quân kỳ hạn 12 tháng chỉ đạt 4.5%.

Ví dụ tốt hơn:
> Năm 2024, giá cả tăng trung bình 3.6%.
> Tiền gửi tiết kiệm chỉ sinh lời khoảng 4.5%.
> Chênh lệch nghe không lớn.
> Nhưng với người sống bằng tiền nhàn rỗi, đó là khoảng cách đủ để thấy sức mua bị bào mòn.

## 5. Quy tắc đoạn văn
Mỗi đoạn nên ngắn.
Lý tưởng là 2–4 câu.

Nhưng “ngắn” không phải để cắt vụn mọi thứ.
Mục tiêu là để mỗi đoạn:
- mang một chuyển động rõ,
- có điểm nghỉ,
- và không buộc người nghe giữ quá nhiều ý trong đầu cùng lúc.

Tách đoạn khi:
- chuyển từ số liệu sang diễn giải,
- chuyển từ cơ chế sang hệ quả,
- chuyển từ macro sang đời sống thật,
- bắt đầu một case study mới,
- hoặc cần thay đổi nhiệt độ câu chữ.

## 6. Từ vựng nên ưu tiên
### Nên ưu tiên
- từ đời thường về tiền bạc,
- động từ có lực nhưng không gào,
- hình ảnh cụ thể,
- từ vựng chuyên môn vừa đủ, có giải nghĩa khi cần.

Ví dụ tốt:
- ăn mòn,
- bốc hơi,
- chạm trần chi phí,
- biên lợi nhuận,
- dòng tiền,
- độ bền,
- sức bật,
- hàm lượng nhập khẩu,
- khả năng chịu sốc.

### Nên tiết chế
- thuật ngữ quá hàn lâm,
- tiếng Anh không cần thiết,
- từ ngữ “content machine”,
- khẩu hiệu rỗng,
- self-promotion trong nội dung.

## 7. Cách dùng thuật ngữ tài chính và công nghệ (Đại chúng hóa thuật ngữ)

### Nguyên tắc Đại chúng hóa
Tuyệt đối không sử dụng trực tiếp các từ viết tắt chuyên ngành hẹp mà không giải nghĩa, vì đối tượng người xem của HieuBietHon là đại chúng, không phải chuyên gia kỹ thuật hay lập trình viên. Bắt buộc chuyển đổi hoặc diễn giải sang các cách gọi dễ hiểu nhất:
- **AWS, Azure, GCP** ➔ *Amazon, Microsoft, Google* hoặc *các dịch vụ đám mây của Amazon, Microsoft, Google*.
- **PUE (Power Usage Effectiveness)** ➔ *chỉ số sử dụng điện năng hiệu quả*.
- **HPC (High-Performance Computing)** ➔ *phân khu máy tính siêu cấp, tính toán hiệu năng cao*.
- **DPPA (Direct Power Purchase Agreement)** ➔ *mua bán điện trực tiếp*.
- **VRAM / Node** ➔ *bộ nhớ đồ họa / nút máy chủ*.
- **Inference (Suy luận AI)** ➔ *xử lý và tạo câu trả lời của AI*.
- **Token** ➔ *đơn vị từ ngữ sinh ra*.

### Cách dùng thuật ngữ
Khi dùng thuật ngữ bắt buộc phải dùng, đi theo thứ tự:
1. nêu thuật ngữ,
2. dịch nó sang ngôn ngữ người,
3. cho ví dụ đủ cụ thể,
4. chốt ý nghĩa của nó trong bối cảnh video.

Ví dụ:
> PE hay Price-to-Earnings, hiểu đơn giản là: bạn đang trả bao nhiêu đồng cho mỗi đồng lợi nhuận mà doanh nghiệp tạo ra.
> PE = 20 nghĩa là bạn bỏ 20 đồng để mua 1 đồng lợi nhuận hiện tại.
> Vấn đề không nằm ở chỗ cao hay thấp một cách cơ học.
> Vấn đề là thị trường đang kỳ vọng điều gì vào 19 đồng còn lại.

## 8. Nhịp điệu cảm xúc trong lời thoại
Một bản voice over tốt phải có nhịp lên xuống.
Nhưng nhịp đó đến từ **nội dung đổi pha**, không phải từ việc cứ vài đoạn lại gằn giọng.

Nhịp khuyến nghị:
- mở bằng một quan sát đủ đắt,
- dẫn dắt bình tĩnh,
- tăng nhiệt khi interpretive turn xuất hiện,
- hạ nhịp khi cần giải thích,
- tăng lại khi chốt insight,
- kết bằng lực vừa đủ, không slogan.

Nếu câu nào cũng “thép”, người nghe sẽ mệt.
Nếu câu nào cũng hiền, video sẽ trôi.

## 9. Expert restraint — quy tắc rất quan trọng
Một script nghe chuyên gia thường không cần nói quá.

### Dấu hiệu của expert restraint
- không cần gọi dữ liệu là “gây sốc” nếu nó đủ mạnh,
- không cần nói “đây mới là phần quan trọng nhất”,
- không cần hỏi 3 câu liên tiếp để tạo giả cảm giác sâu,
- không cần tuyên bố người xem đang bị lừa,
- không cần biến mọi phát hiện thành chân lý đạo đức.

### Khi xung đột giữa “punchy” và “credible”
Luôn chọn **credible**.

### Câu hay không nhất thiết phải gào
Nhiều câu mạnh nhất thường là những câu bình tĩnh nhưng đóng đúng chỗ.

Ví dụ:
> Con số này không sai.
> Nhưng cách đọc nó đang quá nhanh.

## 10. Cách dùng con số trong voice over
Con số là tiền tệ của kênh này.
Nhưng chỉ có giá trị khi người nghe hiểu nó nói gì.

### Nên làm
- làm tròn khi cần cho dễ nghe,
- gắn con số với context,
- so sánh tương đối,
- sau con số phải có ý nghĩa.

### Tránh
- đọc quá nhiều số liền nhau,
- đưa số không giải thích,
- cố làm con số nghe “hoành tráng” bằng tính từ cường điệu.

## 11. Câu nhấn một dòng
Kênh này hợp với câu nhấn ngắn.
Nhưng chỉ dùng khi thật sự đáng.

Câu nhấn tốt:
- chốt một interpretive move,
- hoặc khóa một nghịch lý,
- hoặc mở một layer mới.

Ví dụ:
- “Tăng trưởng thật. Nhưng chưa chắc đã bền.”
- “Dữ liệu đẹp. Cấu trúc thì chưa.”
- “Vấn đề không nằm ở con số. Vấn đề nằm ở cách đọc.”

### Không nên lạm dụng
Nếu đoạn nào cũng có one-liner, one-liner sẽ mất giá.

## 12. Quy tắc oralization
Oralization không chỉ là cắt ngắn câu.
Nó là bước biến văn bản thành lời nói của **một bộ óc đang vận hành**.

Cần làm:
- rút bớt chữ thừa,
- bỏ các phrase nghe như template,
- thêm nhịp nghỉ,
- phá những đoạn quá đều,
- giữ những chỗ “hơi thô nhưng thật” nếu chúng tạo cảm giác người nói đang nghĩ thật.

## 13. Quy tắc tránh “phân tích hay nhưng không nghe được”
Một đoạn sẽ thất bại nếu:
- nhiều số liệu nhưng không có ý nghĩa,
- logic đúng nhưng toàn abstract nouns,
- câu nào cũng đúng nhưng không có edge,
- nghe như research memo được làm đẹp sơ sài,
- hoặc nghe như YouTube script được tối ưu retention.

Hỏi 3 câu này khi polish:
1. Người nghe có thấy một người thật đang nghĩ trong đoạn này không?
2. Đoạn này có nói điều gì chỉ video này mới nói, hay kênh nào cũng nói được?
3. Sau đoạn dữ liệu, đã có interpretation đủ đắt chưa?

## 14. Quy tắc cho đoạn mở đầu
Phần mở đầu phải:
- vào thẳng vấn đề,
- mở bằng một quan sát đủ đắt,
- cho thấy calibre của người nói,
- tránh toàn bộ AI-isms trong `anti_ai_isms.md`.

Thường nên bắt đầu bằng:
- một contrast dữ liệu,
- một nghịch lý,
- một câu hỏi hẹp nhưng sắc,
- hoặc một pain rất thật kéo vào cơ chế lớn hơn.

## 15. Quy tắc cho đoạn kết
Phần kết phải:
- tóm lại insight chính,
- đưa action framework nếu cần,
- chốt bằng một góc nhìn bám lại,
- KHÔNG kết bằng câu slogan chung chung.

Kết tốt là kết khiến người xem nghĩ tiếp.
Không phải kết khiến họ được “truyền động lực” kiểu content machine.

## 16. Checklist cuối trước khi đưa sang TTS
1. Có câu nào quá dài khiến TTS hụt hơi không?
2. Có đoạn nào liệt kê hơn 3 con số mà không giải nghĩa không?
3. Có thuật ngữ nào chưa được giải thích không?
4. Có câu nào nghe như template AI không?
5. Có đoạn nào announce-importance thay vì để content tự nói không?
6. Có quá nhiều câu cùng một hình dạng không?
7. Có đủ những câu cho thấy người viết đang thật sự có chính kiến không?
8. Đọc lớn thành tiếng có mượt và có trí tuệ không?
9. **⛔ CẤM TUYỆT ĐỐI dấu `—` nối ý ngắn** (VD: "kém — mà", "không phải A — mà là B"). TTS đọc dính hoặc tạo pause lạ. Thay bằng dấu chấm tách 2 câu, hoặc dùng dấu phẩy/liên từ. Chỉ giữ `—` khi chèn mệnh đề phụ dài (apposition).
10. **⛔ BẮT BUỘC DỌN DẸP SẠCH SẼ:** Trước khi gửi sang TTS/Voiceover, tất cả các file `chapter_XX.md` phải được xóa bỏ hoàn toàn mọi tiêu đề chương (dạng `# Chương X: ...`), chú thích, metadata, và ghi chú quy trình ở đầu và cuối file. File chỉ giữ lại duy nhất phần văn bản voiceover (phần đọc) sạch sẽ, không có bất kỳ ký tự hoặc ký hiệu kỹ thuật nào khác để tránh làm gián đoạn nhịp đọc của mô hình TTS hoặc người thu âm.

## 17. Chuẩn đầu ra cuối cùng
Một script đạt chuẩn voice over phải cho người nghe cảm giác:
- có người am hiểu đang nói với mình,
- dữ liệu được diễn giải chứ không chỉ ném ra,
- câu chữ đủ gần để nghe hết,
- và video có một cái đầu thật ở trong đó.

Voice over tốt không chỉ truyền thông tin.
Nó truyền được **độ tin cậy, độ rõ, và độ sắc của tư duy**.

Đó mới là thứ khiến người xem tin bạn là người có nghề.