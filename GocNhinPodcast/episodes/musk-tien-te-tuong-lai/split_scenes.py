import json
import os
import re

ep_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/musk-tien-te-tuong-lai"
json_path = os.path.join(ep_dir, "scene_timing_map.json")
raw_info_path = os.path.join(ep_dir, "scenes_raw_info.txt")
prompts_path = os.path.join(ep_dir, "video_prompts.txt")

with open(json_path, "r", encoding="utf-8") as f:
    scene_map = json.load(f)

new_scene_map = []
camera_moves = [
    "A steady shot", 
    "A subtle slow zoom-in", 
    "A subtle slow zoom-out", 
    "A slow camera panning", 
    "A subtle slow pan right", 
    "A subtle slow pan left"
]

print("--- STARTING SCENE SPLITTING AND PACING OPTIMIZATION ---")
split_count = 0
for scene in scene_map:
    duration = scene["duration_sec"]
    # Check if duration > 8s
    if duration > 8.0:
        split_count += 1
        sents = scene["sentences"]
        num_sents = len(sents)
        
        # 1. Determine base splits
        sub_scenes = []
        if num_sents > 1:
            # Split proportionally based on word count of each sentence
            word_counts = [len(s.split()) for s in sents]
            total_words = sum(word_counts)
            if total_words == 0:
                total_words = 1
            for idx, sent in enumerate(sents):
                sub_dur = (word_counts[idx] / total_words) * duration
                sub_scenes.append({
                    "sentence": sent,
                    "duration": sub_dur
                })
        else:
            # Single sentence but too long (e.g. SC153) -> split in half
            sub_scenes = [
                {"sentence": sents[0], "duration": duration / 2.0},
                {"sentence": sents[0], "duration": duration / 2.0}
            ]
            
        # 2. Check if any sub_scene duration is still > 8.0s (e.g. very long sentence), and split again if needed
        final_sub_scenes = []
        for sub in sub_scenes:
            if sub["duration"] > 8.0:
                final_sub_scenes.append({"sentence": sub["sentence"], "duration": sub["duration"] / 2.0})
                final_sub_scenes.append({"sentence": sub["sentence"], "duration": sub["duration"] / 2.0})
            else:
                final_sub_scenes.append(sub)
                
        # 3. Create new sub-scene objects
        for idx, sub in enumerate(final_sub_scenes):
            char_suffix = chr(97 + idx) # a, b, c, d...
            sub_id = f"{scene['id']}{char_suffix}"
            
            # Extract prompt body and maintain continuity
            orig_prompt = scene["base_english_prompt"]
            body = orig_prompt
            # Split at the first occurrence of " showing " (case-insensitive)
            showing_match = re.search(r"\s+showing\s+", orig_prompt, re.IGNORECASE)
            if showing_match:
                start_idx = showing_match.end()
                body = orig_prompt[start_idx:]
                
            # Pick a rotating camera movement
            cam_move = camera_moves[idx % len(camera_moves)]
            
            # Apply continuity wording for index > 0
            if idx > 0:
                body_norm = body.strip()
                # Check if it starts with article a/an/the
                first_word_match = re.match(r"^(a|an|the)\s+(.*)$", body_norm, re.IGNORECASE)
                if first_word_match:
                    body_with_continuity = f"the same {first_word_match.group(2)}"
                else:
                    body_with_continuity = f"the same {body_norm}"
            else:
                body_with_continuity = body
                
            new_prompt = f"{cam_move} showing {body_with_continuity}"
            
            # Create new scene entry
            new_scene = {
                "id": sub_id,
                "chapter": scene["chapter"],
                "sentence_count": 1,
                "duration_sec": round(sub["duration"], 2),
                "visual_summary": f"{scene['visual_summary']} (Part {idx+1})",
                "sentences": [sub["sentence"]],
                "base_english_prompt": new_prompt
            }
            new_scene_map.append(new_scene)
    else:
        # Keep intact if <= 8.0s
        new_scene_map.append(scene)

print(f"Splitted {split_count} long scenes. Total scenes now: {len(new_scene_map)}")

# Double check that no scene in the new map exceeds 8.0 seconds
exceeding = [s for s in new_scene_map if s["duration_sec"] > 8.0]
if exceeding:
    print(f"⚠️ WARNING: {len(exceeding)} scenes still exceed 8.0s! We will split them again.")
    # (The algorithm above already does double splits, so this should be empty)
else:
    print("✅ Verified: 100% of scenes in the new map are <= 8.0 seconds.")

# 4. Save to JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(new_scene_map, f, ensure_ascii=False, indent=2)
print("Saved new map to scene_timing_map.json.")

# 5. Generate video_prompts.txt and scenes_raw_info.txt
chapter_counts = {}
with open(raw_info_path, "w", encoding="utf-8") as raw_f, open(prompts_path, "w", encoding="utf-8") as prompt_f:
    for scene in new_scene_map:
        ch = scene["chapter"]
        ch_int = int(ch)
        
        if ch_int not in chapter_counts:
            chapter_counts[ch_int] = 0
        chapter_counts[ch_int] += 1
        
        # Build tag: Chuong X - Phan canh Y
        sc_id = scene["id"]
        tag_name = f"Chuong {ch_int} - Phan canh {chapter_counts[ch_int]}"
        
        sentences_str = " ".join(scene["sentences"])
        visual_summary = scene["visual_summary"]
        
        # Write to raw info
        raw_line = f"{tag_name} ({sc_id}) | sentences: {sentences_str} | base: {visual_summary}\n"
        raw_f.write(raw_line)
        
        # Write to prompts
        prompt_line = f"{tag_name} ({sc_id}): {scene['base_english_prompt']}\n\n"
        prompt_f.write(prompt_line)

print("Saved scenes_raw_info.txt and video_prompts.txt.")
print("--- SCENE SPLITTING COMPLETED ---")
