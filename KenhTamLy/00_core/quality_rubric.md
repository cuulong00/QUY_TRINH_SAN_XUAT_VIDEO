# quality_rubric.md

## 1. Mục đích của file này
File này dùng để chấm chất lượng của một video script trước khi đưa sang thu âm và dựng hình.
Mục tiêu không phải là “tìm lỗi cho có”, mà là giữ mặt bằng chất lượng ổn định, tránh chuyện script hay ở đầu nhưng yếu về sau, hoặc packaging hứa một đằng mà nội dung trả một nẻo.

## 2. Cách dùng
Chấm theo thang 105 điểm.
Mỗi tiêu chí có mô tả rõ.
Sau khi chấm, kết luận theo ngưỡng:
- **95–105**: rất mạnh, có thể dùng sau chỉnh nhẹ.
- **89–94**: đủ tốt để sản xuất, nhưng nên tối ưu vài điểm.
- **84–88**: trung bình khá, cần sửa những chỗ yếu rõ ràng.
- **dưới 84**: chưa nên sản xuất.

Ngoài điểm số, QA bắt buộc phải trả verdict production:
- `PASS`
- `BLOCK`

Quy tắc: không rewrite cả bài nếu không cần.
Chỉ tập trung sửa các mục có điểm thấp nhất trước.
Nhưng nếu vi phạm hard gate thì phải BLOCK dù câu chữ nghe vẫn mượt.

## 3. Bảng chấm điểm

### A. Packaging alignment — 10 điểm
Câu hỏi:
- Title, thumbnail và hook có nói cùng một lời hứa không?
- Hook có xác nhận đúng tension đã mở ở packaging không?
- Metadata có hứa quá điều script trả được không?

### B. Hook và opening architecture — 15 điểm
Câu hỏi:
- Hook có chạm đúng pain không?
- Hook có mở tò mò không?
- Hook có đúng giọng kênh không?
- Opening có giữ được cấu trúc Hook -> Intro kênh -> CTA mềm -> Bridge vào thân bài không?
- Family opening có hợp đúng loại episode không?
- Opening có tươi mới hay nghe như một template công nghiệp quen tay?
- Nếu dùng câu hỏi tu từ, đó có phải lựa chọn có chủ ý thay vì default không?

### C. Độ rõ của brief và audience fit — 10 điểm
Câu hỏi:
- Script có đang nói với một persona rõ không?
- Nỗi đau có cụ thể không?
- Ví dụ và ngôn ngữ có đúng người nghe mục tiêu không?

### D. Độ sâu nhận thức — 20 điểm
#### D1. Paradox quality — 5 điểm
- Video có ít nhất 1–2 nghịch lý THẬT không?
- Nghịch lý có tạo cognitive tension không?

#### D2. Layer depth — 5 điểm
- Script có sự liên kết hữu cơ giữa con người thật (cảnh đời) và cơ chế (khoa học/tuệ giác) mà không bị gò ép thiển cận theo khuôn rập 3 bước không?

#### D3. Emotional turn count — 5 điểm
- Có ít nhất 2–3 khoảnh khắc “À, thì ra vậy” trong toàn bài không?

#### D4. Authenticity (micro-situations) — 5 điểm
- Mỗi chapter có ít nhất 1 cảnh đời cụ thể không?
- Ví dụ có gần persona không?

### E. Cấu trúc long-form — 10 điểm
Câu hỏi:
- Outline có logic không?
- Mỗi chương có vai trò riêng không?
- Có open loop và bridge rõ không?
- Nửa sau có còn lực không?

### F. Retention engineering — 15 điểm
Câu hỏi:
- Người nghe có được kéo đi về mặt cảm xúc không?
- Có mini re-hooks hay retention moves ở giữa video không?
- Có đoạn nào quá trừu tượng và dễ rớt nghe không?
- Có cao trào nhận thức ở nửa sau không?
- Lời hứa mở đầu có được trả dần trong thân bài không?

### G. Continuity và chống lặp — 10 điểm
Câu hỏi:
- Có lặp cùng một insight quá nhiều lần không?
- Ví dụ, ẩn dụ, cụm từ có bị lặp không?
- Từ đầu đến cuối có cảm giác cùng một hành trình không?

### H. Behavioral safety — 10 điểm
Câu hỏi:
- Có bịa nghiên cứu, số liệu, authority không?
- Có overclaim causal quá tay không?
- Có pseudo-clinical overreach hoặc diagnosis creep không?
- Có shame-based framing hoặc hứa vượt quá khả năng script không?
- Có phân biệt được `evidence_supported`, `clinically_informed`, `behavioral_inference`, `life_observation`, `reflective_prompt` không?

### I. Voiceover readiness — 5 điểm
Câu hỏi:
- Câu có dễ đọc lên không?
- Có nhịp nghỉ không?
- Đoạn văn có gọn không?
- Từ ngữ có gần với lời nói không?
- Có tránh spoken chapter labels trong prose không?

## 4. Mẫu phiếu chấm nhanh
```text
Packaging alignment: /10
Hook + opening: /15
Audience fit: /10
Depth — Paradox quality: /5
Depth — Layer depth: /5
Depth — Emotional turns: /5
Depth — Authenticity: /5
Structure: /10
Retention engineering: /15
Continuity: /10
Behavioral safety: /10
Voiceover readiness: /5

TOTAL: /105

Điểm mạnh nhất:
-
-

Điểm yếu nhất:
-
-

Ưu tiên sửa trước:
1.
2.
3.
```

## 5. Luật ưu tiên khi sửa
Nếu tổng điểm chưa cao, hãy sửa theo thứ tự ưu tiên sau:
1. Behavioral safety
2. Packaging alignment
3. Hook + opening
4. Structure
5. Retention engineering
6. Continuity
7. Voiceover readiness
8. Chỉ sau đó mới chỉnh câu chữ đẹp hơn

Lý do: một script an toàn, đúng cấu trúc, đúng lời hứa và dễ nghe nhưng chưa thật đẹp vẫn dùng được.
Ngược lại, một script đẹp mà sai safety, mismatch packaging, hoặc lỏng retention là không dùng được.

## 6. Dấu hiệu phải yêu cầu viết lại hẳn một chương
Chỉ viết lại hoàn toàn một chương khi gặp một trong các trường hợp sau:
- chương làm sai vai trò của outline,
- chương lặp lại quá 50% ý của chương trước,
- chương drift tone khỏi giọng kênh,
- chương khiến safety risk tăng cao,
- chương làm gãy mạch cảm xúc,
- chương không phục vụ retention move hoặc payoff target đã được outline khóa.

## 7. Red flags phải gắn cảnh báo ngay
Các dấu hiệu đỏ:
- title/thumbnail hứa một đằng nhưng opening đi một nẻo,
- mở đầu chung chung,
- opening nghe như template hàng loạt hoặc quá công nghiệp,
- dùng câu hỏi tu từ như default mà không có lý do rõ,
- topic cần direct clarification nhưng opening quá mềm hoặc thiếu lập trường,
- dùng nhiều từ đẹp nhưng không có pain cụ thể,
- nửa sau chuyển sang giảng lý thuyết,
- kết thúc thành khẩu hiệu,
- toàn bài nghe như một giọng, không có cao thấp,
- editor khó dựng vì nội dung quá trừu tượng,
- đoạn nào cũng đúng nhưng không có discovery thật.

## 8. Chuẩn đầu ra “sẵn sàng sản xuất”
Một script được xem là sẵn sàng sản xuất khi:
- tổng điểm >= 89,
- behavioral safety >= 8/10,
- packaging alignment >= 8/10,
- hook + opening >= 12/15,
- depth tổng >= 16/20,
- retention engineering >= 11/15,
- voiceover readiness >= 4/5,
- runtime contract đạt,
- architecture coverage đạt,
- merge preservation đạt.

### Hard gates phải BLOCK ngay
Các trường hợp sau phải trả verdict `BLOCK` dù câu chữ nghe ổn:
- tổng điểm < 89
- behavioral safety < 8/10
- packaging alignment < 8/10
- hook + opening < 12/15
- depth tổng < 16/20
- retention engineering < 11/15
- voiceover readiness < 4/5
- final merged words/minutes vi phạm runtime contract
- drafted chapter set thấp hơn floor đã khóa
- preservation ratio sau merge thấp hơn floor
- opening architecture bị gãy
- chapter-role coverage không đủ
- payoff requirements hoặc ending destination không được trả đúng

## 9. Nguyên tắc cuối cùng
Không chọn script vì nó “nghe hay lúc mới đọc”.
Hãy chọn script vì nó:
- giữ được người nghe,
- không phản bội tinh thần kênh,
- không phản bội lời hứa đã mở ở packaging,
- không làm người đang đau hiểu sai hơn về mình,
- và vẫn sống được khi đi qua giọng đọc thật.
