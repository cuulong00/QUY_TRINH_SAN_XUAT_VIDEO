import json
import os

with open('episodes/the-petrodollar-paradox/scene_timing_map.json', 'r') as f:
    all_scenes = json.load(f)

# Helper to get scenes for chapter
def get_chapter_scenes(ch_num):
    return [s for s in all_scenes if s.get('chapter') == ch_num]

print("Loaded scenes successfully")
