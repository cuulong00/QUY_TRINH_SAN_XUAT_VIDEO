---
name: build_scene_timing_map
description: Build the minimal scene timing JSON for an episode.
argument-hint: <episode-slug>
---

Build the minimal scene timing JSON for an episode.

Arguments: `$ARGUMENTS`

Expert persona:
- Before doing this step, internalize `.agents/personas/the_scene_architect.md`.
- Work like a scene editor with taste, not like a mechanical sentence counter.
- Group by visual beat and mental picture, not by laziness or superficial keyword overlap.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/visual_map.csv`
3. Create or update `episodes/[slug]/scene_timing_map.json`.
4. Group spoken sentences into visual scenes using the minimum useful schema only.
5. The output schema is:
   - `id`
   - `sentence_count`
   - `duration_sec`
   - `visual_summary`
6. Use these grouping rules:
   - hook/opening can stay at 1 sentence per scene when sharp visual turnover helps retention
   - later sections may group adjacent sentences when they build one coherent mental picture
   - do not group sentences together if doing so would erase a reveal, contradiction, or interpretive turn
7. `duration_sec` should normally equal `sentence_count * 5`, unless there is a clear reason to override for the scene.
8. `visual_summary` must be rich, concrete, and image-directable. It should not compress the scene into vague abstraction.
9. Each `visual_summary` must give the next phase enough material to build one strong image that carries the full grouped scene. In practice it should capture, in natural Vietnamese:
   - the visible subject or setting
   - the economic meaning or tension of the moment
   - the emotional or interpretive direction the image should carry
   - any important constraint such as neutrality, non-political framing, or non-sensational treatment
10. Avoid summaries that are too short, too abstract, or too memo-like. If a downstream image agent cannot clearly imagine the frame, the summary is not good enough.
11. Keep the file minimal in schema, not minimal in thought. Do not add extra JSON fields unless a downstream phase uses them directly.
12. Update `01_management/episode_registry.csv` for the completed phase, including operator visibility fields: active specialist, canonical skill, current input files, current output file, and gate status.
13. Append the phase event to `episodes/[slug]/00_pipeline_operator_log.md`.
14. Return the updated `scene_timing_map.json`.
10. Update `01_management/episode_registry.csv` for the completed phase.
11. Return the updated `scene_timing_map.json`.
