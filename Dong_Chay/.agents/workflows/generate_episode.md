---
description: >-
  Legacy orchestration wrapper for episode production. Prefer the canonical
  phase-by-phase flow defined in .agents/workflows/ and rules in 00_core/.
---

Legacy wrapper only.

Canonical sources of truth:
- `00_core/` for workflow rules, style guides, and non-negotiables
- `.agents/workflows/` for phase step-by-step guides
- `.agents/skills/` for specialist personas and craft methods

Use this file only as a routing reminder:
1. Work in exactly one episode.
2. Run exactly one canonical phase at a time.
3. Stop at the approval gates defined in `.agents/rules/content-os-pipeline.md`.
4. Do not treat this wrapper as a full autonomous pipeline spec.
5. Do not duplicate policy here if it already exists in canonical sources.
