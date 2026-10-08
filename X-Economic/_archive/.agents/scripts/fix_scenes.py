import json
import os
import re

chapters = ["chapter_01.md", "chapter_02.md", "chapter_03.md", "chapter_04.md", "chapter_05.md", "chapter_06.md", "chapter_07.md"]
scenes = []
scene_id = 1

def split_sentences(text):
    text = text.replace("\n", " ")
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in parts if s.strip()]

for i, ch in enumerate(chapters):
    path = os.path.join("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/nghich-ly-gia-xang-viet-nam/", ch)
    with open(path, "r", encoding="utf-8") as f:
        sentences = split_sentences(f.read())
        
        # Chapter 1 is the Hook: 1 sentence = 1 scene
        if i == 0:
            for s in sentences:
                scenes.append({
                    "id": f"SC{scene_id:03d}",
                    "text": s,
                    "sentence_count": 1,
                    "duration_sec": 5,
                    "visual_summary": f"Hook Scene: {s[:60]}..."
                })
                scene_id += 1
        else:
            # Body chapters: max 3 sentences per scene (we will group by 2 or 3 depending on sequence to mix it up)
            chunk = []
            for s in sentences:
                chunk.append(s)
                # Let's just group by 2 so it's consistent 10s, unless there's an odd one left
                if len(chunk) == 2 or s == sentences[-1]:
                    if len(chunk) == 1 and s == sentences[-1] and scenes[-1]["sentence_count"] < 3:
                        # Append to previous scene if it's just 1 sentence left over
                        scenes[-1]["text"] += " " + s
                        scenes[-1]["sentence_count"] += 1
                        scenes[-1]["duration_sec"] += 5
                        chunk = []
                    else:
                        scenes.append({
                            "id": f"SC{scene_id:03d}",
                            "text": " ".join(chunk),
                            "sentence_count": len(chunk),
                            "duration_sec": len(chunk) * 5,
                            "visual_summary": f"Body Scene: {' '.join(chunk)[:60]}..."
                        })
                        scene_id += 1
                        chunk = []

with open("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/nghich-ly-gia-xang-viet-nam/scene_timing_map.json", "w", encoding="utf-8") as f:
    json.dump(scenes, f, indent=2, ensure_ascii=False)
    
print(f"Total Scenes: {len(scenes)}")
print(f"Total Duration: {sum(s['duration_sec'] for s in scenes)} seconds")
