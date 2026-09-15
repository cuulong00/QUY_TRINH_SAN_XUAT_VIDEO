#!/usr/bin/env python3
"""
VideoCore — Master One-Click Video Production CLI Wrapper
==========================================================
Usage:
  python3 scripts/produce_episode_videos.py --episode <slug>
  python3 scripts/produce_episode_videos.py --episode <slug> --monitor-only
  python3 scripts/produce_episode_videos.py --episode <slug> --dest-dir ~/Downloads/<slug>

Features:
  1. Auto-detects project root from cwd.
  2. Scans episodes/<slug>/ for prompts (prompts_chapter_*.txt or prompts/*.txt).
  3. Checks existing .mp4 files in destination to auto-generate prompts_missing.txt.
  4. Auto-detects reference assets in episodes/<slug>/ref_images/.
  5. Verifies Chrome CDP on port 9222.
  6. Launches flow_batch_daemon with 300s watchdog (5 minutes).
  7. Moves completed videos directly to the episode directory.
"""

import os
import sys
import glob
import re
import json
import time
import shutil
import argparse
import subprocess
import urllib.request

def log(msg, level="INFO"):
    timestamp = time.strftime("%H:%M:%S")
    icons = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌", "AUDIT": "📊"}
    icon = icons.get(level, "🔹")
    print(f"[{timestamp}] {icon} [{level}] {msg}", flush=True)

def find_project_root():
    cwd = os.getcwd()
    cur = cwd
    while cur != "/" and cur:
        if os.path.isdir(os.path.join(cur, "episodes")):
            return cur
        cur = os.path.dirname(cur)
    return cwd

def check_chrome_cdp(port=9222):
    last_err = ""
    for host in ["[::1]", "127.0.0.1", "localhost"]:
        try:
            req = urllib.request.Request(f"http://{host}:{port}/json", headers={"Host": f"localhost:{port}"})
            res = urllib.request.urlopen(req, timeout=3)
            tabs = json.loads(res.read().decode("utf-8"))
            return True, tabs
        except Exception as e:
            last_err = str(e)
    return False, last_err

def extract_prompts_by_scene(prompt_files):
    scenes = {}  # scene_id -> {"image": str, "video": str, "source": str}
    scene_regex = re.compile(r"^(CH\d+_SC[A-Za-z0-9_]+)\s*\[(IMAGE|VIDEO)\]:\s*(.+)$", re.IGNORECASE)

    for pfile in sorted(prompt_files):
        with open(pfile, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                m = scene_regex.match(line)
                if m:
                    sid = m.group(1).upper()
                    stype = m.group(2).upper()
                    content = m.group(3).strip()
                    if sid not in scenes:
                        scenes[sid] = {"image": "", "video": "", "source": os.path.basename(pfile)}
                    if stype == "IMAGE":
                        scenes[sid]["image"] = content
                    elif stype == "VIDEO":
                        scenes[sid]["video"] = content
    return scenes

def scan_existing_videos(dest_dir):
    existing = set()
    if not os.path.isdir(dest_dir):
        return existing

    for fpath in glob.glob(os.path.join(dest_dir, "*.mp4")):
        fname = os.path.basename(fpath)
        m = re.match(r"^(CH\d+_SC[A-Za-z0-9_]+)\.mp4$", fname, re.IGNORECASE)
        if m:
            try:
                if os.path.getsize(fpath) > 500 * 1024:
                    existing.add(m.group(1).upper())
            except Exception:
                pass
    return existing

def execute_session_refresh(port=9222, breather_s=30):
    log("==================================================================", "REFRESH")
    log("🔄 [SESSION REFRESH] Đang đảo phiên làm mới: Xóa Cache & Reload Google Flow...", "REFRESH")
    log("==================================================================", "REFRESH")
    try:
        import asyncio
        import websockets

        async def _do_refresh():
            tabs = []
            for host in ["[::1]", "127.0.0.1", "localhost"]:
                try:
                    req = urllib.request.urlopen(f"http://{host}:{port}/json", timeout=3)
                    tabs = json.loads(req.read().decode("utf-8"))
                    break
                except Exception:
                    pass
            flow_tab = next((t for t in tabs if "flow.google.com" in t.get("url", "") and "tool/" in t.get("url", "")), None)
            if not flow_tab:
                flow_tab = next((t for t in tabs if "flow.google.com" in t.get("url", "")), None)
            if not flow_tab:
                log("No flow.google.com tab found to refresh", "WARN")
                return
            ws_url = flow_tab.get("webSocketDebuggerUrl")
            async with websockets.connect(ws_url) as ws:
                # 1. Clear Browser Cache
                await ws.send(json.dumps({"id": 1, "method": "Network.enable"}))
                await ws.recv()
                await ws.send(json.dumps({"id": 2, "method": "Network.clearBrowserCache"}))
                await ws.recv()
                # 2. Hard Reload Page bypassing cache
                await ws.send(json.dumps({"id": 3, "method": "Page.enable"}))
                await ws.recv()
                await ws.send(json.dumps({"id": 4, "method": "Page.reload", "params": {"ignoreCache": True}}))
                await ws.recv()
                log("✅ Browser cache đã xóa & Tab Google Flow đã được Hard-Reload mới tinh!", "SUCCESS")

        asyncio.run(_do_refresh())
    except Exception as e:
        log(f"Session refresh notice: {e}", "WARN")

    log(f"⏸️ Nghỉ xả hơi {breather_s}s để máy chủ Google hồi phục hạn ngạch trước khi sang chương mới...", "COOLDOWN")
    time.sleep(breather_s)

def main():
    parser = argparse.ArgumentParser(description="VideoCore Produce Episode Videos CLI")
    parser.add_argument("--episode", "-e", required=True, help="Episode slug (e.g. sieu-cong-trinh-va-bat-com)")
    parser.add_argument("--project-dir", "-p", default="", help="Project root directory (auto-detected if empty)")
    parser.add_argument("--dest-dir", "-d", default="", help="Destination directory for completed videos")
    parser.add_argument("--port", type=int, default=9222, help="Chrome DevTools port (default: 9222)")
    parser.add_argument("--workers", "-w", type=int, default=4, help="Number of concurrent workers (default: 4)")
    parser.add_argument("--mode", choices=["chapter", "all"], default="chapter", help="Production mode: 'chapter' (rolling refresh per chapter) or 'all'")
    parser.add_argument("--monitor-only", action="store_true", help="Attach to running batch without re-ingesting")
    parser.add_argument("--full", action="store_true", help="Force run all scenes even if videos exist")
    args = parser.parse_args()

    project_root = os.path.abspath(args.project_dir) if args.project_dir else find_project_root()
    slug = args.episode.strip()
    episode_dir = os.path.join(project_root, "episodes", slug)

    if not os.path.isdir(episode_dir):
        log(f"Episode directory not found: {episode_dir}", "ERROR")
        sys.exit(1)

    log("==================================================================", "INFO")
    log(f"🎬 VideoCore Production Pipeline — Episode: {slug}", "INFO")
    log(f"📂 Project Root: {project_root}", "INFO")
    log(f"📁 Episode Dir:  {episode_dir}", "INFO")
    log("==================================================================", "INFO")

    # Determine destination directory
    dest_dir = os.path.abspath(os.path.expanduser(args.dest_dir)) if args.dest_dir else os.path.join(episode_dir, "videos")
    os.makedirs(dest_dir, exist_ok=True)
    log(f"🎯 Target Video Directory: {dest_dir}", "INFO")

    # 1. Check Chrome CDP
    cdp_ok, tabs_or_err = check_chrome_cdp(args.port)
    if not cdp_ok:
        log(f"Chrome Debugger is NOT reachable on port {args.port}: {tabs_or_err}", "ERROR")
        log("👉 Please launch Chrome Debugger with the following command in Terminal:", "WARN")
        print("""
open -na "Google Chrome Canary" --args \\
  --remote-debugging-port=9222 \\
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Canary-Automation" \\
  "https://flow.google.com/project/23e2de09-56ca-4203-bae0-c56f811bde25/tool/cb0f557c-bd15-4f1a-af4a-9a790b69d0c7?fromViewSource=tools&mode=EDIT"
        """)
        sys.exit(1)

    log(f"Connected to Chrome Debugger (Port {args.port}) successfully!", "SUCCESS")

    # If monitor only, directly call daemon
    daemon_script = os.path.join(os.path.dirname(__file__), "flow_batch_daemon.py")
    if not os.path.isfile(daemon_script):
        daemon_script = "/Users/pro16/Documents/VideoProject/VideoCore/scripts/flow_batch_daemon.py"

    if args.monitor_only:
        log("Attaching in MONITOR-ONLY mode...", "INFO")
        cmd = [
            sys.executable, daemon_script,
            "--dest-dir", dest_dir,
            "--port", str(args.port),
            "--monitor-only"
        ]
        subprocess.run(cmd)
        return

    # 2. Gather Prompt Files
    prompt_files = []
    prompt_files.extend(glob.glob(os.path.join(episode_dir, "prompts_chapter_*.txt")))
    prompt_files.extend(glob.glob(os.path.join(episode_dir, "prompts", "*.txt")))

    if not prompt_files:
        log(f"No prompt files found in {episode_dir} (e.g. prompts_chapter_01.txt)", "ERROR")
        sys.exit(1)

    log(f"Found {len(prompt_files)} prompt files in episode directory", "INFO")
    all_scenes = extract_prompts_by_scene(prompt_files)
    total_scenes_count = len(all_scenes)
    log(f"Total defined scenes: {total_scenes_count}", "INFO")

    # 3. Scan existing completed videos
    existing_videos = scan_existing_videos(dest_dir)
    log(f"Existing completed videos in destination: {len(existing_videos)} / {total_scenes_count}", "AUDIT")

    # 4. Calculate Missing Scenes
    missing_scenes = {sid: data for sid, data in all_scenes.items() if sid not in existing_videos} if not args.full else all_scenes

    if not missing_scenes:
        log("🎉 100% of scenes are ALREADY COMPLETED! Nothing to generate.", "SUCCESS")
        sys.exit(0)

    log(f"Missing scenes to generate: {len(missing_scenes)} / {total_scenes_count}", "WARN")

    ref_candidates = [
        os.path.join(episode_dir, "ref_images"),
        os.path.join(episode_dir, "assets"),
        os.path.join(episode_dir, "reference_images")
    ]
    ref_dir = next((c for c in ref_candidates if os.path.isdir(c)), "")
    if ref_dir:
        log(f"Found reference images folder: {ref_dir}", "INFO")
    else:
        log("No reference images folder found (continuing without avatar preloading)", "INFO")

    if args.mode == "chapter":
        # Group missing scenes by chapter
        chapters = {}
        for sid, data in missing_scenes.items():
            m = re.match(r"^(CH\d+)", sid)
            ch_key = m.group(1).upper() if m else "CH00"
            if ch_key not in chapters:
                chapters[ch_key] = {}
            chapters[ch_key][sid] = data

        ch_keys = sorted(chapters.keys())
        log(f"📦 Chế độ sản xuất cuốn chiếu theo từng Chương: {len(ch_keys)} chương cần xử lý ({', '.join(ch_keys)})", "CHAPTER")

        for i, ch_key in enumerate(ch_keys):
            ch_missing = chapters[ch_key]
            log("==================================================================", "CHAPTER")
            log(f"🎬 [{i+1}/{len(ch_keys)}] BẮT ĐẦU CHƯƠNG {ch_key}: {len(ch_missing)} cảnh cần render...", "CHAPTER")
            log("==================================================================", "CHAPTER")

            ch_missing_file = os.path.join(episode_dir, f"prompts_missing_{ch_key}.txt")
            with open(ch_missing_file, "w", encoding="utf-8") as f:
                for sid in sorted(ch_missing.keys()):
                    data = ch_missing[sid]
                    if data["image"]:
                        f.write(f"{sid} [IMAGE]: {data['image']}\n")
                    if data["video"]:
                        f.write(f"{sid} [VIDEO]: {data['video']}\n")
                    f.write("\n")

            cmd = [
                sys.executable, daemon_script,
                "--prompts", ch_missing_file,
                "--dest-dir", dest_dir,
                "--port", str(args.port),
                "--workers", str(args.workers)
            ]
            if ref_dir:
                cmd.extend(["--ref-dir", ref_dir])

            try:
                subprocess.run(cmd)
            except KeyboardInterrupt:
                log(f"Chương {ch_key} bị tạm dừng bởi người dùng.", "WARN")
                break

            ch_post_existing = scan_existing_videos(dest_dir)
            ch_still_missing = [s for s in ch_missing if s not in ch_post_existing]
            if ch_still_missing:
                log(f"Chương {ch_key} vẫn còn {len(ch_still_missing)} cảnh chưa xong. Sẽ được xử lý trong lượt quét kế tiếp.", "WARN")
            else:
                log(f"🎉 Tuyệt vời! Chương {ch_key} đã hoàn tất 100%!", "SUCCESS")

            # Thực hiện đảo phiên (Session Refresh) trước khi sang chương mới
            if i < len(ch_keys) - 1:
                execute_session_refresh(port=args.port, breather_s=30)
    else:
        # Chế độ gom toàn bộ (All in one)
        missing_file = os.path.join(episode_dir, "prompts_missing.txt")
        with open(missing_file, "w", encoding="utf-8") as f:
            for sid in sorted(missing_scenes.keys()):
                data = missing_scenes[sid]
                if data["image"]:
                    f.write(f"{sid} [IMAGE]: {data['image']}\n")
                if data["video"]:
                    f.write(f"{sid} [VIDEO]: {data['video']}\n")
                f.write("\n")

        log("==================================================================", "INFO")
        log(f"🚀 Kicking off flow_batch_daemon for {len(missing_scenes)} scenes (All-in-one)...", "LAUNCH")
        log("==================================================================", "INFO")

        cmd = [
            sys.executable, daemon_script,
            "--prompts", missing_file,
            "--dest-dir", dest_dir,
            "--port", str(args.port),
            "--workers", str(args.workers)
        ]
        if ref_dir:
            cmd.extend(["--ref-dir", ref_dir])

        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            log("Batch production interrupted by user.", "WARN")

    # 8. Post-Execution Audit
    post_existing = scan_existing_videos(dest_dir)
    post_pct = (len(post_existing) / total_scenes_count) * 100 if total_scenes_count > 0 else 0
    log("==================================================================", "AUDIT")
    log(f"🏁 PRODUCTION AUDIT: {len(post_existing)} / {total_scenes_count} scenes ({post_pct:.1f}%) in {dest_dir}", "AUDIT")
    log("==================================================================", "AUDIT")

if __name__ == "__main__":
    main()
