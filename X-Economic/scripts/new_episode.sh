#!/usr/bin/env bash
set -euo pipefail

slug="${1:-}"
if [ -z "$slug" ]; then
  echo "Usage: bash scripts/new_episode.sh <episode-slug>"
  exit 1
fi

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
template_dir="$root_dir/02_templates/episode_template"
target_dir="$root_dir/episodes/$slug"

if [ ! -d "$template_dir" ]; then
  echo "Template directory not found: $template_dir"
  exit 1
fi

if [ -e "$target_dir" ]; then
  echo "Episode already exists: $target_dir"
  exit 1
fi

mkdir -p "$root_dir/episodes"
cp -R "$template_dir" "$target_dir"
rm -f "$target_dir/chapter_template.md"

TARGET_DIR="$target_dir" EPISODE_SLUG="$slug" python3 <<'PY'
from pathlib import Path
import os

target_dir = Path(os.environ["TARGET_DIR"])
slug = os.environ["EPISODE_SLUG"]

for path in target_dir.rglob("*"):
    if path.suffix not in {".md", ".csv"}:
        continue
    content = path.read_text()
    path.write_text(content.replace("__EPISODE_SLUG__", slug))
PY

echo "Created episode folder: $target_dir"
echo "Next step: fill 01_topic_qualification.md before building the brief"
