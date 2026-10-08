---
name: build_thesis
description: Build the thesis map for an episode.
argument-hint: <episode-slug>
---

Build the thesis map for an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/script-architect.md`.
- Align judgment with the `.agents` Script Architect baseline: Macro Strategist + Narrative Director, with research-first discipline.
- This phase exists to lock central thesis pressure, anti-thesis, and proof path before outline work begins.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/01_brief.md`
   - `episodes/[slug]/02_research_map.md`
   - `episodes/[slug]/02_hook_pack.md`
3. Create or update `episodes/[slug]/03_thesis_map.md` only.
4. Lock:
   - title claim
   - hook claim
   - central thesis
   - anti-thesis
   - sub-claims
   - proof path
   - loop payoff map
5. For policy-heavy or international topics, make explicit:
   - what is official position
   - what is market reading
   - what is implementation reality
   - how the issue transmits into Vietnam
6. This skill defines the thesis-mapping workflow; the specialist agent owns the interpretation quality and strategic judgment.
7. Update `01_management/episode_registry.csv` for the completed phase.
6. Do not build outline or write prose chapters yet.
7. Return the full updated `03_thesis_map.md`.