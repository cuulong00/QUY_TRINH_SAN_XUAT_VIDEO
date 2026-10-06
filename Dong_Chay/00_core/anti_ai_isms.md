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

## 3b. Dấu hiệu cấu trúc (chuyển thể từ blader/humanizer, giấy phép MIT)

Văn máy nghe giả không phải vì từng câu sai, mà vì nó luôn chọn phương án "an toàn cho mọi người nghe": câu nào cũng cân, đoạn nào cũng có câu chốt, ý nào cũng được nối bằng một cụm nghe sâu. Người viết thật chọn cho một người nghe cụ thể, nên lựa chọn không đều và cụ thể. Mục này bắt các dấu hiệu ở cấp cấu trúc mà danh sách từ cấm (§2) không bắt được.

Hai nhóm. **Nhóm mạnh:** thấy một lần là xét sửa. **Nhóm yếu:** đứng một mình thì bình thường, chỉ sửa khi hai dấu hiệu trở lên dồn vào cùng một đoạn hoặc cùng một dấu hiệu lặp dày trong chương.

### Nhóm mạnh
| # | Dấu hiệu | Ví dụ lỗi | Giữ khi | Sửa thế nào |
|---|---|---|---|---|
| S1 | "Không phải X, mà là Y" | "Vấn đề không nằm ở giá xe, mà ở niềm tin." | Vế "không phải" sửa một niềm tin mà khán giả THẬT SỰ đang có (đã có trong nguồn, báo chí, số đông), và cả hai vế đều mang thông tin | Nói thẳng Y kèm bằng chứng. Tránh dùng lặp lại làm người nghe thấy khuôn |
| S2 | Câu chốt đứng riêng, chuỗi câu cụt | "Đó là cái giá." · "Không lối thoát. Không đường lui." | Câu ngắn mang thêm một dữ kiện hoặc một hệ quả mới ("Mỗi ngày, lãi vay là 113 tỷ đồng.") | Nếu câu chỉ nén lại ý đoạn vừa nói thì bỏ. Không kết hai đoạn liền nhau bằng câu chốt |
| S3 | Câu nghe sâu sắc | "Cốt lõi của vấn đề là…" · "Suy cho cùng…" · "Bài học ở đây là…" · "X là ngôn ngữ của Y" | Không có | Nói thẳng nội dung. Nếu bỏ câu đi mà đoạn không mất thông tin, bỏ |
| S4 | Rào đón trước khi vào ý | "Hãy cùng nhìn vào…" · "Điều bạn cần biết là…" · "Để hiểu điều này, chúng ta cần quay lại…" | Không có | Bắt đầu bằng chính dữ kiện hoặc câu hỏi |
| S5 | Cãi với người không tồn tại | "Nhiều người lầm tưởng rằng…" | Có nguồn cho thấy niềm tin đó có thật | Xem `00_core/voice_dna.md` §2.1 (chống bù nhìn rơm) |
| S6 | Mượn uy tín không tên | "Giới chuyên gia nhận định…" · "Nhiều ý kiến cho rằng…" · "Theo giới phân tích…" | Không có | Nêu tên nguồn có trong vault, hoặc chuyển thành nhận định của kênh (tầng đặt cược, `00_core/stance_and_judgment.md` §5) |
| S7 | Đuôi câu gắn thêm cho sâu | "…, cho thấy tầm nhìn chiến lược dài hạn." · "…, góp phần khẳng định vị thế." · "…, mở ra một chương mới." | Không có | Cắt đuôi. Nếu thật sự cho thấy điều gì, viết thành câu riêng kèm bằng chứng |

### Nhóm yếu
| # | Dấu hiệu | Ví dụ | Ghi chú |
|---|---|---|---|
| W1 | Bộ ba gượng ép | ba tính từ, ba hành động song song đều nhịp | Xem Pattern 6. Giữ khi nội dung thật sự có ba ý |
| W2 | Lặp cách mở câu | ba câu liền mở bằng "Nó…", "Đó là…", "Và…" | Đổi chủ ngữ hoặc gộp câu |
| W3 | Chồng lớp rào đón | "có thể phần nào", "dường như có lẽ", "ở một mức độ nào đó" | Một mức chắc chắn cho một câu, theo ba tầng giọng |
| W4 | Phóng đại tầm quan trọng | "bước ngoặt lịch sử", "kỷ nguyên mới", "đóng vai trò then chốt", "là minh chứng rõ nét" | Thay bằng con số cho thấy quy mô |
| W5 | Liên hệ mơ hồ | "gắn liền với", "liên quan mật thiết đến", "có tác động đến", "điều đó phản ánh…" | Nói rõ tác động gì, theo chiều nào, bao nhiêu |
| W6 | Né động từ "là", "có" | "đóng vai trò là", "được xem như là", "đóng vai trò như một" | Viết "là" |
| W7 | Giải thích lại điều khán giả vừa nghe | nhắc lại bối cảnh đã nói ở chương trước | Xem `.agents/rules/final-merge.md` |

### Khi nào KHÔNG sửa (đặc thù lời thoại)
Hai tài liệu gốc viết cho văn đọc bằng mắt. Lời nói cần thêm một ít chỗ tựa cho tai:
- Nhắc lại con số chính một lần khi chuyển sang movement mới, để người nghe bám lại.
- Câu ngắn nhấn nhịp có mang số hoặc tên.
- Nhận định và sự phân vân thật của kênh ở tầng đặt cược. Không làm phẳng thành giọng trung tính.
- Câu hỏi mở cuối tập theo chế độ B (`00_core/stance_and_judgment.md` §1b).

**Kỷ luật dữ kiện khi sửa:** chỉ đổi cách nói. Không thêm số, tên, ngày, trích dẫn nào không có sẵn trong chương gốc hoặc `research_vault/`.

### Soi rồi đọc (chapter và Pha 10–11)
Bảng chuyển từ cổng đếm sang hai lớp (user duyệt 06/10/2026):
1. **Lớp soi:** Liệt kê mọi câu khớp dấu hiệu S1–S7 và nhóm yếu. Lớp này là đèn báo, không có ngưỡng đạt/trượt. Dùng máy (grep, script) để soi nhanh và đủ.
2. **Lớp phán:** Đọc từng câu bị soi ra trong đoạn của nó: câu có mang dữ kiện hoặc hệ quả mới không, và có nghe như người có nghề đang nói không?
   - Không: sửa, kể cả khi chỉ xuất hiện 1 lần.
   - Có: giữ, kể cả khi xuất hiện nhiều lần.
   - Kết luận ghi vào chỉ tiêu IX Câu cho tai và VII Giọng của `00_core/narrative_craft_rubric.md`, có trích câu.

| Dấu hiệu | Lớp soi (máy hoặc quét) | Lớp phán (đọc trong đoạn) |
|---|---|---|
| S1 "không phải X mà là Y" và biến thể ("chứ không phải", "chứ chẳng phải"…) | Liệt kê mọi câu khớp | Câu có mang dữ kiện mới không? Hai câu cùng dạng ở gần nhau có làm người nghe thấy khuôn không? Sửa khi đọc thấy khuôn. |
| S2 câu chốt đứng riêng | Liệt kê câu ngắn kết đoạn | Câu mang dữ kiện hay hệ quả mới, hay chỉ nén lại ý vừa nói? |
| S3 câu nghe sâu sắc | Liệt kê câu chứa từ khóa "cốt lõi là", "suy cho cùng", "bài học là", "X là ngôn ngữ của Y" | Bỏ nếu không mất thông tin. Nếu có ý thật, viết thẳng vào dữ kiện. |
| S4 rào đón trước khi vào ý | Liệt kê các câu mở đầu kiểu "hãy cùng nhìn vào", "điều bạn cần biết là" | Bỏ phần rào đón, bắt đầu ngay bằng dữ kiện hoặc câu hỏi. |
| S5 cãi với người không tồn tại | Liệt kê các câu "nhiều người lầm tưởng rằng..." | Có nguồn thực chứng trong vault chứng minh niềm tin sai lệch đó có thật không? Nếu không, bỏ vế gán ghép. |
| S6 mượn uy tín không tên | Liệt kê "giới chuyên gia nhận định", "theo giới phân tích" | Có tên nguồn cụ thể trong vault không? Nếu không, chuyển thành nhận định có trách nhiệm của kênh (đặt cược). |
| S7 đuôi câu gắn thêm cho sâu | Liệt kê các đuôi "cho thấy tầm nhìn...", "khẳng định vị thế...", "mở ra chương mới..." | Cắt đuôi sáo rỗng. Nếu thật sự có hệ quả, viết thành câu độc lập có bằng chứng. |
| Nhóm yếu W1–W7 | Quét bộ ba gượng ép, lặp cách mở câu, chồng lớp rào đón, phóng đại, liên hệ mơ hồ, né động từ là/có, giải thích lại | Đoạn văn có bị vướng vào thói quen văn máy làm loãng ý không? Sửa để câu văn gọn, chắc và có người đang nghĩ. |

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
- **chapter_writer**: scan mỗi chapter sau khi viết nháp theo hai lớp soi và phán của §3b
- **compliance_council**: soi và đọc từng câu ở §3b trên từng chương khi chấm Pha 10–11
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
