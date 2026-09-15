import json

with open("episodes/nghich-ly-ma-sat-thoi-quen/scene_map.json") as f:
    scenes = json.load(f)

missing = [s for s in scenes if s["visual_summary"].startswith("[CẢNH BỔ SUNG")]
print(f"Missing {len(missing)} scenes")

import re, os
def split_sentences(text):
    text = re.sub(r"#{1,3}\s+.*", "", text)
    text = re.sub(r"\*\*|\*|_", "", text)
    text = text.strip()
    sents = [s.strip() for s in re.split(r'(?<=[.!?""*])\s+', text) if s.strip() and len(s.strip()) > 5]
    return sents

chapters = {}
for i in range(1, 9):
    with open(f"episodes/nghich-ly-ma-sat-thoi-quen/chapter_{i:02d}.md") as f:
        chapters[i] = split_sentences(f.read())

for s in missing:
    ch = s["chapter"]
    group_size = 1 if ch == 1 else 3
    ch_scenes = [x for x in scenes if x["chapter"] == ch]
    ch_index = ch_scenes.index(s)
    
    start = ch_index * group_size
    end = start + group_size
    # safely handle out of bounds
    sents = chapters[ch][start:end] if start < len(chapters[ch]) else []
    print(f"[{s['id']}] Ch{ch}: {' '.join(sents)}")
