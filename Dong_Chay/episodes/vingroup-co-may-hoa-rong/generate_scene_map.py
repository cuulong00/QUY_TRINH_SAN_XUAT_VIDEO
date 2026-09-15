import json
import re
import os
import glob

episode_dir = "."
chapter_files = sorted(glob.glob(os.path.join(episode_dir, "chapter_*.md")))

scenes = []
scene_counter = 1

for file in chapter_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Strip headers/metadata
    lines = text.split('\n')
    content_lines = []
    in_header = False
    for line in lines:
        if line.startswith('---'):
            in_header = not in_header
            continue
        if not in_header and not line.startswith('#') and line.strip() != '':
            if not line.startswith('**Dấu vân tay:**') and not line.startswith('**Target:**') and not line.startswith('**LỆNH CỨNG:**'):
                content_lines.append(line)
    
    text = " ".join(content_lines)
    
    # Custom split
    sentences = []
    for s in re.split(r'(?<=[.!?—])\s+', text):
        s = s.strip()
        if s: sentences.append(s)
    
    current_scene_sentences = []
    
    for s in sentences:
        current_scene_sentences.append(s)
        
        # Rule: Hook (chapter 1, first 3 sentences) -> 1 sentence per scene
        is_hook = ("chapter_01" in file and scene_counter <= 3)
        max_sentences = 1 if is_hook else 2
        
        if len(current_scene_sentences) >= max_sentences:
            scene_id = f"SC{scene_counter:03d}"
            # Extract a summary for visual prompt logic
            sample_text = " ".join(current_scene_sentences)
            summary = "A dramatic corporate/economic visual representing: " + sample_text[:100] + "..."
            
            scenes.append({
                "id": scene_id,
                "sentence_count": len(current_scene_sentences),
                "duration_sec": len(current_scene_sentences) * 5,
                "visual_summary": summary
            })
            scene_counter += 1
            current_scene_sentences = []

    if current_scene_sentences:
        scene_id = f"SC{scene_counter:03d}"
        sample_text = " ".join(current_scene_sentences)
        summary = "A dramatic corporate/economic visual representing: " + sample_text[:100] + "..."
        scenes.append({
            "id": scene_id,
            "sentence_count": len(current_scene_sentences),
            "duration_sec": len(current_scene_sentences) * 5,
            "visual_summary": summary
        })
        scene_counter += 1

with open("scene_timing_map.json", 'w', encoding='utf-8') as f:
    json.dump(scenes, f, indent=4, ensure_ascii=False)

print(f"Generated {len(scenes)} scenes in scene_timing_map.json")
