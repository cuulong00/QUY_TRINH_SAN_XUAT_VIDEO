---
name: generate_visual_prompts
description: Translate approved visual scenes into final image prompts.
argument-hint: <episode-slug>
---

Translate approved visual scenes into final image prompts.

Arguments: `$ARGUMENTS`

Expected pattern: `[slug]`

Expert persona:
- Before doing this step, internalize `.agents/personas/the_visual_storyteller.md`.
- Align execution with `.agents/skills/visual_prompter/SKILL.md`.
- Work like a static-image director and concept artist, not like a mechanical paraphraser.
- Each prompt must carry one full scene with composition, metaphor, and visual hierarchy strong enough to earn its place in the episode.

Workflow:
1. Parse episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/scene_timing_map.json`
   - `episodes/[slug]/visual_map.csv`
   - `episodes/[slug]/production_notes.md`
3. Reject requests that try to bypass `scene_timing_map.json`.
4. Generate one prompt block per scene in `scene_timing_map.json`, not one prompt per spoken sentence.
5. The prompt for each scene must honor the grouped `visual_summary` and should be strong enough to generate one image that covers the entire grouped scene.
6. Use camera-angle rotation and composition variety to keep continuity while avoiding repetitive visuals.
7. Keep output aligned with the repo’s visual planning logic and the current episode’s narrative order.
8. Report input scene count vs output prompt count for user verification.
9. After the final image folder exists and is ordered correctly, route the next operational step to `/render_slideshow`.
10. Do not treat visual prompts as a replacement for `visual_map.csv` or `scene_timing_map.json`; this is a downstream production step after visual planning and scene grouping.
