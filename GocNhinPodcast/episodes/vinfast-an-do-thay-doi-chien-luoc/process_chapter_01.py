# -*- coding: utf-8 -*-
import json
import os
from builder_ch01 import ch01_data

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')

with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

# Update Chapter 01 scenes
ch01_count = 0
prompt_lines = []

for s in scenes:
    if s['chapter'] == '01':
        sc_id = s['id']
        if sc_id in ch01_data:
            d = ch01_data[sc_id]
            s['visual_summary'] = d['summary']
            s['text_overlay'] = d['overlay']
            s['camera_motion'] = d['motion']
            s['image_prompt'] = d['image']
            s['video_prompt'] = f"@{sc_id}.png -> {d['motion']}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"
            ch01_count += 1
            
            # Format 2-line prompt for prompts_chapter_01.txt
            prompt_lines.append(f"{sc_id} [IMAGE]: {s['image_prompt']}")
            prompt_lines.append(f"{sc_id} [VIDEO]: {s['video_prompt']}\n")

# Save updated scene_timing_map.json
with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

# Write prompts_chapter_01.txt
out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')
with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print(f"Successfully processed Chapter 01: {ch01_count} scenes enriched and exported to prompts_chapter_01.txt")
