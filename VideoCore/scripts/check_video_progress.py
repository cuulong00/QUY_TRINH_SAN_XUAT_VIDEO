#!/usr/bin/env python3
"""
VideoCore — Episode Video Progress Auditor
==========================================
Usage:
  python3 scripts/check_video_progress.py --episode <slug>
"""

import os
import sys
import glob
import re
import argparse

def find_project_root():
    cwd = os.getcwd()
    cur = cwd
    while cur != "/" and cur:
        if os.path.isdir(os.path.join(cur, "episodes")):
            return cur
        cur = os.path.dirname(cur)
    return cwd

def main():
    parser = argparse.ArgumentParser(description="Audit Episode Video Progress")
    parser.add_argument("--episode", "-e", required=True, help="Episode slug")
    parser.add_argument("--project-dir", "-p", default="", help="Project root directory")
    parser.add_argument("--dest-dir", "-d", default="", help="Directory where .mp4 files reside")
    args = parser.parse_args()

    project_root = os.path.abspath(args.project_dir) if args.project_dir else find_project_root()
    slug = args.episode.strip()
    episode_dir = os.path.join(project_root, "episodes", slug)

    if not os.path.isdir(episode_dir):
        print(f"❌ Episode directory not found: {episode_dir}")
        sys.exit(1)

    # 1. Gather all scenes defined in prompts
    prompt_files = glob.glob(os.path.join(episode_dir, "prompts_chapter_*.txt"))
    prompt_files.extend(glob.glob(os.path.join(episode_dir, "prompts", "*.txt")))

    all_scenes = set()
    scene_regex = re.compile(r"^(CH\d+_SC[A-Za-z0-9_]+)\s*\[(IMAGE|VIDEO)\]:", re.IGNORECASE)
    for pf in prompt_files:
        with open(pf, "r", encoding="utf-8") as f:
            for line in f:
                m = scene_regex.match(line.strip())
                if m:
                    all_scenes.add(m.group(1).upper())

    # 2. Check videos in dest_dir or episode/videos
    dest_candidates = [
        args.dest_dir,
        os.path.join(episode_dir, "videos"),
        os.path.expanduser(f"~/Downloads/{slug}"),
        "/Users/pro16/Downloads/sieucongtrinhvabatcom" if "sieu-cong-trinh" in slug else "",
        os.path.expanduser(f"~/Downloads/vinhthailansongngamngoaigiao") if "vinh-thai-lan" in slug else ""
    ]
    target_dest = ""
    for c in dest_candidates:
        if c and os.path.isdir(c) and glob.glob(os.path.join(c, "*.mp4")):
            target_dest = c
            break
    if not target_dest:
        target_dest = os.path.join(episode_dir, "videos")

    existing_videos = {}
    if os.path.isdir(target_dest):
        for fpath in glob.glob(os.path.join(target_dest, "*.mp4")):
            fname = os.path.basename(fpath)
            m = re.match(r"^(CH\d+_SC[A-Za-z0-9_]+)\.mp4$", fname, re.IGNORECASE)
            if m:
                size_mb = os.path.getsize(fpath) / (1024 * 1024)
                if size_mb > 0.5:
                    existing_videos[m.group(1).upper()] = size_mb

    missing = sorted(list(all_scenes - set(existing_videos.keys())))
    total = len(all_scenes)
    completed = len(existing_videos)
    pct = (completed / total * 100) if total > 0 else 0

    print("==================================================================")
    print(f"📊 EPISODE AUDIT: {slug}")
    print(f"📂 Location:      {target_dest}")
    print(f"✅ Completed:     {completed} / {total} scenes ({pct:.1f}%)")
    print(f"❌ Missing:       {len(missing)} scenes")
    print("==================================================================")

    if missing:
        print("Missing Scene IDs:")
        for i in range(0, len(missing), 6):
            print("  " + "  ".join(missing[i:i+6]))
        print("==================================================================")
    else:
        print("🎉 ALL SCENES COMPLETED 100%!")

if __name__ == "__main__":
    main()
