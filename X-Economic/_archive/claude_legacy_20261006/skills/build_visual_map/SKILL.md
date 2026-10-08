---
name: build_visual_map
description: Build the visual map for an episode.
argument-hint: <episode-slug>
---

Build the visual map for an episode.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/04_retention_map.md`
   - `episodes/[slug]/production_notes.md`
3. Create or update `episodes/[slug]/visual_map.csv`.
4. Map each important script segment to a visual role, source need, chart or b-roll mode, and editor note.
5. Make sure the visual map is usable as the planning input for final image generation.
6. Note that `visual_map.csv` is not the final visual output. After a finalized image folder exists, the next operational step is slideshow render.
7. Update `01_management/episode_registry.csv` for the completed phase, including operator visibility fields: active specialist, canonical skill, current input files, current output file, and gate status.
8. Append the phase event to `episodes/[slug]/00_pipeline_operator_log.md`.
9. Return the updated `visual_map.csv`.
