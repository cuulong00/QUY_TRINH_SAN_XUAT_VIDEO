# Anti-AI-isms — Danh sách cấm

## 1. Mục đích
File này liệt kê cụ thể những từ, cụm, pattern câu mà AI hay tạo ra nhưng nghe giả, công nghiệp, hoặc thiếu chiều sâu. Mọi output trong pipeline PHẢI được scan qua danh sách này trước khi lưu.

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
| "tàn khốc", "tàn nhẫn", "khốc liệt", "điên cuồng", "vô vọng", "ngắc ngoải" | Quá kịch tính (melodramatic), từ ngữ cảm xúc mạnh làm mất đi sự điềm tĩnh mổ xẻ của chuyên gia. Gây cảm giác YouTuber đang cố đẩy drama. | "áp lực", "lặng lẽ nhưng dứt khoát", "phân rã sâu", "chật vật duy trì", "ráo riết", "thu hẹp dư địa" |
| "canh bạc", "canh bạc cuộc đời", "canh bạc tất tay" | Giọng điệu giật gân, rẻ tiền, bị lạm dụng cực kỳ nhiều trên mạng xã hội, làm giảm tính phân tích chuyên nghiệp của video | "sự đánh đổi chiến lược", "bước đi rủi ro", "phân bổ vốn mạo hiểm", "quyết định CAPEX lớn" |

## 2.05 Từ/Cụm cần kiểm tra ngữ cảnh (KHÔNG cấm tuyệt đối — nhưng dễ dùng sai)

Các từ sau **không bị cấm hoàn toàn**, nhưng rất dễ bị lạm dụng sai ngữ cảnh. Trước khi dùng, agent PHẢI tự hỏi: "Từ này có MÔ TẢ ĐÚNG bản chất sự việc không, hay mình đang dùng nó để tăng drama?"

| Từ/Cụm | ✅ Dùng được khi | ❌ Không dùng khi | Cách kiểm tra |
|---|---|---|---|
| "ván cờ", "cuộc chơi", "ván bài" | Mô tả chiến lược cạnh tranh thực sự giữa các bên (VD: VinFast vs Toyota, chiến tranh thương mại Mỹ-Trung) | Mô tả chính sách công vĩ mô đơn thuần (VD: hoán đổi ngày nghỉ lễ, chính sách tiền tệ) — vì chính sách không phải trò chơi | Sự việc có ÍT NHẤT 2 bên đang cạnh tranh chiến lược không? |
| "lật mở bức tranh", "vén màn" | Khi thực sự đang phân tích dữ liệu bị che giấu hoặc ít người biết (VD: số liệu nội bộ FTX bị phơi bày) | Khi đang phân tích dữ liệu công khai mà ai cũng tra được (VD: GDP, lượng khách du lịch) | Thông tin này có THỰC SỰ bị ẩn không, hay chỉ là mình đang phân tích? |
| "biến động ngầm", "sóng ngầm" | Khi mô tả chuyển động thị trường chưa phản ánh lên giá hoặc chưa được truyền thông đưa tin (VD: khối ngoại âm thầm thoái vốn trước tin chính thức) | Khi sự kiện đã công khai hoặc khi dùng như từ trang trí vô nghĩa mà không nói rõ biến động GÌ | Mình có nói được cụ thể biến động GÌ không? Nếu không → bỏ |
| "cực kỳ", "vô cùng" + tính từ mạnh | Khi con số hoặc sự kiện thực sự ở mức cực đoan có thể chứng minh (VD: "cực kỳ hiếm" nếu xác suất < 1%) | Khi dùng để tăng drama mà không có data chứng minh mức độ (VD: "cực kỳ lạnh lùng" cho một chính sách bình thường) | Có DATA nào chứng minh mức "cực kỳ" không? Nếu không → bỏ trạng từ |


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
❌ "GDP 7,83% nghe rất mạnh. Nhưng nếu nhìn kỹ hơn..."
✅ Viết thẳng vào phân tích — không cần câu setup mechanics
```

### Pattern 2: Question cascade (3+ câu hỏi liên tiếp)
```
❌ "GDP có thật không? Ai hưởng lợi? Nó ảnh hưởng gì đến bạn?"
✅ Đặt MỘT câu hỏi sắc, rồi đi trả lời nó
```

### Pattern 3: "Nhưng đó mới chỉ là bề mặt..."
AI transition cliché.
```
❌ "Nhưng đó mới chỉ là bề mặt. Bây giờ chúng ta sẽ nhìn sâu hơn."
✅ Đi thẳng vào layer tiếp theo bằng content — "Cán cân thương mại kể câu chuyện khác."
```

### Pattern 4: Mở bằng "Hãy tưởng tượng..."
```
❌ "Hãy tưởng tượng nền kinh tế là một chiếc xe..."
✅ Nếu cần ẩn dụ, dùng tự nhiên trong câu, không mở bằng "hãy tưởng tượng"
```

### Pattern 5: "Đó là [danh từ trừu tượng]." đứng cuối đoạn
```
❌ "Đó là nghịch lý." / "Đó là sự thật." / "Đó là bài học."
✅ Chốt bằng insight cụ thể thay vì dán nhãn
```

### Pattern 6: Parallel structure lặp [liệt kê 3 cái] quá đều
```
❌ "Tiền ngoài chảy vào. Tiền trong chưa chảy ra. Đó là nghịch lý."
❌ "Nó nhấc đồng tiền... kéo nó ra khỏi... và phân bổ lại cho..." (3 hành động song song đều nhịp)
✅ Phá nhịp — một câu dài, một câu ngắn, một câu chốt khác tone
✅ "Đồng tiền không biến mất. Nó chuyển chỗ. Từ tài khoản tiết kiệm sang quán ăn ven biển Nha Trang."
```

## 4. Transition bị cấm

| ❌ Cấm | ✅ Thay thế |
|---|---|
| "Nhưng đó mới chỉ là bề mặt" | Đi thẳng vào ý tiếp |
| "Bây giờ đến phần gây tranh cãi nhất" | Để nội dung tự gây tranh cãi |
| "Và đây là chỗ mọi thứ thay đổi" | Viết sự thay đổi, không cần annoucement |
| "Bạn đã thấy vấn đề rồi. Câu hỏi là..." | Chuyển bằng logic tự nhiên |
| "Phần tiếp theo sẽ khiến bạn..." | Bỏ — tự promotion |
| "Đây là chỗ [A] đáng để nhìn" | Bỏ — sáo rỗng. Đẩy data của [A] lên luôn. |
| "Đây là điểm nhiều người hay đọc quá nhanh" | Bỏ mẫu câu dán nhãn chê trách đám đông lặp lại. |
| "Điểm đáng nói là..." | Quá mòn, dùng vô tội vạ. |
| "Từ đây mới thấy..." | Quá mòn, văn phong trả bài. |
| "Nếu chapter trước cho thấy X, thì..." | Transition cơ học, cấm dùng từ refer cấu trúc văn bản. |
| "Nói gọn..." / "Nói cách khác..." | Không cấm hoàn toàn, nhưng CẤM LẶP nếu đã dùng rồi. Tốt nhất là bỏ. |

## 5. Nguyên tắc thay thế tổng quát

### Thay vì giật tít → Để dữ liệu tự nói
Số liệu mạnh không cần câu setup "sự thật gây sốc". Nêu thẳng con số, cho context, để khán giả tự choáng.

### Thay vì lên lớp → Chia sẻ phân tích
"Bạn đang hiểu sai" → "Nếu chúng ta nhìn từ góc khác..."

### Thay vì template → Mỗi video có cấu trúc riêng
Không có lý do gì chủ đề GDP phải có cùng cấu trúc hook với chủ đề OpenAI hay Vận 9.

### Thay vì announcement → Content
"Và đây là phần quan trọng nhất" = bạn đang nói với khán giả rằng những gì trước đó KHÔNG quan trọng. Thay vào đó: viết phần quan trọng cho hay, khán giả tự biết.

## 6. Cách dùng file này trong pipeline
- **chapter_writer**: scan mỗi chapter sau khi viết nháp
- **hook_engine**: đối chiếu mỗi hook trước khi chốt
- **oral_polisher**: check round cuối trước merge
- **quality_director**: dùng làm checklist phê bình

## 7. Cấm Pha Tiếng Anh Vào Tiếng Việt VÀ Biệt Ngữ Kỹ Thuật Hẹp (NGHIÊM CẤM)

Kịch bản voiceover là tiếng Việt. **NGHIÊM CẤM** chèn từ tiếng Anh hoặc các biệt ngữ kỹ thuật viết tắt chuyên ngành hẹp (AWS, Azure, GCP, PUE, HPC, DPPA, VRAM, Inference, Token...) vào câu tiếng Việt cho đại chúng mà không có diễn giải. Đối với tên dịch vụ như AWS, Azure, hãy ưu tiên dùng tên mẹ đại chúng (Amazon, Microsoft) để người xem bình thường đều hiểu ngay. Chỉ được phép giữ **tên riêng** (NVIDIA, TSMC, Dat Bike, NextTech, F.C.C, Warren Buffett, Silicon Valley...).

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| pivot | chuyển hướng |
| pattern | quỹ đạo, mô hình lặp |
| builder | người xây |
| showman | người diễn |
| founder | nhà sáng lập |
| demo | trình diễn |
| follow | theo dõi |
| follower | người theo dõi |
| KOL | người có ảnh hưởng trên mạng |
| KPI | chỉ tiêu đo lường |
| flex | khoe |
| show (danh từ) | chương trình |
| marketing | quảng cáo, tiếp thị |
| moat | hào phòng thủ (không cần để tiếng Anh kèm) |
| venture / strategic / institutional | mạo hiểm / chiến lược / tổ chức |
| fintech | công nghệ tài chính |
| logistics | vận chuyển |

**Nguyên tắc:** Nếu một từ tiếng Anh có từ tiếng Việt tương đương tự nhiên, BẮT BUỘC dùng tiếng Việt. Pha trộn ngôn ngữ trong voiceover làm mất uy tín chuyên gia.
