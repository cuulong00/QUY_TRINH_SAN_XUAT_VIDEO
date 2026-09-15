# Báo Cáo Tổng Hợp Nghiên Cứu Chuyên Sâu: Mổ Xẻ Công Nghệ & Tự Chủ Chuỗi Cung Ứng VinFast

Tài liệu này tổng hợp toàn bộ dữ liệu thực chứng chuyên sâu được trích xuất từ 56 nguồn nghiên cứu trên NotebookLM và kết quả khảo sát kỹ thuật về năng lực sản xuất, làm chủ phần cứng, phần mềm và chuỗi cung ứng của VinFast.

---

## I. MẢNG CƠ KHÍ NẶNG & HỆ TRUYỀN ĐỘNG (TỔ HỢP HẢI PHÒNG)

Tại tổ hợp Hải Phòng (mức độ tự động hóa trung bình đạt 90% - 95%), VinFast trực tiếp làm chủ các công đoạn chế tạo cơ khí cốt lõi:

### 1. Xưởng Dập Tấm Thân Vỏ (50.000 m²)
- **VinFast TỰ LÀM CHỦ:** Tự chủ dập hoàn chỉnh hơn 20 tấm thân vỏ lớn cơ bản cấu thành mỗi chiếc xe (ca-pô, chắn bùn, sườn xe, nóc xe, sườn bên, cửa xe, bệ khung gầm). VinFast là nhà máy duy nhất tại Việt Nam sở hữu năng lực dập tấm lớn tự động hóa.
- **Thiết bị & Công nghệ nhập khẩu:** Dây chuyền dập liên hợp tốc độ cao *Tandem XXL Press line* của Schuler (Đức), vận hành đạt 16-20 phát dập/phút. Hệ thống kiểm soát dung sai hình học sử dụng máy đo CMM 3D và thiết bị quét white scanner.

### 2. Xưởng Hàn Thân Xe BIW (100.000 m²)
- **VinFast TỰ LÀM CHỦ:** Hàn ghép các mảng tấm dập thành bộ khung xương xe (*Body-in-White - BIW*) hoàn chỉnh (thông qua liên doanh với Aapico Hitech tại Supplier Park Hải Phòng).
- **Thiết bị & Công nghệ nhập khẩu:** Tự động hóa 100% bằng **1.200 robot công nghiệp ABB (Thụy Sĩ)**. Nhà xưởng được thiết kế, lắp đặt bởi FFT, EBZ, Hirotec (Châu Âu/Nhật Bàn) và quản lý bằng hệ điều hành sản xuất MES của Siemens (Đức).

### 3. Xưởng Động Cơ Điện e-Motor (50.000 m²)
- **VinFast TỰ LÀM CHỦ:**
  * Gia công cơ khí chính xác vỏ nhôm đúc chịu lực bao quanh mô-tơ điện (*Motor Housing*).
  * Chèn cách điện stator, quấn và định hình các cuộn dây đồng, lắp ráp rô-to (*Rotor*) và tích hợp hệ thống trục truyền động điện liền vỏ hộp số (*Reducer*).
  * **Công nghệ quấn dây đồng dạng Hairpin dẹt (Rectangular Hairpin):** Sử dụng máy uốn tự động tạo các thanh hairpin bằng đồng phẳng giúp đạt tỷ lệ lấp đầy rãnh stator (*slot fill factor*) trên 70%, nâng cao mật độ công suất động cơ. Hàn laser các đầu kết nối hairpin, sấy tẩm nhựa cách điện stator bằng phương pháp trickling nhiệt cảm ứng dòng điện, lắp ráp nam châm vĩnh cửu unmagnetized vào rotor, cân bằng động và điện từ hóa nam châm vĩnh cửu.
- **Thiết bị & Công nghệ nhập khẩu:** Dây chuyền quấn hairpin tự động từ GROB-WERKE (Đức) và Haosen. Dây chuyền gia công cơ khí chính xác từ GROB, Thyssenkrupp, AVL (Áo), và MAG.
- **Hợp phần nhập khẩu:** Chip bán dẫn công suất SiC MOSFETs / IGBT dùng cho bộ biến tần (*Inverter*) nhập từ Infineon, STMicroelectronics.

---

## II. KHỐI PIN & PHẦN MỀM BMS VIN ES

Sau khi sáp nhập mảng sản xuất pin VinES Energy Solutions vào cuối năm 2023, VinFast đã làm chủ toàn diện khâu thiết kế đóng gói bộ pin và lập trình phần mềm quản lý:

### 1. Thiết kế Phần cứng Pack Pin (Battery Pack Assembly)
- **VinFast TỰ LÀM CHỦ:** Tự chủ hoàn toàn thiết kế vỏ nhôm pack pin, cấu trúc bảo vệ va đập dưới gầm, đường ống tản nhiệt chất lỏng chủ động (*Liquid cooling loops*) luân chuyển nước-glycol kết hợp Battery Chiller duy trì 20°C - 40°C, và thiết kế hệ thống rơ-le ngắt cao áp (*High-voltage contactors*) bảo vệ ngắt dòng điện hàng trăm Ampe trong mili-giây khi sự cố.
- **Quy trình lắp ráp tự động:** Dây chuyền đóng gói đạt mức tự động hóa 75% - 80%. Khâu kiểm tra chất lượng cell pin đầu vào được tự động hóa 100% (đo nội trở và điện áp đồng nhất).

### 2. Phần mềm Quản lý Pin (BMS - Battery Management System) Tự Viết
Do cell pin LFP có đường cong xả điện cực kỳ phẳng (flat discharge voltage curve), đội ngũ kỹ sư VinFast đã tự viết thuật toán BMS thông minh độc quyền:
- **Tính toán dung lượng SOC (State of Charge):** Tích hợp thuật toán đếm điện lượng Coulomb counting kết hợp giám sát điện áp thời gian thực.
- **Dự báo tuổi thọ SOH (State of Health):** Theo dõi nội trở của từng cell trong chu kỳ sạc để tính toán mức độ suy giảm dung lượng và cảnh báo bảo trì.
- **Quản lý nhiệt độ chủ động:** BMS điều khiển van/bơm dung dịch qua dữ liệu từ 2 cảm biến nhiệt độ gắn trên mỗi cell để ngăn hiện tượng nhiệt cục bộ (*thermal runaway*).
- **Cân bằng cell tích cực (Active Cell Balancing):** Tái phân bổ dòng điện giữa các cell mạnh và yếu trong thời gian dưới 30 phút.

---

## III. NHÀ MÁY ĐÚC CELL PIN LFP VŨNG ÁNG (HÀ TĨNH)

- **VinFast TỰ LÀM CHỦ VẬN HÀNH:** Tổ hợp nhà máy liên doanh pin LFP rộng 14 ha tại Vũng Áng (vốn đầu tư 275 triệu USD, 6.330 tỷ VNĐ). Công suất 5 GWh/năm (khoảng 30 triệu cell pin prismatic/năm) chế tạo cell pin LFP trực tiếp cung ứng cho pack pin VF 3, VF 5.
- **Mô hình hợp tác:** Liên doanh giữa Gotion High-Tech (51% cổ phần - chuyển giao công nghệ hóa học) và VinES (49% cổ phần).
- **Hợp phần nhập khẩu:** Nhập khẩu nguyên liệu thô đầu vào như Lithium Carbonate, Synthetic Graphite (graphite tổng hợp làm cực âm) và tiền chất vật liệu hoạt tính điện cực dương (CAM) do Việt Nam chưa có công nghiệp tinh chế khoáng sản thượng nguồn.

---

## IV. PHẦN MỀM AI, TRỢ LÝ THÔNG MINH & HỆ ĐIỀU HÀNH XE

Đây là khu vực VinFast đạt mức tự chủ sâu nhất nhờ sự cộng hưởng của hệ sinh thái Vingroup:

### 1. Trợ lý ảo thông minh ViVi 2.0 (VinBigData)
- **VinFast TỰ LÀM CHỦ LẬP TRÌNH:** Lập trình lõi hệ thống tương tác người - máy (HMI) trên VinFast Smart OS. Tích hợp mô hình ngôn ngữ lớn **ViGPT LLM (1,6 tỷ tham số, 600 GB dữ liệu tiếng Việt tinh chỉnh)**. Khả năng nhận diện giọng nói tự nhiên đa vùng miền (>98%) và hỗ trợ *Offline Fallback* điều khiển xe khi mất kết nối mạng.

### 2. Thuật toán Thị giác Máy tính & Lái An toàn (VinAI)
- **DMS (InteriorSense):** Thuật toán AI phân tích góc mắt, mí mắt qua camera hồng ngoại IR phát hiện tài xế buồn ngủ/mất tập trung.
- **SVM 360 (SurroundSense):** Thuật toán ghép hình ảnh 4 camera fisheye hiển thị chế độ 3D và công nghệ "Jelly View" (xem xuyên gầm xe).
- **Touch2Park:** Công nghệ đỗ xe tự động *camera-first* không cần cảm biến siêu âm.
- **MirrorSense:** Hệ thống AI tự động chỉnh gương chiếu hậu theo hướng mắt nhìn tài xế (Giải thưởng CES 2024).
- **Tương thích phần cứng:** Thuật toán VinAI dạng *Hardware-Agnostic*, tối ưu hóa linh hoạt trên NPU của Qualcomm Snapdragon Digital Chassis và Nvidia Drive Orin.

### 3. Kiến trúc Điện - Điện tử EE 2.0, VMCU và FOTA
- **VinFast TỰ LÀM CHỦ THIẾT KẾ:** Kiến trúc domain/zonal EE 2.0 hợp nhất các ECU rời rạc thành bộ điều khiển trung tâm xe **VMCU**, giảm 30%-40% chi phí hóa đơn vật liệu (BOM). Tự viết phần mềm **FOTA (Firmware Over-The-Air)** cập nhật thuật toán xe từ xa.
- **Bán dẫn & Siêu máy tính nhập khẩu:** Nhập khẩu siêu máy tính NVIDIA DRIVE / Hyperion, chip Qualcomm Snapdragon, và hệ thống ECU an toàn phanh ABS/ESP từ Bosch (Đức).

---

## V. BẢNG TỔNG HỢP MỔ XẺ: TỰ LÀM CHỦ VS NHẬP KHẨU TIER-1

| Cấu phần công nghệ | VinFast Trực Tiếp Làm Chủ / Tự Sản Xuất / Lập Trình | Nhập Khẩu từ Đối Tác Tier-1 Toàn Cầu |
| :--- | :--- | :--- |
| **Cơ khí & Thân vỏ** | Dập vỏ tấm lớn (Schuler); hàn khung xương BIW tự động 100% bằng 1.200 robot ABB; sơn tĩnh điện Ro-Dip. | Đồ gá khuôn dập (Aapico, Böllhoff). |
| **Động cơ điện (e-Motor)** | Đúc vỏ nhôm mô-tơ; quấn dây đồng Hairpin dẹt tự động; gia công/lắp ráp Rotor & Stator; sấy tẩm trickling & từ hóa. | Máy quấn dây/gia công (Grob, Thyssenkrupp, AVL); Chip công suất SiC/IGBT (Infineon, STMicroelectronics). |
| **Khối Pin (Battery Pack)** | Thiết kế vỏ nhôm; tích hợp đường ống Liquid Cooling; rơ-le ngắt cao áp; **Phần mềm BMS tự viết** (SOC, SOH, làm mát, Active Cell Balancing). | Dây chuyền đóng gói tiêu chuẩn Châu Âu/Mỹ; nhập Cell pin ban đầu (CATL, Samsung SDI, LG Chem). |
| **Cell Pin (Tế bào Hóa học)** | Vận hành nhà máy 5 GWh Hà Tĩnh; tự đúc cell prismatic LFP cho VF 3, VF 5. | Chuyển giao hóa học cell (Gotion High-Tech); Nhập khẩu Lithium thô, Graphite, CAM. |
| **Hệ thống Điện tử & OS** | Thiết kế kiến trúc EE 2.0 domain/zonal; tự làm chủ bộ điều khiển trung tâm VMCU; tự viết hạ tầng **FOTA cập nhật từ xa**. | Hộp điều khiển ECU phanh ABS, ESP, túi khí, cảm biến chủ động (Bosch). |
| **Trí Tuệ Nhân Tạo & ADAS** | Lập trình **Trợ lý ảo ViVi 2.0** (ViGPT LLM 1.6B params); Lập trình thuật toán AI VinAI (**DMS, SVM 360, Touch2Park, MirrorSense**). | Chip bán dẫn AI & Siêu máy tính (NVIDIA, Qualcomm); Thuật toán ADAS L2++/L4 cao cấp (Autobrains, Tensor). |
