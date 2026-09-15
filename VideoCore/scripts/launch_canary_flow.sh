#!/bin/bash
# VideoCore - Launch Google Chrome Canary dedicated for Flow Automation
# Uses persistent user-data-dir so login sessions and cookies are saved permanently.

DATA_DIR="$HOME/Library/Application Support/Google/Chrome-Canary-Automation"
FLOW_URL="https://flow.google.com/project/23e2de09-56ca-4203-bae0-c56f811bde25/tool/cb0f557c-bd15-4f1a-af4a-9a790b69d0c7?fromViewSource=tools&mode=EDIT"

echo "🚀 Launching Google Chrome Canary on debug port 9222..."
echo "📂 Profile Data Directory: $DATA_DIR"

open -na "Google Chrome Canary" --args \
  --remote-debugging-port=9222 \
  --user-data-dir="$DATA_DIR" \
  "$FLOW_URL"
