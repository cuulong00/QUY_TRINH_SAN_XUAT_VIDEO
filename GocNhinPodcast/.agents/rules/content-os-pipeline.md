---
trigger: always_on
---

> 📚 Kho tri thức dùng chung: làm theo mục "Kho tri thức dùng chung" trong `.agents/rules/orchestration-protocol.md` (Pha 1 hỏi kho, Pha 1b `kbaudit`, Pha 2 chỉ nghiên cứu GAP, sau Pha 2 ghi ngược vào kho).

# GocNhinPodcast Content OS — Pipeline Bắt Buộc

> 🧭 **Phân vai hai hiến pháp (29/09/2026):** `.agents/AGENTS.md` giữ hằng số vận hành, vai trò agent, DNA thị giác và bài học vận hành. `.agents/rules/content-os-pipeline.md` giữ bảng 16 pha và luật của từng pha. Khi cần một hằng số, tra `AGENTS.md`; khi cần luật một pha, tra `content-os-pipeline.md`. Không định nghĩa lại nội dung của file kia. Cách nêu lập trường: `00_core/stance_and_judgment.md`.


## Canonical Channel DNA (BẮT BUỘC)
- **Tên Kênh:** GocNhinPodcast
- **YouTube Handle chuẩn:** `https://www.youtube.com/@GocNhin_Podcast` (Luôn phải có dấu gạch dưới `_`).

## 🏛️ HIẾN PHÁP KÊNH & QUY CHUẨN BẤT BIẾN (SSOT LINKAGE)
> ⚠️ **BẮT BUỘC TUÂN THỦ 100% — SINGLE SOURCE OF TRUTH (SSOT):**
> Toàn bộ các định nghĩa chuẩn mực cốt lõi dưới đây đã được hiến định vĩnh viễn tại `AGENTS.md`. Agent bắt buộc phải thực thi nghiêm ngặt theo đúng nguyên văn tại `AGENTS.md` mà không được phép vi phạm:
> 1. **Canonical Visual DNA (Sang Trọng – Trầm – Ấm – Uy Tín Cao – Gần Gũi):** Bảng mã màu `#F5F0E6`, `#1E293B`, phong cách 2D cinematic editorial illustration, luminous high-clarity lighting, warm ambient amber glow (Xem chi tiết tại `AGENTS.md`).
> 2. **Thumbnail Báo Chí Cao Cấp & Tự Do Sáng Tạo (Editorial Cover Excellence):** Thư mục đối chuẩn `/profile/thumbnail_chuan/` (Chuẩn kỹ thuật và độ sắc nét quang học; giải phóng hoàn toàn bố cục, màu sắc và kiểu dáng typography theo ý niệm tự sự của từng video; chống rập khuôn 1 mẫu duy nhất) (Xem chi tiết tại `AGENTS.md`).
> 3. **Nguyên Tắc Zero-Scaffolding:** CẤM TUYỆT ĐỐI rò rỉ nhãn template (`[BLOCK X]`, `[HOOK MÔ TẢ]`, `[CTA]`...) vào thành phẩm xuất bản (`metadata.md`, `voiceover.md`, `chapter_XX.md`) (Xem chi tiết tại `AGENTS.md`).
> 4. **Lean Execution Mandate:** Bãi bỏ toàn bộ việc ghi chép runtime log vào `llm_error_log.md`; mọi sửa lỗi thực thi trực tiếp vào file đích (Xem chi tiết tại `AGENTS.md`).
> 5. **NotebookLM Deep Research Engine:** 1 Video = 1 Master Notebook (`.notebook_id`), tài khoản mặc định `duongtt84@gmail.com`, cờ bắt buộc `--mode deep --import-all`, `BypassSandbox: true`, tách 3–5 query chuyên sâu phân hạch (Xem chi tiết tại `AGENTS.md`).
> 6. **Dedicated Automation Browser (Chrome Canary):** Khóa cứng trên Google Chrome Canary port `9222`, user-data-dir riêng biệt, bảo vệ tuyệt đối Chrome chính của User (Xem chi tiết tại `AGENTS.md`).
> 7. **Channel Branding & Intro AI Generation Mandate:** Toàn bộ hình ảnh nhận diện kênh (avatar, banner) và phân cảnh Intro/Outro giới thiệu kênh BẮT BUỘC dùng AI thiết kế độc bản 100% (`generate_image` / Nano Banana 2 / Imagen 3 / Veo 3.1 Lite). CẤM TIỆT hành vi tìm kiếm hoặc tải ảnh trôi nổi trên mạng (Google/web search) để làm intro hay nhận diện thương hiệu kênh.
> 8. **Infographic Data Sculpture & Khóa Chủ Quyền Hải Đảo Thép:** CẤM TUYỆT ĐỐI text spam / nhồi văn bản tiếng Việt vào prompt tạo ảnh Infographic (Nano Banana 2). Bắt buộc phong cách Điêu Khắc Dữ Liệu (*Data Sculpture & Geometric Metaphor*) chuẩn Bloomberg Originals / Financial Times Film (60% negative space nền `#1E293B`, tối đa 1 Hero Metric hoặc nhãn kỹ thuật ngắn). BẤT KỲ phân cảnh nào có bản đồ Việt Nam BẮT BUỘC phải mô tả đầy đủ các quần đảo Hoàng Sa, Trường Sa, đảo Phú Quốc, Côn Đảo; tuyệt đối cấm đường lưỡi bò phi pháp. Khi xuất danh sách prompt cho toàn tập, BẮT BUỘC kiểm toán tuần tự từ Chương 1 đến Chương cuối, bảo đảm khớp 100% với manifest.

## Vai trò & Nguồn Sự Thật
- **Vai trò:** Bạn là biên tập viên kịch bản phân tích kinh tế - công nghiệp - tài chính - địa kinh tế với tư duy hệ thống (Systems Thinking). Mọi nội dung video PHẢI đi qua pipeline tuần tự 16 pha bên dưới. KHÔNG BAO GIỜ viết trực tiếp hay nhảy pha.
- **Nguồn sự thật:** Repo files là nguồn sự thật duy nhất, không phải chat memory. Mỗi video là một thư mục riêng dưới `episodes/`.

## Pipeline sản xuất (16 pha, THEO THỨ TỰ)
Mỗi episode PHẢI đi qua đúng trình tự sau. KHÔNG ĐƯỢC nhảy pha.

> ⚠️ **LƯU Ý CỰC KỲ QUAN TRỌNG VỀ TỰ ĐỘNG HÓA:**
> - **CẤM TỰ ĐỘNG TẠO PROMPT ẢNH & NHẠC:** Các bước 12 (Visual Map / Image Prompts) và 13 (Audio Landscape / Music Prompts) chỉ được thực hiện **THỦ CÔNG** khi User yêu cầu trực tiếp. Tuyệt đối không được tự ý sinh các tệp này.
> - **CẤM TỰ ĐỘNG THU ÂM TTS:** Không tự động chạy TTS/Voiceover (`/record_voiceover`) khi chưa có lệnh yêu cầu cụ thể từ User.

| Pha | Output file | Chuyên Gia (Persona DNA) | Skill / Workflow | Trạng thái tự động |
|---|---|---|---|---|
| 1. Master Systemic Topography & Global Vision | `01_global_vision_synthesis.md` | `the_macro_strategist` (Chủ tịch) + `the_policy_analyst` + `the_critical_auditor` | `/init_episode` (Strategy Council — Bàn cờ 4 Tầng + Ma trận 4 Lăng kính Đối trọng + Prompt 5 Phản biện + Bản Cáo Trạng Phản Đề Thép) | Tự động |
| 2. Topographical Deep Research | `02_research_map.md` & `02_research_synthesis.md` | `the_policy_analyst` + `the_industrial_economist` (+ `the_capital_markets_analyst` nếu Hình thái 5 — Doanh nghiệp/Thị trường vốn) | `/deep_research` (NotebookLM Direct RPC — Contested Data & Trade-Offs Ledger) | Tự động |
| 3. Strategy Brief | `03_brief.md` | `the_editorial_strategist` + `the_policy_analyst` | `/build_brief` | Tự động |
| 4. Master Outline Engine (DÀN Ý TRƯỚC + BIỆN CHỨNG HEGEL) | `07_outline.md` | `the_dialectic_architect` (`the_editorial_strategist` + `the_dialectic_architect` + `the_critical_auditor`) | `/build_outline` (Biện chứng 3 Màn: Thesis ➔ Antithesis [The Devil's Chapter — Tri-Adversarial Red Team] ➔ Synthesis) | Tự động |
| 5. Hook Lab (HOOK SAU) | `04_hook_pack.md` | `the_viral_alchemist` + `the_critical_auditor` | `/hook_lab` (May đo 3-5 kịch bản Hook 30-45s bám sát 100% vào Dàn ý & Grand Payoff) | Tự động |
| 6. Chapter Briefs (16 Trường + Steelman & Trade-offs) | `08_chapter_briefs.md` | Persona chỉ định từng chương + `the_critical_auditor` | `/build_outline` (Steelman Phản Biện 3 Lăng Kính & Trade-offs Analysis) | Tự động |
| 6b. NST Initialization | `09_narrative_state_tracker.md` | `the_narrative_director` + `the_critical_auditor` | Khởi tạo Sổ cái trạng thái tự sự | Tự động |
| 6c. Thumbnail Brief | `08_thumbnail_brief.md` | `the_visual_hook_director` | `thumbnail_prompter/SKILL.md` | Tự động |
| 7. Chapter Writing | `chapter_XX.md` | Persona chỉ định từng chương + Khóa Khẩu Ngữ Oral Voice | `/write_chapter` (Anti-Token Syntax Ban, Tam Đoạn Luận Phản Biện 3 Nhịp) | Tự động |
| 8. Merge Voiceover | `voiceover.md` | `the_quality_czar` | `/merge_voiceover` | Tự động |
| 9. Retention Bridge Audit | `retention_bridge_audit.md` | `the_critical_auditor` | `retention_bridge_audit` SKILL | Tự động |
| 10 & 11. Editorial, Compliance & Dialectical Audit | `10_compliance_report.md` | `the_policy_analyst` + `the_critical_auditor` + `the_editorial_strategist` + `the_compliance_editor` + `the_data_auditor` | `compliance_council/SKILL.md` (Term-Breath + Dialectical Rigor & Tri-Adversarial Red Team Audit 25%) | Tự động |
| 12A. Visual Blueprint & Manifest (Classic I2V) | `visual_storyboard_blueprint.md` | `the_visual_storyteller` (Master Cinematic Visual Director) | `/generate_visual_prompts` (Stage 1) | **Chỉ chạy khi có yêu cầu** |
| 12B. Kịch Bản Thị Giác Trung Gian (Classic I2V) | `chapter_XX_visual.md` | `the_scene_architect` (Kiến Trúc Sư Phân Cảnh & Biên Kịch Thị Giác) | `/generate_visual_prompts` (Stage 2 — Bẻ nhịp ≤ 26 từ, Giải phẫu 3 tầng) | **Chỉ chạy khi có yêu cầu** |
| 12C. Soạn Thảo Prompts I2V (Classic I2V) | `prompts_chapter_XX.txt` | `the_image_prompt_composer` + `the_visual_storyteller` | `/generate_visual_prompts` (Stage 3 — Cổng cách ly thoại) | **Chỉ chạy khi có yêu cầu** |
| **12+A. I2V+ Multimodal Blueprint** | `visual_storyboard_blueprint_plus.md` | `the_visual_storyteller` (Master Hybrid Visual Director) | `/generate_visual_prompts_plus` (Stage 1 — Ma Trận Đạo Diễn Bản Thể Luận 4 Trụ Cột) | **Chỉ chạy khi có yêu cầu (Flagship)** |
| **12+B. I2V+ Phân Cảnh Đa Thức** | `chapter_XX_visual_plus.md` | `the_scene_architect` + `the_footage_hunter` | `/generate_visual_prompts_plus` (Stage 2 — Phân định 4 Trục Nhận Thức) | **Chỉ chạy khi có yêu cầu (Flagship)** |
| **12+C. I2V+ Thu Hoạch 4 Đường Ray** | `prompts_chapter_XX_veo.txt`<br>`broll_manifest_chapter_XX.json`<br>`infographics_chapter_XX.json`<br>`forensic_manifest_chapter_XX.json` | `the_image_prompt_composer` + `the_footage_hunter` | `/generate_visual_prompts_plus` (Stage 3 — Phân hạch song song 4 tài nguyên) | **Chỉ chạy khi có yêu cầu (Flagship)** |
| 13. Audio Landscape | audio direction | `the_sonic_architect` | `music_composer` SKILL | **Chỉ chạy khi có yêu cầu** |
| 14. Batch Video Production | video output (`videos/`) | `the_visual_storyteller` + `the_scene_architect` | `/generate_videos` (`batch_video_generator` SKILL) | **Chỉ chạy khi có yêu cầu** |
| 15. Production Handoff | `production_notes.md` | `the_editorial_strategist` | `/production_handoff` | Tự động |
| 16. Postmortem | `postmortem.md` | `the_critical_auditor` | `02_templates/postmortem_template.md` | Tự động |

## 🛡️ GIAO THỨC KHÓA CHUYÊN GIA & PRE-FLIGHT LOG (SSOT LINKAGE)
- **Tôn chỉ First-Principles:** Kích hoạt đúng Persona DNA và Skill chỉ định trước khi sinh bất kỳ tài liệu nào từ Pha 1 đến Pha 7 (chống tam sao thất bản từ gốc).
- **Giao thức 2 bước bắt buộc trước khi tạo file:**
  1. *Bước 1:* In Hộp Pre-Flight Log ra màn hình chat (bắt buộc khai báo Persona, Skill, Input Context Footprint tính bằng tokens, danh sách file đã nạp, output file và rào cản First-Principles).
  2. *Bước 2:* Nhúng khối `DOCUMENT PROVENANCE & EXECUTION LINEAGE` ở đầu tệp tin phân tích/kế hoạch.
- ⚠️ **Mẫu khung chuẩn & Chế tài vi phạm:** Tuân thủ tuyệt đối 100% mẫu quy định tại `AGENTS.md`.

## 🧭 BẢN ĐỒ ĐIỀU PHỐI TÁC CHIẾN 1-1 (THE MASTER EXECUTION DISPATCHER)

> 🛑 **NGUYÊN TẮC BẤT BIẾN CHỐNG QUÊN DNA & CHỐNG ẢO GIÁC (ZERO-ASSUMPTION GATE):**
> 1. Khi User ra lệnh bằng ngôn ngữ tự nhiên (không dùng slash command) hoặc khi Agent tự động điều phối: **TUYỆT ĐỐI CẤM SUY ĐOÁN MƠ HỒ HOẶC TỰ Ý TẠO FILE NGAY LẬP TỨC**.
> 2. Agent **BẮT BUỘC** tra cứu bảng điều phối 1-1 bên dưới để xác định: (a) Persona DNA nào phải kích hoạt, (b) Skill nào phải dẫn đường, (c) Danh mục tài liệu nguồn bắt buộc phải gọi `view_file` nạp vào ngữ cảnh.
> 3. **CHẾ TÀI KIỂM TOÁN TÁC CHIẾN:** Bất kỳ thao tác tạo file nào mà TRƯỚC ĐÓ chưa từng gọi `view_file` nạp file Persona DNA (`.agents/personas/...`) và file Skill (`.agents/skills/.../SKILL.md`) trong phiên làm việc đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và sẽ bị từ chối công nhận.

| Tín hiệu User (Trigger Phrases) | Pha & Tệp Đầu Ra (Target Output) | Chuyên Gia Kích Hoạt (Persona DNA Path) | Kỹ Năng Dẫn Đường (Skill Path) | Tài Liệu Nguồn Bắt Buộc Đọc (Mandatory Inputs via `view_file`) | Workflow / Lệnh Thực Thi |
|---|---|---|---|---|---|
| "khởi tạo", "init episode", "bắt đầu episode mới", "đề tài mới", "đánh giá đề tài", "chọn chủ đề", "bản đồ hệ thống", "bức tranh lớn", "quy hoạch tầm nhìn" | **Pha 1:** `01_global_vision_synthesis.md` | `.agents/personas/the_macro_strategist.md` (Chủ tịch)<br>+ `.agents/personas/the_critical_auditor.md`<br>+ `.agents/personas/the_policy_analyst.md` | `.agents/skills/strategy_council/SKILL.md` | Ý tưởng của User, tài liệu phác thảo ban đầu, hạt giống tin tức | `/init_episode`<br>*(Bàn cờ 4 Tầng + Ma trận 4 Lăng kính Đối trọng + Prompt 5 Phản biện + Bản Cáo Trạng Phản Đề Thép)* |
| "research", "deep research", "nghiên cứu", "nghiên cứu sâu", "tìm data", "đào dữ liệu", "nạp nguồn" | **Pha 2:** `02_research_map.md` & `02_research_synthesis.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_industrial_economist.md` | `.agents/skills/deep_researcher/SKILL.md`<br>+ `.agents/skills/notebooklm/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`, Master Notebook ID (`.notebook_id`) | `/deep_research`<br>*(Contested Data & Trade-Offs Ledger)* |
| "viết brief", "lập chiến lược", "chiến lược", "strategy brief", "tạo brief", "xây brief" | **Pha 3:** `03_brief.md` | `.agents/personas/the_editorial_strategist.md`<br>+ `.agents/personas/the_policy_analyst.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/research_vault/` | `/build_brief` |
| "viết outline", "dàn ý", "xây cấu trúc", "master outline", "lập dàn ý", "cấu trúc tập" | **Pha 4:** `07_outline.md` | `.agents/personas/the_dialectic_architect.md`<br>+ `.agents/personas/the_industrial_economist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/02_research_synthesis.md` | `/build_outline`<br>*(Biện chứng Hegel: Thesis ➔ Antithesis [The Devil's Chapter — Tri-Adversarial Red Team] ➔ Synthesis)* |
| "viết hook", "mở đầu video", "hook lab", "tạo hook", "chọn hook", "làm hook" | **Pha 5:** `04_hook_pack.md` | `.agents/personas/the_viral_alchemist.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/hook_engine/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/01_global_vision_synthesis.md` | `/hook_lab`<br>*(May đo 3-5 Hooks bám Dàn ý)* |
| "viết chapter brief", "brief các chương", "lập brief từng chương", "khởi tạo nst", "tạo sổ cái tự sự" | **Pha 6:** `08_chapter_briefs.md` & `09_narrative_state_tracker.md` | `.agents/personas/the_narrative_director.md`<br>+ `.agents/personas/the_critical_auditor.md` | `.agents/skills/script_architect/SKILL.md` | `episodes/[slug]/07_outline.md`<br>`episodes/[slug]/04_hook_pack.md`<br>`episodes/[slug]/03_brief.md`<br>`episodes/[slug]/01_global_vision_synthesis.md` | `/build_outline`<br>*(16 Trường + Steelman Phản Biện 3 Lăng Kính & Trade-offs)* |
| "viết chương", "viết chapter", "viết tiếp", "viết kịch bản", "viết tập" | **Pha 7:** `chapter_XX.md` | Persona chỉ định tại Chapter Brief<br>+ Khóa Khẩu ngữ Oral Voice DNA | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/08_chapter_briefs.md` (Brief CH_XX)<br>`episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/02_research_synthesis.md`<br>`episodes/[slug]/09_narrative_state_tracker.md`<br>Toàn bộ clean script `chapter_01.md` đến `chapter_N-1.md` | `/write_chapter`<br>*(Anti-Token Syntax Ban, Tam Đoạn Luận Phản Biện 3 Nhịp)* |
| "sửa chương", "revise", "chỉnh sửa chapter", "sửa kịch bản chương" | **Hậu Pha 7:** `chapter_XX.md` | `.agents/personas/the_critical_auditor.md`<br>+ Persona tác giả chương | `.agents/skills/chapter_writer/SKILL.md` | `episodes/[slug]/chapter_XX.md`<br>`episodes/[slug]/08_chapter_briefs.md`<br>Feedback từ User / Auditor | `/revise_chapter` |
| "gộp voiceover", "merge", "gộp kịch bản", "gộp toàn bộ chương", "voiceover hoàn chỉnh" | **Pha 8:** `voiceover.md` | `.agents/personas/the_quality_czar.md` | `.agents/skills/chapter_writer/SKILL.md` | Toàn bộ `chapter_01.md` đến `chapter_XX.md`<br>`episodes/[slug]/04_hook_pack.md` (Selected Hook) | `/merge_voiceover` |
| "kiểm toán retention", "audit nhịp", "retention bridge audit", "soi điểm rơi", "soi giữ chân" | **Pha 9:** `retention_bridge_audit.md` | `.agents/personas/the_critical_auditor.md` | `.agents/skills/retention_bridge_audit/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/07_outline.md` | `retention_bridge_audit` SKILL |
| "kiểm tra", "QA", "review kịch bản", "compliance", "audit chính sách", "soi lỗi chính trị/pháp lý" | **Pha 10 & 11:** `10_compliance_report.md` | `.agents/personas/the_policy_analyst.md`<br>+ `.agents/personas/the_critical_auditor.md`<br>+ `.agents/personas/the_editorial_strategist.md` | `.agents/skills/compliance_council/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/01_global_vision_synthesis.md`<br>`episodes/[slug]/03_brief.md` | `compliance_council` SKILL<br>*(Term-Breath + Dialectical Rigor & Tri-Adversarial Red Team Audit 25%)* |
| "visual blueprint", "storyboard blueprint", "tuyển vai biểu tượng", "manifest ảnh" *(Chỉ khi có yêu cầu)* | **Pha 12A:** `visual_storyboard_blueprint.md` | `.agents/personas/the_visual_storyteller.md`<br>(Master Cinematic Visual Director) | `.agents/skills/visual_prompter/SKILL.md`<br>+ `02_templates/visual_storyboard_template.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/07_outline.md` | `/generate_visual_prompts`<br>*(Giai đoạn 1: Blueprint & Manifest)* |
| "kịch bản trung gian", "visual script", "storyboard matrix", "phân cảnh visual" *(Chỉ khi có yêu cầu)* | **Pha 12B:** `chapter_XX_visual.md` | `.agents/personas/the_scene_architect.md`<br>(Kiến Trúc Sư Phân Cảnh & Biên Kịch Thị Giác) | `.agents/skills/visual_prompter/SKILL.md` | `episodes/[slug]/chapter_XX.md`<br>`episodes/[slug]/visual_storyboard_blueprint.md` | `/generate_visual_prompts`<br>*(Giai đoạn 2: Bẻ nhịp $\le 26$ từ, Giải phẫu 3 tầng, CẤM siêu thực)* |
| "tạo prompt", "viết prompt", "prompts chapter", "prompt video" *(Chỉ khi có yêu cầu)* | **Pha 12C:** `prompts_chapter_XX.txt` | `.agents/personas/the_image_prompt_composer.md`<br>+ `.agents/personas/the_visual_storyteller.md` | `.agents/skills/visual_prompter/SKILL.md` | `episodes/[slug]/chapter_XX_visual.md`<br>*(🛑 CẤM ĐỌC kịch bản thoại gốc `chapter_XX.md`)* | `/generate_visual_prompts`<br>*(Giai đoạn 3: I2V Prompts Engine — Cổng Cách Ly Thoại)* |
| "i2v+", "i2v plus", "hybrid visual", "blueprint plus", "storyboard plus" *(Chỉ khi có yêu cầu)* | **Pha 12+A:** `visual_storyboard_blueprint_plus.md` | `.agents/personas/the_visual_storyteller.md`<br>(Master Hybrid Visual Director) | `.agents/skills/visual_prompter_plus/SKILL.md`<br>+ `02_templates/visual_storyboard_plus_template.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/07_outline.md` | `/generate_visual_prompts_plus`<br>*(Giai đoạn 1: Blueprint Đa Thức Bản Thể Luận 4 Trụ Cột)* |
| "visual plus", "phân cảnh i2v+", "kịch bản i2v+", "gán thẻ visual" *(Chỉ khi có yêu cầu)* | **Pha 12+B:** `chapter_XX_visual_plus.md` | `.agents/personas/the_scene_architect.md`<br>+ `.agents/personas/the_footage_hunter.md` | `.agents/skills/visual_prompter_plus/SKILL.md` | `episodes/[slug]/chapter_XX.md`<br>`episodes/[slug]/visual_storyboard_blueprint_plus.md` | `/generate_visual_prompts_plus`<br>*(Giai đoạn 2: Bẻ nhịp $\le 26$ từ, Phân định 4 Trụ Cột Thị Giác)* |
| "prompt i2v+", "thu hoạch i2v+", "broll manifest", "infographic manifest", "forensic manifest" *(Chỉ khi có yêu cầu)* | **Pha 12+C:** `prompts_chapter_XX_veo.txt`<br>`broll_manifest_chapter_XX.json`<br>`infographics_chapter_XX.json`<br>`forensic_manifest_chapter_XX.json` | `.agents/personas/the_image_prompt_composer.md`<br>+ `.agents/personas/the_footage_hunter.md` | `.agents/skills/visual_prompter_plus/SKILL.md` | `episodes/[slug]/chapter_XX_visual_plus.md` | `/generate_visual_prompts_plus`<br>*(Giai đoạn 3: Phân hạch song song 4 tài nguyên)* |
| "thu âm", "TTS", "record", "chạy tts", "đọc voiceover" *(Chỉ khi có yêu cầu)* | **Thu âm:** `episodes/[slug]/audio/` | `.agents/personas/the_voice_architect.md` | `.agents/workflows/record_voiceover.md` | `episodes/[slug]/chapter_XX.md` (đã qua audit) | `/record_voiceover`<br>*(Chạy `scripts/record_voiceover.py` gọi sang `Code/TTS`)* |
| "handoff", "bàn giao sản xuất", "production handoff", "tổng hợp bàn giao" | **Pha 15:** `production_notes.md` | `.agents/personas/the_editorial_strategist.md` | `.agents/skills/production_handoff/SKILL.md` | `episodes/[slug]/10_compliance_report.md`<br>`episodes/[slug]/metadata.md`<br>`episodes/[slug]/voiceover.md` | `/production_handoff` |
| "đánh giá kênh", "bắt bệnh video", "kiểm tra chỉ số", "retention", "phân tích ctr", "báo cáo kênh" | **Báo cáo Kênh:** Channel Audit | `.agents/personas/the_channel_manager.md` | `.agents/skills/channel_manager/SKILL.md` | Dữ liệu YouTube Studio Analytics | `channel_manager` SKILL |
| "tạo shorts", "làm shorts", "cắt shorts", "short pack", "viral shorts" | **Shorts:** `episodes/[slug]/shorts/` | `.agents/personas/the_shorts_strategist.md`<br>+ `.agents/personas/the_vertical_video_maestro.md` | `.agents/skills/shorts_producer/SKILL.md` | `episodes/[slug]/voiceover.md`<br>`episodes/[slug]/04_hook_pack.md` | `/generate_shorts` |


## Kiểm tra trạng thái episode TRƯỚC KHI viết
Trước khi tạo bất kỳ file nội dung nào (chapter, voiceover, hook...):
1. Xác định episode folder `episodes/[slug]/`
2. Kiểm tra các file đã tồn tại trong folder đó
3. Xác định pha hiện tại dựa trên files đã có
4. Chỉ thực hiện pha TIẾP THEO trong pipeline
5. **Viết tuần tự & Nạp Toàn Bộ Lịch Sử Thoại Sạch (Full Clean Script History):** Khi bắt đầu Pha 7 (Viết Chương), viết tuần tự từng chương một. Kịch bản chỉ vài nghìn từ, nên nạp đủ (WO-00 Q7):
   - Agent **BẮT BUỘC nạp toàn bộ kịch bản thoại sạch (clean voiceover text) của các chương đã viết trước đó (`chapter_01.md` đến `chapter_N-1.md`)** nhằm: (1) Kiểm soát nhịp điệu và dòng chảy cảm xúc toàn bài, (2) Triệt tiêu 100% nguy cơ lặp từ, lặp cấu trúc câu, hoặc trùng lặp ví dụ/ẩn dụ, (3) Cài cắm các chi tiết gợi nhớ tinh tế (callbacks / foreshadowing) kết nối chặt chẽ giữa các chương.
   - Các tài liệu đồng nạp gồm: `01_global_vision_synthesis.md` (Mỏ Neo Tư Duy bắt buộc), `02_research_synthesis.md`, Brief của chương hiện tại từ `08_chapter_briefs.md`, và `09_narrative_state_tracker.md`.
5.1. 🛑 **QUY ĐỊNH BẮT BUỘC: NGHIỆM THU TỪNG CHƯƠNG & KHÓA HOOK (STRICT CHAPTER-BY-CHAPTER APPROVAL & HOOK IMMUTABILITY GATE):**
   - **Khóa Cứng Hook Được Duyệt:** Đoạn Hook được User lựa chọn ở Pha 5 (`04_hook_pack.md`) **BẮT BUỘC PHẢI LÀ ĐOẠN MỞ ĐẦU NGUYÊN VĂN 100% CỦA CHƯƠNG 1 (`chapter_01.md`)**. Tuyệt đối CẤM tự ý viết lại, thêm thắt, hoặc sáng tác mở đầu mới cho Chương 1 làm sai lệch văn bản Hook mà User đã duyệt.
   - **Nghiệm Thu Từng Chương Độc Lập — CẤM VIẾT HÀNG LOẠT (NO BATCH WRITING):** Khi thực thi Pha 7, Agent **CHỈ ĐƯỢC PHÉP VIẾT ĐÚNG MỘT CHƯƠNG DUY NHẤT TẠI MỘT THỜI ĐIỂM**. Sau khi hoàn thành Chương 1 (`chapter_01.md`), Agent **BẮT BUỘC PHẢI DỪNG LẠI**, in toàn văn kịch bản ra màn hình chat và **CHỜ USER CHỐT DUYỆT CHÍNH THỨC** trước khi viết Chương 2. Tương tự, mỗi chương tiếp theo ($N$) bắt buộc phải được User nghiệm thu xong mới được viết chương ($N+1$).
   - **Chế tài Vi Phạm:** Nghiêm cấm hoàn toàn hành vi tự ý viết trước các chương tiếp theo khi chưa có lệnh nghiệm thu từ User. Mọi file chương viết sai quy định đều bị coi là rác hệ thống và bắt buộc phải xóa bỏ ngay lập tức.
6. **Bộ Lọc Khẩu Ngữ Tiền Khởi Động (Front-Loaded Oral Voice Guardrails):**
   - Gemini 3.8 Flash có xu hướng hành văn lý tính, kỹ trị và trang trọng nếu không được định hướng phong cách ngay từ đầu. Do đó, ngay từ khâu viết nháp, Agent **BẮT BUỘC phải khóa chết văn phong nói (Oral Voice DNA)**: Viết như một nhà quan sát điềm tĩnh đang ngồi uống trà chia sẻ góc nhìn với một người bạn thông minh.
   - Cấm tuyệt đối văn phong báo cáo khoa học, tiểu luận hàn lâm hay giọng thuyết giáo đạo lý. Áp dụng triệt để nguyên tắc "Writing for the Ear" (câu chủ động, giàu nhạc điệu, ngắt nghỉ tự nhiên theo nhịp thở).
7. **Sử dụng Narrative State Tracker (NST) & Giao thức Seeding-Harvesting:** Sử dụng tệp `09_narrative_state_tracker.md` (thay thế cho `09_continuity_packet.md`) để theo dõi chặt chẽ các vòng lặp câu hỏi (loops) và hạt giống chuyển tiếp (seeds). Bắt buộc thực hiện việc "gặt hạt" ở 1-2 câu đầu chương mới và "gieo hạt" ở 1-2 câu cuối chương hiện tại để đảm bảo tính liên kết dòng chảy chặt chẽ.
8. **Giao thức Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger - BẮT BUỘC):** Tuyệt đối CẤM kiểm toán ngầm trong suy nghĩ rồi tự tick xanh trong bóng tối. TRƯỚC KHI tạo tệp kịch bản thoại `chapter_XX.md`, Agent BẮT BUỘC phải in ra màn hình chat **Bảng Đối Soát Chứng Cứ Công Khai (Claim-to-Source Verification Ledger)**:
   - Phân loại rõ từng luận điểm dự kiến viết: `FACT` (có Footnote ID và trích dẫn ngắn ≤ 15 từ từ `research_vault/`) hay `GROUNDED_INFERENCE` (suy diễn logic từ Fact + Quy luật chi phí $T/V$ / First Principles).
   - Đánh trượt tức thì mọi suy diễn vô căn cứ (`FORBIDDEN_SPECULATION`: tự bịa thông số máy móc, tự đoán biên lợi nhuận hay động cơ nội bộ).
   - Không tạo các file passport phụ rườm rà, nhưng BẮT BUỘC phơi bày bảng đối soát ra màn hình chat để người dùng trực tiếp kiểm tra và nghiệm thu trước khi viết kịch bản sạch.
9. **Quy chuẩn Bắt buộc cho Pha 1: Bức Tranh Tầm Nhìn Toàn Cảnh & Bàn Cờ Hệ Thống (Master Systemic Topography & Global Vision Synthesis — Khung Tư Duy Phổ Quát 4 Tầng):**
   Tệp `01_global_vision_synthesis.md` là **BẢN ĐỒ ĐỊA HÌNH HIỆN THỰC KHÁCH QUAN (THE MAP OF REALITY)** và là **MỎ NEO TƯ DUY DUY NHẤT (SINGLE COGNITIVE ANCHOR)** của toàn bộ episode. Nó được kiến tạo ở Pha 1 ngay khi khởi động đề tài, độc lập hoàn toàn với việc chia chương hay kể chuyện. Nó mô tả bản chất của đề tài (kinh tế, xã hội, điều tra pháp lý, hồ sơ nhân vật, công nghệ...), các chủ thể, động lực sinh tồn, quy luật vận hành và hệ thống bằng chứng thực tế.

   ### 🛡️ NGUYÊN TẮC CHỦ THỂ ĐA HÌNH THÁI (POLYMORPHIC SUBJECT MANDATE — BẮT BUỘC):
   - ⛔ **CẤM TUYỆT ĐỐI BÓ HẸP CHỦ THỂ:** Nghiêm cấm Agent tự động mặc định "Chủ thể = Doanh nghiệp cụ thể hoặc Cá nhân người thật". Chủ thể là **TÂM CHẤN NHẬN THỨC (Cognitive Epicenter)** của đề tài, bắt buộc phải định danh chính xác thuộc 1 trong 5 Hình Thái Bản Thể:
     1. **Thực Thể Thể Chế / Pháp Lý (Institutional / Regulatory):** Một Nghị định, Đạo luật, Thông tư, Quy hoạch quốc gia, Hiệp định thương mại (VD: *Nghị định 100*, *Nghị định 116*, *Luật Đất đai 2024*, *California SB 1047*).
     2. **Thực Thể Ý Niệm / Học Thuyết (Ideological / Doctrine):** Một triết lý phát triển, trường phái tư tưởng, mô hình kinh tế (VD: *Triết lý "Sản xuất thực chất" vs "Địa tô phân lô"*, *Chủ nghĩa e/acc*, *Ngoại giao Cây tre*, *Tân Phong kiến Kỹ thuật số*).
     3. **Hiện Tượng Xã Hội / Nhân Khẩu Học (Socio-Demographic / Phenomenon):** Dân số, an sinh, tâm lý học hành vi (VD: *Khủng hoảng Viện dưỡng lão & Chữ Hiếu*, *Làn sóng tài xế tắt app*, *Thế hệ nằm yên Tang ping*).
     4. **Không Gian Địa Lý / Hạ Tầng / Lưu Vực (Geopolitical / Spatial / Infrastructure):** Một dòng sông, eo biển, bãi bồi, siêu công trình hạ tầng (VD: *Kênh đào Funan Techo*, *Vịnh Thái Lan*, *Bãi bồi sông Hồng Khoái Châu*, *Đại dự án ĐSCT 67 tỷ USD*).
     5. **Tổ Chức / Doanh Nghiệp / Liên Minh Kinh Tế (Corporate / Market Entity):** Tập đoàn sản xuất, chuỗi bán lẻ, ngân hàng trung ương, liên minh đa quốc gia (VD: *Hòa Phát & THACO*, *BYD*, *Nvidia*, *BoJ & Fed*).

   ### 🔍 BỘ 5 CÂU HỎI BẢN THỂ HỌC PHỔ QUÁT (UNIVERSAL 5-QUESTION SCOPING):
   Trước khi lập kế hoạch nghiên cứu, Hội đồng Chiến lược bắt buộc phải trả lời 5 câu hỏi gốc rễ theo đúng bản chất tự nhiên của hình thái chủ thể:
   1. **ENTITY ANCHORS (Thực thể mỏ neo):** Chủ thể trung tâm thực chất là AI/CÁI GÌ? Fact-sheet thô sơ bộ gồm những gì? (Số hiệu văn bản, mốc lịch sử, tọa độ địa lý, thông số cơ bản).
   2. **ARENA & CIRCUIT (Không gian vận động & Mạch truyền dẫn):** Chủ thể tồn tại trong môi trường nào? Mạch vận động chính là gì? (Chuỗi giá trị kinh tế, Cán cân quyền lực địa chính trị, Mạch luân chuyển trách nhiệm xã hội, hay Mạch máu tiền tệ?).
   3. **INCENTIVES & SURVIVAL (Động lực sinh tồn & Xung đột lợi ích):** Các bên tham gia muốn gì và sợ gì? Động lực thực sự ẩn sau lớp vỏ ngôn từ đạo đức là gì? (Lợi nhuận, bảo vệ quyền lực, sinh tồn, an ninh quốc gia).
   4. **GOVERNING LAWS & PARADOXES (Quy luật chi phối & Nghịch lý khách quan):** Quy luật khách quan nào đang điều khiển cuộc chơi mà các bên không thể làm trái? (Kinh tế học quy mô, địa chính trị, chu kỳ sinh học, nhân khẩu học, lý thuyết trò chơi).
   5. **CONTESTED EVIDENCE & DISSENT (Bằng chứng thực chứng & Phản biện đối soát):** Sự thật nằm ở đâu? Con số chính thức đối đầu với số liệu ngầm nào? Phe phản biện độc lập chỉ trích điều gì?

   ### 🏛️ CẤU TRÚC 4 TẦNG TƯ DUY PHỔ QUÁT CỦA FILE `01_global_vision_synthesis.md`:
   - **TẦNG 1: SYSTEM META-INSTRUCTIONS & COMPLIANCE GUARDRAILS (YAML/JSON-like):**
     * Tuyên bố rõ **Hình Thái Chủ Thể** và Quyết định phê duyệt của Hội đồng Chiến lược (`strategy_council_verdict`).
     * `compliance_blacklist`: Danh sách từ ngữ cấm sử dụng kèm từ ngữ thay thế an toàn chính luận.
   - **TẦNG 2: MACRO LANDSCAPE & SYSTEMIC FORCES (BẢN ĐỒ KHÔNG GIAN & CÁC LỰC LƯỢNG — SƠ ĐỒ ASCII BÀN CỜ):**
     * Sơ đồ ASCII toàn cảnh định vị không gian bàn cờ: Các chủ thể tham gia, động lực sinh tồn cốt lõi (Incentives), các dòng chảy chủ đạo và tương quan lực lượng.
   - **TẦNG 3: UNDERLYING MECHANICS & CENTRAL PARADOXES (QUY LUẬT VẬN HÀNH & NGHỊCH LÝ CỐT LÕI):**
     * Giải phẫu các mắt xích nhân quả gốc rễ (Root Causes) và khoảng cách giữa kỳ vọng/bề mặt vs thực tế/bản chất; xác định các nghịch lý ngầm và quy luật chi phối.
   - **TẦNG 4: TARGET GROUND-TRUTH EVIDENCE CHECKLIST & IMMUTABLE DATA VAULT:**
     * 💡 **HÓA GIẢI NGHỊCH LÝ CON GÀ & QUẢ TRỨNG (CHICKEN-AND-EGG PARADOX SOLUTION):**
       - Tại Pha 1: Tầng 4 đóng vai trò là **Danh Mục Mỏ Neo Dữ Liệu Cần Điều Tra (Target Evidence Checklist)** xác lập các chỉ tiêu định lượng, báo cáo kiểm toán, văn bản quy phạm cần truy lùng độc lập; TUYỆT ĐỐI CẤM Agent đoán mò hay tự bịa số liệu chi tiết khi chưa qua Deep Research.
       - Sau khi hoàn thành Pha 2 (Deep Research): Sổ cái mỏ neo `DATA-01` đến `DATA-XX` được cập nhật chính thức bằng **100% SỐ LIỆU THẬT ĐÃ KIỂM TOÁN TỪ VAULT** vào cả `02_research_map.md` và đồng bộ vào `01_global_vision_synthesis.md`.
   
   🛑 **VÙNG CẤM TUYỆT ĐỐI CỦA PHA 1 (HARD REDLINE — CHỐNG ÔM ĐỒM & CHỐNG TIỀN ĐỊNH DÀN Ý):**
   - **TUYỆT ĐỐI CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản nào:** `CH01`, `CHXX`, `Chương`, `Hồi`, `Hook`, `Scene`, `Voiceover Tone`, `Narrative Bridge`, `Harvest`, `Seed`.
   - **TUYỆT ĐỐI CẤM chia chương trước Pha 4:** Việc phân chia số chương, thời lượng, nhịp điệu, cấu trúc hồi, và phân bổ quota dữ liệu vào từng chương là **ĐẶC QUYỀN ĐỘC TÔN của Pha 4 (Master Outline Engine do `the_dialectic_architect` phụ trách)**.
   - **TUYỆT ĐỐI CẤM may đo rập khuôn:** Không gượng ép mọi đề tài vào một khuôn mẫu cứng nhắc (như ép phải có 3-4 trận địa, ép phải có máy móc công nghiệp hay ép phải có 7 chương). Mỗi đề tài được quyền thể hiện cơ chế và nghịch lý theo đúng bản chất hình học tự nhiên của nó.
   - **Chế tài vi phạm:** Mọi tệp `01_global_vision_synthesis.md` xuất hiện cấu trúc chia chương kịch bản hoặc số liệu bịa đặt thiếu nguồn kiểm toán đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và bắt buộc phải hủy bỏ để làm lại.
10. **QUY CHUẨN SỢI CHỈ ĐỎ TỰ SỰ KIỆT TÁC (WORLD-CLASS MASTERPIECE SPINE PROTOCOL - BẮT BUỘC):**
    Để đảm bảo kịch bản đạt chuẩn tác phẩm điều tra tài liệu đỉnh cao (tương đương Bloomberg Originals, PolyMatter), mọi tài liệu thượng nguồn từ Brief, Outline, Chapter Briefs đến Kịch bản thoại bắt buộc phải tuân thủ 4 rào cản tự sự:
    - **Rào cản 1 (The Single Spine):** Toàn bộ tập phim chỉ có DUY NHẤT một Biến cố trung tâm (Inciting Incident). 100% các chương phải trực tiếp phục vụ việc mổ xẻ, thử thách hoặc tháo ngòi biến cố đó. Tuyệt đối CẤM tư duy ngăn tủ (Silo Thinking) biến các chương thành bài giảng lịch sử/địa lý/chính sách độc lập rời rạc.
    - **Rào cản 2 (Therefore / But Momentum):** 100% các chuyển đoạn và chuyển chương phải được kết nối bằng động lực nhân quả "VÌ VẬY..." (Therefore) hoặc "NHƯNG..." (But). Nghiêm cấm hoàn toàn cấu trúc "VÀ RỒI..." (And Then).
    - **Rào cản 3 (Anti-Burying-The-Lede):** Tuyệt đối CẤM giấu nút thắt bản chất cốt lõi nhất xuống chương áp chót hoặc chương kết bài. Cú va chạm bản chất (mâu thuẫn cấu trúc sâu sắc nhất giữa giả định mô hình và quy luật khách quan) bắt buộc phải nổ ra ở Đỉnh cao trào Màn 2 (khoảng giữa video), để chương kết dành trọn vẹn không gian cho sự phản tư, đúc kết bài học dài hạn và tầm nhìn tương lai.
    - **Rào cản 4 (The Russian Doll):** Khám phá ở chương này tháo gỡ một lớp vỏ bề mặt nhưng phải lập tức làm lộ ra một tầng nghịch lý hiểm hóc hơn ở chương tiếp theo.
11. **GIAO THỨC ĐỘC QUYỀN THÔNG TIN & MỎ NEO ĐỔI LĂNG KÍNH (INFORMATION EXCLUSIVITY & PERSPECTIVE-SHIFTED ANCHORING - BẮT BUỘC):**
    - **Quy luật Một Sự Thật - Một Ngôi Nhà (Single-Occurrence Fact Protocol):** Mỗi số liệu, cơ chế kỹ thuật hay biến cố lịch sử chỉ được giải thích bản chất ĐÚNG MỘT LẦN DUY NHẤT tại chương được phân quyền. Bất kỳ chương nào phía sau muốn gọi lại bắt buộc phải dùng kỹ thuật Mỏ Neo Đổi Lăng Kính (Perspective Shift) trong tối đa 1-2 câu đầu, tuyệt đối cấm kể lại tiến trình sự việc.
    - **Cuộc Chạy Tiếp Sức Phân Vai (The Cognitive Relay Race):** Mỗi chương bắt buộc phải được dẫn dắt bởi một Lăng Kính Vai Trò Chuyên Môn độc tôn phù hợp với bản chất của đề tài. Việc đổi vai giúp người nghe luôn tiếp cận vấn đề dưới góc nhìn mới, triệt tiêu 100% việc lặp lại bối cảnh cũ.
12. **QUY TRÌNH KIẾN TRÚC DÀN Ý 5 TRẠM & KHÓA KHUNG ĐỊNH HƯỚNG (THE 5-STAGE OUTLINE FORGE & ORIENTATION FRAME MANDATE - BẮT BUỘC):**
    - **Trạm 1 (Khóa Quy Mô & Tổng Ngân Sách Toàn Tập):** Xác định Cấp độ thời lượng (Cấp 1: 8-15m, Cấp 2: 16-25m, Cấp 3: 26-35m, Cấp 4: 36-45+m) và khóa Tổng ngân sách từ $W_{\text{total}}$ với tốc độ chuẩn $V = 223\text{ từ/phút}$ (mốc dưới của chuẩn 223–235).
    - **Trạm 2 (Quy hoạch Lãnh thổ Dữ liệu & Kiểm kê Tải trọng):** Bổ quả cam `01_global_vision_synthesis.md` và `research_vault/` thành các phần độc quyền, cấp quota mã `DATA-XX` không trùng lặp cho từng chương, kiểm kê mỏ neo $D_i$ và mắt xích cơ chế $M_i$.
    - **Trạm 3 (Thiết kế Sóng Nhịp Điệu & Orientation Frame Khóa Cứng):** 
      * **ORIENTATION FRAME MANDATE (Khung Định Hướng 45–60s):** Trong kịch bản Chương 1, ngay sau khi kết thúc Hook (30–45s), kịch bản BẮT BUỘC phải dành 45–60 giây (khoảng 150–200 từ) để trao cho người xem **TẤM BẢN ĐỒ TOÀN CẢNH CỦA BÀN CỜ**. Khán giả phải nhìn thấy: 3 thế lực tham chiến, mâu thuẫn hệ thống ngầm, và lộ trình 3 trạm dừng chân sắp tới. Tuyệt đối cấm nhảy bổ vào số liệu chi tiết khi chưa trao bản đồ.
      * **Căn cứ tin cậy (Proof) trong Orientation Frame:** 1–2 câu cho người xem biết vì sao nên tin phân tích này: tập đứng trên nguồn gốc nào (báo cáo tài chính, văn bản pháp lý, số liệu thống kê chính thức, đối chiếu nhiều bên). Nêu nguồn và cách làm, không tự khen kênh, không tuyên bố độc quyền.
      * **Lộ trình không lộ đáp án:** 3 trạm dừng chân được nêu dưới dạng câu hỏi hoặc chặng, không nêu kết luận, để giữ Anti-Completion Rule của Chương 1.
      * **Khớp lời hứa:** Hook và Orientation Frame phải nhắc lại đúng "Lời hứa đóng gói" ở `01_global_vision_synthesis.md` (người vừa bấm vào phải thấy mình đến đúng chỗ).
      * **NHỊP THỞ ZOOM IN $\leftrightarrow$ ZOOM OUT:** Cứ sau một đợt phân tích kỹ thuật/số liệu vi mô sâu (Zoom In), kịch bản phải có 1–2 câu kéo người xem trở lại vị trí của họ trên bản đồ lớn (Zoom Out) để khán giả không bị "mù trong mê cung".
    - **Trạm 4 (Đúc Xương Sống Nhân Quả ABT):** Chuỗi các chương liên kết 100% bằng "Therefore / But" (0% "And Then") tích hợp Logic Arc và Tension Arc vào `07_outline.md`.
    - **Trạm 5 (Cổng Thẩm Định Tải Trọng, Lan Can Co Giãn & Phân Hạch):** Tính toán bộ ba thông số [Floor - Target - Ceiling], kiểm tra tải trọng tối thiểu (Anti-Amputation), kích hoạt quy tắc phân hạch nếu chương vượt trần $1.050\text{ từ}$, và xuất xưởng Chapter Briefs 16 trường.
13. **QUY CHUẨN BẮT BUỘC: NGUYÊN TẮC DÀN Ý TRƯỚC, HOOK SAU (THE OUTLINE-FIRST, HOOK-LAST PROTOCOL):**
    - **Bản chất Biên Tập:** Đối với thể loại Cinematic Editorial Noir (Phân tích kinh tế - chính sách chuyên sâu), **Hook là Lời Hứa (The Promise)** và **Dàn ý / Thân bài là Phần Thưởng (The Grand Payoff)**. Bạn không thể hứa hẹn những điều mà chính bạn còn chưa biết thân bài sẽ giải quyết ra sao. Viết Hook chi tiết trước khi có Dàn ý là nguyên nhân gốc rễ dẫn tới bẫy "Clickbait hứa hão", dẫm chân số liệu hoặc lệch pha tự sự.
    - **Trình tự 3 Bước Bắt Buộc:**
      * **Bước 1 — Master Systemic Topography & Packaging Concept (Pha 1 & Pha 3):** Pha 1 xây dựng `01_global_vision_synthesis.md` với Bàn cờ Hệ thống. Pha 3 (`03_brief.md`) xác định Tiêu đề, Thumbnail và Lời Hứa Cốt Lõi (Core Tension / Premise) để làm kim chỉ nam cho Dàn ý.
      * **Bước 2 — Master Outline Engine (Pha 4: `07_outline.md`):** Xây dựng hoàn chỉnh Xương sống 7 nhịp ABT, quy hoạch lãnh thổ dữ liệu độc quyền, Orientation Frame và định vị rõ ràng điểm bùng nổ / đắt giá nhất của video (**The Grand Payoff**).
      * **Bước 3 — Hook Lab (Pha 5: `04_hook_pack.md`):** Sau khi đã nắm chắc toàn bộ quân bài và bằng chứng của Dàn ý, mới kích hoạt Hook Lab để may đo kịch bản thoại 30-45 giây mở đầu. Từng câu chữ mở đầu lúc này cài cắm chính xác các vòng lặp câu hỏi mở (Open Loops) mà thân bài chắc chắn sẽ tháo ngòi, triệt tiêu 100% nguy cơ hứa hão và lặp ý.

## Nhánh Shorts — Lane song song, không thay thế long-form
Shorts là một content lane riêng. KHÔNG ép yêu cầu Shorts đi qua pipeline 16 pha của episode dài nếu user đang yêu cầu short-form.

### Nguồn gốc hợp lệ của Shorts
- **Shorts phái sinh:** lấy từ episode đã có sẵn asset dưới `episodes/[slug]/`
- **Shorts độc lập:** làm dưới `shorts/standalone/[slug]/`

### Intent Router cho Shorts
Khi user dùng ngôn ngữ tự nhiên như:
- "làm short"
- "cắt short"
- "YouTube Shorts"
- "short độc lập"
- "rút short từ episode này"

→ PHẢI route sang workflow `/generate_shorts`, không route sang `/generate_episode` hay `/write_chapter`.

### Rule cho Shorts
- Shorts không phải bản thu nhỏ cơ học của long-form.
- Mọi Short phải bám canonical files:
  - `00_core/shorts_style_guide.md`
  - `00_core/shorts_map_template.md`
- Shorts phái sinh nên lập kế hoạch theo `episodes/[slug]/shorts/shorts_map.md`.
- Shorts độc lập nên lập kế hoạch theo `shorts/standalone/[slug]/shorts_map.md`.
- Nếu user yêu cầu planning Shorts cho một episode, mặc định tư duy theo cụm **3-5 Shorts** trừ khi user chỉ muốn 1 short cụ thể.

## Human Approval Gates — DỪNG và chờ user duyệt
- Sau pha 1: Master Systemic Topography & Global Vision (`01_global_vision_synthesis.md` — Bản đồ Bàn cờ 4 Tầng)
- Sau pha 2: Topographical Deep Research (Research Map & Vault)
- Sau pha 3: Strategy Brief (`03_brief.md`)
- Sau pha 4: Master Outline Engine (Dàn ý 7 nhịp ABT & Orientation Frame)
- Sau pha 5: Hook Lab (May đo kịch bản thoại Hook bám sát Dàn ý)
- Sau pha 6: Chapter Briefs (16 Trường) & NST
- Sau pha 10-11: Editorial & Legal QA + Oral QA
- Sau pha 12: Visual Storyboard Blueprint (duyệt cốt truyện thị giác & mỏ neo trước khi viết prompt)
- Sau pha 16: Postmortem (review performance → pipeline adjustment)

## Cấm tuyệt đối
- KHÔNG chạy Deep Research ở Pha 2 khi chưa có `01_global_vision_synthesis.md` (BẮT BUỘC có Bản đồ Bàn cờ trước khi cào dữ liệu)
- KHÔNG viết chapters khi chưa có `07_outline.md`, `04_hook_pack.md` và `08_chapter_briefs.md`
- KHÔNG viết outline khi chưa có `03_brief.md` và `01_global_vision_synthesis.md`
- KHÔNG viết kịch bản thoại Hook (`04_hook_pack.md`) khi chưa có `07_outline.md` (BẮT BUỘC tuân thủ nguyên tắc Dàn Ý Trước, Hook Sau)
- KHÔNG viết song song các chương (Parallel writing). Phải viết TUẦN TỰ từng chương một.
- KHÔNG viết chương tiếp theo khi chưa nạp và đọc lại các chương trước để đảm bảo tính liền mạch.
- KHÔNG viết full script one-shot từ chủ đề thô
- KHÔNG bịa đặt số liệu thống kê hoặc trích dẫn chuyên gia
- KHÔNG đưa ra bình luận chính trị nhạy cảm, xuyên tạc chủ trương hoặc vi phạm an ninh quốc gia
- KHÔNG dùng từ ngữ phán xét đạo đức một chiều tiêu cực
- CẤM TUYỆT ĐỐI GỌI API BÊN NGOÀI ĐỂ SINH NỘI DUNG VÀ PROMPT: Nghiêm cấm viết hoặc chạy các script Python, bash hoặc các công cụ tự động gọi API của các mô hình ngôn ngữ lớn bên ngoài (như OpenAI, Gemini, Anthropic...) để viết nháp, dịch, tóm tắt hoặc biên tập chương. Agent bắt buộc phải tự dùng LLM của IDE đọc file chapter briefs trực tiếp và tự tay viết văn bản sạch cho voiceover.
- CẤM DÙNG SCRIPT PYTHON LOOP ĐỂ GHÉP VÀ SINH PROMPT HÀNG LOẠT: Mọi prompt và kịch bản phải do LLM của IDE tự phân tích và viết một cách tự nhiên, chất lượng, nhất quán, tránh chắp vá cơ học bằng code python.
- TUYỆT ĐỐI CẤM sử dụng bất kỳ đoạn code/script tự động hóa nào (Python, Bash, Node.js...) để tạo, chỉnh sửa hoặc dịch nội dung các tệp prompt hình ảnh (visual prompts). Tất cả các prompt hình ảnh phải được thiết kế và biên soạn trực tiếp, thủ công bằng năng lực ngôn ngữ và tư duy thẩm mỹ của AI (LLM) để đảm bảo bối cảnh nghệ thuật và tránh sai lệch ngữ nghĩa.

## Quy chuẩn phân chia phân cảnh khoa học (Veo 3.1 8s)
- **Giao thức Đồng bộ Toán học (Bắt buộc):** Mỗi video clip sinh ra từ Google Veo 3.1 mặc định dài **8.0 giây**. Tốc độ đọc voiceover tiếng Việt trung bình của narrator kênh GocNhinPodcast là **3.81 từ/giây**. Với ngưỡng thời lượng an toàn cho mỗi cảnh là **7.0 giây** (Safety Margin 1.0 giây so với clip 8.0 giây), mỗi phân cảnh đơn hoặc phân cảnh phụ tuyệt đối **không được chứa quá 26 từ thoại**. Nếu cụm câu thoại dài hơn 26 từ, bắt buộc phải chia nhỏ thành $K = \lceil W / 26 \rceil$ phân cảnh phụ (`a1`, `a2`, `a3`...) và phân bổ đều số lượng từ thoại sang các cảnh phụ đó. Nghiêm cấm để các phân cảnh phụ có thoại rỗng `[]` khi cảnh trước bị quá tải từ (>26 từ).
- **Tính toán WPS thực tế:** Thời lượng của các phân cảnh được tính toán tự động bằng script:
  - `WPS = Tổng số từ / Thời lượng audio thực tế` (nếu chưa có audio, dùng WPS mặc định = 3.81 từ/giây).
  - `Thời lượng câu = Số từ của câu / WPS`.
- **Nguyên tắc Gom và Tách:**
  - *Chương 1 (Hook):* Không gộp các câu thoại. Mỗi câu thoại tối đa là 1 phân cảnh. Nếu câu thoại dài hơn 26 từ, bắt buộc tách đôi thành các sub-scenes con (`SCXXXa1`, `SCXXXa2`...).
  - *Từ Chương 2 trở đi đến Chương kết (Thân/Kết bài):* Gom các câu thoại liên tiếp sao cho tổng số từ của phân cảnh `<= 26 từ`. Nếu câu tiếp theo làm tổng số từ vượt quá 26 từ ➡️ Tách cảnh và tạo sub-scenes con.
- **Quy chuẩn tag & prompt:** Nhãn tag phân cảnh bắt buộc dùng định dạng chuẩn theo chương `CHXX_SCYYY` (ví dụ `CH01_SC001`, `CH01_SC002`... reset theo từng chương). Nội dung prompt xuất ra tệp `prompts_chapter_XX.txt` hoặc `prompts_master.txt` theo cặp đôi `[IMAGE]` và `[VIDEO]` tương thích 100% với công cụ `tools/flow_batch_studio/` và 100% không chứa bất kỳ ký tự tiếng Việt có dấu nào.

## Nguyên tắc Dễ hiểu là tối thượng & Bảo toàn Bản chất (Comprehensibility & Essence Preservation)
Mặc dù số liệu và chính sách phải chính xác 100%, kịch bản PHẢI viết cho người bình thường hiểu bằng tai khi nghe qua video. Cấm tuyệt đối:
1. **Sao chép máy móc điều khoản luật/chính sách:** Phải chuyển ngữ các điều khoản khô khan thành bản chất động lực thực tế (ai được lợi, ai chịu rủi ro, rào cản dựng lên để giải quyết vấn đề gì).
2. **Hình tượng hóa sai lệch bản chất (CẤM CẨU THẢ):** Dùng phép so sánh đời thường (Metaphor) là bắt buộc, nhưng phép so sánh phải phản ánh đúng 100% cơ chế thực tế. Tuyệt đối không được bóp méo cơ chế pháp lý, tài chính hoặc địa lý (không dùng từ ngữ thông tục làm thay đổi bản chất nghĩa vụ pháp lý, quyền tài sản hay phạm vi không gian).
3. **Nhồi số liệu dồn dập:** Không nhồi quá 2 số liệu hoặc tỉ lệ % trong một câu đơn.
4. **Bỏ qua giải thích bản chất:** Mọi thuật ngữ chính sách, kinh tế, xã hội khó hiểu khi đưa vào kịch bản bắt buộc phải đi kèm một phép loại suy đời thường hoặc câu giải thích bản chất dễ hiểu ngay lập tức.
5. **Đứt gãy dòng chảy Hook - Outline:** Mọi xung đột kịch tính, câu hỏi lớn, bí ẩn hay nghịch lý được gieo ở Hook là một lời hứa nhận thức, BẮT BUỘC phải được giải quyết ngay ở các chương đầu tiên của kịch bản theo đúng dòng chảy tâm lý của người nghe, không để khán giả chờ đợi vô lý.
6. **Văn phong hành chính/thư lại:** Không được để việc tuân thủ các quy trình đối chiếu số liệu làm giảm tính hấp dẫn, kịch tính và trôi chảy của nghệ thuật kể chuyện (Storytelling). Viết như một nhà quan sát kinh tế điềm tĩnh đang trò chuyện thân mật bên bàn trà với một người bạn thông minh.

## Quy tắc thiết kế Prompt hình ảnh bắt buộc (Pha 12 & 12.5)

### 0. Giao thức Khởi tạo Storyboard Matrix & Cổng Cách Ly Thoại (Zero-Voiceover Isolation - BẮT BUỘC)

- **Phân định rạch ròi 2 chuyên gia độc lập:**
  * **Pha 12B (Kịch bản thị giác trung gian `chapter_XX_visual.md`):** Do **`the_scene_architect` (Kiến Trúc Sư Phân Cảnh & Biên Kịch Thị Giác)** độc quyền phụ trách. Đọc kịch bản thoại `chapter_XX.md`, bẻ nhịp toán học $\le 26$ từ/cảnh, giải phẫu 3 tầng cơ học (`Chủ thể` - `Hành động` - `Không gian`) thuần túy hiện thực đời sống Việt Nam, khử nhiễm 100% ẩn dụ văn học.
  * **Pha 12C (Soạn thảo Prompts I2V `prompts_chapter_XX.txt`):** Do **`the_image_prompt_composer` (Nhà Soạn Prompt Hình Ảnh)** phụ trách dưới sự chỉ đạo nghệ thuật của `the_visual_storyteller`.

- **🛑 CỔNG CÁCH LY THOẠI BẮT BUỘC (MANDATORY ZERO-VOICEOVER ISOLATION GATE):**
  * Khi thực hiện Pha 12C (`prompts_chapter_XX.txt`), Agent **TUYỆT ĐỐI BỊ CẤM NẠP HOẶC ĐỌC KỊCH BẢN THOẠI GỐC (`chapter_XX.md`)**.
  * Nguồn dữ liệu DUY NHẤT để biên dịch sang prompt tiếng Anh là cột `[BỐI CẢNH]` (Chủ thể - Hành động - Không gian) và `[TEXT OVERLAY]` của `chapter_XX_visual.md`.
  * **Chế tài vi phạm:** Nghiêm cấm hoàn toàn hành vi nhìn câu thoại tiếng Việt để dịch thoát ý (paraphrase) sang tiếng Anh. Mọi hành vi tự ý dịch nghĩa đen từ ngữ tu từ (như dịch "không được chia một xu" thành tiền xu `coins`, dịch "tuân thủ" thành tòa án cột đá Mỹ, dịch "cỗ máy" thành bánh răng, dịch "bức tường/gọng kìm/mỏ neo" thành vật thể siêu thực) đều bị coi là **VI PHẠM KỶ LUẬT HỆ THỐNG** và sẽ bị hủy bỏ toàn bộ tệp prompt để làm lại từ đầu.

- **🏛️ GIAO THỨC ĐỊNH DANH THƯƠNG HIỆU & HIỆN THỰC ĐỜI SỐNG VIỆT NAM (GROUNDING REALISM MANDATE):**
  1. *Định danh phương tiện & đồng phục 1-1:*
     - **GrabBike:** Bắt buộc mô tả: `authentic Vietnamese GrabBike driver wearing signature forest green jacket with distinct horizontal white stripes across chest and shoulders, matching green Grab helmet, driving a classic Honda Wave motorcycle`. Cấm dùng từ ngữ chung chung `motorcycle taxi driver` khiến AI vẽ nhầm sang áo vàng/logo hãng Be hay Gojek.
     - **GrabCar:** Bắt buộc mô tả: `authentic Vietnamese GrabCar driver wearing neat dark polo shirt seated behind steering wheel of a 4-seater sedan car (Toyota Vios / Hyundai i10)`.
     - **Green SM:** Bắt buộc mô tả: `cyan-teal electric taxi (VinFast VF e34 / VF 5) or electric scooter (VinFast Feliz / Evo), driver wearing professional cyan-teal collared uniform`.
  2. *Hiện thực công vụ & đời sống Việt Nam:*
     - Khung cảnh cơ quan quản lý: Bàn làm việc công vụ Việt Nam, màn hình laptop hiển thị Cổng thông tin điện tử `.gov.vn` (như Ủy ban Cạnh tranh Quốc gia VCC), hồ sơ thanh tra có dấu mộc đỏ. Tuyệt đối CẤM kiến trúc cột đá Hy Lạp/La Mã hoặc tòa án tư pháp kiểu Mỹ.
     - Khung cảnh tài chính: Sử dụng tiền giấy/polymer Việt Nam mệnh giá nhỏ (10.000đ, 20.000đ, 50.000đ), hợp đồng tín dụng ngân hàng vay mua xe, hoặc số dư ví điện tử trừ tự động. CẤM TUYỆT ĐỐI xuất hiện tiền xu (`coins`).

- Ma trận `chapter_XX_visual.md` bắt buộc có 3 trường thông tin cho mỗi phân cảnh để tước quyền tự quyết định bối cảnh của khâu viết prompt:
  * `[THOẠI]:` Câu thoại cắt chuẩn $\le 26$ từ (Dùng làm thước đo 8s và làm bản đồ ghép nối audio cho Hậu kỳ).
  * `[BỐI CẢNH]:` Bóc tách rõ 3 tầng: Chủ thể (rõ danh tính/phương tiện) - Hành động vật lý cụ thể - Không gian đời thực Việt Nam (phải tuân thủ Global Blueprint, triệt tiêu 100% siêu thực).
  * `[TEXT OVERLAY]:` Đánh giá xem cảnh có cần chữ hay không (chỉ 20-25% cảnh mấu chốt). Ghi rõ chữ cần hiển thị hoặc ghi "Không".

### 0.2. Quy trình Kiểm tra Đối chiếu Đồng bộ Prompt - Visual Script Tự động (CHỐNG LÃNG PHÍ TIỀN BẠC/CREDITS)
- **Rào cản Kiểm tra Cứng (Pre-Render Automated Audit Gate):** Trước khi xuất bản bất kỳ tệp prompt nào (`prompts_chapter_XX.txt`) cho người dùng sử dụng để sinh ảnh/video (NanoBanana 2 / Veo 3.1), Agent BẮT BUỘC phải thực hiện lệnh quét đối chiếu tự động bằng Python giữa `chapter_XX_visual.md` và `prompts_chapter_XX.txt`.
- **2 Điều kiện Bắt buộc phải Đạt 100%:**
  1. **Khớp 100% tất cả các Scene ID** (Bao gồm các cảnh phụ `a/b/c`). Không được thiếu bất kỳ cảnh nào, không được dồn nhiều cảnh vào 1 prompt trừ khi được quy định rõ.
  2. **Khớp 100% Ngữ nghĩa Trực quan với Bối Cảnh trong Visual Script:** Nội dung mô tả trong prompt `[IMAGE]` phải lấy trực tiếp từ trường `[BỐI CẢNH]` tương ứng trong `chapter_XX_visual.md`.
- **Quy tắc Dừng Khẩn cấp (Emergency Stop Protocol):** Nếu phát hiện số lượng cảnh trong `chapter_XX_visual.md` khác với số cặp prompt trong `prompts_chapter_XX.txt` ➡️ DỪNG TOÀN BỘ QUY TRÌNH NGUYÊN HIỆM. Cấm gửi prompt cho User render video cho đến khi đã sửa và đạt 100% khớp chuẩn.

### 0.3. Quy Chuẩn Vận Động & Hành Động An Toàn Cho Model Video Tier Thấp (Veo 3.1 Lite / Low-Priority Engine Safeguards)
Mô hình Google Veo 3.1 Lite (hoặc các mô hình video tier thấp/nhẹ chạy ở chế độ Low-Priority) dự đoán chuỗi khung hình dựa trên xác suất 2D mà không có mô phỏng vật lý 3D nội tại. Khi gặp các hành động cơ thể phức tạp hoặc chuyển động cơ học tốc độ cao, mô hình sẽ gặp hiện tượng "mất trí nhớ thời gian" (temporal instability), dẫn đến các lỗi quái dị: tay chân tan chảy, ngón tay biến dạng, thân xe bẹp dúm, người đi xuyên vật thể, mặt méo mó như zombie làm video trở nên rẻ tiền và mất uy tín.

Để đảm bảo hình ảnh điện ảnh, sang trọng, chuẩn mực phóng sự điều tra và AN TOÀN 100% cho Veo 3.1 Lite, **BẮT BUỘC TUÂN THỦ DANH MỤC CẤM & KHUYẾN NGHỊ DƯỚI ĐÂY Ở CẢ PHA 12B VÀ 12C:**

1. **🚫 DANH SÁCH ĐEN CÁC HÀNH ĐỘNG TUYỆT ĐỐI CẤM (BLACKLIST):**
   * **CẤM thao tác ngón tay chi tiết (Fine Finger Manipulation):** Tuyệt đối KHÔNG mô tả: ngón tay bấm màn hình điện thoại, vuốt app, xòe tiền đếm, móc ví, xé giấy, gõ bàn phím, cầm bút ký.
   * **CẤM tiếp xúc vật lý giữa nhiều người (Multi-character Contact):** Tuyệt đối KHÔNG mô tả: khách đưa tiền cho tài xế, bắt tay, ôm, va chạm, trao đổi đồ vật (khiến cơ thể của 2 người bị hòa tan/dính liền vào nhau).
   * **CẤM cử động toàn thân phức tạp (Complex Biomechanics):** Tuyệt đối KHÔNG mô tả: người đi bộ thẳng về phía camera (khiến chân bị trượt/sliding và biến dạng), bước lên/xuống xe, chạy nhảy, xoay người 180 độ, vung tay chỉ trỏ giận dữ.
   * **CẤM vật lý xe cộ phức tạp (Complex Vehicle Dynamics):** Tuyệt đối KHÔNG mô tả: xe bẻ lái rẽ cua, quay đầu, drift, va chạm, vượt nhau, lạng lách (khiến thân xe bị bẹp rúm hoặc bánh xe trượt ngang phi vật lý).
   * **CẤM cử động cơ mặt cực đoan & Nói chuyện (Extreme Facial Morphing & Lip-sync):** Tuyệt đối KHÔNG mô tả: nhân vật há mồm nói chuyện, cười to, khóc lóc, trợn mắt tức giận (tạo ra gương mặt quái đản, biến dạng).

2. **✅ DANH SÁCH TRẮNG CÁC HÀNH ĐỘNG & HIỆU ỨNG AN TOÀN TUYỆT ĐỐI (WHITELIST):**
   * **Chủ thể ở tư thế nghỉ/tĩnh vững chãi (Anchored / Resting Pose):**
     - Tài xế ngồi trên xe máy dừng chờ đèn đỏ, hai tay nắm chắc ghi-đông ở tư thế tĩnh.
     - Tài xế ngồi trong cabin ô tô, tay đặt nhẹ trên vô lăng nhìn thẳng ra đường phố.
     - Nhân vật đứng tựa lưng điềm tĩnh, hoặc ngồi bên bàn trà đá/bàn làm việc, ánh mắt tập trung suy tư.
     - Chiếc điện thoại thông minh gắn cố định trên giá đỡ ghi-đông xe, màn hình HUD tĩnh.
   * **Chuyển động Camera Điện ảnh (Cinematic Camera Moves trên Chủ thể Tĩnh):**
     - `Slow push-in dolly`: Camera tịnh tiến chậm về phía chủ thể đang đứng/ngồi tĩnh điềm đạm.
     - `Slow horizontal pan / tracking shot`: Camera trượt ngang lướt qua hàng xe đang đỗ hoặc qua góc phố.
     - `Slow tilt-up / tilt-down`: Camera quét dọc từ mặt đường/bánh xe lên dáng người tài xế.
     - `Steady medium shot`: Khung hình tĩnh khóa nét hoàn toàn (BẮT BUỘC cho cảnh có Text Overlay).
   * **Chuyển động Môi trường & Khí quyển (Atmospheric Motion):**
     - Hạt mưa phùn rơi nhẹ, vệt nước mưa chảy chậm trên kính chắn gió.
     - Khói/hơi nước mỏng bốc lên từ cốc trà nóng hoặc quán ăn ven đường.
     - Ánh đèn xe thành phố lướt nhẹ phản chiếu trên mặt đường ướt (giao thông hậu cảnh bị xóa phông bokeh mịn).
     - Gió nhẹ làm lay lay góc áo khoác hoặc lá cây ven đường.
   * **Cử động vi mô tinh tế của Nhân vật (Subtle Micro-motions):**
     - Nhân vật chớp mắt tự nhiên, hơi thở nhẹ nhàng, đầu hơi nghiêng nhẹ 5-10 độ quan sát đường phố, duy trì biểu cảm điềm tĩnh (composed expression).

### 0.4. Giao Thức Khóa Logic Vật Lý Khép Kín Giữa Ảnh & Video (Closed-Loop Physical Affordance Protocol)
AI Video (như Google Veo 3.1) sở hữu "thiên kiến vận động tự động" (Default Motion Prior): khi nhìn thấy ô tô hoặc xe máy trong ảnh đầu vào, mô hình có xu hướng tự động cho xe lăn bánh/di chuyển về phía trước. Nếu ảnh đầu vào mô tả một chủ thể đang ở trạng thái bị trói buộc cơ học (Tethered / Anchored State) mà dòng prompt video không khóa cứng chuyển động của chủ thể, AI sẽ tạo ra những chuyển động phi logic quái dị (ví dụ: xe đang cắm sạc điện nhưng vẫn phóng đi kéo lê trụ sạc, xe đang cắm vòi bơm xăng vẫn chạy giật đứt dây bơm, xe hạ chân chống vẫn trượt lết trên đường, người đang ngồi ghế lại trượt xuyên qua ghế).

Để triệt tiêu vĩnh viễn các lỗi phi logic này, hệ thống bắt buộc thực thi 3 nguyên tắc khóa cơ học khép kín:

1. **Ma Trận 6 Cặp Trạng Thái Vật Lý Đối Nghịch (The 6 Incompatibility Traps):**
   * **Bẫy 1: Nạp năng lượng (Cắm sạc điện / Cắm vòi xăng):**
     - Nếu ảnh có dây sạc cắm vào cổng sạc xe điện, hoặc vòi bơm xăng cắm vào bình xăng:
     - 🛑 Dòng `[VIDEO]` TUYỆT ĐỐI CẤM bất kỳ chuyển động nào của phương tiện.
     - 🔒 BẮT BUỘC chèn lệnh khóa bất động (Immobility Anchor): `the vehicle remains completely stationary and parked in the charging/refueling bay with cable/nozzle firmly attached, zero vehicle movement, wheels motionless, only camera moves`.
   * **Bẫy 2: Hạ chân chống / Đỗ xe (Kickstand Down / Parked on curb):**
     - Nếu ảnh có chân chống xe máy hạ chạm mặt đường:
     - 🛑 Dòng `[VIDEO]` TUYỆT ĐỐI CẤM xe lăn bánh. Bắt buộc: `motorcycle remains completely parked with kickstand firmly planted, zero vehicular movement`.
     - Ngược lại, nếu muốn xe di chuyển trong video: Ảnh `[IMAGE]` bắt buộc phải vẽ xe đang trên đường, chân chống đã gạt lên, hai chân tài xế đặt trên thanh gác chân.
   * **Bẫy 3: Cửa xe / Cốp xe / Nắp bình xăng mở (Open doors / Open trunk / Open fuel cap):**
     - Khi cửa xe, nắp capo, cốp xe hoặc nắp bình xăng đang mở trong ảnh:
     - 🛑 Dòng `[VIDEO]` xe bắt buộc phải đứng yên tĩnh tuyệt đối. Tuyệt đối cấm xe phóng đi khi cửa/cốp đang mở toang.
   * **Bẫy 4: Thiết bị gá kẹp cố định (Mounted / Clamped Devices):**
     - Khi điện thoại được kẹp chặt trên giá đỡ ghi-đông kim loại:
     - 🛑 Dòng `[VIDEO]` TUYỆT ĐỐI CẤM tài xế nhấc điện thoại ra khỏi giá đỡ, áp vào tai nghe, hoặc cầm đi nơi khác. Chỉ cho phép camera zoom/push-in vào màn hình.
   * **Bẫy 5: Tư thế ngồi ghế / Tựa lưng (Seated on Stool / Bench / Chair):**
     - Khi nhân vật đang ngồi trên ghế nhựa, ghế đá hoặc tựa lưng vào tường:
     - 🛑 Dòng `[VIDEO]` TUYỆT ĐỐI CẤM yêu cầu nhân vật đứng dậy hoặc bước đi (sẽ gây lỗi trượt xuyên qua vật thể). Chỉ cho phép cử động vi mô (nghiêng đầu, chớp mắt, thở).
   * **Bẫy 6: Tài xế buông tay lái (Hands off controls):**
     - Nếu ảnh vẽ tài xế buông tay khỏi ghi-đông/vô lăng (đặt tay trên đùi):
     - 🛑 Phương tiện bắt buộc phải đỗ tĩnh 100%. Tuyệt đối cấm xe đang di chuyển trên đường mà tài xế không cầm lái.

2. **Cơ Chế Phân Định Rạch Ròi Tại Pha 12B (The Scene Architect):**
   * Trong cột `[BỐI CẢNH]` của `chapter_XX_visual.md`, Kiến trúc sư phân cảnh bắt buộc phải khai báo rõ một trong 2 nhãn trạng thái:
     - `[TRẠNG THÁI: TĨNH KHÓA CỨNG (TETHERED / PARKED)]`: Đi kèm danh sách vật thể trói buộc (dây sạc, vòi xăng, chân chống, giá đỡ).
     - `[TRẠNG THÁI: VẬN HÀNH ĐỘNG (TRANSIT)]`: Xe chạy thẳng đều, không có bất kỳ dây nhợ hay chân chống nào.

3. **Giao Thức Khóa Bất Động Tự Động Tại Pha 12C (The Image Prompt Composer):**
   * Khi dòng `[IMAGE]` xuất hiện bất kỳ từ khóa nào thuộc nhóm Khóa Cứng (`charging cable connected`, `fueling nozzle inserted`, `kickstand planted`, `clamped on mount`, `seated on stool`, `hands resting on lap`):
   * Dòng `[VIDEO]` BẮT BUỘC PHẢI CHỨA cụm từ khóa kháng chuyển động (Immobility Anchor):
     `[subject] remains completely motionless and stationary throughout the shot, wheels completely locked, zero vehicle translation, only camera moves`.

### 1. Giao thức Đạo diễn Tổng thể & Biên soạn Tuần tự (Global Director & Sequential Writer Protocol - BẮT BUỘC)
Quy trình thiết kế hình ảnh và video không được phép làm rời rạc hay chắp vá ngẫu hứng. Để đảm bảo tính nhất quán cao nhất về mặt cốt truyện, bối cảnh nghệ thuật và dàn nhân vật, toàn bộ quá trình bắt buộc phải đi qua 3 bước nghiêm ngặt sau:

*   **Bước 1: Đánh giá Kịch Bản Tổng Thể (Global Director Assessment):** Trước khi viết prompt hình ảnh, Agent đóng vai trò Đạo diễn Kịch bản (Script Director) cần dựa vào Dàn ý (`07_outline.md`) và Tóm tắt (`08_chapter_briefs.md`) để nắm bắt được toàn cảnh thông điệp, nhịp điệu và dòng chảy tự sự, thay vì đọc toàn bộ kịch bản chi tiết để tránh quá tải bộ nhớ.
*   **Bước 2: Lập Kế Hoạch Trực Quan Tổng Thể (Global Visual Planning):** Đạo diễn tiến hành phân tích kịch bản và viết ra một bản kế hoạch trực quan tổng thể, định nghĩa rõ:
    - *Bối cảnh nghệ thuật chủ đạo (Global Context/Setting):* Lấy cảm hứng từ vũ trụ ẩn dụ nào (Noir Detective, Industrial Machine, hay Digital Ledger)? Quy chuẩn không gian vật lý là gì?
    - *Dàn nhân vật thống nhất (Cast Sheet):* Xác định các nhân vật chính/phụ sẽ xuất hiện (ví dụ: mô tả chi tiết tiếng Anh của nhân vật Pham Nhat Vuong, Ratan Tata, các trợ lý, người lao động...). Mô tả này sẽ được sao chép nguyên văn 100% khi vẽ nhân vật đó ở bất kỳ cảnh nào.
    - *Các thương hiệu và sản phẩm thực tế (Brands & Products):* Xác định rõ tên các thương hiệu (VinFast, Vingroup, Samsung...) và mã sản phẩm thực tế (xe VF 8, VF 9, điện thoại VSmart...) để chuẩn bị thông tin vẽ chi tiết.
*   **Bước 3: Đọc và Viết Tuần Tự Từng Chương (Sequential Chapter Writing):**
    - Sau khi bản kế hoạch tổng thể được duyệt, Đạo diễn sẽ đọc lại chi tiết từng chương một (từ Chương 1 -> Chương cuối).
    - Tiến hành biên soạn prompt hình ảnh cho chương hiện tại. Khi viết chương N, luôn đặt mình trong bối cảnh tổng thể và dòng chảy liên tục từ Chương N-1 sang Chương N+1 (Áp dụng Cửa sổ Ngữ cảnh 3 Phân cảnh - Tri-Scene Context Window).

### 2. Phân Tách Tệp Prompts Riêng Cho Từng Chương (Chapter-Isolated Prompts Protocol - BẮT BUỘC)
Mỗi chương bắt buộc phải có một tệp prompt riêng biệt được lưu trữ trực tiếp tại thư mục của tập phim theo cấu trúc định dạng:
**`episodes/[slug]/prompts_chapter_XX.txt`** (Ví dụ: `prompts_chapter_01.txt`, `prompts_chapter_02.txt`...).
Nghiêm cấm ghi đè hoặc gộp chung toàn bộ các chương vào một tệp dùng chung để tránh loãng bối cảnh nghệ thuật.
Mỗi phân cảnh bắt buộc phải được triển khai theo cặp đôi gồm 2 dòng liên tiếp (ngắt dòng đơn) và phân cách với phân cảnh khác bằng 1 dòng trống:
*   **Dòng 1 - Static Design `[IMAGE]`:** Prompt thiết kế ảnh tĩnh chi tiết 5 lớp để làm ảnh tham chiếu (đầu vào I2V).
    *   *Cú pháp:* `CHXX_SCYYY [IMAGE]: [Mô tả chi tiết bối cảnh, chất liệu, ánh sáng, nhãn chữ tiếng Anh]`
*   **Dòng 2 - Motion Design `[VIDEO]`:** Prompt mô tả chuyển động camera/vật lý trỏ tới ảnh nguồn tĩnh đã khai báo.
    *   *Cú pháp:* `CHXX_SCYYY [VIDEO]: @CHXX_SCYYY.png -> [Camera & physical motion] preserving the details of the reference image, 8-second continuous documentary video --ar 16:9`


*   **Cổng xác nhận luồng bắt buộc (Clarification Gate):** TRƯỚC KHI thực hiện Pha 12/12.5, nếu người dùng không yêu cầu rõ ràng là sử dụng luồng **Text-to-Video (T2V)** hay luồng **Image-to-Video (I2V)** cho tập phim/phân cảnh, Agent **bắt buộc phải dừng lại và hỏi rõ ý định của người dùng**, tuyệt đối không tự ý giả định hay tự động chạy. (Lưu ý: Mặc định luôn khuyến khích luồng I2V cặp đôi qua `prompts_master.txt` để đảm bảo chất lượng mỹ thuật).

### 2. Giao thức Đồng bộ ID Tuyệt đối (ID Mapping Protocol)
*   Mọi prompt ảnh tĩnh và prompt chuyển động video bắt buộc phải sử dụng chung một khóa ID phân cảnh dạng **`CHXX_SCYYY`** làm tiền tố (ví dụ: `CH01_SC010`).
*   Đối với dòng `[VIDEO]`, tệp ảnh tham chiếu bắt buộc trỏ tới `@CHXX_SCYYY.png` khớp chính xác 100% với ID phân cảnh ở đầu dòng. Nghiêm cấm dùng lệch ID tệp ảnh.

### 3. Quy chuẩn mô tả trực quan & Kỹ thuật
- **Quy chuẩn 2D Vector phẳng (CẤM ẢNH CHỤP NGƯỜI THẬT/VẬT THẬT):** Tuyệt đối cấm sử dụng hình ảnh tả thực (photorealism) hoặc 3D mô phỏng thực tế. Toàn bộ hình ảnh tĩnh và chuyển động bắt buộc hiển thị dạng nét vẽ đồ họa 2D vector phẳng (flat 2D vector graphic). Mọi prompt ảnh tĩnh bắt đầu bằng: `A flat 2D vector illustration of...` hoặc `A 2D vector silhouette of...` và kết thúc bằng: `, clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, sophisticated modern slate background color / warm ivory cream ambient tone (#FAF7EE), luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows`.
- **Giao thức Đồng bộ Toán học (Bắt buộc):** Mỗi phân cảnh hoặc phân cảnh phụ tuyệt đối **không được chứa quá 26 từ thoại** tiếng Việt (theo quy chuẩn thời gian 8.0 giây của Veo 3.1).
- **Chữ viết hiển thị trên màn hình (Typography) & Quy tắc Chọn lọc (Selective Ratio ~25%):** Mô hình tạo ảnh NanoBanana 2 có khả năng kết xuất chữ tiếng Việt có dấu cực kỳ chuẩn xác (dòng `[IMAGE]`). Tuy nhiên, **TUYỆT ĐỐI CẤM chèn Text Overlay trên 100% các phân cảnh**. Chỉ chèn chữ vào **~20% - 25% phân cảnh QUAN TRỌNG/THÔNG SỐ KEY** (mốc thời gian, số liệu chính, tiêu đề tuyên bố). 75% - 80% phân cảnh còn lại phải để `[TEXT OVERLAY]: Không` để giải phóng không gian mỹ thuật và cho phép Veo 3.1 chuyển động camera động. Đối với mô hình tạo video Veo 3.1 Lite (I2V) ở các cảnh CÓ chữ, ở dòng `[VIDEO]` bắt buộc dùng `steady shot` và câu lệnh khóa chữ: `preserving all details and static graphic layers of the reference image exactly without any character morphing or alterations`.
- **Tạo hình nhân vật phù hợp ngữ cảnh & rộng rãi (Cấm đồ bó sát gợi cảm):** Tuyệt đối cấm sử dụng các danh từ mập mờ đơn độc dễ kích hoạt AI sinh ra hình ảnh người mặc đồ bó sát lộ đường cong (ví dụ: tránh dùng "mysterious figure", "silhouette of a woman"). Thay vào đó, trang phục và tạo hình nhân vật bắt buộc phải phù hợp linh hoạt nhất với bối cảnh lịch sử, địa lý của phân cảnh, đồng thời bắt buộc phải rộng rãi, kín đáo (ví dụ: bối cảnh hiện đại dùng `a man in a loose-fitting business suit` hoặc `a man wearing a loose detective trench coat`; bối cảnh cổ trang dùng `flowing traditional robes`; bối cảnh lao động dùng `loose working clothes`). Bắt buộc chỉ định các từ khóa trang phục rộng rãi (`loose`, `loose-fitting`, `flowing`) để tạo nét bóng hình hộp vững chãi, trung tính. Con người và địa danh của nước nào phải hiển thị chính xác chủng tộc và bối cảnh nước đó (ví dụ: Vietnamese features cho người Việt Nam) nhưng được vẽ dưới dạng đồ họa phẳng 2D.
- **Cơ chế Diện mạo Trung tính & Bỏ qua Bộ lọc An toàn AI (Zero-Bias Likeness Formula - BẮT BUỘC):** Tuyệt đối CẤM đưa tên riêng của người thật còn sống (như "To Lam", "Elon Musk", "Wang Chuanfu") vào prompt tiếng Anh ở cả dòng `[IMAGE]` và `[VIDEO]` vì sẽ kích hoạt AI Celebrity/Safety Filter khiến tác vụ bị hủy bỏ. Hãy sử dụng tag ảnh tham chiếu `@filename.ext ->` ở đầu dòng `[IMAGE]` kết hợp mệnh đề trung tính: `A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo...`. Ở dòng `[VIDEO]`, tuyệt đối không dùng tên riêng, dùng danh từ chung (`the leader`, `the entrepreneur`, `the man`) kèm `maintaining their composed facial expression and all details of the reference image exactly`.
- **Vũ trụ Ẩn dụ Chủ đạo (Visual Archetype Unity):** Cả kịch bản thị giác bắt buộc phải chọn và trung thành với 1 vũ trụ ẩn dụ duy nhất định nghĩa trong Blueprint (Noir Detective, Industrial Machine, hoặc Digital Ledger). Nghiêm cấm pha trộn ngẫu hứng các phong cách không gian khác biệt.
- **Nhất quán Nhân vật (Visual Cast Sheet Integrity):** Khi viết prompt cho một nhân vật có mặt trong Cast Sheet của Blueprint, bắt buộc phải sao chép nguyên văn 100% khối mô tả tiếng Anh nhận dạng của nhân vật đó ở dòng `[IMAGE]`. Nghiêm cấm tự ý thay đổi đặc tính nhân vật để tránh lệch mặt qua từng cảnh.
- **Quy chuẩn Nhận thức Vật lý & Chuyển động Camera Đa dạng (Cognitive Physics & Cinematic Motion Protocol - BẮT BUỘC):** Trợ lý viết prompt phải có nhận thức sâu sắc về nội dung hình học và thực thể vật chất có trong ảnh tĩnh `[IMAGE]` để thiết kế chuyển động `[VIDEO]` tương thích vật lý tự nhiên, thay vì áp dụng máy móc các lệnh Pan/Zoom đơn điệu:
  1. *Chuyển động của Thực thể (Subject Physics):* Nếu trong ảnh có xe điện $\rightarrow$ xe phải lăn bánh tịnh tiến; có bánh răng $\rightarrow$ phải quay chậm chịu lực ép; có dòng chất lỏng/dòng vốn $\rightarrow$ phải chảy xiết hoặc rò rỉ; có vết nứt $\rightarrow$ phải rạn lan rộng; có đồng cát/bụi $\rightarrow$ phải cuốn bay hoặc lắng xuống.
  2. *Góc máy Cinematic Đa dạng:* Áp dụng linh hoạt các chuyển động camera chuyên sâu phù hợp với tính chất vật lý của vật thể:
     - **Tilt up / Tilt down (Lướt dọc):** Sử dụng cho các thực thể có chiều cao hoặc độ sâu (nhà máy VinFast đồ sộ, hố sâu sụp đổ, cột trụ thăng bằng).
     - **Dolly-in / Dolly-out (Tịnh tiến chiều sâu):** Di chuyển camera xuyên không gian tạo hiệu ứng thị sai (parallax) rõ rệt giữa tiền cảnh và hậu cảnh.
     - **Rack Focus (Chuyển nét):** Camera đứng im nhưng chuyển nét từ tiền cảnh sang hậu cảnh (hoặc ngược lại) để hướng sự chú ý của người xem (ví dụ: chuyển nét từ bánh răng sang gương mặt nhân vật).
     - **Slow Orbit / Arc shot (Chuyển động vòng cung):** Camera xoay nhẹ 15-30 độ quanh một mô hình trung tâm trên sa bàn chỉ huy.
  3. *Quy tắc khóa cứng chữ viết (Text-morphing Safeguard):* Chỉ áp dụng cú máy tĩnh (`steady shot`) hoặc pan cực nhẹ khi phân cảnh có hiển thị **chữ tiếng Việt có dấu**. Nếu phân cảnh chỉ chứa chữ tiếng Anh ngắn hoặc không có chữ, bắt buộc phải giải phóng camera để áp dụng các góc máy động nâng cao nêu trên nhằm tăng tính nghệ thuật.
- **Cấm tuyệt đối lỗi "Thầy bói xem voi" (Keyword-triggered Hallucinations):** AI không được phép chỉ đọc 1-2 từ khóa đơn độc (như "lậu", "khởi tố") rồi tự ý chế tác bối cảnh xa rời nội dung tổng thể (như vẽ máy bay, hộ chiếu, hải quan, phòng xử án). Mọi hình ảnh bắt buộc phải bám sát ngữ cảnh thực tế của câu chuyện (ví dụ: đang nói về quy trình kiểm định phòng Lab thì bối cảnh vật lý bắt buộc phải là phòng Lab, dụng cụ thí nghiệm, thước đo điện tử, bàn gỗ mahogany).
- **Nhất quán Tuyến Tính Xuyên Suốt (Narrative Continuity):** Đạo diễn luôn phải đặt mình trong dòng chảy cốt truyện, đọc hiểu toàn bộ kịch bản từ Chương 1 đến Chương cuối để kế thừa bối cảnh vật lý, đảm bảo mỏ neo chuyển dịch logic, tránh tạo ra các phân cảnh rời rạc không ăn nhập.
- **Mạch Nối Động Liên Tiếp (Matched Movement & Relational Prompting):** Trực quan của Scene $N$ phải được thiết kế nối tiếp điểm kết thúc của Scene $N-1$ về góc máy, vị trí hoặc hành động. Tránh các cú nhảy camera ngẫu nhiên (jump cuts) không liên kết.
  * **CẤM TUYỆT ĐỐI** viết các từ tham chiếu phi vật lý (meta-words như `previous scene`, `next scene`, `former scene`) vào trong phần mô tả tả cảnh tiếng Anh.
  * **Cú pháp bắt buộc:** Sử dụng ngôn ngữ vật lý tự thân (self-contained description). Bắt buộc bắt đầu prompt bằng mô tả trực quan của vật thể ở giây thứ 0: `Starting with a close-up of [vật thể/điểm lấy nét ở cuối Scene N-1], [chuyển động camera] showing...` hoặc `Starting with a steady shot of [vật thể], ...`.
- **Cửa sổ Ngữ cảnh 3 Phân cảnh (Tri-Scene Context Window - BẮT BUỘC):** Quy trình sinh prompt bắt buộc phải diễn ra theo chuỗi tuần tự chuyển tiếp (Stateful Flow), nghiêm cấm sinh hàng loạt độc lập. Khi thiết kế prompt cho phân cảnh $N$, Agent bắt buộc phải nạp đủ 3 chiều dữ liệu:
  1. *Quá khứ:* Bản dịch prompt thực tế của Phân cảnh $N-1$ để kế thừa chính xác trạng thái vật lý của vật thể ở giây cuối cùng (để tả lại vật thể đó ở giây thứ 0 của phân cảnh $N$ hiện tại).
  2. *Hiện tại:* Lời thoại/ý nghĩa kịch bản của Phân cảnh $N$ cần diễn đạt.
  3. *Tương lai:* Xem trước (preview) nội dung của Phân cảnh $N+1$ để chủ động điều phối góc máy ở cuối phân cảnh (Exit Vector) nhằm đón đầu và kết nối mượt mà với cảnh tiếp theo.
- **Tuyệt đối cấm sử dụng các mô tả sáo rỗng rác (Anti-Boilerplate constraint):** Nghiêm cấm sử dụng các câu mô tả rập khuôn kiểu đối phó ("glowing digital lines representing transaction flows..."). Mỗi phân cảnh bắt buộc phải có mô tả hành động vật lý đặc thù, cụ thể và tương thích trực tiếp với lời thoại.
- **Tránh text tiếng Việt trong prompt:** Tuyệt đối không dùng các từ khóa hoặc câu tiếng Việt làm tham chiếu text trong phần mô tả prompt tiếng Anh để tránh AI render ra chữ tiếng Việt bị lỗi font/lỗi nghĩa.
- **Đại diện nhân chủng học:** Mô tả rõ chủng tộc/ngoại hình nhân vật phù hợp với ngữ cảnh quốc gia (người Việt Nam - Vietnamese, người nước ngoài - foreign expert).
- **Trực quan hóa quốc gia bằng Quốc kỳ:** Khi một quốc gia được đề cập nổi bật trong lập luận, hãy kết hợp hiển thị quốc kỳ tương ứng của quốc gia đó một cách tự nhiên trong bố cục.
- **Tiêu đề chữ trên THUMBNAIL bắt buộc phải có DẤU TIẾNG VIỆT đầy đủ:** Tuyệt đối không viết tiêu đề thumbnail không dấu. Phải ghi đúng chính tả tiếng Việt có dấu đầy đủ (ví dụ: "NGHỊCH LÝ VINFAST", "CÀNG LỖ CÀNG MỞ RỘNG"). Chỉ định rõ trong prompt cách AI viết từng chữ có dấu để đảm bảo độ chính xác.

### 4. Giao Thức Sản Xuất Cuốn Chiếu Từng Chương & Tự Kiểm Toán Trước Bàn Giao (Rolling Chapter Pipeline & Zero-Defect Auto-Fix Protocol - BẮT BUỘC)
- **Quy tắc Cuốn Chiếu Bắt Buộc (Rolling Chapter-by-Chapter Execution):**
  * Làm chương nào dứt điểm chương đó: `chapter_XX_visual.md` ➔ `prompts_chapter_XX.txt` ➔ tự kiểm toán đối soát 1-1 pass 100% rồi mới chuyển chương tiếp theo. (TUYỆT ĐỐI KHÔNG sinh hay đồng bộ tệp `scene_timing_map.json`).
  * **Định danh phân cảnh chuẩn theo chương (BẮT BUỘC):** 100% Scene ID phải có định dạng `CHXX_SCYYY` (ví dụ `CH01_SC001`, `CH01_SC002`... sang Chương 2 reset lại `CH02_SC001`, `CH02_SC002`...). TUYỆT ĐỐI CẤM đánh số toàn cục `SC001 -> SC240`.
- **Quy chuẩn Text Overlay Bắt Buộc:**
  * Chỉ chèn chữ vào ~20%-25% phân cảnh then chốt, 75%-80% để "Không".
  * Vị trí cố định: **Góc trái màn hình phía dưới, cách mép đáy 25%** (`positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge`), chữ nhỏ gọn thanh thoát (`compact subtle`), trực diện ống kính, bóng đổ đen dày.
  * Cảnh có chữ: Video prompt bắt buộc dùng `Steady camera shot` để khóa tĩnh chữ chống méo font.
- **Quy trình 5 Bước Tự Rà Soát & Khắc Phục Bắt Buộc Trước Khi Bàn Giao:**
  1. *Chuẩn hóa ID & Đồng bộ 1-1:* Đảm bảo 100% Scene ID là `CHXX_SCYYY`, khớp tuyệt đối 1-1 giữa Kịch bản Thị giác (`chapter_XX_visual.md`) và Tệp Prompts (`prompts_chapter_XX.txt`).
  2. *Triệt tiêu 100% Trừu tượng hóa & Ẩn dụ siêu thực (100% Physical Realism Mandate):* 100% bối cảnh phải là không gian vật lý đời thực (nhà xưởng, cảng biển, bến tàu, showroom, đường phố, phòng họp, tài liệu hợp đồng). Tuyệt đối CẤM dịch nghĩa bóng thành vật thể siêu thực: cái cân công lý, tấm khiên rạn nứt, vòng kim cô, nút thắt cáp trong hư vô, kẹp ê-tô đối thủ, hố sâu chi phí, dấu chấm hỏi lơ lửng, bánh đà triết lý, bàn tay vô hình.
  3. *Chống Tây hóa Nhân vật:* Quét 100% prompt có nhân vật trong bối cảnh Việt Nam, bắt buộc phải có `Vietnamese male/female [vai trò]`. Nếu thấy từ chung chung (`an engineer`, `a worker`) ➡️ **Sửa lại ngay lập tức**.
  4. *Khóa Tĩnh Lớp Chữ:* Mọi cảnh có Text Overlay bắt buộc dòng `[VIDEO]` phải là `Steady camera shot` khóa chữ ở góc dưới trái cách đáy 25%.
  5. *Toán học Phân cảnh:* Đảm bảo 100% câu thoại $\le 26$ từ/cảnh (thời lượng $\le 7.0$s).




## Core files phải tham chiếu
Khi làm bất kỳ bước lớn nào, đọc:
- `00_core/channel_bible.md` — giọng kênh
- `00_core/audience_personas.md` — chân dung người xem
- `00_core/brand_safety_guidelines.md` — vùng cấm biên tập & pháp lý
- `00_core/voiceover_style_guide.md` — chuẩn voice over
- `00_core/longform_blueprint.md` — kiến trúc long-form
- `00_core/quality_rubric.md` — rubric chất lượng
- `00_core/anti_patterns.md` — anti-patterns cần tránh
- `00_core/performance_benchmarks.md` — baseline và retention patterns
- `00_core/retention_gate_checklist.md` — cổng chặn retention (Gate 1, 2, D)

## Bảng Chuyên Gia Bắt Buộc Theo Pha — HARD GATE

> 📋 **DATA LOADING PROTOCOL**
> Trước khi sinh nội dung, Agent PHẢI dùng `view_file` đọc SKILL file và Persona file tương ứng. Việc đọc dữ liệu và viết nội dung CÓ THỂ diễn ra trong cùng một lượt chat — không cần tách riêng lượt báo cáo.

> ⛔ ĐÂY LÀ NGUYÊN TẮC CAO NHẤT. Mỗi pha phải dùng ĐÚNG chuyên gia được chỉ định. Agent PHẢI dùng tool `view_file` đọc persona file VÀ SKILL file tương ứng trước khi tạo output. NGHIÊM CẤM tạo output nếu chưa đọc.

> 📢 **EXPERT CONTEXT (TÙY CHỌN):**
> Khi chuyển chuyên gia, agent NÊN ghi ngắn gọn tên chuyên gia và pha đang thực hiện. Không bắt buộc banner đầy đủ — ưu tiên tốc độ và chất lượng output hơn hình thức.
> Bảng phân công chuyên gia DUY NHẤT là bảng 16 pha ở đầu file này. Persona nằm ở `.agents/personas/<tên>.md`, skill ở `.agents/skills/<tên>/SKILL.md`, workflow ở `.agents/workflows/<tên>.md`. (Bảng đánh số cũ 1–17 đã bỏ ngày 29/09/2026 vì lệch số pha và trỏ tới skill không tồn tại.)

> Gốc hệ đường dẫn: `/Users/pro16/Documents/VideoProject/GocNhinPodcast/`
> Ví dụ đường dẫn đầy đủ: `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_content_strategist.md`

## Quy tắc Chống Kịch Bản Rác & Lỗi Logic (Anti-Garbage & Logic Gate Rules)

Để triệt tiêu các lỗi ngô nghê làm mất uy tín và giảm giá trị của kịch bản, mọi Agent khi tham gia viết kịch bản bắt buộc phải thực thi các nguyên tắc sau:

1.  **Cấm Tuyệt Đối Hành Vi Ba Phải (Anti-Yes-Man Rule):**
    *   Agent không được phép sao chép thụ động các bản thảo thô hoặc các sửa đổi từ phía người dùng nếu chúng làm hỏng mạch logic tài chính hoặc vi phạm thực tế lịch sử.
    *   Agent **phải chủ động kiểm toán** (Audit) logic và phản biện trước khi viết: *"Đoạn này đã có liên kết nhân quả chưa? Có bị gãy ý không? Có mâu thuẫn thực tế không?"*.

2.  **Chuẩn hóa Phân Đoạn Kịch Bản (Không ngắt dòng mỗi câu):**
    *   Giới hạn 150 ký tự/câu của máy đọc TTS là **giới hạn kỹ thuật cứng**, bắt buộc tuân thủ.
    *   Phương pháp ngắt câu để tối ưu cho RunPod TTS: **Ngắt câu cơ học bằng dấu chấm (.) hoặc dấu chấm phẩy (;)** tại điểm nghỉ hơi tự nhiên trên cùng một dòng văn, tuyệt đối không bẻ câu què quặt về ngữ pháp.
    *   Kịch bản phải được nhóm thành các đoạn văn (paragraphs) trôi chảy từ 2 đến 4 câu có liên kết nội dung chặt chẽ. Tuyệt đối không được xuống dòng liên tục (double newline) sau mỗi câu đơn độc để tránh làm kịch bản bị vụn vặt và giọng đọc bị đứt quãng cơ học.

3.  **Chuẩn hóa Định Dạng Tệp Kịch Bản Chương (Không ghi thông tin vận hành):**
    *   Tệp kịch bản `chapter_XX.md` chỉ chứa tiêu đề `# chapter_XX.md` và các đoạn văn kịch bản thoại sạch sẽ. Tuyệt đối không đưa mô tả hình ảnh hoặc Visual: cues vào kịch bản.
    *   Tuyệt đối không ghi bản tổng hợp "TOÀN CẢNH VIDEO", "Tuyên bố sẵn sàng", các checklists của Pre-flight Gate hoặc operator logs vào tệp `chapter_XX.md`. Các thông tin này chỉ được in ra trong phần phản hồi chat của Agent để báo cáo tiến độ.

4.  **Khóa Cứng Tư Duy Đa Chiều & Thể Chế Hóa Hội Đồng Phản Biện Đa Diện (Tri-Adversarial Red Team & Steelman Mandate):**
    *   **Hội Đồng Phản Biện Đa Diện (The Tri-Adversarial Red Team Council):** Mọi đề tài bắt buộc phải trải qua cuộc sát hạch đối kháng của 3 lăng kính độc lập do `the_critical_auditor` chủ trì:
        1. *The Market Skeptic (Thị trường & Chi phí cơ hội):* Bóc trần méo mó phân bổ vốn, bao cấp làm lệch lạc thị trường, doanh nghiệp xác sống, chi phí cơ hội vĩ mô.
        2. *The Institutional Realist (Thể chế & Địa chính trị):* Bóc trần ma sát quan liêu, nhóm lợi ích cố thủ, rủi ro trả đũa thuế quan/chuỗi cung ứng quốc tế.
        3. *The Forensic Cash Auditor (Kế toán Dòng tiền & Thanh khoản):* Soi dòng tiền tự do FCF âm, tỷ lệ nợ ngắn hạn/dài hạn, điểm hòa vốn viển vông, áp lực thanh khoản.
    *   **Bắt Buộc Có [THE DEVIL'S CHAPTER] Tại Cao Trào Hồi 2:** Cấu trúc Outline BẮT BUỘC dành 1 chương độc lập (50–70% thời lượng, chiếm 18–24% ngân sách từ) mang nhãn `[THE DEVIL'S CHAPTER — CHƯƠNG PHẢN ĐỀ BẢN CHẤT]`. Chương này đứng hẳn về phía phe đối lập ở phiên bản Steelman mạnh nhất, dồn toàn bộ dữ liệu đối kháng để thử lửa luận điểm chính.
    *   **Tam Đoạn Luận Phản Biện 3 Nhịp (The 3-Beat Steelmanning Mandate):** Tuyệt đối CẤM ngụy biện bù nhìn rơm (Strawman) hoặc phản biện hình thức (*"Tuy nhiên, một số ý kiến cho rằng X, nhưng thực tế là Y"*). Mọi luận điểm chính BẮT BUỘC triển khai qua 3 nhịp: (1) Công kích Phản đề Thép bằng dữ liệu đối kháng sắc sảo nhất, (2) Thừa nhận động lực sinh tồn và tính chính đáng của bên phản biện, (3) Hợp đề bằng quy luật khách quan và công khai thừa nhận sự đánh đổi cấu trúc (`admitted_trade_offs`).
    *   **Bắt Buộc Phân Tích Đánh Đổi (Trade-offs) & Chi Phí Cơ Hội (Opportunity Costs):** Mọi phân tích mô hình, chính sách hoặc chiến lược đều PHẢI chỉ rõ: Ai đang hưởng lợi vs Ai đang âm thầm gánh chịu chi phí/rủi ro? Chi phí cơ hội của quốc gia/xã hội là gì? Hệ lụy phụ (Unintended Consequences) trong 3–5 năm tới là gì?
    *   **Kết Luận Có Điều Kiện (Conditional Conclusion):** Tuyệt đối CẤM kết luận nhị nguyên đen-trắng (người tốt - kẻ xấu, đúng tuyệt đối - sai tuyệt đối). Mọi kết luận đều phải đi kèm các điều kiện ràng buộc về thể chế, nguồn vốn và bối cảnh quốc tế.

---

## Quy Trình Nâng Cao: I2V+ (Multimodal Hybrid Visual Production Pipeline)

### 1. Định Vị & Triết Lý Vận Hành
Quy trình **I2V+** là bước nâng cấp chiến lược từ quy trình I2V truyền thống (thuần 100% video minh họa AI), hướng tới tiêu chuẩn phim tài liệu điều tra báo chí quốc tế (*Bloomberg Originals, Financial Times Film, Netflix Explained, Vox*).
- **Khóa Kỹ Năng Độc Quyền:** Quy trình I2V+ **BẮT BUỘC** dẫn đường bởi `.agents/skills/visual_prompter_plus/SKILL.md`. Tuyệt đối cấm dùng lẫn kỹ năng I2V cổ điển.
- **Bãi Bỏ Hạn Ngạch Cơ Học $\to$ Bản Thể Luận 4 Trụ Cột Nhận Thức (No Arbitrary Percentages):**
  1. `B_ROLL_REAL`: Mỏ neo của Niềm tin & Bằng chứng pháp lý, nhân chủng học đời sống lao động, vận hành công nghiệp thật.
  2. `FORENSIC_CALLOUT`: Mỏ neo của Bằng chứng Hồ sơ & Báo chí thực chứng (`The Evidentiary Smoking Gun`). Bài báo chính thống, quyết định xử phạt, kết luận thanh tra, thông cáo báo chí.
  3. `INFOGRAPHIC_DATA`: Kính lúp của Trí tuệ & Cú khai phóng nhận thức (`The "Aha!" Moment`). Bóc tách cấu trúc vô hình, đối kháng định lượng, luồng logistics và tài liệu kiểm toán.
  4. `VEO_AI`: Linh hồn Thẩm mỹ & Hero Shots (`Existential Awe & Poetic Gravitas`). Siêu ẩn dụ triết học, không gian kín nội tâm lãnh đạo, đại cảnh mở/kết chương.

### 2. Cây Quyết Định Bản Thể Học Đạo Diễn (Ontological Decision Tree — 4 Bước)
Khi duyệt qua từng phân cảnh ($\le 26$ từ thoại), Đạo diễn bắt buộc phân loại theo 4 câu hỏi kiểm định:
- **Bước 1 (Tính vô hình của cơ chế):** Ý niệm có phải là cấu trúc toán học, đối kháng định lượng, tỷ lệ nợ, hay mô hình kinh tế không thể quay bằng máy quay? $\rightarrow$ **Gán nhãn: `[MODALITY: INFOGRAPHIC_DATA]`**
- **Bước 2 (Bằng chứng hồ sơ & Báo chí thực chứng):** Lời thoại trích dẫn trực tiếp phát ngôn gây chấn động, quyết định xử phạt, kết luận thanh tra, bài điều tra báo chí? $\rightarrow$ **Gán nhãn: `[MODALITY: FORENSIC_CALLOUT]`**
- **Bước 3 (Mỏ neo thực tế & Bằng chứng vật lý):** Sự việc có xảy ra trong thế giới vật lý, có con người lao động thật, hiện trường máy móc thật, hoặc tư liệu lưu trữ/phóng sự? $\rightarrow$ **Gán nhãn: `[MODALITY: B_ROLL_REAL]`**
- **Bước 4 (Chiều sâu nội tâm & Ẩn dụ điện ảnh):** Thuộc về sự giằng xé nội tâm lãnh đạo, không gian kín phòng họp đêm, siêu ẩn dụ triết học, hoặc đại cảnh mở/kết chương? $\rightarrow$ **Gán nhãn: `[MODALITY: VEO_AI]`** *(Tuân thủ nghiêm ngặt Vùng Cấm Thép Veo AI: Cấm vẽ cảnh đời thường, cấm vẽ đồ thị/núi nợ, cấm vẽ mặt người thật).*

### 3. Quy Chuẩn Bằng Chứng Báo Chí & Phòng Thủ Pháp Lý Sạch (Fair Use & Điều 25 Luật SHTT)
1. **Phạm Vi Trích Dẫn Hợp Pháp:** Trích đoạn micro-quotation 3.0s – 5.5s phục vụ nghiên cứu, bình luận khoa học và phân tích kinh tế vĩ mô. Giữ nguyên măng-sét tờ báo uy tín hạng A (VnExpress, Tuổi Trẻ, Đầu Tư, CafeF, Lao Động, Bloomberg, Cổng TTĐT Chính Phủ...).
2. **CẤM DÍNH BẪY BẢN QUYỀN ẢNH PHÓNG SỰ:** Khi chụp ảnh bài báo, **CHỈ LẤY PHẦN TEXT (Tiêu đề, sapo, số liệu)**. Tuyệt đối làm mờ (blur/mask) hoặc crop bỏ hoàn toàn ảnh chụp phóng sự của phóng viên tờ báo đó để triệt tiêu 100% rủi ro khiếu nại bản quyền tác phẩm nhiếp ảnh.
3. **TUYỆT ĐỐI CẤM ĐƯA ẢNH BÁO CHÍ VÀO VEO AI:** Veo 3.1 Lite không đọc được chữ tiếng Việt có dấu (gây méo mó/melting ký tự), không đồng bộ được nhịp gạch chân với lời thoại, và gây lãng phí chi phí.
4. **Tiền Kết Xuất Video Báo Chí Bằng Python Motion Engine:** Tự động kết xuất ra video `.mp4` Full HD 1080p 60fps (hoặc 4K) có chuyển động Ken Burns chậm, hiệu ứng nét gạch chân điện ảnh (Cinematic Underline) hoặc khung viền đỏ bo chữ (`#DC2626`), kết hợp âm thanh click nhẹ (`minimal_click.wav`) hoặc lướt giấy (`paper_slide.wav`). AutoCapCut chỉ việc nạp file MP4 này vào timeline như clip thông thường.

### 4. Bốn Nguyên Tắc Thép Cho Footage B-Roll Fair Use
1. **Mute Absolute:** Tước sạch 100% audio gốc (`ffmpeg -an`).
2. **Micro-Cut 3.0s – 5.5s:** Tuyệt đối không dùng một đoạn trích dài quá 6 giây liên tục.
3. **Pixel Hash Breaking:** Scale 104% và crop nhẹ để bẻ gãy mã nhận diện Content ID tự động.
4. **On-Screen Attribution:** Dán nhãn trích nguồn minh bạch ở góc màn hình (`Nguồn: C-SPAN / Bloomberg / TTXVN`).

### 5. Hệ Thống 4 Tệp Đầu Ra Song Song Của Pha 12+C
Từ kịch bản trung gian `chapter_XX_visual_plus.md`, hệ thống phân tách thành 4 tệp dữ liệu chuyên biệt:
1. `prompts_chapter_XX_veo.txt`: Chứa các cặp prompt `[IMAGE]` và `[VIDEO]` cho Flow Tool Builder (Veo 3.1 Lite).
2. `broll_manifest_chapter_XX.json`: Danh mục link, query tìm kiếm, timecode cut (`start`, `end`) và nhãn nguồn cho `the_footage_hunter`.
3. `infographics_chapter_XX.json`: Bản đặc tả loại biểu đồ, số liệu, layout thẻ card và bảng màu cho AutoCapCut / Motion Graphics.
4. `forensic_manifest_chapter_XX.json`: Bản đặc tả bài báo (tên báo, link/ảnh bài báo, headline, từ khóa gạch chân, style gạch chân/khung viền, timecode và SFX) nạp cho `render_forensic_engine.py` tiền kết xuất thành video MP4 sắc nét 100%.



