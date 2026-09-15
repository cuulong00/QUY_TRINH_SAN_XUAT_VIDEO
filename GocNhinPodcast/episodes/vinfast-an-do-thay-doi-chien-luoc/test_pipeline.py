import json

with open('/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-an-do-thay-doi-chien-luoc/scene_timing_map.json') as f:
    scenes = json.load(f)

print(f"Total scenes to process: {len(scenes)}")
