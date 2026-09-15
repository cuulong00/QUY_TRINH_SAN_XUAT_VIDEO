---
name: write_chapter
description: Write one chapter for an episode.
argument-hint: <episode-slug> chapter_01
---

Write one chapter for an episode.

Arguments: `$ARGUMENTS`

Expected pattern: `[slug] chapter_01`

Required specialist context:
- Before producing output, load `.claude/agents/chapter-writer.md`.
- Align the pass with the `.agents` chapter-writer baseline: the writer embodies the Narrative Director, while core argument, data, and counter-argument are already locked upstream by the Script Architect in `chapter_briefs.md`.
- This phase owns prose force, paragraph movement, and spoken authority inside one chapter. It does not reopen thesis design.

Workflow:
1. Parse episode slug and target chapter from `$ARGUMENTS`. If missing, ask the user.
2. Read the minimum working set first:
   - `00_core/voice_dna.md`
   - `00_core/anti_ai_isms.md`
   - `episodes/[slug]/03_brief.md`
   - `episodes/[slug]/07_outline.md`
   - `episodes/[slug]/09_narrative_state_tracker.md`
   - `episodes/[slug]/10_claim_ledger.md`
   - `episodes/[slug]/08_chapter_briefs.md` if it exists
3. Read additional inputs only when the current chapter truly needs them:
   - `episodes/[slug]/02_research_map.md` and `02_research_synthesis.md` for evidence, case study, or data support
   - `episodes/[slug]/05_thesis_map.md` for thesis spine or anti-thesis calibration
   - `episodes/[slug]/06_retention_map.md` for mid-video pacing or re-hook placement
   - `episodes/[slug]/04_hook_pack.md` for chapter_01 or explicit re-hook carryover
   - 3 câu cuối của `chapter_*.md` liền trước để gặt seed
4. Do not default to reading all prior chapters if `09_narrative_state_tracker.md` already captures used insights, used cases, banned repeats, and open loops.
5. Data Validation:
   - ensure all numbers have reasonable sources and are verified in 02_research_map.md
   - ensure at least 1 case study or concrete data point per chapter
   - ensure no buy/sell advice or profit promises
6. Write only the requested chapter file.
7. The chapter must materially deepen the viewer's reading beyond summary. Required qualities should appear inside real prose, not as visible checklist beats.
8. **Chapter-specific validation (hard constraints):**
   - **If writing chapter_01:** Hook MUST end with an OPEN question about the viewer's personal finances/stakes. MUST NOT self-close (Anti-Completion Rule).
   - **If writing chapter_02:** MUST pass the Chapter 2 Gate. MUST use a universal lens ("Chúng ta", "Xã hội hiện đại", "Tầng lớp lao động"). MUST NOT contain international case studies.
   - **If writing chapters 3-4:** MUST include at least 1 re-hook and 1 new data shock.
9. Do not write paragraphs that exist only to satisfy brief fields, bridge obligations, or workflow artifacts.
10. Do not let planning files leak into visible prose form. Avoid reusable bridge formulas, announce-importance transitions, or repeated chapter cadence that feels compiled from the same template.
11. Scan the draft against `00_core/anti_ai_isms.md` before finalizing.
12. The specialist agent owns the voice, judgment, paragraph flow, and expert method; this skill only enforces the phase workflow, required inputs, and output/state contract.
13. Update:
   - `episodes/[slug]/09_narrative_state_tracker.md`
   - `episodes/[slug]/10_compliance_report.md`
   - `01_management/episode_registry.csv`
14. Return the full chapter file plus updated state files.
15. Do not bypass chapter-by-chapter workflow by drafting final merge prose in chat.
