# Khung chấm nghệ thuật kịch bản (Narrative Craft Rubric)

> Khung này tách chất chuyện thành 10 chỉ tiêu, như hội đồng chấm kịch bản chuyên nghiệp, thay thế lượt đọc ba kết luận chung chung. Nó chỉ rõ kịch bản thiếu gì và thiếu ở đâu.
> Là trụ cột **K. Narrative Craft** của `00_core/quality_rubric.md` (20/110 điểm) và là điều kiện cứng: K không đạt mốc ở mục 6 thì tập không qua Pha 10, dù tổng điểm cao.

## 0. Không chỉ tiêu nào chấm bằng đếm
Chất chuyện được chấm bằng tư duy của người đọc, có trích câu làm bằng chứng. Không chỉ tiêu nào quy về số con số, số câu hỏi, số cảnh hay độ dài câu. Lý do: chấm bằng phép đếm thì người viết tối ưu theo phép đếm; bớt số mà vẫn đọc kết quả, thêm câu hỏi mà không ai muốn biết đáp án. Các cổng kỹ thuật (trần 150 ký tự, số khớp sổ, từ cấm) nằm ngoài khung này.

## 1. Phạm vi áp dụng
| Sản phẩm | Cấp chấm | Khi nào | Ai chấm |
|---|---|---|---|
| `07_outline.md` | Cấp bài (Phiếu A) | Pha 4, trước khi xin user duyệt dàn ý | Người khác ngoài người dựng dàn ý chấm mù trước khi xin duyệt (người dựng dàn ý tự soi rà soát câu yếu, không tính điểm) |
| `chapter_XX.md` | Cấp chương (Phiếu B, tự soi chỗ yếu) + cập nhật bảng gieo/gặt của Phiếu A | Pha 7, `chapter_writer/SKILL.md` Bước 3b | Người viết tự soi để sửa trước khi nộp (không tính điểm, không làm cổng) |
| Toàn bộ `chapter_XX.md` | Cả hai cấp, đầy đủ | Pha 10–11, `compliance_council/SKILL.md` Khóa 6 | Critical Auditor chấm mù (điểm chính thức cho K) |
| `voiceover.md` | Chấm lại cấp bài | Sau Pha 8 (merge) | Người khác ngoài người merge chấm mù |

Kết quả chấm của mỗi tập lưu ở `episodes/[slug]/11_narrative_craft_scorecard.md` theo khuôn `02_templates/masterpiece_pipeline/11_narrative_craft_scorecard_template.md`. Bắt buộc với mọi tập mới; tập đã đăng không phải bổ sung.

## 2. Mười chỉ tiêu
Mỗi chỉ tiêu chấm 1–5. Mốc 2 và 4 là mức giữa hai mốc mô tả.

| # | Chỉ tiêu | Câu hỏi chấm | 1 điểm | 3 điểm | 5 điểm | Cấp |
|---|---|---|---|---|---|---|
| I | Câu hỏi kịch tính trung tâm | Có một câu hỏi người xem muốn biết đáp án, đặt trong 60 giây đầu, nhắc lại khi đổi màn, trả ở cao trào? | Không có; video là một chủ đề, không phải một câu hỏi | Có nhưng mờ, hoặc nhiều câu hỏi tranh nhau | Một câu hỏi sắc; mọi chương đều đẩy nó đi | Bài |
| II | Mức cược | Người xem hiểu được hay mất gì nếu đáp án là A hay B, và với ai? (Loại B/C: cái giá cho nền kinh tế, doanh nghiệp, một thế hệ; không ép túi tiền cá nhân) | Không nói cái giá | Nói chung chung ("ảnh hưởng lớn") | Cái giá cụ thể, bằng dữ kiện hoặc cảnh, được nâng dần qua các chương | Bài |
| III | Gieo và gặt (khoảng trống thông tin) | Người kể gieo điều chưa giải thích (con số lạ, mâu thuẫn, chi tiết) rồi gặt đúng lúc; hạt nào gieo cũng được gặt, không gặt thứ chưa gieo? | Thông tin đưa theo thứ tự tài liệu, không có gì được gieo | Có gieo nhưng gặt sớm, hoặc quên gặt | Ít nhất một hạt gieo ở chương 1 được gặt ở cao trào; người nghe đoán được nửa giây trước khi người kể nói ra | Bài |
| IV-a | Cú lật trong chương | Có chỗ cách hiểu của người nghe bị đổi bởi dữ kiện: cách hiểu cũ dựng trước, dữ kiện làm đổi đến sau? | Không có; chương là một danh sách | Có lật nhưng người kể nói đáp án trước khi dựng cách hiểu cũ | Cách hiểu cũ được dựng thật (ở dạng mạnh nhất), rồi mới đổ | Chương |
| IV-b | Cao trào | Cú lật lớn nhất của tập nằm ở đâu và có đủ sức nặng không? | Không có cú lật lớn, hoặc nằm ở 2 phút cuối | Có cú lật lớn nhưng lệch khỏi vùng 50–70% thời lượng, hoặc nói đáp án trước | Cú lật lớn nhất ở 50–70% thời lượng, gặt hạt gieo từ đầu và đổi cách đọc cả tập | Bài |
| V | Vật chứng so với tóm tắt | Chi tiết cụ thể có thật (một văn bản, một công trình, một quyết định có ngày giờ, một con số đặt cạnh con số khác) đi trước, nghĩa đến sau? Cấm nhân vật bịa. Đây KHÔNG phải chỉ tiêu tả cảnh (xem định nghĩa dưới bảng). | Toàn câu khái quát và bảng số; ẩn dụ đứng thay vật chứng | Có chi tiết nhưng dùng minh họa sau khi đã kết luận | Chi tiết đi trước, nghĩa đến sau; có ít nhất một chi tiết đắt | Chương |
| VI | Chủ thể và xung đột | Có người hay tổ chức muốn gì, bị cản bởi gì, đánh đổi gì? Cơ chế được kể qua động cơ các bên, không qua định nghĩa? | Chỉ có "nền kinh tế", "số liệu", "khu vực" | Có các bên nhưng không rõ họ muốn gì | Các bên có động cơ, cản trở và đánh đổi rõ; phía phản biện ở dạng mạnh nhất | Chương |
| VII | Giọng và lập trường | Có một người thật đang nghĩ: nhận định được đặt cược, nói rõ mức chắc, không trốn sau "các chuyên gia cho rằng", không giảng đạo (`00_core/stance_and_judgment.md`)? | Tổng hợp vô danh | Có nhận định nhưng rào đón át ý | Nhận định rõ, có điều kiện có thể sai, chỉ xuất hiện ở chỗ dữ kiện đã đủ | Cả hai: chương (có nhận định không); bài (nhận định nhất quán và đúng chế độ kết không) |
| VIII | Nhịp | Tốc độ đổi theo ý: chậm ở cú lật, nhanh ở chuỗi bằng chứng; không đoạn dài nào một nhịp; chuyển chương bằng câu hỏi, không bằng tóm tắt? | Đều một nhịp | Có đổi nhưng ngẫu nhiên | Nhịp phục vụ ý; người nghe không bao giờ hỏi "sao còn đoạn này" | Chương |
| IX | Câu cho tai | Theo `chapter_writer/SKILL.md` mục "Viết Câu Cho Tai": hiểu ở lần nghe đầu, rõ ai làm gì, dữ kiện trước nhận xét sau, không AI-isms, không câu nghe sâu sắc rỗng, không đọc mục lục? | Văn viết đọc to | Nghe được nhưng có câu phải nghe lại | Nghe như người có nghề đang nói chuyện | Chương |
| X | Kết và nghĩa | Kết trả đúng câu hỏi I theo chế độ đã chọn (A chốt lập trường / B kết mở có cấu trúc), để lại một cách nhìn mới, không tóm tắt lại, không giảng đạo? | Tóm tắt lại, hoặc lửng | Trả lời nhưng không mở ra gì | Người xem rời đi với một công cụ để tự theo dõi hoặc một cách đọc họ chưa có | Bài |

**Vật chứng khác tả cảnh.** Tả cảnh là câu dựng không khí, thời tiết, âm thanh, cảm giác hay tính từ hình ảnh mà không mang dữ kiện ("ánh đèn công trường hắt lên nền trời đêm"). Lối này rườm rà, điệu, không hợp khán giả đã có tuổi, và bị hạn chế: chỉ dùng khi một chi tiết hình ảnh có nguồn tự nó là dữ kiện. Vật chứng là sự thật có nguồn đặt trước mắt người nghe; một câu như "Báo cáo số 818 của Bộ Tài chính ghi vốn trung ương mới giải ngân 44,1%, địa phương 73,6%" là vật chứng, không phải tả cảnh. Chỉ tiêu V chấm vật chứng; câu tả cảnh không làm tăng điểm V và nếu rườm rà thì trừ ở IX Câu cho tai.

**Không có khuôn kể chung.** Giá trị nghệ thuật của phim tài liệu không đến từ một kỹ thuật cố định (tả cảnh, mở bằng nghịch lý, hay ba nhịp). Mỗi chủ đề phải được hình dung từ đầu xem kể thế nào thì hấp dẫn với chính khán giả của kênh: theo dấu một đồng tiền, giải một câu đố, đặt hai con đường cạnh nhau, đi ngược từ một hệ quả… Khung này chấm kết quả (người nghe có muốn biết, có được dẫn đi tìm, có đổi cách hiểu không), không bắt buộc cách làm.

Cột phụ cấp chương: **"Chương này đẩy câu hỏi trung tâm đi bao xa" (1–5)**. 1: chương đứng ngoài câu hỏi I; 3: chương thêm thông tin liên quan nhưng câu hỏi vẫn ở chỗ cũ; 5: sau chương này người nghe hiểu câu hỏi khác đi hoặc tiến gần đáp án rõ rệt. Cột này không tính vào trung bình; nó là bằng chứng cho chỉ tiêu I ở cấp bài.

## 3. Quy trình chấm (5 bước)
1. **Đọc trọn, không ghi chép.** Đọc cả bài (hoặc cả dàn ý) một mạch như người xem lần đầu, không mở brief, sổ dữ kiện hay bản tự soi. Không ghi điểm giữa chừng: ghi chép khi đọc biến lượt đọc thành lượt soát lỗi và mất cảm giác của người nghe.
2. **Chấm cấp bài** (Phiếu A): I, II, III, IV-b, X, cùng VII cấp bài, và điền bảng gieo/gặt.
3. **Chấm cấp chương** (Phiếu B): mỗi chương một dòng gồm IV-a, V, VI, VII, VIII, IX và cột "đẩy câu hỏi đi bao xa". Được đọc lại từng chương ở bước này.
4. **Đối chiếu hai cấp** theo bảng ở mục 5.
5. **Kết luận và lệnh sửa** theo mục 6: chỉ đích danh chương, chỉ tiêu, câu lỗi, một câu viết lại mẫu.

Quy định bằng chứng:
- Mọi điểm 4–5 và mọi điểm 1–2 phải trích câu (≤ 25 từ). Điểm 4–5 không có trích dẫn thì hạ về 3.
- Điểm 1–2 phải ghi câu lỗi và một câu đề xuất viết lại.
- Người chấm so với ngân hàng đoạn mẫu ở mục 7, không chấm theo cảm giác chung.

Tự soi và chấm mù:
- Người viết (hoặc người dựng dàn ý) tự soi để rà soát: chỉ tiêu nào yếu, trích câu, vì sao, câu sửa. Tuyệt đối không tự cho điểm, không tính trung bình, không ghi ĐẠT/KHÔNG/PASS. Việc tự soi này không phải điều kiện qua cổng và không tính vào điểm K.
- Điều kiện qua cổng và điểm số chỉ đến từ chấm mù: Critical Auditor (hoặc agent khác ngoài người viết) chấm mù Phiếu B từng chương và Phiếu A cả bài mà không xem bản tự soi trước khi nộp phiếu của mình. Khi có nhiều agent, giao lượt này cho agent hoặc phiên khác với người viết. Dàn ý: Phiếu A do người khác ngoài người dựng dàn ý chấm trước khi xin user duyệt. Chương: chấm mù ở Pha 10 là điều kiện qua cổng và là nguồn tính điểm K. Sau merge: Phiếu A do người khác ngoài người merge chấm.
- Sau khi đã nộp phiếu chấm mù, hai bên đối chiếu: người chấm mù đọc danh sách chỗ yếu của người viết; chỗ nào người viết thấy yếu mà người chấm mù cho 4–5, hoặc ngược lại (người viết không thấy yếu mà chấm mù cho 1–2), thì hai bên đọc lại đúng đoạn đó, ghi điểm thống nhất và lý do vào phiếu. Điểm K lấy từ phiếu chấm mù chính thức (hoặc điểm thống nhất sau đối chiếu).

## 4. Hai phiếu mẫu

### Phiếu A · Cấp bài
| Chỉ tiêu | Điểm | Trích câu (≤ 25 từ) | Nhận xét / lệnh sửa |
|---|---|---|---|
| I Câu hỏi kịch tính trung tâm | | | |
| II Mức cược | | | |
| III Gieo và gặt | | | |
| IV-b Cao trào (vị trí: …% thời lượng) | | | |
| VII Giọng và lập trường (cấp bài; chế độ kết: A/B) | | | |
| X Kết và nghĩa | | | |
| **Trung bình cấp bài** | | | |

Bảng gieo/gặt:
| Hạt gieo (con số lạ, mâu thuẫn, chi tiết) | Chương gieo | Chương gặt | Trạng thái (gặt đúng lúc / gặt sớm / chưa gặt / gặt thứ chưa gieo) |
|---|---|---|---|
| | | | |

### Phiếu B · Cấp chương
Mỗi ô ghi `điểm · "trích câu ≤ 25 từ"`. Ô điểm 3 được để trống trích dẫn.

| Chương | IV-a Cú lật | V Vật chứng | VI Chủ thể | VII Giọng | VIII Nhịp | IX Câu cho tai | Trung bình | Đẩy câu hỏi đi bao xa (1–5) |
|---|---|---|---|---|---|---|---|---|
| CH01 | | | | | | | | |
| CH02 | | | | | | | | |

## 5. Đối chiếu hai cấp
| Hình thái | Cách đọc | Chuyển về |
|---|---|---|
| Cấp bài cao, cấp chương thấp | Dàn ý có câu hỏi, cao trào, gieo/gặt, nhưng chương viết ra không dựng cú lật, không có cảnh, không có chủ thể | Pha 7: viết lại đúng các chương và chỉ tiêu bị điểm thấp, bắt đầu từ bảng nhịp chương (Chặng 2) |
| Cấp chương cao, cấp bài thấp | Từng chương hay riêng lẻ nhưng không cùng đẩy một câu hỏi; hạt gieo không được gặt; kết không trả câu hỏi | Pha 4: sửa dàn ý (câu hỏi trung tâm, vị trí cao trào, bảng gieo/gặt), rồi mới sửa chương |
| Cả hai thấp | Lỗi từ dàn ý lan xuống chương | Pha 4 trước, rồi Pha 7 |
| Cột "đẩy câu hỏi" thấp ở một chương dù chỉ tiêu cấp chương cao | Chương lạc đề hoặc là chương thừa | Pha 4: gộp, cắt hoặc đổi nhiệm vụ chương |

## 6. Mốc ĐẠT và lệnh sửa
Mốc ĐẠT, áp riêng cho từng cấp theo kết quả chấm mù chính thức (hoặc điểm thống nhất sau đối chiếu):
- Không chỉ tiêu nào dưới 3 (cấp chương: không ô nào của chương nào dưới 3).
- Trung bình ≥ 4,0 (cấp bài: trung bình Phiếu A; cấp chương: trung bình mọi ô của Phiếu B).
- Ba chỉ tiêu quyết định "chuyện hay báo cáo" ≥ 4: I (cấp bài), IV (IV-b ở cấp bài, IV-a ở từng chương), V (từng chương). Chương kết theo chế độ B được tính cú lật là phép đặt hai cách đọc cạnh nhau.

Loại ngay (Hard-Fail, nằm trong `quality_rubric.md` §4): cấp bài có I hoặc X dưới 3; hoặc có chương mà IV-a và V cùng ≤ 2.

Điểm K quy về thang 20 của `quality_rubric.md`: K = (trung bình cấp bài + trung bình cấp chương) ÷ 2 × 4, lấy từ kết quả chấm mù chính thức (hoặc điểm thống nhất sau đối chiếu), tuyệt đối không lấy từ bản tự soi của người viết. Đây là phép quy đổi điểm đã chấm, không phải phép đếm trên văn bản.

Mẫu lệnh sửa (mỗi lệnh một dòng):
| Chương | Chỉ tiêu | Câu lỗi (trích nguyên) | Vì sao | Một câu viết lại mẫu |
|---|---|---|---|---|
| CH03 | IV-a Cú lật | [Mẫu lỗi đọc bảng số]: "Tăng trưởng đạt [X]% do ngành A tăng [Y]%, ngành B tăng [Z]%..." | Đáp án được đọc theo thứ tự bảng, không có cách hiểu cũ nào bị đổi | [Mẫu sửa bằng phép tách]: "Muốn biết mức tăng [X]% thực sự đến từ đâu, hãy thử một phép tách: bỏ ngành A ra, phần còn lại chưa tới một nửa." |

## 7. Ngân hàng đoạn mẫu
Đoạn 1 điểm (hoặc điểm thấp) và điểm 5 dùng mô tả kỹ thuật hoặc [CHỜ USER CHỌN MẪU]. Không chép lời kịch bản của kênh tham chiếu; chỉ mô tả kỹ thuật. Khi một tập sau có đoạn đạt 5 ở chỉ tiêu nào, thay mô tả kỹ thuật bằng đoạn đó và ghi nguồn.

### I. Câu hỏi kịch tính trung tâm
- **Điểm thấp (Mô tả kỹ thuật):** Mục lục đứng thay câu hỏi: người nghe biết video sẽ nói về chủ đề gì nhưng không biết mình đang đi tìm lời giải cho mâu thuẫn nào.
- **Mức 4 (Mô tả kỹ thuật):** Câu hỏi có thật về động lực kéo chỉ số và tính bền vững của chu kỳ, nhưng chưa được nhắc lại khi chuyển màn.
- **Mức 5 (Mô tả kỹ thuật):** Câu hỏi sinh ra từ hai sự thật va nhau mà người xem vừa thấy, đặt trước giây 60; mỗi lần đổi màn người kể quay lại đúng câu hỏi ấy với một hiểu biết mới ("giờ ta biết X, nhưng…"); cao trào trả lời nó bằng một dữ kiện, không bằng một lời tuyên bố.

### II. Mức cược
- **Điểm thấp (Mô tả kỹ thuật):** Liệt kê các mục tiêu chính sách hay con số kế hoạch chung chung mà không nêu rõ ai sẽ phải trả giá hoặc mất gì nếu mục tiêu thất bại.
- **Mức 5 (Mô tả kỹ thuật):** Cái giá được gọi tên sớm bằng một dữ kiện có chủ thể (ai trả, trả bằng gì, khi nào), rồi nâng dần: mỗi màn thêm một tầng người phải trả hoặc một khoản phải trả lớn hơn; không dùng tính từ ("rất lớn", "nghiêm trọng") thay cho cái giá.

### III. Gieo và gặt
- **Điểm thấp (Mô tả kỹ thuật):** Thông tin đưa theo danh sách cơ quan dự báo tuần tự, không gieo ẩn số từ trước và không gặt lại ở cao trào.
- **Mức 5 (Mô tả kỹ thuật):** Hạt gieo ở chương 1 (một con số lạ hay nghịch lý ngầm), gặt ở chương giữa hoặc cao trào, đúng lúc người nghe ngỡ đã quên nó là một câu hỏi.

### IV. Cú lật (IV-a trong chương, IV-b cao trào)
- **Điểm thấp (Mô tả kỹ thuật):** Đặt câu hỏi rồi lập tức đọc đáp án tuần tự theo bảng thống kê; không có cách hiểu cũ nào được dựng lên để rồi bị lật đổ.
- **Mức 5 (Mô tả kỹ thuật):** Cách hiểu thông thường được dựng lên ở phiên bản mạnh nhất cho người nghe tin trước, rồi một dữ kiện đối chứng thứ hai từ cùng nguồn làm sụp đổ nó.

### V. Vật chứng so với tóm tắt
- **Điểm thấp (Mô tả kỹ thuật):** Ẩn dụ đứng thay cảnh: không có văn bản, số liệu kiểm toán, công trình hay quyết định có thật nào được cho xem.
- **Mức 4–5 (Mô tả kỹ thuật):** Chi tiết định lượng cụ thể (một phép tách dữ liệu, hai mốc số liệu đặt cạnh nhau) đi trước, kết luận bản chất đi sau.
- **Mức 5 (Mô tả kỹ thuật):** Thêm một chi tiết đắt có ngày giờ và nguồn mà người nghe nhận ra ngay là một sự thật cụ thể (một tờ trình, một dòng trong báo cáo kiểm toán đặt cạnh dòng khác), đặt trước lời giải thích; nói bằng dữ kiện, không bằng câu tả không khí.

### VI. Chủ thể và xung đột
- **Điểm thấp (Mô tả kỹ thuật):** Chủ thể là các khái niệm trừu tượng chung chung ("nền kinh tế", "khu vực"); không bên nào có động lực sinh tồn rõ ràng và không có xung đột lợi ích.
- **Mức 5 (Mô tả kỹ thuật):** Mỗi cơ chế được kể qua một bên có thật (cơ quan quản lý, nhóm doanh nghiệp, người ra quyết định) với ba vế: họ muốn gì, cái gì cản họ, họ đã đánh đổi gì để lấy gì; phía phản biện cũng là một bên có động cơ chính đáng, nói ở dạng mạnh nhất. Không phán xét động cơ cá nhân (`stance_and_judgment.md` §4).

### VII. Giọng và lập trường
- **Điểm thấp (Mô tả kỹ thuật):** Thuật lại một báo cáo một cách vô danh, người kể vắng mặt, không có nhận định hay lập trường riêng.
- **Mức 5 (Mô tả kỹ thuật):** Nhận định đặt ngay sau dữ kiện đủ đỡ nó, nói một lần, kèm mức chắc (ba tầng giọng, `stance_and_judgment.md` §5) và điều kiện khiến kênh đổi ý (§6); không rào đón trước ý chính; cả tập giữ một lập trường nhất quán đúng chế độ kết.

### VIII. Nhịp
- **Điểm thấp (Mô tả kỹ thuật):** Các đoạn văn đều đều một nhịp "số liệu, giải thích, số liệu", gây buồn ngủ và đơn điệu.
- **Mức 5 (Mô tả kỹ thuật):** Chuỗi bằng chứng đi nhanh (câu gọn, mỗi câu một manh mối); trước cú lật nhịp chậm lại để người nghe kịp giữ cách hiểu cũ; sau cú lật có một câu đứng riêng mang hệ quả mới; chuyển chương bằng câu hỏi kế tiếp, không bằng tóm tắt.

### IX. Câu cho tai
- **Điểm thấp (Mô tả kỹ thuật):** Câu văn phức hợp nhiều vế, nhiều mốc thời gian và điều kiện lồng nhau khiến người nghe phải tua lại để hiểu.
- **Mức 5 (Mô tả kỹ thuật):** Đạt hai phép thử của mục "Viết Câu Cho Tai" ở mọi đoạn: đọc to không vấp; nghe riêng không cần tài liệu; mỗi câu một ý, rõ ai làm gì, mục đích trước hành động, tên riêng lần đầu có vế giới thiệu.

### X. Kết và nghĩa
- **Điểm thấp (Mô tả kỹ thuật):** Đoạn kết mở bằng việc tóm tắt lại các chương trước một cách máy móc.
- **Mức 5 (Mô tả kỹ thuật):** Kết trả đúng câu hỏi I bằng một dữ kiện hoặc một phép đặt cạnh mới, không nhắc lại đường đi; chế độ A chốt lập trường một lần kèm điều kiện có thể sai; chế độ B trao các cách đọc, biến số quyết định và một công cụ người xem tự dùng được (chỉ báo, câu hỏi để kiểm); không giảng đạo.
