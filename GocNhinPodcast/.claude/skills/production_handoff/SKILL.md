---
name: production_handoff
description: Prepare the production handoff for an episode.
argument-hint: <episode-slug>
---

Prepare the production handoff for an episode.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/editorial_qa.md`
   - `episodes/[slug]/oral_qa.md`
   - `episodes/[slug]/visual_map.csv`
   - `episodes/[slug]/production_notes.md`
3. Confirm whether slideshow render has already been completed. If yes, include the rendered output path in handoff notes. If not, note the expected image folder and render target.
4. Create or update `episodes/[slug]/production_notes.md`.
5. Fill in:
   - voice direction
   - pacing profile
   - pronunciation watchlist
   - thumbnail direction
   - packaging hooks
   - asset requests
   - slideshow render inputs/outputs/status
   - legal caution notes
6. Update `01_management/episode_registry.csv` for the completed phase, including operator visibility fields: active specialist, canonical skill, current input files, current output file, and gate status.
7. Append the phase event to `episodes/[slug]/00_pipeline_operator_log.md`.
8. Return the full updated `production_notes.md`.
