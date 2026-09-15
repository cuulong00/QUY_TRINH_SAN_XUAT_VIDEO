# 07_outline.md (Đã loại bỏ trùng lặp với Tập 1)

## THESIS MAP
- **Core Thesis:** Vệ tinh VinSpace là bài test sinh tử về năng lực Tích hợp Hệ thống (Systems Engineering) của người Việt, nơi phần mềm chuyến bay phải gánh vác rủi ro của linh kiện thương mại rẻ tiền để sống sót ở quỹ đạo LEO.

## RETENTION MAP
- **Mở đầu:** Nghịch lý 350.000 USD và tỷ lệ chết yểu 60%.
- **Chương 2:** Bóc tách 7 hệ thống, chỉ ra phần mua và phần tự làm.
- **Chương 3:** Giải mã kỹ thuật D2D giúp xe VinFast kết nối vệ tinh.
- **Chương 4:** Hai sát thủ vô hình (Bức xạ, Nhiệt độ) giết chết vệ tinh.
- **Chương 5:** Quy trình AIT tàn khốc.
- **Chương 6:** Đúc kết về giá trị của Kỹ sư hệ thống.

## OUTLINE

### CHƯƠNG 1: HOOK — NGHỊCH LÝ 350.000 USD (Đã viết)
- Giá phóng 350.000 USD + vệ tinh 120.000 USD = Quá rẻ.
- Câu hỏi: Vậy VinSpace tự làm cái gì? 
- Rủi ro 60% thất bại ngay lần đầu.

### CHƯƠNG 2: GIẢI PHẪU KIẾN TRÚC VỆ TINH (Đã viết)
- Phân loại: LEO, Nano/Micro (<50kg).
- Nhóm mua ngoài (COTS): Bus, EPS, ADCS.
- Nhóm tự R&D: SDR, Edge AI, RTOS.
- Sự tương đồng với VinFast (Pack pin, BMS) và SpaceX (TMR, chip dân dụng).

### CHƯƠNG 3: GIAO THỨC D2D VÀ KẾT NỐI VINFAST (Tái cấu trúc)
- VinSpace không cạnh tranh Starlink (băng thông rộng), mà tập trung IoT doanh nghiệp.
- Giải phẫu 3GPP R17 (Direct-to-Device).
- Chip Qualcomm Snapdragon Auto 5G Gen 2 trên xe VinFast.
- Xóa bỏ vùng lõm sóng.

### CHƯƠNG 4: HAI SÁT THỦ VÔ HÌNH TRÊN QUỸ ĐẠO LEO
- Sát thủ 1: Bức xạ SEU lật bit, Latch-up cháy mạch. Giải pháp RTOS + TMR.
- Sát thủ 2: Ứng suất nhiệt (+120°C đến -70°C). Góc Beta. 
- Vũ trụ không có dịch vụ "Triệu hồi" (Recall).

### CHƯƠNG 5: QUY TRÌNH AIT — NƠI KHAI SINH VỆ TINH
- AIT: Assembly, Integration, and Testing.
- Buồng nhiệt chân không TVAC (mô phỏng nhiệt độ vũ trụ).
- Bàn rung xóc (mô phỏng gia tốc tên lửa Falcon 9).
- Trạm gác cuối cùng trước khi bàn giao cho SpaceX.

### CHƯƠNG 6: KẾT LUẬN — BÀI TOÁN KỸ SƯ HỆ THỐNG
- Liên hệ lịch sử Hyundai, Samsung, TSMC.
- Sản xuất vệ tinh là mài giũa năng lực "Systems Engineering".
- Năng lực hấp thụ thất bại để vươn lên chuỗi giá trị toàn cầu.
