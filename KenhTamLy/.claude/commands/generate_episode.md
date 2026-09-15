Generate a complete episode through the modular workflow.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the topic or episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read before doing anything else:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/depth_and_humanness.md`
   - `.claude/rules/episode_state.md`
   - `.claude/rules/creative_dna.md`
   - `.claude/rules/expert_panel.md`
   - `03_playbooks/episode_workflow.md`
   - `03_playbooks/quality_stability_system.md`
   - all relevant `00_core/*.md`
3. Throughout the workflow, explicitly activate the stage expert persona rather than producing neutral generic copy.
4. Phase 0 — Topic Strategy (Gate 0, blocking):
   - if the user is giving a raw topic, activate `.claude/agents/topic-ideator.md` first
   - compare multiple angles, hidden pains, and touchpoints before locking the brief
   - choose the sharpest angle for this episode, not the most generic one
   - do not proceed until Gate 0 has produced:
     - one chosen angle
     - one central hidden pain
     - one clear reason this angle deserves to represent the channel lens
5. Phase 1 — Brief:
   - activate `.claude/agents/script-architect.md`
   - only begin after Gate 0 is complete; if the angle is still soft or generic, stop and sharpen it first
   - create or refresh `episodes/[slug]/01_brief.md`
   - lock audience, pain, promise, behavioral lens, evidence posture, Topic Depth Score, and runtime contract
   - stop for user checkpoint after brief
6. Phase 2 — Hook Lab:
   - activate `.claude/agents/hook-engine.md`
   - create or refresh `episodes/[slug]/02_hook_pack.md`
   - generate angles, title candidates, thumbnail angles, 10 hooks, top 3 hooks, final hook, intro kênh, CTA mềm, and 5 mini re-hooks
   - stop for user checkpoint after hook pack
7. Phase 3 + 4 — Thesis Map + Retention-first Outline:
   - activate `.claude/agents/script-architect.md`
   - create or refresh `episodes/[slug]/03_thesis_map.md` and `episodes/[slug]/04_outline.md`
   - ensure open loops, paradoxes, payoff requirements, chapter roles, retention moves, and chapter budgets are locked
   - stop for user checkpoint after outline
8. Phase 5 — Chapter Writing:
   - activate `.claude/agents/chapter-writer.md`
   - write one `chapter_XX.md` at a time
   - after each chapter update `05_continuity_packet.md`, `06_claim_ledger.md`, and `07_golden_lines.md`
   - do not skip chapter-by-chapter state updates
   - keep one living voice and strong bridge continuity across the set
9. Phase 6 — Final Merge:
   - activate `.claude/agents/oral-polisher.md`
   - create or refresh `final_voiceover.md`
   - preserve opening architecture, chapter roles, second-half lifts, transitions, and ending payoff
10. Phase 7 — Final QA:
   - activate `.claude/agents/behavioral-safety-qa.md`
   - run behavioral safety QA, repetition QA, retention QA, oral QA, packaging/alignment QA, runtime compliance QA, architecture coverage QA, and anti-industrial continuity QA
   - only proceed if verdict is PASS
   - stop for user checkpoint after QA
11. Phase 8 — Packaging Finalization:
   - activate `.claude/agents/thumbnail-architect.md` for `08_thumbnail_brief.md`
   - activate `.claude/agents/metadata-architect.md` for `09_youtube_metadata.md`
   - create or refresh `08_thumbnail_brief.md`
   - create or refresh `09_youtube_metadata.md`
12. Phase 9 — Visual Planning:
   - create or refresh `visual_map.csv`
13. Phase 10 — Scene Mapping:
   - create or refresh `scene_map.json`
   - enforce: hook 1 câu = 1 ảnh; các phần khác tối đa 3 câu = 1 ảnh
   - ensure `visual_summary` preserves the full meaning of all grouped sentences
14. Phase 11 — Visual Prompts:
   - create or refresh `visual_prompts.md`
   - generate exactly one prompt block per scene in `scene_map.json`
15. Phase 12 — Image Finalization + Slideshow Render:
   - finalize images into `images_final/`
   - render `video/slideshow_base.mp4`
   - update `production_notes.md` with image/render handoff notes
16. Update `01_management/episode_registry.csv` at major checkpoints.
17. Never collapse the whole task into a one-shot script response.
18. Never bypass Gate 0 by letting a raw topic drift straight into brief or outline language.
