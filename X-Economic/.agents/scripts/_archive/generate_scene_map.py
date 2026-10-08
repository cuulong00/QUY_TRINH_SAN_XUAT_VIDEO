import json
import os
import re
import argparse

def generate_english_base_summary(text):
    text_lower = text.lower()
    
    # Very basic universal mapping to ensure Grok/Midjourney can render something 
    # even without sophisticated AI translation, to prevent empty fields.
    if "xe" in text_lower or "điện" in text_lower or "đường" in text_lower:
        desc = "A high-tech electric vehicle driving on a modern futuristic highway"
    elif "nợ" in text_lower or "lỗ" in text_lower or "phá sản" in text_lower or "đỏ" in text_lower:
        desc = "A dramatic red downward financial chart plunging into a dark void with glowing numbers"
    elif "nhà" in text_lower or "bất động sản" in text_lower or "căn hộ" in text_lower:
        desc = "Ghost city of empty unfinished apartment buildings towering in dark shadows"
    elif "chính quyền" in text_lower or "chính sách" in text_lower or "nhà nước" in text_lower:
        desc = "A giant glowing golden protective hand saving a modern city from destruction"
    elif "tiền" in text_lower or "việc làm" in text_lower or "nhân viên" in text_lower:
        desc = "An ordinary worker looking stressed as glowing data numbers evaporate from their wallet"
    else:
        desc = "A dramatic cinematic macro-economic visualization, dark conceptual art"
    
    return desc

def process_episode(episode_dir):
    scenes = []
    scene_id = 1
    total_words = 0
    chapters_found = False

    for i in range(1, 20):  # Check up to chapter 19
        filepath = os.path.join(episode_dir, f'chapter_{i:02d}.md')
        if os.path.exists(filepath):
            chapters_found = True
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                words = len(content.split())
                total_words += words
                
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.startswith('#')]
                
                # Rule 1: Hook gets 1 sentence = 1 scene
                if i == 1:
                    for p in paragraphs:
                        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', p) if s.strip()]
                        for s in sentences:
                            if len(s) > 10:
                                scenes.append({
                                    "id": f"SC{scene_id:03d}",
                                    "chapter": f"0{i}",
                                    "sentence_count": 1,
                                    "duration_sec": 5,
                                    "visual_summary": "",
                                    "sentences": [s],
                                    "base_english_prompt": generate_english_base_summary(s)
                                })
                                scene_id += 1
                # Rule 2: Body chapters get 2-3 sentences per scene, duration based on word count
                else:
                    for p in paragraphs:
                        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', p) if len(s.strip()) > 10]
                        # group sentences into chunks of 3
                        chunks = [sentences[i:i + 3] for i in range(0, len(sentences), 3)]
                        for chunk in chunks:
                            if not chunk: continue
                            combined_s = " ".join(chunk)
                            word_count = len(combined_s.split())
                            duration = max(5, int((word_count / 215) * 60) + 2) # Add 2 sec padding
                            scenes.append({
                                "id": f"SC{scene_id:03d}",
                                "chapter": f"0{i}",
                                "sentence_count": len(chunk),
                                "duration_sec": duration,
                                "visual_summary": "",
                                "sentences": chunk,
                                "base_english_prompt": generate_english_base_summary(combined_s)
                            })
                            scene_id += 1

    if not chapters_found:
        print(f"Error: No chapter files found in {episode_dir}")
        return

    total_duration = float(sum(int(s.get('duration_sec', 0)) for s in scenes))
    estimated_vo_duration = float((total_words / 215) * 60)

    print("=" * 50)
    print("SCENE EXTRACTION REPORT")
    print("=" * 50)
    print(f"Total Words Extracted: {total_words}")
    print(f"Est. Voiceover Duration: {estimated_vo_duration:.0f} seconds")
    print(f"Total Scenes Generated:  {len(scenes)}")
    print(f"Total Scene Duration:    {total_duration:.0f} seconds")
    print("=" * 50)
    
    if total_duration < estimated_vo_duration:
        print("❌ CRITICAL WARNING: Visual duration is shorter than voiceover!")
    else:
        print("✅ SUCCESS: Visual duration covers voiceover safely.")

    out_path = os.path.join(episode_dir, 'scene_timing_map.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(scenes, f, indent=2, ensure_ascii=False)
    print(f"Saved strictly parsed scene map to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Strict Scene Timing Extractor to prevent LLM bypass.')
    parser.add_argument('episode_dir', type=str, help='Absolute path to the episode directory')
    args = parser.parse_args()
    
    process_episode(args.episode_dir)
