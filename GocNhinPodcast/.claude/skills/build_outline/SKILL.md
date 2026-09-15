---
name: build_outline
description: Build the outline for an episode after thesis and retention are already locked.
argument-hint: <episode-slug>
---

Build the outline for an episode after thesis and retention are already locked.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/script-architect.md`.
- Align judgment with the `.agents` Script Architect baseline: Macro Strategist + Narrative Director.
- This phase must lock structure, chapter necessity, and Personal Stakes by Chapter 2 without scripting prose choreography.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Read:
   - `00_core/*.md`
   - `episodes/[slug]/01_brief.md`
   - `episodes/[slug]/02_research_map.md`
   - `episodes/[slug]/02_hook_pack.md`
   - `episodes/[slug]/03_thesis_map.md`
   - `episodes/[slug]/04_retention_map.md`
3. Create or update `episodes/[slug]/04_outline.md` only.
4. Ensure each chapter has:
   - a distinct analytical function
   - a belief to overturn
   - an evidence anchor
   - an expert lens
   - a chapter signature (a unique writing/tone rule for this specific chapter to prevent monotony)
   - a reason this chapter exists in the argument
   - NO mechanistic transition sentences (never require the writer to output a predefined bridge)
   - NO prompt metadata leaks (never prescribe labels like 'interpretive move' or 'judgment')
5. **PERSONAL-FIRST STRUCTURE (mandatory):**
   - **6-8 chapters, 18-25 minutes.** Not 10-12 chapters.
   - **COLD AUDIENCE RULE:** GocNhinPodcast is a NEW channel. No loyal audience. Viewers arrive via algorithm with ZERO trust and ZERO patience. They will scroll away in 3 seconds if the hook is not immediately relevant.
     - **Hook MUST open with CURRENT data/events** — something the viewer JUST saw on their newsfeed (GDP just released, FDI latest, policy just announced, trending debate).
     - **NEVER open with distant history** (1954, 1986, etc.) — cold viewers won't wait for the connection. History goes in Ch.3+ as pattern/evidence.
     - **First sentence = reason to STOP SCROLLING.** No second chances.
   - Ch.1 = Hook + Open Loop (tied to viewer's PERSONAL finances). Hook MUST NOT self-close.
   - **Ch.2 = Personal Stakes** — "How does this affect YOUR money/job/mortgage?" (MANDATORY. NEVER framework, case study, or foreign economics.)
   - Re-hook between Ch.2-Ch.3 promising PERSONAL value.
   - Ch.3 = Mechanism + max 1 international case study.
   - New Data Shock between Ch.3-Ch.4.
   - Ch.4-5 = Deepening + Action Framework.
   - Ch.6 (or final) = High-energy close + CTA.
6. **STRUCTURAL CONSTRAINTS (hard fail):**
   - Maximum 2 international case studies in the entire outline. Each ≤ 3 minutes.
   - No segment > 3 minutes of pure framework/theory without personal-stakes anchor.
   - Hook must NOT self-close (Anti-Completion Rule).
   - Ch.2 MUST be Personal Stakes — if it's framework/foreign case study → reject outline.
7. **RETENTION GATE:** Before proceeding to chapter briefs, verify outline against `00_core/retention_gate_checklist.md`. If outline scores < 8/10 → fix outline first.
8. Make sure the outline contains real analytical movement, not just clean structure.
9. Leave the interpretation style, judgment quality, and role-specific thinking to the relevant specialist agent; this skill defines the workflow contract, not the expert persona.
10. Update `01_management/episode_registry.csv` for the completed phase.
11. Do not write prose chapters.
12. Stop for user approval after returning the full updated `04_outline.md`.
13. If thesis + retention are also being finalized in this pass, stop for user approval before chapter planning.