# -*- coding: utf-8 -*-
from builder_ch01 import ch01_data

# Keep text overlay ONLY for 10 key milestones (exactly 25% of 40 scenes)
KEY_OVERLAYS = {
    "SC002": "THUẾ QUAN 70% - 100%",
    "SC006": "CAM KẾT 500 TRIỆU USD",
    "SC007": "ƯU ĐÃI THUẾ: 15%",
    "SC010": "TRUY THU THUẾ TOÀN BỘ",
    "SC012": "THOOTHUKUDI: 50.000 XE/NĂM",
    "SC020": "LINH KIỆN CKD CÁT HẢI",
    "SC023": "300+ XƯỞNG CƠ KHÍ BẢN ĐỊA",
    "SC030": "TẠM DỪNG NỘI ĐỊA HÓA",
    "SC037": "TOP 4 THỊ PHẦN (8/2026)",
    "SC040": "BÀI TOÁN KHẤU HAO KHUÔN DẬP"
}

for sc_id, d in ch01_data.items():
    if sc_id in KEY_OVERLAYS:
        d['overlay'] = KEY_OVERLAYS[sc_id]
        # Keep text overlay in prompt
    else:
        d['overlay'] = ""
        # Remove text overlay from image prompt and make camera move dynamic
        img = d['image']
        # Clean text overlay mention
        if 'text overlay' in img:
            import re
            img = re.sub(r',?\s*glowing [^,]+ text overlay [^,]+ reading "[^"]+"', '', img)
            img = re.sub(r',?\s*glowing [^,]+ text overlay [^,]+ facing camera directly', '', img)
            d['image'] = img
        # If camera was steady, make it a dynamic cinematic move
        if 'Steady camera shot' in d['motion']:
            d['motion'] = "Slow cinematic tracking shot across the industrial scene"
            d['video'] = f"@{sc_id}.png -> {d['motion']}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"

import json, os
EPISODE_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc'
map_path = os.path.join(EPISODE_DIR, 'scene_timing_map.json')

with open(map_path, 'r', encoding='utf-8') as f:
    scenes = json.load(f)

prompt_lines = []
for s in scenes:
    if s['chapter'] == '01':
        sc_id = s['id']
        d = ch01_data[sc_id]
        s['visual_summary'] = d['summary']
        s['text_overlay'] = d['overlay']
        s['camera_motion'] = d['motion']
        s['image_prompt'] = d['image']
        s['video_prompt'] = f"@{sc_id}.png -> {d['motion']}, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9"
        prompt_lines.append(f"{sc_id} [IMAGE]: {s['image_prompt']}")
        prompt_lines.append(f"{sc_id} [VIDEO]: {s['video_prompt']}\n")

with open(map_path, 'w', encoding='utf-8') as f:
    json.dump(scenes, f, ensure_ascii=False, indent=2)

out_txt = os.path.join(EPISODE_DIR, 'prompts_chapter_01.txt')
with open(out_txt, 'w', encoding='utf-8') as f:
    f.write('\n'.join(prompt_lines))

print("Refined Chapter 01 overlays.")
