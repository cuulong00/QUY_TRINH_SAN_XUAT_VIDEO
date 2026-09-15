---
description: >-
  Orchestration workflow for full episode production. Coordinates the canonical
  phase-by-phase flow defined in .agents/rules/content-os-pipeline.md and implemented in .agents/skills/*.
---

Episode production orchestration workflow.

Canonical sources of truth:
- `.agents/rules/content-os-pipeline.md` for workflow order, approval gates, and non-negotiables
- `.agents/AGENTS.md` for channel DNA, strict protocols, and safety compliance
- `.agents/skills/*` for phase execution contracts and specialist craft methods
- `CLAUDE.md` for episode mandatory files and audit tools

Operating rules:
1. Work in exactly one episode folder under `episodes/[slug]/`.
2. Run exactly one canonical phase at a time in sequence. Do NOT skip phases.
3. Stop at the human approval gates defined in `content-os-pipeline.md`.
4. Always read and update repo files. Files are the single source of truth.
