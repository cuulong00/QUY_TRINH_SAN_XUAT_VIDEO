---
name: generate_shorts
description: Build short-form packages for YouTube Shorts from an episode or as standalone shorts.
argument-hint: <episode-slug or standalone-short-slug>
---

Build short-form packages for YouTube Shorts.

Arguments: `$ARGUMENTS`

Required specialist context:
- Shorts in this repo must follow the `.agents` baseline specialist chain.
- Use the correct specialist at the correct phase:
  - Strategy / insight lock → `.agents/personas/the_shorts_strategist.md`
  - Hook creation → `.agents/personas/the_short_hook_specialist.md`
  - Body writing → `.agents/personas/the_short_script_writer.md`
  - Visual prompts → `.agents/personas/the_vertical_video_maestro.md`
- Align execution with `.agents/workflows/generate_shorts.md` and `.agents/skills/shorts_producer/SKILL.md`.

Canonical sources to read first:
- `00_core/shorts_style_guide.md`
- `00_core/shorts_map_template.md`
- `00_core/voice_dna.md`
- `CLAUDE.md`

Workflow:
1. Determine whether the request is:
   - a derived short from `episodes/[slug]/`
   - or a standalone short under `shorts/standalone/[slug]/`
2. Lock one of the six canonical short types:
   - `data_shock`
   - `paradox`
   - `comparison`
   - `golden_quote`
   - `hook_teaser`
   - `mini_essay`
3. Lock one insight only. A short is not a compressed long-form chapter.
4. For shorts ≥ 30 seconds, build or verify the 4-beat structure:
   - Hook
   - Context
   - Insight
   - Twist / CTA
5. Use the specialist phases in order:
   - Shorts Strategist locks source type, short type, one insight, and 4-beat brief
   - Short Hook Specialist generates 3-5 hook variants
   - Stop for hook approval when the task requires iterative approval
   - Short Script Writer writes the body after the hook is chosen
   - Stop for script approval when the task requires iterative approval
   - Vertical Video Maestro builds short-form visual prompts when needed
6. Derived shorts should pull traffic to the relevant long-form video or episode asset.
7. Standalone shorts should pull to channel or playlist, not fake urgency.
8. If the short touches assets or investment, include the short disclaimer: `Nội dung giáo dục, không phải lời khuyên đầu tư.`
9. Do not force short-form requests through long-form chapter workflow.
10. Return only the files requested by the user’s scope.
