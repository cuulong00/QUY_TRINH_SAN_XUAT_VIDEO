# Kế Hoạch Triển Khai Tuyến Đồ Họa & Video I2V: VinFast Ấn Độ - Thay Đổi Chiến Lược

Tập phim: `vinfast-an-do-thay-doi-chien-luoc`  
Định dạng sản xuất: **Image-to-Video (I2V)** sử dụng mô hình tạo ảnh tĩnh **NanoBanana 2 (Imagen 3)** kết hợp mô hình sinh chuyển động video điện ảnh **Google Veo 3.1** (16:9, clip 8 giây chuẩn documentary).

---

## 📊 1. Khảo Sát & Phân Tích Hiện Trạng Dữ Liệu Thượng Nguồn

Sau khi đọc và phân tích kỹ lưỡng toàn bộ 7 chương kịch bản thoại (`chapter_01.md` đến `chapter_07.md`), file tổng hợp chiến lược vĩ mô `00_Global_Vision_Synthesis.md`, dàn ý `07_outline.md` và kiểm tra trực tiếp các tệp âm thanh gốc trong thư mục `audio/`:

| Hạng mục | Thông số thực chứng | Ý nghĩa sản xuất I2V |
| :--- | :---: | :--- |
| **Tổng số chương** | 7 chương hoàn chỉnh | Kịch bản thoại đã được kiểm duyệt nghiêm ngặt, không có rác văn bản |
| **Tổng số từ thoại** | 4.477 từ tiếng Việt | Mật độ thông tin cao, giàu thuật ngữ kinh tế - cơ khí chính xác |
| **Thời lượng audio thực tế** | **1.363,14 giây** (~22,72 phút) | Đã có sẵn 7 tệp WAV thu âm chất lượng cao từ narrator kênh |
| **Tốc độ đọc trung bình (WPS)** | **3,28 từ/giây** | Tốc độ đĩnh đạc, trầm ấm của thể loại phim tài liệu kinh tế (Cinematic Editorial Noir) |
| **Tổng số phân cảnh cần tạo** | **240 phân cảnh (scenes)** | Khớp chuẩn quy tắc toán học: Mỗi cảnh thoại $\le 26$ từ ($\le 7.0$ giây thoại, chừa 1.0 giây đệm) |
| **Mô hình sinh ảnh tĩnh** | **NanoBanana 2 / Imagen 3** | Khởi tạo hình ảnh minh họa báo chí 2D vector, render text tiếng Việt có dấu sắc nét |
| **Mô hình sinh video** | **Google Veo 3.1 (I2V Mode)** | Nhận ảnh tham chiếu `@CHXX_SCYYY.png`, sinh chuyển động camera điện ảnh 8 giây mượt mà |

### Phân bổ 240 phân cảnh theo từng chương:
- **Chương 01 (Phát súng tháng 7/2026 & Quả bom nội bộ):** 40 phân cảnh (Audio: 198,46s | 702 từ)
- **Chương 02 (Bài toán 25.000 xe & Khấu hao khuôn dập):** 34 phân cảnh (Audio: 249,26s | 637 từ)
- **Chương 03 (Hải trình 3.000 hải lý & Chiếc bẫy thể chế SMEC):** 35 phân cảnh (Audio: 184,16s | 683 từ)
- **Chương 04 (Cú đâm sầm của VF 3 & Tử địa giá bán lẻ):** 33 phân cảnh (Audio: 179,82s | 629 từ)
- **Chương 05 (Bàn cờ 2 bánh Tamil Nadu & Nước cờ 840 triệu USD):** 38 phân cảnh (Audio: 178,12s | 731 từ)
- **Chương 06 (Bài học 40 năm Maruti Suzuki & May đo bản địa):** 34 phân cảnh (Audio: 181,90s | 614 từ)
- **Chương 07 (Bước lùi để cắm rễ & Khúc dạo đầu kẻ sinh tồn):** 26 phân cảnh (Audio: 191,42s | 483 từ)

---

## 🎨 2. Định Hướng Nghệ Thuật & Bản Sắc Thị Giác (Visual DNA)

### A. Vũ Trụ Ẩn Dụ: Cinematic Editorial Noir (Industrial Investigative)
- **Phong cách thị giác chủ đạo:** Đồ họa minh họa báo chí 2D phẳng cao cấp (`A 2D cinematic editorial noir illustration, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dramatic chiaroscuro lighting, deep noir shadows`).
- **Triệt tiêu 100% siêu thực phi vật lý (Anti-Surrealism Gate):** Tuyệt đối không có hình ảnh ma thuật hay phi lý (như bàn tay thép khổng lồ trên trời, người khổng lồ giẫm nát nhà máy, hay cơn mưa tiền). Mọi ẩn dụ kinh tế vĩ mô bắt buộc phải chuyển hóa thành **hành động và không gian vật lý thực tế**:
  * Dây chuyền dập khuôn CNC tia lửa cam rực sáng.
  * Container trên tàu biển vượt sóng Ấn Độ Dương.
  * Phòng họp đàm phán hợp đồng căng thẳng với bản vẽ kỹ thuật trải rộng.
  * Đồng hồ áp suất thể chế SMEC và các ngăn kéo hồ sơ bảo lãnh ngân hàng.
  * Bãi lắp ráp xe máy điện Tamil Nadu ngập tràn ánh nắng và các đợt ngập lụt mùa mưa gió mùa Nam Á.

### B. Hệ Thống 4 Mỏ Neo Thị Giác Xuyên Suốt (Central Visual Anchors)
1. **Mỏ neo A: Khối Khuôn Dập Thép Khổng Lồ (The Massive Automotive Die Tooling Block):**
   * *Mô tả:* Khối kim loại chrome/thép xám nguyên khối đồ sộ, bề mặt chạm khắc chính xác đường cong thân vỏ VF 6/VF 7, xung quanh là máy ép thủy lực và tia lửa cam neon (`neon orange sparks`). Đại diện cho gánh nặng chi phí cố định (CAPEX) và bài toán 25.000 xe.
   * *Tiến hóa:* Xuất hiện rực lửa ở CH01, bị khóa xích tính toán chi phí ở CH02, và được thay thế bằng bàn vẽ may đo linh hoạt ở CH06.
2. **Mỏ neo B: Tàu Biển Chở Container CKD & Hải Trình 3.000 Hải Lý (The Maritime CKD Freight Vessel):**
   * *Mô tả:* Con tàu container sừng sững trên nền biển xanh thẫm (`deep indigo`), chở các thùng hàng container màu xanh ngọc và xám bạc có nhãn Cát Hải - Thoothukudi. Đại diện cho chiếc khiên phòng thủ chi phí và dòng máu logistics kết nối Việt Nam - Ấn Độ.
   * *Tiến hóa:* Rẽ sóng tiến vào cảng Tuticorin ở CH01, CH03; đối chiếu với đường sá nội địa Ấn Độ ách tắc ở CH03.
3. **Mỏ neo C: Khối Pin Mô-đun & Khung Xe 2 Bánh (The Modular Battery Pack & E-Scooter Tube Frame):**
   * *Mô tả:* Cụm pin lăng trụ phát sáng xanh ngọc (`glowing electric green pack`), bộ điều khiển điện tử công suất đồng bộ, được lắp ghép linh hoạt từ ô tô sang khung xe máy điện ống hàn đơn giản. Đại diện cho nước cờ đòn bẩy quy mô 1 triệu xe gánh DVA.
   * *Tiến hóa:* Xuất hiện như điểm nghẽn thiếu hụt ở CH03 ➔ trở thành vị cứu tinh công nghiệp tràn ngập xưởng Tamil Nadu ở CH05.
4. **Mỏ neo D: Thước Đo Thể Chế SMEC & Hợp Đồng Bảo Lãnh Ngân Hàng (The SMEC Gauge & Bank Guarantee Vault):**
   * *Mô tả:* Đồng hồ đo áp suất thể chế bằng đồng thau với hai lằn ranh đỏ khắc nghiệt: 25% (năm thứ 3) và 50% (năm thứ 5), bên cạnh là phong bì bảo lãnh ngân hàng có dấu niêm phong đỏ.
   * *Tiến hóa:* Chiếc thòng lọng đe dọa ở CH01, CH03 ➔ kim chỉ số nhảy vọt vượt qua 50% ở CH05 nhờ sản lượng xe máy điện.

### C. Bảng Nhân Vật Cố Định (Visual Cast Sheet)
Để đảm bảo AI sinh ảnh giữ nguyên diện mạo, trang phục và phong thái qua các phân cảnh:
- **Nhân vật 1: Kỹ Sư Trưởng VinFast (Vietnamese Lead Automotive Engineer):**
  * *Prompt cố định:* `[A Vietnamese male automotive engineer in his late 30s, sharp determined eyes, short clean black hair, wearing a clean dark navy blue factory technical uniform with subtle high-vis orange trim and clear safety goggles, focused analytical posture]`
  * *Xuất hiện:* CH01, CH03, CH04, CH06.
- **Nhân vật 2: Chủ Xưởng Cơ Khí Phụ Trợ Ấn Độ (Indian Precision Tooling Industrialist):**
  * *Prompt cố định:* `[A South Asian Indian male industrialist in his early 50s, greying mustache, wearing a crisp formal light-grey collared work shirt, holding digital calipers or inspecting metal tooling die, thoughtful calculating expression]`
  * *Xuất hiện:* CH01, CH02, CH06.
- **Nhân vật 3: Quan Chức Quản Lý Thể Chế Ấn Độ (Indian Policy Regulator):**
  * *Prompt cố định:* `[A distinguished Indian male senior regulator in his late 40s, neatly combed black hair, wearing a dark charcoal formal Nehru jacket with mandarin collar, standing in a sleek government conference room with institutional policy binders]`
  * *Xuất hiện:* CH01, CH03, CH05.

### D. Tuyến Màu Sắc 60-30-10 & Tâm Lý Cảm Xúc Qua 7 Chương
| Chương | Tông màu nền (60%) | Màu nét vẽ & Chủ thể (30%) | Màu nhấn ẩn dụ (10%) | Sắc thái cảm xúc kịch bản |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `dark warm charcoal` | `warm cream outlines & silhouettes` | `glowing terracotta orange` | Bất ngờ, căng thẳng điều tra |
| **02** | `deep industrial slate grey` | `light silver grey & chrome` | `glowing crimson coral red` | Khắc nghiệt, bế tắc toán học khuôn dập |
| **03** | `deep ocean indigo` | `cool steel grey & white mist` | `glowing neon amber` | Nguy cơ thể chế, thòng lọng SMEC |
| **04** | `dark charcoal grey` | `matte black vehicle silhouettes` | `warning crimson red` | Tử địa giá xe nhỏ, cú đâm sầm của VF 3 |
| **05** | `muted dark olive green` | `clean ivory outlines & copper` | `glowing electric turquoise green` | Bừng sáng, giải phóng quy mô xe 2 bánh |
| **06** | `warm charcoal noir` | `warm brass & terracotta` | `bright electric green` | Điềm tĩnh, bài học Suzuki, may đo bản địa |
| **07** | `deep minimalist charcoal` | `solid architectural silhouettes` | `glowing warm gold & turquoise` | Trưởng thành công nghiệp, khúc dạo đầu sinh tồn |

---

## 🛠️ 3. Kế Hoạch Triển Khai Chi Tiết (5 Bước Cốt Lõi)

### Bước 1: Chuẩn Hóa Bảng Phân Cảnh (`scene_timing_map.json`)
- Đã chạy thành công script chuẩn hóa toán học `generate_scene_map.py`.
- Tiếp theo, kích hoạt Persona **The Scene Architect**: Đọc từng phân cảnh trong số 240 scenes, phân tích ngữ nghĩa các câu thoại trong mảng `"sentences"`, và viết lại trường `"visual_summary"` thành các ẩn dụ thị giác đồ họa 2D giàu chuyển động và hàm ý, đồng bộ tuyệt đối với trục thời gian audio thực tế.

### Bước 2: Xây Dựng Kịch Bản Thị Giác Tổng Thể (`visual_storyboard_blueprint.md`)
- Soạn thảo bản blueprint theo đúng cấu trúc chuẩn của Art Director:
  * Khóa cứng Narrative Archetype, Central Visual Anchors, Cast Sheet, Color Arc.
  * Thiết kế lộ trình camera (`slow push-in`, `subtle tracking shot`, `steady shot`).
  * Thiết kế 6 bạch cầu chuyển tiếp thị giác mượt mà giữa các chương (Inter-chapter Visual Bridges: CH01 ➔ CH02 ➔ CH03 ➔ CH04 ➔ CH05 ➔ CH06 ➔ CH07) nhằm loại bỏ hoàn toàn hiện tượng nhảy cảnh đột ngột (jump cut).
  * Lập bảng quy hoạch toàn bộ 240 phân cảnh theo chuẩn luồng I2V.

### Bước 3: Tạo Bộ Prompt I2V Tách Biệt Cho Từng Chương (Phase 12.5)
Áp dụng nguyên tắc **Chunking Gate** (chống tràn context và chống suy giảm chú ý LLM), chia thành 7 tệp riêng biệt:
- `prompts_chapter_01.txt` (40 phân cảnh)
- `prompts_chapter_02.txt` (34 phân cảnh)
- `prompts_chapter_03.txt` (35 phân cảnh)
- `prompts_chapter_04.txt` (33 phân cảnh)
- `prompts_chapter_05.txt` (38 phân cảnh)
- `prompts_chapter_06.txt` (34 phân cảnh)
- `prompts_chapter_07.txt` (26 phân cảnh)

Mỗi phân cảnh tuân thủ cú pháp chuẩn 2 dòng I2V:
```text
CH01_SC001 [IMAGE]: A 2D cinematic editorial noir illustration of a giant crushing mechanical press in a shadowy automobile factory, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark warm charcoal background (#1A1A1A), dramatic chiaroscuro lighting, glowing terracotta orange highlights (#FF7043) on heavy steel machinery parts.
CH01_SC001 [VIDEO]: @CH01_SC001.png -> Slow dramatic push-in shot toward the heavy mechanical press, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9
```

### Bước 4: Kiểm Toán Chất Lượng Tự Động (Auto-QA Gate)
Trước khi bàn giao, chạy kiểm toán trên toàn bộ 240 phân cảnh qua 5 chốt chặn:
1. **Chống Tây hóa nhân vật:** 100% nhân vật đều có chỉ định danh tính rõ ràng (`Vietnamese engineer`, `Indian industrialist`, `Indian regulator`).
2. **Chống siêu thực phi lý:** 100% bối cảnh neo vào không gian cơ khí / thể chế thực tế.
3. **Quy tắc chọn lọc Text Overlay (20-25%):** Chỉ xuất hiện ở các con số bước ngoặt (như "THUẾ 70% - 100%", "500 TRIỆU USD", "25.000 XE/NĂM", "SMEC 50% DVA", "1 TRIỆU XE MÁY ĐIỆN"). Các cảnh có chữ bắt buộc dùng cú máy `Steady camera shot` để chống méo font.
4. **An ninh chủ quyền:** 100% bản đồ là mạng lưới điểm nút số hóa trừu tượng (`abstract cyber nodes`), tuyệt đối không vẽ biên giới địa chính trị hay đường phân định biển.
5. **Đồng bộ 1-1 ID:** Toàn bộ ID từ `CH01_SC001` đến `CH07_SC240` khớp nhau tuyệt đối giữa `scene_timing_map.json`, `visual_storyboard_blueprint.md` và các file prompts.

### Bước 5: Kế Hoạch Sản Xuất Đồ Họa & Dựng Video (Production Handoff)
- Tạo thư mục lưu trữ ảnh tham chiếu: `episodes/vinfast-an-do-thay-doi-chien-luoc/images/`.
- Sẵn sàng script tự động hoặc batch prompt cho công cụ sinh ảnh NanoBanana 2 và công cụ video Veo 3.1.

---

## 🎯 4. Sản Phẩm Bàn Giao Cụ Thể (Deliverables)

1. `scene_timing_map.json`: Bảng phân cảnh 240 scenes đã được làm giàu `visual_summary` bởi The Scene Architect.
2. `visual_storyboard_blueprint.md`: Kịch bản chỉ đạo nghệ thuật tổng thể toàn tập phim.
3. `prompts_chapter_01.txt` đến `prompts_chapter_07.txt`: 7 tệp prompt I2V hoàn chỉnh, sẵn sàng nạp vào công cụ render.
4. Báo cáo đối soát chất lượng Auto-QA xác nhận không có bất kỳ lỗi lặp từ hay vi phạm quy chuẩn.
