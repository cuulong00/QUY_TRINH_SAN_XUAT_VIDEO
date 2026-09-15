---
description: Tuyến Chuyển Hóa Nội Dung (Content Transformation) — Tham khảo đề tài từ kênh khác & Tái cấu trúc 100% kịch bản, nghiên cứu sâu không ảo giác, an toàn tuyệt đối trước chính sách Reused Content của YouTube.
---

# Giao Thức Chuyển Hóa Nội Dung & Nghiên Cứu Sâu (Content Transformation & Deep Research Protocol)

Meta-Workflow chuẩn hóa quy trình: **Tiếp nhận đề tài tham khảo → Bóc tách hạt nhân sự thật khoa học → Nghiên cứu sâu qua NotebookLM (Zero Hallucination) → Tái cấu trúc kịch tính hóa 100% → Đồng bộ Toán học Phân cảnh (Veo 3.1 8s) & Visual Prompts 2D Noir**.

---

### BƯỚC 1: TIẾP NHẬN & BÓC TÁCH HẠT NHÂN SỰ THẬT (NUCLEAR FACT HARVEST)
1. **Nạp nguồn đa phương thức:**
   - Nếu là YouTube URL: Chạy `node scripts/tools/extract_transcript.cjs "[URL]" "./episodes/[slug]"` để lấy nội dung.
   - Nếu là Bài báo / PDF / Ý tưởng: Lưu tài liệu gốc vào `episodes/[slug]/00_source_raw.md`.
2. **Nguyên tắc "Tách lớp hạt nhân" (Nuclear Fact Extraction):**
   - Chỉ trích xuất: *(1) Câu hỏi tò mò cốt lõi (Core Thesis)*, *(2) Các sự thật khoa học/dữ liệu thực chứng công cộng (Public Domain Facts)*.
   - **TUYỆT ĐỐI CẤM** sao chép cấu trúc câu, văn phong, câu đùa hoặc ví von của tác giả gốc.
3. Lưu kết quả vào `episodes/[slug]/01_nuclear_facts_harvest.md`.

---

### BƯỚC 2: NGHIÊN CỨU SÂU & KHÓA SỐ LIỆU THỰC CHỨNG (DEEP RESEARCH & DATA VAULT)
1. **Khởi tạo Master NotebookLM (1 Video = 1 Master Notebook):**
   - Tạo Master Notebook cho episode: Ghi ID vào `episodes/[slug]/.notebook_id`.
   - Nạp các chủ đề/từ khóa chuyên sâu vào NotebookLM:
     ```bash
     # BẮT BUỘC: BypassSandbox: true và --mode deep
     notebooklm source add-research "<Chủ đề nghiên cứu chuyên sâu>" --mode deep --import-all -n <notebook_id>
     ```
2. **Chính sách CẤM TUYỆT ĐỐI BỊA SỐ LIỆU (Zero Hallucination Policy):**
   - Mọi con số (khoảng cách, vận tốc, năng lượng, tỷ lệ %, mốc thời gian, điều luật) khi đưa vào kịch bản **BẮT BUỘC PHẢI ĐƯỢC XÁC THỰC**.
   - Nếu phát hiện số liệu bị khuyết, mơ hồ hoặc nghi ngờ $\rightarrow$ Chạy lệnh Deep Research trên NotebookLM hoặc Web Search để truy xuất nguồn gốc. Tuyệt đối **CẤM TỰ Ý ĐOÁN MÒ HOẶC LÀM TRÒN TÙY TIỆN**.
3. **Bổ sung 20–30% Dữ liệu mới (Information Asymmetry):**
   - Tìm kiếm thêm các góc nhìn phản biện, công nghệ thực nghiệm, hoặc case study mới mà video tham khảo không có nhằm tạo giá trị chuyển hóa độc lập (Transformative Value) cho YouTube.
4. Lưu bảng số liệu đã kiểm chứng vào `episodes/[slug]/02_verified_data_vault.md`.
5. 🛑 **CHECKPOINT 1:** Trình bày tóm tắt hạt nhân sự thật và bảng dữ liệu đã kiểm chứng cho User.

---

### BƯỚC 3: QUY HOẠCH TẦM NHÌN TOÀN CẢNH (GLOBAL VISION SYNTHESIS)
1. Xây dựng tệp `vault/00_Global_Vision_Synthesis.md` theo cấu trúc 4 tầng:
   - **Tầng 1:** Meta-Instructions & Guardrails.
   - **Tầng 2:** Global ASCII Architecture (Trục tự sự, Ticking Clock).
   - **Tầng 3:** Atomic Chapter Blueprints (7 trường chuẩn hóa cho từng chương).
   - **Tầng 4:** Immutable Data Vault (Mã hóa `DATA-01` đến `DATA-XX`).
2. Lập Strategy Brief (`03_brief.md`) định nghĩa rõ góc tiếp cận mới mang phong cách *The Infographics Show*.

---

### BƯỚC 4: SÁNG TẠO HOOK LAB & OUTLINE MỚI 100%
1. Kích hoạt `hook_engine`: Tạo 5–7 hooks kịch tính với con số thực chứng gây sốc.
2. 🛑 **CHECKPOINT 2:** Gửi Hook Pack cho User duyệt.
3. Kích hoạt `script_architect`: Dựng `05_thesis_map.md`, `06_retention_map.md`, `07_outline.md`, và `08_chapter_briefs.md`.
4. Khởi tạo `09_narrative_state_tracker.md` (NST) để theo dõi seeding-harvesting.

---

### BƯỚC 5: VIẾT KỊCH BẢN CHUYỂN HÓA (TRANSFORMATIVE WRITING - AUTOPILOT)
1. Kích hoạt `chapter_writer`. Viết tuần tự từng chương (`chapter_01.md` → `chapter_N.md`).
2. **Quy tắc Vàng cho Kịch bản Chuyển Hóa:**
   - **Áp dụng Giao thức Biến Đổi 4 Lớp:** (1) Đổi góc tự sự kịch tính, (2) Đổi 100% ví von khoa học, (3) Bổ sung 20–30% kiến thức mới, (4) Đồng bộ toán học nhịp thở.
   - **Đồng bộ Toán học Veo 3.1 8s:** Mỗi câu thoại là 1 phân cảnh hoặc phân cảnh phụ, **tuyệt đối không dài quá 26 từ** (trung bình 18–22 từ).
   - **Phân đoạn tự nhiên:** Nhóm các câu thành đoạn văn (2–4 câu) trôi chảy, không ngắt dòng vụn vặt.
3. Cập nhật NST sau mỗi chương. Gộp toàn bộ thành `final_voiceover.md`.

---

### BƯỚC 6: KIỂM TOÁN CHỐNG REUSED CONTENT & KIỂM TOÁN DỮ LIỆU
1. **Kiểm toán Chống Trùng Lặp Ngữ Nghĩa (Semantic Differentiation Audit):**
   - So sánh kịch bản mới với tài liệu tham khảo: Đảm bảo độ khác biệt câu chữ $> 80\%$, không có quá 6 từ liên tiếp trùng lặp.
2. **Kiểm toán Số Liệu Thực Chứng (Zero Hallucination Audit):**
   - Quét 100% con số trong kịch bản, đối chiếu 1-1 với `02_verified_data_vault.md`.
3. Lưu báo cáo vào `10_compliance_report.md`.
4. 🛑 **CHECKPOINT 3:** Gửi kịch bản sạch + Báo cáo kiểm toán cho User duyệt.

---

### BƯỚC 7: THIẾT KẾ STORYBOARD MATRIX & PROMPT I2V 2D NOIR
1. Tạo Storyboard Matrix (`chapter_XX_visual.md`):
   - Cắt chuẩn câu thoại $< 26$ từ/cảnh.
   - Định nghĩa hành động vật lý thực tế (loại bỏ 100% hình ảnh trừu tượng/siêu thực).
   - Chỉ định Text Overlay Tiếng Anh cho ~20–25% cảnh quan trọng, 75–80% cảnh còn lại để `Không`.
2. Tạo Prompt File (`prompts_chapter_XX.txt`):
   - 100% Prompt ảnh tĩnh `[IMAGE]` bắt đầu bằng: `A 2D cinematic editorial noir illustration of [Subject], minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dramatic chiaroscuro lighting...`.
   - Text Overlay: Tiếng Anh phẳng (`clean, elegant flat sans-serif typography`), đặt cố định ở **vùng góc trái phía dưới cách đáy 20%** (`lower-left quadrant approximately 20% above bottom edge`).
   - Prompt video `[VIDEO]` cho cảnh có chữ: `Steady camera shot... preserving all typography and static graphic layers...`.
3. Chạy script kiểm toán tự động: Khớp 100% Scene ID và $\le 26$ từ/cảnh.

---

### BƯỚC 8: NHẠC NỀN & SẢN XUẤT HOÀN THIỆN
1. Tạo Master Music Prompt (`music_prompt.txt`) cho 1 bản nhạc điện ảnh 80 BPM xuyên suốt video.
2. Tạo YouTube SEO Metadata (`09_youtube_metadata.md`) & Thumbnail Brief (`08_thumbnail_brief.md`).
3. Khi User yêu cầu: Tiến hành thu âm qua Google TTS / Chirp3-HD.
4. Bàn giao gói sản xuất hoàn chỉnh (`production_notes.md`).
