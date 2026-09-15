#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED_RULE_FILES = [
    Path('.claude/rules/script_production_flow.md'),
    Path('.claude/rules/core_references.md'),
    Path('.claude/rules/quality_constraints.md'),
    Path('.claude/rules/episode_state.md'),
]

PROJECT_SENTINELS = [
    Path('CLAUDE.md'),
    Path('.claude/commands'),
    Path('.claude/agents'),
]

PROTECTED_PATHS = {
    'CLAUDE.md',
    '.claude/settings.json',
}


def emit_allow():
    print(json.dumps({
        'hookSpecificOutput': {
            'hookEventName': 'PreToolUse',
            'permissionDecision': 'allow',
            'permissionDecisionReason': 'Repo guard checks passed.'
        }
    }))


def emit_deny(reason: str):
    print(json.dumps({
        'hookSpecificOutput': {
            'hookEventName': 'PreToolUse',
            'permissionDecision': 'deny',
            'permissionDecisionReason': reason
        }
    }))


def paths_from_payload(payload: dict) -> list[str]:
    tool_name = payload.get('tool_name') or payload.get('toolName')
    tool_input = payload.get('tool_input') or payload.get('toolInput') or {}
    if tool_name in {'Write', 'Edit'}:
        path = tool_input.get('file_path')
        return [path] if path else []
    if tool_name == 'MultiEdit':
        path = tool_input.get('file_path')
        return [path] if path else []
    return []


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        emit_allow()
        return

    project_dir = Path(payload.get('cwd') or payload.get('project_dir') or '.').resolve()

    for sentinel in PROJECT_SENTINELS:
        if not (project_dir / sentinel).exists():
            emit_deny(f'Missing required project structure: {sentinel}')
            return

    for rule_file in REQUIRED_RULE_FILES:
        if not (project_dir / rule_file).exists():
            emit_deny(f'Missing required Claude rule file: {rule_file}')
            return

    target_paths = paths_from_payload(payload)
    relative_targets = []
    for raw in target_paths:
        if not raw:
            continue
        try:
            path = Path(raw)
            if path.is_absolute():
                rel = path.resolve().relative_to(project_dir)
            else:
                rel = (project_dir / path).resolve().relative_to(project_dir)
            relative_targets.append(rel.as_posix())
        except Exception:
            continue

    if any(target in PROTECTED_PATHS for target in relative_targets):
        emit_deny('Protected repo governance file detected. Re-run intentionally after reviewing the standardization surface.')
        return

    emit_allow()


if __name__ == '__main__':
    main()
