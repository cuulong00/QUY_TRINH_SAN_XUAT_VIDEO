# Sổ Tay Mỏ Neo Thị Giác Kỹ Thuật & Kiến Trúc (Visual Engineering & Architecture Bible)
*Tài liệu nguồn sự thật trực quan (Visual Source of Truth) phục vụ cho Pha 12: Phân tách kịch bản Visual Storyboard Matrix và Tạo Prompt I2V (NanoBanana 2 & Veo 3.1).*

---

## 🎨 1. NGUYÊN TẮC THẨM MỸ TOÀN CỤC & QUY TRÌNH CHUYỂN HÓA CƠ HỌC (GLOBAL STYLE & MECHANICAL TRANSLATION)
- **Triết lý "Quy Trình Đồng Nhất Khép Kín" (Unified End-to-End Pipeline):**
  * Kịch bản gốc (`chapter_XX.md`) $\rightarrow$ Kịch bản Visual Trung gian (`chapter_XX_visual.md`) $\rightarrow$ Tệp Prompts I2V (`prompts_chapter_XX.txt`) là **MỘT THỂ THỐNG NHẤT BẮT BUỘC**.
  * Bản chất kịch bản gốc mang ngôn ngữ phân tích vĩ mô và phát thanh. Kịch bản trung gian đóng vai trò **Bộ dịch thuật cơ học (Mechanical Translator)**: Bắt buộc phải chuyển hóa câu từ vĩ mô thành **mô tả giải phẫu vật lý 3 tầng dễ hiểu, rõ ràng, chính xác**, để khi viết prompt AI có thể dễ dàng nắm bắt chính xác cần vẽ gì và chuyển động ra sao.
- **Quy Tắc Mô Hình Giải Phẫu Cơ Học 3 Tầng (3-Tier Mechanical Anatomy - BẮT BUỘC):**
  * Đối với mọi phân cảnh mô tả công nghệ, công trình, máy móc, trường `[BỐI CẢNH]` bắt buộc bóc tách rõ:
    1. *Tầng 1 - Đế Cố Định (Anchor/Base):* Khán đài bê tông, móng ngầm, mặt đất công trường, xưởng cơ khí.
    2. *Tầng 2 - Bộ Truyền Động / Cơ Chế Chủ Lực (Actuators & Mechanisms):* Tháp nâng thủy lực Strand Jacking màu vàng, ray cơ khí trượt tự động, đầu dò siêu âm NDT, chip cảm biến nhiệt điện tử.
    3. *Tầng 3 - Khối Tác Động & Hướng Lực (Payload & Motion Vector):* Mái vòm thép đang được nâng, khay cỏ lặn xuống hầm ngầm, mũi tên động lực học.
- **Quy Tắc Nhãn Chú Thích Kỹ Thuật Đích Danh (Engineering Technical Callouts):**
  * Ở các cảnh giải mã công nghệ, bắt buộc khai báo các nhãn chú thích tiếng Việt 3D trực diện ở `[TEXT OVERLAY]` và prompt `[IMAGE]` (ví dụ: `"THÁP NÂNG THỦY LỰC"`, `"MÁI VÒM THÉP 40.000 TẤN"`, `"CÁP KÉO ĐỒNG BỘ"`). Ở dòng `[VIDEO]`, luôn khóa tĩnh lớp nhãn để tránh lỗi font chữ.
- **Phong cách mỹ thuật:** **Cinematic Editorial Noir** (Đồ họa Báo chí Điện ảnh bán thực tế, sắc sảo, tối giản, sang trọng). Tránh tuyệt đối phong cách hoạt hình (cartoon) hoặc 3D game thô cứng.
- **Bảng màu 60-30-10:**
  * **60% Nền/Bóng tối:** `Dark warm charcoal (#1A1A1A)` và `Deep industrial slate (#1E2522)`.
  * **30% Chủ thể/Kết cấu:** Màu thép titan công nghiệp, bê tông xám thanh lịch, nét vẽ viền kem ấm `warm cream (#FFFDF0)`.
  * **10% Điểm nhấn dẫn mắt:** Màu cam đồng rực rỡ `glowing terracotta orange (#FF7043)` của họa tiết Trống đồng và màu xanh ngọc công nghệ `glowing turquoise (#26A69A)` của luồng dữ liệu AI/LED/Tàu cao tốc.
- **Quy chuẩn Ống kính & Ánh sáng:** `Shot on 35mm anamorphic lens`, `shallow depth of field`, `cinematic chiaroscuro lighting` (tương phản sáng tối sâu), góc quay đại cảnh hùng vĩ (`Low-angle wide shot`, `Epic aerial wide shot`).
- **Quy tắc Dàn Nhân Vật & Bảo Tồn Diện Mạo (Cast Sheet & Context Consistency - BẮT BUỘC):**
  * Trong mọi bối cảnh tại Việt Nam (công trường VinCons, nhà máy Đại Dũng, VinMetal, phòng điều khiển BIM/AI), nhân vật xuất hiện **BẮT BUỘC là người Việt Nam và ƯU TIÊN nhân vật nam**:
    - *Kỹ sư trưởng:* `a focused Vietnamese male chief engineer in a high-visibility orange-and-slate reflective safety vest and white hard hat`.
    - *Đội ngũ kỹ sư kết cấu:* `a team of Vietnamese male structural engineers and BIM specialists in protective hard hats`.
    - *Đội ngũ công nhân thi công:* `Vietnamese male construction workers in standardized VinCons safety uniforms`.
  * Không đưa tên người thật/thương hiệu vào prompt video để tránh bộ lọc bảo mật (dùng: *the Vietnamese male chief engineer in safety vest*, *a team of Vietnamese structural engineers*).
  * Mọi chuyển động camera I2V phải mượt mà (`slow cinematic push-in dolly shot`, `sweeping aerial orbit`, `smooth vertical crane tilt-down`).


---

## 🏛️ 2. MÔ HÌNH VẬT LÝ & THÔNG SỐ KIẾN TRÚC TOÀN CẢNH (GLOBAL ARCHITECTURAL SPECS)

| Thực Thể / Hạng Mục | Quy Chuẩn Hình Ảnh Chi Tiết Cho Prompt Image (NanoBanana 2) | Cơ Chế Chuyển Động Vật Lý Cho Prompt Video (Veo 3.1) |
| :--- | :--- | :--- |
| **1. Đại Lộ 120m & Siêu Đầu Mối Ga Ngọc Hồi** | Góc nhìn flycam từ trên cao: Trục đại lộ khổng lồ 120 mét rực sáng ánh đèn đêm dẫn thẳng vào Ga Ngọc Hồi hiện đại; các đoàn tàu cao tốc khí động học lướt đi trên đường ray đa tầng. | Cú máy flycam bay lướt dọc theo trục đại lộ 120m (forward aerial tracking shot), các luồng xe điện và tàu cao tốc chuyển động êm ái. |
| **2. Bản Hồ Sơ Năng Lực Sống Của Người Việt** | Nhóm kỹ sư và tổng thầu Việt Nam trong trang phục bảo hộ hiện đại đứng trên đỉnh khán đài lộng gió, ngắm nhìn công trình vòm thép Trống Đồng 120m vươn cao kiêu hãnh dưới ánh bình minh. | Cú máy quay chậm từ phía sau lưng các kỹ sư ngước lên vòm thép (slow low-angle push-in), ánh sáng mặt trời vàng óng chiếu rọi qua các dầm thép. |
| **3. Tàu Cao Tốc VinSpeed 350 km/h & Vịnh Hạ Long** | Cảnh phân đôi điện ảnh: Một bên là đoàn tàu cao tốc trắng bạc VinSpeed lao đi với vận tốc 350 km/h, một bên là khung cảnh hoàng hôn thanh bình trên Vịnh Hạ Long với các du thuyền 5 sao. | Cú máy lướt mượt mà nối hai khung cảnh, thể hiện tốc độ và sự tiện nghi của hành lang kinh tế thể thao - di sản. |
| **4. Cảm Biến Nhiệt Bê Tông & Móng Ngầm** | Cắt cảnh mặt cắt lòng đất (cross-section): Cụm đài móng bê tông khổng lồ đang đông kết; hàng ngàn cảm biến nhiệt điện tử phát sáng xanh lá cây truyền sóng dữ liệu nhiệt độ không dây lên màn hình trung tâm. | Cú máy hạ chậm vào lòng đất (slow crane tilt-down), các xung sóng dữ liệu nhiệt từ cảm biến lan tỏa nhịp nhàng trong khối bê tông. |
| **5. Bản Sao Số BIM 4D/5D (Digital Twin)** | Kỹ sư trưởng đứng trước màn hình Hologram 3D phát sáng hiển thị mô phỏng từng dầm thép và xung đột không gian theo thời gian thực; các luồng dữ liệu tiến độ và chi phí chạy dọc theo khung vòm. | Cú máy quay chậm 180 độ quanh mô hình Hologram 3D (slow orbit shot), các phân đoạn dầm thép ảo tự động khớp nối nhịp nhàng. |
| **6. Nhà Máy Cơ Khí CNC Đại Dũng & Siêu Âm NDT** | Bên trong xưởng chế tạo rộng hàng chục hecta: Cánh tay robot cắt thép CNC phát ra chùm tia plasma xanh; kỹ sư dùng đầu dò sóng siêu âm NDT quét kiểm tra từng milimét mối hàn thép sáng bóng. | Cú máy tracking cận cảnh (macro tracking shot) theo vệt quét sóng siêu âm phát sáng trên đường hàn thép hoàn hảo. |
| **7. Kích Nâng Thủy Lực Strand Jacking (Cốt 0)** | Hệ mái vòm 40.000 tấn được tổ hợp hoàn thiện ở mặt đất (cốt 0); cụm kích thủy lực Strand Jacking siêu tải trọng kết nối các bó cáp thép cường độ cao bắt đầu kích nâng khối thép lên trời. | Cú máy time-lapse từ mặt đất: Hệ kích thủy lực từ từ nâng toàn bộ khối thép vòm đồ sộ lên cao độ 120 mét một cách vững chắc tuyệt đối. |
| **8. Khán Đài 135k Ghế & Màn Hình LED 360 Độ** | Khung cảnh lòng chảo với chiếc **màn hình LED 360 độ vô cực hình elip khổng lồ** treo lơ lửng giữa không trung; phát sáng rực rỡ các pha bóng tua lại độ phân giải 8K và biểu đồ nhiệt AI. | Cú máy góc thấp từ sân cỏ ngước lên (low-angle tilt-up), màn hình LED 360 độ quay chậm các pha bóng sắc nét trong không gian hoành tráng. |

---

## 🎬 3. DANH BẠ MỎ NEO TRỰC QUAN THEO TỪNG CHƯƠNG (CHAPTER VISUAL ANCHORS)

### 📌 CHƯƠNG 1: Nghịch Lý Thời Gian Của Kỷ Lục Hành Tinh
* **Mỏ neo 1.1 (Cú va chạm thời gian thế giới):** SoFi 46 tháng, Tottenham 48 tháng, Tổ Chim 56 tháng vs VinFast 19 tháng.
* **Mỏ neo 1.2 (Sức nặng 40.000 tấn thép):** Hình bóng 4 Tháp Eiffel / 10.000 voi đặt cạnh vòm thép.
* **Mỏ neo 1.3 (Hồ sơ World Cup của Đại Dũng):** Kỹ sư Việt Nam kiểm tra mối hàn thép tại Sân Lusail Qatar.

### 📌 CHƯƠNG 2: Quy Mô Kỷ Lục & Kiến Trúc Siêu Công Nghệ
* **Mỏ neo 2.1 (Góc nhìn Trống Đồng từ bầu trời):** Top-down aerial view Trống Đồng 408m trong quần thể Hùng Vương 400ha.
* **Mỏ neo 2.2 (Khẩu độ mái vòm >350m xô đổ kỷ lục Singapore):** Vòm thép vươn qua độ cao 120m, trượt đóng mở <30 phút.
* **Mỏ neo 2.3 (Cổng soát vé Face-ID 3s & Màn hình LED 360 độ):** Khán giả bước qua cổng nhận diện sinh trắc học và chiêm ngưỡng màn hình vô cực 8K lơ lửng giữa lòng chảo.
* **Mỏ neo 2.4 (Làm mát vi khí hậu dưới chân 135k ghế 5G):** Họng gió làm mát mini dưới chân ghế và màn hình smartphone tua lại 4K.
* **Mỏ neo 2.5 (Hầm ươm cỏ ngầm đối chiếu Mỹ Đình & Âm học phòng thu):** Khay cỏ lặn xuống hầm ngầm LED tím hồng; tấm tiêu âm nano gầm mái triệt dội âm cho concert.
* **Mỏ neo 2.6 (Mái pin BIPV & Quần thể Olympic 400ha):** Mái quang điện BIPV tự sản xuất điện sạch và đại cảnh Khu liên hợp Hùng Vương.

### 📌 CHƯƠNG 3: Kỷ Luật Thép & Bí Mật Đảm Bảo Chất Lượng 100%
* **Mỏ neo 3.1 (Hồ sơ quốc tế Đại Dũng World Cup Qatar & Mỹ):** Sân Lusail Qatar và xưởng chế tạo xuất khẩu thép đi 50 quốc gia.
* **Mỏ neo 3.2 (Bản sao số BIM 4D/5D Digital Twin):** Màn hình mô phỏng 3D triệt tiêu xung đột không gian dầm thép và ống dẫn MEP.
* **Mỏ neo 3.3 (Gia công CNC & Siêu âm mối hàn NDT 100%):** Máy cắt CNC plasma độ chính xác 2mm và kỹ sư quét đầu dò siêu âm tại nhà máy Đại Dũng.
* **Mỏ neo 3.4 (Kích nâng Strand Jacking ở mặt đất cốt 0):** Cụm kích thủy lực máy tính kéo khối vòm thép 40.000 tấn từ mặt đất lên đỉnh 120m.
* **Mỏ neo 3.5 (Đại công trường đêm 3 ca 4 kíp & Thợ tinh hoa VinCons):** Công trường rực rỡ ánh sáng đèn cao áp 24/7 và hình ảnh những người thợ Việt Nam làm việc kỷ luật, tự tin.

### 📌 CHƯƠNG 4: Đánh Đổi Tốc Độ & Bức Tranh Tự Chủ Công Nghiệp Thép
* **Mỏ neo 4.1 (Cảm biến nhiệt bê tông đài móng ngầm):** Màn hình hiển thị biểu đồ nhiệt thủy hóa 24/7 ngăn nứt nhiệt bê tông khối lớn.
* **Mỏ neo 4.2 (Thép tấm cường độ cao Eurocode 3 nhập khẩu cảng biển):** Cuộn thép tấm dày chịu lực uốn cực hạn tại cảng biển quốc tế.
* **Mỏ neo 4.3 (Tổ hợp luyện cán thép Hòa Phát / VinMetal):** Phác thảo nhà máy luyện kim công nghệ cao tự chủ thép ray đường sắt tốc độ cao 350 km/h.

### 📌 CHƯƠNG 5: Canh Bạc Tiếp Thị Quyền Lực & Cỗ Máy Khai Thác Kinh Tế Toàn Cầu
* **Mỏ neo 5.1 (Hiệu ứng Swiftonomics & Mega-Concert):** 135.000 khán giả cuồng nhiệt dưới ánh đèn laser đại nhạc hội quốc tế.
* **Mỏ neo 5.2 (Siêu tàu cao tốc VinSpeed 350 km/h nối Vịnh Hạ Long):** Tàu cao tốc VinSpeed đưa du khách từ sân vận động về các resort 5 sao bên vịnh di sản trong 20 phút.
* **Mỏ neo 5.3 (Tuyến Metro số 2 & Bãi đáp trực thăng Helipad):** Khách quốc tế đi thẳng từ Sân bay Nội Bài về sân; trực thăng đón tiếp quan chức FIFA.

### 📌 CHƯƠNG 6: Bản Tuyên Ngôn Công Nghiệp & Kỷ Nguyên Vươn Mình
* **Mỏ neo 6.1 (Đại lộ 120m & Đô thị 9.171ha & Ga Ngọc Hồi):** Toàn cảnh trục đại lộ 120m rực rỡ ánh đèn nối thẳng Ga Ngọc Hồi và đại đô thị thể thao.
* **Mỏ neo 6.2 (Bản hồ sơ năng lực sống & Tự hào Việt Nam):** Kỹ sư Việt Nam đứng hiên ngang trước siêu công trình hoàn thiện, biểu tượng cho năng lực làm chủ đường sắt cao tốc 67 tỷ USD và xuất khẩu hạ tầng thế giới.
