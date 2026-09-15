Revise one chapter for an episode while preserving continuity.

Arguments: `$ARGUMENTS`

Expected pattern: `[slug] chapter_01 <revision feedback>`

Workflow:
1. Parse the episode slug, target chapter, and revision request from `$ARGUMENTS`. If anything important is missing, ask the user.
2. Read before revising:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/episode_state.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/depth_and_humanness.md`
   - `.claude/rules/expert_panel.md`
   - `00_core/*.md`
   - `episodes/[slug]/01_brief.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/03_thesis_map.md`
   - `episodes/[slug]/04_outline.md`
   - `episodes/[slug]/05_continuity_packet.md`
   - `episodes/[slug]/06_claim_ledger.md`
   - `episodes/[slug]/07_golden_lines.md`
   - all `chapter_*.md` files in the episode
   - `.claude/agents/chapter-writer.md`
3. Rewrite only the specified chapter while preserving the locked role of neighboring chapters.
4. Preserve golden lines unless the revision request explicitly requires changing them.
5. Update:
   - `episodes/[slug]/05_continuity_packet.md`
   - `episodes/[slug]/06_claim_ledger.md`
   - `episodes/[slug]/07_golden_lines.md`
6. Verify the revised chapter still:
   - serves the same chapter role unless the user asked to change it
   - speaks in one living voice continuous with adjacent chapters
   - deepens scene/mechanism/insight where needed instead of flattening
   - bridges naturally to adjacent chapters
   - avoids duplicated examples or metaphors
   - remains oral-friendly and free of spoken chapter labels
   - does not drift into generic or industrial prose
7. Return the revised chapter plus all updated state files.
