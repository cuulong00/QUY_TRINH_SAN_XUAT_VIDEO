<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/i2v_plus_implementation_plan.md
- Activated Persona: the_visual_storyteller (Master Multimodal Visual Director) + the_quality_czar
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 1)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/voiceover.md
  * episodes/san-golf-lo-co-may-ngon-dat/07_outline.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
- Execution Timestamp: 2026-09-22 16:22
-->

# KẾ HOẠCH TRIỂN KHAI I2V+ (MULTIMODAL HYBRID PIPELINE) CHO TẬP PHIM: KINH TẾ HỌC SÂN GOLF

> **Dự án:** `episodes/san-golf-lo-co-may-ngon-dat`  
> **Kênh:** Dòng Chảy — Phân tích kinh tế vĩ mô, địa chính trị, tài chính doanh nghiệp và sự hưng vong của các thể chế  
> **Quy chuẩn thực thi:** **I2V+ Multimodal Hybrid Visual Production Protocol (Phiên bản Flagship 3.0)**  
> **Tài liệu nền tảng:** 8 Chương kịch bản thoại sạch (`chapter_01.md` đến `chapter_08.md`), Master Outline Engine (`07_outline.md`), Global Vision Synthesis (`vault/00_Global_Vision_Synthesis.md`) và 10 hồ sơ chuyên sâu trong `research_vault/`.

---

## 📊 1. BÁO CÁO THẨM ĐỊNH HIỆN TRẠNG DỰ ÁN (PROJECT AUDIT)

### 1.1. Bức Tranh Chiến Lược & Luận Điểm Cốt Lõi
- **Đề tài:** *Kinh tế học sân golf: Nghịch lý thua lỗ và bàn cờ địa tô tỷ đô*.
- **Inciting Incident (Nghịch lý mở màn):** Doanh nghiệp sân golf trên sàn chứng khoán (tiêu biểu PV-Inconess) lỗ ròng triền miên 12 năm liên tiếp dù kín lịch khách, phá vỡ định kiến thông thường rằng kinh doanh sân golf là "hốt bạc".
- **Sợi chỉ đỏ (The Narrative Spine):**
  1. *Giới hạn vật lý (Chương 1):* CapEx 1.500 tỷ, OpEx 40 tỷ/năm nhưng trần công suất bị khóa cứng ở 180–220 lượt/ngày $\to$ Doanh thu trần 84 tỷ/năm không đủ bù chi phí vốn.
  2. *Mô hình B - Mỏ neo địa tô (Chương 2):* Sân golf không sinh lời từ tiền vé, mà đóng vai trò hạ tầng cảnh quan mỏ neo kích hoạt hiệu ứng Golf Premium 20%–50% cho biệt thự xung quanh, tạo thặng dư +3.600 tỷ bù trọn CapEx.
  3. *Mô hình C - Đòn bẩy tài chính (Chương 3):* Dùng mô hình định giá DCF 50 năm thổi phồng khu đất 400 tỷ thành 3.000 tỷ để vay ngân hàng 1.800 tỷ và phát hành trái phiếu riêng lẻ lãi suất 11%–12%.
  4. *The Devil's Chapter - Phản đề Mô hình A (Chương 4):* Sân golf hoàn toàn tự chủ tài chính nếu quy hoạch thành cụm du lịch quốc tế (Thái Lan thu 2 tỷ USD/năm; Vietnam Golf Coast Miền Trung 60%–75% khách quốc tế, EBITDA dương 30–70 tỷ/năm).
  5. *Đỉnh cao trào (Chương 5):* Vòng xoáy đốt 200 tỷ tiền mặt/năm nghiền nát Mô hình C; Bài học lịch sử bong bóng Nhật Bản 1989–1991 khi thẻ golf Koganei bốc hơi 95%, để lại 100 tỷ USD nợ xấu.
  6. *Bước ngoặt thể chế (Chương 6):* Luật Đất đai 2024 bỏ khung giá đất, tiền thuê đất tăng gấp 3–5 lần (15–35 tỷ/năm); Nghị định 52 cấm kèm nhà ở thương mại và cấm đất lúa 2 vụ.
  7. *Chi phí cơ hội xã hội (Chương 7):* Bàn cân giữa tiêu thụ nước (2.000–3.500 m3/ngày) vs Việc làm caddie (300–500 lao động, thu nhập 12–20 triệu); Bài học Mỹ chuyển đổi sang AI Data Center và Nhật Bản làm Mega Solar.
  8. *Grand Payoff (Chương 8):* Phá hủy sáng tạo Schumpeter: NGF 2024 người chơi Off-course (32,9M) vượt On-course; Topgolf EBITDA 30%–34% trên 5 ha; Golfzon 5.000 phòng máy; Đúc kết phân bổ nguồn lực xã hội.

---

## ⏱️ 2. KHẢO SÁT TOÁN HỌC & ĐỒNG BỘ PHÂN CẢNH (MATHEMATICAL SCENE GROUPING)

### 2.1. Ràng Buộc Kỹ Thuật Bất Biến
- **Thời lượng clip Google Veo 3.1 Lite:** Cố định **8.0 giây/clip**.
- **Tốc độ đọc voiceover tiếng Việt chuẩn của kênh:** **3.81 từ/giây**.
- **Ngưỡng an toàn phân cảnh:** **7.0 giây thoại** (tương đương 26 từ thoại), chừa ra **1.0 giây đệm hình ảnh** để dựng timeline hậu kỳ trong CapCut không bị hụt video clip.
- **Quy tắc toán học vàng:** **Mỗi phân cảnh đơn hoặc phân cảnh phụ tuyệt đối không vượt quá 26 từ thoại ($W \le 26$)**. Nếu câu nào vượt quá 26 từ, bắt buộc chia tách thành `a1, a2` và chia đều số từ.

### 2.2. Bảng Phân Bổ Số Lượng Phân Cảnh 8 Chương
Toàn bộ kịch bản gồm **4.747 từ thoại sạch**, phân bổ toán học như sau:

| Chương | Tiêu Đề Chương Kịch Bản | Dung Lượng | Số Câu Thoại | Số Cảnh Tính Toán ($K = \lceil W / 26 \rceil$) | Thời Lượng Voiceover | Vai Trò Kể Chuyện Cốt Lõi |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **CH01** | Nghịch Lý Bảng P&L Và Giới Hạn Vật Lý 200 Lượt Chơi | 533 từ | 26 câu | **26 phân cảnh** | ~2 phút 20 giây | Unit Economics; Giới hạn 200 lượt; PV-Inconess; La bàn 120s dẫn qua 3 mô hình. |
| **CH02** | Cỗ Máy Mỏ Neo Địa Tô: Tháo Ngòi Nổ Lỗ Bằng Biệt Thự | 544 từ | 27 câu | **27 phân cảnh** | ~2 phút 23 giây | Mô hình B; Địa tô David Ricardo; Quy hoạch 1/500 đại đô thị 200 ha; Golf Premium 20–50%. |
| **CH03** | Ảo Ảnh Định Giá DCF 50 Năm Và Bẫy Đòn Bẩy Trái Phiếu | 613 từ | 30 câu | **30 phân cảnh** | ~2 phút 41 giây | Mô hình C; Kỹ thuật tài chính DCF 50 năm; Thổi giá 400 tỷ lên 3.000 tỷ; Trái phiếu 11–12%. |
| **CH04** | 🛡️ **THE DEVIL'S CHAPTER: Khi Sân Golf Tự Chủ Ngoại Tệ Rực Rỡ** | 786 từ | 38 câu | **39 phân cảnh** | ~3 phút 26 giây | **MÀN 2: PHẢN ĐỀ CỐT TỬ** — Tri-Adversarial Red Team: Mô hình A; Thái Lan 2 tỷ USD; Vietnam Golf Coast Miền Trung. |
| **CH05** | ⚡ **ĐỈNH CAO TRÀO: Tử Huyệt Thanh Khoản Và Vết Xe Đổ Nhật Bản** | 630 từ | 31 câu | **31 phân cảnh** | ~2 phút 45 giây | **ĐỈNH CAO TRÀO MÀN 2 (55–65%)** — Đốt 200 tỷ tiền mặt/năm; Bong bóng Nhật Bản sụp 95%, 100 tỷ USD nợ xấu. |
| **CH06** | Bước Ngoặt Luật Đất Đai 2024: Khai Tử Đầu Cơ Đất Rẻ | 522 từ | 27 câu | **27 phân cảnh** | ~2 phút 17 giây | Luật Đất đai 2024 bỏ khung giá đất; Tiền thuê đất tăng 3–5 lần (15–35 tỷ); Nghị định 52 cấm nhà ở. |
| **CH07** | Chi Phí Cơ Hội Của Đất Nước: Nước, Việc Làm Và Sự Tái Sinh | 582 từ | 30 câu | **30 phân cảnh** | ~2 phút 33 giây | Chi phí nước vs Thu nhập caddie 12–20 triệu; Chuyển đổi công năng Data Center và Mega Solar. |
| **CH08** | Sự Phá Hủy Sáng Tạo: Off-Course Golf Và Cuộc Cách Mạng Dân Chủ Hóa | 537 từ | 27 câu | **27 phân cảnh** | ~2 phút 21 giây | Schumpeter; NGF 2024 Off-course vượt On-course; Topgolf EBITDA 30–34%; Golfzon 5.000 phòng máy. |
| **TỔNG** | **8 CHƯƠNG TOÀN TẬP** | **4.747 từ** | **236 câu** | **~237 phân cảnh** | **~20 phút 46 giây** | **Quy mô chuẩn điện ảnh tài chính Dòng Chảy** |

---

## 🎨 3. ĐỊNH HƯỚNG THỊ GIÁC & TỔ HỢP 3 ĐƯỜNG RAY

```
                       ┌─────────────────────────────────────────────────────────────┐
                       │          TẬP PHIM: KINH TẾ HỌC SÂN GOLF — ĐỊA TÔ TỶ ĐÔ      │
                       │             (Tổng quy mô: 236 câu thoại ~ 237 Cảnh)         │
                       └──────────────────────────────┬──────────────────────────────┘
                                                      │
             ┌────────────────────────────────────────┼────────────────────────────────────────┐
             │                                        │                                        │
             ▼                                        ▼                                        ▼
   ┌───────────────────┐                    ┌───────────────────┐                    ┌───────────────────┐
   │     TRACK 1:      │                    │     TRACK 2:      │                    │     TRACK 3:      │
   │      VEO_AI       │                    │    B_ROLL_REAL    │                    │  INFOGRAPHIC_DATA │
   │   (40% – 45%)     │                    │    (30% – 35%)    │                    │    (20% – 25%)    │
   │   ~106 Phân Cảnh  │                    │   ~71 Phân Cảnh   │                    │   ~60 Phân Cảnh   │
   └─────────┬─────────┘                    └─────────┬─────────┘                    └─────────┬─────────┘
             │                                        │                                        │
    ► Video Cel-Animated 2D                 ► Tư Liệu Lịch Sử & Thời Sự             ► Đồ Họa Chuyển Động Số Liệu
    ► Google Flow: Nano Banana 2            ► B-Roll Fair Use 100%                  ► Vox Motion Graphics Style
      vẽ ảnh -> Veo 3.1 tạo clip              (Tước audio, cut 3-6s,                  (Hạch toán P&L 84 tỷ,
    ► Đại cảnh fairway cồn cát,               scale 104%, dán nguồn)                  DCF 50 năm 3.000 tỷ,
      phòng thẩm định DCF, buồng              ► Cụm sân golf Thái Lan,                Nikkei bốc hơi 95%,
      lái xe golf cart, chân dung               Vietnam Golf Coast Miền Trung,          Luật Đất đai bỏ khung giá,
      Ricardo & Schumpeter diện mạo             tư liệu bong bóng Nhật Bản 1989,        cơ cấu Topgolf vs Golfzon)
      trung tính bảo toàn nhân dạng             Quốc hội thông qua Luật Đất đai
```

---

## 🛠️ 4. PIPELINE SẢN XUẤT & BỘ CÔNG CỤ THỰC THI (PRODUCTION TOOLKIT)

### 4.1. Đường Ray 1: Veo 3.1 Lite & Google Flow Tool Builder
- **Công cụ điều khiển:** Chrome Canary CDP Port 9222 qua script tự động hóa `tools/flow_batch_studio`.
- **Thư mục lưu trữ:** `episodes/san-golf-lo-co-may-ngon-dat/ref_images/` cho ảnh tham chiếu và `prompts_chapter_XX_veo.txt` cho prompt đầu vào.
- **Kỷ luật Prompt:** 
  - Gắn tag `@filename.ext ->` ở đầu dòng `[IMAGE]`.
  - Dòng `[IMAGE]` mô tả chi tiết: Bối cảnh, ánh sáng, góc máy, phục trang, nhân dạng trung tính.
  - Dòng `[VIDEO]` mô tả chuyển động camera điện ảnh: `Cinematic slow dolly forward...`, `Steady camera shot` khi có Text Overlay, và mệnh đề khóa nét mặt `maintaining their composed facial expression and all details of the reference image exactly`.

### 4.2. Đường Ray 2: FootageHunter & Fair Use B-Roll
- **Công cụ thực thi:** Script săn tư liệu tự động `FootageHunter` (`scripts/batch_hunt_i2vplus.py`).
- **Thư mục lưu trữ:** `episodes/san-golf-lo-co-may-ngon-dat/broll_manifest_chapter_XX.json`.
- **4 Nguyên Tắc Fair Use Thép:**
  1. *Tước sạch âm thanh gốc:* Chạy lệnh `-an` trên toàn bộ video tải về.
  2. *Micro-cut thời lượng ngắn:* Chỉ cắt các phân đoạn đắt giá từ 3.0 đến 6.0 giây.
  3. *Scale nhẹ & Chỉnh màu:* Phóng to 104% (`scale=1.04`) để chống quét tự động và áp filter màu kem ngà / slate đồng bộ với palette Dòng Chảy.
  4. *Dán nhãn nguồn:* Hiển thị text nhỏ gọn góc trên bên phải: `Source: [Tên nguồn báo chí / Hãng tin]`.

### 4.3. Đường Ray 3: Infographics Generator & AutoCapCut Motion Graphics
- **Công cụ thực thi:** Kịch bản đồ họa dữ liệu chuyên sâu `prompts_chapter_XX_infographics.txt` và manifest `infographics_manifest_chapter_XX.json`.
- **Thiết kế chuẩn:** Vox-Style kinetic typography, các khối thẻ tài chính (Financial Data Cards), biểu đồ so sánh hai cột (Dual-Bar), và sơ đồ cấu trúc nhiều tầng (Waterfall / Multi-Tier Diagram).

---

## 📋 5. KẾ HOẠCH TỪNG BƯỚC THỰC THI (ACTION ROADMAP)

### Bước 1: Khởi tạo mã nguồn tự động hóa sinh Kịch bản Thị giác Đa thức
- Xây dựng script Python `generate_i2vplus_san_golf.py` để duyệt toàn bộ 8 chương thoại trong `voiceover.md` (hoặc từng tệp `chapter_XX.md`), bẻ nhỏ thành các scene $\le 26$ từ, gán nhãn Modality theo ma trận Blueprint, và sinh ra cấu trúc chuẩn cho từng chương:
  - `chapter_01_visual_plus.md` đến `chapter_08_visual_plus.md`
  - `prompts_chapter_01_veo.txt` đến `prompts_chapter_08_veo.txt`
  - `broll_manifest_chapter_01.json` đến `broll_manifest_chapter_08.json`
  - `infographics_manifest_chapter_01.json` đến `infographics_manifest_chapter_08.json`

### Bước 2: Kiểm toán Toán học & Chất lượng Từng Chương
- Chạy script kiểm toán:
  - Kiểm tra số từ mỗi cảnh $\le 26$ từ (không có cảnh nào bị tràn thời lượng).
  - Kiểm tra tỷ lệ 3 đường ray: Veo AI (40–50%), B-Roll (25–35%), Infographic (20–25%).
  - Kiểm tra Zero-Bias trong prompt tiếng Anh (không rò rỉ tên riêng người thật).
  - Kiểm tra Selective Lower-Left 25% Typography & Steady Camera Shot.

### Bước 3: Đóng gói và Handoff cho các Trạm Sản Xuất Tiếp Theo
- Bàn giao `prompts_chapter_XX_veo.txt` cho `videocore_director` / Google Flow.
- Bàn giao `broll_manifest_chapter_XX.json` cho `the_footage_hunter`.
- Bàn giao `infographics_manifest_chapter_XX.json` cho `autocapcut_engineer`.
