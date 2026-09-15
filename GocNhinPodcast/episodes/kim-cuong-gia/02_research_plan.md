# Kế hoạch Nghiên cứu (02_research_plan.md) - Episode: kim-cuong-gia

## 1. Mục tiêu Nghiên cứu
Xây dựng nền tảng dữ liệu vững chắc cho kịch bản "Nghịch lý thanh khoản kim cương: Khi 'lá chắn' giấy tờ sụp đổ". Nghiên cứu tập trung vào 3 cốt lõi:
- Khủng hoảng kiểm định: Vụ án Đặng Ngọc Thảo (PNJ Lab) và lịch sử bê bối GIA 2005.
- Tác động tới PNJ: Cơ cấu sở hữu, phản ứng khủng hoảng, biến động cổ phiếu.
- Khủng hoảng thanh khoản: Hiện tượng "bank run" tại các tiệm vàng nhỏ (Kim Lý, Long Ngọc...) do gãy dòng tiền thâu mua.

## 2. Thiết kế hai bước (Double-Query Design)

### Bước 1: Structured Ingestion Prompt (Nạp nguồn qua Deep Research)
```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu và nguồn thông tin cho các chủ đề sau:

1. Vụ án khởi tố ông Đặng Ngọc Thảo (Cựu Giám đốc PNJ Lab / Công ty TNHH MTV Giám định PNJ) liên quan đến buôn lậu kim cương và mài mã số GIA:
- Chi tiết hành vi, phương thức mài xóa mã số laser gốc trên cạnh gờ viên đá lậu để khắc đè mã số mới nhằm hợp thức hóa nguồn gốc và cấp chứng nhận mới.
- Khối lượng kim cương lậu bị phát hiện (đường dây buôn lậu 28.000 viên kim cương của đối tượng người nước ngoài).

2. Tác động tới CTCP Vàng bạc Đá quý Phú Nhuận (PNJ):
- Mối quan hệ pháp lý, sở hữu giữa PNJ và PNJ Lab.
- Phản ứng khủng hoảng truyền thông của PNJ (thông cáo báo chí, cam kết với khách hàng mua kim cương retail).
- Biến động giá cổ phiếu PNJ (mã: PNJ) trên sàn chứng khoán khi tin tức nổ ra và tác động doanh thu/tâm lý khách hàng.
- Làn sóng người dân mang trang sức có giấy PNJ Lab đi kiểm định chéo tại các đơn vị khác (như SJC, GIA).

3. Hiện tượng mất thanh khoản tại các tiệm kim hoàn vừa và nhỏ Việt Nam (cuối 2024 - 2025):
- Thông tin về các cửa hàng ngừng thâu mua kim cương như tiệm vàng Kim Lý (Q.5, TP.HCM), Long Ngọc Luxury, Helia, PJA...
- Phân tích nguyên nhân đứt gãy dòng tiền mặt do làn sóng người dân ồ ạt bán lại rút vốn (Liquidity Run).

4. Bê bối hối lộ giám định của GIA năm 2005 (GIA grading scandal 2005) tại Mỹ:
- Chi tiết sự việc nhân viên giám định GIA nhận hối lộ để nâng phẩm cấp kim cương (color, clarity) cho các nhà buôn lớn tại New York.
- Hậu quả (CEO GIA từ chức) và cách thức GIA tái cấu trúc quy trình, công nghệ kiểm định để lấy lại niềm tin thị trường.

5. Xu hướng thị trường kim cương toàn cầu 2024-2026:
- Tác động của kim cương nhân tạo (Lab-grown Diamond - LGD) đối với giá trị và thuộc tính độc quyền của kim cương tự nhiên. Tỷ lệ giảm giá của kim cương tự nhiên.
```

### Bước 2: Danh sách Câu hỏi Trích xuất (Extraction Queries List)

*   **Query 1 (Vụ án Đặng Ngọc Thảo - PNJ Lab):**
    *   *Câu hỏi:* Hãy trích xuất chi tiết vụ án khởi tố cựu Giám đốc PNJ Lab Đặng Ngọc Thảo. Hành vi phạm tội cụ thể, thủ đoạn mài xóa mã số laser trên vành viên kim cương lậu để cấp mã số/chứng nhận mới là gì? Có bao nhiêu viên kim cương lậu bị phát hiện trong đường dây này?
    *   *Ràng buộc:* Ưu tiên dữ liệu mới nhất (2024-2026). Bắt buộc dẫn nguồn cụ thể (báo chí chính thống). Định dạng đầu ra: báo cáo chi tiết, phân tích rõ cơ chế lỗ hổng kiểm soát.
*   **Query 2 (Mối quan hệ PNJ & PNJ Lab):**
    *   *Câu hỏi:* Phân tích mối quan hệ sở hữu và pháp lý giữa CTCP Vàng bạc Đá quý Phú Nhuận (PNJ) và Công ty TNHH MTV Giám định PNJ (PNJ Lab). Doanh thu/lợi nhuận PNJ Lab đóng góp thế nào cho PNJ?
    *   *Ràng buộc:* Dựa trên các báo cáo tài chính công khai của PNJ. Trình bày dưới dạng bảng đối sánh hoặc gạch đầu dòng rõ ràng.
*   **Query 3 (Tác động tới PNJ & Phản ứng khủng hoảng):**
    *   *Câu hỏi:* Bê bối PNJ Lab ảnh hưởng thế nào đến giá cổ phiếu PNJ (mã: PNJ) trên sàn chứng khoán ngay sau khi tin tức nổ ra? Phản ứng truyền thông và thông điệp chính thức của PNJ nhằm xoa dịu khách hàng là gì? Có hiện tượng khách hàng mang đá đi kiểm định chéo không?
    *   *Ràng buộc:* Trích dẫn trực tiếp nội dung cam kết của PNJ và số liệu biến động cổ phiếu cụ thể.
*   **Query 4 (Lịch sử Bê bối GIA 2005):**
    *   *Câu hỏi:* Chi tiết cuộc khủng hoảng hối lộ nâng cấp chứng nhận của GIA năm 2005 tại Mỹ. Ai là người bị truy tố/từ chức? Hậu quả danh tiếng và cách GIA khắc phục quy trình kiểm định sau đó để khôi phục niềm tin toàn cầu là gì?
    *   *Ràng buộc:* Thông tin khách quan, chính xác từ các nguồn uy tín toàn cầu. Trích dẫn rõ ràng các mốc thời gian và biện pháp sửa đổi của GIA.
*   **Query 5 (Khủng hoảng thanh khoản các tiệm nhỏ):**
    *   *Câu hỏi:* Thu thập thông tin và phân tích hiện tượng các tiệm kim hoàn nhỏ (như Kim Lý, Long Ngọc Luxury, Helia...) tạm ngừng thâu mua kim cương từ cuối năm 2024 - 2025. Tại sao cơ chế cam kết thu đổi chịu lỗ ít (90-95%) lại dẫn đến đứt gãy dòng tiền mặt khi xảy ra panic run?
    *   *Ràng buộc:* Phân tích dưới lăng kính tài chính (Incentive & Cashflow Analysis).
*   **Query 6 (Sự càn quét của LGD toàn cầu):**
    *   *Câu hỏi:* Xu hướng giá kim cương tự nhiên toàn cầu giai đoạn 2024-2026 chịu tác động ra sao trước sự trỗi dậy của kim cương nhân tạo (Lab-grown Diamond)? Tỷ lệ sụt giảm giá trị của kim cương tự nhiên là bao nhiêu?
    *   *Ràng buộc:* Sử dụng dữ liệu thống kê từ các tổ chức nghiên cứu thị trường xa xỉ uy tín (Bain, Rapaport...).
*   **Query 7 (Quy trình tự bảo vệ của người tiêu dùng):**
    *   *Câu hỏi:* Trích xuất quy trình chuẩn và các bước cụ thể để người tiêu dùng tự tra cứu, hậu kiểm mã số GIA online và soi mã số cạnh trực tiếp tại cửa hàng.
    *   *Ràng buộc:* Hướng dẫn chi tiết, rõ ràng, dễ hiểu.
*   **Query 8 (Worst-case Scenario & Rủi ro pháp lý):**
    *   *Câu hỏi:* Đâu là kịch bản xấu nhất đối với thị trường kim cương Việt Nam nếu cuộc thanh tra nguồn gốc, hóa đơn chứng từ bị siết chặt diện rộng? Các thương hiệu nhỏ và hàng xách tay sẽ bị ảnh hưởng thế nào?
    *   *Ràng buộc:* Góc nhìn phản biện, an toàn pháp lý, mang tính dự báo vĩ mô khách quan.
