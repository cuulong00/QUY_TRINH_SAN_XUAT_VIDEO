Quy trình xây dựng video của kênh Dòng Chảy

Mình viết tài liệu này để giải thích cách kênh Dòng Chảy sản xuất nội dung. Mình đóng vai trò tổng biên tập — là người ra quyết định ở mọi khâu, từ chọn chủ đề, duyệt kịch bản, đến duyệt hình ảnh trước khi xuất bản. Hỗ trợ mình là một đội ngũ trợ lý chuyên môn, mỗi người phụ trách một mảng riêng.

Không có video nào trên kênh được lấy lại hay sử dụng lại nội dung từ bất kỳ nguồn nào. Mọi thứ đều được xây dựng từ đầu.

---

Đội ngũ trợ lý

- Trợ lý chiến lược nội dung: hỗ trợ đánh giá chủ đề, đề xuất góc nhìn
- Trợ lý nghiên cứu tài chính: hỗ trợ phân tích vĩ mô, chính sách kinh tế
- Trợ lý phân tích thị trường: hỗ trợ đi sâu vào tài chính doanh nghiệp khi cần
- Trợ lý kịch bản: hỗ trợ xây dàn ý, cấu trúc nội dung tổng thể
- Trợ lý viết nội dung: hỗ trợ viết nội dung chi tiết theo chỉ đạo
- Trợ lý kiểm soát chất lượng: hỗ trợ rà soát kịch bản, tìm lỗi logic
- Trợ lý kiểm toán số liệu: hỗ trợ kiểm tra lại con số và nguồn dữ liệu
- Trợ lý giọng đọc: hỗ trợ chỉnh câu cú cho tự nhiên khi thu âm
- Trợ lý hình ảnh: hỗ trợ chia cảnh và tạo hình minh hoạ

Tất cả đều là trợ lý. Mình là người duyệt, quyết định và chịu trách nhiệm cuối cùng.

---

Các bước thực hiện

Bước 1 — Nghiên cứu và thu thập tài liệu

Mình dùng Gemini Deep Research để nghiên cứu chủ đề theo cách thủ công — mình tự đặt câu hỏi, tự đọc kết quả, tự chọn lọc thông tin đáng tin. Bên cạnh đó mình cũng đọc thêm báo cáo từ Tổng cục Thống kê, IMF, World Bank, các bài phân tích từ công ty chứng khoán, báo chí tài chính. Toàn bộ tài liệu được lưu lại theo từng chủ đề.

Bước 2 — Chọn góc nhìn và ra bản định hướng

Mình giao tài liệu cho trợ lý chiến lược nội dung, yêu cầu đề xuất 2-3 góc tiếp cận. Mình đọc hết rồi chọn góc nào sắc nhất. Sau đó chỉ đạo trợ lý kịch bản viết bản định hướng: luận điểm chính, khán giả mục tiêu, những câu hỏi video sẽ trả lời, và vùng cấm nội dung.

Mình duyệt bản định hướng. Chưa duyệt thì không ai được làm tiếp.

Bước 3 — Nghiên cứu bổ sung và viết câu mở đầu

Mình giao trợ lý nghiên cứu tổng hợp thêm dữ liệu. Đồng thời giao trợ lý viết vài phương án câu mở đầu cho video. Mình đọc, chọn phương án mạnh nhất, bổ sung dữ liệu nếu thấy cần.

Bước 4 — Xây dàn ý

Mình chỉ đạo trợ lý kịch bản xây dàn ý chi tiết: bao nhiêu phần, mỗi phần nói gì, dữ liệu dùng ở đâu. Mình duyệt dàn ý, sửa nếu cần — thêm bớt hay đổi thứ tự phần nào thì quyết ở bước này.

Bước 5 — Viết kịch bản

Mình giao trợ lý viết nội dung chi tiết từng phần theo dàn ý đã duyệt. Viết xong phần nào mình đọc phần đó, đối chiếu số liệu với tài liệu gốc. Phần nào chưa đạt thì cho viết lại.

Bước 6 — Kiểm tra chất lượng

Mình giao trợ lý kiểm toán rà soát lại toàn bộ số liệu. Sau đó giao trợ lý giọng đọc chỉnh câu cú cho tự nhiên khi thu âm. Mình đọc lại toàn bộ kịch bản lần cuối rồi mới cho qua.

Bước 7 — Thiết kế hình ảnh và hậu kỳ

Sau khi kịch bản được duyệt, mình chỉ đạo trợ lý hình ảnh viết lại kịch bản thoại (Oral Polish) thành các câu đơn ngắn gọn dưới 26 từ ra tệp `chapter_XX_visual.md`. Trợ lý hình ảnh tiến hành lập sơ đồ phân cảnh và thiết kế tệp prompts master (`prompts_master.txt`) theo luồng I2V/T2V: vẽ ảnh tĩnh bằng NanoBanana 2 và tạo chuyển động video bằng Veo 3.1 Lite. Tiếp theo là thu âm giọng đọc và dựng phim (ghép hình và âm thanh). Mình kiểm tra video lần cuối trước khi xuất bản.

---

Cam kết về tính nguyên bản

Toàn bộ nội dung trên kênh Dòng Chảy được xây dựng từ đầu theo quy trình trên:

- Kịch bản do đội ngũ viết theo chỉ đạo của mình, không copy từ bất kỳ nguồn nào
- Số liệu thu thập từ nguồn chính thống, có ghi rõ nguồn gốc
- Hình ảnh minh hoạ được tạo mới cho từng video, không lấy lại ảnh có sẵn
- Giọng đọc thu âm riêng cho từng video
- Mỗi video có góc phân tích riêng, không trùng với nội dung có sẵn trên mạng

Mình sẵn sàng cung cấp toàn bộ tài liệu nghiên cứu gốc, kịch bản nháp và file chỉnh sửa để chứng minh nội dung do kênh tự sản xuất.
