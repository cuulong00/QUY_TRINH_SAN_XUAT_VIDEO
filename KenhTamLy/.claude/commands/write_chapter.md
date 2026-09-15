Write one chapter for an episode.

Arguments: `$ARGUMENTS`

Expected pattern: `[slug] chapter_01`

Workflow:
1. Parse the episode slug and target chapter from `$ARGUMENTS`. If missing, ask the user.
2. Read before writing:
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
   - all existing `episodes/[slug]/chapter_*.md`
   - `.claude/agents/chapter-writer.md`
3. Activate the chapter-writer expert stance explicitly: write as one living human voice with behavioral clarity, humane authority, screenwriting movement, and oral realism.
4. Front-load Originality before drafting a single sentence:
   - read the target chapter's `chapter_signature`, `target_words`, `word_range`, `retention_move`, `loop_progress`, and `payoff_target` from `04_outline.md`
   - pause to absorb the chapter's linguistic fingerprint, emotional temperature, and cognitive pressure
   - enter the highest expert soul of the channel before choosing words
   - decide the chapter's rhythm and consciousness first; do not paraphrase the outline into prose
5. Write only the requested chapter file.
   - The chapter file must contain only clean voiceover prose.
   - Do not include template labels, slug metadata, chapter_number, chapter_title, emotional_function, or `bridge_to_next:` markers inside the chapter file.
   - Any structural tracking belongs in state files, not in spoken-script chapter files.
6. Update:
   - `episodes/[slug]/05_continuity_packet.md`
   - `episodes/[slug]/06_claim_ledger.md`
   - `episodes/[slug]/07_golden_lines.md`
7. Verify the chapter:
   - serves one dominant emotional function
   - advances one major argumentative movement
   - moves through scene -> mechanism -> reframe where depth is required
   - contains at least one concrete micro-situation
   - contains at least one emotional turn
   - avoids repeated examples/metaphors from prior chapters
   - respects the target word band or explains any meaningful deviation
   - ends with a bridge that carries meaning, not just flow
   - opens in a way that grows naturally out of the previous chapter
   - does not speak chapter labels aloud in voiceover prose
   - does not narrate structure, leak workflow metadata, or sound like outline-to-prose conversion
   - clearly embodies the target `chapter_signature` rather than a flat neutral voice
   - does not feel generic, industrial, or templated
8. Return the full chapter file plus all updated state files.
