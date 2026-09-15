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

if [ -e "$target_dir" ]; then
  echo "Episode already exists: $target_dir"
  exit 1
fi

mkdir -p "$root_dir/episodes"
cp -R "$template_dir" "$target_dir"
find "$target_dir" -type f \( -name '*.md' -o -name '*.csv' \) -print0 | while IFS= read -r -d '' file; do
  sed -i '' "s/__EPISODE_SLUG__/$slug/g" "$file"
done

echo "Created episode folder: $target_dir"