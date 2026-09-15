# Query & Extraction Blueprint: Sự Thật Về "Think and Grow Rich"

*   **Episode**: `su-that-think-and-grow-rich`
*   **Master Notebook URL**: `https://notebooklm.google.com/notebook/f404f058-2167-49a2-8368-e1046238eaf2`

Bản thiết kế này phân định rõ ràng các truy vấn Deep Research sẽ chạy hàng loạt (để nạp nguồn) và các câu hỏi trích xuất hàng loạt (để lưu vào research vault).

---

## 1. Kế Hoạch Chạy Deep Research Hàng Loạt (Bulk Deep Research Queries)

> **Mục tiêu**: Nạp đầy đủ nguồn tài liệu đa dạng vào NotebookLM bằng cách chạy tối thiểu 6-9 truy vấn Deep Research liên tiếp. Tuyệt đối không gọi xen kẽ ask request giữa các lần chạy này.

| STT | Loại Truy Vấn | Ngôn Ngữ | Nội Dung Truy Vấn (Query) |
|---|---|---|---|
| 1 | Lịch sử (Thesis) | Tiếng Anh | "Andrew Carnegie biography David Nasaw Napoleon Hill meeting debunked fraud history" |
| 2 | Khoa học (Thesis) | Tiếng Anh | "Napoleon Hill brain as broadcasting station pseudoscience electromagnetism physics analysis" |
| 3 | Tâm lý học (Thesis) | Tiếng Anh | "Law of Attraction pseudoscience psychology magical thinking cognitive reframing" |
| 4 | Đổ lỗi nạn nhân (Context) | Tiếng Anh | "Think and Grow Rich victim blaming self help ideology socioeconomic factors" |
| 5 | Tiểu sử (Thesis) | Tiếng Anh | "Napoleon Hill biography frauds scams bankruptcies Matt Novak Gizmodo analysis" |
| 6 | Nghiên cứu Phản biện (Counter-Thesis) | Tiếng Anh | "Scientific benefits of visualization in goal setting mental contrasting Gabriele Oettingen WOOP" |
| 7 | Tái lập & Nhận thức (Context) | Tiếng Anh | "How positive fantasizing drains energy motivation psychology studies Gabriele Oettingen" |

---

## 2. Kế Hoạch Trích Xuất Dữ Liệu Hàng Loạt (Bulk Extraction / Ask Queries)

> **Mục tiêu**: Sau khi nạp đủ toàn bộ nguồn, sử dụng công cụ `batch_to_vault` để trích xuất dữ liệu đồng loạt vào `research_vault/`.

Các câu hỏi trích xuất được thiết kế kèm cấu trúc và freshness yêu cầu:

### Câu hỏi 1 (Historical Fraud)
*   **Tên file xuất**: `001_historical_fraud.md`
*   **Nội dung câu hỏi**: "Phân tích chi tiết bằng chứng lịch sử chứng minh Napoleon Hill thêu dệt mối quan hệ với Andrew Carnegie và các vĩ nhân khác (Edison, Henry Ford). Những phát hiện của các nhà sử học (như David Nasaw) là gì? Liệt kê các mốc thời gian và điểm mâu thuẫn lớn nhất trong câu chuyện của Hill."
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*

### Câu hỏi 2 (Brain Pseudoscience)
*   **Tên file xuất**: `002_brain_pseudoscience.md`
*   **Nội dung câu hỏi**: "Phân tích chi tiết lý thuyết 'não bộ là trạm phát sóng' của Napoleon Hill dưới góc nhìn vật lý học và sinh học thần kinh hiện đại. Sóng não thực tế (Alpha, Beta, Gamma) hoạt động như thế nào, cường độ ra sao, và tại sao nó không thể truyền đi xa để 'thu hút' vật chất hay cơ hội?"
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*

### Câu hỏi 3 (Law of Attraction & Dopamine Trap)
*   **Tên file xuất**: `003_dopamine_trap.md`
*   **Nội dung câu hỏi**: "Bản chất của Luật hấp dẫn trong cuốn sách và cơ chế tâm lý 'bán hy vọng'. Tại sao việc mơ mộng (positive fantasizing) tạo ra dopamine ảo và làm giảm động lực hành động thực tế? Trích dẫn các nghiên cứu của Gabriele Oettingen về sự cản trở của việc mơ tưởng tích cực một chiều đối với sự thành công thực chất."
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*

### Câu hỏi 4 (Victim Blaming & Attribution Bias)
*   **Tên file xuất**: `004_victim_blaming.md`
*   **Nội dung câu hỏi**: "Cơ chế 'đổ lỗi cho nạn nhân' (victim blaming) và thiên kiến quy kết (attribution bias) trong công thức của Napoleon Hill. Cách nó gieo rắc sự tự trách và ảnh hưởng xấu đến tâm thần của người đọc khi áp dụng thất bại. Sự thiếu sót của công thức này đối với các yếu tố vĩ mô và nguồn lực cá nhân thực tế là gì?"
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*

### Câu hỏi 5 (Napoleon Hill Personal Life Scams)
*   **Tên file xuất**: `005_personal_life_scams.md`
*   **Nội dung câu hỏi**: "Tóm tắt chi tiết tiểu sử tài chính, các vụ phá sản, và các cáo buộc/vụ kiện tụng lừa đảo của Napoleon Hill (trước năm 1937 và sau đó). Cuộc sống thực tế của ông mâu thuẫn như thế nào với những gì ông rao giảng trong sách? Ông thực sự kiếm được tài sản nhờ kinh doanh hay nhờ bán sách dạy làm giàu?"
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*

### Câu hỏi 6 (Mental Contrasting & Actionable Solutions - Counter-Thesis/Application)
*   **Tên file xuất**: `006_actionable_solutions.md`
*   **Nội dung câu hỏi**: "Lợi ích thực sự của việc hình dung (visualization) khi kết hợp với đối lập tinh thần (mental contrasting) là gì? Giải thích cơ chế của phương pháp WOOP (Wish, Outcome, Obstacle, Plan) của Gabriele Oettingen. Làm thế nào để chuyển đổi từ tư duy Luật hấp dẫn siêu hình sang tư duy hành động thực tế nhằm đạt kết quả?"
*   **Prompt ép chất lượng**: *"Ưu tiên dữ liệu và nghiên cứu mới nhất. Mọi thí nghiệm và số liệu phải ghi rõ tên nhà nghiên cứu, năm công bố, phương pháp thực hiện (mẫu thử bao nhiêu người, đo lường thế nào). Trình bày dưới dạng báo cáo chuyên nghiệp. Chỉ giữ phần lõi nội dung."*
