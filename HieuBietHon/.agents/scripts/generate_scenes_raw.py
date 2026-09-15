import os
import re
import json

chapters = ["chapter_01.md", "chapter_02.md", "chapter_03.md", "chapter_04.md", "chapter_05.md", "chapter_06.md", "chapter_07.md"]

scenes = []
scene_id = 1

for ch in chapters:
    path = os.path.join("/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/nghich-ly-gia-xang-viet-nam/", ch)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Remove disclaimer or extra lines if present, just working with prose
    text = text.replace("\n", " ")
    
    # Simple sentence split
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Group by 2 sentences per scene on average
    group = []
    for s in sentences:
        group.append(s)
        if len(group) == 2 or s == sentences[-1]:
            words = sum(len(x.split()) for x in group)
            duration = int(round((words / 215.0) * 60))
            if duration < 3: duration = 3
            
            scenes.append({
                "id": f"SC{(scene_id):03d}",
                "text": " ".join(group),
                "sentence_count": len(group),
                "duration_sec": duration,
                "visual_summary": "",
                "word_count": words
            })
            scene_id +=1
            group = []

# Verify duration
total_duration = sum(s["duration_sec"] for s in scenes)
total_words = sum(s["word_count"] for s in scenes)

dump = {
    "total_words": total_words,
    "total_duration_sec": total_duration,
    "total_expected_duration_sec": int((total_words/215) * 60),
    "total_scenes": len(scenes),
    "scenes": scenes
}

with open("/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/nghich-ly-gia-xang-viet-nam/scene_raw_split.json", "w", encoding="utf-8") as f:
    json.dump(dump, f, indent=2, ensure_ascii=False)
