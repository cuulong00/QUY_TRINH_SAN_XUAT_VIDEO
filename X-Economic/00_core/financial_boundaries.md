# financial_boundaries.md — Vùng Cấm Nội Dung Tài Chính (Investment Advice Redline)

## Mục đích
Kênh X-Economy phân tích doanh nghiệp, thị trường vốn và chính sách kinh tế — nhưng **không phải là kênh tư vấn đầu tư có giấy phép**. File này định nghĩa ranh giới giữa "bình luận/phân tích kinh tế" (được phép) và "tư vấn đầu tư" (bị cấm), phối hợp cùng `the_compliance_editor` tại Pha 10 & 11.

## 1. Được phép (Commentary & Analysis)
- Mô tả cơ chế dòng tiền, cấu trúc vốn, đòn bẩy, biên lợi nhuận của một doanh nghiệp dựa trên báo cáo tài chính đã công bố.
- Phân tích bối cảnh vĩ mô (lãi suất, tỷ giá, giá hàng hóa) và tác động logic tới một ngành/doanh nghiệp.
- Trình bày các kịch bản rủi ro (risk scenarios) mang tính trung lập: "nếu X xảy ra, doanh nghiệp/ngành sẽ chịu áp lực Y" — miễn không kèm khuyến nghị hành động.
- Trích dẫn nhận định của các chuyên gia/tổ chức phân tích uy tín (có nguồn công khai), có gắn nhãn rõ đây là quan điểm của bên thứ ba.

## 2. Tuyệt đối cấm (Investment Advice Redline)
- **Khuyến nghị mua/bán/giữ** bất kỳ cổ phiếu, trái phiếu, tiền mã hóa hay tài sản tài chính cụ thể nào.
- **Dự đoán mức giá mục tiêu** hoặc thời điểm "vào hàng/thoát hàng".
- **Ngôn ngữ "phím hàng"**: "múc mạnh tay", "chốt lời ngay", "cơ hội vàng để xuống tiền", "đu đỉnh".
- **Cam kết lợi nhuận hoặc mức độ an toàn** của bất kỳ khoản đầu tư nào ("chắc chắn sinh lời", "an toàn tuyệt đối").
- **Tư vấn phân bổ danh mục cá nhân** ("bạn nên dồn 30% tài sản vào ngành này").

## 3. Xử lý khi đề tài chạm ranh giới
- Nếu kịch bản cần đề cập một cổ phiếu/tài sản cụ thể để giải thích cơ chế thị trường: mô tả **hiện tượng đã xảy ra** (giá đã biến động thế nào, vì sao), không mô tả **điều sẽ xảy ra kèm khuyến nghị**.
- Nếu khán giả có thể suy ra một hành động đầu tư ngầm định dù không nói thẳng ra, `the_compliance_editor` phải gắn thêm câu trung hòa rõ ràng (ví dụ: "Đây là phân tích cơ chế, không phải khuyến nghị đầu tư").
- Mọi episode có nội dung thị trường vốn bắt buộc chứa dòng lưu ý: `Nội dung chia sẻ luận điểm khách quan, mang tính thảo luận và xây dựng. Mọi phân tích không cấu thành khuyến nghị đầu tư tài chính.` (theo `.agents/AGENTS.md`).

## 4. Tham chiếu chuyên gia phụ trách
- `the_capital_markets_analyst` — chịu trách nhiệm về độ chính xác số liệu tài chính và giữ giọng "hoài nghi có phương pháp" thay vì giọng phím hàng.
- `the_compliance_editor` — chịu trách nhiệm audit cuối cùng đối chiếu với file này tại Pha 10 & 11 (`10_compliance_report.md`).
