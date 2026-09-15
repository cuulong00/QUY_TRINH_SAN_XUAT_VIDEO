---
name: build_brief
description: Build the episode brief after topic qualification is approved.
argument-hint: <episode-slug>
---

Build the episode brief after topic qualification is approved.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/script-architect.md`.
- Align the pass with the `.agents` Script Architect baseline: Macro Strategist + Narrative Director, with research-first discipline from `.agents/skills/script_architect/SKILL.md`.
- This phase locks audience, pain, promise, and strategic pressure. It is not generic briefing.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/00_topic_qualification.md`
3. Create or update `episodes/[slug]/01_brief.md` only.
4. Lock:
   - audience
   - pain
   - promise
   - practical outcome
   - forbidden zones
   - virality / retention hypotheses
5. Update `01_management/episode_registry.csv` for the completed phase.
6. Do not create hooks, thesis, or outline yet.
7. Stop for user approval after returning the full updated `01_brief.md`.
8. Do not bypass this phase by drafting later outputs in chat.