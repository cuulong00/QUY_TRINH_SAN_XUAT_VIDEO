---
description: Revise a specific chapter based on user feedback while maintaining continuity
---
1. Ask for the episode slug, chapter number, and revision feedback if missing. A revision order from the narrative-craft review (`00_core/narrative_craft_rubric.md` §6) must name the chapter, the criterion (vd IV-a Cú lật, V Vật chứng), the faulty sentence quoted verbatim, and one sample rewrite; if an order lacks these, read `11_narrative_craft_scorecard.md` to recover them before rewriting.
2. Read the `chapter-writer` skill instructions from `.agent/skills/chapter_writer/SKILL.md`.
3. Read all core files and all state files for the target episode.
4. Read ALL existing `chapter_*.md` files in the episode (for continuity context).
5. Read `episodes/[slug]/07_golden_lines.md` to know which sentences must be preserved.
6. Rewrite only the specified chapter, incorporating the user's feedback while following chapter-writer skill guidelines.
7. Preserve any golden lines from the chapter unless the feedback explicitly asks to change them.
8. Update `09_narrative_state_tracker.md` to reflect any changes in ideas, examples, or metaphors.
8b. Self-inspect the revised chapter with **Phiếu B** of `00_core/narrative_craft_rubric.md` (quote evidence for every 4–5 and 1–2; no counting) to spot weak lines and revise before submitting; self-inspection is not a gate condition and does not count toward point K (official gate is blind scoring in Phase 10 `compliance_council` Khóa 6); record the self-inspection row in `11_narrative_craft_scorecard.md`.
9. Run the Quality & Compliance Council check on the revised chapter to update `10_compliance_report.md`.
10. Update `07_golden_lines.md` if the revision produced new strong lines or removed old ones.
11. Verify that the revised chapter still bridges naturally to the next chapter.
12. Verify that no previously used examples or metaphors from other chapters are now duplicated.
