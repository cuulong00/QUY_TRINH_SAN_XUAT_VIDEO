---
description: >-
  Legacy orchestration wrapper for episode production. Prefer the canonical
  phase-by-phase flow defined in CLAUDE.md and implemented in .claude/skills/*.
---

Legacy wrapper only.

Canonical sources of truth:
- `CLAUDE.md` for workflow order, approval gates, and non-negotiables
- `.claude/rules/*` for artifact and phase rules
- `.claude/skills/*` for phase execution contracts

Use this file only as a routing reminder:
1. Work in exactly one episode.
2. Run exactly one canonical phase at a time.
3. Stop at the approval gates defined in `CLAUDE.md`.
4. Do not treat this wrapper as a full autonomous pipeline spec.
5. Do not duplicate policy here if it already exists in canonical sources.
