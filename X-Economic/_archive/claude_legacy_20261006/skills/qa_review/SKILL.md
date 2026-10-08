---
name: qa_review
description: Run the legacy combined QA flow for an episode.
argument-hint: <episode-slug>
---

Run the combined QA flow for an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load the specialist sequence for this combined pass:
  - `.claude/agents/editorial-quality-director.md`
  - `.claude/agents/editorial-qa.md`
  - `.claude/agents/oral-polisher.md`
- Align the editorial/legal compliance and oral portions with the stricter `.agents` baselines for Data Auditor and Voice Architect discipline.
- This skill coordinates the sequence; it does not replace the specialist judgments inside each pass.

Canonical review order:
- editorial quality review
- editorial QA
- oral QA
- visual map build if the script is approved to move forward

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read only what the editorial director pass needs first:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/03_thesis_map.md`
   - `episodes/[slug]/04_retention_map.md`
   - `episodes/[slug]/02_hook_pack.md`
3. Run in order:
   - editorial quality review for thesis fidelity, repetition, generic drift, and payoff strength
   - editorial QA for safety/compliance
   - oral QA for spoken authority and cadence
4. Only backtrace into chapters or wider state if one of the three passes cannot resolve a flagged issue from the working set.
5. Update:
   - `episodes/[slug]/editorial_qa.md`
   - `episodes/[slug]/oral_qa.md`
   - `episodes/[slug]/final_voiceover.md` if needed
   - `01_management/episode_registry.csv`
6. Only move to `visual_map.csv` after the script is strong enough in caliber, not merely compliant.
7. If a finalized image folder already exists, the next canonical production step is `/render_slideshow` before handoff.
8. Return the updated files and a concise QA summary including caliber judgment.

Preferred modern usage: run the separate phase skills plus editorial-quality-director review rather than treating QA as compliance only.