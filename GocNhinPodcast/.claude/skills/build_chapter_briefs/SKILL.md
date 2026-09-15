---
name: build_chapter_briefs
description: Build chapter briefs for an episode before writing chapters.
argument-hint: <episode-slug>
---

Build chapter briefs for an episode before writing chapters.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/script-architect.md`.
- Align the pass with the `.agents` Script Architect baseline: Macro Strategist + Narrative Director, with chapter briefs treated as locked argument/evidence handoff rather than prose choreography.
- This phase must lock chapter necessity, evidence pressure, and continuity without pre-writing the writer's sentence music.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/03_brief.md`
   - `episodes/[slug]/02_research_map.md`
   - `episodes/[slug]/02_research_synthesis.md`
   - `episodes/[slug]/04_hook_pack.md`
   - `episodes/[slug]/05_thesis_map.md`
   - `episodes/[slug]/06_retention_map.md`
   - `episodes/[slug]/07_outline.md`
   - `episodes/[slug]/09_narrative_state_tracker.md`
3. Create or update `episodes/[slug]/08_chapter_briefs.md` only.
4. For each chapter, define only the load-bearing constraints:
   - chapter purpose
   - misconception to correct or shallow reading to overturn
   - load-bearing evidence
   - expert lens
   - novelty delta versus prior chapters
   - downstream dependency for the next chapter
5. Make each chapter brief specific enough that two chapters cannot be swapped without weakening the episode.
6. **Ch.2 brief MUST explicitly state:** "This chapter MUST connect macro to the universal life of citizens/workers. MUST use a universal stakes lens ('Chúng ta', 'Xã hội hiện đại', 'Tầng lớp lao động'). MUST NOT jump to international case studies."
7. Chapter briefs must constrain argument, evidence, and continuity — not prose choreography.
8. Do not prescribe rhetorical devices, emotional management, sentence cadence, reusable bridge wording, or `human texture` as a fill-in field.
9. If a chapter can be drafted as a checklist directly from the brief, the brief is over-specified and must be simplified.
10. **PREREQUISITE:** Outline must have passed the Retention Gate (`00_core/retention_gate_checklist.md` ≥ 8/10) before chapter briefs can be created.
11. Update `01_management/episode_registry.csv` for the completed phase.
12. Do not write prose chapters yet.
13. Return the full updated `chapter_briefs.md`.