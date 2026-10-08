---
name: render_slideshow
description: Render slideshow base video from a finalized image folder.
argument-hint: <episode-slug>
---

Render slideshow base video from a finalized image folder.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/production_notes.md`
   - `episodes/[slug]/visual_map.csv`
3. Confirm or determine the input image folder. Preferred default: `episodes/[slug]/images_final/`.
4. Confirm or determine the output video path. Preferred default: `episodes/[slug]/video/slideshow_base.mp4`.
5. Run the slideshow renderer using:
   - module: `scripts/slideshow_video`
   - CLI: `PYTHONPATH=scripts python -m slideshow_video ...`
6. Suggested defaults unless the user specifies otherwise:
   - duration per image: 8
   - transition duration: 1
   - fps: 30
   - seed: 42
7. Update `episodes/[slug]/production_notes.md` with:
   - `images_final_dir`
   - `slideshow_output_file`
   - `slideshow_duration_per_image`
   - `slideshow_transition_duration`
   - `slideshow_fps`
   - `slideshow_seed`
   - `slideshow_render_status`
8. Update `01_management/episode_registry.csv` for the completed phase, including operator visibility fields: active specialist, canonical skill, current input files, current output file, and gate status.
9. Append the phase event to `episodes/[slug]/00_pipeline_operator_log.md`.
10. Stop for user approval if the video base needs review before handoff.
11. Return the output MP4 path and the full updated `production_notes.md`.
