# -*- coding: utf-8 -*-
import json
import os
import re

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')
out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')

with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

prompt_lines = []
for s in scenes:
    if s['chapter'] == '01':
        sc_id = s['id']
        overlay = s.get('text_overlay', '')
        
        img = s['image_prompt']
        # Remove old text overlay string if present
        img = re.sub(r', glowing terracotta orange 3D text overlay [^.]+', '', img)
        img = re.sub(r', compact subtle [^.]+', '', img)
        img = img.rstrip('.')
        
        if overlay:
            # User requirement: Chữ nhỏ, góc trái phía dưới, cách bottom 25%
            overlay_str = (
                f', compact and subtle glowing terracotta orange 3D typography text overlay '
                f'positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), '
                f'facing camera directly, horizontal orientation with crisp edges and heavy black drop shadow reading "{overlay}"'
            )
            img = img + overlay_str + '.'
            vid = f"@{sc_id}.png -> Steady camera shot maintaining perfect focus on the lower-left typography and subject, preserving the 2D vector noir graphic novel aesthetic and sharp text, 8-second continuous documentary video --ar 16:9"
        else:
            img = img + '.'
            motion = s.get('camera_motion', 'Slow smooth camera glide through the shadowy factory bay')
            if 'Steady' in motion:
                motion = 'Slow cinematic horizontal tracking pan across the industrial setting'
            vid = f"@{sc_id}.png -> {motion}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"
            
        s['image_prompt'] = img
        s['video_prompt'] = vid
        
        prompt_lines.append(f"{sc_id} [IMAGE]: {img}")
        prompt_lines.append(f"{sc_id} [VIDEO]: {vid}\n")

with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print("Successfully updated Chapter 01 with small typography positioned in lower-left (25% above bottom)!")
