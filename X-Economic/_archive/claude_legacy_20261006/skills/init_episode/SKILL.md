---
name: init_episode
description: Initialize or refresh an episode workspace.
argument-hint: <episode-slug>
---

Initialize or refresh an episode workspace.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the target episode slug from `$ARGUMENTS`. If missing, ask the user.
2. If `episodes/[slug]` does not exist, create it by copying `02_templates/episode_template/`.
3. Replace `__EPISODE_SLUG__` placeholders in the copied files.
4. Read all files in `00_core/`.
5. Create or refresh only the foundational setup files:
   - `episodes/[slug]/01_topic_qualification.md`
   - `episodes/[slug]/02_research_map.md`
   - `episodes/[slug]/03_brief.md`
   - `episodes/[slug]/04_hook_pack.md`
   - `episodes/[slug]/05_thesis_map.md`
   - `episodes/[slug]/06_retention_map.md`
   - `episodes/[slug]/07_outline.md`
   - `episodes/[slug]/08_chapter_briefs.md`
   - `episodes/[slug]/09_narrative_state_tracker.md`
   - `episodes/[slug]/10_claim_ledger.md`
   - `episodes/[slug]/10_compliance_report.md`
   - `episodes/[slug]/production_notes.md`
   - `episodes/[slug]/postmortem.md`
6. Update `01_management/episode_registry.csv`.
7. Do not create hooks, chapters, merge output, or QA content yet.
8. Return a concise scaffold summary and the full `00_topic_qualification.md`.