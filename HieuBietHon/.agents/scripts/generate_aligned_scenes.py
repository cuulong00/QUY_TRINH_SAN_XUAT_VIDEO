import json
import os
import re

chapters = ["chapter_01.md", "chapter_02.md", "chapter_03.md", "chapter_04.md", "chapter_05.md", "chapter_06.md", "chapter_07.md"]
sentences = []

for ch in chapters:
    path = os.path.join("/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/nghich-ly-gia-xang-viet-nam/", ch)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().replace("\n", " ")
        parts = re.split(r'(?<=[.!?])\s+', text)
        sentences.extend([s.strip() for s in parts if s.strip()])

# We have N sentences, we want 60 scenes.
# Group them proportionally.
total_sentences = len(sentences)
scenes = []
chunk_size = total_sentences / 60.0

current_chunk = []
current_words = 0
scene_id = 1
next_target = chunk_size

for i, s in enumerate(sentences):
    current_chunk.append(s)
    current_words += len(s.split())
    
    if (i + 1) >= next_target or i == len(sentences) - 1:
        duration = int(round((current_words / 215.0) * 60))
        if duration < 3: duration = 3
        
        scenes.append({
            "id": f"SC{scene_id:03d}",
            "text": " ".join(current_chunk),
            "sentence_count": len(current_chunk),
            "duration_sec": duration,
            "visual_summary": f"Scene illustrating: {' '.join(current_chunk)[:50]}..."
        })
        scene_id += 1
        current_chunk = []
        current_words = 0
        next_target += chunk_size

# ensure we don't have exactly 61 if precision issue
if len(scenes) > 60:
    # merge last two
    scenes[-2]["text"] += " " + scenes[-1]["text"]
    scenes[-2]["sentence_count"] += scenes[-1]["sentence_count"]
    scenes[-2]["duration_sec"] += scenes[-1]["duration_sec"]
    scenes.pop()

with open("/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/nghich-ly-gia-xang-viet-nam/scene_timing_map.json", "w", encoding="utf-8") as f:
    json.dump(scenes, f, indent=2, ensure_ascii=False)
