Merge all chapters into a final voiceover script.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read before merging:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/episode_state.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/depth_and_humanness.md`
   - `.claude/rules/creative_dna.md`
   - `.claude/rules/expert_panel.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/03_thesis_map.md`
   - `episodes/[slug]/04_outline.md`
   - `episodes/[slug]/05_continuity_packet.md`
   - `episodes/[slug]/06_claim_ledger.md`
   - `episodes/[slug]/07_golden_lines.md`
   - all `chapter_*.md` files in `episodes/[slug]/`
   - `.claude/agents/oral-polisher.md`
3. Activate the oral-polisher expert stance explicitly: merge by ear, not by spreadsheet, while preserving one sharp, humane, lived-through voice across the whole final narration.
4. Create or update `episodes/[slug]/final_voiceover.md`.
5. Treat merge as preservation-first: keep opening architecture, chapter roles, open loops, second-half lifts, carry line, transition logic, ending payoff, and the identity of the Main Author voice.
6. Merge in chapter order and audit preservation before cutting anything.
7. Remove repetition surgically; do not compress in a way that breaks the runtime contract or thins out content-bearing mass.
8. Protect continuity at chapter seams:
   - opening of chapter N must feel grown from chapter N-1
   - duplicated seam lines must be removed surgically
   - transitions must carry meaning, not just signal movement
   - the final script must read as one living human voice, not stacked modules
9. Apply oral polish for spoken Vietnamese while preserving emotional turns, micro-situations, golden lines, bridge meaning, and the grounded authority of the Main Author.
10. TTS-clean the final file:
   - remove chapter template headings
   - remove spoken chapter labels
   - remove `<!-- TRANSITION -->` markers while keeping bridge prose
   - avoid formatting artifacts that would pollute TTS
11. Verify that the intro + CTA still sit naturally after the hook and that the ending pays off the packaging promise.
12. Verify that the Main Author voice still feels present in the final script rather than being flattened into neutral narration.
13. Measure preservation ratio against drafted chapter mass; if it falls below the floor without justification, treat merge as failed.
14. Return the full updated `final_voiceover.md`.
