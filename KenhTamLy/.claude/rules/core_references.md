---
description: "Danh sách file lõi bắt buộc đọc trước các bước lớn trong flow sản xuất."
---

# Tài liệu tham chiếu bắt buộc

## Luật cơ bản
- Repo files là nguồn sự thật duy nhất.
- Trước mỗi bước lớn, đọc file liên quan thay vì đoán.
- Với Claude Code, authority runtime nằm ở `CLAUDE.md`, `.claude/settings.json`, `.claude/rules/*.md`, `.claude/commands/*.md`, `.claude/agents/*.md`.
- `.agents/` chỉ là nguồn migration / tham khảo để làm giàu runtime hiện tại, không phải bề mặt runtime chính cho Claude Code.

## Thứ bậc đọc tham chiếu
1. `CLAUDE.md`
2. `.claude/settings.json`
3. `.claude/rules/*.md`
4. `.claude/commands/*.md`
5. `.claude/agents/*.md`
6. `03_playbooks/*.md`
7. `00_core/*.md`
8. `episodes/[slug]/*`
9. `.agents/*` (legacy reference only khi cần đối chiếu/migrate)

## Rule files chính
- `.claude/rules/script_production_flow.md`
- `.claude/rules/core_references.md`
- `.claude/rules/quality_constraints.md`
- `.claude/rules/depth_and_humanness.md`
- `.claude/rules/episode_state.md`
- `.claude/rules/creative_dna.md`
- `.claude/rules/expert_panel.md`

## File DNA kênh
- `00_core/channel_bible.md`
- `00_core/audience_personas.md`
- `00_core/longform_blueprint.md`
- `00_core/voiceover_style_guide.md`
- `00_core/quality_rubric.md`
- `00_core/anti_patterns.md`
- `00_core/voice_dna_benchmark.md`

## File chuyên biệt
- `00_core/hook_library.md` — khi làm hook / retention
- `00_core/thumbnail_style_guide.md` — khi packaging thumbnail
- `00_core/youtube_seo_guide.md` — khi viết metadata
- `00_core/reference_stories.md` — khi viết chapter, tránh lặp
- `00_core/remix_differentiation_guide.md` — khi làm remix
- `intro_chanel.md` — khi khóa intro kênh trong hook pack
- `00_core/doctrine_boundaries.md` — file legacy cần đọc cẩn trọng trong giai đoạn migration; không dùng như authority doctrinal, chỉ đối chiếu để thay bằng boundary logic mới ở runtime hiện tại

## Agent surfaces chính
- `.claude/agents/topic-ideator.md` — khi phân tích chủ đề thô, chọn angle, định hidden pain sâu nhất trước brief
- `.claude/agents/script-architect.md` — khi khóa brief, thesis, outline
- `.claude/agents/hook-engine.md` — khi làm packaging, hook, re-hook
- `.claude/agents/chapter-writer.md` — khi viết hoặc sửa chapter
- `.claude/agents/oral-polisher.md` — khi merge / polish voiceover
- `.claude/agents/behavioral-safety-qa.md` — khi rà evidence integrity, mental health safety, ethical persuasion, và overclaim
- `.claude/agents/thumbnail-architect.md` — khi làm thumbnail brief
- `.claude/agents/metadata-architect.md` — khi làm YouTube metadata

## Playbooks hỗ trợ
- `03_playbooks/episode_workflow.md`
- `03_playbooks/quality_stability_system.md`
- `03_playbooks/claude_code_playbook.md`

## File quản lý
- `01_management/episode_registry.csv`
- `01_management/lessons_learned.md`
- `01_management/topic_backlog.md`
