# X-Economics Workspace Rules & Persisted Learnings

## 📌 Canonical Channel DNA & Social Assets (MANDATORY ACCURACY)
- **Official Channel Name:** X-Economics
- **YouTube Official Channel URL Handle:** `https://www.youtube.com/@X-Economics-b9x`
- **Editorial DNA:** Investigative Global Macroeconomics, Geopolitics, Supply Chains & Industrial Strategy.
- **Thematic Scope:** Applying the signature *Góc Nhìn* investigative & systemic lens to the **United States, the United Kingdom, and Global Geoeconomics** (Housing market distortions, private equity financialization, infrastructure decay, semiconductor chokepoints, productivity traps).
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

## 🛑 QUY ĐỊNH BẮT BUỘC: GHI NHẬN & GIÁM SÁT KHUYẾT TẬT LLM (LLM DEFECT LOGGING MANDATE)

> ⚠️ **BẮT BUỘC TUÂN THỦ 100% TRONG TOÀN BỘ QUÁ TRÌNH TẠO KỊCH BẢN:**
> 1. **Sổ Cái Khuyết Tật Tập (`episodes/[slug]/llm_error_log.md`):**
>    - Mỗi episode bắt buộc phải duy trì tệp `llm_error_log.md` theo cấu trúc chuẩn từ `02_templates/llm_error_log_template.md`.
>    - Toàn bộ các lỗi phát sinh từ lúc khởi tạo đến khi ra kịch bản cuối cùng phải được ghi nhận đầy đủ, tuyệt đối cấm âm thầm sửa lỗi bỏ qua việc ghi log.
> 2. **Hệ Thống Phân Loại 6 Nhóm Khuyết Tật:**
>    - `[FORMAT_SYNTAX]`: Lỗi câu >150 ký tự, dấu em-dash (`—`), rò rỉ scaffolding `[BLOCK 1]`, lộ prompt metadata.
>    - `[VOCABULARY_TONE]`: Dính từ cấm AI (`anti_ai_isms.md`), trôi dạt văn phong hàn lâm/báo cáo, sến sẩm hoặc giật gân.
>    - `[DATA_GROUNDING]`: Ảo giác số liệu tài chính/kinh tế, trích dẫn sai nguồn, vi phạm ZUI, nhầm lẫn thực thể.
>    - `[LOGIC_REASONING]`: Ngụy biện bù nhìn rơm (Strawman), cắt xén cơ chế First-Principles, tư duy ngăn tủ ("And Then"), giấu bài về cuối.
>    - `[PROCESS_PROTOCOL]`: Bỏ qua Pre-Flight Log, vi phạm sandbox, quên nạp persona, dính lỗi lặp lại (Forbidden Echoes).
>    - `[HUMAN_REJECTION]`: Người dùng từ chối bản nháp, yêu cầu đổi framing, đổi ví dụ hoặc viết lại hoàn toàn.
> 3. **Cơ Chế Kích Hoạt Ghi Log Bắt Buộc:**
>    - Khi Post-Write Audit (Pha 7) hoặc Compliance Council (Pha 10 & 11) phát hiện lỗi $\to$ Ghi ngay vào `llm_error_log.md` trước khi sửa.
>    - Khi Người dùng phản hồi yêu cầu chỉnh sửa (`/revise_chapter` hoặc chat feedback) $\to$ Bắt buộc tạo 1 entry `[HUMAN_REJECTION]` ghi rõ lý do không đạt của bản trước.
> 4. **Vòng Lặp Cải Tiến Liên Tục (Continuous Improvement):**
>    - Dữ liệu từ `llm_error_log.md` được tổng kết vào Section 6.1 của `postmortem.md` (Pha 16) và chuyển giao vào Sổ cái trung tâm `01_management/llm_error_analytics.md` để định kỳ vá System Prompts và Skills.

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
>    - Bức tranh toàn cảnh là **BẢN ĐỒ ĐỊA HÌNH CỦA HIỆN THỰC KHÁCH QUAN (The Map of Reality)**: Mô tả bản chất của vùng đất đề tài (kinh tế, xã hội, điều tra, nhân vật hay công nghệ), các chủ thể, động lực sinh tồn, quy luật vận hành và hệ thống bằng chứng thực tế. Nó tồn tại khách quan, độc lập với việc kể chuyện.
>    - Dàn ý kịch bản (Outline ở Pha 4) là **LỘ TRÌNH DẪN ĐƯỜNG CHỦ QUAN (The Guided Tour)**: Quyết định số trạm dừng (số chương), nhịp điệu, cảm xúc và thời lượng (8m, 20m hay 45m).
> 2. **Cấu trúc 4 Tầng Tư Duy Phổ Quát (Universal 4-Tier Blueprint — Áp dụng cho MỌI thể loại đề tài):**
>    - **Tầng 1 (Meta-Instructions & Redlines):** Khối YAML/JSON định vị vai trò quan sát/điều tra độc lập (Editorial Noir DNA), rào cản chính luận, blacklist từ cấm nhạy cảm chính trị, và chính sách khóa cứng số liệu mỏ neo thực chứng bất biến.
>    - **Tầng 2 (Macro Landscape & Systemic Forces — Bản Đồ Không Gian & Các Lực Lượng):** Sơ đồ ASCII toàn cảnh định vị không gian bàn cờ: Các chủ thể tham gia (Nhà nước, doanh nghiệp, người dân, dòng vốn, các nhóm lợi ích...), động lực sinh tồn/kinh tế/chính trị cốt lõi (Incentives), các dòng chảy chủ đạo (dòng tiền, quyền lực, thông tin, hàng hóa) và tương quan lực lượng.
>    - **Tầng 3 (Underlying Mechanics & Central Paradoxes — Quy Luật Vận Hành & Nghịch Lý Cốt Lõi):** Giải phẫu các mắt xích nhân quả gốc rễ (Root Causes & Causal Chains) và khoảng cách giữa kỳ vọng/bề mặt vs thực tế/bản chất. Xác định điểm gãy cấu trúc hoặc quy luật khách quan chi phối toàn bộ đề tài (quy luật chi phí, rào cản thể chế, bẫy cơ cấu, động lực tâm lý xã hội...).
>    - **Tầng 4 (Immutable Ground-Truth Data Vault — Sổ Cái Bằng Chứng Thực Chứng Bất Biến):** Bảng tra cứu mã số liệu, văn bản pháp quy, mốc thời gian, hồ sơ kiểm toán (`DATA-01` đến `DATA-XX`) đối chiếu 1-1 với nguồn tài liệu gốc trong `research_vault/`. Đây là "mỏ than dữ liệu sạch" bất biến cung cấp nhiên liệu cho toàn bộ pipeline hạ nguồn xúc dùng.
> 3. 🛑 **VÙNG CẤM TUYỆT ĐỐI CỦA PHA 2.5 (HARD REDLINE — CHỐNG ÔM ĐỒM & CHỐNG TIỀN ĐỊNH DÀN Ý):**
>    - **TUYỆT ĐỐI CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản nào:** `CH01`, `CHXX`, `Chương`, `Hồi`, `Hook`, `Scene`, `Voiceover Tone`, `Narrative Bridge`, `Harvest`, `Seed`.
>    - **TUYỆT ĐỐI CẤM chia chương trước Pha 4:** Việc phân chia số chương, thời lượng, nhịp điệu, cấu trúc hồi, và phân bổ quota dữ liệu vào từng chương là **ĐẶC QUYỀN ĐỘC TÔN của Pha 4 (Master Outline Engine do `the_master_script_dramaturg` phụ trách)**.
>    - **TUYỆT ĐỐI CẤM may đo rập khuôn:** Không gượng ép mọi đề tài vào một khuôn mẫu cứng nhắc (như ép phải có 3-4 trận địa hay ép phải có 7 chương). Mỗi đề tài được quyền thể hiện cơ chế và nghịch lý theo đúng bản chất hình học tự nhiên của nó (đối xứng, chu kỳ luẩn quẩn, mạng lưới nhện, hay dòng chảy thác lũ).
>    - **Chế tài vi phạm:** Mọi tệp `00_Global_Vision_Synthesis.md` xuất hiện cấu trúc chia chương kịch bản đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** (làm ô nhiễm ngữ cảnh, gây thiên kiến trói tay chuyên gia dàn ý) và sẽ bị hủy bỏ để làm lại.

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
>         Đối với các tệp phân tích, chiến lược, brief, outline (`01` đến `08`, `00_Global_Vision_Synthesis.md`, `09_narrative_state_tracker.md`), BẮT BUỘC chèn khối Metadata ở đầu file:
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
| "khởi tạo", "init episode", "bắt đầu episode mới", "đề tài mới", "đánh giá đề tài", "chọn chủ đề" | **Pha 1:** `01_topic_qualification.md` | `.agents/personas/the_macro_strategist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/strategy_council/SKILL.md` | Ý tưởng của User, tài liệu phác thảo ban đầu, hạt giống tin tức | `/init_episode` |
| "research", "deep research", "nghiên cứu", "nghiên cứu sâu", "tìm data", "đào dữ liệu", "nạp nguồn" | **Pha 2:** `02_research_map.md` & `02_research_synthesis.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_industrial_economist.md` | `.agents/skills/deep_researcher/SKILL.md`<br>+ `.agents/skills/notebooklm/SKILL.md` | `episodes/[slug]/01_topic_qualification.md`, Master Notebook ID (`.notebook_id`) | `/deep_research`<br>*(BypassSandbox: true, --mode deep)* |
| "quy hoạch tầm nhìn", "bức tranh tổng thể", "global vision", "tầm nhìn toàn cảnh", "synthesis", "bức tranh 4 tầng" | **Pha 2.5:** `vault/00_Global_Vision_Synthesis.md` | `.agents/personas/the_macro_strategist.md`<br>+ `.agents/personas/the_editorial_strategist.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/01_topic_qualification.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/research_vault/` | `/build_global_vision`<br>*(Bản đồ Địa hình Hiện thực 4 Tầng — CẤM chia chương)* |
| "viết brief", "lập chiến lược", "chiến lược", "strategy brief", "tạo brief", "xây brief" | **Pha 3:** `03_brief.md` | `.agents/personas/the_editorial_strategist.md`<br>+ `.agents/personas/the_policy_analyst.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/vault/00_Global_Vision_Synthesis.md`<br>`episodes/[slug]/01_topic_qualification.md`<br>`episodes/[slug]/02_research_synthesis.md` | `/build_brief` |
| "viết outline", "dàn ý", "xây cấu trúc", "master outline", "lập dàn ý", "cấu trúc tập" | **Pha 4:** `07_outline.md` | `.agents/personas/the_dialectic_architect.md`<br>+ `.agents/personas/the_industrial_economist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/vault/00_Global_Vision_Synthesis.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/02_research_synthesis.md` | `/build_outline`<br>*(Quy trình 5 Trạm Master Outline Forge & Lan can Co giãn)* |
| "viết hook", "mở đầu video", "hook lab", "tạo hook", "chọn hook", "làm hook" | **Pha 5:** `04_hook_pack.md` | `.agents/personas/the_viral_alchemist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/hook_engine/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/vault/00_Global_Vision_Synthesis.md` | `/hook_lab`<br>*(May đo 3-5 Hooks bám Dàn ý)* |
| "viết chapter brief", "brief các chương", "lập brief từng chương", "khởi tạo nst", "tạo sổ cái tự sự" | **Pha 6:** `08_chapter_briefs.md` & `09_narrative_state_tracker.md` | `.agents/personas/the_narrative_director.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/04_hook_pack.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/vault/00_Global_Vision_Synthesis.md` | `/build_outline`<br>*(16 Trường Chuẩn hoá & NST)* |
| "viết chương", "viết chapter", "viết tiếp", "viết kịch bản", "viết tập" | **Pha 7:** `chapter_XX.md` | Persona chỉ định tại Chapter Brief<br>+ Khóa Khẩu ngữ Oral Voice DNA | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/08_chapter_briefs.md` (Brief CH_XX)<br>`episodes/[slug]/vault/00_Global_Vision_Synthesis.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/09_narrative_state_tracker.md`<br>Toàn bộ clean script `chapter_01.md` đến `chapter_N-1.md` | `/write_chapter`<br>*(Bắt buộc in Claim Ledger ra chat)* |
| "sửa chương", "revise", "chỉnh sửa chapter", "sửa kịch bản chương" | **Hậu Pha 7:** `chapter_XX.md` | `.agents/personas/the_critical_auditor.md`<br>+ Persona tác giả chương | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/chapter_XX.md`<br>`episodes/[slug]/08_chapter_briefs.md`<br>Feedback từ User / Auditor | `/revise_chapter` |
| "gộp voiceover", "merge", "gộp kịch bản", "gộp toàn bộ chương", "voiceover hoàn chỉnh" | **Pha 8:** `voiceover.md` | `.agents/personas/the_quality_czar.md` | `.agents/skills/chapter_writer/SKILL.md` | Toàn bộ `chapter_01.md` đến `chapter_XX.md`<br>`episodes/[slug]/04_hook_pack.md` (Selected Hook) | `/merge_voiceover` |
| "kiểm toán retention", "audit nhịp", "retention bridge audit", "soi điểm rơi", "soi giữ chân" | **Pha 9:** `retention_bridge_audit.md` | `.agents/personas/the_critical_auditor.md` | `.agents/skills/retention_bridge_audit/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/07_outline.md` | `retention_bridge_audit` SKILL |
| "kiểm tra", "QA", "review kịch bản", "compliance", "audit chính sách", "soi lỗi chính trị/pháp lý" | **Pha 10 & 11:** `10_compliance_report.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_critical_auditor.md`<br>+ `.agents/personas/the_editorial_strategist.md` | `.agents/skills/compliance_council/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/vault/00_Global_Vision_Synthesis.md`<br>`episodes/[slug]/03_brief.md` | `compliance_council` SKILL<br>*(5 International Safety Gates & Term-Breath Debate)* |
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

Kênh Góc Nhìn Podcast định vị là kênh phân tích kinh tế - xã hội - chính sách chuyên sâu (Cinematic Editorial Noir). Khán giả của kênh là những người thông minh, có học thức và tư duy phản biện. 
**Người viết kịch bản không hành xử như một chiếc máy chắp vá từ ngữ (fix code / fix case), mà phải vận hành bằng TƯ DUY BIÊN TẬP NGUYÊN BẢN (First-Principles Editorial Mindset).** Mọi kịch bản phải tuân thủ 4 trụ cột tư duy cốt lõi sau:

### 1. Tư Duy Bản Chất & Cơ Chế Thực Chứng (Substance & Mechanism First)
- **Nắm chắc cơ chế trước khi hạ bút:** Trước khi viết bất kỳ nhận định nào về chính sách, thuế quan, tài chính hay công nghệ, người viết phải tự trả lời được bản chất vận hành:
  * *Chủ thể và không gian quy định là gì?* (Phân định rạch ròi giữa yếu tố pháp lý lãnh thổ địa lý với yếu tố con người/quốc tịch; không được đánh đồng khái niệm).
  * *Dòng tiền và quyền tài sản dịch chuyển như thế nào?* (Hiểu rõ bản chất kế toán, chế tài hoàn thuế, truy thu, khấu hao hay xử lý tài sản bảo đảm; không dùng ngôn từ thông tục làm biến dạng nghĩa vụ pháp lý).
  * *Động lực kinh tế (Incentives) thực sự của các bên là gì?* (Mọi hành vi kinh doanh phải được giải thích bằng bài toán chi phí, rủi ro, thị phần và điểm hòa vốn, tuyệt đối không quy kết cảm tính hay đạo đức hóa).

### 2. Tư Duy Hình Tượng Hóa Chuẩn Xác (Precision Metaphor)
- Kịch bản viết cho người bình thường nghe hiểu bằng tai qua video, do đó việc sử dụng hình ảnh đời thường và phép loại suy (Metaphor) là bắt buộc.
- **Tuy nhiên, hình tượng hóa chỉ để LÀM SÁNG TỎ CƠ CHẾ, không được BÓP MÉO BẢN CHẤT:** Một phép ẩn dụ xuất sắc phải phản ánh đúng logic vận hành thực tế. Nếu một phép so sánh làm khán giả hiểu sai về cách thức hoạt động của luật pháp, kinh tế hay kỹ thuật, đó là một phép so sánh tồi và phá hủy uy tín của kênh.

### 3. Hợp Đồng Nhận Thức & Dòng Chảy Tuyến Tính (Narrative Contract & Cognitive Flow)
- Người xem tiếp nhận video theo trục thời gian một chiều (Linear Time). Phần mở đầu (Hook) chính là một **Hợp đồng nhận thức (Cognitive Contract)** ký kết với khán giả: Mọi xung đột kịch tính, câu hỏi lớn, bí ẩn hay nghịch lý được gieo ở Hook là lời hứa mà người viết bắt buộc phải giải tỏa ngay trong các phân đoạn tiếp theo.
- Tuyệt đối không được "bỏ rơi" câu hỏi của khán giả để nói sang các chủ đề lan man khác. Mạch truyện phải giải quyết từng nút thắt theo đúng dòng tâm lý tự nhiên của người nghe: *Nêu nghịch lý ➔ Giải mã nguyên nhân trực tiếp ➔ Đào sâu cơ chế cốt lõi ➔ Mở rộng tác động hệ thống ➔ Đúc kết bài học.*

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

Đây là tài liệu đúc kết tư duy trực quan và hướng dẫn viết prompt mẫu cho các chủ đề phân tích xã hội, góc nhìn chuyên gia vĩ mô và công nghệ. Tài liệu này đóng vai trò **gợi ý tư duy nghệ thuật và tham chiếu thiết kế**, không phải quy chuẩn cứng (hardcode) áp dụng cho mọi thể loại. Mỗi tập phim sẽ được tiếp cận theo cách riêng biệt tùy bối cảnh.

### 1. Triết lý thiết kế "Cinematic Editorial Noir"
- **Minh họa báo chí cao cấp (Editorial Illustration):** Hình ảnh hướng tới phong cách bán thực tế (semi-realistic), sắc sảo, tối giản và nghệ thuật như các trang minh họa phóng sự chuyên sâu của các tờ báo lớn. Tránh hoàn toàn cảm giác hoạt hình (cartoon) trẻ con hay nét vẽ thô sơ.
- **BẮT BUỘC FRONT-LOAD PHONG CÁCH 2D BÁO CHÍ (2D Art Medium Front-Loading - BẮT BUỘC):** 100% prompt ảnh tĩnh `[IMAGE]` bắt buộc phải bắt đầu bằng cụm từ cố định: `A 2D cinematic editorial noir illustration of [Chủ thể], minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures...`. Tuyệt đối CẤM mở đầu bằng các từ chỉ góc máy chụp ảnh như `A photo of...`, `A wide shot of...`, `A low-angle shot of...`, `An exterior shot of...` (khiến AI hiểu lầm là ảnh chụp thật photorealism).
- **Tính liên kết và logic vật lý:** Mọi chuyển động camera và sắp đặt cảnh quan phải bám sát ngữ cảnh thực tế của câu chuyện, có tính liên kết không gian (Background Anchoring) chặt chẽ giữa cảnh trước và cảnh sau.

### 2. Các nguyên tắc thiết kế gợi ý khi triển khai

#### A. Phối màu 60-30-10 & Thích ứng Chủ đề
- **60% Chủ đạo (Nền/Bóng tối):** Gam màu tối ấm áp hoặc trầm tính như `dark warm charcoal (#1A1A1A)`, `muted dark olive green (#1E2522)` hoặc `deep indigo gradient`.
- **30% Bổ trợ (Nét vẽ/Chủ thể):** Nét vẽ màu kem ấm `warm cream (#FFFDF0) outlines` hoặc chi tiết bạc để tạo cảm giác đồ họa hữu cơ.
- **10% Điểm nhấn (Dẫn mắt):** Chỉ dùng một màu nhấn duy nhất để làm bật lên tiêu điểm:
  *   *Xã hội/Đời sống/Con người:* Cam đất `glowing terracotta orange (#FF7043)`.
  *   *Giải pháp/Điểm sáng:* Xanh ngọc `glowing turquoise (#26A69A)` hoặc xanh xô thơm `electric sage green (#81C784)`.
  *   *Khủng hoảng/Cảnh báo:* Đỏ san hô `glowing crimson coral red (#EF5350)`.
- **Thích ứng theo Tuyến:**
  *   *Tuyến Xã hội Việt Nam:* Sử dụng tông màu ấm organic, chi tiết văn hóa thuần Việt (`culturally authentic Vietnamese elements, warm organic tones`).
  *   *Tuyến Công nghệ Toàn cầu:* Sử dụng phong cách Futuristic Cyber-Minimalism với nền tối sâu, dòng chảy dữ liệu AI, robot hoặc không gian số tối giản.

#### B. Thiết kế chữ trên màn hình (Cinema Typography Layout)
- **Tọa độ thẳng song song:** Chữ overlay luôn facing camera trực diện, song song với ống kính (`facing the camera directly, perfectly horizontal and straight 3D text overlay`). CẤM viết chữ nghiêng (Italic) hoặc chữ uốn méo theo phối cảnh 3D của môi trường.
- **Ngôn ngữ hiển thị:** Đối với kênh tiếng Anh X-Economics, toàn bộ text overlays trên màn hình PHẢI HOÀN TOÀN BẰNG TIẾNG ANH (in ALL CAPS hoặc Title Case ngắn gọn, ví dụ: `SUPPLY CHAIN CRITICAL FAILURE`, `THE \$1.2T DEFICIT`, `SILICON CHOKEPOINT`). Chỉ định rõ kết cấu chữ cứng cáp, bóng đổ đen dày (`heavy black drop shadow`) trên nền không gian âm sạch.
- **Quy tắc Chọn lọc Text Overlay (Selective Typography Rule - BẮT BUỘC KHÔNG ĐƯỢC NHẬP SAI):** Tuyệt đối **CẤM chèn Text Overlay trên 100% mọi phân cảnh**. Chữ overlay chỉ được phép xuất hiện tại **~20% - 25% các phân cảnh QUAN TRỌNG NHẤT** (như mốc thời gian lịch sử, thông số kỹ thuật/tài chính cốt lõi, danh hiệu hoặc tuyên bố mang tính bước ngoặt). Với **75% - 80% các phân cảnh còn lại**, bắt buộc phải để `[TEXT OVERLAY]: None` (hoặc không nhắc đến text overlay trong prompt ảnh) để trả lại không gian mỹ thuật đồ họa cho NanoBanana 2 và cho phép mô hình Veo 3.1 chuyển động ống kính linh hoạt (`slow push-in dolly shot`, `panning shot`, `tracking shot`, `tilt-up shot`), tránh làm video bị rác chữ và đơn điệu.

#### B1. Quy Chuẩn An Ninh Chủ Quyền & Bản Đồ Số Hóa (Sovereignty & Clean Map Protocol - BẮT BUỘC)
- **Tuyệt đối CẤM vẽ bản đồ ranh giới lãnh thổ / biên giới địa chính trị chi tiết:** Đặc biệt là khu vực Biển Đông, Đông Nam Á và Châu Á, nhằm ngăn chặn triệt để 100% nguy cơ mô hình AI tự vẽ hoặc áp đặt hình ảnh phi pháp ("đường lưỡi bò" / "nine-dash line").
- **100% Bản đồ bắt buộc phải là BẢN ĐỒ KINH TẾ & CÔNG NGHỆ TRỪU TƯỢNG (Abstract Economic & Tech Network Nodes):**
  * Chỉ sử dụng mạng lưới các điểm nút số hóa (`abstract digital cyber grid with illuminated financial/tech nodes`) kết nối bằng các tia sáng/luồng truyền dữ liệu số (`radiant data transfer vectors`).
  * Chỉ định vị các điểm nút tài chính/kinh tế/công nghệ/công nghiệp trọng điểm trong kịch bản bằng các khối biểu tượng hình học và mũi tên luồng tiền/hàng hóa/nhân tài.
  * TUYỆT ĐỐI KHÔNG vẽ đường biên giới lãnh thổ, không vẽ các đường phân định biển.

#### C. Ẩn dụ Xã hội và Hệ thống (Deep Social Metaphor)
- Thay thế các hình ảnh mô tả nghĩa đen thô sơ bằng các ẩn dụ hình học/vật lý sâu sắc: Kẹt xe biến thành dòng chảy hồng cầu nghẹt thở trong huyết quản; Vòng lặp công sở biến thành cầu thang gỗ Escher vô tận; Áp lực thi cử biến thành những cổng vòm đá khổng lồ ghép từ các bài thi điểm đỏ.

#### D. Tối ưu hóa mô hình AI Video (Veo 3.1 Lite & NanoBanana 2)
- **Linh hoạt giữ chữ tĩnh tránh lỗi font (Veo 3.1 Lite I2V):** Vì mô hình sinh video thường bóp méo ký tự, đối với các phân cảnh có chữ tiếng Việt có dấu ở ảnh gốc, tại dòng prompt `[VIDEO]` tuyệt đối CẤM nhắc đến nội dung chữ và bắt buộc sử dụng cú máy tĩnh (`steady shot`) kèm câu lệnh khóa tĩnh lớp đồ họa chữ: `preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations`. Ngược lại, các phân cảnh không có chữ có dấu thì bắt buộc phải linh hoạt sử dụng các chuyển động camera động (zoom, pan, tilt, dolly) để tránh video bị đơn điệu.
- **Chống lệch mặt nhân vật & Chuẩn hóa Nhân vật theo Bối cảnh (Cast Sheet Rule - BẮT BUỘC):**
  * Trong bối cảnh Việt Nam (công trường, nhà máy, phòng điều hành, sàn thi công), nhân vật xuất hiện **BẮT BUỘC phải là người Việt Nam và ƯU TIÊN nhân vật nam** (ví dụ: *a Vietnamese male chief engineer in safety vest and hard hat*, *a team of Vietnamese male structural engineers*, *Vietnamese male construction workers in professional industrial safety gear*).
  * Trong prompt động `[VIDEO]`, tuyệt đối cấm nhắc lại tên riêng của nhân vật thực tế (các doanh nhân, nhà sáng lập, chính khách, nhân vật lịch sử...). Hãy thay bằng danh từ chung (*the man*, *the leader*, *the chief engineer*, *the entrepreneur*) và câu lệnh bảo tồn diện mạo từ ảnh tham chiếu: `preserving his facial features and the details of the reference image`.
- Định dạng camera: `shot on 35mm anamorphic lens`, `shallow depth of field`, `low-angle perspective`.
- Đảm bảo Exit Vector (góc máy thoát của cảnh trước) khớp với giây thứ 0 của cảnh tiếp theo để tránh jump cuts.
- Không đưa tên người thật/thương hiệu vào prompt video để tránh bộ lọc bảo mật. Thay thế bằng danh từ mô tả chung (ví dụ: `a visionary tech billionaire`, `a government official with Asian features`).

#### E. Tư duy Dịch chuyển Kịch bản sang Visual Prompt (Script-to-Prompt)
- **Quy trình Diễn giải Trực quan 5 Bước (Visual SOP):**
  1. *Giải mã Ngữ cảnh & Xác định Living Scene:* Dịch khái niệm trừu tượng thành thực thể, hành động vật lý thực tế ngoài đời.
  2. *Định vị Mỏ neo Trực quan:* Xác định rõ địa điểm bối cảnh, nhân vật nhất quán theo Cast Sheet, và vật thể thương hiệu/quốc gia.
  3. *Bố cục Điện ảnh & Ánh sáng Noir:* Sử dụng 60-30-10, chiaroscuro lighting, deep noir shadows, góc máy đa dạng.
  4. *Vật lý Chuyển động & Khóa Chữ:* Thiết kế camera và subject tương thích vật lý tự nhiên, khóa tĩnh tuyệt đối lớp chữ tiếng Việt.
  5. *Hội đồng QA Độc lập (Audience-View Check):* Kiểm tra logic trực quan (có giải thích câu thoại không?), nhạy cảm văn hóa, và trùng lặp ý tưởng.
- **Tôn trọng Tên Thực thể & Thương hiệu Gốc (Brand Integrity Principle - BẮT BUỘC):** Tuyệt đối nghiêm cấm việc tự ý thay thế tên của các thực thể, tập đoàn, nhãn hiệu hoặc dòng sản phẩm có thật xuất hiện trong kịch bản (như Vinamilk, Hòa Phát, Vingroup, Masan, VinFast...) thành các tên giả định (như sữa Minh Trí, thép Việt Phát, tập đoàn Vương Phát...). Phải bảo toàn 100% tên thương hiệu trong kịch bản và đưa trực tiếp vào prompt để AI vẽ chuẩn xác, trừ phi có chỉ thị bằng văn bản rõ ràng từ người dùng.
- **Phá vỡ Lời nguyền Kiến thức (Curse of Knowledge):** Luôn đứng ở vị trí của khán giả xem lần đầu chưa biết kịch bản để thiết kế hình ảnh mang tính dẫn dắt trực quan cao. Nghiêm cấm lạm dụng các biểu tượng trừu tượng lặp lại nhàm chán (như cái cân) hoặc các chi tiết quá cô độc (như chỉ vẽ mỗi bảng tên đồng thay vì vẽ cả công trình).
- **Trực quan hóa Thực tế (Internal to External):** Chuyển hóa các khái niệm trừu tượng, dữ liệu, chính sách, hoặc suy nghĩ nội tâm thành các hành động vật lý và bối cảnh sống động ngoài đời thực (ví dụ: thay vì vẽ bàn tay đặt khối hộp để biểu thị "thâu tóm đất đai", hãy vẽ một chiếc Limousine đen đỗ cạnh cánh đồng rộng mênh mông có rào tôn quây xung quanh và máy xúc đứng tĩnh lặng).
- **Tư duy Đạo diễn Góc quay (Shot Director) & Khung prompt 3 lớp:** Viết prompt theo cấu trúc kẹp chặt chẽ: `[Subject & Action] + [Environment & Lighting] + [Camera & Style Specs]`.
- **Cấm Nhạy cảm Văn hóa (Quy tắc ảnh thờ):** Tuyệt đối cấm sử dụng hình ảnh các khung ảnh chân dung đơn độc xếp hàng trên bàn gỗ tối trong bóng tối mờ (trông giống ảnh thờ/cúng trong văn hóa Việt Nam). Thay vào đó, hãy vẽ nhân vật đang làm việc, đi lại hoặc thảo luận tích cực trong môi trường thực tế (boardroom, phòng khách, sảnh lớn).
- **Cấm Phi logic Công nghệ (Quy tắc lò rèn):** Tuyệt đối cấm sử dụng hình ảnh lò rèn thủ công, tia lửa rực hay các dải thép nóng chảy loằng ngoằng phi vật lý trong bối cảnh sản xuất công nghệ cao (nhà máy xe điện, phòng thí nghiệm R&D, lắp ráp tự động). Phải thay bằng thiết kế hologram 3D, cánh tay robot lắp ráp sạch sẽ, màn hình biểu đồ kỹ thuật chính xác.
- **Cấm Ẩn dụ Siêu thực Trừu tượng (Anti-Surrealism Rule):** Tuyệt đối cấm sử dụng các ẩn dụ mang tính siêu thực trừu tượng nằm ngoài trải nghiệm vật lý đời thường của người xem (như con đường chia đôi ngả dưới trời giông bão sấm sét, bức tượng đá khổng lồ Atlas bị quấn xích sắt gánh cây cầu, hay cầu thang Escher xoắn ốc ngược chiều). Mọi bối cảnh phải là không gian vật lý thực tế (phòng họp, nhà máy, sảnh cao ốc, công trường, xe buýt thành phố).
- **Phô diễn tầm vóc công trình vật lý:** Khi kịch bản nhắc đến công trình biểu tượng (sân vận động, cầu vượt biển, tàu cao tốc), prompt bắt buộc phải phác họa được quy mô hoành tráng của công trình đó dưới góc máy điện ảnh (Low-angle wide shot, Wide shot) kết hợp với chữ overlay đồ họa để đảm bảo an toàn chữ viết.
- **Cấm Tuyệt Đối Tóm Tắt Hoặc Lược Bỏ Nội Dung (Anti-Summarization Rule - BẮT BUỘC):** Khi chuyển dịch từ kịch bản gốc sang kịch bản visual trung gian (`chapter_XX_visual.md`), Agent tuyệt đối KHÔNG ĐƯỢC PHÉP tóm tắt, viết gọn lại hay lược bỏ bất kỳ ý tứ, mệnh đề hoặc câu văn nào từ kịch bản gốc. Mọi thông tin, số liệu, luận điểm của kịch bản gốc phải được bảo toàn đầy đủ 100%. Nếu câu kịch bản quá dài, chỉ được phép tách thành các câu đơn độc lập ngắn gọn và trọn vẹn nghĩa để chia cảnh, không được phép cắt bỏ nội dung. Việc tự ý tóm tắt làm mất câu thoại sẽ dẫn đến việc thiếu phân cảnh nghiêm trọng và làm sai lệch trục thời gian khi so khớp với voiceover thực tế.

- **Giao thức Xử lý Câu dài & Tránh Tách câu Cơ học (Anti-Mechanical Splitting):**
  * Tuyệt đối cấm cắt đôi một câu thoại một cách cơ học theo số lượng từ nếu điều đó làm đứt gãy dòng chảy ngữ nghĩa hoặc cắt xén câu ở giữa chừng. Mỗi phân cảnh/prompt bắt buộc phải đi liền với một câu thoại trọn vẹn ngữ nghĩa để hình ảnh không bị vụn vặt, lắt nhắt.
  * Khi một câu thoại dài có nguy cơ làm voiceover vượt quá thời lượng an toàn 8 giây, bắt buộc áp dụng 2 trường hợp xử lý:
    - **Trường hợp 1 (Một ý nghĩa nhưng dài do liệt kê hoặc bay bổng):** Viết lại câu thoại gốc cho súc tích, cô đọng hơn, hoặc **chỉ tạo 1 video duy nhất** (không tách cảnh) kéo dài suốt toàn bộ câu thoại đó.
    - **Trường hợp 2 (Câu dài chứa nhiều ý nghĩa/câu ghép):** Bắt buộc phải thực hiện công đoạn viết lại kịch bản thoại (Oral Polish) ra file riêng để viết prompt, tách hẳn câu ghép đó thành các câu đơn ngắn độc lập, đảm bảo mỗi câu thoại mới truyền đạt trọn vẹn 1 ý và có 1 prompt video riêng biệt đi kèm.

#### F. Quy trình Bảo toàn Mỏ neo Dữ liệu & Chống Bỏ sót Tài liệu (Data Vault Preservation Protocol - BẮT BUỘC)
- **Bước 1: Trích xuất Mỏ neo Dữ liệu (Data Anchor Extraction):** Trước khi bắt đầu viết bất kỳ chương kịch bản nào (`chapter_XX.md`), Agent bắt buộc phải thực hiện quét toàn bộ các tệp trong thư mục `research_vault/` và `02_research_synthesis.md` để lập danh sách **Mỏ neo Dữ liệu (Data Anchors)** gồm: Tên riêng doanh nghiệp/nhà cung cấp Tier-1, tên công nghệ/model sản phẩm, các số liệu kỹ thuật/sản lượng thực chứng, và các căn cứ văn bản pháp lý (Quyết định/Thông tư).
- **Bước 2: Cấm Thay thế Tên riêng bằng Từ chung mờ nhạt (Strict Technical Naming Rule):** Nghiêm cấm tuyệt đối việc tóm tắt hoặc thay thế các tên riêng chuyên môn (như StoreDot, ProLogium, ZF AxTrax 2, Autobrains, Qualcomm, NVIDIA, NXP, Bosch, Renesas, Thông tư 11...) thành các danh từ chung mờ nhạt (như "các nhà cung cấp quốc tế", "các công nghệ mới"). Tên riêng và thông số kỹ thuật là "sức nặng chuyên môn" cốt lõi của kênh Góc Nhìn Podcast, bắt buộc phải xuất hiện chính xác trong kịch bản thoại.
- **Bước 3: Giao thức Đối chiếu Mỏ neo trước khi Chốt (Data Anchor Audit Gate):** Trước khi bàn giao kịch bản cho User duyệt hoặc chuyển sang làm Visual Prompts, Agent bắt buộc phải chạy đối chiếu bảng Mỏ neo Dữ liệu với kịch bản các chương, đảm bảo không có bất kỳ dữ liệu thực chứng nào bị bỏ sót hay rớt lại trong kho nghiên cứu.

#### H. Quy trình Đối chiếu Đồng bộ Kịch bản - Prompt Tự động (Mandatory Visual Script & Prompt Sync Gate - BẮT BUỘC KHÔNG ĐƯỢC BỎ QUA)
- **Nguyên tắc Đồng bộ 1-1 Tuyệt đối (Strict 1-to-1 Mapping):**
  * Tệp `chapter_XX_visual.md` (Kịch bản Visual) là **NGUỒN SỰ THẬT DUY NHẤT** về phân cảnh.
  * Mọi Scene ID trong `chapter_XX_visual.md` (bao gồm các phân cảnh phụ `CHXX_SCYYYa`, `CHXX_SCYYYb`...) BẮT BUỘC phải có đúng 1 cặp prompt `[IMAGE]` và `[VIDEO]` tương ứng 100% trong `prompts_chapter_XX.txt`.
  * TUYỆT ĐỐI CẤM sinh prompt từ dàn ý cũ hoặc tệp thoại chưa qua công đoạn tách cảnh Visual.
- **Cổng kiểm tra tự động trước khi bấm Render (Pre-Render Automated Audit Gate - CHỐNG LÃNG PHÍ CREDITS/TIỀN BẠC):**
  * Trước khi bàn giao bất kỳ tệp prompt nào cho User hoặc đưa vào công cụ sinh ảnh/video (Veo 3.1 / NanoBanana 2), Agent **BẮT BUỘC phải chạy script Python kiểm tra đối chiếu tự động** giữa `chapter_XX_visual.md` và `prompts_chapter_XX.txt`.
  * Script phải xác nhận 2 điều kiện cứng:
    1. **100% Scene ID khớp tuyệt đối** (Không thiếu cảnh nào, không có Scene ID ma).
    2. **Nội dung thị giác trong Prompt mô tả chính xác 100% câu thoại tương ứng tại timestamp đó**.
  * Nếu phát hiện bất kỳ sự trượt chỉ số hay lệch pha nào ➡️ **LẬP TỨC DỪNG TOÀN BỘ QUY TRÌNH**, re-generate lại tệp prompt trước khi cho phép bấm Render sinh video.
- **Cổng khóa phiên bản (Version Lock Gate):** Mỗi khi tệp `chapter_XX_visual.md` có bất kỳ chỉnh sửa hay tách câu nào, tệp prompt `prompts_chapter_XX.txt` phải được làm mới và audit lại ngay lập tức để tránh trượt chỉ số dây chuyền.

#### I. Quy Trình Chuyển Hóa Kịch Bản Trung Gian & Giải Phẫu Cơ Học Trực Quan (Unified Intermediate Visual & Mechanical Explainer Protocol - BẮT BUỘC)
- **Triết Lý "Quy Trình Đồng Nhất Khép Kín" (End-to-End Unified Pipeline):**
  * Kịch bản gốc (`chapter_XX.md`) $\rightarrow$ Kịch bản Visual Trung gian (`chapter_XX_visual.md`) $\rightarrow$ Tệp Prompts I2V (`prompts_chapter_XX.txt`) là **MỘT DÒNG CHẢY HỢP NHẤT KHÔNG THỂ TÁCH RỜI**.
  * Bản chất kịch bản gốc mang tính tư duy vĩ mô và ngôn ngữ phát thanh. Kịch bản trung gian (`chapter_XX_visual.md`) đóng vai trò là **Bộ dịch thuật cơ học (Mechanical Translator)**, có nhiệm vụ chuyển hóa câu từ trong kịch bản gốc thành một bức tranh giải phẫu vật lý dễ hiểu và trực quan nhất. Nhờ đó, khâu viết prompt tiếp theo có thể dễ dàng chuyển ngữ chính xác sang tiếng Anh mà không bị hiểu sai ngữ cảnh hay rơi vào bẫy trừu tượng.

- **Quy Tắc Mô Hình Giải Phẫu Cơ Học 3 Tầng (3-Tier Mechanical Anatomy):**
  * Đối với mọi phân cảnh mô tả công nghệ, kết cấu hạ tầng, hoặc vận hành công nghiệp, trường `[BỐI CẢNH]` trong kịch bản trung gian bắt buộc phải bóc tách rõ 3 tầng vật lý:
    1. *Tầng 1 - Đế Cố Định (Anchor/Base):* Lòng chảo khán đài bê tông, đài móng ngầm, nhà xưởng, cảng biển.
    2. *Tầng 2 - Bộ Truyền Động / Cơ Chế Chủ Lực (Actuators & Mechanisms):* Tháp nâng thủy lực Strand Jacking, ray cơ khí trượt, đầu dò sóng siêu âm NDT, chip cảm biến nhiệt điện tử.
    3. *Tầng 3 - Khối Tác Động & Hướng Lực (Payload & Motion Vector):* Mái vòm thép đang được kéo lên, khay cỏ lặn xuống hầm ngầm, dầm thép đang cắt CNC, mũi tên chỉ hướng lực nâng.
- **Quy Tắc Nhãn Chú Thích Kỹ Thuật Đích Danh (Engineering Technical Callouts):**
  * Nghiêm cấm để hình ảnh trơn khiến người xem phải tự đoán. Mọi phân cảnh giải phẫu kỹ thuật bắt buộc phải khai báo nhãn chú thích tiếng Việt 3D trực diện ở trường `[TEXT OVERLAY]` và đưa vào prompt `[IMAGE]` (ví dụ: `"THÁP NÂNG THỦY LỰC"`, `"MÁI VÒM THÉP 40.000 TẤN"`, `"CÁP KÉO ĐỒNG BỘ"`).
  * Ở dòng `[VIDEO]`, luôn khóa tĩnh lớp nhãn (`preserving all technical callout labels and static graphic layers...`) để bảo tồn chữ viết trên mô hình Veo 3.1.
- **Quy Tắc "1 Khái Niệm Cơ Học = 1 Cú Máy Điện Ảnh Liền Mạch" (Unitary Mechanical Motion):**
  * Tuyệt đối cấm băm vụn một chu trình cơ học thành các cảnh slide rời rạc. Một hành động vật lý (như kéo vòm thép từ cốt 0 lên 120m, hoặc trượt khay cỏ xuống hầm) phải được thực hiện trong 1 cú máy chuyển động mượt mà 8 giây trọn vẹn.

#### J. Giao Thức Rà Soát Lỗi Tự Động & Sửa Chữa Trước Khi Bàn Giao (Mandatory Pre-Delivery Self-Review, Auto-Fix & QA Gate Protocol - BẮT BUỘC)
- **Nguyên Tắc "Không Bàn Giao Khi Chưa Sạch Lỗi" (Zero-Defect Delivery Rule):**
  * Sau khi hoàn tất việc tạo hoặc chỉnh sửa bất kỳ tệp Visual Script (`chapter_XX_visual.md`) hoặc Tệp Prompts (`prompts_chapter_XX.txt`), Agent **TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP** thông báo hoàn thành hay trả kết quả về cho người dùng ngay lập tức.
  * Agent bắt buộc phải thực hiện quy trình tự rà soát (Self-Review Loop) qua toàn bộ 10 cổng checklist chất lượng, phát hiện và **TỰ ĐỘNG SỬA CHỮA TOÀN BỘ CÁC LỖI TỒN ĐỌNG TRƯỚC** khi gửi thông báo.
- **Quy Trình 5 Bước Tự Rà Soát & Khắc Phục Lỗi (Self-Audit & Auto-Fix Workflow):**
  1. *Bước 1: Rà soát & Khắc phục Lỗi Nhân khẩu học / Tây hóa Nhân vật:* Quét toàn bộ prompt `[IMAGE]`. Nếu cảnh diễn ra tại Việt Nam mà thiếu định danh `Vietnamese male/female [vai trò]` (hoặc dùng từ chung chung như `an engineer`, `a doctor`, `a worker` khiến AI vẽ người Tây da trắng) ➡️ **Sửa lại ngay lập tức** trong tệp prompt.
  2. *Bước 2: Rà soát & Khắc phục Lỗi Trừu tượng hóa / Siêu thực:* Quét toàn bộ mô tả bối cảnh. Nếu phát hiện các hình ảnh siêu thực (cái cân công lý bay, bàn tay thép trên trời, cơn mưa tiền, khoảng không hư vô, quả cầu năng lượng) ➡️ **Sửa lại ngay lập tức** thành hành động vật lý và không gian đời thực cụ thể.
  3. *Bước 3: Rà soát & Khắc phục Lỗi Khóa Chữ (Text Freezing):* Đối chiếu với trường `[TEXT OVERLAY]`. Mọi cảnh có chữ bắt buộc dòng `[VIDEO]` phải là `Steady camera shot` và chứa câu lệnh khóa tĩnh chống méo font. Nếu thiếu ➡️ **Bổ sung ngay**.
  4. *Bước 4: Rà soát Toán học Thời lượng & Khớp ID 1-1:* Chạy script kiểm tra độ dài câu thoại ($\le 26$ từ/cảnh) và đảm bảo 100% Scene ID khớp tuyệt đối giữa Visual Script và Prompts File. Nếu có câu quá 26 từ ➡️ **Tách sub-scenes và cập nhật ngay**.
  5. *Bước 5: Chạy Script Kiểm tra Tự Động (`check_boilerplate.py`):* Thực thi script kiểm tra cụm từ rác và lộ mã ID. Chỉ khi script báo `SUCCESS (S-Grade)`, Agent mới được bàn giao và xuất báo cáo cho người dùng.


## 🎬 QUY ĐỊNH BẮT BUỘC: SẢN XUẤT VIDEO TỰ ĐỘNG (PHA 14 — VIDEOCORE BATCH PRODUCTION)

> ⚠️ **BẮT BUỘC TUÂN THỦ KHI SẢN XUẤT VIDEO CHO X-ECONOMICS:**
> 1. **Cơ chế 1-Chạm Bản Địa:** Khi User yêu cầu tạo video hoặc gõ `/generate_videos`, Agent thực thi trực tiếp từ thư mục dự án:
>    ```bash
>    python3 scripts/produce_episode_videos.py --episode <slug>
>    ```
> 2. **Hạ tầng Dùng Chung VideoCore:**
>    - Toàn bộ engine điều phối nằm tại `VideoCore` và đã được liên kết mềm (symlink) vào `scripts/` và `.agents/skills/batch_video_generator`.
>    - Tự động quét diff các cảnh thiếu, tự nạp ảnh tham chiếu `@avatar.jpg` từ `episodes/<slug>/ref_images/`, kết nối Chrome port 9222, kích hoạt watchdog 300s, và tự động chuyển file `.mp4` về `episodes/<slug>/videos/`.
> 3. **Kiểm toán Hoàn tất:** Dùng `python3 scripts/check_video_progress.py --episode <slug>` để xác nhận 100% video hợp lệ.
