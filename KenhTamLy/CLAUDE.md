# CLAUDE.md

## Runtime authority
- File này tồn tại để đáp ứng runtime authority và prewrite guard của repo.
- Với Claude Code, source of truth cho workflow nằm ở:
  1. `CLAUDE.md`
  2. `.claude/settings.json`
  3. `.claude/rules/*.md`
  4. `.claude/commands/*.md`
  5. `.claude/agents/*.md`

## Current migration context
- Workspace này đã được refactor hoàn chỉnh từ hệ sản xuất nội dung Phật giáo sang hệ sản xuất nội dung về **Tâm lý học Hành vi & Khoa học Hành vi**.
- Quy trình đã được đồng bộ với hệ tiêu chuẩn 17 pha của X-Economic, hỗ trợ nghiên cứu tự động chuyên sâu qua NotebookLM và kiểm soát giọng đọc TTS chặt chẽ.

## Working principles
- Không dùng chat memory làm source of truth cho episode work.
- Trước mỗi bước lớn, đọc rules/commands/agents liên quan.
- Không viết one-shot full script từ chủ đề thô.
- **1 Video = 1 Master Notebook:** Luôn đọc `.notebook_url` trước khi chạy deep research hoặc ask question.
- **Không dùng file gộp voiceover:** Oral polish và TTS được thực thi trực tiếp trên từng `chapter_XX.md`.
- Mọi đầu ra phải tối ưu cho giọng đọc và bộ thu âm TTS (câu < 150 ký tự, đầy đủ dấu chấm ngắt nghỉ).

## Registered Commands
- `/init_episode` — Khởi tạo thư mục và xác thực chủ đề (Pha 1).
- `/deep_research` — Chạy nghiên cứu sâu qua NotebookLM, Batch Extract và lập Research Map (Pha 2).
- `/build_brief` — Lập Strategy Brief (Pha 3).
- `/hook_lab` — Thiết kế Angle và Hook Pack (Pha 4).
- `/build_outline` — Lập Thesis Map, Retention Map, Outline và Chapter Briefs (Pha 5–8).
- `/write_chapter` — Viết prose chi tiết cho một chương (Pha 9).
- `/revise_chapter` — Sửa đổi chi tiết một chương dựa trên phản hồi.
- `/qa_review` — Kiểm định chuyên sâu kịch bản: Scientific QA (Pha 10) & Oral QA (Pha 11).
- `/generate_visual_prompts` — Lập bản đồ hình ảnh & visual prompts (Pha 12).
- Video Render (CapCut - Manual) — Dựng hậu kỳ thủ công từ các video clip và voiceover (Pha 14).
- `/record_voiceover` — Chạy TTS thu âm từ các file chapter đã duyệt.
