# Visual Style Guide — Kênh GocNhinPodcast (I2V Reference Asset Protocol & S-Grade Cinematic Video)

> **Kênh:** GocNhinPodcast — Phân tích xã hội, kinh tế vĩ mô và chính sách chuyên sâu dành cho người Việt hiện đại
> **Phiên bản:** 3.0 — Cập nhật Tháng 9/2026 (I2V Reference Asset Protocol & Luminous Cinematic Art)
> **Áp dụng cho:** Tất cả các phân cảnh video (Video Generation Prompts) trong video long-form.

---

## 🛠️ QUY TRÌNH TẠO MEDIA (Bắt buộc tuân thủ)

### Bước 1: Phân tích Cảnh & Đồng bộ Toán học (Mathematical Scene Grouping)
*   **Không áp dụng bất kỳ quy tắc tự do cơ học nào.** Phân nhóm cảnh bắt buộc phải tuân thủ chặt chẽ trục thời gian và số lượng từ thoại.
*   **Giao thức Đồng bộ Toán học cho Veo 3.1:** Thời lượng video clip cố định là **8.0 giây**. Tốc độ đọc voiceover tiếng Việt trung bình của kênh là **3.81 từ/giây**. Với ngưỡng thời lượng an toàn cho mỗi cảnh là **7.0 giây** (chừa lại 1.0 giây hình dự phòng hậu kỳ), mỗi phân cảnh đơn hoặc phân cảnh phụ tuyệt đối **không được chứa quá 26 từ thoại**.
*   **Quy tắc phân cảnh phụ (Sub-scenes):** Nếu cụm câu thoại cùng ngữ cảnh có số từ $W$ lớn hơn 26 từ, bắt buộc phải chia nhỏ thành $K = \lceil W / 26 \rceil$ phân cảnh phụ (`a1`, `a2`, `a3`...) và phân bổ đều số từ thoại sang các cảnh phụ đó. Nghiêm cấm để các phân cảnh phụ có thoại rỗng `[]` khi cảnh trước bị quá tải từ (>26 từ).

### Bước 2: Thiết kế Kịch bản Thị giác & Danh mục Ảnh tham chiếu (Phase 12)
*   Lập `visual_storyboard_blueprint.md` theo mẫu chuẩn, xác định rõ: Mỏ neo thị giác, Tuyến camera, Hệ màu và **Bảng Danh Mục Ảnh Tham Chiếu (Reference Asset Manifest)**.
*   **Tuyển vai Biểu tượng (Iconic Casting Mandate):** Ưu tiên số 1 là con người (nguyên thủ quốc gia, lãnh đạo chính phủ, bộ trưởng, CEO tập đoàn, nhà sáng lập). Việc đưa nhân vật biểu tượng có thật vào đúng phân cảnh mang lại sức nặng chính luận, sự uy tín và tính thuyết phục tuyệt đối. (Các công trình, địa danh nổi tiếng đã có sẵn trong dữ liệu huấn luyện của Nano Banana 2 nên không bắt buộc cần ảnh tham chiếu).
*   **Human-in-the-loop Gate:** Dừng lại hiển thị Manifest để Người dùng tải ảnh vào `episodes/[slug]/ref_images/` theo chuẩn tên file `@filename.ext` và nạp vào Asset Bin của `flow_batch_studio`.

### Bước 3: Tạo Prompts Cuốn Chiếu Từng Chương (Phase 12.5 - Rolling Chapter Prompts)
*   Mỗi chương được xuất ra tệp `prompts_chapter_XX.txt` theo đúng cú pháp cặp đôi `[IMAGE]` và `[VIDEO]` cho công cụ `tools/flow_batch_studio/`.
*   Cùng một phân cảnh: Dòng `[IMAGE]` và dòng `[VIDEO]` viết liền kề (không dòng trống). Giữa các phân cảnh cách nhau đúng 1 dòng trống. Cuối dòng `[VIDEO]` có `--ar 16:9 --dur 8s`.

### Bước 4: Dựng và Ghép Video Thủ Công (Manual Editing & Stitching)
*   Sau khi các clip `.mp4` được sinh ra từ Veo 3.1, lưu chúng vào thư mục `videos_final/`.
*   **Dựng hậu kỳ:** Người dựng nhập thủ công các video clip vào CapCut/Premiere/DaVinci, căn chỉnh khớp hoàn hảo với nhịp điệu của file voiceover đã thu âm.
*   Xuất video base hoàn chỉnh ở định dạng 1080p, 30fps, codec H.264, tỷ lệ 16:9 và lưu vào đường dẫn `video/slideshow_base.mp4`.

---

## 🎨 HỆ MÀU THƯƠNG HIỆU & ÁNH SÁNG SÁNG SỦA (Luminous Editorial DNA)

Tuyệt đối cấm sử dụng các dải màu cầu vồng tự do hoặc cụm từ "vibrant color palette" thiếu định hướng. Đồng thời **TUYỆT ĐỐI CẤM phong cách u ám, tối tăm (No Pitch-Black / Grim Shadows)** như nền đen `#1A1A1A` hay `deep noir chiaroscuro shadows`.

### 1. Bảng Màu Nền & Chủ Đạo (60%)
- **Tông Ngà Kem Ấm Áp (Warm Ivory Cream - Ưu tiên hàng đầu cho chiều sâu báo chí):** `warm ivory cream ambient tone (#FAF7EE)`, tạo cảm giác trang nhã, học thuật, như trang tạp chí phân tích kinh tế quốc tế cao cấp.
- **Tông Slate Hiện Đại (Modern Slate):** `#2A323D`, `#2C3539`, `#1E293B` mang lại cảm giác công nghệ cao, vững chãi và chuyên nghiệp.

### 2. Nét Vẽ & Chủ Thể (30%)
- Nét vẽ mực thanh thoát, dứt khoát: `clean bold ink outlines`, `stylized flat vector textures`.
- Khối nhận diện nhân chủng học Đông Nam Á / Việt Nam rõ ràng, da sáng ấm tự nhiên (`warm light-tan skin`).

### 3. Màu Nhấn Dữ Liệu & Điểm Mấu Chốt (10%)
- *Xã hội / Đời sống / Con người:* `terracotta orange` (`#FF7043`) hoặc hổ phách ấm (`#F59E0B`).
- *Chính sách / Chiến lược / Điểm sáng:* `turquoise` (`#26A69A`) hoặc `sage green` (`#81C784`).
- *Cảnh báo / Khủng hoảng / Xung đột:* `crimson coral red` (`#EF5350`).

### 4. Ánh Sáng Sáng Sủa, Trong Trẻo (Luminous High-Clarity Lighting)
- Luôn sử dụng: `luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows` hoặc `soft golden daylight streaming in`.
- Tránh xa các hiệu ứng tối tăm, mờ mịt gây cảm giác u buồn hay ghê rợn.

---

## 🧠 TƯ DUY ẨN DỤ XÃ HỘI & 100% HIỆN THỰC VẬT LÝ

Tuyệt đối cấm các hình ảnh siêu thực, trừu tượng không có thật ngoài đời (cái cân bay, bàn tay thép, hố sâu chi phí, quả cầu trong hư vô, con đường phân đôi giữa bão). Mọi khái niệm kinh tế - xã hội phải được thể hiện qua **hành động vật lý và bối cảnh đời thực**:
- **Chính sách vĩ mô:** Lãnh đạo và chuyên gia họp bàn quanh bản đồ quy hoạch in giấy thật trên bàn gỗ, tài liệu pháp lý trang trọng.
- **Dòng chảy kinh tế / Logistics:** Cảng biển Hải Phòng tấp nập, cần cẩu container bốc dỡ hàng, đoàn tàu chở hàng lăn bánh trong sương sớm.
- **Áp lực cơ cấu / Thị trường:** Kỹ sư trong phòng điều hành nhà máy theo dõi dữ liệu trên màn hình bảng điều khiển thực tế.

---

## ✍️ QUY CHUẨN ĐỊNH VỊ CHỮ TRÊN MÀN HÌNH (Selective Lower-Left 25% Rule)

*   **Tỷ lệ chọn lọc:** Chỉ xuất hiện ở 20% - 25% phân cảnh then chốt (số liệu đột phá, mốc thời gian, đạo luật). 75% - 80% còn lại KHÔNG chèn chữ để giữ khung hình thoáng đãng.
*   **Vị trí & Kích thước:** Thiết kế chữ nhỏ gọn, thanh thoát (`compact subtle`), đặt cố định tại **góc dưới bên trái cách đáy 25%** (`positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge`).
*   **Ngôn ngữ hiển thị:** 
    *   Chuyển sang Tiếng Anh hoặc Tiếng Việt không dấu (ví dụ: `"DATA POINT"`, `"POLICY 2026"`, `"VIETNAM EV"`).
    *   Mô tả chữ: `compact subtle glowing turquoise 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "[TEXT]"`.
*   **Khóa tĩnh chữ trong Video:** Khi cảnh có chữ, dòng `[VIDEO]` bắt buộc dùng cú máy tĩnh `Steady camera shot` để khóa chết vị trí chữ không bị biến dạng.

---

## 🔒 QUY TẮC AN TOÀN AI & CƠ CHẾ BẢO TOÀN DIỆN MẠO TRUNG TÍNH (Zero-Bias Safety Formula)

> ⚠️ **NGUYÊN LÝ SỐNG CÒN:**
> Các mô hình AI Video lớn (Google Veo 3.1, Nano Banana 2) tích hợp bộ lọc bản quyền và nhân vật công chúng cực kỳ nghiêm ngặt. Việc gõ tên thật của nhân vật còn sống hoặc chính khách (như "To Lam", "Elon Musk", "Wang Chuanfu") trực tiếp vào câu lệnh tiếng Anh sẽ khiến hệ thống trả về lỗi **"Safety Policy Violation"** và hủy bỏ tác vụ.

### Giải pháp Chuẩn Hóa của Kênh GocNhinPodcast:
1.  **Chỉ đặt tên trên file tham chiếu:** Đặt tên nhân vật vào file ảnh tham chiếu (ví dụ `@lanhdao_tolam.jpg`, `@ceo_byd_wangchuanfu.jpg`).
2.  **Sử dụng mệnh đề trung tính tuyệt đối trong prompt:**
    `@filename.ext -> A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The subject is [Action & Setting]...`
3.  **Khóa nét mặt ở dòng Video:** Dòng `[VIDEO]` sử dụng câu lệnh `maintaining their composed facial expression and all details of the reference image exactly`.
4.  **Trang phục nghiêm túc, rộng rãi (Loose-fitting attire):** Luôn chỉ định trang phục phù hợp hoàn cảnh, lịch sự, rộng rãi (`a loose-fitting business suit`, `loose working clothes`, `flowing traditional robes`). Tuyệt đối cấm trang phục bó sát hay hở hang.

---

## 🛡️ DANH SÁCH ĐIỀU CẤM KỶ LUẬT (Hard Redlines)
1.  **CẤM TÊN NGƯỜI THẬT TRONG MÔ TẢ PROMPT:** Chỉ dùng tag `@filename.ext ->` và mệnh đề `"the person depicted in the reference image"`.
2.  **CẤM ĐƯỜNG LƯỠI BÒ & BẢN ĐỒ VI PHẠM CHỦ QUYỀN:** 100% cảnh có bản đồ Biển Đông/Đông Nam Á bắt buộc chèn: `clean neutral open ocean, strictly no nine-dash line, strictly no dotted maritime border lines in South China Sea, Vietnamese territorial integrity respected`.
3.  **CẤM PHONG CÁCH U ÁM / ẢNH THỜ:** Cấm chụp chân dung đơn độc trên nền tối mịt trông giống ảnh thờ. Luôn cho nhân vật hoạt động trong bối cảnh sống động, ánh sáng trong trẻo.
4.  **CẤM ẨN DỤ SIÊU THỰC & PHI VẬT LÝ:** Cấm cân bay, bàn tay thép, lò rèn cổ lỗ trong nhà máy công nghệ cao.
5.  **CẤM VIẾT SAI ĐỊNH DẠNG PARSER:** Giữ đúng quy cách cặp dòng liền kề `[IMAGE]` và `[VIDEO]`, cách 1 dòng giữa các cảnh, đuôi `--ar 16:9 --dur 8s`.

---

## LỊCH SỬ PHONG CÁCH

| Ngày | Thay đổi |
|---|---|
| 24/04/2026 | Chốt phong cách Hoạt hình 2D Hiện đại làm DNA chính thức. |
| 18/06/2026 | Nâng cấp lên S-Grade Video Generation (Cel-Animated), hệ màu 60-30-10. |
| 06/09/2026 | Nâng cấp lên **Phiên bản 3.0: I2V Reference Asset Protocol**, tích hợp ảnh tham chiếu biểu tượng, công thức diện mạo trung tính (Zero-Bias Safety), bảng màu kem ngà sáng sủa `#FAF7EE` và chuẩn parser `flow_batch_studio`. |
