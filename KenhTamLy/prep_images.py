import json, glob, shutil, os
src = "/Users/pro16/Downloads/dopamin-ngaquy"
dest = "/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/ma-tuy-so/images_final"
scene_map = "/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/ma-tuy-so/scene_timing_map.json"
os.makedirs(dest, exist_ok=True)
with open(scene_map, 'r') as f:
    scenes = json.load(f)
shutil.copy(scene_map, "/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/ma-tuy-so/scene_map.json")
missing = 0
for i, sc in enumerate(scenes):
    id = sc['id'] # e.g. "SC001"
    matches = glob.glob(f"{src}/*_{id}_*")
    if matches:
        ext = matches[0].split('.')[-1]
        shutil.copy(matches[0], f"{dest}/img_{i:03d}.{ext}")
    else:
        print(f"Missing {id}")
        missing += 1
print(f"Copied {len(scenes) - missing} files, missing: {missing}")
