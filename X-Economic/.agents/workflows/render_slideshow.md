---
description: Canonical wrapper for video clip stitching. Relies on the `.agents/skills/video_renderer/SKILL.md` to concatenate generated video clips into a single base video.
---

Canonical workflow for Video Rendering:
- `.agents/skills/video_renderer/SKILL.md` — Guide the post-production process in NLE (Premiere/DaVinci) or I2V+ tools to build the base `.mp4` video.

Reminder:
- This step requires an existing `videos` folder filled with valid video clips (`.mp4` format generated from the video prompts) and the recorded voiceover.
- The operator imports all assets, syncs them on the timeline, and exports to `video/slideshow_base.mp4` (preserving this filename for repository validator compatibility).
- After the stitched video is exported to `video/slideshow_base.mp4`, it is handed over to the Production Handoff phase.
