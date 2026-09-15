---
name: postmortem
description: Write the postmortem for an episode after review or publish.
argument-hint: <episode-slug>
---

Write the postmortem for an episode after review or publish.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read all final state files for the episode.
3. Create or update `episodes/[slug]/postmortem.md`.
4. Summarize what worked, what felt weak, the best hook/case/re-hook pattern, and what rules should be encoded into core files.
5. Update management files after the postmortem is complete:
   - `01_management/episode_registry.csv`
   - `01_management/lessons_learned.md` when a reusable pattern is discovered
6. Return the full updated `postmortem.md`.