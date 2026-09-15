<!--
PROVENANCE METADATA:
- Target File: episodes/grab-vs-gsm-tai-xe-tat-app/research_vault/01_september_2026_grab_strike_and_dynamic_fare.md
- Extracted From: Master Notebook (0c6bc1a7-7f75-4254-b521-6b4a79f7912c) Deep Research Report (2026-09-09)
- Key Topics: Sự kiện bãi công tắt app 12-13/9/2026, tăng phí nền tảng 28/4/2026, Ghost Bookings, Dynamic Pricing & Surge Pricing bẻ gãy bãi công theo Cân bằng Nash.
-->

# HỒ SƠ 01: SỰ KIỆN TẮT APP 12–13/9/2026 & THUẬT TOÁN SURGE PRICING BẺ GÃY ĐÌNH CÔNG

## 1. Nguyên nhân trực tiếp bùng phát bãi công ngày 12–13/9/2026
- **Cú hích phí nền tảng ngày 28/04/2026:** Grab quyết định điều chỉnh tăng phí nền tảng cố định thu từ khách hàng:
  * Xe 2 bánh (GrabBike, GrabFood): tăng lên **3.000 đồng/chuyến**.
  * Xe 4 bánh (GrabCar): tăng từ **5.000 đồng đến 19.000 đồng/chuyến** tùy cự ly và khu vực.
  * *Bản chất bất đối xứng:* Khoản phí này thu thêm từ khách dưới dạng phụ phí vận hành nhưng không được tính vào giá cước cơ sở chia cho tài xế. Doanh thu của tài xế không tăng, nhưng khách hàng phải trả đắt hơn, dẫn đến lượng tip giảm và khách phàn nàn.
- **Tổng tỷ lệ khấu trừ thực tế đạt đỉnh kỷ lục:**
  * Thuế VAT 8% (theo Nghị định 174/2025/NĐ-CP áp dụng từ tháng 7/2025 đến hết năm 2026).
  * Chiết khấu hoa hồng ứng dụng: 20% – 25% (2 bánh) và 25% – 28.6% (4 bánh).
  * Thuế TNCN 1.5% đối với doanh thu trên 100 triệu/năm.
  * Phí nền tảng cố định 3.000đ – 19.000đ/cuốc.
  * **Tổng tỷ lệ khấu trừ thực tế chạm mốc 28,2% – 32,5% đối với GrabBike và 28,5% – 35,8% đối với GrabCar**.
- **Cơn bão chi phí xăng dầu:** Giá xăng RON95 leo thang tiệm cận 30.000đ/lít khiến chi phí nhiên liệu ngốn tới **40% – 50% tổng doanh thu** của tài xế xe xăng. Cộng với hệ số chạy rỗng (Dead Mileage) từ 20% đến 30% để đón khách xa, biên lợi nhuận ròng của tài xế bị bóp nghẹt hoàn toàn.

## 2. Diễn biến bãi công và Chiến thuật "Ghost Bookings"
- Đầu tháng 9/2026, hàng chục nghìn tài xế tại Hà Nội, TP.HCM và Đà Nẵng lập các nhóm kín kêu gọi ngắt kết nối ứng dụng trong 48 giờ (ngày 12 và 13/9/2026).
- **Chiến thuật "Ghost Bookings" (Đặt cuốc ảo):** Tài xế rủ nhau tạo các tài khoản ảo đặt chuyến rồi hủy liên tục hoặc nhận cuốc nhưng không di chuyển nhằm làm nhiễu loạn thuật toán điều phối và gây tê liệt hệ thống tại các điểm nút giao thông trọng điểm.

## 3. Cơ chế Thuật toán Surge Pricing bẻ gãy bãi công theo Cân bằng Nash
- **Kích hoạt giá cước động (Surge Pricing):** Khi hàng ngàn tài xế ngắt kết nối, nguồn cung phương tiện tại các quận trung tâm lập tức sụt giảm nghiêm trọng. Thuật toán AI của Grab tự động kích hoạt tính năng nhân giá cước lên **1,5 đến 2,5 lần** bình thường.
- **Bài toán Lưỡng nan của Tù nhân (Prisoner's Dilemma) & Cân bằng Nash:**
  * Tài xế công nghệ là lao động tự do không có hợp đồng lao động, không có quỹ dự phòng công đoàn để trợ cấp ngày nghỉ chạy. Họ chịu áp lực tiền cơm ngày mai, tiền thuê trọ và nợ ngân hàng.
  * Đứng trước bản đồ đỏ rực với mức cước tăng 1.5x - 2.5x, chiến lược thống trị cá nhân (Dominant Strategy) của từng người là: **Lẳng lặng bật app chạy lén để bắt các cuốc xe giá cao**.
  * Hành động đơn lẻ này nhanh chóng lan rộng, biến các tài xế thành đối thủ cạnh tranh của chính đồng nghiệp mình. Khối đoàn kết tự phát tan vỡ từ bên trong chỉ sau vài giờ mà Grab không cần đưa ra bất kỳ nhượng bộ chính sách nào.
- **Chế tài thuật toán trừng phạt:** Hệ thống tự động kích hoạt tính năng nhận chuyến cưỡng bức đối với tài xế có tỷ lệ nhận chuyến < 50%, hoặc khóa tài khoản vĩnh viễn đối với những tài xế bị phát hiện tham gia đặt cuốc ảo.

## 4. Sự đối lập tài chính: Thu hoạch lợi nhuận cho phố Wall
- Trong khi tài xế kiệt quệ, BCTC của Grab Holdings Limited cho thấy:
  * Doanh thu hợp nhất toàn cầu năm 2025 đạt **3,37 tỷ USD**, lần đầu tiên báo **lãi ròng 200 triệu USD**, Adjusted EBITDA đạt **500 triệu USD**.
  * Thị trường Việt Nam đóng góp **255 triệu USD** doanh thu năm 2025.
  * Nửa đầu năm 2026 (H1/2026), mảng dịch vụ di chuyển (Mobility) toàn cầu của Grab tiếp tục đạt **668 triệu USD**, riêng Việt Nam mang về **140 triệu USD** doanh thu (+12% YoY).
- Grab bước dứt khoát vào "Pha thu hoạch" (Harvesting Phase): Tối ưu hóa dòng tiền sạch bằng cách siết chi phí và chuyển toàn bộ gánh nặng lạm phát sang lưng người lao động.
