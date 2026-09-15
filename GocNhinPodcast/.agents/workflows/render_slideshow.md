---
description: Canonical wrapper for video slideshow rendering. Relies on the `.agents/skills/video_renderer/SKILL.md` to map image assets into an FFmpeg slideshow.
---

Canonical workflow for Video Rendering:
- `.agents/skills/video_renderer/SKILL.md` — Guide the manual post-production process in CapCut to build the base `.mp4` video.

Reminder:
- This step requires an existing `videos_final` folder filled with valid video clips (`.mp4` format generated from the video prompts) and the recorded voiceover.
- The operator manually imports all assets into CapCut, syncs them on the timeline, and exports to `video/slideshow_base.mp4` (preserving this filename for consistency).
- After the manually stitched video is exported to `video/slideshow_base.mp4`, it is handed over to the Production Handoff phase.
