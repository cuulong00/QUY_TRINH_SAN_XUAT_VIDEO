---
name: editorial_qa
description: Run editorial and legal compliance QA on an episode.
argument-hint: <episode-slug>
---

Run editorial & legal QA on an episode.

Arguments: `$ARGUMENTS`

Required specialist context:
- Before producing output, load `.claude/agents/editorial-qa.md`.
- Align the pass with the `.agents` Editorial QA baseline led by the Data Auditor and calibrated against the stricter evidentiary discipline in `.agents/personas/the_data_auditor.md`.
- This phase is for safety, sourcing, claim strength, and taxonomy calibration. It must not drift into generic editorial cleanup or oral polish.

Workflow:
1. Determine the episode slug from `$ARGUMENTS`. If missing, ask the user.
2. Run the automated Google AI Search Mode audit:
   - Run `python3 scripts/google_ai_audit.py episodes/[slug] --all` to cross-verify all script chapters against current web data.
   - Read the generated `episodes/[slug]/google_ai_audit_results.md` to identify factual inaccuracies, outdated laws, or overclaiming.
3. Read the editorial QA working set:
   - `episodes/[slug]/final_voiceover.md`
   - `episodes/[slug]/10_claim_ledger.md`
   - `00_core/brand_safety_guidelines.md`
   - `00_core/anti_patterns.md`
4. Only backtrace to chapter files, research state, or other upstream files when a flagged claim cannot be resolved from the working set or the Google AI audit report.
5. Review for:
   - compliance note presence
   - political/cybersecurity risk
   - moralizing tone and social bias risk
   - fabricated stats risk
   - claim-labeling consistency
   - overclaiming
   - overdramatized causality
   - advice drift hidden behind disclaimers
   - unsupported implication chains
6. This phase is for safety, evidence, and regulatory calibration only; editorial caliber, repetition, and voice authority belong to editorial review and oral QA, not editorial QA.
7. The specialist agent owns evidentiary judgment and calibration; this skill only defines the QA workflow, files, and update contract.
8. Create or update `episodes/[slug]/editorial_qa.md`.
9. Update `episodes/[slug]/final_voiceover.md` if safety wording must change.
10. Update `01_management/episode_registry.csv` for the completed phase.
11. Return the updated QA file and any changed voiceover content.

