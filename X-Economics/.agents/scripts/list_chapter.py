import json, sys, os
if len(sys.argv) < 2:
    print("Usage: python list_chapter.py [chapter_num] [optional_episode_slug]")
    sys.exit(1)
chapter = sys.argv[1]
slug = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("EPISODE_SLUG", "")
if not slug:
    eps = [d for d in os.listdir("episodes") if os.path.isdir(os.path.join("episodes", d)) and not d.startswith(".")]
    if eps:
        slug = sorted(eps, key=lambda d: os.path.getmtime(os.path.join("episodes", d)), reverse=True)[0]
    else:
        print("Error: No episode directory found and no episode slug provided.")
        sys.exit(1)
file_path = f"episodes/{slug}/scene_timing_map.json"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)
with open(file_path) as f:
    scenes = json.load(f)
ch = [s for s in scenes if s["chapter"] == chapter]
print(f"Chapter {chapter}: {len(ch)} scenes")
for s in ch:
    sid = s["id"]
    dur = s["duration_sec"]
    txt = " ".join(s["sentences"])
    words = len(txt.split())
    print(f"{sid} ({words}w, {dur}s): {txt}")
