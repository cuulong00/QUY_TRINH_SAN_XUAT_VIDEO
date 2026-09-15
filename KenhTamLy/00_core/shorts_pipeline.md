# SHORTS PIPELINE — Quy Trình Tạo Video Ngắn

## TRIẾT LÝ CỐT LÕI
Shorts KHÔNG phải video dài bị cắt ngắn.
Shorts là một cú đánh cực ngắn vào attention, nhưng vẫn phải giữ được phẩm chất của kênh: đúng cơ chế, đúng nỗi đau, đúng lời hứa.

## ĐỊNH DẠNG KỊCH BẢN (TTS-CLEAN 100%)
File kịch bản Short là **file thu âm trực tiếp**. Tuyệt đối KHÔNG chèn BẤT KỲ thứ rác nào vào file kể cả tiêu đề Markdown hay metadata (như thời lượng, giọng đọc, tác giả, `## HOOK`). TTS sẽ đọc hết vào audio gây lỗi.

**Quy tắc:**
- Dòng 1 của file kịch bản phải là câu thoại đầu tiên. TUYỆT ĐỐI KHÔNG ghi Tiêu đề, Header hay Note sản xuất.
- Phân đoạn bằng **dòng trắng** hoặc **gạch ngang `---`** để tạo nhịp thở.
- Thân kịch bản = 100% lời thoại thuần, sạch bóng. Mọi metadata hay ghi chú quản lý phải để ở file khác (`00_content_strategy.md`).

## ĐỊNH DẠNG VISUAL PROMPTS (FLAT-FILE EXPORT)
Khi tạo prompt để chạy tool tự động (như `make_bespoke_prompts.py`), visual prompts bắt buộc phải được xuất ra định dạng thuần `.txt` (ví dụ `visual_prompts.txt`). Không dùng định dạng markdown `.md` cho file nạp vào máy.

**Quy tắc:**
- Mỗi phân cảnh/prompt bắt buộc phải nằm trên **một dòng duy nhất** (TUYỆT ĐỐI KHÔNG xuông dòng giữa chừng trong một prompt).
- Có đánh số ID ở đầu, ví dụ: `[01] A warm living room...`.
- Mỗi prompt cách nhau bởi đúng **1 khoảng trắng (1 dòng trống)**.
- Mục đích: Tránh cho các script batch-processing bị gãy khi parse (phân tích) file văn bản.

## PHONG CÁCH HÌNH ẢNH (VISUAL STYLE DNA CHO SHORTS)
Đối với định dạng Shorts, phong cách hình ảnh mặc định là **Hoạt hình 2D sinh động, màu sắc tươi sáng (Vivid 2D animation, bright colors)**. Khác với video dài (thường u ám, Nordic Noir, Chiaroscuro), Shorts thiên về việc giữ chân bằng sự bắt mắt, chuyển động mượt và năng lượng cao.
- **Từ khóa bắt buộc trong prompt:** Vivid 2D animation, bright colors, engaging, expressive characters, lively.
- Cảm xúc các nhân vật phải được phóng đại, rõ nét (hoạt hình), biến các khái niệm tâm lý nặng nề thành các meta-phor dễ thương, dễ hiểu.

## NHÁNH RIÊNG — SHORT TỪ VIDEO THAM KHẢO
Khi người dùng đưa một video tham khảo để tạo short mới, pipeline bắt buộc phải đi theo chuỗi này:
1. lấy transcript của video nguồn
2. lưu transcript vào thư mục short đích
3. đọc transcript để hiểu vấn đề cốt lõi
4. viết `01_source_analysis.md`
5. khóa một angle mới / cách tiếp cận mới
6. chỉ sau đó mới viết short script

### CẤM TUYỆT ĐỐI
- Cấm viết short chỉ từ URL, tiêu đề, thumbnail, hoặc trí nhớ về video nguồn.
- Cấm paraphrase transcript thành short mới.
- Cấm giữ nguyên sequence lập luận rồi chỉ đổi câu chữ.

### Transcript artifacts bắt buộc cho short từ source video
Trong thư mục `shorts/standalone/[slug]/` hoặc workspace đích tương đương, phải có:
- `00_raw_transcript.txt`
- `00_transcript_meta.json`
- `00_transcript_segments.json`
- nếu fail:
  - `00_transcript_status.md`
  - `00_transcript_error.json`
- `01_source_analysis.md`

## `01_source_analysis.md` bắt buộc phải trả lời
- video nguồn thực ra đang nói gì?
- 3-7 ý chính của source là gì?
- pain / mechanism mạnh nhất của source là gì?
- điều gì trong source đáng giữ làm nguyên liệu?
- điều gì phải thay đổi để đúng chất KenhTamLy?
- angle mới của short này là gì?
- điểm nào tuyệt đối không được paraphrase theo source?

## SHORT MỚI PHẢI KHÁC Ở ĐÂU?
Short mới phải khác source ở ít nhất một trong các tầng sau:
1. angle
2. mechanism explanation
3. pain framing
4. audience stance
5. structure

Nếu không khác ở ít nhất một tầng, short đó bị xem là fail.

## CTA THÔNG MINH (BẮT BUỘC CHO MỌI SHORT)

Mỗi Short PHẢI kết bằng một câu CTA ngắn (2 câu, tối đa 3 giây đọc). CTA này KHÔNG ĐƯỢC là lời xin chung chung ("Đăng ký kênh nhé!"). Nó phải tuân thủ cấu trúc:

**Công thức: [Tóm gọn insight vừa học] + [Hành động follow/đăng ký gắn với lợi ích cụ thể]**

### Nguyên tắc
1. **Gắn trực tiếp vào nội dung:** CTA phải dùng chính insight vừa trình bày làm lý do đăng ký. Người xem cảm thấy "follow để học thêm" chứ không phải "follow vì bị xin."
2. **Dí dỏm, nhẹ nhàng:** Giọng điệu hơi hóm hỉnh, không lên gân, không giảng đạo. Như một người bạn nháy mắt cuối câu chuyện.
3. **Ngắn tuyệt đối:** Tối đa 2 câu. Câu 1 = tóm insight. Câu 2 = follow + lợi ích.
4. **Không được lặp pattern:** Mỗi Short phải có CTA viết riêng, không copy-paste.

### Ví dụ đạt chuẩn
- (Short về lời khen): *"Khen con cũng phải học. Follow kênh Tâm Lý — để mỗi lời bạn nói với con, đều đúng chỗ."*
- (Short về trì hoãn): *"Lười không phải tại bạn — tại não. Follow kênh Tâm Lý — để hiểu bộ não trước khi đánh nhau với nó."*
- (Short về so sánh): *"So sánh là bản năng — nhưng biết dừng là kỹ năng. Follow kênh Tâm Lý — để trang bị kỹ năng đó."*

### Ví dụ KHÔNG đạt (CẤM)
- ❌ "Đăng ký kênh và bấm chuông nhé!"
- ❌ "Like và share nếu bạn thấy hay!"
- ❌ "Follow kênh Tâm Lý để xem thêm video!"
