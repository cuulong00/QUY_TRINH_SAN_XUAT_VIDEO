# BÁO CÁO KIỂM TOÁN HIỆN TRẠNG QUY TRÌNH I2V, I2V+ VÀ RENDER VIDEO (PHA 12 — PHA 14)
**Dự án:** X-Economic (Kênh: X-Economy)  
**Tác nhân kiểm toán:** Antigravity (Heavy Technical Executor)  
**Mục đích:** Cung cấp bức tranh hiện trạng trung thực 100% về quy trình, tooling, luồng dữ liệu và rào cản kỹ thuật phục vụ Claude Code đánh giá và tối ưu hóa.

---

## 1. TỔNG QUAN KIẾN TRÚC: HAI NHÁNH THỊ GIÁC SONG HÀNH

Hệ thống hiện tại trong kho lưu trữ `X-Economic` (kế thừa từ `VideoProject`) chứa **hai nhánh quy trình thị giác độc lập**, được định nghĩa qua các tệp Workflow, Skill và Persona riêng biệt:

1. **Nhánh 1 — I2V Cổ Điển (Classic I2V Pipeline — Pha 12A, 12B, 12C ➔ 14):**
   - *Triết lý:* 100% các phân cảnh đều là video AI sinh chuyển động từ ảnh minh họa 2D Cinematic Editorial Noir.
   - *Chuỗi tệp tin:* `visual_storyboard_blueprint.md` ➔ `chapter_XX_visual.md` ➔ `prompts_chapter_XX.txt` ➔ clips AI (`videos/ai_videos/`).
   - *Kỹ năng điều phối:* `.agents/skills/visual_prompter/SKILL.md` và `.agents/skills/scene_timing_builder/SKILL.md`.

2. **Nhánh 2 — I2V+ Đa Thức (Flagship Multimodal Hybrid Pipeline — Pha 12+A, 12+B, 12+C ➔ 14):**
   - *Triết lý:* Mô hình phim tài liệu điều tra báo chí quốc tế (*Bloomberg Originals, Financial Times Film, Vox*), loại bỏ sự đơn điệu của 100% AI bằng cách phối khí tương phản động 4 trụ cột nhận thức:
     - `B_ROLL_FOOTAGE` (Hiện trường thế giới vật lý thực tế).
     - `FORENSIC_CALLOUT` (Bằng chứng tài liệu, bài báo gốc, gạch chân/highlight).
     - `INFOGRAPHIC_DATA` (Điêu khắc dữ liệu, mô hình hình học, cấu trúc vĩ mô).
     - `VEO_AI` (Video điện ảnh AI cho siêu ẩn dụ, chiều sâu nội tâm và đại cảnh mở/kết).
   - *Chuỗi tệp tin:* `visual_storyboard_blueprint_plus.md` ➔ `chapter_XX_visual_plus.md` ➔ Phân hạch thành 4 manifests độc lập (`prompts_chapter_XX_veo.txt`, `broll_manifest_chapter_XX.json`, `forensic_manifest_chapter_XX.json`, `infographics_manifest_chapter_XX.json`).
   - *Kỹ năng điều phối:* `.agents/skills/visual_prompter_plus/SKILL.md` và `.agents/skills/footage-hunter/`.

---

## 2. GIẢI PHẪU CHI TIẾT TỪNG PHA THEO CÁC CÔNG CỤ & WORKFLOW THẬT

### 🎬 PHA 12A / 12+A: VISUAL STORYBOARD BLUEPRINT & MANIFESTS

* **Mục tiêu:** Định hình ngôn ngữ thị giác tổng thể của toàn bộ tập phim và lên danh mục tài nguyên cần thu thập trước khi viết kịch bản chi tiết.
* **Input:**
  - `episodes/[slug]/voiceover.md` (hoặc các file `chapter_XX.md`).
  - `episodes/[slug]/07_outline.md`.
  - Biểu mẫu: `02_templates/visual_storyboard_template.md` (bản Classic) hoặc `02_templates/visual_storyboard_plus_template.md` (bản I2V+).
* **Output:**
  - Classic: `episodes/[slug]/visual_storyboard_blueprint.md`.
  - I2V+: `episodes/[slug]/visual_storyboard_blueprint_plus.md`.
* **Tác nhân & Bản chất xử lý:**
  - **Persona:** `the_visual_storyteller` (Master Cinematic Visual Director / Master Hybrid Visual Director).
  - **Công cụ:** **100% LLM suy luận nghệ thuật**. Không có script hay thuật toán tự động nào can thiệp.
* **Nội dung tạo ra:**
  - Bảng màu 60-30-10 (`#0A0E17`, `#D4AF37`, `#00E5FF`).
  - Lộ trình phát triển hình ảnh (Visual Arc), ẩn dụ thị giác xuyên suốt.
  - **Bản danh mục thu hoạch (Harvest Manifests):**
    - *Bản Classic:* Bảng `Reference Asset Manifest` (Danh mục ảnh tham chiếu `@filename.jpg` cho lãnh đạo/nhân vật có thật để nạp vào thư mục `ref_images/`).
    - *Bản I2V+:* Bổ sung thêm 3 danh mục: `B-Roll Target Hunting Manifest`, `Forensic Media Hunting Manifest`, và `Infographic Architecture Manifest`.
* **Cổng phê duyệt (Gate):** Dừng lại in toàn văn danh mục ra chat cho User duyệt và User nạp ảnh vào `ref_images/`.

---

### ✍️ PHA 12B / 12+B: KỊCH BẢN THỊ GIÁC TRUNG GIAN (VISUAL SCRIPT)

* **Mục tiêu:** Chia nhỏ kịch bản thoại thành từng phân cảnh độc lập, kiểm soát thời lượng toán học và mô tả bối cảnh vật lý thực tế trước khi dịch sang prompt.
* **Input:**
  - `episodes/[slug]/chapter_XX.md` (chỉ nạp từng chương một để cách ly ngữ cảnh).
  - `visual_storyboard_blueprint.md` hoặc `visual_storyboard_blueprint_plus.md`.
* **Output:**
  - Classic: `episodes/[slug]/chapter_XX_visual.md`.
  - I2V+: `episodes/[slug]/chapter_XX_visual_plus.md`.
* **Tác nhân & Bản chất xử lý:**
  - **Persona:** `the_scene_architect` (Kiến Trúc Sư Phân Cảnh), phối hợp cùng `the_footage_hunter` ở bản I2V+.
  - **Kỹ năng:** `.agents/skills/scene_timing_builder/SKILL.md` hoặc `.agents/skills/visual_prompter_plus/SKILL.md`.
  - **Công cụ:** **100% LLM suy luận nghệ thuật**. (Đặc biệt lưu ý: Tệp `scene_timing_map.json` cơ học cũ đã bị phế truất, Markdown Table là nguồn sự thật duy nhất).
* **Quy chuẩn kỹ thuật cơ học:**
  - **Bẻ nhịp toán học:** Giới hạn cứng **$\le 26$ từ thoại** cho mỗi phân cảnh (tương ứng $\le 7.0$ giây thoại ở tốc độ đọc 223 từ/phút của kênh, chừa 1.0 giây hình dự phòng cho clip Veo dài 8.0 giây). Câu dài hơn 26 từ bắt buộc phải tách đôi thành `CHXX_SCYYYa`, `CHXX_SCYYYb`.
  - **Bản Classic (`chapter_XX_visual.md`):** Bảng 4 cột: `Scene ID` | `[THOẠI]` | `[BỐI CẢNH]` (giải phẫu 3 tầng: Chủ thể, Hành động vật lý, Không gian đời thực ngoài đời, tag `@ref.jpg`) | `[TEXT OVERLAY]` (chỉ xuất hiện ở 20-25% cảnh quan trọng, vị trí góc trái dưới 25%).
  - **Bản I2V+ (`chapter_XX_visual_plus.md`):** Áp dụng *Cây Quyết Định Bản Thể Học 4 Bước* để phân định rõ mỗi cảnh thuộc 1 trong 4 trụ cột (`FORENSIC_CALLOUT`, `INFOGRAPHIC_DATA`, `B_ROLL_FOOTAGE`, `VEO_AI`), kèm các trường đặc tả riêng cho từng trụ cột. Tuân thủ luật cân bằng cảm giác (không quá 2 cảnh Infographic/Forensic liên tiếp, không quá 3-4 cảnh B-roll liên tiếp).
* **Cổng phê duyệt (Intermediate Gate):** Dừng lại in toàn văn kịch bản thị giác ra chat để User duyệt chính thức trước khi chuyển sang pha viết prompt.

---

### 🎨 PHA 12C / 12+C: SOẠN THẢO PROMPTS & PHÂN HẠCH TÀI NGUYÊN (PROMPTS ENGINE)

* **Mục tiêu:** Chuyển hóa kịch bản thị giác trung gian thành các tệp chỉ thị kỹ thuật chính xác cho từng cỗ máy sản xuất.
* **Input:**
  - `chapter_XX_visual.md` hoặc `chapter_XX_visual_plus.md`.
  - **CỔNG CÁCH LY THOẠI TUYỆT ĐỐI (Zero-Voiceover Isolation Gate):** Tác nhân ở pha này **BỊ CẤM NẠP TỆP THOẠI `chapter_XX.md`**, chỉ được đọc cột `[BỐI CẢNH]` và `[TEXT OVERLAY]` của kịch bản thị giác trung gian để chống việc AI tự suy diễn tu từ hoặc hallucinate văn học.
* **Output:**
  - *Nhánh Classic:* `episodes/[slug]/prompts_chapter_XX.txt`.
  - *Nhánh I2V+:* Phân hạch song song thành 4 tệp độc lập:
    1. `prompts_chapter_XX_veo.txt` (Chỉ thị video AI).
    2. `broll_manifest_chapter_XX.json` (Danh mục săn B-roll thực tế).
    3. `forensic_manifest_chapter_XX.json` (Danh mục chụp bài báo & văn bản).
    4. `infographics_manifest_chapter_XX.json` (Danh mục số liệu cho đồ họa chuyển động).
* **Tác nhân & Bản chất xử lý:**
  - **Persona:** `the_image_prompt_composer` dưới sự giám sát của `the_visual_storyteller`.
  - **Công cụ:** **100% LLM biên dịch và chuẩn hóa cú pháp**.
* **Quy cách kỹ thuật cú pháp prompt AI (`prompts_chapter_XX.txt`):**
  - Cặp đôi liền kề: Dòng `[IMAGE]` và dòng `[VIDEO]` nằm sát nhau, cách nhau 1 dòng trống giữa các Scene.
  - Phân cảnh có ảnh tham chiếu nhân vật: Cú pháp `@<filename>.jpg -> A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, bone structure, hairstyle, and attire...`.
  - Đuôi dòng video chuẩn parser `flow_batch_studio`: `--ar 16:9 --dur 8s`.
  - Video Prompt chỉ mô tả chuyển động máy quay (Pure Optical Camera Motion: *slow push-in dolly, smooth tracking, steady shot*) và vi vật lý ánh sáng/khí quyển; cấm tả lại nhân vật để tránh méo mặt (Delta-Motion Prompting).

---

### 🎵 PHA 13: AUDIO LANDSCAPE & MUSIC COMPOSER

* **Mục tiêu:** Thiết kế cấu trúc âm thanh, nhịp điệu, điểm rơi kịch tính, khoảng lặng (drops & silences) và câu lệnh tạo nhạc nền bằng AI.
* **Input:** `voiceover.md`, `07_outline.md`, `06_retention_map.md`, `chapter_XX_visual.md`.
* **Output:** `episodes/[slug]/music_prompts.txt` và `episodes/[slug]/audio_cues.md`.
* **Tác nhân & Bản chất xử lý:**
  - **Persona:** `the_cinematic_sonic_alchemist` (Kỹ năng: `.agents/skills/music_composer/SKILL.md`).
  - **Công cụ:** **LLM suy luận nghệ thuật**.
  - **Quy tắc thi hành:** Prompt nhạc bóc tách 6 lớp (cảm xúc, pulse nhịp, texture chất liệu âm thanh, độ dày hòa âm, restraint/mở, danh sách cấm).
* **Trạng thái thực thi:** **CHỈ CHẠY THỦ CÔNG KHI CÓ YÊU CẦU CỦA USER** (theo bảng quy trình master, cấm tự động sinh nhạc hay thu âm TTS).

---

### 🖥️ PHA 14: BATCH VIDEO PRODUCTION & FINAL ASSEMBLY

* **Mục tiêu:** Sản xuất toàn bộ các tệp video clip ngắn độc lập (`.mp4`), xử lý footage B-roll và ráp nối thành video base hoàn chỉnh khớp với voiceover.
* **Input:**
  - Các tệp prompt: `prompts_chapter_XX.txt` hoặc `prompts_chapter_XX_veo.txt`.
  - Các thư mục tài nguyên: `ref_images/` (ảnh mẫu), `voiceover.wav` (file thu âm giọng đọc), `broll_manifest_*.json`, `forensic_manifest_*.json`.
* **Output:**
  - Video clips AI riêng lẻ: `episodes/[slug]/videos/ai_videos/CHXX_SCYYY.mp4`.
  - Video clips B-roll đã xử lý Fair Use: `episodes/[slug]/footages/CHXX_SCYYY.mp4`.
  - Video hoàn chỉnh cuối cùng: `episodes/[slug]/video/slideshow_base.mp4` (1080p, 30fps, H.264).
* **Các Cỗ Máy Kỹ Thuật Tham Gia Thực Thi:**
  1. **Cỗ máy 1 — Google Flow Tool Builder (Nano Banana 2 & Veo 3.1 Lite):**
     - *Điều khiển:* Python script `scripts/produce_episode_videos.py` kết nối trực tiếp vào trình duyệt Google Chrome Canary qua giao thức **Chrome CDP (DevTools Protocol) cổng 9222/9223**.
     - *Cơ chế:* Đọc file prompts, tự nạp ảnh tham chiếu `@filename.jpg`, tự điền prompt vào giao diện web Flow, kích hoạt Matrix batch render, watchdog giám sát 300s, tự động tải file `.mp4` 8 giây về máy và kiểm tra magic bytes.
  2. **Cỗ máy 2 — Cloud GPU ComfyUI MiniMax H3 (Singularity REF2VA INT8):**
     - *Điều hành:* `.agents/skills/batch_video_generator/SKILL.md` (`scripts/hoa_phat_streaming_pipeline.py`).
     - *Cơ chế:* Chạy trên NVIDIA RTX 5090 / RTX 3090 (Vast.ai / RunPod). Sử dụng mô hình MiniMax H3 nạp ảnh tĩnh từ Nano Banana 2 làm `<Picture 1>`, áp dụng Turbo LoRA 4-step (`res_multistep × simple`), tạo video chuyển động điện ảnh 2K/4K.
  3. **Cỗ máy 3 — Bộ Xử Lý Footage B-Roll Fair Use (`tools/footage_processor/process_broll.py`):**
     - *Cơ chế:* Đọc `broll_manifest_chapter_XX.json`, tải video nguồn bằng yt-dlp, sau đó gọi **FFmpeg cục bộ** thực hiện 4 biến đổi Fair Use:
       `ffmpeg -ss <start> -to <end> -i <input> -an -vf "scale=1.04*iw:-1,crop=1920:1080" -c:v libx264 -crf 20 <output>.mp4`
       (Tước bỏ 100% âm thanh `-an`, cắt micro-cut 3–5.5s, phóng to 104% bẻ pixel hash).
  4. **Cỗ máy 4 — Lắp Ráp Video Hoàn Chỉnh (Assembly & Editing):**
     - *Hiện trạng quy định trong repo (`.claude/rules/slideshow-render.md` & `render_slideshow.md`):* **Thực hiện DỰNG HẬU KỲ THỦ CÔNG TRONG CAPCUT**.
     - *Quy trình:* Người dựng (Operator) kéo toàn bộ video clips final (`videos_final/`), clips B-roll, ảnh forensic và file âm thanh voiceover vào phần mềm CapCut Desktop. Đồng bộ timeline thủ công khớp từng câu thoại, gắn nhãn nguồn góc màn hình, áp dụng transitions và xuất file `video/slideshow_base.mp4`.
     - *Công cụ dự phòng/bổ trợ:* Hệ thống có các templates AutoCapCut (`templates/capcut_modern_template/`) và script liên kết dự án AutoCapCut ngoài (`/Users/pro16/Documents/VideoProject/AutoCapCut`).

---

## 3. BẢNG MA TRẬN TỔNG HỢP CÁC BƯỚC

| Pha | Tên Bước | Tài Liệu Nạp Vào (Input) | Tệp Xuất Ra (Output) | Tác Nhân / Công Cụ Thực Thi | Bản Chất Xử Lý |
|---|---|---|---|---|---|
| **12A** | Classic Visual Blueprint | `voiceover.md`, `07_outline.md` | `visual_storyboard_blueprint.md` | `the_visual_storyteller` | **LLM suy luận nghệ thuật 100%** |
| **12+A** | Multimodal Hybrid Blueprint | `voiceover.md`, `07_outline.md`, template 12+ | `visual_storyboard_blueprint_plus.md` | `the_visual_storyteller` | **LLM suy luận nghệ thuật 100%** |
| **12B** | Classic Visual Script | `chapter_XX.md`, `visual_storyboard_blueprint.md` | `chapter_XX_visual.md` | `the_scene_architect` | **LLM bẻ nhịp $\le 26$ từ & bóc tách 3 tầng** |
| **12+B** | Multimodal Visual Script | `chapter_XX.md`, `visual_storyboard_blueprint_plus.md` | `chapter_XX_visual_plus.md` | `the_scene_architect` + `the_footage_hunter` | **LLM phân loại 4 Modality & cân bằng nhịp** |
| **12C** | Classic Prompts Engine | `chapter_XX_visual.md` (Cách ly thoại gốc) | `prompts_chapter_XX.txt` | `the_image_prompt_composer` | **LLM chuẩn hóa cú pháp Flow parser** |
| **12+C** | 4-Rail Manifest Extraction | `chapter_XX_visual_plus.md` (Cách ly thoại gốc) | `prompts_chapter_XX_veo.txt`, `broll_manifest_*.json`, `forensic_manifest_*.json`, `infographics_manifest_*.json` | `the_image_prompt_composer` + LLM extraction | **LLM trích xuất song song 4 luồng dữ liệu** |
| **13** | Audio Landscape | `voiceover.md`, `chapter_XX_visual.md` | `music_prompts.txt`, `audio_cues.md` | `the_cinematic_sonic_alchemist` | **LLM thiết kế hòa âm & điểm rơi** *(Chỉ chạy thủ công)* |
| **14-A** | AI Batch Video Render | `prompts_chapter_XX.txt`, `ref_images/` | `videos/ai_videos/*.mp4` (8s / clip) | Python script (`produce_episode_videos.py`) qua Chrome CDP:9222 ➔ Google Flow (Nano Banana 2 + Veo 3.1) HOẶC ComfyUI MiniMax H3 GPU cloud | **Script tự động hóa điều khiển Engine AI ngoài** |
| **14-B** | B-Roll Footage Processing | `broll_manifest_*.json`, YouTube URLs | `footages/*.mp4` (3–5.5s / clip) | Python script (`tools/footage_processor/process_broll.py`) gọi `yt-dlp` + `ffmpeg` | **Script tự động hóa xử lý video vật lý** |
| **14-C** | Final Video Assembly | `videos_final/*.mp4`, `footages/*.mp4`, `voiceover.wav` | `video/slideshow_base.mp4` | Người dựng (Operator) thao tác thủ công trên CapCut Desktop (hoặc AutoCapCut) | **Dựng phim hậu kỳ (Manual Stitching)** |

---

## 4. VIDEO CUỐI CÙNG ĐƯỢC RÁP TỪ NHỮNG LOẠI NGUỒN NÀO?

Trong hệ sinh thái hiện tại, một tập video hoàn chỉnh được cấu thành từ **5 loại nguồn tài nguyên thị giác**:

1. **Video AI sinh chuyển động (I2V AI Video Clips — Chiếm 40% - 60% ở nhánh I2V+ hoặc 100% ở nhánh Classic):**
   - Clip ngắn dài đúng 8.0 giây (`.mp4`), độ phân giải 720p/1080p, tỉ lệ 16:9.
   - Do Google Veo 3.1 Lite hoặc MiniMax H3 sinh chuyển động từ ảnh minh họa 2D Cinematic Editorial Noir của Nano Banana 2.
2. **Footage tư liệu B-Roll quay thật ngoài đời (Real-world Documentary Footage — Chiếm 20% - 30% ở nhánh I2V+):**
   - Clip thực tế trích xuất từ các hãng thông tấn chính thống (VTV, Bloomberg, CNBC, C-SPAN) hoặc kênh chính thức của tập đoàn (VinFast, THACO, Foxconn...).
   - Được cắt ngắn 3.0s – 5.5s, tước sạch âm thanh gốc, scale 104%, crop 1080p và dán nhãn nguồn góc màn hình.
3. **Bằng chứng báo chí thực chứng (Forensic Callouts — Chiếm 10% - 15% ở nhánh I2V+):**
   - Ảnh chụp màn hình bài báo thật từ các cơ quan báo chí có giấy phép hoặc hồ sơ kiểm toán SEC 10-K, văn bản nghị định nhà nước.
   - Cắt crop tỷ lệ 16:9, áp dụng hiệu ứng camera push-in nhẹ và vẽ highlight/gạch chân chuyển động vào các câu từ then chốt.
4. **Đồ họa dữ liệu chuyển động (Motion Infographics & Data Sculpture — Chiếm 10% - 15% ở nhánh I2V+):**
   - Biểu đồ so sánh đối kháng, sơ đồ luồng tiền tệ, bản đồ nhiệt địa chính trị.
   - Thiết kế trên nền Slate tối (`#0A0E17`), ngà kem (`#F5F0E6`), điểm nhấn Cyan (`#00E5FF`) và Amber (`#D4AF37`).
5. **Âm thanh tổng hợp (Audio Master Track):**
   - File Voiceover đọc chuẩn phát thanh Mỹ (US Documentarian Voice) không ngắt quãng.
   - Nhạc nền (BGM) đa tầng và sound effects (SFX) đặt tại các điểm rơi kịch tính theo thiết kế của Pha 13.

---

## 5. CÁC QUY TẮC RÀNG BUỘC & RÀO CẢN BẢO VỆ PHÁP LÝ / NGHỆ THUẬT HIỆN HÀNH

Toàn bộ pipeline đang bị khóa cứng bởi các văn bản luật kỹ thuật trong thư mục `.claude/rules/`, `.agents/rules/` và `00_core/`:

1. **Rào cản Cấm Code Tự Động Sinh Prompt (`visual-asset-safety.md` dòng 23):**
   > *"TUYỆT ĐỐI CẤM sử dụng code, thuật toán tự động hoặc script ghép nối từ khóa để sinh prompt tự động. Việc chuyển thể từ kịch bản sang prompt video bắt buộc phải được thực hiện bằng suy luận nghệ thuật của mô hình AI (LLM) để đảm bảo chất lượng chuyển thể hoàn hảo nhất."*
2. **Rào cản Bộ Lọc An Toàn & Người Nổi Tiếng (Celebrity & Safety Filter Defense):**
   - CẤM gọi thẳng tên người nổi tiếng, lãnh đạo quốc gia trong câu lệnh prompt video gửi sang Veo 3.1 hay MiniMax H3.
   - Bắt buộc dùng cú pháp trung tính: `the person depicted in the reference image` kết hợp thẻ tham chiếu `@filename.jpg` đứng ở ĐẦU DÒNG.
3. **Khóa Nhân Chủng Học Thép (Anthropological Fidelity Gate):**
   - TUYỆT ĐỐI CẤM để AI tự do vẽ người phương Tây (Caucasian) trong các bối cảnh đại diện cho người Việt Nam/Đông Nam Á. Prompt bắt buộc chứa khối nhận diện: `strictly preserving authentic Vietnamese demographics, straight dark hair, warm light-tan skin, natural East Asian facial features, strictly no Western features`.
4. **Cấm Tuyệt Đối Ngụy Tạo Báo Chí Bằng Code (Zero Synthetic Evidence):**
   - TUYỆT ĐỐI CẤM dùng Python Pillow, HTML canvas hay AI để tự chế bài báo giả mạo, tự đặt tít báo giả. 100% tài liệu ở trụ cột Forensic Callout phải là ảnh chụp từ URL báo chí có kiểm chứng hoặc tài liệu lưu trữ thật.
5. **Khóa Cương Vực Hải Đảo Thép:**
   - Mọi phân cảnh có bản đồ Việt Nam hoặc Biển Đông bắt buộc phải mô tả đầy đủ: Quần đảo Hoàng Sa, Trường Sa, đảo Phú Quốc, Côn Đảo dưới dạng chòm đảo vector vàng kim phát sáng; tuyệt đối cấm đường lưỡi bò phi pháp (`strictly no nine-dash line`).
6. **Bốn Bộ Lọc Chuyển Hóa Fair Use Bắt Buộc Cho B-Roll (`footage_hunting_standard.md`):**
   - Mute Absolute (`-an`): Tước bỏ 100% âm thanh gốc.
   - Micro-Cut: Chỉ cắt đoạn trích từ 3.0s đến 5.5s (dưới 6 giây).
   - Pixel Hash Breaking: Phóng to 104% và crop 16:9 1080p.
   - On-Screen Attribution: Bắt buộc dán nhãn nguồn góc màn hình.
7. **Toán Học Thời Lượng & Khóa Tĩnh Chữ:**
   - Mỗi cảnh $\le 26$ từ thoại ($\le 7.0$ giây).
   - Text overlay chỉ xuất hiện ở 20-25% cảnh then chốt, đặt tại góc trái phía dưới cách đáy 25%. Cảnh có chữ bắt buộc dòng `[VIDEO]` dùng cú máy tĩnh (`Steady camera shot`) để chống méo chữ.
8. **Action Blacklist (Veo 3.1 Lite Safeguards):**
   - Quét sạch 100% các hành động gây lỗi biến dạng mô hình video AI: Không ngón tay bấm điện thoại/đếm tiền lẻ, không va chạm cơ thể giữa 2 người, không người đi bộ trượt chân vào camera, không xe rẽ cua gấp/drift, không mở miệng nói chuyện.
