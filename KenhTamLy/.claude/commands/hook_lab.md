Create the hook pack for an episode.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read before writing:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/depth_and_humanness.md`
   - `.claude/rules/creative_dna.md`
   - `00_core/*.md`
   - `episodes/[slug]/01_brief.md`
   - `.claude/agents/hook-engine.md`
3. Activate the hook-engine expert stance explicitly: opening must feel human, lived-in, sharp, and packaging-aligned — never textbook-first or template-like.
4. When locking thumbnail angle candidates and title-thumbnail-hook alignment, explicitly consult `.claude/agents/thumbnail-architect.md` so thumbnail packaging is decided with the visual specialist in the loop.
5. Create or update `episodes/[slug]/02_hook_pack.md`.
6. Generate 7 angles, 10 hooks, top 3 hooks, 1 final hook, and 5 mini re-hooks.
7. Score hook candidates using: curiosity, pain_resonance, depth_signal, retention_pull, and channel_fit.
8. Ensure the hook set spans multiple opening families rather than defaulting to rhetorical-question variants.
9. For misconception-correction or myth-busting episodes, include direct-clarification and belief-flip candidates.
10. Lock these sections in `02_hook_pack.md`:
   - packaging thesis
   - core promise
   - title candidates
   - thumbnail angle candidates
   - title-thumbnail-hook alignment
   - selected final hook
   - official intro + CTA
   - macro open loops from opening
   - mini re-hooks
   - re-hook placement map
11. Verify every serious hook candidate:
   - opens from pain, scene, paradox, or direct clarification
   - could not be pasted unchanged into unrelated episodes
   - does not sound like generic empathy or MC hosting
   - confirms the same promise as title and thumbnail
12. If the final hook is question-led, explain briefly why it beat the direct alternatives for this episode.
13. Do not write outline or prose chapters.
14. Return the full updated `02_hook_pack.md`.
