---
name: build_retention_map
description: Build the retention map for an episode.
argument-hint: <episode-slug>
---

Build the retention map for an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/script-architect.md`.
- Also load `.claude/agents/hook-engine.md` because this phase inherits hook pressure, anti-completion discipline, and re-hook logic.
- Align with the `.agents` baseline that treats retention as content movement and unresolved tension, not teaser scaffolding.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/01_brief.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/03_thesis_map.md`
3. Create or update `episodes/[slug]/04_retention_map.md` only.
4. Design:
   - opening shock
   - recognition moment (Personal Stakes by Ch.2)
   - analytical peaks
   - re-hooks
   - fatigue risk zones
   - payoff turn
5. **Required retention anchors (mandatory):**
   - **Anti-Completion:** Hook must NOT self-close. Must end with an open question tied to viewer's personal finances.
   - **Re-hook #1 (~3:30):** MUST promise PERSONAL value ("your mortgage", "your assets"). Not generic "interesting insight."
   - **Re-hook #2 (~7:00):** NEW data shock not seen in earlier chapters.
   - **Re-hook #3 (~11:00, if video > 15 min):** Promise of Action Framework.
   - **3-minute rule:** Flag any planned segment > 3 minutes of pure framework/theory without personal-stakes anchor.
6. Keep retention design rooted in content movement, not teaser language; the specialist agent owns the opening/retention taste.
7. Update `01_management/episode_registry.csv` for the completed phase.
8. Do not build outline or write prose chapters yet.
9. Return the full updated `04_retention_map.md`.