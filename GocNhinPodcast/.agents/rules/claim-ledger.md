# claim-ledger

Nguồn gốc của mọi claim là **sổ dữ kiện xuyên tập** `episodes/**/00_so_du_kien.md` (khuôn: `02_templates/masterpiece_pipeline/00_so_du_kien_template.md`, tạo ở Pha 1, chỉ thêm dòng). Bảng claim trong `10_compliance_report.md` là bản trích từ sổ, không tạo mã mới. Áp dụng cho sổ và cho bảng claim trong `episodes/**/10_compliance_report.md` (các tên cũ `06_claim_ledger.md`, `10_claim_ledger.md` không còn dùng). Cách nói tương ứng với từng nhãn: `00_core/stance_and_judgment.md` §5.

## Taxonomy lock
Chỉ dùng 3 classification sau:
- `verified_data`
- `market_analysis`
- `opinion_commentary`

## Rules
- Nếu claim không có dữ liệu cứng đủ chắc, không được gắn `verified_data`.
- Nếu claim là diễn giải dựa trên dữ liệu, dùng `market_analysis`.
- Nếu claim là nhận định/góc nhìn, dùng `opinion_commentary`.
- Không bịa nguồn hoặc mô tả nguồn mơ hồ.
- Ledger phải luôn bám sát script/chapter hiện hành, không để claim mồ côi.
- Outline, brief, chương trỏ mã `M-xx` của sổ thay cho chép lại câu; nhãn đi theo mã, không gán lại khi viết lại. Mắt xích chưa có trong sổ thì thêm dòng trước khi viết.
- Phép tính kênh tự làm phải ghi `tự tính: M? / M?` và mang nhãn `market_analysis`.