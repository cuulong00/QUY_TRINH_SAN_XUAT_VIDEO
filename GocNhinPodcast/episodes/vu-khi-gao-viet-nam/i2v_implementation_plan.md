# Kế Hoạch Triển Khai Chi Tiết Quy Trình I2V: Vũ Khí Lúa Gạo Việt Nam

**Dự án:** `/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam`  
**Chủ đề:** *VŨ KHÍ LƯƠNG THỰC: BÁT CƠM 35K VÀ CHIẾC BẪY RỖNG RUỘT CỦA CÁC NƯỚC LÁNG GIỀNG*  
**Công nghệ sản xuất:** **Image-to-Video (I2V)** tích hợp mô hình tạo ảnh tĩnh **Nano Banana 2 (Imagen 3)** và mô hình sinh chuyển động video điện ảnh **Google Veo 3.1** (16:9, clip 8 giây chuẩn tài liệu phóng sự), điều phối tự động qua **Google Flow Batch Studio** (`tools/flow_batch_studio`).

---

## 1. Khảo Sát Hiện Trạng Dữ Liệu & Quy Mô Dự Án

Dựa trên kết quả rà soát dữ liệu tại `episodes/vu-khi-gao-viet-nam`:
- **Cấu trúc kịch bản toàn tập:** 10 chương theo mô hình tự sự sóng kép (Double-Apex Arc), tổng ngân sách từ mục tiêu ~9.000 từ (~41 phút phát thanh).
- **Tiến độ kịch bản hiện tại:**
  - **4 chương đã hoàn thành kịch bản thoại sạch:** `chapter_01.md`, `chapter_02.md`, `chapter_03.md`, `chapter_04.md` (Tổng cộng ~3.300 từ thoại).
  - **6 chương đang trong pipeline:** `chapter_05.md` đến `chapter_10.md` (~5.700 từ) đã có đầy đủ khung dàn ý chi tiết tại `07_outline.md`, `08_chapter_briefs.md` và `vault/00_Global_Vision_Synthesis.md`.
- **Ước tính khối lượng phân cảnh I2V:**
  - Tuân thủ công thức đồng bộ toán học: Thoại $\le 26$ từ/phân cảnh ($\le 7.0$ giây thoại / clip Veo 3.1 dài 8.0 giây).
  - **Giai đoạn 1 (CH01 - CH04):** ~130 – 145 phân cảnh.
  - **Toàn bộ 10 chương (CH01 - CH10):** ~360 – 400 phân cảnh.

---

## 2. User Review Required (Các Quyết Định Cần Xác Nhận)

> ⚠️ **1. Phương thức Triển khai I2V (Cuốn chiếu vs Toàn bộ):**
> - **Lựa chọn A (Khuyên dùng - Cuốn chiếu / Hybrid Staged Execution):** Triển khai ngay quy trình I2V (Scene Map -> Visual MD -> Blueprint -> Flow Prompts) cho **4 chương đã hoàn thành (CH01 đến CH04, ~140 scenes)** để nạp vào Google Flow Batch Studio render kiểm toán chất lượng trước; song song đó tiếp tục viết các chương CH05 - CH10.
> - **Lựa chọn B (Chờ toàn bộ 10 chương hoàn tất):** Hoàn thiện nốt kịch bản thoại CH05 đến CH10 trước rồi mới chạy đồng loạt I2V cho toàn bộ ~380 phân cảnh một lần.

> ⚠️ **2. Chuẩn Bản Sắc Thị Giác (Luminous High-Clarity vs Dark Charcoal):**
> Kế hoạch này áp dụng tiêu chuẩn Art Direction mới nhất của kênh:
> - **Không dùng phong cách u ám đen kịt (`#1A1A1A`, grim noir shadows)**.
> - Áp dụng ánh sáng trong trẻo (**Luminous High-Clarity Editorial Lighting**), tông màu nền **Ngà kem ấm `#FAF7EE`** (màu hạt gạo, màu trang sách báo chí) đan xen **Slate hiện đại thanh lịch (`#2A323D`, `#1E293B`)**, điểm nhấn vàng lúa chín (`#F59E0B`), cam đất (`#EA580C`) và xanh mạ non (`#10B981`).

---

## 3. Hệ Thống Nghệ Thuật & Art Direction (Visual DNA)

### A. Vũ Trụ Ẩn Dụ: 100% Không Gian Vật Lý Đời Thực (Anti-Surrealism Gate)
Tuyệt đối loại bỏ các biểu tượng siêu thực, trừu tượng hóa mơ hồ (như cái cân đĩa bay, bàn tay thép khổng lồ, hố sâu chi phí, mưa tiền, khoảng không vô cực). Mọi xung đột địa kinh tế và chính sách vĩ mô bắt buộc chuyển hóa thành hành động cơ học và bối cảnh hiện trường sống động:
1. **Cánh đồng lúa & Guồng máy sinh học:** Cánh đồng mẫu lớn ngút ngàn, máy gặt đập liên hợp cuốn bụi vàng dưới nắng sớm, sà lan chở đầy lúa rẽ sóng trên kênh xáng Chợ Gạo.
2. **Chiếc lò xo vĩ mô & Bát cơm bình dân:** Quán cơm bình dân ven khu công nghiệp, người công nhân ăn bát cơm 35K nóng hổi đối lập với phòng sạch sản xuất wafer bán dẫn và dây chuyền lắp ráp điện tử.
3. **Bi kịch bỏ rơi nông nghiệp:** Tấm biển Viện Lúa Quốc tế IRRI phủ bụi tại Los Baños, dòng người xếp hàng dài dưới nắng gắt Manila mua gạo trợ cấp, các siêu thị vét sạch kệ hàng đối lập với các tòa cao ốc BPO.
4. **Đại đối sách & Công trình thế kỷ:** Siêu cống Cái Lớn - Cái Bé đóng mở van ngăn mặn, mô hình vuông tôm - ruộng lúa luân canh, đại công trình cảng biển nước sâu Trần Đề đón tàu mẹ quốc tế.
5. **Quyền lực mềm nhân văn:** Giáo sư Võ Tòng Xuân và các chuyên gia nông nghiệp Việt Nam lội bùn hướng dẫn nông dân Cuba, Mozambique, Sierra Leone gieo cấy lúa nước.

### B. Hệ Thống 4 Mỏ Neo Thị Giác Xuyên Suốt (Central Physical Anchors)
```
[MỎ NEO 1: BÁT CƠM 35K vs PHIẾN WAFER BÁN DẪN] ──(CH01, CH02, CH10: Bệ phóng sinh tồn vs Lâu đài trên cát)
[MỎ NEO 2: GUỒNG MÁY SINH HỌC 3 VỤ & ĐOÀN SÀ LAN] ──(CH03, CH05, CH07: Cỗ máy tuần hoàn 365 ngày không nghỉ)
[MỎ NEO 3: BI KỊCH MANILA & VIỆN LÚA IRRI]       ──(CH01, CH04: Chiếc bẫy phi công nghiệp hóa rỗng ruột)
[MỎ NEO 4: ĐẠI ĐỐI SÁCH THUẬN THIÊN & NGOẠI GIAO] ──(CH07, CH08, CH09: Cống Cái Lớn, GS Võ Tòng Xuân, Hạt gạo nhân văn)
```

### C. Danh Mục Ảnh Tham Chiếu (Reference Asset Manifest `ref_images/`)
Áp dụng **Giao thức Bảo Toàn Diện Mạo Trung Tính (Zero-Bias Likeness Protocol)** — Tuyệt đối không đưa tên riêng của nhân vật vào prompt tiếng Anh nhằm tránh Celebrity Safety Filter của Google Cloud:
- `@gs_vo_tong_xuan.jpg`: Nhà khoa học nông nghiệp huyền thoại Việt Nam (mái tóc bạc, nụ cười hiền hậu, áo sơ mi cởi cúc lội ruộng).
- `@bo_truong_nong_nghiep.jpg`: Lãnh đạo ngành nông nghiệp Việt Nam (thuyết trình đề án 1 triệu ha lúa chất lượng cao).
- `@marcos_jr.jpg`: Lãnh đạo cấp cao Philippines (ký sắc lệnh EO 39 áp giá trần lúa gạo, đối thoại ngoại giao).
- `@modi_india.jpg`: Lãnh đạo cấp cao Ấn Độ (ký sắc lệnh hạn chế xuất khẩu lúa gạo tháng 7/2023).
- `@vietnamese_farmer_hero.jpg`: Chân dung người nông dân ĐBSCL thời kỳ mới (gương mặt cương nghị, làn da rám nắng, kiểm tra lúa trên tablet).
- `@vietnamese_irrigation_engineer.jpg`: Kỹ sư thủy lợi Việt Nam (mặc áo phản quang, kiểm tra vận hành cống Cái Lớn).

---

## 4. Quy Chuẩn Kỹ Thuật Đầu Vào Cho `flow_batch_studio`

Mọi tệp prompt xuất ra (`prompts_chapter_XX.txt`) phải tuân thủ nghiêm ngặt chuẩn parser của Flow Batch Studio:
1. **Cấu trúc cặp đôi:** Dòng `[IMAGE]` và dòng `[VIDEO]` của cùng một cảnh viết **LIỀN KỀ NHAU** (không có dòng trống ở giữa).
2. **Khoảng cách:** Giữa 2 phân cảnh khác nhau cách nhau đúng **1 DÒNG TRỐNG DUY NHẤT**.
3. **Quy chuẩn dòng Video:** Bắt buộc có cú pháp `@CHXX_SCYYY.png -> ... --ar 16:9 --dur 8s`.
4. **Khóa tĩnh Chữ & Typography (Selective Lower-Left 25% Rule):**
   - Chỉ 20–25% phân cảnh có text overlay (các con số mốc như "ẤN ĐỘ CẤM XUẤT KHẨU", "ĐỈNH GIÁ 650 USD", "43.4 TRIỆU TẤN LÚA", "LẠM PHÁT > 8%", "CỐNG CÁI LỚN 3.300 TỶ").
   - Chữ đặt cố định tại **góc trái dưới, cách đáy 25%**.
   - Dòng `[VIDEO]` tương ứng bắt buộc dùng cú máy `Steady camera shot` kèm lệnh: `preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations`.
5. **Ngôn ngữ:** 100% tiếng Anh không dấu (chỉ cho phép tên file tham chiếu dạng `@ten_file.jpg`).

---

## 5. Lộ Trình Triển Khai 5 Giai Đoạn (Execution Roadmap)

### 📍 Giai Đoạn 1: Chuẩn Bị Tài Nguyên & Thư Viện Tham Chiếu
- Tạo thư mục lưu trữ ảnh tham chiếu: `episodes/vu-khi-gao-viet-nam/ref_images/`.
- Thu thập và chuẩn hóa kích thước (1:1 hoặc 16:9), đổi tên file chuẩn không dấu cho các nhân vật biểu tượng.

### 📍 Giai Đoạn 2: Phân Rã Phân Cảnh Toán Học (`scene_timing_map.json`)
- Kích hoạt Persona **The Scene Architect** và Skill `scene-timing-builder`.
- Thực thi script hệ thống cố định:
  ```bash
  python3 .agents/scripts/generate_scene_map.py /Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam
  ```
- Script tự động quét các file `chapter_XX.md`, tách câu theo quy chuẩn $\le 26$ từ ($\le 7.0$s), tính toán thời lượng chính xác dựa trên WPS.
- Kiểm tra log terminal đảm bảo thông báo `✅ SUCCESS`.

### 📍 Giai Đoạn 3: Soạn Storyboard Matrix & Master Visual Blueprint
- **Tạo Kịch bản Thị giác Trung gian (`chapter_XX_visual.md`):**
  - Xây dựng ma trận 3 tầng giải phẫu vật lý cho từng cảnh (Tầng 1: Không gian cố định | Tầng 2: Chủ thể/Hành động | Tầng 3: Góc máy & Tác động).
  - Phân bổ chính xác 20-25% Text Overlay.
- **Tạo Bản thiết kế Đạo diễn Tổng thể (`visual_storyboard_blueprint.md`):**
  - Khóa cứng Color Script 60-30-10 theo từng chương.
  - Thiết kế nhịp điệu camera và các "Bạch cầu thị giác" (Inter-chapter Visual Bridges) chuyển giao mượt mà giữa các chương.
  - Khóa danh sách nhân vật và mỏ neo vật lý.

### 📍 Giai Đoạn 4: Biên Soạn Bộ Prompt Cho Flow Batch Studio
- Kích hoạt Persona **The Master Cinematic Visual Director** và Skill `visual_prompter`.
- Xuất ra các tệp:
  - `prompts_chapter_01.txt` (~30-35 scenes)
  - `prompts_chapter_02.txt` (~35-40 scenes)
  - `prompts_chapter_03.txt` (~35-40 scenes)
  - `prompts_chapter_04.txt` (~38-42 scenes)
  - *(Tiếp nối CH05 đến CH10 khi kịch bản hoàn thành)*
- **Chạy Auto-QA Gate 7 Chốt Chặn:**
  1. Cú pháp Spacing: 2 dòng liền kề trong cảnh, 1 dòng trống giữa 2 cảnh.
  2. Không gian đời thực 100%: Loại bỏ toàn bộ từ ngữ trừu tượng/siêu thực.
  3. Chuẩn nhân chủng học: Nhân vật Việt Nam/Đông Nam Á tự nhiên, không Tây hóa.
  4. An ninh chủ quyền biển đảo: Không có đường chín đoạn, hải phận quốc tế trung lập.
  5. Cú pháp tham chiếu: Dùng `@filename.ext ->` với mệnh đề trung tính, né bộ lọc tên riêng.
  6. Khóa tĩnh chữ: Text overlay đặt góc trái dưới 25%, cú máy `Steady shot` ở dòng video.
  7. Đồng bộ 1-1: Khớp mã `CHXX_SCYYY` giữa mọi tài liệu.

### 📍 Giai Đoạn 5: Thực Thi Render Trên Flow Batch Studio & Bàn Giao
- Mở ứng dụng **Google Flow Batch Studio** (`tools/flow_batch_studio`).
- Kéo thả thư mục `ref_images/` vào Reference Asset Bin.
- Nạp từng file `prompts_chapter_XX.txt`.
- Hệ thống tự động kích hoạt 6 luồng:
  - Luồng Imagen 3 / Nano Banana 2 tạo ảnh tĩnh `.png`.
  - Luồng Google Veo 3.1 nhận ảnh tham chiếu tạo video 8s `.mp4`.
- Tải về và tổ chức lưu trữ:
  - `episodes/vu-khi-gao-viet-nam/images/CHXX_SCYYY.png`
  - `episodes/vu-khi-gao-viet-nam/videos/CHXX_SCYYY.mp4`
- Cung cấp danh sách timeline khớp với Voiceover để dựng trên phần mềm dựng phim (Premiere / CapCut / DaVinci).

---

## 6. Proposed Changes & File Modifications

### Component: Visual & I2V Architecture

#### [NEW] [ref_images/](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam/ref_images)
Thư mục lưu trữ các hình ảnh chân dung/thiết bị tham chiếu cho các cảnh có gắn tag `@filename.ext`.

#### [NEW] [scene_timing_map.json](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam/scene_timing_map.json)
Bảng ánh xạ phân cảnh toán học ($\le 26$ từ/cảnh, duration $\le 7.0$s) sinh ra từ script hệ thống.

#### [NEW] [chapter_01_visual.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam/chapter_01_visual.md) đến `chapter_04_visual.md`
Ma trận phân cảnh thị giác 3 tầng chi tiết cho từng chương đã viết.

#### [NEW] [visual_storyboard_blueprint.md](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam/visual_storyboard_blueprint.md)
Bản kế hoạch chỉ đạo nghệ thuật tổng thể, quy chuẩn ánh sáng, màu sắc và danh mục tham chiếu toàn tập phim.

#### [NEW] [prompts_chapter_01.txt](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vu-khi-gao-viet-nam/prompts_chapter_01.txt) đến `prompts_chapter_04.txt`
Các tệp prompt đầu vào cho Flow Batch Studio với cú pháp chuẩn xác 100%.

---

## 7. Verification Plan

### Automated Checks
- Kiểm tra cú pháp phân cảnh qua script kiểm toán regex: Đảm bảo 100% cảnh có đủ 2 dòng `[IMAGE]` và `[VIDEO]`, không có dòng trống ở giữa, có đủ cờ `--ar 16:9 --dur 8s`.
- Kiểm tra độ dài thoại: Quét `scene_timing_map.json` xác nhận không có cảnh nào vượt quá 26 từ.
- Quét từ cấm an ninh và siêu thực: Đảm bảo không chứa từ khóa siêu thực hay vi phạm chủ quyền bản đồ.

### Manual Verification
- Nạp thử nghiệm `prompts_chapter_01.txt` vào Google Flow Batch Studio trên trình duyệt, kiểm tra khả năng parse tự động của công cụ.
- Kiểm tra trực quan 5 ảnh và video đầu tiên sinh ra từ Nano Banana 2 và Veo 3.1 để đánh giá độ nhất quán phong cách và ánh sáng sáng sủa.
