#!/usr/bin/env bash
# ==============================================================================
# VideoCore — Universal Project Symlink & Integration Provisioner
# ==============================================================================
# Usage:
#   bash setup_project_symlinks.sh /path/to/project
# Example:
#   bash setup_project_symlinks.sh /Users/pro16/Documents/VideoProject/Dong_Chay
# ==============================================================================

set -euo pipefail

CORE_DIR="/Users/pro16/Documents/VideoProject/VideoCore"
TARGET_DIR="${1:-}"

if [[ -z "$TARGET_DIR" || ! -d "$TARGET_DIR" ]]; then
  echo "❌ Error: Please specify a valid target project directory."
  echo "Usage: bash $0 /path/to/project"
  exit 1
fi

TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
PROJECT_NAME="$(basename "$TARGET_DIR")"

echo "=================================================================="
echo "🔗 Provisioning VideoCore Symlinks for: $PROJECT_NAME"
echo "📂 Target Directory: $TARGET_DIR"
echo "📂 Core Engine:      $CORE_DIR"
echo "=================================================================="

# 1. Setup Scripts Symlinks
mkdir -p "$TARGET_DIR/scripts"

for script in produce_episode_videos.py check_video_progress.py flow_batch_daemon.py; do
  TARGET_FILE="$TARGET_DIR/scripts/$script"
  SOURCE_FILE="$CORE_DIR/scripts/$script"
  
  if [[ -L "$TARGET_FILE" || -f "$TARGET_FILE" ]]; then
    rm -f "$TARGET_FILE"
  fi
  ln -s "$SOURCE_FILE" "$TARGET_FILE"
  echo "  ✅ Linked: scripts/$script -> VideoCore/scripts/$script"
done

# 2. Setup Agent Skill Symlink
mkdir -p "$TARGET_DIR/.agents/skills"
TARGET_SKILL="$TARGET_DIR/.agents/skills/batch_video_generator"
SOURCE_SKILL="$CORE_DIR/.agents/skills/batch_video_generator"

if [[ -L "$TARGET_SKILL" || -d "$TARGET_SKILL" ]]; then
  rm -rf "$TARGET_SKILL"
fi
ln -s "$SOURCE_SKILL" "$TARGET_SKILL"
echo "  ✅ Linked: .agents/skills/batch_video_generator -> VideoCore/.agents/skills/batch_video_generator"

# 3. Setup Tools Symlink
mkdir -p "$TARGET_DIR/tools"
TARGET_STUDIO="$TARGET_DIR/tools/flow_batch_studio"
SOURCE_STUDIO="$CORE_DIR/tools/flow_batch_studio"

if [[ -L "$TARGET_STUDIO" || -d "$TARGET_STUDIO" ]]; then
  rm -rf "$TARGET_STUDIO"
fi
ln -s "$SOURCE_STUDIO" "$TARGET_STUDIO"
echo "  ✅ Linked: tools/flow_batch_studio -> VideoCore/tools/flow_batch_studio"

echo "=================================================================="
echo "🎉 Project '$PROJECT_NAME' is now fully equipped with VideoCore!"
echo "👉 You can now run directly inside '$PROJECT_NAME':"
echo "   python3 scripts/check_video_progress.py --episode <slug>"
echo "   python3 scripts/produce_episode_videos.py --episode <slug>"
echo "=================================================================="
