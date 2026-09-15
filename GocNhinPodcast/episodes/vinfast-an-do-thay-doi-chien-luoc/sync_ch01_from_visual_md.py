# -*- coding: utf-8 -*-
import json
import os
import re

EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
visual_md_path = os.path.join(EPISODE_DIR, 'chapter_01_visual.md')
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')

with open(visual_md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse Markdown table rows
rows = [line.strip() for line in content.split('\n') if line.startswith('| **SC')]

parsed_scenes = {}
for r in rows:
    parts = [p.strip() for p in r.split('|')[1:-1]]
    sc_id = re.search(r'\*\*(SC\d+)\*\*', parts[0]).group(1)
    
    # Parse duration and text
    m_dur = re.search(r'`([\d\.]+)s`', parts[1])
    dur = float(m_dur.group(1)) if m_dur else 4.0
    m_txt = re.search(r'\*\"(.*)\"\*', parts[1])
    text = m_txt.group(1) if m_txt else ""
    
    # Parse tiers
    t1_match = re.search(r'\*\*Tầng 1 \(Đế cố định\):\*\*\s*(.*?)<br/>', parts[2])
    t2_match = re.search(r'\*\*Tầng 2 \(Bộ truyền động/Chủ thể\):\*\*\s*(.*?)<br/>', parts[2])
    t3_match = re.search(r'\*\*Tầng 3 \(Khối tác động & Góc máy\):\*\*\s*(.*)$', parts[2])
    
    t1 = t1_match.group(1) if t1_match else ""
    t2 = t2_match.group(1) if t2_match else ""
    t3 = t3_match.group(1) if t3_match else ""
    
    # Parse overlay
    raw_overlay = parts[3].replace('**', '').strip()
    overlay = "" if raw_overlay == "Không" else raw_overlay.replace('"', '').strip()
    
    parsed_scenes[sc_id] = {
        "id": sc_id,
        "duration_sec": dur,
        "text": text,
        "summary": f"{t1} {t2} {t3}",
        "overlay": overlay,
        "t1": t1,
        "t2": t2,
        "t3": t3
    }

print(f"Parsed {len(parsed_scenes)} scenes from chapter_01_visual.md")

# Load existing scene_timing_map.json
with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

# Update Chapter 01
prompt_lines = []
for s in scenes:
    if s['chapter'] == '01':
        sc_id = s['id']
        ps = parsed_scenes[sc_id]
        
        s['visual_summary'] = ps['summary']
        s['text_overlay'] = ps['overlay']
        
        # Build English Image Prompt
        # Front-load: A 2D cinematic editorial noir illustration of...
        overlay_prompt = ""
        if ps['overlay']:
            overlay_prompt = f', glowing terracotta orange 3D text overlay facing camera directly with heavy black drop shadow reading "{ps["overlay"]}"'
            camera_motion = "Steady camera shot focusing on the subject and bold straight text overlay"
        else:
            # Dynamic camera motion based on t3
            if "push-in" in ps['t3'].lower():
                camera_motion = "Slow dramatic push-in shot toward the central focal point"
            elif "tracking" in ps['t3'].lower() or "pan" in ps['t3'].lower():
                camera_motion = "Slow cinematic horizontal tracking pan across the industrial setting"
            elif "zoom" in ps['t3'].lower():
                camera_motion = "Slow subtle zoom-in on the critical component"
            elif "tilt" in ps['t3'].lower():
                camera_motion = "Slow upward tilt revealing the towering industrial structure"
            else:
                camera_motion = "Slow smooth camera glide through the shadowy factory bay"
        
        # Craft English prompt from t1 and t2
        img_prompt = f"A 2D cinematic editorial noir illustration of {ps['t2'].rstrip('.')}, set in {ps['t1'].rstrip('.')}, minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, dark warm charcoal background (#1A1A1A), dramatic chiaroscuro lighting, deep noir shadows{overlay_prompt}."
        
        vid_prompt = f"@{sc_id}.png -> {camera_motion}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"
        
        s['camera_motion'] = camera_motion
        s['image_prompt'] = img_prompt
        s['video_prompt'] = vid_prompt
        
        prompt_lines.append(f"{sc_id} [IMAGE]: {img_prompt}")
        prompt_lines.append(f"{sc_id} [VIDEO]: {vid_prompt}\n")

# Save updated scene_timing_map.json
with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

# Write prompts_chapter_01.txt
out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')
with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print(f"Successfully synced scene_timing_map.json and prompts_chapter_01.txt from chapter_01_visual.md!")
