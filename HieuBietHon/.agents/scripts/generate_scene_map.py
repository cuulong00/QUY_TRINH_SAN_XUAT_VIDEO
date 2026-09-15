import json
import os
import re
import argparse

WPS = 3.81
MAX_SCENE_DUR = 7.0

def clean_sentence(s):
    return s.strip()

def split_sentence_by_duration(s, wps):
    words = s.split()
    n = len(words)
    dur = n / wps
    if dur <= MAX_SCENE_DUR:
        return [(s, dur)]
    
    # Try splitting at comma, colon, semicolon, or dash
    commas = [m.start() for m in re.finditer(r'[,:;\-]', s)]
    if commas:
        mid = len(s) / 2
        best_comma = min(commas, key=lambda x: abs(x - mid))
        part1 = s[:best_comma].strip()
        part2 = s[best_comma+1:].strip()
        if part1 and part2:
            return split_sentence_by_duration(part1, wps) + split_sentence_by_duration(part2, wps)
            
    # Fallback: split by word count
    mid_word = n // 2
    part1 = ' '.join(words[:mid_word])
    part2 = ' '.join(words[mid_word:])
    return split_sentence_by_duration(part1, wps) + split_sentence_by_duration(part2, wps)


def process_episode(episode_dir):
    scenes = []
    scene_id = 1
    total_words = 0
    chapters_found = False
    for i in range(1, 6):  # Check chapters 1 to 5 only
        visual_filepath = os.path.join(episode_dir, f'chapter_{i:02d}_visual.md')
        orig_filepath = os.path.join(episode_dir, f'chapter_{i:02d}.md')
        if os.path.exists(visual_filepath):
            filepath = visual_filepath
            chapters_found = True
        elif os.path.exists(orig_filepath):
            filepath = orig_filepath
            chapters_found = True
        else:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
                
            # Count words
            lines = [line.strip() for line in content.split('\n') if line.strip() and not line.strip().startswith('#')]
            clean_text = ' '.join(lines)
            words = len(clean_text.split())
            total_words += words
            
            lines = [line.strip() for line in content.split('\n') if line.strip() and not line.strip().startswith('#')]
            for line in lines:
                m = re.match(r'^(SC\d+)\s*(?:\[TEXT OVERLAY:\s*"([^"]+)"\])?\s*:\s*(.*)$', line)
                if m:
                    sc_id, overlay, spoken = m.groups()
                    words_list = spoken.split()
                    n_words = len(words_list)
                    dur = round(n_words / WPS, 2)
                    scenes.append({
                        "id": sc_id,
                        "chapter": f"{i:02d}",
                        "sentence_count": 1,
                        "duration_sec": dur,
                        "text_overlay": overlay if overlay else "",
                        "visual_summary": spoken,
                        "sentences": [spoken],
                        "base_english_prompt": "A cinematic realistic documentary shot"
                    })
                else:
                    words_list = line.split()
                    n_words = len(words_list)
                    dur = round(n_words / WPS, 2)
                    scenes.append({
                        "id": f"SC{scene_id:03d}",
                        "chapter": f"{i:02d}",
                        "sentence_count": 1,
                        "duration_sec": dur,
                        "text_overlay": "",
                        "visual_summary": line,
                        "sentences": [line],
                        "base_english_prompt": "A cinematic realistic documentary shot"
                    })
                scene_id += 1



    if not chapters_found:
        print(f"Error: No chapter files found in {episode_dir}")
        return

    total_duration = float(sum(s.get('duration_sec', 0) for s in scenes))
    estimated_vo_duration = float((total_words / WPS))

    print("=" * 50)
    print("SCENE EXTRACTION REPORT (OPTIMAL SCENE-GROUPING)")
    print("=" * 50)
    print(f"Total Words Extracted: {total_words}")
    print(f"Est. Voiceover Duration: {estimated_vo_duration:.2f} seconds")
    print(f"Total Scenes Generated:  {len(scenes)}")
    print(f"Total Scene Duration:    {total_duration:.2f} seconds")
    print("=" * 50)
    
    # Verify durations
    exceeding = [s["id"] for s in scenes if s["duration_sec"] > MAX_SCENE_DUR]
    if exceeding:
        print(f"❌ CRITICAL WARNING: {len(exceeding)} scenes exceed max duration of {MAX_SCENE_DUR}s: {exceeding}")
    else:
        print("✅ SUCCESS: Visual duration covers voiceover safely. 100% of scenes are <= 7.0s.")

    out_path = os.path.join(episode_dir, 'scene_timing_map.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(scenes, f, indent=2, ensure_ascii=False)
    print(f"Saved strictly parsed scene map to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optimal Duration-Bounded Scene Timing Extractor.')
    parser.add_argument('episode_dir', type=str, help='Absolute path to the episode directory')
    args = parser.parse_args()
    
    process_episode(args.episode_dir)
