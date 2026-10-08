---
name: qualify_topic
description: Qualify a raw topic for an episode before writing the brief.
argument-hint: <episode slug or topic file>
---

Qualify a raw topic for an episode before writing the brief.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/content-strategist.md`.
- Align judgment with the `.agents` baseline for this phase, especially `.agents/personas/the_content_strategist.md` and `.agents/skills/content_strategist/SKILL.md`.
- This phase is not generic topic brainstorming; it is a Content Strategist pass.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read `00_core/*.md`.
3. Create or update `episodes/[slug]/00_topic_qualification.md` only.
4. Identify:
   - primary persona candidate
   - hidden pain
   - false belief to attack
   - why now
   - 3 viral angle candidates
   - data / case-study viability
   - legal or safety risks
5. Update `01_management/episode_registry.csv` for the completed phase.
6. Do not write the brief yet.
7. Stop for user approval after returning the full updated `00_topic_qualification.md`.
8. Do not bypass this phase by drafting later outputs in chat.