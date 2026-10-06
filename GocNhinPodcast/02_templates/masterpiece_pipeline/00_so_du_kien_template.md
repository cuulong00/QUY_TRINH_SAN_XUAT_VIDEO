# SỔ DỮ KIỆN XUYÊN TẬP — `episodes/[slug]/00_so_du_kien.md`

> Một dòng cho mỗi mắt xích (dữ kiện, suy luận, đặt cược) mà tập dùng. Tạo ở Pha 1 từ các OBS của bản đồ nền; mỗi pha **thêm dòng**, không ghi đè, không xóa (bỏ thì đổi trạng thái và ghi lý do). Outline, brief, chương **trỏ mã M**, không chép lại câu, nên nhãn không rơi khi viết lại. Bảng claim trong `10_compliance_report.md` là bản trích từ sổ này. Cổng máy `scripts/kiem_pha.py` đọc sổ để bắt: số không có mã M, câu viết vượt nhãn, chân đỡ Pha 1 biến mất.

## Quy ước nhãn (theo `.agents/rules/claim-ledger.md`, cách nói theo `00_core/stance_and_judgment.md` §5)
- `verified_data`: có mã OBS hiện hành hoặc câu nguyên văn trong vault kèm URL/ngày. Nói thẳng.
- `market_analysis`: suy luận từ ≥1 hàng verified; ghi đường đi (từ M? → kết luận). Nói kiểu "đặt hai con số này cạnh nhau…".
- `opinion_commentary`: đặt cược của kênh; nói "chúng tôi cho rằng" (≤4 lần/tập).
- Phép tính kênh tự làm ghi `tự tính: M? / M?` và nhãn `market_analysis`; không có đầu vào mã M thì không được tính.

## Bảng mắt xích
| Mã M | Mắt xích (một câu ngắn) | Nhãn | Nguồn (`vault/R0X` hoặc URL + ngày, kèm câu nguyên văn ≤15 từ) | Kỳ · phạm vi · đơn vị | Mã E (`00_bang_gia_thuyet.md`) | Pha đưa vào | Dùng ở (chương) | Trạng thái | Ngày |
|---|---|---|---|---|---|---|---|---|---|
| M01 | | verified_data | `vault/R0X` hoặc URL | | E01 | 1 | | dùng | |
| M02 | | market_analysis | từ M01 + M03: … | | | 3 | | dùng | |
| M03 | | opinion_commentary | đặt cược của kênh, điều kiện sai: … | | | 3 | | dùng | |

## Chân đỡ của giả thuyết dẫn đầu (điền ở Pha 1, kiểm ở Pha 3 và Pha 4)
| Mã M | Vai trò trong giả thuyết | Còn mặt ở Pha 3 brief? | Còn mặt ở Pha 4 outline? | Nếu bỏ: lý do |
|---|---|---|---|---|
| | | | | |

## Kho vật chứng thực chứng (`VC-01` đến `VC-XX`, thêm 06/10/2026, user duyệt)
> Ghi những gì có thể cho người xem THẤY: một quyết định, văn bản, công trình, khoảnh khắc có ngày giờ và chủ thể đứng sau.
> Nuôi các trường `vat_chung` và `chu_the_va_dong_co` của brief chương, và chỉ tiêu V của khung chấm nghệ thuật.
> CẤM TUYỆT ĐỐI cảnh dựng lại hay nhân vật bịa. Mọi vật chứng bắt buộc có nguồn mở được kèm câu nguyên văn.
> Không bắt buộc với tập đang chạy trước ngày 06/10/2026.

| Mã VC | Vật chứng (mô tả một câu) | Ngày giờ | Chủ thể và điều họ muốn | Nguồn và câu nguyên văn | Câu hỏi Pha 1 trả lời | Dùng ở (chương) | Ghi chú |
|---|---|---|---|---|---|---|---|
| VC-01 | [Văn bản, quyết định, công trình hoặc khoảnh khắc có thật] | [Ngày/tháng/năm] | [Chủ thể đứng sau và điều họ muốn] | [URL / vault kèm câu nguyên văn] | [Mã câu hỏi hoặc ô Pha 1, vd: CH01] | | dùng |
| VC-02 | | | | | | | dùng |
