---
description: Revise a specific chapter based on user feedback while maintaining continuity
---
1. Ask for the episode slug, chapter number, and revision feedback if missing.
2. Read the `chapter-writer` skill instructions from `.agent/skills/chapter_writer/SKILL.md`.
3. Read all core files and all state files for the target episode.
4. Read ALL existing `chapter_*.md` files in the episode (for continuity context).
5. Read `episodes/[slug]/07_golden_lines.md` to know which sentences must be preserved.
6. Rewrite only the specified chapter, incorporating the user's feedback while following chapter-writer skill guidelines.
7. Preserve any golden lines from the chapter unless the feedback explicitly asks to change them.
8. Update `05_continuity_packet.md` to reflect any changes in ideas, examples, or metaphors.
9. Update `06_claim_ledger.md` if any claims were added, removed, or reclassified.
10. Update `07_golden_lines.md` if the revision produced new strong lines or removed old ones.
11. Verify that the revised chapter still bridges naturally to the next chapter.
12. Verify that no previously used examples or metaphors from other chapters are now duplicated.
