---
description: Tuyến Chuyển Hóa Kịch Bản Độc Quyền Tự Động (Single URL to 100% Transformative Script & Production Package) — Tham khảo link video, bóc tách hạt nhân khoa học, nghiên cứu sâu qua NotebookLM (Zero Hallucination), tái cấu trúc 100% cốt truyện kịch tính theo DNA Hiểu Biết Hơn (The Infographics Show), đồng bộ toán học Veo 3.1 8s (<= 26 từ/cảnh), sinh Storyboard, Thumbnail AI và SEO Metadata hoàn chỉnh.
---

# 🚀 Slash Command: `/remix_to_script [URL]`
### Giao Thức Chuyển Hóa Video Tham Khảo Thành Kịch Bản Độc Quyền Hoàn Chỉnh 100%

> **CÚ PHÁP SỬ DỤNG:**
> ```text
> /remix_to_script [URL_VIDEO_THAM_KHAO]
> ```
> *Ví dụ:* `/remix_to_script https://www.youtube.com/watch?v=kY3B9V6X_z8`

---

## 🎯 4 NGUYÊN TẮC THÉP BẮT BUỘC (MANDATORY GUARDRAILS)
1. **Tấm Khiên Chống Reused Content (Zero Reused Content):** Tuyệt đối CẤM dịch lại câu chữ của video gốc. Chỉ bóc tách *(1) Đề tài/Câu hỏi tò mò cốt lõi* và *(2) Sự thật khoa học/dữ liệu thực chứng công cộng*. Tái cấu trúc 100% cốt truyện và bổ sung thêm ít nhất 20–30% kiến thức mới.
2. **Cấm Tuyệt Đối Bịa Đặt Số Liệu (Zero Data Hallucination):** 100% số liệu (khoảng cách, vận tốc, năng lượng, tỷ lệ %, mốc thời gian) bắt buộc phải có nguồn kiểm chứng xác thực qua **NotebookLM Deep Research (`--mode deep`, `BypassSandbox: true`)** hoặc Web Search. Tuyệt đối cấm đoán mò hoặc làm tròn tùy tiện.
3. **Đồng Bộ Toán Học Veo 3.1 8s:** Mỗi câu thoại trong kịch bản là 1 phân cảnh hoặc phân cảnh phụ, **tuyệt đối không dài quá 26 từ** (trung bình 18–22 từ/cảnh) để đảm bảo an toàn tuyệt đối cho clip 8.0 giây.
4. **Văn Phong Đoạn Văn Tự Nhiên (Paragraph Flow):** Không ngắt dòng rời rạc từng câu đơn. Gom các câu liên tiếp thành đoạn văn (2–4 câu) trôi chảy, hấp dẫn, dễ đọc cho narrator.

---

## 🔄 QUY TRÌNH 8 BƯỚC TỰ ĐỘNG HÓA CHI TIẾT

### 📥 BƯỚC 1: TIẾP NHẬN & BÓC TÁCH HẠT NHÂN SỰ THẬT (NUCLEAR FACT EXTRACTION)
1. **Tạo thư mục tập mới:** Tự động tạo thư mục `episodes/[slug]/` dựa trên đề tài của video.
2. **Trích xuất Transcript:**
   - Chạy lệnh: `node scripts/tools/extract_transcript.cjs "[URL]" "./episodes/[slug]"`
   - Lưu transcript gốc vào `episodes/[slug]/00_source_raw.md`.
3. **Bóc tách Hạt nhân Khoa học:**
   - Trích xuất:
     * *Core Thesis:* Câu hỏi tò mò/nghịch lý cốt lõi của video.
     * *Public Domain Facts:* Danh mục các định luật vật lý, hằng số, sự kiện lịch sử công cộng.
   - Lưu vào `episodes/[slug]/01_nuclear_facts_harvest.md`.

---

### 🔬 BƯỚC 2: DEEP RESEARCH & KHÓA DỮ LIỆU THỰC CHỨNG (DATA VAULT)
1. **Khởi tạo Master NotebookLM (1 Video = 1 Master Notebook):**
   - Tạo notebook mới, lưu ID vào `episodes/[slug]/.notebook_id` và URL vào `.notebook_url`.
   - Nạp các chủ đề/từ khóa chuyên sâu bằng lệnh bắt buộc:
     ```bash
     notebooklm source add-research "<Chủ đề/Từ khóa nghiên cứu sâu>" --mode deep --import-all -n <notebook_id>
     ```
2. **Kiểm chứng chéo số liệu:** Đối chiếu từng con số trong tài liệu gốc với Master Notebook hoặc Web Search.
3. **Bổ sung 20–30% Dữ liệu mới (Information Asymmetry):** Tìm kiếm thêm các góc nhìn phản biện, công nghệ thực nghiệm, phát hiện mới hoặc case study mà video tham khảo không có.
4. Lưu toàn bộ số liệu bất biến vào `episodes/[slug]/02_verified_data_vault.md`.
5. 🛑 **GATE 1:** Báo cáo Hạt nhân khoa học & Bảng số liệu thực chứng cho User.

---

### 🌐 BƯỚC 3: QUY HOẠCH TẦM NHÌN TOÀN CẢNH (GLOBAL VISION SYNTHESIS - 4 TẦNG)
Xây dựng tệp `vault/00_Global_Vision_Synthesis.md` theo cấu trúc 4 tầng chuẩn hóa:
* **Tầng 1 (Meta-Instructions):** Persona giọng đọc kịch tính (*The Infographics Show*), danh sách từ cấm chính trị, chính sách khóa cứng số liệu bất biến.
* **Tầng 2 (ASCII Macro Architecture):** Sơ đồ ASCII toàn cảnh định vị trục tự sự và nhịp độ leo thang căng thẳng.
* **Tầng 3 (Atomic Chapter Blueprints):** 5–7 mô-đun chương độc lập chuẩn hóa 7 trường máy đọc (`THESIS`, `CONTEXT & CONSTRAINTS`, `IMMUTABLE DATA ANCHORS`, `DIALECTIC OPPOSITION`, `NARRATIVE BRIDGE`, `VOICEOVER TONE`, `COMPLIANCE & TERMINOLOGY`).
* **Tầng 4 (Immutable Data Vault):** Bảng tra cứu mã số liệu `DATA-01` đến `DATA-XX`.
* Lập Strategy Brief tại `episodes/[slug]/03_brief.md`.

---

### 🎣 BƯỚC 4: SÁNG TẠO HOOK LAB & DÀN Ý GIỮ CHÂN (OUTLINE ARCHITECTURE)
1. Kích hoạt `hook_engine`: Tạo 5–7 hooks kịch tính với con số thực chứng gây sốc $\rightarrow$ Lưu `04_hook_pack.md`.
2. Kích hoạt `script_architect`: Dựng `05_thesis_map.md`, `06_retention_map.md`, `07_outline.md`, và `08_chapter_briefs.md`.
3. Khởi tạo `09_narrative_state_tracker.md` (NST) để theo dõi các vòng lặp tò mò (loops) và giao thức gieo-gặt hạt giống (seeds/harvests).
4. 🛑 **GATE 2:** Báo cáo Hook Pack & Dàn ý chương cho User duyệt.

---

### ✍️ BƯỚC 5: VIẾT KỊCH BẢN CHUYỂN HÓA TUẦN TỰ (TRANSFORMATIVE WRITING)
1. Kích hoạt `chapter_writer`. Viết TUẦN TỰ từng chương một (`chapter_01.md` $\rightarrow$ `chapter_N.md`).
2. **Nạp Ngữ Cảnh Cuộn (Rolling Context):** Chỉ nạp `vault/00_Global_Vision_Synthesis.md`, brief chương hiện tại, NST, và đúng 3 câu cuối của chương trước để nối mạch.
3. **Quy Chuẩn Toán Học Veo 3.1 8s:**
   - Mỗi câu thoại $\le 26$ từ (trung bình 18–22 từ).
   - Nếu câu dài $> 26$ từ $\rightarrow$ Tách đôi thành 2 phân cảnh phụ (`a1`, `a2`) và phân bổ đều từ thoại.
   - Gom các câu liên tiếp thành đoạn văn (2–4 câu) trôi chảy tự nhiên, giàu kịch tính và ẩn dụ khoa học trực quan.
4. Cập nhật NST sau mỗi chương và gộp toàn bộ thành `episodes/[slug]/final_voiceover.md`.

---

### 🛡️ BƯỚC 6: KIỂM TOÁN CHỐNG REUSED CONTENT & KIỂM TOÁN DỮ LIỆU
Chạy script kiểm toán tự động `python3 scripts/tools/remix_pipeline_runner.py --slug [slug]`:
* **Độ khác biệt ngữ nghĩa:** Đảm bảo $> 80\%$ câu chữ được viết mới hoàn toàn so với transcript gốc.
* **Kiểm toán số liệu thực chứng:** 100% con số trong kịch bản khớp với `02_verified_data_vault.md`.
* **Kiểm toán độ dài câu thoại:** 100% các câu thoại $\le 26$ từ.
* Lưu báo cáo kiểm toán vào `episodes/[slug]/10_compliance_report.md`.
* 🛑 **GATE 3:** Bàn giao Kịch bản Hoàn thiện & Báo cáo Kiểm toán cho User.

---

### 🎬 BƯỚC 7: THIẾT KẾ STORYBOARD MATRIX & PROMPTS VEO 3.1
1. **Storyboard Matrix (`chapter_XX_visual.md`):** Chuẩn hóa 3 trường cho từng cảnh:
   * `[THOẠI]:` Câu thoại cắt chuẩn $\le 26$ từ.
   * `[BỐI CẢNH]:` Chỉ định không gian địa lý, nhân vật, hành động vật lý cụ thể.
   * `[TEXT OVERLAY]:` Ghi rõ chữ Tiếng Anh phẳng hoặc ghi "Không" (chỉ xuất hiện tại ~20–25% cảnh quan trọng).
2. **File Prompt (`prompts_chapter_XX.txt`):**
   * Prompt ảnh tĩnh `[IMAGE]`: 2D Cinematic Noir Vector hoặc Photorealistic 8K.
   * Text Overlay: Tiếng Anh phẳng đặt ở **vùng góc trái phía dưới cách đáy 20%** (`lower-left quadrant approximately 20% above bottom edge`).
   * Prompt video `[VIDEO]`: Cú máy điện ảnh (zoom, pan, tracking) kèm câu lệnh khóa tĩnh đồ họa cho cảnh có chữ.

---

### 📦 BƯỚC 8: BỘ ASSET SẢN XUẤT HOÀN THIỆN
1. **Master Music Prompt (`music_prompt.txt`):** Prompt nhạc nền không gian điện ảnh 80 BPM xuyên suốt video, sạch 100% từ cấm bản quyền.
2. **Sinh Thumbnail AI:** Tự động sinh thumbnail 16:9 chất lượng cao bằng NanoBanana 2 / Imagen 3 với tiêu đề nổi bật, chữ tiếng Việt có dấu chuẩn xác.
3. **YouTube SEO Metadata (`09_youtube_metadata.md`):** Bộ Tiêu đề, Mô tả 5 Block có Timestamps, 3-tier Hashtags, Tags SEO, Tuyên bố trách nhiệm (Disclaimer), và 2 mẫu Bình luận ghim (Pinned Comments).
4. **Bàn giao sản xuất:** Lưu toàn bộ thông tin chỉ dẫn vào `episodes/[slug]/production_notes.md`.

---

## ⚡ HƯỚNG DẪN THỰC THI NHANH
Khi User nhập link:
```text
/remix_to_script https://www.youtube.com/watch?v=XXXXX
```
Agent sẽ tự động đọc workflow này và kích hoạt tuần tự từng bước từ 1 đến 8.
