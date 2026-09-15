---
name: batch-video-generator
description: Automated video production pipeline using Google Flow Tool Builder (Nano Banana 2 & Veo 3.1 Lite) via Chrome Remote Debugging Protocol (CDP port 9222). Supports smart queue diffing, 5-minute watchdog, slot force-skip with image preservation, and auto-downloading.
---

# Batch Video Generator Skill

## Overview
This skill automates the production of batch AI videos for documentary/podcast episodes across all channels (`GocNhinPodcast`, `Dong_Chay`, `X-Economics`, etc.). It coordinates between prompt files, reference assets, Chrome CDP (port 9222), Google Flow Tool Builder, and local file management.

## Prerequisites
1. **Dedicated Automation Browser: Google Chrome Canary (BẮT BUỘC)**:
   - **Tôn chỉ cách ly tuyệt đối:** TUYỆT ĐỐI KHÔNG dùng hoặc can thiệp vào trình duyệt Google Chrome chính của người dùng. Mọi tác vụ tự động hóa video/flow BẮT BUỘC phải chạy trên **Google Chrome Canary** (Icon Vàng óng).
   - **Ghi nhớ phiên đăng nhập vĩnh viễn:** Sử dụng thư mục `--user-data-dir` cố định để bảo toàn cookies và thông tin đăng nhập Google Flow, không bao giờ phải đăng nhập lại.
   - Khởi chạy nhanh bằng script hoặc câu lệnh:
     ```bash
     bash scripts/launch_canary_flow.sh
     # Hoặc chạy lệnh trực tiếp:
     open -na "Google Chrome Canary" --args \
       --remote-debugging-port=9222 \
       --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Canary-Automation" \
       "https://flow.google.com/project/23e2de09-56ca-4203-bae0-c56f811bde25/tool/cb0f557c-bd15-4f1a-af4a-9a790b69d0c7?fromViewSource=tools&mode=EDIT"
     ```
2. **Episode Directory Structure**:
   ```text
   episodes/[slug]/
   ├── prompts_chapter_01.txt ... prompts_chapter_XX.txt (or prompts/*.txt)
   ├── ref_images/ (optional reference assets e.g. @avatar.jpg)
   └── videos/ (destination folder for completed .mp4 files)
   ```

## Standard Execution

### 1. Audit Progress
To check what scenes are already completed vs missing:
```bash
python3 scripts/check_video_progress.py --episode <slug>
```

### 2. Launch or Resume Production
To automatically diff missing scenes, ingest prompts & reference assets, and launch the batch:
```bash
python3 scripts/produce_episode_videos.py --episode <slug>
```

### 3. Attach in Monitor-Only Mode
If a batch is already running in Chrome and you only want to monitor progress, auto-skip stuck slots, and move downloaded videos:
```bash
python3 scripts/produce_episode_videos.py --episode <slug> --monitor-only
```

## System Invariants & Safety Protocols
- **Watchdog Timeout**: Must be set to **5 minutes (300 seconds)** for Veo 3.1 Lite video requests.
- **Image Preservation**: When a video request times out, the slot's `close` button is clicked to demote only the video task to the tail of the queue. Generated images are never deleted.
- **Zero-Token Rule**: The agent must run monitoring via the background daemon rather than polling in continuous chat turns.
- **Circuit Breaker Defense**: If Google Flow hits 10 consecutive server errors, the system freezes for 180s to cool down before resuming safely.
