import os
import re

prompts_file = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/so-sanh-dong-co-vinfast-tesla-byd/prompts_master.txt"
video_dir = "/Users/pro16/Downloads/so-sanh-dong-co"
output_file = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/so-sanh-dong-co-vinfast-tesla-byd/missing_prompts.txt"

# 1. Get all scene IDs from prompts_master.txt
with open(prompts_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract scene IDs. Looking for lines like "CHxx_SCyyy [IMAGE]" or "[VIDEO]"
# Actually, just looking for lines that start with CHxx_SCyyy
scene_ids = []
for line in lines:
    match = re.match(r'^(CH\d{2}_SC\d{3})', line)
    if match:
        scene_id = match.group(1)
        if scene_id not in scene_ids:
            scene_ids.append(scene_id)

print(f"Found {len(scene_ids)} unique scene IDs in prompts_master.txt")

# 2. Get list of generated videos
# Videos are usually named something like CH01_SC001.mp4 or similar.
generated_scene_ids = set()
if os.path.exists(video_dir):
    for filename in os.listdir(video_dir):
        # Find scene ID in the filename
        match = re.search(r'(CH\d{2}_SC\d{3})', filename)
        if match:
            generated_scene_ids.add(match.group(1))
else:
    print(f"Directory {video_dir} does not exist!")

print(f"Found {len(generated_scene_ids)} generated videos in {video_dir}")

# 3. Find missing scenes
missing_scenes = sorted([sid for sid in scene_ids if sid not in generated_scene_ids])

print(f"Missing {len(missing_scenes)} scenes.")

# 4. Extract prompts for missing scenes
missing_prompts = []
for sid in missing_scenes:
    # Find the [IMAGE] and [VIDEO] lines for this scene
    for line in lines:
        if line.startswith(f"{sid} [IMAGE]") or line.startswith(f"{sid} [VIDEO]"):
            missing_prompts.append(line)

# 5. Write to output file
if missing_prompts:
    with open(output_file, 'w', encoding='utf-8') as f:
        # Add a blank line between each prompt line for readability, similar to master
        for p in missing_prompts:
            f.write(p)
            f.write("\n")
    print(f"Wrote missing prompts to {output_file}")
else:
    print("No missing prompts!")
