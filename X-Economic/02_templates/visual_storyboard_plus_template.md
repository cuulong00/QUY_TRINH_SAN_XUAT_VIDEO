# Visual Storyboard Blueprint Plus — [Tên Tập Phim]

Bản thiết kế này đóng vai trò **Đạo diễn Nghệ thuật & Tổng Biên Tập Thị Giác Đa Thức (Master Multimodal Visual Director)** cho kênh **X-Economy**, xác lập ngôn ngữ thị giác toàn tập theo Hợp đồng Kiến trúc Phân cảnh theo Nhịp Ý tại `.agents/contracts/i2v_nhip_y.md`.

---

## 🌌 1. Visual Narrative Archetype & Color Arc (Vũ Trụ Thị Giác & Tuyến Màu Sắc)
*   **Vũ trụ thị giác chủ đạo:** [Historical Epic / Geopolitical Power / Industrial Dynamo / Macroeconomic Tide]
*   **Bảng màu 60-30-10 chuẩn mực:**
    *   *60% Nền Slate trầm thể chế & Tông Ngà kem ấm áp:* `#FAF7EE` (chiều sâu báo chí tài chính quốc tế) hoặc Slate thể chế `#1E293B`, `#2A323D` (hoặc Obsidian đen tuyền `#080C14` cho bối cảnh địa chính trị căng thẳng).
    *   *30% Nét vẽ & Chi tiết nhận diện:* Nét mực thanh thoát `clean bold ink outlines`, nét phẳng `stylized flat vector textures`, màu da người Việt/Châu Á `warm light-tan skin`, chi tiết gỗ ấm, kim loại xước.
    *   *10% Điểm nhấn số liệu & Kịch tính:* 
        - Tăng trưởng / Dòng tiền / Thắng lợi: Hổ phách ấm `#F59E0B`, Xanh ngọc điện ảnh Cyan `#00C2CB` hoặc `#10B981`.
        - Rủi ro / Khủng hoảng / Xung đột / Cảnh báo: Đỏ san hô `#EF5350`, Đỏ cảnh báo `#DC2626`, Cam rực `#FF7043`.
*   **Ánh sáng chuẩn:** `luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows` hoặc `soft golden daylight streaming in`.

---

## ⚖️ 2. Ma Trận Đạo Diễn Bản Thể Luận 5 Loại Shot (The 5-Shot Cognitive Matrix)

Quy định theo Hợp đồng `.agents/contracts/i2v_nhip_y.md` mục 4:

| Loại Shot (Modality) | Sứ Mệnh Nhận Thức & Trải Nghiệm Khán Giả | Tiêu Chuẩn Áp Dụng Bắt Buộc | Rào Cản Kỷ Luật (Redlines) |
|---|---|---|---|
| **`VIDEO_AI` (Video do AI tạo)** | **Linh hồn Thẩm mỹ & Hero Shots** (`Existential Awe & Poetic Gravitas`). | Tái hiện nhân vật/lãnh đạo lịch sử, bối cảnh điện ảnh, đại cảnh mở/kết chương, ẩn dụ triết học. | Sàn 4s, trần thường 10s. Khóa nét mặt trung tính, cấm biến dạng cử động, camera điện ảnh slow dolly/pan. |
| **`BROLL` (Tư liệu thực tế & Lịch sử)** | **Mỏ neo của Niềm tin & Sự thấu cảm da thịt** (`Visceral Historical Grounding`). Tạo tính bất khả phủ nhận. | Sự kiện lịch sử thật, hội nghị thượng đỉnh, phát biểu lãnh đạo, con người lao động thật, dây chuyền nhà máy & công trình thật. | Sàn 5s, trần thường 10s (chuẩn 5.5s–7.0s), cấm cắt clip dưới 5.0s. Mute 100% audio (`-an`), scale 104%, dán nhãn nguồn góc màn hình. |
| **`INFOGRAPHIC_TINH` (Đồ họa dữ liệu & Bản đồ tĩnh)** | **Kính lúp của Trí tuệ & Cú khai phóng nhận thức** (`The "Aha!" Moment`). Bóc tách cấu trúc vô hình. | Bản đồ địa chính trị, hải trình thương mại, chu kỳ nợ/dòng tiền, sơ đồ kiến trúc thể chế, đối kháng định lượng. | Sàn 4s + thời gian đọc (số chữ chia 4 chữ/giây), trần 10s. 100% biểu đồ chuẩn mực (Bar, Breakdown, Sankey, Comparison, Timeline, Map). Cấm hình khối siêu thực (bục đá, khối bay). |
| **`INFOGRAPHIC_DONG` (Sơ đồ cơ chế động)** | **Giải phẫu động lực & Cơ chế trừu tượng** (`Mechanistic Clarity`). | Sơ đồ chuyển động nhiều tầng, mạch logic, mô hình giải thích cơ chế sâu tuần tự theo nhịp đọc. | Thời lượng: hết hoạt hình + 1,5s giữ, theo nhịp. Giữ phong cách 2D vector noir, nét vẽ tinh tế đồng bộ với palette màu của tập. |
| **`BAO_CHI` (Báo chí & Hồ sơ pháp lý)** | **Bản mộc Kiểm chứng & Sự thuyết phục tuyệt đối** (`Evidentiary Rigor`). Đưa ra bằng chứng bên thứ ba không thể chối cãi. | Bài báo chính thống, hiệp ước, công báo, văn kiện lịch sử, quyết định thanh tra/xử phạt, số liệu kiểm toán độc lập. | Sàn 5s, theo nhịp (zoom dần vào đoạn nhấn). ⛔ **CẤM DÍNH BẪY ẢNH PHÓNG SỰ:** Khóa chặt tiêu cự vào CHỮ (tiêu đề/sapo), làm mờ/crop bỏ toàn bộ ảnh phóng sự. Render MP4 1080p 60fps qua Python Motion Engine kèm gạch chân/callout. |

---

## 👥 3. Bản Danh Mục Ảnh Tham Chiếu (Reference Asset Manifest)

Danh mục nhân vật, thực thể và phương tiện chủ đạo cần chuẩn bị ảnh tham chiếu trước khi bước vào sản xuất phân cảnh:

| STT | Tên Nhân Vật / Thực Thể | Vai Trò Chính Luận & Lịch Sử | Tên File Quy Ước (`@[ten_file].jpg`) | Bối Cảnh Địa Lý / Văn Hóa | Ghi Chú Tìm Ảnh (Góc mặt, trang phục, thần thái) | Trạng Thái Nạp |
|:---:|---|---|---|---|---|:---:|
| 1 | [Tên nhân vật / Thực thể] | Vai trò trong tiến trình lịch sử | `@[ten_file].jpg` | [Tọa độ địa lý / Văn hóa của câu chuyện] | Áo vest/quân phục/thường phục chuẩn thời kỳ, nhìn trực diện | `[Chờ nạp]` |
| 2 | ... | ... | ... | ... | ... | ... |

---

## 🎥 4. Directorial Flow & Pacing Rhythm (Nhịp Điệu Dựng Phim)
*   **Nguyên tắc chuyển đổi nhịp thở:**
    - Cảnh VIDEO_AI (sàn 4s, trần thường 10s): Trầm tĩnh, chiêm nghiệm, góc máy slow dolly/pan, ánh sáng điện ảnh sang trọng.
    - Cảnh BROLL thật (sàn 5s, trần thường 10s, chuẩn 5.5s–7.0s): Sắc lẹm, nhịp cắt tự nhiên, scale 104%, dán nhãn nguồn minh bạch. Cấm tiệt cắt clip dưới 5.0s.
    - Cảnh BAO_CHI (sàn 5s, theo nhịp): Tĩnh tại, zoom chậm vào dòng chữ được gạch chân sắc nét, âm thanh lướt giấy/click nhẹ.
    - Cảnh INFOGRAPHIC_TINH & INFOGRAPHIC_DONG (theo Mục 4 Hợp đồng): Dừng mắt ổn định, hiệu ứng kinetic zoom chậm để khán giả kịp thẩm thấu con số và cơ chế.
*   **Quy tắc Không Lệch Pha Thẩm Mỹ:** Toàn bộ B-roll, Báo chí và Infographic đều phải được cân chỉnh màu (Color Grading) để hòa hợp tuyệt đối với palette màu chuẩn `#FAF7EE` và `#1E293B` của kênh.
