# NotebookLM Master Prompts — Dòng Chảy Content OS

Đây là bộ prompt tối ưu hóa cho NotebookLM để trích xuất dữ liệu "sạch", chuẩn format nhằm phục vụ cho hệ thống Dòng Chảy Content OS (cụ thể là mớm data cho AI Agent - Deep Researcher).

## Hướng dẫn sử dụng
1. Tạo một Notebook mới trong NotebookLM cho từng episode.
2. Nạp toàn bộ tài liệu nguồn (Báo cáo thường niên, File PDF tài chính, bài báo, nghiên cứu học thuật).
3. Copy và Paste lần lượt các Prompt bên dưới vào NotebookLM.
4. Copy toàn bộ câu trả lời của NotebookLM và lưu vào file: `episodes/[slug]/raw_research/notebook_lm_export.md`.
5. Gọi Agent Antigravity chạy lệnh `/hook_lab` để xử lý tiếp.

---

## Prompt 1: Data Point Extraction (Bóc tách dữ liệu vĩ mô & tài chính)
*Mục đích: Lấy toàn bộ các chỉ số tài chính, kinh tế, vĩ mô một cách chính xác.*

> **Prompt:**
> "Bạn là một nhà nghiên cứu tài chính vĩ mô. Hãy duyệt qua toàn bộ tài liệu được nạp và liệt kê MỌI con số, tỷ lệ phần trăm, số tiền, và dữ liệu định lượng quan trọng liên quan đến chủ đề chính của các tài liệu này. 
> 
> Yêu cầu định dạng BẮT BUỘC dưới dạng bảng Markdown với các cột sau:
> | Tên số liệu (Data Point) | Con số cụ thể | Thời điểm (Năm/Quý) | Context ngắn gọn | Nguồn trích dẫn (Tên file & Trang) |
> 
> Chú ý:
> - Tương đối tuyệt đối trung thành với tài liệu, KHÔNG tự suy diễn hay làm tròn số liệu sai lệch.
> - Nếu một số liệu có sự mâu thuẫn giữa các tài liệu, hãy ghi chú rõ sự mâu thuẫn đó."

---

## Prompt 2: Timeline & Case Studies (Chuỗi sự kiện)
*Mục đích: Lấy các mốc sự kiện quan trọng để xây dựng mạch logic cho video.*

> **Prompt:**
> "Dựa trên các tài liệu được cung cấp, hãy lập một Dòng thời gian (Timeline) chi tiết về các sự kiện có tính chất bước ngoặt, các quyết định chiến lược, hoặc các cuộc khủng hoảng.
> 
> Định dạng:
> - **[Năm/Tháng] - [Tên sự kiện]**
>   - Nguyên nhân (dựa trên tài liệu)
>   - Kết quả/Tác động kinh tế
>   - Trích dẫn gốc (Copy 1-2 câu quan trọng nhất từ tài liệu để chứng minh)
> 
> Nếu trong tài liệu có nhắc đến các Case Study (ví dụ so sánh với quốc gia khác, hoặc công ty khác trong quá khứ), hãy tạo thêm một phần **Case Studies** và tóm tắt ngắn gọn."

---

## Prompt 3: The Counter-Thesis (Góc nhìn phản biện & Rủi ro)
*Mục đích: Tìm kiếm lỗ hổng, rủi ro, và góc nhìn trái chiều để tạo chiều sâu và tránh việc tung hô một chiều (bias).*

> **Prompt:**
> "Kênh Dòng Chảy luôn cần cái nhìn đa chiều. Hãy đóng vai một chuyên gia phản biện. Tìm trong các tài liệu mọi điểm yếu, rủi ro tiềm ẩn, nợ xấu, thất bại, hoặc các nhận định tiêu cực/cảnh báo từ giới phân tích về chủ đề này.
> 
> Liệt kê dưới dạng Bullet points:
> - **[Tên Rủi ro / Điểm yếu]**
>   - Giải thích cơ chế rủi ro
>   - Trích dẫn nguyên văn bằng tiếng Việt/tiếng Anh từ tài liệu để chứng minh.
>   - Đánh giá mức độ nghiêm trọng (dựa trên ngữ cảnh tài liệu)."

---

## Prompt 4: FAQ & Logic Gaps (Dành cho việc kiểm tra chất lượng)
*Mục đích: Dùng để rà soát xem tài liệu đã đủ sâu chưa, có bị thiếu hụt mảng nào không.*

> **Prompt:**
> "Đóng vai một người xem khó tính, am hiểu kinh tế. Sau khi đọc các tài liệu này, theo bạn có những 'Lỗ hổng logic' (Logic gaps) nào chưa được giải thích thỏa đáng không? Có những câu hỏi lớn nào về dòng tiền, về tính bền vững của mô hình mà các tài liệu này ĐANG NÉ TRÁNH hoặc CHƯA TRẢ LỜI ĐƯỢC không? Hãy liệt kê ra."
