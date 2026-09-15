Create a new episode from an existing source video using the repo's remix workflow.

Arguments: `$ARGUMENTS`

Workflow:
1. Determine the source URL or target remix slug from `$ARGUMENTS`. If missing, ask the user.
2. Read before starting:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/episode_state.md`
   - `.claude/rules/creative_dna.md`
   - `03_playbooks/episode_workflow.md`
   - all relevant `00_core/*.md`
   - `00_core/remix_differentiation_guide.md`
3. Extract the source transcript into a dedicated remix episode folder.
   - required success artifacts:
     - `00_raw_transcript.txt`
     - `00_transcript_meta.json`
     - `00_transcript_segments.json`
   - required failure artifacts:
     - `00_transcript_status.md`
     - `00_transcript_error.json`
4. If transcript extraction fails, stop. Do not infer video content from URL, title, thumbnail, or memory.
5. Create `01_source_analysis.md` to capture source strengths, weaknesses, audience differences, core mechanism, and differentiation opportunities.
6. Before locking the remix brief, activate `.claude/agents/topic-ideator.md` if a sharper differentiated angle is needed.
7. Build `01_brief.md` for the remix based on a clearly differentiated angle.
8. Stop for user checkpoint after source analysis + brief.
9. Continue through the same modular flow as a normal episode:
   - `02_hook_pack.md`
   - `03_thesis_map.md`
   - `04_outline.md`
   - `chapter_XX.md` + `05`, `06`, `07`
   - `final_voiceover.md`
   - QA
   - packaging finalization
   - `visual_map.csv`
10. Ensure the remix does not copy source wording, story sequencing, or argument structure too closely.
11. Return differentiated outputs phase by phase rather than as a one-shot rewrite.
