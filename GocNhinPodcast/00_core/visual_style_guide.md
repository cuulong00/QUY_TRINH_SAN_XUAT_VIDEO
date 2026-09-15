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

## 🎨 CANONICAL VISUAL DNA: SANG TRỌNG – TRẦM – ẤM – UY TÍN CAO – GẦN GŨI
*(Sophisticated, Grounded, Warm, Authoritative, Approachable)*

> 🛑 **NGUYÊN TẮC BẤT BIẾN (PERMANENT SYSTEM DIRECTIVE):**
> Toàn bộ ngôn ngữ thị giác, hình ảnh minh họa và video của kênh Góc Nhìn Podcast BẮT BUỘC phải quán triệt 5 giá trị thẩm mỹ cốt lõi, áp dụng vĩnh viễn trên toàn hệ thống mà không cần nhắc lại:
> 1. **SANG TRỌNG (Sophisticated & Prestigious):** Tinh thần đồ họa báo chí điện ảnh cao cấp (đẳng cấp tương tự Financial Times, Bloomberg Originals, Monocle, The Economist). Nét vẽ mực thanh tao (`clean refined ink outlines`), chất liệu mờ mịn tinh tế (`matte textures`), bố cục cân đối chuẩn mực điện ảnh 16:9, tuyệt đối cấm phong cách hoạt hình trẻ con hay màu mè lòe loẹt.
> 2. **TRẦM (Grounded & Deep Muted Tones):** Tông màu sâu lắng, độ bão hòa được kiểm soát chặt chẽ (`controlled muted saturation`), dải màu nền slate trầm sang trọng (`#1E293B`, `#252D37`), than ấm sâu (`warm deep charcoal #212529`), không dùng màu neon chói gắt hay màu nguyên bản sặc sỡ.
> 3. **ẤM (Warm & Amber Glow):** Không gian bao trùm bởi ánh sáng ấm áp, giàu sinh khí: Ánh sáng hổ phách dịu (`soft ambient amber glow`), nắng vàng dịu (`soft golden hour daylight`), tông ngà kem ấm cổ điển (`rich warm ivory cream #F5F0E6`), ánh đồng xước (`burnished bronze`), chi tiết gỗ ấm (`warm teakwood/mahogany`). Triệt tiêu hoàn toàn cảm giác lạnh lẽo, xám xịt hoặc xanh tái vô hồn.
> 4. **UY TÍN CAO (Authoritative & Institutional Rigor):** Không gian bối cảnh mang sức nặng học thuật và thể chế: Bàn họp gỗ tự nhiên, bản đồ quy hoạch in sắc nét, phòng lab kiểm định chuẩn xác, nhà xưởng công nghiệp quy chuẩn quốc tế, tài liệu in mộc đỏ trang trọng. Ánh sáng chiếu rọi rõ nét (`luminous high-clarity institutional lighting`), độ nét quang học cao, bố cục đối xứng hoặc 1/3 đĩnh đạc.
> 5. **GẦN GŨI (Approachable & Human-Centric):** Con người là trái tim của khung hình. Kỹ sư, người thợ, nhà hoạch định chính sách đều xuất hiện với diện mạo chân thực, nét mặt điềm tĩnh, ấm áp, ánh mắt tập trung và trách nhiệm. Góc máy ngang tầm mắt (Eye-level shot) hoặc trung cận (Medium shot), tạo cảm giác người xem đang cùng đứng trong không gian đó, đồng hành và quan sát một cách chân thực, không xa cách tượng đài.

### 1. Bảng Màu Thương Hiệu (The 60-30-10 Palette)
- **60% Màu Nền & Không Gian Chủ Đạo (Grounded & Warm Base):**
  * *Tông Ngà Kem Ấm Sang Trọng:* `rich warm ivory cream (#F5F0E6 / #FAF7EE)` — mang chiều sâu của những trang sách và tài liệu nghiên cứu kinh tế quốc tế.
  * *Tông Slate Trầm Uy Tín:* `deep institutional slate (#1E293B / #252D37)` — biểu trưng cho sự vững chãi, kỹ thuật công nghiệp và thể chế vĩ mô.
- **30% Cấu Trúc & Nét Vẽ Chủ Thể (Refined Craftsmanship):**
  * Nét mực tinh tế: `clean refined ink outlines`, chất liệu vector phẳng mờ `stylized matte vector textures`.
  * Khối màu vật liệu tự nhiên: Nâu đồng `burnished bronze (#8D6E63)`, gỗ tếch ấm `warm teakwood (#5D4037)`.
  * Nhân chủng học Việt Nam chân thực: da sáng ấm tự nhiên (`warm light-tan skin, authentic Southeast Asian heritage`).
- **10% Màu Nhấn Dữ Liệu & Hơi Thở Cuộc Sống (Warm & Prestigious Accents):**
  * *Điểm nhấn chủ đạo (Warmth):* Hổ phách rực ấm (`warm amber glow #D97706`), vàng kim mờ sang trọng (`muted champagne gold #D4AF37`).
  * *Điểm sáng thể chế & chính sách:* Ngọc lam trầm uy tín (`muted deep teal #0D5C75`).
  * *Cảnh báo & rủi ro chi phí:* Đỏ đất nung trầm (`muted terracotta red #C0392B`).

### 2. Tiêu Chuẩn Ánh Sáng (Luminous Institutional Lighting)
- Luôn sử dụng: `luminous high-clarity institutional lighting, soft ambient amber glow, crisp clean contours, delicate warm shadows` hoặc `soft golden daylight streaming in`.
- Tuyệt đối CẤM phong cách u ám đen kịt (`chiaroscuro noir, pitch-black #1A1A1A, grim horror shadows`) gây cảm giác tang tóc hay ảnh thờ.

### 3. Câu Lệnh Phong Cách Bắt Buộc (Mandatory Style Prompt Anchor)
Mọi prompt ảnh tĩnh `[IMAGE]` đều bắt buộc tích hợp mệnh đề chuẩn:
> `sophisticated 2D cinematic editorial illustration, warm muted color palette, luxurious deep slate and rich warm ivory cream tones (#F5F0E6, #1E293B), soft ambient amber glow, burnished bronze accents, clean refined ink outlines, luminous high-clarity institutional lighting, grounded human-centric warmth, dignified and authoritative atmosphere, approachable documentary aesthetic, 16:9`


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
