# Specialist Map — .claude Sync Layer

Mục tiêu của file này là làm cầu nối rõ ràng giữa execution contracts trong `.claude/*` và baseline specialist workflow trong `.agents/*`.

## Nguyên tắc
- `CLAUDE.md` và `.claude/*` giữ vai trò execution contract và workflow order.
- `.agents/*` là baseline cho specialist DNA, persona loading, và craft method.
- Mỗi pha trong `.claude/skills/*` phải nói rõ specialist nào đang dẫn và cần nạp context nào trước khi tạo output.

## Phase → Specialist map

| Pha | Canonical skill | Specialist dẫn | Context phải nạp |
|---|---|---|---|
| Topic Qualification | `qualify_topic` | `content-strategist` | `.claude/agents/content-strategist.md` + `.agents/personas/the_content_strategist.md` |
| Brief | `build_brief` | `script-architect` | `.claude/agents/script-architect.md` + Macro Strategist / Narrative Director baseline |
| Research Map | `build_research_map` | `script-architect` | `.claude/agents/script-architect.md` + research-first baseline từ `.agents/skills/script_architect/SKILL.md` |
| Hook Lab | `hook_lab` | `hook-engine` with `script-architect` support | `.claude/agents/hook-engine.md` + `.claude/agents/script-architect.md` |
| Thesis Map | `build_thesis` | `script-architect` | `.claude/agents/script-architect.md` |
| Retention Map | `build_retention_map` | `script-architect` + `hook-engine` support | `.claude/agents/script-architect.md` + `.claude/agents/hook-engine.md` |
| Outline | `build_outline` | `script-architect` | `.claude/agents/script-architect.md` |
| Chapter Briefs | `build_chapter_briefs` | `script-architect` | `.claude/agents/script-architect.md` |
| Chapter Writing | `write_chapter` | `chapter-writer` | `.claude/agents/chapter-writer.md` + Narrative Director baseline from `.agents/skills/chapter_writer/SKILL.md` |
| Final Merge | `merge_voiceover` | `chapter-writer` + `editorial-quality-director` judgment | `.claude/agents/chapter-writer.md` + `.claude/agents/editorial-quality-director.md` |
| Editorial & Legal QA | `editorial_qa` | `editorial-qa` | `.claude/agents/editorial-qa.md` + Data Auditor baseline |
| Oral QA | `oral_qa` | `oral-polisher` | `.claude/agents/oral-polisher.md` + Voice Architect baseline |
| Combined QA | `qa_review` | `editorial-quality-director` → `editorial-qa` → `oral-polisher` | `.claude/agents/editorial-quality-director.md`, `.claude/agents/editorial-qa.md`, `.claude/agents/oral-polisher.md` |
| Visual Map | `build_visual_map` | visual planning under Scene Architect logic | `.claude/skills/build_scene_timing_map/SKILL.md` scene baseline + episode visual planning files |
| Scene Timing Map | `build_scene_timing_map` | Scene Architect | `.agents/personas/the_scene_architect.md` |
| Visual Prompts | `generate_visual_prompts` | Visual Storyteller / Visual Prompter | `.agents/personas/the_visual_storyteller.md` + `.agents/skills/visual_prompter/SKILL.md` |
| Render Slideshow | `render_slideshow` | production execution | production notes + render contract |
| Production Handoff | `production_handoff` | production execution | production notes + QA + visual outputs |

## Shorts lane
Shorts là lane song song, không ép qua long-form chapter workflow.
Canonical skill: `generate_shorts`


| Lane | Specialist chain | Context phải nạp |
|---|---|---|
| Shorts strategy | Shorts Strategist | `.agents/personas/the_shorts_strategist.md` |
| Shorts hook | Short Hook Specialist | `.agents/personas/the_short_hook_specialist.md` |
| Shorts body | Short Script Writer | `.agents/personas/the_short_script_writer.md` |
| Shorts visual prompts | Vertical Video Maestro | `.agents/personas/the_vertical_video_maestro.md` |

Khi `.claude` có Shorts skill riêng, file đó phải bám đúng chuỗi specialist này.
