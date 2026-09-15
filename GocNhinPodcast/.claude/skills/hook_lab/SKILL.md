---
name: hook_lab
description: Create the hook pack for an episode.
argument-hint: <episode-slug>
---

Create the hook pack for an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/hook-engine.md`.
- Also load `.claude/agents/script-architect.md` so the hook pass stays locked to the actual strategic angle rather than becoming isolated packaging.
- Align taste with the `.agents` Hook Engine baseline: contradiction-led curiosity, anti-completion, personal-stakes anchoring, and non-reusable openings.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/00_topic_qualification.md`
   - `episodes/[slug]/01_brief.md`
   - `episodes/[slug]/02_research_map.md`
3. Create or update `episodes/[slug]/02_hook_pack.md` only.
4. Generate:
   - multiple angle candidates
   - multiple title directions
   - multiple hook candidates
   - top hooks
   - one final hook
   - one backup hook
   - 5 mini re-hooks
5. Ensure title-hook alignment is explicit and hook wording stays financial-safe.
6. Include at least one calm, high-caliber “quiet expert” hook that does not rely on shock phrases or teaser language.
7. Reject hooks that use banned AI-isms or could fit almost any finance video.
8. Add an originality check: explain why the final hook sounds specific to this episode and this channel.
9. **ANTI-COMPLETION CHECK (mandatory):** Every hook MUST be tested: "If the viewer stops after this hook, do they feel they understood enough?" If YES → hook self-closes → REWRITE.
10. **PERSONAL STAKES ANCHOR:** Hook MUST contain at least 1 phrase tied to viewer's personal finances ("tiền", "lãi vay", "sổ đỏ", "việc làm", "khoản vay", "tài sản", "thu nhập").
11. **RE-HOOK #1:** The first re-hook (~3:30 mark) MUST promise PERSONAL value ("your mortgage", "your assets"), NOT just "interesting insight."
12. Update `01_management/episode_registry.csv` for the completed phase.
13. Do not write thesis, outline, or prose chapters.
14. Stop for user approval after returning the full updated `02_hook_pack.md`.
15. Do not bypass this phase by drafting later outputs in chat.