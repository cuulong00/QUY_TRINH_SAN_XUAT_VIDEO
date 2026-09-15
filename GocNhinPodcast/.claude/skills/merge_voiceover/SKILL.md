---
name: merge_voiceover
description: Merge all chapters into a final voiceover script.
argument-hint: <episode-slug>
---

Merge all chapters into a final voiceover script.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read the merge working set:
   - all `chapter_*.md` files in `episodes/[slug]/`
   - `episodes/[slug]/03_thesis_map.md`
   - `episodes/[slug]/04_retention_map.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/05_continuity_packet.md`
   - `episodes/[slug]/06_claim_ledger.md`
   - `.claude/rules/final-merge.md`
3. Only backtrack to earlier planning files if the merge detects a thesis or evidence conflict that the working set cannot resolve.
4. Create or update `episodes/[slug]/final_voiceover.md` only.
5. Remove repetition and preserve the logic arc.
6. Preserve thesis fidelity: the merged script must not regress to a more familiar but shallower argument spine.
7. Preserve the strongest interpretive turns from chapter drafts rather than flattening them into clean but generic prose.
8. Apply anti-repetition judgment at the insight level, not just the sentence level.
9. Keep the text voiceover-friendly, sharp, and human-sounding.
10. Scan merged prose against `00_core/anti_ai_isms.md` and remove obvious formulaic scaffolding.
11. Ensure disclaimer is present and metadata in `final_voiceover.md` stays accurate.
12. Update `01_management/episode_registry.csv` for the completed phase.
13. Stop for user approval after returning the full updated `final_voiceover.md`.
14. Do not use merge as a shortcut before chapter workflow is complete.
