# Editorial & Legal QA Report — Ngân Hàng Lấy Tiền Đâu Cho 18 Siêu Dự Án?
Ngày QA: 2026-06-25

**Tổng claim kiểm tra:** 15 (từ Claim 001 đến Claim 015 trong `10_claim_ledger.md`)
**An toàn:** 15
**Cần điều chỉnh:** 0
**Rủi ro cao:** 0

## Chi tiết đánh giá theo tiêu chí:

### 1. Kiểm chứng nguồn dữ liệu và văn bản luật (Freshness & Accuracy Gate)
- **Công văn 5386/NHNN-TD (ban hành ngày 22/06/2026):** Trích dẫn đúng tên văn bản hành chính của NHNN về cơ chế loại trừ room tín dụng đối với 18 dự án hạ tầng vĩ mô.
- **Nhu cầu vốn 752.138 tỷ đồng:** Khớp chính xác với báo cáo nhu cầu vốn giai đoạn 2026-2028.
- **Tỷ lệ LDR (115% - 2026, 109% - 2025, 106% - 2024):** Được so sánh cụ thể theo dòng thời gian lịch sử, dựa trên báo cáo phân tích của VDSC.
- **Thông tư 25/2026/TT-NHNN và Thông tư 08/2026/TT-NHNN:** Trích dẫn đúng số hiệu văn bản pháp lý còn hiệu lực.
- **Lãi suất liên ngân hàng ngắn hạn (> 7%):** Neo đúng mốc thời điểm cuối tháng 6/2026.
- **Quy mô phát hành trái phiếu ngân hàng (61.000 tỷ 5 tháng, 33.000 tỷ tháng 5/2026):** Neo số liệu thống kê thị trường trái phiếu thực tế.
- **Lãi suất Fed neo giữ (3,5% - 3,75%):** Chính xác.

### 2. Kiểm tra tính khách quan và xây dựng (Constructiveness & Tone Audit)
- Giọng văn duy trì **Cold Analysis** (phân tích lạnh lùng, kỹ trị), không có bất kỳ câu chữ nào công kích cá nhân, tổ chức hay nhà điều hành.
- Loại bỏ hoàn toàn các từ ngữ giật gân, nhạy cảm chính trị, hoặc phán xét đạo đức một chiều. Các cụm từ được sử dụng đều là thuật ngữ kinh tế học chuẩn mực ("hiệu ứng lấn át tín dụng", "lệch pha kỳ hạn", "chi phí vốn bình quân", "hợp vốn tín dụng").

### 3. Kiểm tra tính đa chiều (Steelman Standard)
- Kịch bản trình bày rõ ràng mục đích của chính sách nới lỏng an toàn (Thông tư 25, Thông tư 08, đặc cách room): Nhằm ưu tiên tháo gỡ rào cản dòng vốn cho hạ tầng chiến lược quốc gia (APEC, sân bay Gia Bình, đường sắt tốc độ cao), đây là động lực cốt lõi cho tăng trưởng kinh tế dài hạn. Tuy nhiên, kịch bản cũng chỉ ra mặt đối lập một cách khoa học: Hệ quả là rủi ro mất cân đối kỳ hạn bảng cân đối của ngân hàng và hiệu ứng lấn át dòng vốn SMEs. Sự đánh đổi này được trình bày dưới góc độ quy luật kinh tế khách quan.

### 4. Phân tích động lực (Incentive Audit)
- Mismatch kỳ hạn và chi phí vốn cao được lý giải do đặc thù cấu trúc nguồn vốn Việt Nam (80-90% tiền gửi ngắn hạn) chứ không đổ lỗi cho lỗi chủ quan của các ngân hàng hay các tập đoàn tư nhân.
- Hợp vốn tín dụng được giải mã như một phản ứng kỹ thuật hợp pháp để tuân thủ Luật Các TCTD mới về giới hạn an toàn cho vay một khách hàng và nhóm liên quan (10-15% vốn tự có).

## Verdict: DUYỆT (Kịch bản hoàn toàn an toàn về biên tập và pháp lý)
