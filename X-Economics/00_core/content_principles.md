# 5 Nguyên Tắc Lõi — X-Economics Content Principles

> **Vai trò:** Đây là Tầng 1 — nạp vào context MỌI LÚC khi viết nội dung.
> Tầng 2 (chi tiết, ví dụ, từ cấm) nằm ở `anti_patterns.md` — chỉ nạp khi Quality Czar scan hoặc khi cần tra cứu case cụ thể.

---

## 1. Accuracy-First — Sự thật chính xác TẠO RA kịch tính

Drama phải đến từ sự thật nguyên bản, không đến từ sự cắt xén hay phóng đại.

**Cách thực hiện:**
- Mọi con số phải có nguồn + đúng bản chất + đúng phạm vi hiệu lực.
- Giữ nguyên các từ định vị ngữ cảnh (thời gian, phạm vi địa lý, phân khúc). THÀ BỎ CON SỐ CÒN HƠN viết sai phạm vi.
- Tương quan ≠ nhân quả. Phải giải thích cơ chế truyền dẫn, không ép 2 data point rời rạc vào quan hệ nhân quả.
- *Chỉ thị:* Bắt buộc neo tựa vào sự thật pháp lý và số liệu công khai (Nguyên tắc 4 của Khung tư duy AI). Mọi lập luận mang tính bước ngoặt phải dựa trên báo cáo tài chính chính thức và văn bản pháp luật chính thống có số hiệu cụ thể.
- Dự báo phải trình bày như dự báo (có độ không chắc chắn), không như sự thật.
- Số liệu tính toán (derived) phải ghi rõ phép tính + nguồn gốc.
- **Chống phiến diện và "chơi trội" bằng luận điểm thiếu căn cứ:** Quan điểm cá nhân chỉ được phép đưa ra khi dựa trên hệ thống số liệu rộng mở, đúng đắn, bao quát và đủ độ tin cậy. Nếu góc nhìn thiếu tính bao quát và phản biện, quan điểm đó sẽ tạo ra sự thiên kiến nguy hiểm. Cốt lõi của kênh là **đa chiều, tính phản biện cao và bám sát sự thật dữ liệu** đã qua nghiên cứu sâu (deep research).

> *Một sự thật chính xác nhưng bất ngờ LUÔN kịch tính hơn một sự phóng đại dễ bị bắt lỗi.*

**Tham chiếu chi tiết:** `anti_patterns.md` #17 (bịa số), #26 (ngôn ngữ đóng đinh/superlative), #28 (hindsight bias).


---

## 2. Audience Relevance Early — Khán giả phải thấy MÌNH hoặc TÒ MÒ TRÍ TUỆ trong 3 phút đầu

Người xem rời đi khi không thấy mình liên quan hoặc không thấy lý do để quan tâm. Điểm tựa giữ chân (Relevance Anchor) phải là ưu tiên số 1 trong cấu trúc mở đầu.

**Cách thực hiện theo bản chất 3 loại đề tài:**
- **Loại A (Đời sống / Tiêu dùng / Xã hội trực tiếp):**
  * Personal Stakes xuất hiện ngay trong **Chương 2** (phút 1:30-3:30).
  * Mỗi 3-4 phút có ít nhất 1 điểm chạm đời sống (thu nhập, chi phí, việc làm, tài sản, an sinh).
  * Sử dụng lăng kính phổ quát ("Chúng ta", "Người lao động", "Xã hội hiện đại") — KHÔNG bịa đặt nhân vật cá nhân hóa gượng gạo ("Anh Nam 30 tuổi").
- **Loại B (Doanh nghiệp / Thể chế / Công nghiệp):**
  * Relevance Anchor nằm ở bài toán tối ưu chi phí, rủi ro quản trị, tác động dây chuyền chuỗi giá trị và bài học sinh tồn của doanh nghiệp/quốc gia.
  * TUYỆT ĐỐI CẤM gượng ép "sổ đỏ, túi tiền của bạn" vào đề tài công nghiệp nặng hay phân tích tài khóa.
- **Loại C (Documentary / Toàn cầu / Địa chính trị dài hạn):**
  * Intellectual Relevance Anchor: Khán giả ở lại vì TÒ MÒ TRÍ TUỆ trước các quy luật lớn, nghịch lý lịch sử và cú sốc dữ liệu (Data Shock).
  * TUYỆT ĐỐI CẤM ép nỗi sợ mất tiền hay liên hệ Việt Nam gượng ép vào đề tài phân tích nhân loại toàn cầu.
- **Quy tắc chung:** Không để quá 3 phút liên tiếp chỉ có lý thuyết suông mà không có: (a) con số thực chứng mới, (b) phép loại suy trực quan đời thường, hoặc (c) câu hỏi phản biện làm mới sự chú ý.

> *Nội dung vừa đủ sâu và kết nối đúng tầng nhận thức của khán giả — luôn giữ chân người xem đến giây cuối cùng.*

**Tham chiếu chi tiết:** `anti_patterns.md` #1, #13, #19-20, #22.

---

## 3. Incentive-First — Phân tích bằng động lực kinh tế, không bằng đạo đức

Hệ thống kinh tế vận hành theo incentives. Hiểu incentive = hiểu bản chất. Phán xét đạo đức = chỉ thấy bề mặt.

**Cách thực hiện:**
- Khi phân tích hành vi doanh nghiệp/chính phủ, LUÔN hỏi: "Áp lực NÀO trong hệ thống buộc họ hành động? Nếu ở vị trí đó với cùng thông tin, ta có quyết định khác không?"
- *Chỉ thị:* Dịch chuyển trục xung đột sang sự khốc liệt của quy luật khách quan (Nguyên tắc 1 của Khung tư duy AI). Tuyệt đối cấm tạo xung đột giữa doanh nghiệp/nhà nước với người dân. Giải thích mọi hiện tượng bằng chi phí cơ hội, cung-cầu, rủi ro hệ thống và tính thâm dụng vốn thay vì động cơ chủ quan.
- Trade-off analysis bắt buộc: "Chọn A thì hy sinh B."
- Phân tích quyết định quá khứ: đặt trong bối cảnh thông tin TẠI THỜI ĐIỂM ĐÓ, không phán xét bằng dữ liệu tương lai.
- Không gán động cơ đạo đức ("tham lam", "chiêu trò") cho chiến lược kinh tế hợp pháp. Mô tả bằng cơ chế: "tối đa hóa lợi nhuận ngắn hạn", "chấp nhận rủi ro cao".

> *Khi giải mã được động lực → mọi hành vi đều có tính logic. Video sẽ sâu hơn vì giải thích CƠ CHẾ thay vì chỉ QUY KẾT.*

**Tham chiếu chi tiết:** `anti_patterns.md` #27 (binary trap), #28 (hindsight bias), #29 (moralizing).

---

## 4. Expert Voice — Chuyên gia phân tích, không phải guru hay MC tin tức

Giọng kênh là *cold analytical urgency* — sự khẩn cấp của người hiểu rõ vấn đề, nhưng đủ kỷ luật để không moralize hay hoảng loạn.

**Cách thực hiện:**
- Insight phải đi kèm data. Câu nào không có số liệu hoặc cơ chế cụ thể → câu đó rỗng.
- Không dùng giọng "bạn phải", "bạn nên". Đặt vấn đề đủ rõ để khán giả tự rút ra.
- Không dùng từ guru: "mindset triệu đô", "tư duy đại bàng", "thay đổi cuộc đời".
- Không hứa lợi nhuận. Không tạo FOMO giả. Không đưa lời khuyên mua bán cụ thể.
- Thuật ngữ chuyên môn phải giải thích bằng ngôn ngữ đời thường ngay lập tức.
- Sự trung thực về giới hạn bằng chứng ("Chưa đủ dữ liệu để kết luận, nhưng...") không làm yếu kịch bản — nó làm đáng tin hơn.
- **Kịch tính kinh tế học thay vì nhạy cảm chính trị (Nguyên tắc 3 của Khung tư duy AI):** Luôn chuyển dịch các câu hỏi, luận điểm nhạy cảm chính trị hoặc cơ cấu quan hệ ngầm sang phân tích động lực tài chính thực chứng và năng lực thực thi thực tế của doanh nghiệp. Sử dụng ngôn ngữ kinh tế học toàn cầu và toán học để gọi tên hiện tượng (ví dụ: thâm dụng vốn lớn, chiến lược phát triển quán quân quốc gia, tính ổn định hệ thống, chi phí cơ hội vĩ mô), tránh tuyệt đối các từ ngữ biểu cảm hay suy đoán.

> *Sức mạnh của narration đến từ sự tĩnh lặng và sắc bén của logic, không phải từ ngôn từ la hét.*

**Tham chiếu chi tiết:** `anti_patterns.md` #2 (guru), #3 (giảng dạy), #5 (thuật ngữ), #6 (hứa lợi nhuận), #8 (khẩu hiệu), #11 (thiếu empathy).

---

## 5. Unique Lens — Không có giá trị gia tăng = không có lý do tồn tại

Nếu bỏ tên kênh đi mà video không khác gì 5 video cùng chủ đề trên YouTube → video đó thất bại.

**Cách thực hiện:**
- Mỗi episode phải có lăng kính độc bản (tâm lý học hành vi, lịch sử kinh tế, lý thuyết trò chơi, chuỗi cung ứng...) — ghi rõ trong `03_brief.md`.
- *Chỉ thị:* Luôn áp dụng lăng kính so sánh lịch sử quốc tế (Nguyên tắc 5 của Khung tư duy AI - Lăng kính lịch sử sơn vàng) và quy tắc trung lập tuyệt đối (Nguyên tắc 2 - Objective Hook) bằng cách cân bằng hai luồng dư luận đối lập khi mở đầu và thiết kế cliffhanger an toàn ở kết chương.
- Mỗi insight phải mở thêm một lớp mới. Nếu đổi từ nhưng không thêm lớp → đang lặp, không phải phát triển.
- Tối đa 2 case study quốc tế. Ưu tiên case liên quan trực tiếp nhất đến VN.
- Script phải sinh ra visual map theo đoạn — không ghép hình random.
- Mỗi chapter phải mở nhất 1 khoảnh khắc "Wait, that means..." — nơi khán giả connect the dots trước narrator.

> *Kênh này thắng bằng sự trung thực, số liệu thật, sự tỉnh táo, và khả năng khiến người xem thấy MÌNH trong câu chuyện vĩ mô.*

**Tham chiếu chi tiết:** `anti_patterns.md` #4 (lặp insight), #10 (ví dụ xa lạ), #14 (viết cho đọc), #16 (lời hứa không trả), #30 (me-too trap).

---

## 6. The Masterpiece Narrative Spine — Sợi Chỉ Đỏ Tự Sự Kiệt Tác (0% Phân Mảnh)

Một video phân tích dài không phải là một tập hợp các bài tiểu luận ghép lại, mà là một cỗ máy đồng hồ tinh xảo vận hành theo một trọng lực tự sự duy nhất.

**Cách thực hiện:**
- **The Single Spine:** Chỉ có DUY NHẤT một Biến cố trung tâm (Inciting Incident). 100% các chương phải phục vụ việc mổ xẻ, thử thách hoặc tháo ngòi biến cố này. Tuyệt đối CẤM tư duy ngăn tủ (Silo Thinking) biến các chương thành bài giảng lịch sử, địa lý hay thể chế độc lập.
- **Quy luật Nhân quả "THEREFORE / BUT" (Zero "And Then"):** 100% các chuyển đoạn và chuyển chương phải được kết nối bằng động lực nhân quả "VÌ VẬY..." (Therefore) hoặc "NHƯNG..." (But). Cấm liên từ nối sáo rỗng ("Và rồi...", "Mặt khác...", "Bên cạnh đó...").
- **Cấu trúc Búp Bê Nga (The Russian Doll Escalating Layers):** Bóc tách bí ẩn theo 4 tầng tăng tiến từ Bề mặt $\rightarrow$ Thể chế $\rightarrow$ Bản chất kỹ thuật/kinh tế $\rightarrow$ Chuyển hóa chiến lược.
- **Anti-Burying-The-Lede:** Tuyệt đối CẤM giấu nút thắt kỹ thuật/kinh tế bản chất nhất xuống chương áp chót hoặc chương kết bài. Cú va chạm bản chất BẮT BUỘC phải nổ ra ở Đỉnh cao trào Màn 2 (khoảng giữa video), để chương kết dành trọn vẹn cho sự phản tư và bài học dài hạn.

> *Kịch bản kiệt tác không chạy theo chiều ngang (kể hết chuyện này sang chuyện khác), mà xoáy sâu vào tâm bão của biến cố trung tâm.*

