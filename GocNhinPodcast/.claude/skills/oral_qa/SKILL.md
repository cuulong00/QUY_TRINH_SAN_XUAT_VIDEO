---
name: oral_qa
description: Run oral QA on an episode.
argument-hint: <episode-slug>
---

Run oral QA on an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/oral-polisher.md`.
- Align the pass with the `.agents` Voice Architect baseline from `.agents/personas/the_voice_architect.md` and `.agents/skills/oral_polisher/SKILL.md`.
- This phase owns breath, cadence, spoken authority, and TTS/human narration readiness. It must not become a substitute for financial QA or structural editorial review.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/04_retention_map.md`
   - `episodes/[slug]/07_golden_lines.md` if it exists
   - `00_core/anti_ai_isms.md`
3. Do not default to reading all state files or all chapter drafts unless a pacing or transition issue cannot be diagnosed from the working set.
4. Review for:
   - spoken opening quality
   - mid-video pacing
   - breath rhythm
   - number readability
   - re-hook naturalness
   - ending impact
   - announcement density
   - slogan density
   - expert credibility in the ear
5. This phase focuses on orality, cadence, and spoken authority. It should not become a substitute for financial QA or editorial caliber review.
6. The specialist agent owns spoken taste, cadence, and vocal authority; this skill only defines the QA workflow, files, and update contract.
7. Create or update `episodes/[slug]/oral_qa.md`.
8. Update `episodes/[slug]/final_voiceover.md` if needed.
9. Update `01_management/episode_registry.csv` for the completed phase.
10. Stop for user approval after returning the updated QA file and any changed voiceover content.
