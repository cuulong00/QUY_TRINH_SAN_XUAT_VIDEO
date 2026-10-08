# QUY CHUẨN ĐẠO DIỄN THỊ GIÁC & KỸ THUẬT SĂN B-ROLL THỰC CHỨNG (BẢN CỤC BỘ KÊNH X-ECONOMY)
## Master Directives for Real-world B-Roll Production (X-Economy 3-Pillar Edition)

> **Tài liệu chuẩn hóa thị giác CỤC BỘ của kênh X-Economy.**  
> Áp dụng bắt buộc cho toàn bộ các tập phim của kênh **X-Economy**, kỹ năng `visual_prompter_plus`, `the_footage_hunter` và quy trình dựng phim X-Economic.  
> *(Tuân thủ bản dùng chung VPOS Standard V7.0 tại thư mục gốc).*

---

## 🏛️ I. NGUYÊN LÝ CỐT LÕI: TƯ DUY ĐIỆN ẢNH VÀ NGỮ CẢNH THỊ GIÁC
*(Cinematic Context & Atmosphere over Word-for-Word Matching)*

### 1. Phá Vỡ "Bẫy Dịch Thô Kịch Bản" (The Literal Translation Trap)
Sai lầm nghiêm trọng nhất trong sản xuất tư liệu tự động là cố gắng **dịch sát nghĩa từng từ của kịch bản thành từ khóa tìm kiếm trên YouTube**:
- **Thực tế sai lầm đã phát hiện qua Audit:**
  - Kịch bản viết: *"Hệ thống điều độ SCADA vận hành lưới điện"* $\rightarrow$ Agent đi tìm: `"SCADA điều độ lưới điện"` $\rightarrow$ **0 kết quả YouTube!**
  - Kịch bản viết: *"Đóng bó thanh khoản ngân hàng"* $\rightarrow$ Agent đi tìm: `"đóng bó thanh khoản"` $\rightarrow$ **Bị loãng kết quả, không ra phóng sự chính thống!**
  - Kịch bản viết: *"Lãi suất tăng vọt 50%"* $\rightarrow$ Agent đi tìm: `"50 percent tăng vọt"` $\rightarrow$ **Rơi vào video giải toán!**
  - Thuật ngữ góc máy: Nhét `"close up"`, `"gần cảnh"` $\rightarrow$ **Bị lệch vào video dạy quay phim!**
  - Kịch bản viết: *"Kỹ sư trưởng chỉ huy san lấp"* $\rightarrow$ Agent đi tìm: `"xe lu máy ủi san gạt đất"` $\rightarrow$ **Rơi vào video quảng cáo xe cơ giới!**
- **Nguyên lý điện ảnh tài liệu:** **HÌNH VÀ TIẾNG KHÔNG BAO GIỜ PHẢI BẰNG NHAU CHẰN CHẶN TỪNG TỪ.**
  - Khi phân tích kinh tế - vĩ mô, khán giả **không cần nhìn thấy đúng hành động người đó vừa đọc**, mà cần **thấy đúng không khí, đúng bối cảnh, đúng quy mô và đẳng cấp của chủ thể** (Visual Context & Cinematic Metaphor).

### 2. Tách Bạch Tuyệt Đối `visual_intent` và `search_query`
Trong toàn bộ manifest (`broll_manifest_chapter_XX.json`), hệ thống phân định cứng:
- **`visual_intent`:** Mô tả chi tiết ý đồ nghệ thuật, hành động, không khí (chỉ phục vụ audit và hiểu ý đồ, **CẤM TUYỆT ĐỐI dùng làm query tìm kiếm**).
- **`search_query`:** CHỈ chứa công thức tối giản:  
  $$\text{Search Query} = [\text{Chủ thể Vĩ mô / Sự kiện}] + [\text{Từ khóa Bối cảnh chuẩn}] + [\text{Nguồn Tier 1}]$$  
  *(Từ khóa bối cảnh BẮT BUỘC chọn từ từ điển [`00_core/context_tier_vocabulary.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/context_tier_vocabulary.md)).*

---

## 🎨 II. MA TRẬN 7 CỤM BỐI CẢNH ĐIỆN ẢNH VĨ MÔ (CONTEXT ARCHETYPES)

Toàn bộ các phân cảnh B-roll của X-Economy bắt buộc quy hoạch về 7 cụm bối cảnh chuẩn hóa:

| Cụm Bối Cảnh | Phạm vi Tự sự | Bối cảnh Hình ảnh Cần Thấy | Search Query Chuẩn Khuyến Nghị |
| :--- | :--- | :--- | :--- |
| **1. MACRO_FINANCE** | Tài chính, Ngân hàng, Cơ quan Điều hành | Hội trường họp chính sách, bảng điện tử, kho bạc, ký kết văn bản | `"Cục Dự trữ Liên bang Mỹ họp lãi suất Bloomberg"`, `"Ngân hàng Nhà nước họp điều hành VTV24"` |
| **2. INDUSTRIAL_HEAVY** | Công nghiệp nặng, Luyện kim, Chế tạo | Lò cao rực lửa, cuộn thép cán nóng, robot lắp ráp | `"Hòa Phát Dung Quất nhà máy thép cán nóng VTV24"`, `"dây chuyền ô tô hiện đại VTV1"` |
| **3. INFRASTRUCTURE** | Đại công trường, Cao tốc, Cầu cảng | Đại công trường, flycam cầu cạn, thi công hầm | `"đại công trường cao tốc Bắc Nam VTV1"`, `"tiến độ thi công hầm Đèo Cả VNEWS"` |
| **4. RAILWAY_TRANSPORT** | Đường sắt tốc độ cao, Tuyến ray | Tuyến ray đôi, tàu cao tốc lướt qua cảnh quan, ga hiện đại | `"shinkansen bullet train 4K"`, `"tàu hỏa Bắc Nam đèo Hải Vân 4K"` |
| **5. MARITIME_LOGISTICS** | Cảng biển nước sâu, Chuỗi cung ứng | Cần cẩu giàn khổng lồ, tàu container cập cảng | `"cảng Cái Mép Thị Vải tàu container VTV1"`, `"cảng biển Hải Phòng bốc dỡ hàng hóa VTV24"` |
| **6. URBAN_MARKET** | Bất động sản, Đô thị, Nhà ở xã hội | Đại đô thị flycam, khu nhà ở khang trang, phố thị tấp nập | `"khu đô thị mới flycam 4K"`, `"dự án nhà ở xã hội VTV1"` |
| **7. HIGH_TECH** | Bán dẫn, Vi mạch, Phòng sạch | Kỹ sư áo phòng sạch, cánh tay robot gắp wafer, vi mạch | `"nhà máy bán dẫn vi mạch phòng sạch VTV24"`, `"semiconductor cleanroom fabrication 4K"` |

---

## 🔍 III. NGUYÊN TẮC HÌNH THÀNH TRUY VẤN YOUTUBE (QUERY SYNTHESIS ENGINE)

1. **Bộ Lọc Nguồn Động 3 Tầng (3-Tier Dynamic Source Architecture):**
   - **Tầng 1 (Chính thống Quốc gia):** VTV1, VTV24, VNEWS Thông tấn xã, Kênh YouTube chính chủ tập đoàn (Hòa Phát, THACO, Vingroup, Viettel...).
   - **Tầng 2 (Báo chí Chuyên ngành Hạng A):** Báo Lao Động, Báo Tuổi Trẻ, Báo Thanh Niên, VnExpress, Đài PT-TH địa phương (Đà Nẵng, Quảng Ninh...).
   - **Tầng 3 (Quốc tế Uy tín):** Bloomberg Originals, Reuters, Financial Times, CNBC, AP.
2. **Danh Sách Đen Cấm Tiệt (Strict Exclusion Filters):**
   - **Kênh cấm:** Chứa từ `"hài"`, `"phim"`, `"tiểu phẩm"`, `"reup"`, `"review"`, `"sách nói"`, `"audiobook"`, `"kể chuyện"`, `"karaoke"`, `"nhạc"`, `"truyện"`, `"parody"`, `"độc đáo tv"`.
   - **Tiêu đề cấm:** Án mạng, đâm chết, giết người, tai nạn, điện giật, ngộ độc, cháy nổ, sạt lở, lừa đảo, đánh ghen, giang hồ, bắt giữ, khởi tố, tạm giam, xét xử, tòa án, hoa hậu, showbiz, bạo lực.

---

## 💎 IV. KHÓA ĐỘ PHÂN GIẢI THÉP & CHẤT LƯỢNG RENDER (RESOLUTION AXIOMS)

1. **Cấm Tuyệt Đối Bộ Lọc `[ext=mp4]`:** Phải dùng format selector: `bestvideo[height>=1080]/bestvideo+bestaudio/best`.
2. **Tiêu Chuẩn Render FFmpeg Chuẩn Điện Ảnh:**
   - CRF 15, Bitrate 8000k, Lanczos scaling 1080p 24fps, Mute 100% audio (`-an`).
   - Áp LUT màu Slate trầm ấm (`Warm Slate Tone`, `#1E293B` 10%).

---

## 🎬 V. QUY TRÌNH BÓC TÁCH FOOTAGE HIỆN TRƯỜNG & LOẠI BỎ MC PHÒNG THU

1. **Quy Tắc Vùng Chết (The 0–8s Dead Zone):** CẤM TIỆT cắt clip trong khoảng từ $0s \rightarrow 8s$ (MC ngồi đọc tin).
2. **Quy Tắc Voice-Alignment:** Khớp phụ đề WebVTT, cắt tại mốc $T_{\text{voice}} + 1.0s$.
3. **Quy Tắc Sweet Spot (15s–35s):** Nếu không có phụ đề, cắt trong khoảng 15.0s–35.0s (góc máy hiện trường đắt giá nhất).

---

## 🛡️ VI. BỘ LỌC KIỂM TOÁN TRỰC QUAN & CỔNG CHẶN BẮT BUỘC (VISUAL AUDIT GATE)

1. **Cổng Kiểm Toán Lưới Ảnh Bắt Buộc (Mandatory Contact Sheet Audit Gate):**
   - Sau khi tải toàn bộ clip ứng viên của một chương, hệ thống tự động chạy `core/audit_matrix.py` để ghép thành 1 ảnh lưới tiếp xúc (`audit_contact_sheet_CHXX.jpg`).
   - LLM/Auditor chấm một lượt duy nhất cho toàn bộ các ô:
     - `FIT`: Đúng bối cảnh, đúng quy mô, màu sắc điện ảnh, sạch sẽ.
     - `BORDERLINE`: Hơi lệch hướng nhìn nhưng chấp nhận được nếu thiếu tư liệu.
     - `REJECT`: Sai bối cảnh (đồ chơi, máy cơ giới nhỏ lẻ, mặt MC phòng thu, phóng sự rẻ tiền).
   - **RÀO CẢN BẤT DI BẤT DỊCH:** CẤM TUYỆT ĐỐI đưa clip vào timeline dựng (`videos_final/`) nếu chưa vượt qua Contact Sheet Audit Gate.
2. **Kỷ Luật Tách Biệt Kho Lưu Trữ X-Economy:**
   - **Footage B-roll thực tế (1080p Full HD):** Lưu trữ tại `videos/` và `footages/`.
   - **Ảnh tĩnh Infographic AI (Nano Banana 2):** Lưu tại `images/infographics/`.
   - **Forensic Callout MP4:** Lưu tại `videos/forensic/`.
3. **Cơ Chế Circuit Breaker (X-Economy 3-Pillar):**
   - Nếu tìm kiếm 4 ứng viên uy tín đều không đạt bối cảnh mong muốn: Chuyển sang **The Forensic Callout** (chụp bài báo thực tế) hoặc **Static AI Infographic** (Data Sculpture).
   - **TUYỆT ĐỐI KHÔNG FALLBACK VÀO VIDEO AI TẠO HÌNH NGƯỜI (VEO_AI ĐÃ BỊ LOẠI BỎ KHỎI PIPELINE CỦA X-ECONOMY).**
