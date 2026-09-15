# Antigravity Workspace Rules — X-Economics

## Mission
This repository is a content operating system for producing long-form English YouTube investigative documentary scripts about global macroeconomics, geopolitics, supply chain choke-points, and industrial strategy.

## Required operating mode
Always work in: Plan -> Execute -> Verify.
Never jump directly from a raw topic to a full script.

### 🛑 Dual-Stage Language Protocol & Mandatory User Approval Gates:
1. **Giai đoạn 1 (Tư duy & Kịch bản gốc — 100% TIẾNG VIỆT):**
   - Mọi tài liệu: Khảo cứu, Dàn ý (Outline), Hook Lab, và Kịch bản từng chương BẮT BUỘC PHẢI VIẾT BẰNG TIẾNG VIỆT để User trực tiếp đọc, thẩm định, phản biện và kiểm duyệt.
   - TUYỆT ĐỐI CẤM viết kịch bản bằng tiếng Anh khi bản thảo tiếng Việt chưa được User duyệt "OK HẾT".
2. **Giai đoạn 2 (Chuyển ngữ sang Tiếng Anh):**
   - CHỈ thực hiện sau khi kịch bản tiếng Việt đã được User duyệt hoàn tất 100%.
3. **Cổng kiểm duyệt bắt buộc (Mandatory User Gates):**
   - Cổng Duyệt Dàn ý: User duyệt mới làm Hook.
   - Cổng Duyệt Hook Lab: AI tạo 3-5 hooks tiếng Việt, BẮT BUỘC DỪNG LẠI in ra chat chờ User duyệt chọn. CẤM AI tự chọn Hook rồi tự viết tiếp!
   - Cổng Duyệt Kịch bản Tiếng Việt: Viết kịch bản tiếng Việt, trình User duyệt từng chương. User duyệt "OK HẾT" mới được dịch sang tiếng Anh.

## Source of truth
The repository files are the source of truth, not chat memory.
Always read and update files.

## Mandatory core files
Always consult:
- `00_core/channel_bible.md`
- `00_core/audience_personas.md`
- `00_core/brand_safety_guidelines.md`
- `00_core/hook_library.md`
- `00_core/longform_blueprint.md`
- `00_core/voiceover_style_guide.md`
- `00_core/quality_rubric.md`
- `00_core/anti_patterns.md`

## Mandatory episode state
Every episode must maintain:
- `01_topic_qualification.md`
- `02_research_map.md`
- `03_brief.md`
- `04_hook_pack.md`
- `05_thesis_map.md`
- `06_retention_map.md`
- `07_outline.md`
- `08_chapter_briefs.md`
- `09_continuity_packet.md`
- `10_claim_ledger.md`
- `chapter_XX.md`
- `10_compliance_report.md`
- `google_ai_audit_results.md` (kèm các file `google_ai_audit_XX.md` và `google_ai_audit_XX.png` tương ứng từng chương)
- `visual_storyboard_blueprint.md`, `scene_timing_map.json` & `prompts_chapter_XX.txt` (Pha 12 — Chỉ khi có yêu cầu)
- `production_notes.md`
- `postmortem.md`

## Never do these
- never fabricate public statistics, demographic data, or expert quotes
- never violate Vietnamese media regulations, cybersecurity laws, or make unverified political claims
- never use politically sensitive or instigating terms
- never write a 20–30 minute script one-shot
- never skip continuity updates after a chapter
- never use random visuals in final mapping
- never use moralizing tones to judge individuals or groups (use Incentive Analysis instead)
- never automatically generate image prompts, music prompts, or run TTS/voiceover recording without explicit user requests.
- never use external LLM APIs (like OpenAI, Gemini API, Anthropic API, etc.) inside python scripts or other automation tools to read script files, write outlines, create content, or generate prompts. MUST use the IDE's native LLM (the current running model) via built-in file reading tools to read files, think, and write contents directly. Never delegate thinking/generation to external APIs.
- never write scripts in English or translate to English before the Vietnamese script is fully reviewed, edited, and approved ("OK HẾT") by the user.
- never automatically select a hook or advance to chapter writing without the user explicitly choosing and approving the hook from Hook Lab.
- never execute multiple pipeline phases autonomously without pausing and getting approval at mandatory user approval gates.

## Quality constraints
- Start from everyday societal observations, public pain points, or shocking data, not abstract theory
- Keep voice intellectual, data-driven, empathetic, and spoken
- Preserve one dominant analytical function per chapter
- Use editorial caution, ensure balanced perspectives (Steelman), and always include compliance disclaimers
- Remove repetition aggressively
- Optimize for retention and oral delivery
- Every chapter must have at least 1 concrete data point, decree, or expert quote
- **BẮT BUỘC CẤU TRÚC KẾT CHƯƠNG 2 PHẦN (MANDATORY CHAPTER CLOSING DUALITY):** Mọi chương (từ CH01 đến CH07) ở phần kết thúc BẮT BUỘC phải có đầy đủ 2 khối rõ rệt:
  1. **Khối Tổng kết & Đóng chương (Chapter Closure / Payoff):** Đúc kết lại bài học, bản chất cơ chế hoặc phát hiện cốt lõi của chương, khép lại trọn vẹn vòng lặp nhận thức đã mở ra ở đầu chương đó.
  2. **Khối Cầu nối & Mở ra chương mới (Narrative Bridge / Forward Propulsion):** Đặt ra mâu thuẫn mới, câu hỏi hở hoặc chuyển dịch thế cờ, sử dụng động lực nhân quả "THEREFORE" hoặc "BUT" để đẩy khán giả sang tọa độ chiến trường của chương tiếp theo, tuyệt đối không để rơi năng lượng hay thỏa mãn tĩnh lặng.

## Deliverable discipline
When editing a file, return the full file.
When completing a phase, state what changed.
When uncertain, reduce claims and add disclaimers.

## Review discipline
Before marking a task done, verify:
1. continuity preserved
2. no regulatory violations, biased socio-political critiques, or moralizing tones
3. tone matches channel bible (intellectual, empathetic, objective, constructive)
4. script is easy to voice (sentences < 150 characters, ngắt câu cơ học bằng dấu chấm hoặc chấm phẩy theo Term-Breath Protocol, no `—` marks)
5. output file names are correct
6. compliance note is present (`Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng`)
7. all script files (`chapter_XX.md`) are strictly cleaned for production: absolutely NO metadata headers, NO footers, and NO titles (`# Chương X: ...`) remaining (only raw, clean voiceover paragraphs for the ear).

## Intent Router
Khi người dùng yêu cầu xử lý bằng ngôn ngữ tự nhiên, hãy ánh xạ chính xác sang hành động tương ứng:
- "viết kịch bản", "tạo video", "làm episode mới", "sản xuất nội dung" -> Chạy `/generate_episode`
- "khởi tạo", "init episode", "bắt đầu episode mới" -> Chạy `/init_episode`
- "research", "deep research", "nghiên cứu", "nghiên cứu sâu", "tìm data" -> Chạy `/deep_research`
- "viết brief", "lập chiến lược", "chiến lược" -> Chạy `/build_brief`
- "viết hook", "mở đầu video", "hook lab" -> Chạy `/hook_lab`
- "viết outline", "dàn ý", "xây cấu trúc" -> Chạy `/build_outline`
- "viết chương", "viết chapter", "viết tiếp" -> Chạy `/write_chapter`
- "kiểm tra", "QA", "review kịch bản" -> Chạy `/qa_review`
- "edit bằng google AI", "kiểm chứng bằng Google AI", "fact-check bằng Google", "audit bằng Google Search AI" -> Chạy `/google_ai_audit` (hoặc chạy trực tiếp script `scripts/google_ai_audit.py`)
- "visual", "tạo hình", "prompt ảnh" -> Chạy `/generate_visual_prompts`
- "thu âm", "TTS", "record" -> Chạy `/record_voiceover`
- "sửa chương", "revise" -> Chạy `/revise_chapter`
- "đánh giá kênh", "bắt bệnh video", "kiểm tra chỉ số", "retention" -> Chạy `channel_manager` SKILL

## Video Scene Splitting Quality Constraints (Veo 3.1 8s & I2V Reference Asset Protocol)
- **Safety Margin for Video Prompts:** Mọi phân cảnh trong video prompts bắt buộc phải giới hạn thời lượng thoại tối đa là **7.0 giây** (đối với clip Veo 3.1 dài cố định 8.0 giây) để luôn dư ít nhất 1.0 giây hình cho hậu kỳ và dự phòng sai số tốc độ đọc thực tế.
- **Scientific Word Count & WPS Calculation:** Thời lượng của các phân cảnh phải được ước lượng chính xác dựa trên số từ và độ dài audio thực tế của chương:
  - `WPS (Words Per Second) = Tổng số từ / Thời lượng audio thực tế` (nếu không có audio, dùng WPS mặc định = 3.81 từ/giây).
  - Giới hạn cứng: Mỗi phân cảnh hoặc phân cảnh phụ tuyệt đối không chứa quá **26 từ thoại** tiếng Việt.
  - `Thời lượng câu = Số từ của câu / WPS`.
- **Gom và Tách Phân Cảnh:**
  - *Chương 1 (Hook):* Không được gộp câu thoại. Mỗi câu thoại là 1 phân cảnh. Nếu câu thoại `> 7.0` giây hoặc `> 26` từ, bắt buộc phải tách đôi câu đó thành 2 sub-scenes con (`SCXXXa`, `SCXXXb`), mỗi cảnh con có prompt riêng.
  - *Từ Chương 2 trở đi đến Chương kết:* Gom các câu thoại liên tiếp sao cho tổng số từ `<= 26` từ (thời lượng `<= 7.0` giây) và tối đa là 3 câu/scene. Nếu câu tiếp theo làm tổng số từ vượt quá 26 từ, hoặc một câu đơn lẻ `> 26` từ ➡️ Tách cảnh và tạo sub-scenes con (`SCXXXa1`, `SCXXXa2`...).
- **Tag & Prompt Format:** Tệp prompts xuất ra theo từng chương (`prompts_chapter_XX.txt`) hoặc tổng hợp (`prompts_master.txt`). Tuân thủ định dạng cặp đôi `[IMAGE]` và `[VIDEO]` tương thích 100% với công cụ `tools/flow_batch_studio/` và giao thức ảnh tham chiếu (`@filename.ext ->`). Nội dung prompt mô tả tiếng Anh 100% không chứa ký tự tiếng Việt có dấu.