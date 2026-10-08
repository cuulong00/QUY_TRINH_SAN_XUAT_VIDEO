# final-merge

Áp dụng cho `episodes/**/final_voiceover.md`.

## Preconditions
- Chỉ merge sau khi đã có các state files cần thiết và có chapter files.

## Must do
- Loại bỏ ý trùng, case study trùng, số liệu trùng.
- Loại bỏ việc restate thesis ở nhiều đoạn nếu đoạn mới không mở thêm layer phân tích.
- Chỉ giữ một echo khi nó tạo payoff, contradiction mới, hoặc giúp chuyển movement; không giữ echo chỉ để nhấn mạnh cùng một ý.
- Khi hai đoạn nói gần cùng một điều, giữ đoạn có interpretive sharpness, oral rhythm, và payoff tốt hơn.
- Không lặp case study hoặc số liệu nếu lần lặp không mang góc đọc mới.
- Transition phải mở movement tiếp theo, không recap movement cũ bằng câu chữ khác.
- Giữ logic arc rõ ràng từ hook đến payoff.
- Giữ thesis fidelity: bản merge cuối không được regress về một spine quen thuộc hơn nhưng nông hơn.
- Giữ các interpretive turns đắt của từng chapter, không được làm phẳng thành prose sạch nhưng generic.
- Đảm bảo disclaimer xuất hiện rõ ràng: "Đây là nội dung giáo dục, không phải lời khuyên đầu tư".
- Giữ giọng voiceover-first: sắc, logic, dễ nghe, nhưng vẫn có người thật ở trong đó.
- Sau merge phải cập nhật `01_management/episode_registry.csv`.
- Sau merge phải dừng chờ user duyệt trước khi qua QA.

## Must not do
- Không tạo final voiceover trực tiếp từ raw topic.
- Không dùng merge như đường tắt để bỏ qua chapter workflow.
- Không dùng merge để đổi một video có lập luận riêng thành một script nghe giống mọi video tài chính khác.
- Không giữ các câu AI-isms, announce-importance, hoặc self-promotion chỉ để tạo retention giả.