# Giải Phẫu Các Thảm Họa Đại Dự Án Do Nhà Nước Dẫn Dắt

> **Extraction Query ID:** 01_state_led_failures.md
> **Master Notebook ID:** `c586d12e-218f-4032-8944-80fe253afd1c`

---

Để chuẩn bị một bài phân tích chuyên sâu, toàn diện và có độ chính xác định lượng cao nhất cho bạn, tôi đã tiến hành khảo sát toàn bộ hệ thống tài liệu trong dự án. 

Hiện tại, nguồn tư liệu sẵn có trong notebook của bạn **đáp ứng cực kỳ chi tiết** cho 4 trường hợp đầu tiên và dự án máy tính thế hệ thứ 5 (FGCS) của Nhật Bản, cụ thể:
1. **British Leyland (Anh Quốc):** Có đầy đủ dữ liệu về Đạo luật quốc hữu hóa 1975 [1], **Ryder Report** và gói cứu trợ phình to từ ngân sách lên tới **hơn £2.8 tỷ** (hơn **£11 tỷ** theo giá trị điều chỉnh lạm phát ngày nay) [2, 3]. Dữ liệu định lượng về năng suất lao động (BLMC chỉ đạt **4.5 xe/người/năm** so với **12 xe** của Volkswagen) [4], lượng tài sản cố định cực thấp (**£2,000/nhân viên** so với **£6,000** của Fiat/VW) [4]. Các cuộc đình công liên tục dưới sự lãnh đạo của Derek Robinson ("Red Robbo") (**523 cuộc bãi công** tại Longbridge riêng năm 1978) [5]. Chi tiết về các thiết kế lỗi thời/lỗi kỹ thuật của Austin Allegro (vô lăng vuông, rò rỉ nước, rụng kính sau) [6] và Morris Marina [7].
2. **Concorde (Anh - Pháp):** Chi tiết hiệp ước song phương năm 1962 [8]; chi phí phát triển thực tế tăng vọt từ ước tính ban đầu £70-90 triệu lên **hơn \$2.8 tỷ** (£1.2 tỷ năm 1975, tương đương **£11 tỷ** ngày nay) [9, 10]. Cơ chế pháp lý của hiệp ước không có điều khoản rút lui đơn phương đã trực tiếp tạo ra **"Concorde Fallacy" (Bẫy chi phí chìm)** do áp lực chính trị và thể diện quốc gia [11-13]. Các hãng hàng không quốc gia được trợ cấp để mua Concorde với đơn giá **£23 triệu** mỗi chiếc vào năm 1977 [14, 15].
3. **Plan Calcul & Máy tính Bull (Pháp):** Khởi nguồn từ việc Mỹ cấm vận siêu máy tính CDC/IBM năm 1966 đối với Ủy ban Năng lượng Nguyên tử Pháp (CEA) [16, 17] và sự kiện General Electric thâu tóm Machines Bull năm 1964 [16, 17]. Cơ chế mua sắm công bắt buộc cho các cơ quan hành chính (**"hệ thống kho vũ khí" - arsenal pattern**) [18] nhưng cap thị phần nội địa ở mức **11%** (năm 1970) [19]. Sự can thiệp chính trị thô bạo của tổng thống Giscard d'Estaing năm 1975 khi đơn phương khai tử liên minh châu Âu Unidata [20, 21] để sáp nhập CII với Honeywell-Bull [20, 22].
4. **Trabant & Wartburg (Đông Đức):** Quá trình chuyển đổi sang vỏ xe **Duroplast** do thiếu hụt thép và cấm vận COCOM [23, 24]. Thời gian chờ mua xe kéo dài **10-13 năm** [25]. Quyết định phủ quyết của Bộ Chính trị (Günter Mittag) hủy bỏ dự án hatchback hiện đại **P603** năm 1969 dù đã đầu tư **35 triệu Marks** [26, 27]. Sự sụp đổ của dự án xe chung Comecon (**RGW-Auto**) năm 1979 do thiếu hụt ngân sách quốc phòng [28] và sự kém hiệu quả của nỗ lực muộn màng mua bản quyền động cơ VW Polo lắp vào bộ khung vỏ cũ kỹ những năm 1960 [29, 30].
5. **Dự án máy tính thế hệ 5 (FGCS) của Nhật Bản (MITI):** Khởi xướng năm 1982 với mục tiêu AI xử lý logic [31], tạo ra làn sóng lo ngại lớn ở Mỹ và châu Âu (kích hoạt dự án Strategic Computing của DARPA và Alvey của Anh) [32-34]. Tuy nhiên, FGCS gặp nhiều trở ngại lớn về kiến trúc phần mềm và không đạt được thành công thương mại mang tính đột phá [35].

⚠️ **Khoảng trống thông tin trong nguồn của bạn:** 
Tài liệu hiện tại **KHÔNG chứa thông tin lịch sử hay phân tích kinh tế về dự án xe hơi Proton của Malaysia** (chỉ có từ khóa "Proton Saga" xuất hiện dưới dạng gợi ý tìm kiếm ngẫu nhiên trên một trang web về xe Trabant [36]).

---

### 📋 Đề xuất Kế hoạch Hành động:

Tôi muốn đề xuất một quy trình xây dựng bài phân tích hoàn chỉnh dưới dạng một **Báo cáo chuyên sâu (Tailored Report)** hiển thị trực tiếp trong bảng **Studio** (bên phải màn hình của bạn) để bạn có thể lưu trữ, theo dõi và sử dụng lâu dài:

*   **Bước 1: Nghiên cứu Web về Proton (Malaysia):** Tôi sẽ tiến hành tra cứu trên internet để bổ sung dữ liệu lịch sử về Proton (bắt đầu từ năm 1983 dưới thời Thủ tướng Mahathir Mohamad, việc bảo hộ thuế quan đối với xe nhập khẩu lên tới hơn 100%, sự hợp tác với Mitsubishi, bẫy thị trường nội địa nhỏ hẹp khiến Proton không thể đạt quy mô kinh tế tối thiểu, và thương vụ bán lại cổ phần cho Geely).
*   **Bước 2: Trình bày và Nhập nguồn:** Tôi sẽ tóm tắt kết quả nghiên cứu Proton cho bạn duyệt, sau đó nhập các tài liệu này vào danh sách nguồn của dự án để đảm bảo mọi trích dẫn trong báo cáo đều được đối chiếu chính xác.
*   **Bước 3: Biên soạn Báo cáo trong Studio:** Tôi sẽ tổng hợp toàn bộ 5 trường hợp điển hình trên thành một báo cáo song ngữ hoặc tiếng Việt học thuật, phân tích sâu các cơ chế kinh tế thể chế:
    *   **Ràng buộc ngân sách mềm (Soft Budget Constraint)** của János Kornai [37].
    *   **Lý thuyết "Tiền của người khác" (Other People's Money - OPM)** và vấn đề rủi ro đạo đức (Moral Hazard) [3, 38].
    *   **Mô hình "Hệ thống kho vũ khí" (Arsenal System)** so với kỷ luật thị trường (Market Discipline) [18, 39].

Bạn có đồng ý để tôi **bắt đầu thực hiện Bước 1 (Nghiên cứu Web về Proton)** ngay bây giờ không, hay bạn muốn tôi bỏ qua case study Proton để tập trung phân tích 4 trường hợp còn lại và FGCS ngay lập tức?
