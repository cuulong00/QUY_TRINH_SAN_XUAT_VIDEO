---
description: "Quy tắc bắt buộc cho sản xuất kịch bản. Luôn đọc trước mọi tác vụ liên quan đến episode, research, hook, chapter, QA, packaging."
---

# Quy trình sản xuất kịch bản — Flow Enforcement

## Mission
Repository này là hệ điều hành sản xuất kịch bản cho kênh YouTube về Tâm lý học Hành vi.
- Không viết kịch bản dạng one-shot từ chủ đề thô.
- Không dùng chat memory làm nguồn sự thật (source of truth).
- Mọi đầu ra phải được tối ưu hóa sâu sắc cho giọng đọc và bộ thu âm TTS.
- Với Claude Code, `.claude/*` là runtime authority; `.agents/*` chứa workflows legacy để tham khảo/migrate.

> 🛑 **COLD BOOT PROTOCOL (ÉP BUỘC THỰC THI — VÁ LỖ HỔNG LƯỜI BIẾNG CỦA AI)**
> TRƯỚC KHI sinh ra bất kỳ dòng nội dung nào (Hook, Outline, Chapter...):
> Agent BẮT BUỘC phải thực hiện một lượt phản hồi CHỈ ĐỂ BÁO CÁO quá trình nạp dữ liệu, theo format sau:
> 
> ```
> ⚙️ COLD BOOT: [Tên Phase]
> [x] Đã dùng view_file đọc SKILL: [Tên file]
> [x] Đã dùng view_file đọc PERSONA 1: [Tên file]
> [x] Đã dùng view_file đọc PERSONA 2: [Tên file]
> [x] Đã dùng view_file đọc DATA/VAULT liên quan.
> Báo cáo: Đã nạp đủ kiến thức. Sẵn sàng sinh nội dung ở lượt chat tiếp theo.
> ```
> NGHIÊM CẤM Agent gộp bước nạp dữ liệu và bước viết kịch bản vào cùng 1 lượt chat. Phải đợi User xác nhận "OK" hoặc lệnh tiếp tục mới được viết.

> 📢 **ACTIVATION BANNER — BẮT BUỘC HIỂN THỊ:**
> Mỗi khi kích hoạt chuyên gia cho bất kỳ pha nào, PHẢI hiển thị banner sau cho user TRƯỚC KHI bắt đầu công việc:
>
> ```
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 🎭 CHUYÊN GIA: [Tên chuyên gia]
> 📋 PHA: [Số pha] — [Tên pha]
> 🎬 EPISODE: [Tên episode]
> 📂 SKILL: [Tên SKILL file đang dùng]
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ```

## NotebookLM — 1 Video = 1 Master Notebook (Tuyệt đối không vi phạm)
- TUYỆT ĐỐI KHÔNG tạo notebook mới cho mỗi lần research.
- Mỗi episode có file `episodes/[slug]/.notebook_url` chứa URL notebook duy nhất.
- **Trước khi gọi `deep_research`, `ask_question`, `add_source`, `batch_to_vault`:** ĐỌC file `.notebook_url` và truyền tham số `notebook_url`. KHÔNG BAO GIỜ bỏ trống.
- **Khi tạo notebook mới cho episode:** GHI ngay URL vào `episodes/[slug]/.notebook_url`.

## Intent detection bắt buộc
Khi user yêu cầu một tác vụ sản xuất bằng ngôn ngữ tự nhiên, phải map sang command tương ứng:

| Intent | Command bắt buộc |
|---|---|
| Khởi tạo hoặc xác thực chủ đề mới | `/init_episode` |
| Nghiên cứu sâu bằng NotebookLM | `/deep_research` |
| Lập chiến lược brief | `/build_brief` |
| Thiết kế Hook / opening | `/hook_lab` |
| Thesis / Outline / Chapter Briefs | `/build_outline` |
| Viết 1 chapter | `/write_chapter` |
| Sửa 1 chapter | `/revise_chapter` |
| Kiểm tra QA (Scientific + Oral QA) | `/qa_review` |
| Tạo bản đồ hình ảnh & visual prompts | `/generate_visual_prompts` |
| Thu âm / TTS | `/record_voiceover` |

Nếu episode đã tồn tại, phải đọc state files và tiếp tục từ pha hiện tại. Không nhảy pha.

## Bảng Chuyên Gia Bắt Buộc Theo Pha — HARD GATE
Mỗi pha phải dùng ĐÚNG chuyên gia được chỉ định. Agent PHẢI dùng tool `view_file` đọc persona file VÀ SKILL file tương ứng trước khi tạo output.

| Pha | Chuyên gia bắt buộc | Persona file (Đường dẫn tuyệt đối) | SKILL file (Đường dẫn tuyệt đối) |
|---|---|---|---|
| 1 — Xác Thực Chủ Đề | **The Content Strategist** | `.agents/personas/the_topic_strategist.md` | `.agents/skills/topic_ideator/SKILL.md` |
| 2 — Deep Research | **Deep Researcher** | `.agents/personas/the_research_scientist.md` | `.agents/skills/deep_researcher/SKILL.md` |
| 3 — Bản Chiến Lược | **Script Architect** | `.agents/personas/the_behavioral_psychologist.md` + `.agents/personas/the_narrative_director.md` | `.agents/skills/script_architect/SKILL.md` |
| 4 — Hook Lab | **Script Architect + Hook Engine** | `.agents/personas/the_behavioral_psychologist.md` | `.agents/skills/hook_engine/SKILL.md` |
| 5-8 — Outline & Briefs | **Script Architect** | `.agents/personas/the_behavioral_psychologist.md` + `.agents/personas/the_narrative_director.md` | `.agents/skills/script_architect/SKILL.md` |
| 9 — Viết Chương | **Chapter Writer** | `.agents/personas/the_behavioral_psychologist.md` + `.agents/personas/the_narrative_director.md` | `.agents/skills/chapter_writer/SKILL.md` |
| 9.5 — Scan Kịch Bản | **Quality Czar** | `.agents/personas/the_quality_czar.md` | `.agents/skills/quality_czar/SKILL.md` (nếu có) |
| 10 — Kiểm Tra Khoa Học | **Scientific QA** | `.agents/personas/the_research_scientist.md` | `.agents/skills/scientific_qa/SKILL.md` |
| 11 — Kiểm Tra Lời Nói | **Oral Polisher** | `.agents/personas/the_voice_architect.md` | `.agents/skills/oral_polisher/SKILL.md` |
| 12 — Bản Đồ Hình Ảnh | **Visual Prompter + Scene Architect** | `.agents/personas/the_scene_architect.md` + `.agents/personas/the_visual_storyteller.md` | `.agents/skills/scene_timing_builder/SKILL.md` + `.agents/skills/generate_visual_prompts/SKILL.md` |
| 16 — Postmortem | **Quality Czar** | `.agents/personas/the_quality_czar.md` | `02_templates/postmortem_template.md` |
| 17 — Quản trị Kênh | **The Channel Manager** | `.agents/personas/the_topic_strategist.md` | `.agents/skills/channel_manager/SKILL.md` (nếu có) |

## Pipeline sản xuất 17 pha bắt buộc
Mọi kịch bản phải đi qua tuần tự 17 pha sau. Không được nhảy chặng.

| Pha | Output file | Command/Skill |
|---|---|---|
| 1. Topic Qualification | `01_topic_qualification.md` | `/init_episode` |
| 2. Data Mining & Verification | `02_research_map.md` | `/deep_research` |
| 3. Strategy Brief | `03_brief.md` | `/build_brief` |
| 4. Hook Lab | `04_hook_pack.md` | `/hook_lab` |
| 5. Thesis Map | `05_thesis_map.md` | `/build_outline` |
| 6. Retention Map | `06_retention_map.md` | `/build_outline` |
| 7. Outline | `07_outline.md` | `/build_outline` |
| 8. Chapter Briefs | `08_chapter_briefs.md` | `/build_outline` |
| 9. Chapter Writing | `chapter_XX.md` | `/write_chapter` (từng chương) |
| 10. Scientific QA | `scientific_qa.md` | `/qa_review` |
| 11. Oral QA | `oral_qa.md` | `/qa_review` |
| 12. Visual Map | `visual_map.csv` | `/generate_visual_prompts` |
| 13. Audio Landscape | Audio direction | `music_composer` SKILL |
| 14. Video Render (CapCut - Manual) | Video output | `video_renderer` SKILL |
| 15. Production Handoff | `production_notes.md` | `/production_handoff` |
| 16. Postmortem | `postmortem.md` | `02_templates/postmortem_template.md` |
| 17. Performance Review | Cập nhật benchmarks | Manual |

## Checkpoint Rules & Human Approval Gates
Phải dừng lại xin duyệt của User ở các chặng sau:
- Sau pha 1: Topic Qualification
- Sau pha 2: Data Mining (Research Map)
- Sau pha 3-4: Strategy Brief + Hook Lab
- Sau pha 5-8: Thesis Map + Outline + Chapter Briefs
- Sau pha 10-11: Scientific QA + Oral QA
- Sau pha 16: Postmortem

## Hard Blocks
Tuyệt đối cấm:
1. Viết kịch bản chapter khi chưa có `03_brief.md` và `07_outline.md`.
2. Bỏ qua bước Deep Research mà đi thẳng vào Brief.
3. Chẩn đoán người xem hoặc hứa thay thế trị liệu trong văn kịch bản.
4. Bịa nghiên cứu, thí nghiệm, hoặc số liệu khoa học.
5. Sử dụng file gộp `final_voiceover.md` (Bước Merge đã bị loại bỏ hoàn toàn khỏi quy trình). Oral Polish phải được thực hiện trực tiếp trên từng `chapter_XX.md`.
6. Chuyển sang khâu thu âm TTS khi chưa thực hiện AI Script Self-Audit (kiểm duyệt thủ công không dùng API) quét lỗi lặp từ và bẫy tự hồi quy (dấu ngoặc kép, ký tự đặc biệt) trên từng chapter.
7. TUYỆT ĐỐI CẤM sử dụng code, thuật toán tự động hoặc script ghép nối từ khóa để sinh prompt tự động. Việc chuyển thể từ kịch bản sang prompt video bắt buộc phải được thực hiện bằng suy luận nghệ thuật của mô hình AI (LLM) để đảm bảo chất lượng hình ảnh chuyển dịch hoàn hảo nhất.


## State-First Principle
Trước mọi hành động liên quan đến kịch bản:
1. Xác định thư mục `episodes/[slug]/`
2. Đọc các file state hiện có
3. Xác định pha hiện tại
4. Chỉ tiếp tục làm đúng pha tiếp theo.
