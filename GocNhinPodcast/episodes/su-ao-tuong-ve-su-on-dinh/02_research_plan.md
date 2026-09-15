# Kế hoạch Nghiên cứu (Deep Research Plan)

Tài liệu này xác định các truy vấn sẽ được sử dụng để nạp tài liệu vào NotebookLM (Ingestion) và bộ câu hỏi trích xuất (Extraction) dữ liệu cho kho lưu trữ Vault, dựa trên góc tiếp cận "Self-Organized Criticality".

## User Review Required
> [!IMPORTANT]
> Đây là thiết kế truy vấn (Double-Query Design) nhằm điều khiển AI chạy nghiên cứu tự động. Việc thiết kế chuẩn xác ở bước này sẽ tiết kiệm chi phí API và mang lại dữ liệu sắc bén nhất.
> Hãy xem xét **Prompt nạp nguồn** và **Danh sách câu hỏi trích xuất**. Nếu bạn thấy hướng tìm kiếm dữ liệu đã bao phủ đủ các góc cạnh (Cháy rừng, FED/QE, Doanh nghiệp Zombie, Evergrande, và Giải pháp cá nhân), hãy phản hồi "Duyệt". Tôi sẽ kích hoạt hệ thống NotebookLM để tiến hành nạp nguồn và trích xuất.

## 1. Mục tiêu Nghiên cứu
Khai thác dữ liệu thực chứng để chứng minh luận điểm: *Việc loại bỏ các rủi ro nhỏ (suy thoái ngắn hạn, công ty phá sản) bằng sự can thiệp nhân tạo (bơm tiền, hạ lãi suất) không làm hệ thống an toàn hơn, mà thực chất đang tích tụ rủi ro cho một cú sụp đổ khổng lồ mang tính hệ thống.*

## 2. Prompt Nạp Nguồn Cấu Trúc (Structured Ingestion Prompt - Bước 1)
*Prompt này sẽ được đưa vào công cụ Deep Research của NotebookLM để thu thập một lượng lớn tài liệu bối cảnh.*

```text
Hãy thực hiện nghiên cứu sâu (Deep Research) trên web để thu thập đầy đủ tài liệu, báo cáo, và phân tích cho các chủ đề sau liên quan đến nguyên lý 'Self-Organized Criticality' và rủi ro kinh tế vĩ mô:

1. Sự kiện cháy rừng Yellowstone năm 1988:
- Nguyên nhân sâu xa từ chính sách dập lửa triệt để của Cục Lâm nghiệp Mỹ từ năm 1935.
- Hậu quả, mức độ thiệt hại (số liệu cụ thể) và bài học rút ra về sự tích tụ rủi ro hệ thống sinh thái.

2. Tính tới hạn tự tổ chức (Self-Organized Criticality) & Nghịch lý St. Petersburg:
- Lời giải thích dễ hiểu về mô hình đống cát (Sandpile Simulator) của nhà vật lý Per Bak.
- Khái niệm 'Quy luật Lũy thừa' (Power Law) khác biệt thế nào với 'Phân phối chuẩn' (Normal Distribution) trong việc dự báo các sự kiện cực đoan (Thiên nga đen).

3. Chính sách nới lỏng định lượng (QE), cứu trợ (Bailout) và Doanh nghiệp Zombie:
- Phân tích của các chuyên gia hoặc tổ chức tài chính uy tín (IMF, BIS) về việc FED hoặc các Ngân hàng Trung Ương liên tục hạ lãi suất/cứu trợ (ví dụ năm 2008, 2020) đã ngăn chặn suy thoái ngắn hạn nhưng làm tăng tỷ lệ nợ xấu và tạo ra các 'Doanh nghiệp Zombie' ra sao (tìm số liệu cập nhật 2023-2025).

4. Sự sụp đổ của Evergrande (Case study điểm mù):
- Quá trình phình to của Evergrande dưới các chính sách hỗ trợ tín dụng và 'Ảo tưởng ổn định' của thị trường bất động sản Trung Quốc.
- Diễn biến sụp đổ đột ngột (2021-2024) và cách nó minh họa cho nguyên lý 'tia sét đánh vào đống cành khô' khi chính sách quay xe (Lằn ranh đỏ).
```

## 3. Danh sách Câu hỏi Trích xuất (Optimized Extraction Queries - Bước 2)
*Các câu hỏi này sẽ được quét qua kho dữ liệu đã nạp bằng công cụ Batch to Vault để tạo ra các mảnh dữ liệu (Data points) cho kịch bản.*

1. **[Lịch sử/Sinh thái]:** Trích xuất chi tiết số liệu về vụ cháy rừng Yellowstone 1988 (diện tích cháy, thiệt hại, so sánh với các năm trước) và chỉ ra mối liên hệ nhân quả trực tiếp với chính sách "dập tắt lửa trước 10h sáng" của Cục Lâm nghiệp.
2. **[Khoa học]:** Trích xuất định nghĩa và ví dụ dễ hiểu nhất về "Self-Organized Criticality" (Tính tới hạn tự tổ chức) và "Power Law" (Quy luật lũy thừa). So sánh sự khác biệt cốt lõi của chúng với "Normal Distribution".
3. **[Vĩ mô/Số liệu]:** Tìm và trích xuất các số liệu thống kê (phải có nguồn và năm) về tỷ lệ hoặc số lượng "Doanh nghiệp Zombie" tại Mỹ hoặc toàn cầu trước và sau giai đoạn áp dụng các chính sách nới lỏng tiền tệ (QE/Lãi suất thấp) từ 2010 - 2024.
4. **[Cơ chế]:** Mô tả chi tiết cơ chế vĩ mô: Việc dòng tiền rẻ và dễ dãi ngăn chặn các "cuộc suy thoái nhỏ" (natural corrections) đã làm méo mó việc phân bổ vốn và nuôi dưỡng "cành khô" trong hệ thống kinh tế như thế nào?
5. **[Phản biện]:** Tại sao các Ngân hàng Trung ương (như FED) lại BẮT BUỘC phải thực hiện bailout hoặc nới lỏng tiền tệ trong các cuộc khủng hoảng dù biết sẽ để lại di chứng (Tình thế Catch-22)? Trích xuất lập luận bảo vệ chính sách này.
6. **[Case Study]:** Phân tích sự sụp đổ của Evergrande (Trung Quốc) qua lăng kính "Tích tụ cành khô". Điều gì là nguyên nhân sâu xa (ảo tưởng an toàn, bơm tín dụng quá mức) và điều gì là "tia sét" kích hoạt (3 lằn ranh đỏ)?
7. **[Ứng dụng vi mô]:** Đúc kết bài học hành vi cho cá nhân/nhà đầu tư nhỏ lẻ. Dựa trên các nguyên lý về rủi ro này (hoặc tư duy Barbell của Nassim Taleb), các chuyên gia khuyên người dân nên có chiến lược gì để tồn tại thay vì bám víu vào sự "ổn định tuyệt đối"?

---
## Kế hoạch Thực thi (Sau khi duyệt)
1. Lưu tài liệu này thành `episodes/su-ao-tuong-ve-su-on-dinh/02_research_plan.md`.
2. Khởi tạo một Notebook mới qua tool `create_notebook`.
3. Bơm nguồn dữ liệu qua `deep_research` với prompt cấu trúc.
4. Trích xuất tự động qua `batch_to_vault` dựa trên 7 câu hỏi trên.
5. Tổng hợp thành `02_research_map.md` và `02_research_synthesis.md` để hoàn tất Pha 2.
