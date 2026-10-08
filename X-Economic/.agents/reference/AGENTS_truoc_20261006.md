# X-Economy Workspace Rules & Persisted Learnings

## 📌 Canonical Channel DNA & Social Assets (MANDATORY ACCURACY)
- **Official Channel Name:** X-Economy
- **YouTube Official Channel URL Handle:** `https://www.youtube.com/@X-Economy`
- **Editorial DNA:** Investigative Global Macroeconomics, Geopolitics, Supply Chains & Industrial Strategy.
- **Thematic Scope:** Applying the signature investigative & systemic lens to the **United States, the United Kingdom, and Global Geoeconomics** (Housing market distortions, private equity financialization, infrastructure decay, semiconductor chokepoints, productivity traps).
- **Primary Language (Sản phẩm cuối):** English (US English Accent / Documentarian Voice).
- **QUY TRÌNH NGÔN NGỮ 2 GIAI ĐOẠN (DUAL-STAGE LANGUAGE PROTOCOL — BẮT BUỘC 100%):**
  1. **Giai đoạn 1 (Tư duy, Phân tích, Dàn ý, Hook & Kịch bản gốc): 100% BẰNG TIẾNG VIỆT.**
     - Toàn bộ tài liệu từ Pha 1 đến Pha 7 (Dàn ý, Hook Lab, Chapter Scripts chi tiết) **BẮT BUỘC PHẢI VIẾT BẰNG TIẾNG VIỆT** để User trực tiếp đọc, thẩm định, phản biện và kiểm soát 100% nội dung.
     - **TUYỆT ĐỐI CẤM** tự ý viết kịch bản bằng tiếng Anh khi bản thảo tiếng Việt chưa được User duyệt "OK HẾT".
  2. **Giai đoạn 2 (Bản địa hóa & Dịch sang Tiếng Anh): CHỈ THỰC HIỆN KHI USER ĐÃ DUYỆT XONG BẢN TIẾNG VIỆT.**
     - Sau khi User duyệt "OK HẾT" kịch bản tiếng Việt, AI mới được biên dịch sang tiếng Anh chuẩn Mỹ cho voiceover.

## 🛑 QUY ĐỊNH BẮT BUỘC VỀ CÁC CỔNG KIỂM DUYỆT CỦA USER (MANDATORY USER APPROVAL GATES):
> ⚠️ **TUYỆT ĐỐI CẤM TỰ Ý CHẠY VƯỢT RÀO:**
> 1. **CỔNG 1 (Duyệt Kế hoạch Nghiên cứu):** Phải trình câu hỏi nghiên cứu, User duyệt mới được chạy deep research.
> 2. **CỔNG 2 (Duyệt Dàn ý):** Trình dàn ý chi tiết tiếng Việt, User duyệt mới đi tiếp.
> 3. **CỔNG 3 (Duyệt Hook Lab — BẮT BUỘC DỪNG LẠI):**
>    - AI tạo 3-5 kịch bản Hook bằng tiếng Việt.
>    - **BẮT BUỘC DỪNG LẠI**, in toàn văn các Hook ra chat để USER TRỰC TIẾP CHỌN.
>    - **NGHIÊM CẤM** AI tự chọn Hook rồi tự động viết tiếp kịch bản!
> 4. **CỔNG 4 (Duyệt Kịch bản Tiếng Việt):**
>    - Viết kịch bản chi tiết bằng tiếng Việt, trình User đọc duyệt từng chương hoặc toàn bài.
>    - User yêu cầu chỉnh sửa đến khi User xác nhận **"OK HẾT"**.
> 5. **CỔNG 5 (Dịch sang Tiếng Anh):** Chỉ dịch sang tiếng Anh khi Cổng 4 đã được duyệt.
> 6. **CỔNG 6 (Thủ công Visual, Nhạc, TTS):** Chỉ chạy khi User yêu cầu rõ ràng.

## ⚡ NGUYÊN TẮC PHẢN HỒI NHANH & LOẠI BỎ GHI LOG KHUYẾT TẬT RUNTIME (LEAN EXECUTION MANDATE)

> ⚠️ **CHỈ ĐẠO CHÍNH THỨC TỪ NGƯỜI DÙNG: BÃI BỎ TOÀN BỘ VIỆC GHI LOG KHUYẾT TẬT RUNTIME (`llm_error_log.md`):**
> 1. **Loại Bỏ Hoàn Toàn Khỏi Quy Trình Phản Hồi:** 
>    - Tuyệt đối KHÔNG ghi chép, cập nhật số lượng lỗi, viết báo cáo RCA hay can thiệp vào tệp `llm_error_log.md` mỗi khi nhận phản hồi, chỉnh sửa kịch bản hoặc phát hiện lỗi.
>    - Việc ghi log rườm rà làm phân tán tài nguyên, gây chậm trễ thời gian phản hồi và làm gián đoạn luồng làm việc.
> 2. **Tập Trung 100% Vào Hành Động Thực Thi Trực Tiếp:**
>    - Khi Người dùng phản hồi hoặc phát hiện bất kỳ lỗi nào (số liệu, câu chữ, logic, thực thể) $\to$ Agent **chỉnh sửa trực tiếp ngay vào file đích** (`chapter_XX_vni.md`, `chapter_XX.md`, `chapter_XX_visual.md`, `voiceover.md`...), bảo đảm tốc độ tối đa, súc tích, giải quyết dứt điểm vấn đề trong 1 bước duy nhất.


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

## 🌐 QUY ĐỊNH BẮT BUỘC: LẬP BỨC TRANH TOÀN CẢNH & BÀN CỜ HỆ THỐNG (MASTER SYSTEMIC TOPOGRAPHY & GLOBAL VISION — 4 TẦNG)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI TẠO `01_global_vision_synthesis.md` (Pha 1):**
> 1. **Triết lý Cốt Lõi: Bản Đồ Địa Hình Hiện Thực vs. Lộ Trình Dẫn Đường (The Map of Reality vs. The Guided Tour):**
>    - Bức tranh toàn cảnh là **BẢN ĐỒ ĐỊA HÌNH CỦA HIỆN THỰC KHÁCH QUAN (The Map of Reality)**: Mô tả bản chất của vùng đất đề tài (kinh tế, vĩ mô, địa chính trị, thị trường vốn hoặc chuỗi cung ứng công nghiệp), các chủ thể, động lực sinh tồn, quy luật vận hành và hệ thống bằng chứng thực tế. Nó tồn tại khách quan, độc lập với việc kể chuyện, do **`the_macro_strategist` (Chủ tịch Hội đồng)** chủ trì kiến tạo ngay tại Pha 1.
>    - Dàn ý kịch bản (Outline ở Pha 4) là **LỘ TRÌNH DẪN ĐƯỜNG CHỦ QUAN (The Guided Tour)**: Quyết định số trạm dừng (số chương), nhịp điệu, cảm xúc và thời lượng.
> 2. **Nguyên Tắc Chủ Thể Đa Hình Thái (Polymorphic Subject Mandate — BẮT BUỘC):**
>    - ⛔ **CẤM TUYỆT ĐỐI BÓ HẸP CHỦ THỂ:** Chủ thể là **Tâm Chấn Nhận Thức (Cognitive Epicenter)**, không chỉ là công ty hay cá nhân. Bắt buộc phân loại chính xác thuộc 1 trong 5 Hình Thái:
>      * (1) *Thực thể Thể chế / Đạo luật / Ngân hàng TW:* CHIPS Act, Dodd-Frank, Fed, ECB, BoJ, SEC regulations.
>      * (2) *Thực thể Ý niệm / Học thuyết / Mô hình:* Triffin Dilemma, Cantillon Effect, Bretton Woods, Neoliberalism.
>      * (3) *Hiện tượng Xã hội / Nhân khẩu / Thị trường Lao động:* Chi phí sinh hoạt, đình công công nghiệp, khủng hoảng nhà ở.
>      * (4) *Không gian Địa lý / Hành lang Thương mại / Lưu vực:* Eo biển Malacca, Biển Đỏ, Kênh đào Panama, Hành lang năng lượng châu Âu.
>      * (5) *Tập đoàn / Chuỗi Cung ứng / Thị trường Vốn:* ASML, TSMC, Nvidia, BlackRock, thị trường trái phiếu kho bạc Mỹ.
> 3. **Bộ 5 Câu Hỏi Bản Thể Học Phổ Quát (Universal 5-Question Scoping):**
>    Trước khi lập kế hoạch nghiên cứu, Hội đồng Chiến lược bắt buộc phải trả lời 5 câu hỏi gốc rễ:
>    - `1. Entity Anchors`: Chủ thể trung tâm thực chất là AI/CÁI GÌ? Fact-sheet thô sơ bộ gồm những gì?
>    - `2. Arena & Circuit`: Không gian vận động & Mạch truyền dẫn dòng tiền/công nghệ/quyền lực là gì?
>    - `3. Incentives & Survival`: Các bên tham gia muốn gì và sợ gì? Động lực sinh tồn thực sự là gì?
>    - `4. Governing Laws & Paradoxes`: Quy luật khách quan nào đang điều khiển cuộc chơi mà các bên không thể làm trái?
>    - `5. Contested Evidence & Dissent`: Sự thật kiểm toán nằm ở đâu? Con số ngầm & Phe phản biện chỉ trích điều gì?
> 4. **Cấu trúc 4 Tầng Tư Duy Phổ Quát (Universal 4-Tier Blueprint):**
>    - **Tầng 1 (Meta-Instructions & Redlines):** Tuyên bố rõ Hình thái Chủ thể, Quyết định phê duyệt đề tài (Strategy Council Verdict), định vị vai trò quan sát độc lập (Cinematic Editorial Noir), rào cản pháp lý quốc tế (Lowe v. SEC, Corporate Libel), blacklist từ cấm.
>    - **Tầng 2 (Macro Landscape & Systemic Forces — Bản Đồ Không Gian & Các Lực Lượng):** Sơ đồ ASCII toàn cảnh định vị không gian bàn cờ: Các chủ thể tham gia, động lực sinh tồn/kinh tế cốt lõi (Incentives), các dòng chảy chủ đạo và tương quan lực lượng.
>    - **Tầng 3 (Underlying Mechanics & Central Paradoxes — Quy Luật Vận Hành & Nghịch Lý Cốt Lõi):** Giải phẫu các mắt xích nhân quả gốc rễ (Root Causes) và khoảng cách giữa kỳ vọng/bề mặt vs thực tế/bản chất. Xác định điểm gãy cấu trúc và quy luật khách quan chi phối.
>    - **Tầng 4 (Target Ground-Truth Evidence Checklist & Immutable Data Vault):** 
>      * *Hóa giải Nghịch lý Con gà & Quả trứng (Two-Stage Ledger):* Tại Pha 1, Tầng 4 đóng vai trò là **Danh Mục Mỏ Neo Dữ Liệu Cần Điều Tra (Target Evidence Checklist)** xác lập các chỉ tiêu định lượng, hồ sơ SEC 10-K, báo cáo IMF/WB cần truy lùng độc lập; TUYỆT ĐỐI CẤM đoán mò hay tự bịa số liệu chi tiết khi chưa qua Deep Research.
>      * Sau khi hoàn thành Pha 2 (Deep Research), Sổ cái `DATA-01` đến `DATA-XX` được cập nhật chính thức bằng **100% SỐ LIỆU THẬT ĐÃ KIỂM TOÁN TỪ VAULT** vào cả `02_research_map.md` và đồng bộ vào `01_global_vision_synthesis.md`.
> 5. 🛑 **VÙNG CẤM TUYỆT ĐỐI CỦA PHA 1 (HARD REDLINE — CHỐNG ÔM ĐỒM & CHỐNG TIỀN ĐỊNH DÀN Ý):**
>    - **TUYỆT ĐỐI CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản nào:** `CH01`, `CHXX`, `Chương`, `Hồi`, `Hook`, `Scene`, `Voiceover Tone`, `Narrative Bridge`, `Harvest`, `Seed`.
>    - **TUYỆT ĐỐI CẤM chia chương trước Pha 4:** Việc phân chia số chương, thời lượng, nhịp điệu, cấu trúc hồi, và phân bổ quota dữ liệu vào từng chương là **ĐẶC QUYỀN ĐỘC TÔN của Pha 4 (Master Outline Engine do `the_master_script_dramaturg` phụ trách)**.
>    - **TUYỆT ĐỐI CẤM may đo rập khuôn:** Không gượng ép mọi đề tài vào một khuôn mẫu cứng nhắc. Mỗi đề tài được quyền thể hiện cơ chế và nghịch lý theo đúng bản chất hình học tự nhiên của nó.
>    - **Chế tài vi phạm:** Mọi tệp `01_global_vision_synthesis.md` xuất hiện cấu trúc chia chương kịch bản hoặc số liệu bịa đặt thiếu nguồn kiểm toán đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và sẽ bị hủy bỏ để làm lại.


## 🛡️ QUY ĐỊNH BẮT BUỘC: KHÓA CHUYÊN GIA & KỸ NĂNG THƯỢNG NGUỒN (CHỐNG TAM SAO THẤT BẢN TỪ GỐC)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% Ở MỌI PHA TẠO TÀI LIỆU (PHA 1 ĐẾN PHA 7):**
> 1. **Nguyên lý Triệt tiêu Rác từ Gốc (Root-Cause Upstream Discipline):**
>    - Mọi sai lệch bản chất, suy diễn viển vông hay ảo giác kỹ thuật trong kịch bản thoại (Pha 7) đều có nguồn gốc từ việc **các tài liệu thượng nguồn (Nghiên cứu Pha 2, Brief Pha 3, Outline Pha 4, Chapter Briefs Pha 6) bị thả nổi, thiếu danh tính chuyên gia chuyên ngành và thiếu kiểm toán kỹ thuật**.
>    - Khi tài liệu thượng nguồn dịch ẩu thuật ngữ kỹ thuật, đánh đồng các quy trình sản xuất khác biệt hoặc tự ý nâng cấp quan hệ thương mại (như biến tiếp xúc ban đầu thành hợp đồng ràng buộc), nó sẽ trở thành **nguồn nước bị đầu độc (Poisoning the Well)** lây lan xuống toàn bộ pipeline.
> 2. **Ràng buộc Định danh Chuyên gia & Kỹ năng Bắt buộc:**
>    - Mọi pha tạo tài liệu bắt buộc phải gán chặt với Persona DNA và Skill chuyên môn (Pha 1: `strategy_council`; Pha 2: `deep_research` + `the_industrial_economist` + `the_policy_analyst`; Pha 3: `the_editorial_director` + `the_policy_analyst`; Pha 4 (Master Outline Engine): `the_master_script_dramaturg`; Pha 5 (Hook Lab): `the_viral_alchemist` + `the_critical_auditor`; Pha 6 (Chapter Briefs & NST): `the_narrative_director` + `the_critical_auditor`; Pha 7 (Chapter Writing): `chapter_writer`).
>    - Ở khâu Nghiên cứu (Pha 2): Persona kỹ thuật/kinh tế bắt buộc phải kiểm toán tính chuẩn xác của từng thuật ngữ, phân định rạch ròi giữa bản vẽ thiết kế, hồ sơ quy hoạch môi trường với dây chuyền thực tế. Tuyệt đối CẤM dịch thoát ý làm biến dạng nguyên lý cơ học hoặc pháp lý.
>    - Ở khâu Dàn ý & Briefs: Persona `the_critical_auditor` bắt buộc phải rà soát từng luận điểm (Core Claim) và mỏ neo vật lý (Physical Anchor). Mọi giải pháp kinh tế - kỹ thuật được đề xuất phải khả thi ngoài đời thực, cấm bịa đặt các giải pháp phi vật lý hoặc vi phạm quy luật kinh tế quy mô.
> 3. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG & TRUY XUẤT NGUỒN GỐC (MANDATORY PRE-FLIGHT LOG & PROVENANCE PROTOCOL):**
>    - **Quy tắc Bất Biến:** TRƯỚC KHI tạo ra bất kỳ tài liệu nào (từ Pha 1 đến Pha 16, gồm: `01_topic_qualification.md`, `02_research_map.md`, `02_research_synthesis.md`, `vault/00_Global_Vision_Synthesis.md`, `03_brief.md`, `04_hook_pack.md`, `05_thesis_map.md`, `06_retention_map.md`, `07_outline.md`, `08_chapter_briefs.md`, `09_narrative_state_tracker.md`, `chapter_XX.md`, `10_compliance_report.md`...), Agent **BẮT BUỘC PHẢI THỰC HIỆN 2 BƯỚC GHI LOG**:
>      1. **Bước 1 — In Hộp Log Pre-Flight ra màn hình chat TRƯỚC KHI gọi lệnh tạo file:**
>         ```markdown
>         > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO TÀI LIỆU <Tên_Tài_Liệu>]**
>         > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** [Tên Persona] (`.agents/personas/[file_name].md`)
>         > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** [Tên Skill] (`.agents/skills/[skill_name]/SKILL.md`)
>         > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
>         >   * `[Đường_dẫn_tài_liệu_1]` (Mục đích nạp: ...)
>         >   * `[Đường_dẫn_tài_liệu_2]` (Mục đích nạp: ...)
>         > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/[output_file]`
>         > - 🛡️ **Rào Cản Kiểm Toán & Tôn Chỉ First-Principles:** [Tóm tắt 1-2 dòng nguyên lý cốt lõi]
>         ```
>      2. **Bước 2 — Nhúng Khối Provenance Metadata ở đầu tệp tin (Áp dụng cho các tệp phân tích/kế hoạch):**
>         Đối với các tệp phân tích, chiến lược, brief, outline (`01_global_vision_synthesis.md`, `02_research_map.md`, `03_brief.md`, `04_hook_pack.md`, `07_outline.md`, `08_chapter_briefs.md`, `09_narrative_state_tracker.md`), BẮT BUỘC chèn khối Metadata ở đầu file:
>         ```markdown
>         <!--
>         DOCUMENT PROVENANCE & EXECUTION LINEAGE:
>         - Output Document: episodes/[slug]/[file_name]
>         - Activated Persona: [Tên Persona] (.agents/personas/[file_name].md)
>         - Activated Skill: [Tên Skill] (.agents/skills/[skill_name]/SKILL.md)
>         - Source Documents Consulted:
>           * [Tài liệu nguồn 1]
>           * [Tài liệu nguồn 2]
>         - Execution Timestamp: YYYY-MM-DD HH:MM
>         -->
>         ```
>         *(Riêng với `chapter_XX.md`, nhằm bảo vệ 100% văn bản thoại sạch cho mô hình TTS đọc không bị lẫn rác kỹ thuật, khối Provenance này CHỈ in ra chat ở Bước 1, không nhúng vào tệp kịch bản).*
>    - **Chế tài Vi phạm:** Nghiêm cấm hoàn toàn hành vi âm thầm tạo file mà không khai báo log. Mọi tài liệu tạo ra mà không có log định danh đều bị coi là vi phạm kỷ luật hệ thống và bắt buộc phải xóa làm lại.

## 🧭 BẢN ĐỒ ĐIỀU PHỐI TÁC CHIẾN 1-1 (THE MASTER EXECUTION DISPATCHER)

> 🛑 **NGUYÊN TẮC BẤT BIẾN CHỐNG QUÊN DNA & CHỐNG ẢO GIÁC (ZERO-ASSUMPTION GATE):**
> 1. Khi User ra lệnh bằng ngôn ngữ tự nhiên (không dùng slash command) hoặc khi Agent tự động điều phối: **TUYỆT ĐỐI CẤM SUY ĐOÁN MƠ HỒ HOẶC TỰ Ý TẠO FILE NGAY LẬP TỨC**.
> 2. Agent **BẮT BUỘC** tra cứu bảng điều phối 1-1 bên dưới để xác định: (a) Persona DNA nào phải kích hoạt, (b) Skill nào phải dẫn đường, (c) Danh mục tài liệu nguồn bắt buộc phải gọi `view_file` nạp vào ngữ cảnh.
> 3. **CHẾ TÀI KIỂM TOÁN TÁC CHIẾN:** Bất kỳ thao tác tạo file nào mà TRƯỚC ĐÓ chưa từng gọi `view_file` nạp file Persona DNA (`.agents/personas/...`) và file Skill (`.agents/skills/.../SKILL.md`) trong phiên làm việc đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và sẽ bị từ chối công nhận.

| Tín hiệu User (Trigger Phrases) | Pha & Tệp Đầu Ra (Target Output) | Chuyên Gia Kích Hoạt (Persona DNA Path) | Kỹ Năng Dẫn Đường (Skill Path) | Tài Liệu Nguồn Bắt Buộc Đọc (Mandatory Inputs via `view_file`) | Workflow / Lệnh Thực Thi |
|---|---|---|---|---|---|
| "khởi tạo", "init episode", "bắt đầu episode mới", "đề tài mới", "đánh giá đề tài", "chọn chủ đề", "bản đồ hệ thống", "bức tranh lớn", "quy hoạch tầm nhìn" | **Pha 1:** `01_global_vision_synthesis.md` | `.agents/personas/the_macro_strategist.md`<br>+ `.agents/personas/the_critical_auditor.md`<br>+ `.agents/personas/the_policy_analyst.md` | `.agents/skills/strategy_council/SKILL.md` | Ý tưởng của User, tài liệu phác thảo ban đầu, hạt giống tin tức | `/init_episode`<br>*(Bàn cờ 4 Tầng + Ma trận 4 Lăng kính Đối trọng + Prompt 5 Phản biện + Cáo Trạng Phản Đề Thép)* |
| "research", "deep research", "nghiên cứu", "nghiên cứu sâu", "tìm data", "đào dữ liệu", "nạp nguồn" | **Pha 2:** `02_research_map.md` & `02_research_synthesis.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_industrial_economist.md` | `.agents/skills/deep_researcher/SKILL.md`<br>+ `.agents/skills/notebooklm/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`, Master Notebook ID (`.notebook_id`) | `/deep_research`<br>*(BypassSandbox: true, --mode deep, Contested Ledger)* |
| "viết brief", "lập chiến lược", "chiến lược", "strategy brief", "tạo brief", "xây brief" | **Pha 3:** `03_brief.md` | `.agents/personas/the_editorial_strategist.md`<br>+ `.agents/personas/the_policy_analyst.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/research_vault/` | `/build_brief` |
| "viết outline", "dàn ý", "xây cấu trúc", "master outline", "lập dàn ý", "cấu trúc tập" | **Pha 4:** `07_outline.md` | `.agents/personas/the_dialectic_architect.md`<br>+ `.agents/personas/the_industrial_economist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/02_research_synthesis.md` | `/build_outline`<br>*(Biện chứng Hegel 3 Màn: Thesis ➔ Antithesis [The Devil's Chapter — Tri-Adversarial Red Team] ➔ Synthesis)* |
| "viết hook", "mở đầu video", "hook lab", "tạo hook", "chọn hook", "làm hook" | **Pha 5:** `04_hook_pack.md` | `.agents/personas/the_viral_alchemist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/hook_engine/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/01_global_vision_synthesis.md` | `/hook_lab`<br>*(May đo 3 Động cơ nhận thức 30–45s bám Dàn ý)* |
| "viết chapter brief", "brief các chương", "lập brief từng chương", "khởi tạo nst", "tạo sổ cái tự sự" | **Pha 6:** `08_chapter_briefs.md` & `09_narrative_state_tracker.md` | `.agents/personas/the_narrative_director.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/04_hook_pack.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/01_global_vision_synthesis.md` | `/build_outline`<br>*(16 Trường + Steelman Phản Biện 3 Lăng Kính & Trade-offs)* |
| "viết chương", "viết chapter", "viết tiếp", "viết kịch bản", "viết tập" | **Pha 7:** `chapter_XX_vni.md` ➔ `chapter_XX.md` | Persona chỉ định tại Chapter Brief<br>+ Khóa Khẩu ngữ Oral Voice DNA | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/08_chapter_briefs.md` (Brief CH_XX)<br>`episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/09_narrative_state_tracker.md`<br>Toàn bộ clean script `chapter_01.md` đến `chapter_N-1.md` | `/write_chapter`<br>*(Dual-Stage Protocol: Duyệt bản VNI ➔ Bản ENG <150 chars/câu)* |
| "sửa chương", "revise", "chỉnh sửa chapter", "sửa kịch bản chương" | **Hậu Pha 7:** `chapter_XX.md` | `.agents/personas/the_critical_auditor.md`<br>+ Persona tác giả chương | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/chapter_XX.md`<br>`episodes/[slug]/08_chapter_briefs.md`<br>Feedback từ User / Auditor | `/revise_chapter` |
| "gộp voiceover", "merge", "gộp kịch bản", "gộp toàn bộ chương", "voiceover hoàn chỉnh" | **Pha 8:** `voiceover.md` | `.agents/personas/the_quality_czar.md` | `.agents/skills/chapter_writer/SKILL.md` | Toàn bộ `chapter_01.md` đến `chapter_XX.md`<br>`episodes/[slug]/04_hook_pack.md` (Selected Hook) | `/merge_voiceover` |
| "kiểm toán retention", "audit nhịp", "retention bridge audit", "soi điểm rơi", "soi giữ chân" | **Pha 9:** `retention_bridge_audit.md` | `.agents/personas/the_critical_auditor.md` + `.agents/personas/the_quality_czar.md` | `.agents/skills/retention_bridge_audit/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/07_outline.md` | `retention_bridge_audit` SKILL<br>*(Quy tắc Payoff Void & Dead Air scan >60 words)* |
| "kiểm tra", "QA", "review kịch bản", "compliance", "audit chính sách", "soi lỗi chính trị/pháp lý" | **Pha 10 & 11:** `10_compliance_report.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_critical_auditor.md`<br>+ `.agents/personas/the_editorial_strategist.md` | `.agents/skills/compliance_council/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/03_brief.md` | `compliance_council` SKILL<br>*(Lowe v. SEC, Corporate Libel, Tri-Adversarial Red Team $\ge 25\%$)* |
| "seo", "metadata", "tiêu đề", "viết mô tả", "tags", "tối ưu youtube" | **Hậu kịch bản:** `metadata.md` | `.agents/personas/the_algorithm_whisperer.md`<br>+ `.agents/personas/the_content_strategist.md` | `.agents/skills/metadata_strategist/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/04_hook_pack.md` | `metadata_strategist` SKILL |
| "visual", "tạo hình", "prompt ảnh", "scene timing", "visual map", "storyboard" *(Chỉ khi có yêu cầu)* | **Pha 12:** `scene_timing_map.json`<br>& `visual_storyboard_blueprint.md`<br>& `prompts_chapter_XX.txt` | `.agents/personas/the_scene_architect.md`<br>+ `.agents/personas/the_visual_storyteller.md`<br>(Master Cinematic Visual Director) | `.agents/skills/scene_timing_builder/SKILL.md`<br>+ `.agents/skills/visual_prompter/SKILL.md`<br>+ `02_templates/visual_storyboard_template.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/ref_images/` | `/generate_visual_prompts`<br>*(I2V Reference Asset Protocol)* |
| "audio direction", "nhạc nền", "music cue", "sound landscape", "sound design" *(Chỉ khi có yêu cầu)* | **Pha 13:** `audio_cues.md` | `.agents/personas/the_sonic_architect.md`<br>+ `.agents/personas/the_cinematic_sonic_alchemist.md` | `.agents/skills/music_composer/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/scene_timing_map.json` | `music_composer` SKILL |
| "thu âm", "TTS", "record", "chạy tts", "đọc voiceover" *(Chỉ khi có yêu cầu)* | **Thu âm:** `episodes/[slug]/audio/` | `.agents/personas/the_voice_architect.md` | `scripts/record_voiceover.py`<br>(OmniVoice GPU Bridge) | `episodes/[slug]/voiceover.md` (hoặc từng `chapter_XX.md`) | `/record_voiceover` |
| "handoff", "bàn giao sản xuất", "production handoff", "tổng hợp bàn giao" | **Pha 15:** `production_notes.md` | `.agents/personas/the_editorial_strategist.md` | `.agents/skills/production_handoff/SKILL.md` | `episodes/[slug]/10_compliance_report.md`<br>`episodes/[slug]/metadata.md`<br>`episodes/[slug]/voiceover.md` | `/production_handoff` |
| "đánh giá kênh", "bắt bệnh video", "kiểm tra chỉ số", "retention", "phân tích ctr", "báo cáo kênh" | **Báo cáo Kênh:** Channel Audit | `.agents/personas/the_channel_manager.md` | `.agents/skills/channel_manager/SKILL.md` | Dữ liệu YouTube Studio Analytics | `channel_manager` SKILL |
| "tạo shorts", "làm shorts", "cắt shorts", "short pack", "viral shorts" | **Shorts:** `episodes/[slug]/shorts/` | `.agents/personas/the_shorts_strategist.md`<br>+ `.agents/personas/the_vertical_video_maestro.md` | `.agents/skills/shorts_producer/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/04_hook_pack.md` | `/generate_shorts` |

## 🎙️ QUY ĐỊNH BẮT BUỘC: VIẾT KỊCH BẢN CHƯƠNG (PHA 7 — GEMINI 3.8 FLASH UNIFIED CO-PILOT)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI THỰC HIỆN PHA 7 (`chapter_writer`):**
> 1. **Kiến Trúc Ngữ Cảnh Toàn Cảnh (Full Clean History Injection):**
>    - Khi viết Chương $N$, Agent **BẮT BUỘC nạp toàn bộ kịch bản thoại sạch của các chương đã viết trước đó (`chapter_01.md` đến `chapter_N-1.md`)**.
>    - Tuyệt đối không giới hạn trong 3 câu cuối. Tận dụng triệt để cửa sổ 1 triệu tokens của Gemini 3.8 Flash để kiểm soát nhịp điệu, chống lặp từ/lặp cấu trúc câu và tạo các liên kết gợi nhớ (callbacks) tinh tế.
> 2. **Khóa Khẩu Ngữ Tiền Khởi Động (Front-Loaded Oral Voice DNA):**
>    - Gemini 3.8 Flash có xu hướng hành văn trang trọng, lý tính. Do đó, ngay từ khâu viết nháp, Agent **BẮT BUỘC phải khóa chết văn phong nói**: Viết như một nhà quan sát điềm tĩnh đang ngồi uống trà trò chuyện thân mật với một người bạn thông minh. Cấm tuyệt đối văn phong báo cáo hàn lâm, tiểu luận khô khan hoặc thuyết giáo đạo lý.
> 3. **Giao Thức Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger - BẮT BUỘC):**
>    - Tuyệt đối CẤM kiểm toán ngầm trong suy nghĩ rồi tự tick xanh trong bóng tối.
>    - TRƯỚC KHI tạo tệp kịch bản thoại `chapter_XX.md`, Agent **BẮT BUỘC phải in ra màn hình chat Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger)**.
>    - Phân định rạch ròi: `FACT` (100% có Footnote ID và trích dẫn ngắn ≤ 15 từ từ `research_vault/`) vs `GROUNDED_INFERENCE` (suy diễn logic từ Fact + Quy luật chi phí $T/V$ / First Principles). Đánh trượt tức thì mọi suy diễn vô căn cứ (`FORBIDDEN_SPECULATION`: tự bịa thông số máy móc, tự đoán biên lợi nhuận hay động cơ nội bộ).
> 4. **Mô Hình Biện Chứng Kinh Tế Chuẩn Mực (First-Principles Dialectical Triad):**
>    - Mọi xung đột trong kịch bản phải tuân theo mô hình 3 bước thực chứng:
>      $$\text{Chính đề (Mô hình vận hành \& Giả định ban đầu)} \longrightarrow \text{Phản đề (Mâu thuẫn cấu trúc nội tại \& Quy luật chi phí)} \longrightarrow \text{Hợp đề (Sự tiến hóa mô hình \& Cân bằng mới)}$$
>    - Tuyệt đối CẤM công thức "dư luận nghĩ gì ➔ thực tế nghiệt ngã ➔ ca ngợi quyết định dũng cảm". Không biến kênh thành nơi cãi nhau với mạng xã hội hoặc làm PR bưng bô cho doanh nghiệp.
> 5. **Kỷ Luật Phân Đoạn Văn Xuôi (Paragraph Integrity Hard Gate — $S/P \ge 1.8$):**
>    - Giới hạn 150 ký tự/câu là giới hạn kỹ thuật âm học cho máy đọc TTS thở, CHỈ áp dụng cho **độ dài của một câu đơn kết thúc bằng dấu chấm (.) hoặc chấm phẩy (;)** trên cùng một dòng văn.
>    - **TUYỆT ĐỐI CẤM NGẮT DÒNG TỪNG CÂU:** Tuyệt đối cấm hiểu sai thành việc xuống dòng `\n\n` sau mỗi câu! Toàn bộ kịch bản (cả tiếng Việt `chapter_XX_vi.md`, tiếng Anh `chapter_XX_en.md`, `chapter_XX.md` và `voiceover.md`) **BẮT BUỘC PHẢI VIẾT THÀNH CÁC ĐOẠN VĂN VĂN XUÔI (PROSE PARAGRAPHS) TRÔI CHẢY**, mỗi đoạn gom từ 2 đến 4 câu có liên kết logic nhân quả chặt chẽ.
>    - **Chỉ số kiểm toán bắt buộc:** Tỷ lệ trung bình $S/P = \text{Tổng số câu} / \text{Tổng số đoạn văn} \ge 1.8$. Nếu $S/P < 1.5$ (dấu hiệu ngắt dòng từng câu), tệp kịch bản bị đánh rớt ngay lập tức.
>    - **Tách bạch 100% giữa Kịch bản đọc và Phân cảnh hình ảnh:** Phân cảnh thị giác (`scene_timing_map.json`, `prompts_chapter_XX.txt`) có thể là 1 câu/scene để khớp video 8s, nhưng văn bản kịch bản thoại PHẢI LUÔN LÀ CÁC ĐOẠN VĂN HOÀN CHỈNH. Tuyệt đối không đem định dạng 1 câu/cảnh gán ngược vào kịch bản voiceover.

## 🧠 QUY CHUẨN TƯ DUY VIẾT BÀI CHUYÊN GIA (EDITORIAL & NARRATIVE MINDSET)

Kênh X-Economy định vị là kênh phóng sự điều tra kinh tế vĩ mô, địa chính trị, thị trường vốn và chuỗi cung ứng toàn cầu (Cinematic Editorial Noir). Khán giả của kênh là những nhà đầu tư, chuyên gia, và công dân toàn cầu thông minh, có học thức và tư duy phản biện cao. 
**Người viết kịch bản không hành xử như một chiếc máy chắp vá từ ngữ (fix code / fix case), mà phải vận hành bằng TƯ DUY BIÊN TẬP NGUYÊN BẢN (First-Principles Editorial Mindset).** Mọi kịch bản phải tuân thủ 4 trụ cột tư duy cốt lõi sau:

### 1. Tư Duy Bản Chất & Cơ Chế Thực Chứng (Substance & Mechanism First)
- **Nắm chắc cơ chế trước khi hạ bút:** Trước khi viết bất kỳ nhận định nào về chính sách tiền tệ, thuế quan, tài chính phái sinh hay chuỗi bán dẫn, người viết phải tự trả lời được bản chất vận hành:
  * *Chủ thể và không gian quy định là gì?* (Phân định rạch ròi giữa thẩm quyền tài phán, quy chế NHTW, lệnh trừng phạt và hiệp định thương mại).
  * *Dòng tiền và quyền tài sản dịch chuyển như thế nào?* (Hiểu rõ cơ chế repo, đường cong lợi suất, tài sản bảo đảm, bảo hiểm rủi ro tín dụng CDS; không dùng ngôn từ thông tục làm méo mó bản chất tài chính).
  * *Động lực kinh tế (Incentives) thực sự của các bên là gì?* (Mọi hành vi kinh doanh phải được giải thích bằng bài toán chi phí biên, rủi ro thanh khoản, thị phần và điểm hòa vốn, tuyệt đối không quy kết cảm tính hay đạo đức hóa).

### 2. Tư Duy Hình Tượng Hóa Chuẩn Xác (Precision Metaphor)
- Kịch bản viết cho khán giả toàn cầu nghe hiểu qua video tài liệu, do đó việc sử dụng hình tượng đời thường và phép loại suy (Metaphor) là bắt buộc.
- **Tuy nhiên, hình tượng hóa chỉ để LÀM SÁNG TỎ CƠ CHẾ, không được BÓP MÉO BẢN CHẤT:** Một phép ẩn dụ xuất sắc phải phản ánh đúng logic vận hành thực tế. Nếu một phép so sánh làm khán giả hiểu sai về cách thức hoạt động của thị trường vốn, địa chính trị hay công nghệ, đó là một phép so sánh tồi và phá hủy uy tín của kênh.

### 3. Hợp Đồng Nhận Thức & Mạch Dẫn Tuyến Tính (Narrative Contract & Cognitive Flow)
- Người xem tiếp nhận video theo trục thời gian một chiều (Linear Time). Phần mở đầu (Hook) chính là một **Hợp đồng nhận thức (Cognitive Contract)** ký kết với khán giả: Mọi xung đột kịch tính, câu hỏi lớn, bí ẩn hay nghịch lý được gieo ở Hook là lời hứa mà người viết bắt buộc phải giải tỏa ngay trong các phân đoạn tiếp theo.
- Tuyệt đối không được "bỏ rơi" câu hỏi của khán giả để nói sang các chủ đề lan man khác. Mạch phim phải giải quyết từng nút thắt theo đúng dòng tâm lý tự nhiên của người nghe: *Nêu nghịch lý ➔ Giải mã nguyên nhân trực tiếp ➔ Đào sâu cơ chế cốt lõi ➔ Mở rộng tác động hệ thống ➔ Đúc kết bài học.*

### 4. Kỷ Luật Tự Phản Biện Độc Lập (Inversion & Skeptical Audit)
- Người viết kịch bản phải luôn tự đặt mình vào vị trí của một chuyên gia kinh tế trưởng, một luật sư hoặc một nhà quan sát độc lập khó tính nhất để tự vấn:
  * Câu văn này có đang bị "trôi" theo cảm xúc hay sa vào bẫy giật gân, nói quá?
  * Thuật ngữ và số liệu đưa ra có đứng vững trước sự soi xét của giới chuyên môn không?
  * Phép lập luận có nhất quán về logic nhân quả không, hay đang đánh đồng tương quan với nguyên nhân?

### 5. Ba Rào Cản Tư Duy Biên Tập Chống Mờ Nhạt & Chống Văn Phong Bào Chữa (The 3 Cognitive Gates)
- **Gate 1: Vị thế Nhà điều tra Độc lập (Third-Party Investigator):**
  * Người viết là nhà phân tích kinh tế / điều tra công nghiệp độc lập, tuyệt đối KHÔNG hành xử như luật sư bào chữa hay nhân viên PR của doanh nghiệp.
  * Khi đối mặt với sự kiện tiêu cực hoặc thông tin trái chiều, tuyệt đối không dùng văn phong phòng thủ, thanh minh hay đối đầu với truyền thông (*"tin đồn thất thiệt", "tiêu đề giật gân vội vã quy chụp", "đập tan đồn đoán"*). Hãy thừa nhận sức nặng của sự kiện như một hiện tượng khách quan và tập trung giải mã bản chất cơ chế kinh tế/động lực lợi ích đằng sau nó.
- **Gate 2: Luật Hướng tâm Xung đột (Conflict-Centric Momentum):**
  * Hook gieo quả bom nhận thức nào, thân bài phải lập tức tháo ngòi quả bom đó. Tuyệt đối không được "đổi chủ đề" hoặc lùi về vùng an toàn dễ dãi (như kể công thành tích hay báo cáo hoạt động chung chung) để né tránh xung đột gai góc.
  * Phải đưa khán giả bước thẳng vào hiện trường vụ việc: Văn bản đó phát lệnh gì, ai chịu áp lực, cơ chế nào dẫn tới quyết định đó.
- **Gate 3: Gia tốc Thông tin & Chống Nhai lại Số liệu (Information Velocity):**
  * Mỗi câu văn tiếp theo phải đẩy nhận thức của người nghe tiến về phía trước.
  * Triệt tiêu 100% việc lặp lại cơ học các số liệu đã xuất hiện ở Hook. Dữ liệu cũ chỉ đóng vai trò là mỏ neo tương phản nền tảng, không liệt kê lại các con số trung gian nếu chúng không phục vụ trực tiếp cho một luận điểm hoàn toàn mới.


## 🎨 Tư duy Trực quan Tham chiếu: Cinematic Editorial Noir (Đồ họa Báo chí Điện ảnh)

Đây là tài liệu đúc kết tư duy trực quan và hướng dẫn viết prompt mẫu cho các chủ đề phân tích kinh tế vĩ mô, địa chính trị và công nghệ toàn cầu của X-Economy.

### 1. Triết lý thiết kế "Cinematic Editorial Noir"
- **Minh họa báo chí cao cấp (Editorial Illustration):** Hình ảnh hướng tới phong cách bán thực tế (semi-realistic), sắc sảo, tối giản và nghệ thuật như các trang phóng sự chuyên sâu của *The Economist, Bloomberg Originals, Financial Times*. Tránh hoàn toàn cảm giác hoạt hình (cartoon) trẻ con hay nét vẽ thô sơ.
- **BẮT BUỘC FRONT-LOAD PHONG CÁCH 2D BÁO CHÍ (2D Art Medium Front-Loading - BẮT BUỘC):** 100% prompt ảnh tĩnh `[IMAGE]` bắt buộc phải bắt đầu bằng cụm từ cố định: `A 2D cinematic editorial noir illustration of [Chủ thể], minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures...`. Tuyệt đối CẤM mở đầu bằng các từ chỉ góc máy chụp ảnh như `A photo of...`, `A wide shot of...`, `A low-angle shot of...`, `An exterior shot of...` (khiến AI hiểu lầm là ảnh chụp thật photorealism).
- **Tính liên kết và logic vật lý:** Mọi chuyển động camera và sắp đặt cảnh quan phải bám sát ngữ cảnh thực tế của câu chuyện, có tính liên kết không gian (Background Anchoring) chặt chẽ giữa cảnh trước và cảnh sau.

### 2. Các nguyên tắc thiết kế gợi ý khi triển khai

#### A. Phối màu 60-30-10 & Thích ứng Chủ đề
- **60% Chủ đạo (Nền/Bóng tối):** Gam màu tối sang trọng như `dark warm charcoal (#1A1A1A)`, `luxurious deep slate (#1E293B)`, `deep indigo gradient`.
- **30% Bổ trợ (Nét vẽ/Chủ thể):** Nét vẽ màu kem ấm `warm cream (#FFFDF0) outlines`, tông ngà ấm hoặc chi tiết đồng xước `burnished bronze accents`.
- **10% Điểm nhấn (Dẫn mắt):** Chỉ dùng một màu nhấn duy nhất để làm bật lên tiêu điểm:
  *   *Thị trường/Dòng vốn/Công nghệ:* Xanh ngọc điện tử `glowing turquoise (#26A69A)` hoặc xanh xô thơm `electric sage green (#81C784)`.
  *   *Khủng hoảng/Điểm nghẽn/Nợ công:* Đỏ san hô `glowing crimson coral red (#EF5350)` hoặc cam đất `glowing terracotta orange (#FF7043)`.
- **Thích ứng theo Tuyến:**
  *   *Tuyến Phóng sự Thể chế & Vĩ mô:* Sử dụng gam màu tối sang trọng (#1E293B, #1A1A1A), nét vẽ kem ấm (#FFFDF0), ánh sáng hổ phách và đồng xước.
  *   *Tuyến Công nghệ & Bán dẫn Toàn cầu:* Sử dụng phong cách Futuristic Cyber-Minimalism với nền tối sâu, dòng chảy dữ liệu AI, robot hoặc mạng lưới bán dẫn tối giản.

#### B. Thiết kế chữ trên màn hình (Cinema Typography Layout)
- **Tọa độ thẳng song song:** Chữ overlay luôn facing camera trực diện, song song với ống kính (`facing the camera directly, perfectly horizontal and straight 3D text overlay`). CẤM viết chữ nghiêng (Italic) hoặc chữ uốn méo theo phối cảnh 3D của môi trường.
- **Ngôn ngữ hiển thị:** Đối với kênh tiếng Anh X-Economy, toàn bộ text overlays trên màn hình PHẢI HOÀN TOÀN BẰNG TIẾNG ANH (in ALL CAPS hoặc Title Case ngắn gọn, ví dụ: `SUPPLY CHAIN CRITICAL FAILURE`, `THE $1.2T DEFICIT`, `SILICON CHOKEPOINT`). Chỉ định rõ kết cấu chữ cứng cáp, bóng đổ đen dày (`heavy black drop shadow`) trên nền không gian âm sạch.
- **Quy tắc Chọn lọc Text Overlay (Selective Typography Rule - BẮT BUỘC KHÔNG ĐƯỢC NHẬP SAI):** Tuyệt đối **CẤM chèn Text Overlay trên 100% mọi phân cảnh**. Chữ overlay chỉ được phép xuất hiện tại **~20% - 25% các phân cảnh QUAN TRỌNG NHẤT** (như mốc thời gian lịch sử, thông số kỹ thuật/tài chính cốt lõi, danh hiệu hoặc tuyên bố mang tính bước ngoặt). Với **75% - 80% các phân cảnh còn lại**, bắt buộc phải để `[TEXT OVERLAY]: None` (hoặc không nhắc đến text overlay trong prompt ảnh) để trả lại không gian mỹ thuật đồ họa cho NanoBanana 2 và cho phép mô hình Veo 3.1 chuyển động ống kính linh hoạt (`slow push-in dolly shot`, `panning shot`, `tracking shot`, `tilt-up shot`), tránh làm video bị rác chữ và đơn điệu.

#### B1. Quy Chuẩn An Ninh Chủ Quyền & Bản Đồ Số Hóa (Sovereignty & Clean Map Protocol - BẮT BUỘC)
- **Tuyệt đối CẤM vẽ bản đồ ranh giới lãnh thổ / biên giới địa chính trị chi tiết:** Đặc biệt là khu vực Biển Đông, Đông Nam Á và Châu Á, nhằm ngăn chặn triệt để 100% nguy cơ mô hình AI tự vẽ hoặc áp đặt hình ảnh phi pháp ("đường lưỡi bò" / "nine-dash line").
- **100% Bản đồ bắt buộc phải là BẢN ĐỒ KINH TẾ & CÔNG NGHỆ TRỪU TƯỢNG (Abstract Economic & Tech Network Nodes):**
  * Chỉ sử dụng mạng lưới các điểm nút số hóa (`abstract digital cyber grid with illuminated financial/tech nodes`) kết nối bằng các tia sáng/luồng truyền dữ liệu số (`radiant data transfer vectors`).
  * Chỉ định vị các điểm nút tài chính/kinh tế/công nghệ/công nghiệp trọng điểm trong kịch bản bằng các khối biểu tượng hình học và mũi tên luồng tiền/hàng hóa/nhân tài.
  * TUYỆT ĐỐI KHÔNG vẽ đường biên giới lãnh thổ, không vẽ các đường phân định biển.
#### C. Tôn Chỉ Zero-Metaphor — Tuyệt Đối Cấm Ẩn Dụ Trừu Tượng Hóa & Lỗi Thời Niên Đại (Zero-Metaphor Mandate)
- ⛔ **CẤM TUYỆT ĐỐI ẩn dụ hóa siêu thực/trừu tượng:** Cấm các biểu tượng vô nghĩa như bánh răng nợ công khổng lồ quay giữa hư không, cổng đá nguyên khối bán dẫn, bàn cờ bay lơ lửng, chuỗi xoắn ốc DNA phát sáng trên đồng ruộng, quả cầu năng lượng, cái cân công lý bay trên trời, bàn tay sắt điều khiển con rối.
- ⛔ **CẤM đưa thực thể sai lệch niên đại lịch sử hoặc hạ cấp hoàn cảnh:** Không đưa đèn dầu le lói, công cụ cổ xưa, lò rèn thủ công vào bối cảnh tài chính, công nghệ cao hay nhà xưởng hiện đại thế kỷ 21.
- 🎯 **Quy tắc Hiện thực Vật lý Dễ Hiểu trong 0.5s:** Mọi cảnh AI bắt buộc phải vẽ hiện thực vật lý cụ thể, chân thực, chuẩn xác niên đại lịch sử, bám sát hành động của con người hoặc máy móc thực tế (nhà phân tích ngồi trước dàn màn hình Bloomberg Terminal, kỹ sư trong phòng sạch cleanroom kiểm tra tấm wafer quang khắc, lãnh đạo cấp cao họp bàn quanh hồ sơ in chữ rõ nét) để khán giả nhìn vào hiểu ngay lập tức.

#### D. Tối ưu hóa mô hình AI Video (Veo 3.1 Lite & NanoBanana 2)
- **Linh hoạt giữ chữ tĩnh tránh lỗi font (Veo 3.1 Lite I2V):** Vì mô hình sinh video thường bóp méo ký tự, đối với các phân cảnh có chữ tiếng Anh ở ảnh gốc, tại dòng prompt `[VIDEO]` tuyệt đối CẤM nhắc đến nội dung chữ và bắt buộc sử dụng cú máy tĩnh (`steady shot`) kèm câu lệnh khóa tĩnh lớp đồ họa chữ: `preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations`. Ngược lại, các phân cảnh không có chữ thì bắt buộc phải linh hoạt sử dụng các chuyển động camera động (zoom, pan, tilt, dolly) để tránh video bị đơn điệu.
- **Chống lệch mặt nhân vật & Chuẩn hóa Nhân vật theo Bối cảnh (Cast Sheet Rule - BẮT BUỘC):**
  * Nhân vật xuất hiện phải phù hợp với bối cảnh thể chế/công nghiệp quốc tế (Wall Street financial analysts, central bank officials, semiconductor fab engineers in cleanroom suits, port cargo supervisors, sovereign wealth fund directors).
  * Trong prompt động `[VIDEO]`, tuyệt đối cấm nhắc lại tên riêng của nhân vật thực tế (các doanh nhân, nhà sáng lập, chính khách, nhân vật lịch sử...). Hãy thay bằng danh từ chung (*the executive*, *the analyst*, *the chief engineer*, *the policymaker*) và câu lệnh bảo tồn diện mạo từ ảnh tham chiếu: `preserving facial features and the details of the reference image`.
- Định dạng camera: `shot on 35mm anamorphic lens`, `shallow depth of field`, `low-angle perspective`.
- Đảm bảo Exit Vector (góc máy thoát của cảnh trước) khớp với giây thứ 0 của cảnh tiếp theo để tránh jump cuts.
- Không đưa tên người thật/thương hiệu vào prompt video để tránh bộ lọc bảo mật. Thay thế bằng danh từ mô tả chung (ví dụ: `a central bank governor in formal attire`, `a prominent semiconductor executive`).

#### E. Tư duy Dịch chuyển Kịch bản sang Visual Prompt (Script-to-Prompt)
- **Quy trình Diễn giải Trực quan 5 Bước (Visual SOP):**
  1. *Giải mã Ngữ cảnh & Xác định Living Scene:* Dịch khái niệm trừu tượng thành thực thể, hành động vật lý thực tế ngoài đời.
  2. *Định vị Mỏ neo Trực quan:* Xác định rõ địa điểm bối cảnh, nhân vật nhất quán theo Cast Sheet, và vật thể thương hiệu/quốc gia.
  3. *Bố cục Điện ảnh & Ánh sáng Noir:* Sử dụng 60-30-10, chiaroscuro lighting, deep noir shadows, góc máy đa dạng.
  4. *Vật lý Chuyển động & Khóa Chữ:* Thiết kế camera và subject tương thích vật lý tự nhiên, khóa tĩnh tuyệt đối lớp chữ đồ họa overlay.
  5. *Hội đồng QA Độc lập (Audience-View Check):* Kiểm tra logic trực quan (có giải thích câu thoại không?), nhạy cảm văn hóa, và trùng lặp ý tưởng.
- **Tôn trọng Tên Thực thể & Thương hiệu Gốc (Brand Integrity Principle - BẮT BUỘC):** Tuyệt đối nghiêm cấm việc tự ý thay thế tên của các thực thể, tập đoàn, tổ chức tài chính hoặc chuỗi cung ứng có thật xuất hiện trong kịch bản (như NVIDIA, TSMC, ASML, BlackRock, Federal Reserve, Boeing, Intel, Apple...) thành các tên giả định. Phải bảo toàn 100% tên thương hiệu/thực thể trong kịch bản và đưa trực tiếp vào prompt để AI vẽ chuẩn xác.
- **Phá vỡ Lời nguyền Kiến thức (Curse of Knowledge):** Luôn đứng ở vị trí của khán giả xem lần đầu chưa biết kịch bản để thiết kế hình ảnh mang tính dẫn dắt trực quan cao. Nghiêm cấm lạm dụng các biểu tượng trừu tượng lặp lại nhàm chán (như cái cân) hoặc các chi tiết quá cô độc.
- **Trực quan hóa Thực tế (Internal to External):** Chuyển hóa các khái niệm trừu tượng, dữ liệu, chính sách, hoặc tính toán tài chính thành các hành động vật lý và bối cảnh sống động ngoài đời thực (ví dụ: thay vì vẽ mũi tên đồ thị rơi, hãy vẽ một sàn giao dịch tài chính London ngập tràn màn hình đỏ rực, các nhà giao dịch đứng chôn chân nhìn bảng điện tử).
- **Tư duy Đạo diễn Góc quay (Shot Director) & Khung prompt 3 lớp:** Viết prompt theo cấu trúc kẹp chặt chẽ: `[Subject & Action] + [Environment & Lighting] + [Camera & Style Specs]`.
- **Cấm Nhạy cảm Văn hóa & Tín ngưỡng:** Tuyệt đối cấm sử dụng các khung ảnh chân dung đơn độc xếp hàng trên bàn gỗ tối trong bóng tối mờ. Thay vào đó, hãy vẽ nhân vật đang làm việc, đi lại hoặc thảo luận tích cực trong môi trường thực tế (boardroom, trading floor, congressional hearing).
- **Cấm Phi logic Công nghệ (Quy tắc lò rèn):** Tuyệt đối cấm sử dụng hình ảnh lò rèn thủ công, tia lửa rực trong bối cảnh sản xuất công nghệ cao (phòng sạch bán dẫn, trung tâm dữ liệu AI, lắp ráp hàng không). Phải thay bằng thiết kế phòng sạch cleanroom class-1, cánh tay robot chính xác, màn hình quang khắc quang học.
- **Cấm Ẩn dụ Siêu thực Trừu tượng (Anti-Surrealism Rule):** Tuyệt đối cấm sử dụng các ẩn dụ mang tính siêu thực trừu tượng nằm ngoài trải nghiệm vật lý đời thường của người xem. Mọi bối cảnh phải là không gian vật lý thực tế (phòng họp Hội đồng quản trị, cảng container, nhà máy bán dẫn, tòa nhà quốc hội, trung tâm dữ liệu).
- **Phô diễn tầm vóc công trình vật lý:** Khi kịch bản nhắc đến công trình biểu tượng (cảng nước sâu, nhà máy fab tỷ đô, tuyến đường ống dẫn khí), prompt bắt buộc phải phác họa được quy mô hoành tráng của công trình đó dưới góc máy điện ảnh kết hợp với chữ overlay đồ họa tiếng Anh.
- **Cấm Tuyệt Đối Tóm Tắt Hoặc Lược Bỏ Nội Dung (Anti-Summarization Rule - BẮT BUỘC):** Khi chuyển dịch từ kịch bản gốc sang kịch bản visual trung gian (`chapter_XX_visual.md`), Agent tuyệt đối KHÔNG ĐƯỢC PHÉP tóm tắt, viết gọn lại hay lược bỏ bất kỳ ý tứ, mệnh đề hoặc câu văn nào từ kịch bản gốc. Mọi thông tin, số liệu, luận điểm của kịch bản gốc phải được bảo toàn đầy đủ 100%.

- **Giao thức Xử lý Câu dài & Tránh Tách câu Cơ học (Anti-Mechanical Splitting):**
  * Tuyệt đối cấm cắt đôi một câu thoại một cách cơ học theo số lượng từ nếu điều đó làm đứt gãy dòng chảy ngữ nghĩa hoặc cắt xén câu ở giữa chừng. Mỗi phân cảnh/prompt bắt buộc phải đi liền với một câu thoại trọn vẹn ngữ nghĩa để hình ảnh không bị vụn vặt, lắt nhắt.
  * Khi một câu thoại dài có nguy cơ làm voiceover vượt quá thời lượng an toàn 8 giây, bắt buộc viết lại câu thoại cho súc tích hơn hoặc tách câu ghép thành các câu đơn trọn ý trước khi tạo scene.

#### F. Quy trình Bảo toàn Mỏ neo Dữ liệu & Chống Bỏ sót Tài liệu (Data Vault Preservation Protocol - BẮT BUỘC)
- **Bước 1: Trích xuất Mỏ neo Dữ liệu (Data Anchor Extraction):** Trước khi bắt đầu viết bất kỳ chương kịch bản nào (`chapter_XX.md`), Agent bắt buộc phải thực hiện quét toàn bộ các tệp trong thư mục `research_vault/` và `02_research_synthesis.md` để lập danh sách **Mỏ neo Dữ liệu (Data Anchors)** gồm: Tên riêng doanh nghiệp/nhà cung cấp Tier-1, tên công nghệ/model sản phẩm, các số liệu tài chính/kinh tế thực chứng, và các căn cứ hồ sơ pháp lý/kiểm toán.
- **Bước 2: Cấm Thay thế Tên riêng bằng Từ chung mờ nhạt (Strict Technical Naming Rule):** Nghiêm cấm tuyệt đối việc tóm tắt hoặc thay thế các tên riêng chuyên môn (như ASML, TSMC, BlackRock, Nvidia, Thông tư/Nghị định SEC...) thành các danh từ chung mờ nhạt. Tên riêng và thông số kỹ thuật là "sức nặng chuyên môn" cốt lõi của kênh X-Economy, bắt buộc phải xuất hiện chính xác trong kịch bản thoại.
- **Bước 3: Giao thức Đối chiếu Mỏ neo trước khi Chốt (Data Anchor Audit Gate):** Trước khi bàn giao kịch bản cho User duyệt hoặc chuyển sang làm Visual Prompts, Agent bắt buộc phải chạy đối chiếu bảng Mỏ neo Dữ liệu với kịch bản các chương, đảm bảo không có bất kỳ dữ liệu thực chứng nào bị bỏ sót hay rớt lại trong kho nghiên cứu.

#### H. Quy trình Đối chiếu Đồng bộ Kịch bản - Prompt Tự động (Mandatory Visual Script & Prompt Sync Gate - BẮT BUỘC)
- **Nguyên tắc Đồng bộ 1-1 Tuyệt đối (Strict 1-to-1 Mapping):**
  * Tệp `chapter_XX_visual.md` (Kịch bản Visual) là **NGUỒN SỰ THẬT DUY NHẤT** về phân cảnh.
  * Mọi Scene ID trong `chapter_XX_visual.md` BẮT BUỘC phải có đúng 1 cặp prompt `[IMAGE]` và `[VIDEO]` tương ứng 100% trong `prompts_chapter_XX.txt`.
  * TUYỆT ĐỐI CẤM sinh prompt từ dàn ý cũ hoặc tệp thoại chưa qua công đoạn tách cảnh Visual.
- **Cổng kiểm tra tự động trước khi bấm Render (Pre-Render Automated Audit Gate):**
  * Trước khi bàn giao bất kỳ tệp prompt nào cho User hoặc đưa vào công cụ sinh ảnh/video, Agent **BẮT BUỘC phải chạy script Python kiểm tra đối chiếu tự động** giữa `chapter_XX_visual.md` và `prompts_chapter_XX.txt`.
  * Xác nhận 100% Scene ID khớp tuyệt đối và nội dung thị giác mô tả chính xác câu thoại.

#### I. Quy Trình Chuyển Hóa Kịch Bản Trung Gian & Giải Phẫu Cơ Học Trực Quan (Unified Intermediate Visual & Mechanical Explainer Protocol - BẮT BUỘC)
- **Triết Lý "Quy Trình Đồng Nhất Khép Kín":**
  * Kịch bản gốc (`chapter_XX.md`) $\rightarrow$ Kịch bản Visual Trung gian (`chapter_XX_visual.md`) $\rightarrow$ Tệp Prompts I2V (`prompts_chapter_XX.txt`) là **MỘT DÒNG CHẢY HỢP NHẤT KHÔNG THỂ TÁCH RỜI**.
- **Quy Tắc Mô Hình Giải Phẫu Cơ Học 3 Tầng (3-Tier Mechanical Anatomy):**
  * Trường `[BỐI CẢNH]` trong kịch bản trung gian bóc tách rõ 3 tầng vật lý:
    1. *Tầng 1 - Đế Cố Định (Anchor/Base):* Tòa nhà trụ sở, phòng họp Fed, nhà máy bán dẫn, cảng biển nước sâu.
    2. *Tầng 2 - Bộ Truyền Động / Cơ Chế Chủ Lực (Actuators & Mechanisms):* Hệ thống buồng chân không quang khắc EUV, bảng cân đối kế toán số hóa, mạng lưới máy chủ trung tâm dữ liệu.
    3. *Tầng 3 - Khối Tác Động & Hướng Lực (Payload & Motion Vector):* Dòng chảy dữ liệu số, tấm wafer silicon đang được xử lý, tàu container đang rời cảng.
- **Quy Tắc Nhãn Chú Thích Kỹ Thuật Đích Danh (Engineering Technical Callouts):**
  * Khai báo nhãn chú thích tiếng Anh 3D trực diện ở trường `[TEXT OVERLAY]` và đưa vào prompt `[IMAGE]` (ví dụ: `"EUV LITHOGRAPHY SYSTEM"`, `"SUBSEA GAS PIPELINE"`, `"FEDERAL RESERVE BALANCE SHEET"`).
  * Ở dòng `[VIDEO]`, luôn khóa tĩnh lớp nhãn (`preserving all technical callout labels and static graphic layers...`).

#### J. Giao Thức Rà Soát Lỗi Tự Động & Sửa Chữa Trước Khi Bàn Giao (Zero-Defect Delivery Rule)
- Sau khi tạo xong Visual Script hoặc Prompts, tự rà soát qua các cổng kiểm tra, sửa trực tiếp các lỗi tồn đọng trước khi bàn giao.



## 🎬 QUY ĐỊNH BẮT BUỘC: SẢN XUẤT VIDEO TỰ ĐỘNG (PHA 14 — VIDEOCORE BATCH PRODUCTION)

> ⚠️ **BẮT BUỘC TUÂN THỦ KHI SẢN XUẤT VIDEO CHO X-ECONOMY:**
> 1. **Cơ chế 1-Chạm Bản Địa:** Khi User yêu cầu tạo video hoặc gõ `/generate_videos`, Agent thực thi trực tiếp từ thư mục dự án:
>    ```bash
>    python3 scripts/produce_episode_videos.py --episode <slug>
>    ```
> 2. **Hạ tầng Dùng Chung VideoCore:**
>    - Toàn bộ engine điều phối nằm tại `VideoCore` và đã được liên kết mềm (symlink) vào `scripts/` và `.agents/skills/batch_video_generator`.
>    - Tự động quét diff các cảnh thiếu, tự nạp ảnh tham chiếu `@avatar.jpg` từ `episodes/<slug>/ref_images/`, kết nối Chrome port 9222, kích hoạt watchdog 300s, và tự động chuyển file `.mp4` về `episodes/<slug>/videos/`.
> 3. **Kiểm toán Hoàn tất:** Dùng `python3 scripts/check_video_progress.py --episode <slug>` để xác nhận 100% video hợp lệ.

## 🎬 QUY ĐỊNH BẮT BUỘC: QUY TRÌNH I2V+ (CHUẨN ĐẠO DIỄN ĐIỆN ẢNH ĐA THỨC — MULTIMODAL HYBRID PIPELINE)

> ⚠️ **BẮT BUỘC TUÂN THỦ KHI KÍCH HOẠT NHÁNH I2V+ (PHA 12+A, 12+B, 12+C):**
> 1. **Khóa Kỹ Năng Độc Quyền (Skill Isolation Mandate):**
>    - Khi thực thi nhánh I2V+, Agent **BẮT BUỘC** kích hoạt duy nhất kỹ năng: **`.agents/skills/visual_prompter_plus/SKILL.md`**.
>    - Tuyệt đối CẤM nạp hoặc sử dụng kỹ năng `visual_prompter/SKILL.md` (vốn chỉ dành cho I2V cổ điển 100% video vẽ AI).
>
> 2. **Bãi Bỏ Hạn Ngạch Cơ Học $\to$ Bản Thể Luận 4 Trụ Cột Nhận Thức (No Arbitrary Percentages):**
>    - Tuyệt đối KHÔNG phân chia tỷ lệ % số học máy móc. Mọi phân cảnh được phân loại dựa trên **Nhiệm vụ Nhận thức & Trải nghiệm Cảm xúc** của khán giả:
>      * **`B_ROLL_REAL` (Mỏ neo Niềm tin & Tư liệu Quốc tế Thực chứng):** Bắt buộc cho các sự kiện tài chính/địa chính trị thật (họp báo Fed, phiên điều trần Quốc hội Mỹ, hội nghị thượng đỉnh), sàn giao dịch chứng khoán (NYSE, LSE), bến cảng container (Los Angeles, Rotterdam) và dây chuyền lắp ráp công nghiệp thật (Boeing, TSMC, xe điện). Mang lại tính bất khả phủ nhận và sự thấu cảm da thịt (`Visceral Real-World Grounding`).
>      * **`FORENSIC_CALLOUT` (Mỏ neo Bằng chứng Hồ sơ & Báo chí Thực chứng):** Bắt buộc khi trích dẫn báo chí quốc tế chính thống Hạng A (WSJ, Financial Times, Bloomberg, Reuters, The Economist), hồ sơ kiểm toán SEC Form 10-K, văn kiện đạo luật (CHIPS Act, Dodd-Frank, Fed FOMC Statement), phán quyết tư pháp (DOJ, SEC, FTC). Mang lại cú đấm thực tế không thể chối cãi (`The Evidentiary Smoking Gun`).
>      * **`INFOGRAPHIC_DATA` (Kính lúp Trí tuệ & Cấu trúc Vô hình):** Bắt buộc cho đối kháng định lượng (so sánh đòn bẩy D/E, Capex AI vs Doanh thu), chu kỳ vĩ mô (đảo ngược đường cong lợi suất, chu kỳ nợ dài hạn) và bản đồ chuỗi cung ứng/điểm nghẽn địa chính trị độc quyền. Mang lại cú khai phóng nhận thức (`The "Aha!" Moment`).
>      * **`VEO_AI` (Linh hồn Thẩm mỹ & Hero Shots Điện ảnh):** Tái hiện các không gian chiến lược kín không có camera thật (phòng họp Hội đồng quản trị kín, phòng điều hành quỹ đầu tư quốc gia), bối cảnh công nghệ cao (kỹ sư trong phòng sạch quang khắc EUV) hoặc đại cảnh trung tâm dữ liệu AI/cảng biển sử thi với tông màu ấm ngà kem `#FAF7EE` và slate `#1E293B`. Mang lại sức nặng điện ảnh và sự choáng ngợp sử thi (`Epic Cinematic Awe`).
>
> 3. **Tôn Chỉ Zero-Metaphor — Tuyệt Đối Cấm Ẩn Dụ Trừu Tượng Hóa & Lỗi Thời Niên Đại (Zero-Metaphor Mandate):**
>    - ⛔ **CẤM TUYỆT ĐỐI ẩn dụ hóa siêu thực/trừu tượng:** Cấm các biểu tượng vô nghĩa như bánh răng nợ công khổng lồ quay giữa hư không, cổng đá nguyên khối bán dẫn, bàn cờ bay lơ lửng, chuỗi xoắn ốc DNA phát sáng trên đồng ruộng, quả cầu năng lượng, cái cân công lý bay trên trời, bàn tay sắt điều khiển con rối.
>    - ⛔ **CẤM đưa thực thể sai lệch niên đại lịch sử hoặc hạ cấp hoàn cảnh:** Không đưa đèn dầu le lói, công cụ cổ xưa, lò rèn thủ công vào bối cảnh tài chính, công nghệ cao hay nhà xưởng hiện đại thế kỷ 21.
>    - 🎯 **Quy tắc Hiện thực Vật lý Dễ Hiểu trong 0.5s:** Mọi cảnh AI bắt buộc phải vẽ hiện thực vật lý cụ thể, chân thực, chuẩn xác niên đại lịch sử, bám sát hành động của con người hoặc máy móc thực tế (nhà phân tích ngồi trước dàn màn hình Bloomberg Terminal, kỹ sư trong phòng sạch cleanroom kiểm tra tấm wafer quang khắc, lãnh đạo cấp cao họp bàn quanh hồ sơ in chữ rõ nét) để khán giả nhìn vào hiểu ngay lập tức.
>
> 4. **Vùng Cấm Thép Của Veo AI & Rào Cản Báo Chí (The Hard Redlines):**
>    - ⛔ **CẤM** dùng Veo vẽ lại các cảnh đời thường có sẵn ngoài thực tế (xe container chạy trên cao tốc, sàn chứng khoán thông thường, kho hàng $\to$ dùng `B_ROLL_REAL`).
>    - ⛔ **CẤM** dùng Veo vẽ đồ thị, núi nợ, núi tiền, cán cân hoạt hình ($\to$ dùng `INFOGRAPHIC_DATA`).
>    - ⛔ **CẤM** ghi tên người thật trong dòng `[VIDEO]` (chỉ dùng Pure Optical Camera Motion).
>    - ⛔ **CẤM ĐƯA ẢNH BÁO CHÍ VÀO VEO AI:** Veo 3.1 Lite làm biến dạng/nát chữ tiếng Anh và tiếng Việt, không gạch chân chính xác theo nhịp thoại và gây lãng phí chi phí. Toàn bộ `FORENSIC_CALLOUT` phải dùng Python Motion Engine tiền kết xuất ra MP4 sắc nét 1080p 60fps.
>
> 5. **Quy Chuẩn Bằng Chứng Báo Chí & Pháp Lý Bản Quyền Sạch (US Fair Use 17 U.S.C. § 107 & Điều 25 Luật SHTT):**
>    - Trích đoạn micro-quotation 3.0s – 5.5s phục vụ nghiên cứu khoa học, phân tích kinh tế và bình luận thời sự, giữ nguyên măng-sét báo uy tín (WSJ, FT, Bloomberg, Reuters, The Economist...).
>    - ⛔ **CẤM DÍNH BẪY BẢN QUYỀN ẢNH PHÓNG SỰ:** Khi trích xuất bài báo, **CHỈ LẤY PHẦN TEXT (Tiêu đề, sapo, số liệu)**. Tuyệt đối làm mờ (blur/mask) hoặc crop bỏ toàn bộ ảnh chụp phóng sự của phóng viên để triệt tiêu hoàn toàn khiếu nại bản quyền hình ảnh.
>    - Hiệu ứng thị giác: Nét gạch chân điện ảnh (Cinematic Underline) hoặc khung viền vàng hổ phách/đỏ bo chữ (`#F59E0B` / `#FF7043` / `#EF5350`), kết hợp âm thanh lướt giấy (`paper_slide.wav`) hoặc click nhẹ (`minimal_click.wav`).
>
> 6. **Bốn Nguyên Tắc Thép Cho Footage B-Roll Fair Use:**
>    - ① *Mute Absolute:* Tước bỏ 100% audio gốc (`-an`).
>    - ② *Micro-Cut:* Độ dài mỗi clip chỉ từ 3.0s – 5.5s (không bao giờ quá 6s).
>    - ③ *Pixel Hash Breaking:* Scale 104% và crop nhẹ 16:9 để bẻ gãy Content ID.
>    - ④ *On-Screen Attribution:* Dán nhãn nguồn trích dẫn minh bạch góc màn hình (`Source: Bloomberg / CNBC / C-SPAN / Reuters / Federal Reserve...`).
>
> 7. **Cấu Trúc Xuất Bản 4 Đường Ray Pha 12+C:**
>    - Cảnh `VEO_AI` $\to$ `prompts_chapter_XX_veo.txt` (nạp Flow Tool Builder).
>    - Cảnh `B_ROLL_REAL` $\to$ `broll_manifest_chapter_XX.json` (nạp `the_footage_hunter`).
>    - Cảnh `INFOGRAPHIC_DATA` $\to$ `infographics_chapter_XX.json` (nạp AutoCapCut / Motion Graphics).
>    - Cảnh `FORENSIC_CALLOUT` $\to$ `forensic_manifest_chapter_XX.json` (nạp `render_forensic_engine.py` tiền kết xuất thành video MP4 sắc nét 100%).
