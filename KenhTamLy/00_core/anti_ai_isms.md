# Anti-AI-isms — Danh sách cấm

## 1. Mục đích
File này liệt kê cụ thể những từ, cụm, pattern câu mà AI hay tạo ra nhưng nghe giả, công nghiệp, hoặc thiếu chiều sâu. Mọi kịch bản trong pipeline PHẢI được scan qua danh sách này trước khi ghi nhận.

## 2. Từ/Cụm bị cấm tuyệt đối

| ❌ Cấm | Lý do | ✅ Thay thế |
|---|---|---|
| "bóc trần" | Giọng YouTuber giật tít, không phải chuyên gia | Phân tích, nhìn kỹ, hoặc không dùng — để nội dung tự nói |
| "bóc tách" | Tương tự, quá overused | Phân tích cấu trúc, tách ra xem |
| "90% người không biết" | Con số bịa, giọng lên lớp | Bỏ hoàn toàn. Nếu cần: "điều ít được chú ý" |
| "sự thật gây sốc" | Giật tít rẻ tiền | Nêu sự thật thẳng — nếu nó thật sự sốc, khán giả tự biết |
| "bạn đang bị lừa" | Thao túng, paternalistic | "Bức tranh phức tạp hơn headline" |
| "bạn đang đọc sai" | Lên lớp | "Có một cách đọc khác" |
| "đây là phần quan trọng nhất" | AI filler, tự quảng cáo | Bỏ. Viết hay thì khán giả tự nhận ra |
| "và đây là phần 99% video không dám làm" | FOMO giả, self-aggrandize | Bỏ hoàn toàn |
| "hãy giữ chặt ghế" | Cliché drama | Bỏ |
| "câu trả lời sẽ khiến bạn bất ngờ" | Clickbait | Bỏ |
| "quan trọng hơn cả" | AI filler transition | Bỏ hoặc thay bằng logic tự nhiên |
| "không thể tin được" | Hyperbole rẻ | Bỏ |
| "câu hỏi thật sự là" | Template AI lặp lại qua nhiều episode — thông báo rằng sắp hỏi thay vì hỏi thẳng | Đặt câu hỏi trực tiếp, bỏ cụm dẫn |
| "Có một X mà Y không bao giờ Z" | Template AI mở đầu chương — giống nhau qua mọi video. VD: "Có một câu hỏi mà tin tức không bao giờ trả lời" | Nói thẳng nội dung, bỏ cấu trúc dẫn. VD: "Tin tức nói X. Nhưng không ai giải thích: tại sao..." |
| "tàn khốc", "tàn nhẫn", "khốc liệt", "điên cuồng", "vô vọng", "ngắc ngoải" | Quá kịch tính (melodramatic), từ ngữ cảm xúc mạnh làm mất đi sự điềm tĩnh mổ xẻ của chuyên gia. | "áp lực", "lặng lẽ nhưng dứt khoát", "phân rã sâu", "chật vật duy trì", "ráo riết", "thu hẹp dư địa" |

## 2.05 Từ/Cụm cần kiểm tra ngữ cảnh (KHÔNG cấm tuyệt đối — nhưng dễ dùng sai)

Các từ sau **không bị cấm hoàn toàn**, nhưng rất dễ bị lạm dụng sai ngữ cảnh. Trước khi dùng, agent PHẢI tự hỏi: "Từ này có MÔ TẢ ĐÚNG bản chất sự việc không, hay mình đang dùng nó để tăng drama?"

| Từ/Cụm | ✅ Dùng được khi | ❌ Không dùng khi | Cách kiểm tra |
|---|---|---|---|
| "cuộc chơi", "ván cờ" | Mô tả chiến lược cạnh tranh thực sự giữa các bên hoặc các thế lực. | Mô tả các phản ứng hành vi tự nhiên hoặc cơ chế sinh lý. | Sự việc có ÍT NHẤT 2 bên đang cạnh tranh chiến lược không? |
| "lật mở bức tranh", "vén màn" | Khi thực sự đang phân tích dữ liệu bị che giấu hoặc nghiên cứu ít người biết. | Khi đang phân tích hiện tượng phổ biến mà ai cũng thấy rõ. | Thông tin này có THỰC SỰ bị ẩn không, hay chỉ là mình đang phân tích? |
| "biến động ngầm", "sóng ngầm" | Khi mô tả sự thay đổi tâm lý âm thầm trước khi bộc phát ra hành vi. | Khi hiện tượng đã bộc phát rõ ràng hoặc dùng như từ trang trí. | Mình có nói được cụ thể biến động GÌ không? Nếu không → bỏ |
| "cực kỳ", "vô cùng" + tính từ mạnh | Khi sự kiện thực sự ở mức cực đoan có thể chứng minh qua thống kê. | Khi dùng để tăng drama mà không có bằng chứng hay đo lường cụ thể. | Có DATA nào chứng minh mức "cực kỳ" không? Nếu không → bỏ trạng từ |

## 2.1 Cấm Tuyệt Đối Lộ Prompt Metadata (Bệnh Công Nghiệp)
Viết để đọc thu âm, không phải viết để report log cho system. Mọi tên biến workflow, nhãn luận điểm từ prompt đều bị CẤM TẠO RA DƯỚI DẠNG CHỮ CỦA VOICEOVER.

| ❌ Cấm | Lý do | ✅ Thay thế |
|---|---|---|
| "chapter này", "chương này" | Voiceover không nói "chapter này". Nó là text format. | Dùng đại từ chỉ định cho vấn đề, không nhắc cấu trúc kịch bản |
| "interpretive move" | Nhại lại instruction prompt máy móc | Xóa sạch |
| "judgment", "editorial judgment" | Nhại lại instruction prompt | Xóa sạch |
| "contradiction" | Dùng như một nhãn dán cứng nhắc | Phân tích trực tiếp mâu thuẫn |
| "đây là cầu nối để..." | Cặn quy trình do nhại prompt | Xóa sạch |

## 3. Pattern câu bị cấm

### Pattern 1: "X nghe rất Y. Nhưng Z."
Quá công thức, mọi hook đều ra pattern này.
```
❌ "Kiểm soát nghe rất tốt. Nhưng nếu nhìn kỹ hơn..."
✅ Viết thẳng vào phân tích — không cần câu setup mechanics
```

### Pattern 2: Question cascade (3+ câu hỏi liên tiếp)
```
❌ "Họ nghĩ gì? Tại sao họ làm vậy? Họ có hạnh phúc không?"
✅ Đặt MỘT câu hỏi sắc, rồi đi trả lời nó
```

### Pattern 3: "Nhưng đó mới chỉ là bề mặt..."
AI transition cliché.
```
❌ "Nhưng đó mới chỉ là bề mặt. Bây giờ chúng ta sẽ nhìn sâu hơn."
✅ Đi thẳng vào layer tiếp theo bằng content — "Cơ chế tự vệ kể câu chuyện khác."
```

### Pattern 4: Mở bằng "Hãy tưởng tượng..."
```
❌ "Hãy tưởng tượng tâm trí là một chiếc hộp..."
✅ Nếu cần ẩn dụ, dùng tự nhiên trong câu, không mở bằng "hãy tưởng tượng"
```

### Pattern 5: "Đó là [danh từ trừu tượng]." đứng cuối đoạn
```
❌ "Đó là sự phản kháng." / "Đó là nỗi đau." / "Đó là cơ chế."
✅ Chốt bằng insight cụ thể thay vì dán nhãn
```

### Pattern 6: Parallel structure lặp [liệt kê 3 cái] quá đều
```
❌ "Tâm trí phản kháng. Cơ thể mệt mỏi. Hành vi đình trệ."
✅ Phá nhịp — một câu dài, một câu ngắn, một câu chốt khác tone
```

## 4. Transition bị cấm

| ❌ Cấm | ✅ Thay thế |
|---|---|
| "Nhưng đó mới chỉ là bề mặt" | Đi thẳng vào ý tiếp |
| "Bây giờ đến phần gây tranh cãi nhất" | Để nội dung tự thể hiện |
| "Và đây là chỗ mọi thứ thay đổi" | Viết sự thay đổi, không cần thông báo |
| "Bạn đã thấy vấn đề rồi. Câu hỏi là..." | Chuyển bằng logic tự nhiên |
| "Phần tiếp theo sẽ khiến bạn..." | Bỏ — tự quảng cáo |
| "Đây là chỗ [A] đáng để nhìn" | Bỏ — sáo rỗng. Đẩy luận cứ của [A] lên luôn. |
| "Đây là điểm nhiều người hay đọc quá nhanh" | Bỏ mẫu câu dán nhãn chê trách đám đông lặp lại. |
| "Điểm đáng nói là..." | Quá mòn, dùng vô tội vạ. |
| "Từ đây mới thấy..." | Quá mòn, văn phong trả bài. |
| "Nếu chapter trước cho thấy X, thì..." | Transition cơ học, cấm dùng từ refer cấu trúc văn bản. |
| "Nói gọn..." / "Nói cách khác..." | Không cấm hoàn toàn, nhưng CẤM LẶP nếu đã dùng rồi. Tốt nhất là bỏ. |

## 5. Nguyên tắc thay thế tổng quát

### Thay vì giật tít → Để cơ chế tự lên tiếng
Lý luận tâm lý học mạnh không cần câu setup "sự thật gây sốc". Nêu thẳng hiện tượng, chỉ ra cơ chế hoạt động, để khán giả tự nhận thức và đối chiếu với cuộc sống của họ.

### Thay vì lên lớp → Chia sẻ phân tích
"Bạn đang hiểu sai" → "Nếu chúng ta quan sát kỹ hơn từ một góc độ khác..."

### Thay vì template → Mỗi video có cấu trúc riêng
Không có lý do gì chủ đề Nghịch lý kiểm soát phải có cùng cấu trúc hook với chủ đề Trì hoãn hay Áp lực đồng lứa.

### Thay vì announcement → Content
"Và đây là phần quan trọng nhất" = bạn đang nói với khán giả rằng những gì trước đó KHÔNG quan trọng. Thay vào đó: viết phần quan trọng cho hay, khán giả tự biết.

## 6. Cách dùng file này trong pipeline
- **chapter_writer**: scan mỗi chapter sau khi viết nháp
- **hook_engine**: đối chiếu mỗi hook trước khi chốt
- **oral_polisher**: check round cuối cùng trước khi đưa đi thu âm
- **quality_czar**: dùng làm checklist phê bình chất lượng

## 7. Cấm Pha Tiếng Anh Vào Tiếng Việt VÀ Biệt Ngữ Kỹ Thuật Hẹp (NGHIÊM CẤM)

Kịch bản voiceover là tiếng Việt. **NGHIÊM CẤM** chèn từ tiếng Anh hoặc các biệt ngữ viết tắt chuyên ngành hẹp tâm lý/thần kinh (amygdala, prefrontal cortex, dopamine deficit, CBT, ACT, OCD...) vào câu tiếng Việt cho đại chúng mà không có giải thích ngắn gọn, dễ hiểu trước. Đối với thuật ngữ tiếng Anh, ưu tiên dịch nghĩa tự nhiên sang tiếng Việt. Chỉ được giữ tên riêng (Sigmund Freud, Carl Jung, Ivan Pavlov...).

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| pivot | chuyển hướng |
| pattern | vòng lặp, quỹ đạo hành vi |
| trigger (động từ) | kích hoạt, làm bùng phát |
| dopamine | chất dẫn truyền thần kinh dopamine (kèm chú thích ngắn nếu cần) |
| mindset | tư duy |
| self-care | chăm sóc bản thân |
| toxic | độc hại |
| gaslighting | thao túng tâm lý |
| healing | chữa lành, xoa dịu |
| burnout | kiệt sức |

**Nguyên tắc:** Nếu một từ tiếng Anh có từ tiếng Việt tương đương tự nhiên, BẮT BUỘC dùng tiếng Việt. Pha trộn ngôn ngữ trong voiceover làm mất uy tín khoa học và sự thấu cảm.
