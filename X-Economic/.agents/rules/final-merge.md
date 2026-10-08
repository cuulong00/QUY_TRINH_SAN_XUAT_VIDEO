# final-merge

Áp dụng cho `episodes/**/voiceover.md` (Pha 8).

Lưu ý: `voiceover.md` chỉ phục vụ kiểm định toàn bài và thu âm tổng thể. Pha 12 (I2V+) thực hiện độc lập theo từng chương và đọc trực tiếp các file `chapter_XX.md` theo Hợp đồng `.agents/contracts/i2v_nhip_y.md`, tuyệt đối không đọc `voiceover.md`.

## Preconditions
- Chỉ merge sau khi đã có các state files cần thiết và có chapter files.

## Must do
- Loại bỏ ý trùng, case study trùng, số liệu trùng.
- Khi cần rút ngắn, chỉ cắt phần lặp ý. Không cắt phần giải thích giúp người nghe hiểu ngay khi nghe một lần (giải nghĩa thuật ngữ, kết luận nói thẳng, chủ ngữ hoặc tân ngữ được gọi tên lại); bản merge dài hơn ngân sách vì phần này là hợp lệ, báo user thời lượng mới (`.agents/workflows/build_outline.md` Trạm 5, ngoại lệ "người nghe hiểu").
- Loại bỏ việc restate thesis ở nhiều đoạn nếu đoạn mới không mở thêm layer phân tích.
- Chỉ giữ một echo khi nó tạo payoff, contradiction mới, hoặc giúp chuyển movement; không giữ echo chỉ để nhấn mạnh cùng một ý.
- Khi hai đoạn nói gần cùng một điều, giữ đoạn có interpretive sharpness, oral rhythm, và payoff tốt hơn.
- Không lặp case study hoặc số liệu nếu lần lặp không mang góc đọc mới.
- Transition phải mở movement tiếp theo, không recap movement cũ bằng câu chữ khác.
- Giữ logic arc rõ ràng từ hook đến payoff.
- Giữ thesis fidelity: bản merge cuối không được regress về một spine quen thuộc hơn nhưng nông hơn.
- Giữ các interpretive turns đắt của từng chapter, không được làm phẳng thành prose sạch nhưng generic.
- Đảm bảo dòng lưu ý nội dung bắt buộc xuất hiện đúng nguyên văn trong `CLAUDE.md` ("Nội dung chia sẻ luận điểm khách quan, mang tính thảo luận và xây dựng"); ranh giới tư vấn đầu tư theo `00_core/financial_boundaries.md`.
- Giữ đúng chế độ kết đã chọn (`00_core/stance_and_judgment.md` §1): chế độ A giữ lập trường chính, chế độ B giữ đủ khung kết mở; khi gộp không làm mềm thành câu lửng lơ và không cộng dồn các cụm "chúng tôi cho rằng" từ nhiều chương.
- Bắt buộc chấm lại cấp bài sau merge bằng Phiếu A của `00_core/narrative_craft_rubric.md` do người khác ngoài người merge (Auditor / Claude / agent khác) chấm: rà soát toàn bộ tác phẩm sau gộp (câu hỏi kịch tính trung tâm I, cao trào IV-b, gieo/gặt hạt, và tính liền mạch của các cú lật); người merge có thể tự soi lại mạch chuyện; ghi nhận kết quả vào `11_narrative_craft_scorecard.md`.
- Giữ giọng voiceover-first: sắc, logic, dễ nghe, nhưng vẫn có người thật ở trong đó.
- Sau merge phải cập nhật `01_management/episode_registry.csv` và `00_pipeline_operator_log.md`.
- Sau merge phải dừng chờ user duyệt trước khi qua QA.

## Must not do
- Không tạo final voiceover trực tiếp từ raw topic.
- Không dùng merge như đường tắt để bỏ qua chapter workflow.
- Không dùng merge để đổi một video có lập luận riêng thành một script nghe giống mọi video tài chính khác.
- Không giữ các câu AI-isms, announce-importance, hoặc self-promotion chỉ để tạo retention giả.