# BÓC TÁCH KỸ THUẬT VÀ CHUỖI CUNG ỨNG NỘI ĐỊA HÓA VINFAST
**Tài liệu Nghiên cứu Chuyên sâu (Deep Research Vault Q-011)**

---

## 1. HỆ THỐNG ĐỘNG CƠ ĐIỆN (E-AXLE 3-IN-1)

### A. Cấu trúc tích hợp 3-trong-1 (3-in-1 E-Axle)
Hệ truyền động của VinFast đóng gói đồng bộ 3 thành phần trong cùng 1 vỏ hộp hợp kim nhôm để triệt tiêu cáp kết nối cao áp, giảm tổn hao truyền tải năng lượng:
1. **Động cơ điện (Electric Motor):** Đồng bộ nam châm vĩnh cửu (PMSM) làm mát bằng dung dịch glycol-nước.
   - *Stator:* Công nghệ quấn dây trâm cài (**Hairpin Winding**) tự động, nâng hệ số lấp đầy rãnh stator (slot fill factor) > 70%, giảm điện trở đồng, tăng tản nhiệt, đạt hiệu suất cực đại 97%.
   - *Rotor:* Tích hợp nam châm đất hiếm Neodymium-Iron-Boron (NdFeB) chịu nhiệt độ cao trong rãnh rotor (IPM), đạt tốc độ quay cực đại 16.000 RPM.
2. **Bộ biến tần (Inverter / Power Electronics):** Biến đổi điện DC từ pin thành AC 3 pha điều khiển motor. Sử dụng bán dẫn **Silicon Carbide (SiC MOSFET)** chịu điện áp và nhiệt độ cao, giảm hao tổn đóng cắt.
3. **Hộp số giảm tốc đơn cấp (Reduction Gearbox):** Tỷ số truyền tối ưu với cụm vi sai cơ khí chính xác cao.

### B. VinFast làm chủ & sản xuất tại Cát Hải (Hải Phòng)
- **Đúc & gia công vỏ nhôm (Housing machining):** Đúc nhôm áp lực cao vỏ động cơ/hộp số và gia công CNC chính xác tại phân xưởng động cơ Hải Phòng.
- **Chế tạo Stator Hairpin:** Đùn ép và quấn cuộn dây đồng Stator dạng trâm cài hoàn toàn tự động (dây chuyền Thyssenkrupp System Engineering).
- **Lắp ráp Rotor & E-axle:** Lắp ráp cơ khí định tâm rotor, đóng gói 3-trong-1 Stator + Rotor + Inverter + Hộp số.
- **Kiểm thử E-end-of-line (EOL) test:** Thử nghiệm xả tải, độ kín khí và độ bền cơ học 100% sản phẩm trước khi chuyển sang xưởng lắp ráp.

### C. Danh mục Linh kiện & Nhà cung cấp Tier-1 toàn cầu
- **Inverter & Biến tần:** Vitesco Technologies / Bosch.
- **Bộ điều khiển phanh tái tạo cơ điện tử:** Bosch iBooster / ESP.
- **Cụm truyền động bánh răng & vi sai:** ZF Group / ERAE AMS.
- **Chip SiC MOSFET công suất:** Infineon / STMicroelectronics.
- **Vòng bi động cơ tốc độ cao:** SKF (chịu dòng điện rò chống mài mòn điện hóa).

---

## 2. HỆ THỐNG PIN (BATTERY PACK & BMS)

### A. Bản đồ Sourcing Cell Pin
1. **CATL:** Cung cấp cell pin LFP/NMC và công nghệ **Cell-to-Pack (CTP)** tích hợp trực tiếp cell vào khung vỏ (bỏ module trung gian) cho VF 9 (92–123 kWh), VF 8, VF 7.
2. **Gotion High-Tech:** Cung cấp cell LFP prismatic cho VF 3, VF 5.
3. **Samsung SDI & LG Energy Solution:** Samsung SDI cung cấp cell NMC trụ 21700 cho lô VF 8 xuất Mỹ đầu tiên; LG Energy Solution cung cấp cell NMC dạng túi (pouch cell) cho dải thương mại.
4. **Liên doanh VinES - Gotion (Hà Tĩnh):** Tổng vốn 275 triệu USD, diện tích 14 ha, công suất **5 GWh/năm** (~30 triệu cell/năm) sản xuất đại trà cell LFP lăng trụ mã **L141F** (điện cực âm than chì nhân tạo) tại Vũng Áng.

### B. VinFast / VinES làm chủ 100%
1. **Khung vỏ Pack nhôm chịu lực (Battery Pack Enclosure):** Tự thiết kế và đúc khung nhôm chịu lực va đập đa hướng chống va đập gầm, đạt chuẩn kháng nước/bụi **IP68**.
2. **Tấm tản nhiệt chất lỏng (Cooling Plate):** Tự thiết kế các rãnh tản nhiệt nhôm đúc đáy module tạo dòng chảy rối (**turbulent flow**), làm mát đồng đều cell pin + tích hợp bộ sưởi cao áp HV Heater.
3. **Hệ thống Quản lý Pin BMS (Battery Management System):**
   - *Phần cứng bo mạch BMS:* Tự thiết kế và sản xuất bo mạch điện tử BMS.
   - *Phần mềm mã nguồn BMS:* Thuật toán cân bằng cell chủ động/thụ động; áp dụng **Bộ lọc Kalman mở rộng (EKF)** ước lượng chính xác dung lượng pin (SoC) và độ suy hao vật lý (SoH); tối ưu dốc tự hao hụt < 1.5%/ngày khi bật BMS và < 4%/tháng khi tắt BMS thủ công.

---

## 3. PHẦN MỀM ĐIỀU KHIỂN (VCU, SDV) & TRÍ TUỆ NHÂN TẠO (VINAI / VINBRAIN)

### A. VCU (Vehicle Control Unit) & Xe định nghĩa bằng Phần mềm (SDV)
VinFast làm chủ 100% mã nguồn phần mềm VCU:
- **Phân bổ mô-men xoắn chủ động (Torque Control):** Tính toán và phân bổ lực kéo giữa 2 cầu AWD trong vài mili-giây.
- **Điều khiển phanh tái tạo (Regenerative Braking):** Phối hợp mượt mà giữa phanh điện nạp ngược năng lượng và phanh ma sát thủy lực.
- **Cập nhật từ xa FOTA (Firmware Over-The-Air):** Mã hóa đám mây cập nhật phần mềm định kỳ cho tất cả ECU trên xe.

### B. Hệ sinh thái AI Việt Nam (VinAI & VinBrain)
1. **VinAI:**
   - *Driver & Occupant Monitoring System (DOMS):* Nhận diện hành vi xao nhãng, ngủ gật của tài xế bằng camera hồng ngoại.
   - *MirrorSense:* AI tự động chỉnh gương chiếu hậu theo góc nhìn mắt tài xế 3D (đoạt giải CES Innovation Award).
   - *DrunkSense:* Nhận diện nồng độ cồn qua phân tích hành vi lái xe thụ động (độ nhạy 85%).
   - *3D ASVM & Jelly View:* Dựng hình ảnh 3D toàn cảnh Bird's Eye View và chế độ **gầm xe trong suốt** giúp nhìn xuyên thấu sàn xe.
   - *Touch2Park:* Đỗ xe tự động cấp độ 2 dựa hoàn toàn vào thị giác máy tính AI (Computer Vision) thay vì cảm biến siêu âm.
   - *Trợ lý ảo ViVi:* AI giọng nói tiếng Việt đa vùng miền.
2. **VinBrain (AIScaler):** Nền tảng tự động làm sạch và gán nhãn dữ liệu hình ảnh đường phố để huấn luyện mạng thần kinh nhân tạo cho ADAS.

### C. Vi chip Xử lý Trung tâm (Hardware)
- **NVIDIA Drive Orin-X (254 TOPS):** Chip tính toán hiệu năng cao chuyên trách ADAS L2+ và tự lái.
- **Qualcomm Snapdragon 8155 / 8295:** Chip điều khiển màn hình Smart Cockpit và xử lý thuật toán AI in-cabin của VinAI.
- **Mobileye EyeQ5:** Chip xử lý thị giác máy tính cho camera ADAS tiêu chuẩn.
