# Chuỗi 4 bước nghiên cứu sơ bộ bằng Gem (user đề xuất 02/10/2026)

Tầng tri thức nền của một đề tài. Mỗi bước kế thừa bước trước. Chạy cả chuỗi trong **cùng một hội thoại Gem** để Gemini tự giữ ngữ cảnh. Mỗi bước lưu nguyên văn ra file riêng.

| Bước | Việc | Chế độ | Ghi chú |
|---|---|---|---|
| 1. Toàn cảnh | vẽ bản đồ hệ thống, chưa kết luận | Deep Research + Tư duy mở rộng | Ở chế độ Deep Research, chỉ dẫn của Gem bị lấn át: cấu trúc mong muốn phải nằm ngay trong câu prompt |
| 2. Nghiên cứu trực tiếp | câu hỏi trung tâm, ≥3 cách giải thích cạnh tranh, bằng chứng ngược | Deep Research + Tư duy mở rộng | Không nhét giả thuyết của mình vào câu hỏi |
| (kiểm) | rút 10–15 dữ kiện và vật chứng then chốt, mở nguồn gốc, lập bản tóm kế thừa | agent | Chặn lỗi di truyền sang bước 3–4 |
| 3. Khía cạnh, câu hỏi, góc tiềm năng viral | xếp hạng theo độ hấp dẫn và độ chắc | Deep Research + Tư duy mở rộng (user chốt 03/10/2026: cả 4 bước đều Deep Research) | Đưa vào chân dung khán giả và tiêu đề thật của kênh nếu có. Chế độ Deep Research lấn át chỉ dẫn của Gem nên cấu trúc mong muốn và bản tóm kế thừa phải nằm ngay trong câu prompt |
| 4. Dàn ý tham khảo | khung chương, mạch kể | Deep Research + Tư duy mở rộng (user chốt 03/10/2026) | Chỉ tham khảo; agent viết không bị buộc theo |

Mọi số liệu Gem đưa ra là manh mối cho tới khi mở nguồn gốc. Mỗi lúc chỉ một agent dùng trình duyệt Gem (cổng 9225).

## Mẫu prompt (thay phần trong <…>)

**Bước 1 — Toàn cảnh (Deep Research)**
> Tôi muốn hiểu toàn cảnh câu chuyện này: <tóm sự kiện 2–3 câu, kèm đường dẫn bài gốc>. Trước khi đi vào chi tiết, hãy vẽ cho tôi bức tranh toàn cảnh: các bên liên quan và quan hệ giữa họ; mọi thị trường mà câu chuyện chạm tới và quy mô thật của từng thị trường; đối thủ ở từng thị trường và họ đang đi đường nào; luật chơi, chính sách, thuế đang tác động (nói rõ cái nào đang có hiệu lực, cái nào mới là kế hoạch); bối cảnh lớn của ngành ở thời điểm này. Ghi ngày của mọi số liệu, ưu tiên nguồn chính thức và nguồn bản địa. Chưa cần kết luận; cuối bài liệt kê những điều còn chưa rõ.

**Bước 2 — Nghiên cứu trực tiếp (Deep Research, cùng hội thoại)**
> Dựa trên bức tranh vừa vẽ, giờ đi thẳng vào câu hỏi: <câu hỏi trung tâm, viết trung tính>. Hãy đưa ra ít nhất ba cách giải thích cạnh tranh, trong đó có cách đơn giản nhất <ví dụ "đây chỉ là một hợp đồng mua bán thông thường">. Với mỗi cách, nêu dữ kiện ủng hộ, dữ kiện bác bỏ, và điều gì sẽ chứng minh nó sai (chú ý cả con số lẫn vật chứng thực tế: văn bản, quyết định, mốc ngày giờ, lời phát biểu hoặc sự kiện có thật có nguồn; cấm cảnh dựng lại hay nhân vật bịa). Chủ động tìm bằng chứng ngược và những gì báo chí chưa nói. Mỗi dữ kiện ghi nguồn và ngày; hai nguồn mâu thuẫn thì nêu cả hai.

**Kiểm (agent):** rút 10–15 dữ kiện và vật chứng then chốt nhất từ bước 1–2, mở nguồn gốc, ghi khớp, lệch hoặc không mở được. Viết `ban_tom_ke_thua.md` dài 1–2 trang: các khía cạnh chính, các cách giải thích, dữ kiện đã kiểm, danh sách "sai, không dùng", câu hỏi còn mở.

**Bước 3 — Khía cạnh, câu hỏi, góc tiềm năng (Deep Research, cùng hội thoại, dán bản tóm kế thừa)**
> Đây là bản tóm những gì đã kiểm chứng: <dán ban_tom_ke_thua.md>. Giờ hãy nghĩ như một người làm phim tài liệu kinh tế cho khán giả Việt Nam: chủ yếu nam 35–40 tuổi, hiểu biết, rất phản biện; họ không cần nghe lại điều báo chí đã viết. Đây là vài tiêu đề từng được kênh đón nhận tốt: <5–10 tiêu đề lấy từ `01_management/title_performance_log.md`>. Từ tất cả những gì đã tìm, đâu là những nghịch lý, câu hỏi và góc nhìn đáng kể nhất, những thứ có thể khiến họ dừng lại xem đến cuối? Sắp xếp từ hấp dẫn nhất, nói rõ góc nào chắc, góc nào còn là suy đoán. Cứ kể tự nhiên, được dùng ví von.

**Bước 4 — Dàn ý tham khảo (Deep Research, cùng hội thoại)**
> Từ những góc trên, dựng giúp tôi một dàn ý tham khảo cho video khoảng <15–20> phút: mở bằng một nghịch lý, đáp án lộ dần qua các bằng chứng, có một phần dựng lập luận phản biện mạnh nhất chống lại chính luận điểm của video, cao trào là bằng chứng quyết định, kết có lập trường kèm điều có thể khiến lập trường đó sai. Gợi ý thời lượng từng phần.
