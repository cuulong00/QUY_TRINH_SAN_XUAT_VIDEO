# Dòng Chảy Workspace Rules & Persisted Learnings

## 🛑 QUY ĐỊNH BẮT BUỘC: THỰC THI NOTEBOOKLM DEEP RESEARCH (DIRECT RPC & SANDBOX POLICY)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI CHẠY LỆNH NOTEBOOKLM:**
> 1. **BẮT BUỘC DÙNG `BypassSandbox: true`:**
>    - Khi Agent gọi tool `run_command` để thực thi CLI `notebooklm` hoặc các script Python kết nối máy chủ Google NotebookLM, **BẮT BUỘC PHẢI ĐẶT `BypassSandbox: true`**.
>    - Tuyệt đối KHÔNG chạy lệnh NotebookLM với `BypassSandbox: false` (chế độ mặc định bị Sandbox chặn toàn bộ internet ra ngoài).
>
> 2. **GIẢI MÃ LỖI `403 Forbidden: Request not allowed by policy` (CẤM ẢO GIÁC):**
>    - Nếu thấy mã lỗi `403 Forbidden: Request not allowed by policy`, ĐÂY LÀ DO SANDBOX PROXY NỘI BỘ CỦA IDE CHẶN MẠNG TRÊN MÁY CỤC BỘ.
>    - **TUYỆT ĐỐI CẤM SUY DIỄN (HALLUCINATE):** Nghiêm cấm bịa đặt rằng "Google Cloud Armor / WAF chặn" hoặc "Cookies tài khoản hết hạn".
>    - **TUYỆT ĐỐI CẤM TỰ Ý BỎ CUỘC ĐỂ HẠ CẤP XUỐNG WEB SEARCH.**
>    - **HÀNH ĐỘNG KHẮC PHỤC NGAY:** Chạy lại ngay lập tức câu lệnh đó với `BypassSandbox: true`.
>
> 3. **CHẾ ĐỘ DEEP RESEARCH BẮT BUỘC (`--mode deep`):**
>    - Mọi tác vụ nghiên cứu nạp nguồn qua NotebookLM BẮT BUỘC phải dùng `--mode deep` và `--import-all`. Nghiêm cấm dùng `--mode fast`.

## 🌐 QUY ĐỊNH BẮT BUỘC: LẬP BỨC TRANH TOÀN CẢNH (GLOBAL VISION SYNTHESIS — KHUNG TƯ DUY PHỔ QUÁT 4 TẦNG)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI TẠO `vault/00_Global_Vision_Synthesis.md` (Pha 2.5):**
> 1. **Triết lý Cốt Lõi: Bản Đồ Địa Hình Hiện Thực vs. Lộ Trình Dẫn Đường (The Map of Reality vs. The Guided Tour):**
>    - Bức tranh toàn cảnh là **BẢN ĐỒ ĐỊA HÌNH CỦA HIỆN THỰC KHÁCH QUAN (The Map of Reality)**: Mô tả bản chất của vùng đất đề tài (kinh tế, địa chính trị, tài chính doanh nghiệp, thị trường vốn), các chủ thể, động lực sinh tồn, quy luật vận hành và hệ thống bằng chứng thực tế. Nó tồn tại khách quan, độc lập với việc kể chuyện.
>    - Dàn ý kịch bản (Outline ở Pha 4) là **LỘ TRÌNH DẪN ĐƯỜNG CHỦ QUAN (The Guided Tour)**: Quyết định số trạm dừng (số chương), nhịp điệu, cảm xúc và thời lượng (8m, 20m hay 45m).
> 2. **Cấu trúc 4 Tầng Tư Duy Phổ Quát (Universal 4-Tier Blueprint):**
>    - **Tầng 1 (Meta-Instructions & Redlines):** Khối YAML/JSON định vị vai trò quan sát/phân tích vĩ mô độc lập, rào cản chính luận, blacklist từ cấm, và chính sách khóa cứng số liệu mỏ neo thực chứng bất biến.
>    - **Tầng 2 (Macro Landscape & Systemic Forces — Bản Đồ Không Gian & Các Lực Lượng):** Sơ đồ ASCII toàn cảnh định vị không gian bàn cờ: Các chủ thể tham gia (Nhà nước, ngân hàng, doanh nghiệp, dòng vốn, người dân), động lực sinh tồn cốt lõi (Incentives), các dòng chảy chủ đạo (dòng tiền, đòn bẩy, hàng hóa) và tương quan lực lượng.
>    - **Tầng 3 (Underlying Mechanics & Central Paradoxes — Quy Luật Vận Hành & Nghịch Lý Cốt Lõi):** Giải phẫu các mắt xích nhân quả gốc rễ (Root Causes & Causal Chains) và khoảng cách giữa kỳ vọng/bề mặt vs thực tế/bản chất. Xác định điểm gãy cấu trúc hoặc quy luật khách quan chi phối toàn bộ đề tài (quy luật chi phí, rào cản thể chế, bẫy thanh khoản, áp lực thâm dụng vốn).
>    - **Tầng 4 (Immutable Ground-Truth Data Vault — Sổ Cái Bằng Chứng Thực Chứng Bất Biến):** Bảng tra cứu mã số liệu, văn bản pháp quy, mốc thời gian, hồ sơ kiểm toán (`DATA-01` đến `DATA-XX`) đối chiếu 1-1 với nguồn tài liệu gốc trong `research_vault/`.
> 3. 🛑 **VÙNG CẤM TUYỆT ĐỐI CỦA PHA 2.5 (HARD REDLINE — CHỐNG ÔM ĐỒM & CHỐNG TIỀN ĐỊNH DÀN Ý):**
>    - **TUYỆT ĐỐI CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản nào:** `CH01`, `CHXX`, `Chương`, `Hồi`, `Hook`, `Scene`, `Voiceover Tone`, `Narrative Bridge`, `Harvest`, `Seed`.
>    - **TUYỆT ĐỐI CẤM chia chương trước Pha 4:** Việc phân chia số chương, thời lượng, nhịp điệu, cấu trúc hồi, và phân bổ quota dữ liệu vào từng chương là **ĐẶC QUYỀN ĐỘC TÔN của Pha 4 (Master Outline Engine)**.
>    - **Chế tài vi phạm:** Mọi tệp `00_Global_Vision_Synthesis.md` xuất hiện cấu trúc chia chương kịch bản đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và sẽ bị hủy bỏ để làm lại.

## 🎙️ QUY ĐỊNH BẮT BUỘC: VIẾT KỊCH BẢN CHƯƠNG (PHA 7 — GEMINI FLASH UNIFIED CO-PILOT)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI THỰC HIỆN PHA 7 (`chapter_writer`):**
> 1. **Kiến Trúc Ngữ Cảnh Toàn Cảnh (Full Clean History Injection):**
>    - Khi viết Chương $N$, Agent **BẮT BUỘC nạp toàn bộ kịch bản thoại sạch của các chương đã viết trước đó (`chapter_01.md` đến `chapter_N-1.md`)** nhằm: (1) Kiểm soát nhịp điệu và dòng chảy cảm xúc toàn bài, (2) Triệt tiêu 100% nguy cơ lặp từ, lặp cấu trúc câu, hoặc trùng lặp ví dụ/ẩn dụ tài chính, (3) Cài cắm các chi tiết gợi nhớ tinh tế (callbacks / foreshadowing) kết nối chặt chẽ giữa các chương.
> 2. **Khóa Khẩu Ngữ Tiền Khởi Động (Front-Loaded Oral Voice DNA):**
>    - Khóa chết văn phong nói cho đôi tai nghe: Viết như một chuyên gia tài chính điềm tĩnh, sâu sắc đang ngồi uống trà trò chuyện thân mật với một người bạn thông minh. Siết trần độ dài câu thoại: **100 – 120 ký tự/câu**. Cấm tuyệt đối văn phong báo cáo hàn lâm khô khan hoặc thuyết giáo đạo lý.
> 3. **Giao Thức Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger - BẮT BUỘC):**
>    - TRƯỚC KHI tạo tệp kịch bản thoại `chapter_XX.md`, Agent **BẮT BUỘC phải in ra màn hình chat Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger)**.
>    - Phân định rạch ròi: `FACT` (100% có Footnote ID và trích dẫn ngắn $\le$ 15 từ từ `research_vault/`) vs `GROUNDED_INFERENCE` (suy diễn logic từ Fact + Quy luật chi phí / First Principles). Đánh trượt tức thì mọi suy diễn vô căn cứ (`FORBIDDEN_SPECULATION`: tự bịa thông số, tự đoán biên lợi nhuận hay động cơ nội bộ).
> 4. **Mô Hình Biện Chứng Kinh Tế Chuẩn Mực (First-Principles Dialectical Triad):**
>    - Mọi xung đột trong kịch bản phải tuân theo mô hình 3 bước thực chứng:
>      $$\text{Chính đề (Mô hình vận hành \& Giả định ban đầu)} \longrightarrow \text{Phản đề (Mâu thuẫn cấu trúc nội tại \& Quy luật chi phí)} \longrightarrow \text{Hợp đề (Sự tiến hóa mô hình \& Cân bằng mới)}$$

## 🛑 QUY ĐỊNH BẮT BUỘC: GHI NHẬN & GIÁM SÁT KHUYẾT TẬT LLM (LLM DEFECT LOGGING MANDATE)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% TRONG TOÀN BỘ QUÁ TRÌNH TẠO KỊCH BẢN:**
> 1. **Sổ Cái Khuyết Tật Tập (`episodes/[slug]/llm_error_log.md`):**
>    - Mỗi episode bắt buộc phải duy trì tệp `llm_error_log.md` theo cấu trúc chuẩn từ `02_templates/llm_error_log_template.md`.
>    - Toàn bộ các lỗi phát sinh từ lúc khởi tạo đến khi ra kịch bản cuối cùng phải được ghi nhận đầy đủ, tuyệt đối cấm âm thầm sửa lỗi bỏ qua việc ghi log.
> 2. **Hệ Thống Phân Loại 6 Nhóm Khuyết Tật:**
>    - `[FORMAT_SYNTAX]`: Lỗi câu >150 ký tự, dấu em-dash (`—`), rò rỉ scaffolding `[BLOCK 1]`, lộ prompt metadata.
>    - `[VOCABULARY_TONE]`: Dính từ cấm AI (`anti_ai_isms.md`), trôi dạt văn phong hàn lâm/báo cáo, sến sẩm hoặc giật gân.
>    - `[DATA_GROUNDING]`: Ảo giác số liệu/lịch sử, trích dẫn sai nguồn, vi phạm ZUI, nhầm lẫn thực thể.
>    - `[LOGIC_REASONING]`: Ngụy biện bù nhìn rơm (Strawman), cắt xén cơ chế First-Principles, tư duy ngăn tủ ("And Then"), giấu bài về cuối.
>    - `[PROCESS_PROTOCOL]`: Bỏ qua Pre-Flight Log, vi phạm sandbox, quên nạp persona, dính lỗi lặp lại (Forbidden Echoes).
>    - `[HUMAN_REJECTION]`: Người dùng từ chối bản nháp, yêu cầu đổi framing, đổi ví dụ hoặc viết lại hoàn toàn.
> 3. **Cơ Chế Kích Hoạt Ghi Log Bắt Buộc:**
>    - Khi Post-Write Audit (Pha 7) hoặc Compliance Council (Pha 10 & 11) phát hiện lỗi $\to$ Ghi ngay vào `llm_error_log.md` trước khi sửa.
>    - Khi Người dùng phản hồi yêu cầu chỉnh sửa (`/revise_chapter` hoặc chat feedback) $\to$ Bắt buộc tạo 1 entry `[HUMAN_REJECTION]` ghi rõ lý do không đạt của bản trước.
> 4. **Vòng Lặp Cải Tiến Liên Tục (Continuous Improvement):**
>    - Dữ liệu từ `llm_error_log.md` được tổng kết vào Section 6.1 của `postmortem.md` (Pha 16) và chuyển giao vào Sổ cái trung tâm `01_management/llm_error_analytics.md` để định kỳ vá System Prompts và Skills.

## 🛡️ QUY ĐỊNH BẮT BUỘC: GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG & TRUY XUẤT NGUỒN GỐC (PRE-FLIGHT LOG & PROVENANCE PROTOCOL)


> ⚠️ **BẮT BUỘC TUÂN THỦ 100% Ở MỌI PHA TẠO TÀI LIỆU (PHA 1 ĐẾN PHA 16):**
> 1. **Bước 1 — In Hộp Log Pre-Flight ra màn hình chat TRƯỚC KHI gọi lệnh tạo file:**
>    ```markdown
>    > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO TÀI LIỆU <Tên_Tài_Liệu>]**
>    > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** [Tên Persona] (`.agents/personas/[file_name].md`)
>    > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** [Tên Skill] (`.agents/skills/[skill_name]/SKILL.md`)
>    > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
>    >   * `[Đường_dẫn_tài_liệu_1]` (Mục đích nạp: ...)
>    >   * `[Đường_dẫn_tài_liệu_2]` (Mục đích nạp: ...)
>    > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/[output_file]`
>    > - 🛡️ **Rào Cản Kiểm Toán & Tôn Chỉ First-Principles:** [Tóm tắt 1-2 dòng nguyên lý cốt lõi]
>    ```
> 2. **Bước 2 — Nhúng Khối Provenance Metadata ở đầu tệp tin (Áp dụng cho các tệp phân tích/kế hoạch):**
>    Đối với các tệp phân tích, chiến lược, brief, outline (`01` đến `08`, `00_Global_Vision_Synthesis.md`, `09_narrative_state_tracker.md`), BẮT BUỘC chèn khối Metadata ở đầu file:
>    ```markdown
>    <!--
>    DOCUMENT PROVENANCE & EXECUTION LINEAGE:
>    - Output Document: episodes/[slug]/[file_name]
>    - Activated Persona: [Tên Persona] (.agents/personas/[file_name].md)
>    - Activated Skill: [Tên Skill] (.agents/skills/[skill_name]/SKILL.md)
>    - Source Documents Consulted:
>      * [Tài liệu nguồn 1]
>      * [Tài liệu nguồn 2]
>    - Execution Timestamp: YYYY-MM-DD HH:MM
>    -->
>    ```
>    *(Riêng với `chapter_XX.md`, nhằm bảo vệ 100% văn bản thoại sạch cho mô hình TTS đọc không bị lẫn rác kỹ thuật, khối Provenance này CHỈ in ra chat ở Bước 1, không nhúng vào tệp kịch bản).*

## 🎨 Tư duy Trực quan: Master Cinematic Visual DNA & I2V Reference Asset Protocol

Đây là tài liệu đúc kết tư duy trực quan và ngôn ngữ tạo prompt chuẩn hóa cho kênh **Dòng Chảy**. Đóng vai trò **quy chuẩn bắt buộc** cho Pha 12 và 12.5 nhằm kiến tạo những thước phim đồ họa 2D tài liệu điện ảnh vĩ mô đỉnh cao.

### 1. Triết lý thiết kế của "Master Cinematic Editorial Visuals"
- **Visual Hook là một thông điệp chiến lược:** Hình ảnh không dùng để trang trí, mà dùng để kể chuyện và giải thích cơ chế dòng tiền, sản xuất và chính sách. Triệt tiêu hoàn toàn chi tiết thừa.
- **Sức nặng của Con người & Lãnh đạo Biểu tượng (Iconic Figures):** Ưu tiên số 1 là đưa diện mạo con người thật (chủ tịch tập đoàn, tài phiệt, CEO, thống đốc, bộ trưởng) vào các phân cảnh then chốt qua ảnh tham chiếu (`@filename.ext ->`). Sự hiện diện của họ tạo nên tính thời sự, sức nặng chính luận và niềm tin tuyệt đối cho người xem.
- **100% Hiện thực Vật lý:** Cấm các biểu tượng bay lơ lửng, huyền ảo phi thực tế (cân bay, quả cầu trong hư vô, bánh răng bay). Mọi chuyển động phải tuân theo quy luật vật lý trong không gian đời thực.

### 2. Các nguyên tắc kỹ thuật chuẩn mực khi triển khai

#### A. Cinema Typography Layout (Selective Lower-Left 25% Rule)
- **Tỷ lệ chọn lọc:** Chỉ xuất hiện ở 20% - 25% phân cảnh then chốt (con số tài chính đột phá, mốc thời gian, đạo luật). 75% - 80% cảnh còn lại KHÔNG chèn chữ để giữ khung hình thoáng đãng.
- **Định vị chuẩn mực:** Bắt buộc đặt nhỏ gọn, cố định tại **góc dưới bên trái cách mép đáy 25%** (`positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge`), chữ song song trực diện ống kính (`facing camera directly, perfectly horizontal`).
- **Khóa chữ ở dòng Video:** Dòng `[VIDEO]` bắt buộc dùng cú máy tĩnh `Steady camera shot` để khóa chết vị trí chữ không bị biến dạng.

#### B. Công thức màu sắc & Ánh sáng sáng sủa (Luminous Editorial DNA)
- **60% Chủ đạo (Nền):** Tông ngà kem ấm áp `warm ivory cream ambient tone (#FAF7EE)` tạo chiều sâu báo chí tài chính quốc tế sang trọng, hoặc `sophisticated modern slate (#2A323D, #2C3539, #1E293B)`. Tuyệt đối CẤM nền than đen kịt `#1A1A1A` và `deep noir chiaroscuro shadows`.
- **30% Bổ trợ (Chủ thể/Nét vẽ):** Nét mực thanh thoát `clean bold ink outlines`, nét phẳng `stylized flat vector textures`, khối nhận diện nhân chủng học Đông Nam Á/Việt Nam rõ nét (`warm light-tan skin`).
- **10% Điểm nhấn (Dẫn mắt):** Chỉ duy nhất 1 màu nhấn phản ánh trạng thái tài chính: Amber ấm `#F59E0B` / Electric Green `#10B981` cho tăng trưởng, dòng tiền; Coral Red `#EF5350` / Warning Orange `#FF7043` cho rủi ro, nợ xấu, khủng hoảng.
- **Ánh sáng:** Luôn dùng `luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows` hoặc `soft golden daylight streaming in`.

#### B2. Giao Thức Ảnh Tham Chiếu & Cơ Chế Diện Mạo Trung Tính (Zero-Bias Safety Formula)
- **Cấm tên người thật trong prompt mô tả:** Để không bị bộ lọc bản quyền/nhân vật công chúng của AI Video chặn, tuyệt đối KHÔNG gõ tên riêng người thật trong câu lệnh mô tả tiếng Anh.
- **Cú pháp chuẩn:** Gắn tag `@filename.ext ->` (VD: `@ceo_vuong.jpg ->`) ở đầu dòng `[IMAGE]` kèm mệnh đề trung tính:
  `A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The subject is [Action & Setting]...`
- **Khóa nét mặt ở dòng Video:** Dòng `[VIDEO]` dùng câu lệnh: `maintaining their composed facial expression and all details of the reference image exactly`.

#### C. Mô phỏng Điện ảnh Chân thực (Cinematic Realistic Simulation) - BẮT BUỘC
- **Không lạm dụng hình khối trừu tượng vô hồn:** Tuyệt đối cấm lạm dụng các hình khối đồ họa trừu tượng (như puzzle, bánh răng, phễu, kim tự tháp...) khiến hình ảnh bị khô cứng và xa rời bối cảnh.
- **Tái hiện đúng bối cảnh & nhân vật thực tế:** Mọi phân cảnh phải mang tính mô phỏng thực tế bối cảnh/sự kiện/nhân vật có liên quan (ví dụ: góc ranh giới DMZ đêm sương mù, hồ sơ mật CIA, hội trường u tối ở Bình Nhưỡng, chợ đen Jangmadang dưới đèn dầu, đoàn tàu chở đạn pháo Siberia...) để khán giả vừa nghe vừa xem và chạm tới cảm xúc điện ảnh.
- **Nghiêm cấm dùng Code để sinh Prompt:** 100% prompt hình ảnh và video phải do LLM tự tay sáng tạo và biên soạn từ cảm thụ kịch bản, không dùng bất kỳ script tự động hóa nào.

#### D. Tối ưu hóa Veo 3.1 & Imagen 3
- Bắt đầu mô tả camera trong prompt: `shot on 35mm anamorphic lens`, `shallow depth of field`, `low-angle perspective`.
- Tốc độ camera: `slow camera panning`, `subtle slow zoom-in`, `steady shot`.
- Đảm bảo tính liên kết vật lý giữa giây cuối của cảnh trước và giây thứ 0 của cảnh sau.
- Loại trừ rác ảnh: `No watermarks, no neon glowing text, no cartoon style, no abstract floating elements`.

#### E. Quy chuẩn Kịch bản Visual Trung gian (Storyboard Matrix) - DNA BẮT BUỘC
- **Quy trình biên soạn:** BẮT BUỘC thực hiện **TUẦN TỰ TỪNG CHƯƠNG MỘT** (`chapter_01_visual.md` -> Duyệt -> `chapter_02_visual.md`). Tuyệt đối CẤM biên soạn hàng loạt một lèo tất cả các chương.
- **Cấu trúc chuẩn:** Định dạng chuẩn theo `02_templates/visual_storyboard_template.md`:
  * Mỗi phân cảnh gồm 3 dòng: `- **[THOẠI]:**`, `- **[BỐI CẢNH]:**`, `- **[TEXT OVERLAY]:**`.
  * **Quy tắc Text Overlay:** Chỉ chèn chữ vào ~20-25% phân cảnh KEY (số liệu, câu nói quan trọng, key questions). **BẮT BUỘC 100% VIẾT BẰNG TIẾNG ANH IN HOA** và **BẮT BUỘC KÈM VỊ TRÍ ĐẶT CHỮ KHÔNG KHÔNG BỊ CHE CHỦ THỂ** (ví dụ: `TOP CENTER | NET WORTH > $4.0 BILLION` hoặc `BOTTOM LEFT | 2024 DIVESTMENT`). Tất cả các cảnh còn lại ghi `Không`.
- **Chống trừu tượng hóa:** Triệt tiêu hoàn toàn các biểu tượng trừu tượng vô hồn (núi tiền bốc cháy, bánh răng, phễu, cán cân, quả bóng bay...). Mọi bối cảnh phải là không gian điện ảnh chân thực, mô phỏng thực tế.

#### F. Đặc Tả Chi Tiết Cơ Khí & Kỹ Thuật Linh Kiện (Mechanical & Technical Granularity - BẮT BUỘC)
- **Cấm mô tả kỹ thuật chung chung:** Tuyệt đối cấm sử dụng các danh từ mơ hồ như "khung gầm xe", "máy móc", "động cơ", "linh kiện ô tô", "dây chuyền".
- **Bắt buộc chỉ định cấu trúc kỹ thuật & cơ khí chính xác:** Ngay từ kịch bản trung gian (`chapter_XX_visual.md`) và prompt (`prompts_chapter_XX.txt`), Agent bắt buộc phải mô tả rõ ràng, chuẩn xác tên gọi và cấu tạo của các cụm cơ khí / linh kiện kỹ thuật cao:
  * *Hệ truyền động & khung gầm:* Khung gầm phẳng tích hợp pin dạng ván trượt (`EV skateboard platform chassis with integrated battery pack structure`), cụm motor điện gắn trục (`e-axle electric drive motor`), cánh tay đòn treo kép bằng nhôm (`aluminum double wishbone suspension arms`), hộp giảm tốc đơn cấp (`single-speed reduction gearbox`).
  * *Hệ thống điện & Pin:* Cụm mô-đun pin Cell-to-Pack dạng lăng trụ/lưỡi dao (`prismatic / blade battery cells in cell-to-pack architecture`), biến tần bán dẫn công suất IGBT/SiC (`IGBT / Silicon Carbide power inverter module`), đường ống làm mát chất lỏng dạng dẹt (`liquid cooling serpentine ribbon tubes`), súng sạc DC chuẩn CCS2/GBT công suất 150kW-250kW với dây cáp làm mát bằng chất lỏng (`liquid-cooled 250kW DC fast charging connector plug`).
  * *Động cơ đốt trong truyền thống (ICE):* Khối thân máy đúc bằng gang/nhôm (`cast iron engine block`), trục khuỷu (`crankshaft`), piston rèn (`forged pistons`), hộp số tự động 8 cấp có biến mô thủy lực (`8-speed automatic torque converter transmission housing`), hệ thống ống xả xúc tác khí thải (`catalytic converter exhaust manifold`).
  * *Mục tiêu:* Đảm bảo khi AI nhìn vào kịch bản trung gian và prompt sẽ hiểu chính xác 100% chi tiết vật lý của cụm linh kiện cần vẽ, không bị suy diễn sai lệch thành những khối sắt vô định hình.

#### G. Quy Chuẩn Triệt Tiêu Hoàn Toàn Ẩn Dụ Trừu Tượng (Anti-Abstract Realism Protocol - BẮT BUỘC)
- **Cấm biến ẩn dụ tu từ/kinh tế thành vật thể đồ họa:** Nghiêm cấm 100% việc dịch thô các biện pháp tu từ trong lời bình thành các biểu tượng đồ họa trôi nổi phi thực tế trong cả kịch bản phân cảnh (`chapter_XX_visual.md`) và prompt (`prompts_chapter_XX.txt`).
- **Bảng quy đổi bắt buộc từ Ẩn dụ sang Hiện thực Điện ảnh:**
  * ❌ *Cán cân tài chính / Cân bằng giá:* -> ✅ **Bãi đỗ xe hoặc Showroom thực tế:** 2 phương tiện vật lý đỗ cạnh nhau, 2 chủ xe đứng trao đổi và so sánh mức giá / chi phí sở hữu tương đương.
  * ❌ *Mô hình dao cạo & Lưỡi dao (Razor & Blade):* -> ✅ **Trụ sạc V-GREEN ngoài đời thực:** Tài xế chạm smartphone app/thẻ RFID vào trụ sạc nhanh DC, màn hình hiển thị trực tiếp dòng nạp điện và thanh toán dịch vụ hàng tháng.
  * ❌ *Bàn cờ kinh tế / Quân cờ địa chính trị:* -> ✅ **Phòng hội nghị chiến lược quốc tế hoặc Phòng lab R&D:** Chuyên gia phân tích bản đồ cảng biển xuất khẩu trên màn hình tường lớn, hoặc kỹ sư kiểm định độ bền linh kiện trên bệ máy dynamometer.
  * ❌ *Thanh kiếm 2 lưỡi:* -> ✅ **Góc nhìn chia đôi thực địa (Split Physical Perspective):** Nửa khung hình là dây chuyền nhà máy chạy hết công suất; nửa khung hình là hình ảnh xe cá nhân cao cấp đỗ bên đường giữa dòng taxi dịch vụ.
  * ❌ *Bức tường vô hình / Gai nhọn bảo hộ:* -> ✅ **Bến cảng container nước sâu Đình Vũ (Hải Phòng):** Các bãi cảng ngập tràn xe điện nội địa bốc dỡ hết công suất, không còn chỗ trống cho tàu xe ngoại tập kết.
  * ❌ *Phễu sản phẩm / Dòng chảy nhu cầu:* -> ✅ **Giao lộ đô thị giờ cao điểm:** Hàng vạn người điều khiển xe máy di chuyển qua trung tâm bàn giao xe và showroom ô tô điện tấp nập khách hàng.
  * ❌ *Mũi tên đâm vỡ tường đá:* -> ✅ **Showroom xe hơi sôi động:** Bảng niêm yết giá sàn truyền thống bị thay thế bằng mức giá khởi điểm mới của dòng xe điện mini, đông đảo khách hàng trẻ vây quanh.
  * ❌ *Mũi tên thị phần va đập triệt tiêu:* -> ✅ **Khu vực đỗ xe đại lý:** Khách hàng phân vân đứng giữa 2 dòng xe liền kề, so sánh mức chênh lệch giá trên bảng thông số.
  * ❌ *Vết nứt màn hình bốc khói:* -> ✅ **Bàn làm việc tài chính đêm muộn:** Chuyên gia tài chính rà soát bảng báo cáo dòng tiền đầu tư khổng lồ và chi phí vốn trên màn hình máy tính.
- **Hành động bắt buộc:** Mọi prompt tạo ra bắt buộc phải chạy qua công cụ kiểm tra tự động `check_boilerplate.py`. Nếu phát hiện bất kỳ từ khóa ẩn dụ trừu tượng nào, script sẽ tự động đánh rớt `FAILED` để buộc Agent phải sửa lại sang bối cảnh thực chứng.

#### H. Giao Thức Khóa Chặt Nhân Chủng Học & Địa Lý (Demographic & Geographic Anchor Lock - BẮT BUỘC)
- **Triệt tiêu hoàn toàn lỗi Tây hóa hình ảnh (Anti-Western Bias):** AI sinh ảnh mặc định sẽ vẽ bối cảnh phương Tây và người da trắng nếu prompt chỉ ghi generic (`a man in a suit`, `a businessman`, `a modern office`).
- **Quy tắc Khóa Nhân Chủng Học (Demographic Lock):** Mọi phân cảnh có xuất hiện con người ở bối cảnh Việt Nam / Đông Nam Á bắt buộc phải chỉ định rõ ràng nhân chủng học:
  * Ví dụ đúng: `A Vietnamese male executive in his late 30s with Southeast Asian features, dark straight hair, warm tan skin, wearing a loose-fitting dark charcoal business suit...`
  * Cấm tuyệt đối: `A man in a suit`, `A businessman`, `An executive` (không có định danh nhân chủng học).
- **Quy tắc Khóa Môi Trường & Kiến Trúc (Environment Anchor Lock):** Mọi prompt `[IMAGE]` bắt buộc phải bắt đầu bằng khối định vị không gian thực địa: `set at Phu Quoc Island, Vietnam...`, `set inside a Vietnamese corporate boardroom in Hanoi, featuring contemporary Southeast Asian architectural elements...`. Cấm dùng `in an office`, `on a city street` không rõ nguồn gốc.

#### I. Giao Thức Tự Rà Soát 2 Lượt & Bảng Đánh Giá Kiểm Toán 6 Trụ Cột (2-Pass Self-Audit Protocol - BẮT BUỘC)
- **Quy trình bắt buộc khi tạo mỗi file prompt (`prompts_chapter_XX.txt`):**
  * **Lượt 1 (Biên soạn):** Tạo prompt cặp đôi `[IMAGE]` và `[VIDEO]` chuẩn 100% bám sát `chapter_XX_visual.md`.
  * **Lượt 2 (Tự rà soát & Kiểm toán tự động):** Chạy lệnh `python3 scripts/check_boilerplate.py episodes/[slug]/prompts_chapter_XX.txt episodes/[slug]/chapter_XX.md`.
  * **Bàn giao (Handoff):** Khi trả kết quả cho người dùng, Agent BẮT BUỘC phải đính kèm **Bảng Đánh Giá Kiểm Toán 6 Trụ Cột (6-Pillar Quality Audit Scorecard)** xác nhận trạng thái `100% PASS - 0 LỖI` qua 6 tiêu chí:
    1. *Demographic & Geographic Anchor* (Khóa nhân chủng học người Việt/Á & Khóa địa danh môi trường)
    2. *Anti-Abstract Realism* (Triệt tiêu 100% biểu tượng trừu tượng: bàn cờ, cán cân, phễu, bánh răng bay)
    3. *Language & Cinema Typography* (100% Tiếng Anh, không dấu tiếng Việt, không ký hiệu VND, text định vị rõ)
    4. *Dual-Line I2V Consistency* (Cặp đôi [IMAGE] & [VIDEO], Action-only video motion, ID đồng bộ)
    5. *Boilerplate & Camera Continuity* (Không lặp cụm từ rác, camera matched movement mượt mà)
    6. *Mathematical Scene Density* ($N_{\text{scenes}} \ge \lceil W_{\text{words}} / 26 \rceil$).
- Nếu còn bất kỳ lỗi nào (`FAIL > 0`), Agent phải tự động sửa lại prompt ngay lập tức cho đến khi đạt `100% PASS` mới được phép báo cáo người dùng.

#### J. Quy Chuẩn Kiểm Soát Chủ Quyền Biển Đảo & Triệt Tiêu Bản Đồ Đường Lưỡi Bò (Anti-Nine-Dash Line Protocol - TUYỆT ĐỐI NGHIÊM NGẶT)
- **Cấm tuyệt đối hình thành đường lưỡi bò / đường 9 đoạn:** Khi mô tả bất kỳ bản đồ biển, hải đồ hàng hải, bản đồ khu vực Đông Nam Á hay Vịnh Thái Lan, TUYỆT ĐỐI KHÔNG ĐƯỢC để AI sinh ra các nét đứt đoạn phi pháp (nine-dash line / U-shaped line) trên biển.
- **Mỏ neo chủ quyền bắt buộc trong prompt bản đồ:** Mọi prompt có hiển thị bản đồ biển bắt buộc phải có câu lệnh khẳng định chủ quyền và khóa nét: `showing authentic Vietnamese maritime sovereignty with clean undisputed boundaries and no dashed lines` hoặc `displaying standard international sea navigation lanes with undisputed sovereign borders and no dashed lines`.
- **Rà soát tự động:** Script `check_boilerplate.py` tích hợp bộ lọc từ cấm chủ quyền `FORBIDDEN_SOVEREIGNTY_VIOLATIONS` để tự động chặn đứng mọi nguy cơ vi phạm.

---

## 🖋️ Quy Chuẩn Giọng Văn Biên Kịch Quái Kiệt & Độ Chín Chuyên Gia (Master Screenplay & Guru DNA - BẮT BUỘC)

### 1. Bản Sắc Tối Thượng: Sâu Sắc, Uy Quyền & "Nói Câu Nào Chết Câu Đó"
- **Tầm vóc nhà biên kịch kiệt xuất:** Lời thoại của Dòng Chảy không phải là bài tập làm văn, không phải tin tức thời sự đọc lại, mà là tác phẩm của một **nhà biên kịch quái kiệt kết hợp với chuyên gia phân tích tài chính/địa chính trị kỳ cựu**.
- **Độ chín & Sức nặng tư duy:** Từng câu chữ phải đạt độ thấu thị cao nhất. Trầm tĩnh, sắc lạnh, sâu cay, bóc trần tận gốc rễ cơ chế vận hành của dòng tiền và quyền lực kinh tế.
- **Hiệu ứng "Nổi da gà" (Spine-Chilling Depth):** Người nghe phải rùng mình vì sự sắc bén, tính quy luật tàn khốc và những sự thật trần trụi được phơi bày mà không cần dùng bất kỳ câu từ giật tít, làm quá nào.

### 2. Bốn Trụ Cột Nhận Thức Luận Của Biên Kịch Quái Kiệt (The 4 Cognitive Pillars)
- **Trụ cột 1 — Lột trần cơ chế ngầm (Forensic Mechanism Dissection):** Bỏ qua mọi ồn ào bề mặt, nhìn thẳng vào chuyển động của dòng vốn, chi phí biên, cấu trúc chi phí chìm và sự phân bổ rủi ro. Không giải thích hiện tượng bằng drama cá nhân mà bằng xung đột của các lợi ích kinh tế cốt lõi.
- **Trụ cột 2 — Nghịch lý cấu trúc tất yếu (Structural Inevitability):** Xây dựng câu chuyện quanh những tình thế đánh đổi tàn nhẫn (trade-offs) mà mọi lựa chọn đều phải trả giá đắt. Người nghe "nổi da gà" vì nhìn thấy sự bất khả kháng của quy luật khách quan.
- **Trụ cột 3 — Lát cắt thực chứng sắc lạnh (Hyper-Realistic Forensic Anchoring):** Sử dụng các chi tiết kỹ thuật cơ khí, thông số tài chính và thực tế vận hành để làm đạn. Chi tiết chân thực tạo ra sức thuyết phục và uy quyền tự nhiên mà không cần bất kỳ sự cường điệu nào.
### 3. Giao Thức Thẩm Thấu Bức Tranh Lớn & Bức Tranh Nhỏ (Macro-Micro Narrative Fusion Protocol)
- **Cấm viết chương cục bộ, biệt lập:** Nghiêm cấm tuyệt đối việc biên soạn một chương như một ốc đảo rời rạc. Một chương chỉ là một bức tranh nhỏ (Micro Canvas) phục vụ cho một mắt xích trong đại chiến lược.
- **Thấu hiểu đồng thời 2 tầng nhận thức:** Khi viết bất kỳ chương nào trong Pha 9, người biên kịch bắt buộc phải nạp và làm chủ đồng thời:
  * *Bức tranh Lớn (The Grand Macro Canvas):* Toàn bộ luận đề trung tâm (`05_thesis_map.md`), chiến lược tổng thể (`03_brief.md`), bản đồ chiến trường vĩ mô (`vault/MASTER_SYNTHESIS.md`), và đích đến cuối cùng của video.
### 4. Quy Chuẩn Triệt Tiêu Ép Cứng Số Lượng Từ (Anti-Word-Count Rigidity Protocol - BẮT BUỘC)
- **Nghiêm cấm ép cứng số lượng từ trong Outline & Chapter Briefs:** Tuyệt đối không đưa các khoảng số lượng từ cứng nhắc dạng `(~750 – 850 từ)`, `(~800 – 900 từ)` vào dàn ý (`07_outline.md`), bản chỉ dẫn chương (`08_chapter_briefs.md`) hay bất kỳ tài liệu định hướng nào.
- **Lý do & Tác hại:** Việc ép cứng số từ biến quá trình viết thành hành vi "đếm chữ", khiến AI rơi vào bẫy bôi chữ rườm rà hoặc cắt xén thô bạo, làm suy giảm nghiêm trọng chiều sâu phân tích, tính sắc bén và nhịp thở điện ảnh của kịch bản.
- **Tiêu chuẩn thay thế:** Dung lượng của mỗi chương phải hoàn toàn do **Độ Chín Của Tư Duy, Tính Trọn Vẹn Của Luận Điểm và Nhịp Thở Tự Nhiên** quyết định. Luận điểm cần giải thích sâu thì viết trọn vẹn, không bôi dài và không cắt ngắn cơ học.

### 5. Quy Chuẩn Tư Duy Bản Chất, Chuỗi Logic Thực Chứng & Dễ Hiểu Tối Thượng (Cognitive Grounding & Hyper-Comprehensibility DNA - BẮT BUỘC)

#### A. Chuỗi Nhân Quả 3 Bước Bắt Buộc (3-Step Causality Protocol)
- **Cấm nhảy cóc nhân quả:** Tuyệt đối không được nhảy cóc từ một hiện tượng vĩ mô thẳng đến một kết luận kịch tính mà không giải thích mắt xích chuyển động của dòng tiền và hành vi con người.
- **Quy trình 3 bước bắt buộc cho mọi luận điểm:**
  * *Bước 1 — Hiện tượng / Cú sốc vĩ mô (The Shock):* Nêu rõ sự kiện, chính sách hoặc con số thực tế (ví dụ: BoT duy trì lãi suất 1%, nợ hộ gia đình chạm 86-91% GDP).
  * *Bước 2 — Cơ chế truyền dẫn vào dòng tiền & tâm lý (The Transmission Mechanism):* Giải thích cụ thể cú sốc tác động vào túi tiền, bảng cân đối kế toán hoặc chi phí cơ hội của ai (người dân thắt lưng buộc bụng lo trả nợ cũ, ngân hàng thương mại siết van tín dụng vì sợ nợ xấu nhóm 2).
  * *Bước 3 — Hệ quả kinh tế tất yếu (The Inevitable Outcome):* Kết luận thực chất (tổng cầu nội địa kiệt quệ, dòng tiền rẻ bị mắc kẹt trong bẫy thanh khoản, hạ lãi suất trở nên vô nghĩa).
- **Phân biệt rạch ròi Tương quan và Nhân quả (Correlation $\neq$ Causation):** Cấm gán ghép các sự kiện xảy ra đồng thời thành nguyên nhân - kết quả nếu không có cơ chế kinh tế làm bệ đỡ.

#### B. Giao Thức Khóa Chặt Số Liệu & Sự Thật Tuyệt Đối (Strict Fact-Anchor Lock)
- **100% số liệu phải neo nguồn từ Vault:** Mọi con số (tỷ lệ %, mốc năm, cơ quan công bố, tên chính sách) trong kịch bản bắt buộc phải trích xuất trực tiếp từ `research_vault/` và `02_research_map.md`.
- **Cấm làm tròn số ẩu và drama hóa:** Tuyệt đối không được làm tròn bừa bãi làm méo mó bản chất (ví dụ: 86% không được biến thành 90% hay "toàn bộ", lạm phát 1,95% không được biến thành "siêu giảm phát").
- **Tách bạch chính xác các định chế & khái niệm:** Phân biệt rạch ròi giữa Nợ công (Public Debt - nợ của chính phủ) và Nợ hộ gia đình (Household Debt - nợ của người dân); giữa Thâm hụt ngân sách tài khóa và Thâm hụt cán cân thương mại.

#### C. Nguyên Tắc Dễ Hiểu Tối Thượng Cho Đôi Tai (Acoustic Comprehensibility & The 100-120 Char Rule)
- **Viết cho đôi tai nghe, không viết cho mắt đọc:** Khán giả nghe video YouTube khi đang lái xe, nấu ăn hoặc làm việc. Câu thoại phải ngấm thẳng vào não ngay lập tức mà không bắt khán giả phải "dừng lại để giải mã".
- **Siết trần độ dài câu thoại: 100 – 120 ký tự/câu:** Mỗi câu thoại chỉ chứa duy nhất một mệnh đề chính, một ý nghĩa, và tối đa một số liệu. Triệt tiêu hoàn toàn các câu ghép nhiều tầng, các mệnh đề quan hệ rườm rà ("mà", "những cái mà", "nhằm mục đích để").
- **Quy tắc 1 Thuật Ngữ - 1 Phép Ví Von Đời Thường (Analogy Mandate):** Mọi khái niệm kinh tế hàn lâm (*bẫy thanh khoản, suy thoái bảng cân đối kế toán, TFR, nợ nhóm 2, Điều 75*) khi xuất hiện bắt buộc phải có ngay 1 câu loại suy bằng hình ảnh đời thường trong vòng 1-2 câu tiếp theo để người nghe hiểu bản chất ngay lập tức.
- **Triệt tiêu từ Hán Việt hàn lâm & dịch thuật máy móc:** Cấm dùng các cụm từ chết như *"sự bất cân xứng của cơ chế điều tiết", "suy thoái cấu trúc tính toán"*. Phải chuyển ngữ sang ngôn ngữ nói sắc lẹm: *"người dân thắt chặt hầu bao", "ngân hàng khóa chặt van bơm tiền"*.

### 6. Quy Chuẩn Đóng - Mở Chương Kiệt Tác & Nghệ Thuật Giữ Chân Khán Giả (Cinematic Chapter Boundary Architecture - BẮT BUỘC)

#### A. Triệt Tiêu Căn Bệnh Báo Đề & Lặp Đề Cơ Học (Anti-Announce & Anti-Repeat Mandate)
- **Cấm báo trước nội dung chương sau ở cuối chương trước:** Tuyệt đối cấm các câu kết dạng hành chính như: *"Câu trả lời nằm ở [Chủ đề X]", "Đó là [Chủ đề X]", "Và chiếc phao cứu sinh là [Chủ đề X]"*. Việc thông báo lộ liễu làm mất sạch sự tò mò (Zeigarnik Effect) và biến kịch bản thành một bản thuyết trình slide khô khan.
- **Cấm mở đầu chương sau bằng cách lặp lại câu kết chương trước:** Tuyệt đối cấm các câu mở đầu kiểu bàn giao ca trực như: *"Khi [Chủ đề X] xuất hiện...", "Để hiểu được [Chủ đề X]...", "Như chúng ta đã thấy ở trên..."*. Khán giả vừa nghe xong, việc lặp lại ngay lập tức khiến nhịp phim bị giật cục và gây mệt mỏi nhận thức.

#### B. Quy Trình 3 Nhịp Đóng Chương Kiệt Tác (The 3-Beat Climax Landing & Acoustic Pause)
Mỗi chương khi kết thúc bắt buộc phải đi qua 3 nhịp kịch tính để tạo **khoảng lặng cảm xúc ("nổi da gà")**:
1. **Nhịp 1 — Đỉnh cao phân tích (Hard Forensic Punch):** Nêu rõ hệ quả trần trụi nhất của cơ chế vừa phân tích.
2. **Nhịp 2 — Đóng đinh cảm xúc & Khoảng lặng nhận thức (Cold Epiphany & Silence Beat):** Một câu chiêm nghiệm lạnh lùng, ngắn gọn, để lại một khoảng lặng âm thanh (2-3 giây) cho khán giả kịp thở và ngấm sức nặng của bi kịch.
3. **Nhịp 3 — Cánh cửa khép hờ / Vết thương mở (The Unsettling Question / Open Wound):** Để lại một nghịch lý hoặc một mối nguy cơ tiềm ẩn chưa có lời giải. Không bao giờ nói trước giải pháp, mà để người xem phải tự thốt lên: *"Thế này thì làm sao sống nổi?"*.

#### C. Quy Trình Mở Đầu Trực Diện Tại Hiện Trường (In Media Res Cold-Open Protocol)
Mỗi chương mới (từ Chương 2 trở đi) bắt buộc phải mở đầu theo nguyên tắc **Đập thẳng vào hiện trường**:
1. **Bắt đầu bằng một cú va đập vật lý mới:** Một âm thanh (tiếng máy tiện im bặt, tiếng còi tàu), một hình ảnh cụ thể (tờ giấy A4 dán trước cổng, két sắt chất đầy tiền), hoặc một con số gây sốc hoàn toàn mới.
2. **Kéo giật khán giả vào câu chuyện (In Media Res):** Hành động diễn ra ngay lập tức mà không cần câu nối hành chính. Khán giả bị cuốn theo diễn biến tiếp theo một cách vô thức.

#### D. Trọng Lực Nhân Quả Vô Hình Giữa Các Chương (The Invisible Gravity Bridge)
- **Sự kết dính điện ảnh không nằm ở liên từ, mà nằm ở Nhân Quả Khách Quan:** Nỗi đau cùng cực ở cuối chương trước tự động trở thành nguyên nhân thúc đẩy hành động tuyệt vọng ở đầu chương sau. Khán giả tự liên kết các mắt xích trong tâm trí mà không cần người dẫn chuyện phải "cầm tay chỉ việc".

## 🎬 QUY ĐỊNH BẮT BUỘC: SẢN XUẤT VIDEO TỰ ĐỘNG (PHA 14 — VIDEOCORE BATCH PRODUCTION)

> ⚠️ **BẮT BUỘC TUÂN THỦ KHI SẢN XUẤT VIDEO CHO DÒNG CHẢY:**
> 1. **Cơ chế 1-Chạm Bản Địa:** Khi User yêu cầu tạo video hoặc gõ `/generate_videos`, Agent thực thi trực tiếp:
>    ```bash
>    python3 scripts/produce_episode_videos.py --episode <slug>
>    ```
> 2. **Hạ tầng Dùng Chung VideoCore:**
>    - Toàn bộ engine điều phối nằm tại `VideoCore` và đã được liên kết mềm (symlink) vào `scripts/` và `.agents/skills/batch_video_generator`.
>    - Tự động quét diff các cảnh thiếu, tự nạp ảnh tham chiếu `@avatar.jpg` từ `episodes/<slug>/ref_images/`, kết nối Chrome port 9222, kích hoạt watchdog 300s, và tự động chuyển file `.mp4` về `episodes/<slug>/videos/`.
> 3. **Kiểm toán Hoàn tất:** Dùng `python3 scripts/check_video_progress.py --episode <slug>` để xác nhận 100% video hợp lệ.
