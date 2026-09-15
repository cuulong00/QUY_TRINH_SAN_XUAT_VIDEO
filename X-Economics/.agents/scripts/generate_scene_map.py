import json
import os
import re
import argparse

WPS = 2.4 # Standard English documentary narration pace (~144 WPM)
MAX_SCENE_DUR = 7.0 # Hard cap for an 8.0s Veo clip (leaving 1.0s visual buffer)
MAX_WORDS = int(MAX_SCENE_DUR * WPS) # Exactly 16 words max (16 / 2.4 = 6.67s <= 7.0s)

def clean_sentence(s):
    return s.strip()

def split_sentence_by_duration(s, wps):
    words = s.split()
    n = len(words)
    dur = round(n / wps, 2)
    if n <= MAX_WORDS and dur <= MAX_SCENE_DUR:
        return [(s, dur)]
    
    # Try splitting at comma, colon, semicolon, or dash that has at least 4 words on each side
    mid = len(s) / 2
    valid_commas = [m.start() for m in re.finditer(r'[,:;\-–—]', s) 
                    if len(s[:m.start()].split()) >= 4 and len(s[m.start():].split()) >= 4]
    if valid_commas:
        best_comma = min(valid_commas, key=lambda x: abs(x - mid))
        part1 = s[:best_comma].strip()
        part2 = s[best_comma+1:].strip()
        if part1 and part2:
            return split_sentence_by_duration(part1, wps) + split_sentence_by_duration(part2, wps)
            
    # Fallback: split evenly by word count
    mid_word = n // 2
    part1 = ' '.join(words[:mid_word])
    part2 = ' '.join(words[mid_word:])
    return split_sentence_by_duration(part1, wps) + split_sentence_by_duration(part2, wps)

def extract_sentences_from_text(text):
    lines = [line.strip() for line in text.split('\n') if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('---')]
    all_sentences = []
    for line in lines:
        # Avoid splitting inside common abbreviations or decimals like 2.196, 7.2%, v.v.
        # Simple robust regex split on sentence endings (.!?) followed by space
        raw_parts = re.split(r'(?<=[.!?])\s+', line)
        for part in raw_parts:
            p = part.strip()
            if p:
                all_sentences.append(p)
    return all_sentences

def process_episode(episode_dir):
    scenes = []
    total_words = 0
    chapters_found = False
    
    # Check chapters up to 20
    for i in range(1, 21):
        ch_scene_id = 1
        visual_filepath = os.path.join(episode_dir, f'chapter_{i:02d}_visual.md')
        orig_filepath = os.path.join(episode_dir, f'chapter_{i:02d}.md')
        
        filepath = None
        is_visual = False
        if os.path.exists(visual_filepath):
            filepath = visual_filepath
            is_visual = True
            chapters_found = True
        elif os.path.exists(orig_filepath):
            filepath = orig_filepath
            is_visual = False
            chapters_found = True
        else:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if is_visual:
            # Parse existing visual markdown
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            cur_id = None
            cur_overlay = ""
            cur_spoken = ""
            cur_summary = ""
            
            for line in lines:
                # Support markdown table row: | **ID** | (Dur |) Thoại | Bối cảnh | Text overlay | ...
                if line.startswith('|') and '**' in line and not line.strip().startswith('| :'):
                    cols = [c.strip() for c in line.split('|')[1:-1]]
                    m_id = re.search(r'\*\*([A-Za-z0-9_]+)\*\*', cols[0]) if cols else None
                    if m_id:
                        row_id = m_id.group(1)
                        if len(cols) >= 5 and re.match(r'^\d+(\.\d+)?s?$', cols[1]):
                            # 5 or 6 cols: ID, Dur, Spoken, Summary, Overlay, [Flow]
                            row_spoken = cols[2]
                            row_summary = cols[3]
                            row_overlay = cols[4].replace('`', '')
                        elif len(cols) >= 4:
                            row_spoken = cols[1]
                            row_summary = cols[2]
                            row_overlay = cols[3].replace('`', '')
                        else:
                            row_spoken = cols[1]
                            row_summary = cols[1]
                            row_overlay = ""

                        w_list = row_spoken.split()
                        dur = round(len(w_list) / WPS, 2)
                        total_words += len(w_list)
                        tag = row_id if row_id.startswith(f"CH{i:02d}_") else f"CH{i:02d}_SC{ch_scene_id:03d}"
                        scenes.append({
                            "id": tag,
                            "original_tag": row_id,
                            "chapter": f"{i:02d}",
                            "sentence_count": 1,
                            "duration_sec": dur,
                            "text_overlay": row_overlay if row_overlay and row_overlay.lower() != "không" else "",
                            "visual_summary": row_summary if row_summary else row_spoken,
                            "sentences": [row_spoken],
                            "base_english_prompt": "A 2D cinematic editorial noir illustration"
                        })
                        ch_scene_id += 1
                        continue

                m_header = re.match(r'^(?:###\s+|\|\s*\*\*)([A-Za-z0-9_]+)', line)
                m_thoai = re.match(r'^(?:-\s+\*\*\[THOẠI\]:\*\*|`[^`]+`\s*\(.*?\)<br\/>\*"|[^|]*\|\s*`[^`]+`\s*\([^)]+\)<br\/>\*"|\*\*)(.*)$', line)
                m_overlay = re.match(r'^-\s+\*\*\[TEXT OVERLAY\]:\*\*\s*(.*)$', line)
                m_boicanh = re.match(r'^-\s+\*\*\[BỐI CẢNH\]:\*\*\s*(.*)$', line)
                
                if m_header:
                    if cur_spoken:
                        w_list = cur_spoken.split()
                        dur = round(len(w_list) / WPS, 2)
                        total_words += len(w_list)
                        tag = cur_id if cur_id and cur_id.startswith(f"CH{i:02d}_") else f"CH{i:02d}_SC{ch_scene_id:03d}"
                        scenes.append({
                            "id": tag,
                            "original_tag": cur_id,
                            "chapter": f"{i:02d}",
                            "sentence_count": 1,
                            "duration_sec": dur,
                            "text_overlay": cur_overlay if cur_overlay and cur_overlay.lower() != "không" else "",
                            "visual_summary": cur_summary if cur_summary else cur_spoken,
                            "sentences": [cur_spoken],
                            "base_english_prompt": "A 2D cinematic editorial noir illustration"
                        })
                        ch_scene_id += 1
                    cur_id = m_header.group(1)
                    cur_overlay = ""
                    cur_spoken = ""
                    cur_summary = ""
                elif m_thoai:
                    cur_spoken = m_thoai.group(1).strip().replace('"*', '').replace('"', '')
                elif m_overlay:
                    cur_overlay = m_overlay.group(1).strip()
                elif m_boicanh:
                    cur_summary = m_boicanh.group(1).strip()
                    
            if cur_spoken:
                w_list = cur_spoken.split()
                dur = round(len(w_list) / WPS, 2)
                total_words += len(w_list)
                tag = cur_id if cur_id and cur_id.startswith(f"CH{i:02d}_") else f"CH{i:02d}_SC{ch_scene_id:03d}"
                scenes.append({
                    "id": tag,
                    "original_tag": cur_id,
                    "chapter": f"{i:02d}",
                    "sentence_count": 1,
                    "duration_sec": dur,
                    "text_overlay": cur_overlay if cur_overlay and cur_overlay.lower() != "không" else "",
                    "visual_summary": cur_summary if cur_summary else cur_spoken,
                    "sentences": [cur_spoken],
                    "base_english_prompt": "A 2D cinematic editorial noir illustration"
                })
                ch_scene_id += 1
        else:
            # Parse raw chapter text
            sentences = extract_sentences_from_text(content)
            
            # Step 1: ensure every single sentence is <= MAX_WORDS (26 words)
            processed_units = []
            for s in sentences:
                units = split_sentence_by_duration(s, WPS)
                for text_part, dur_part in units:
                    w_count = len(text_part.split())
                    total_words += w_count
                    processed_units.append((text_part, w_count, dur_part))
            
            # Step 2: Grouping
            if i == 1:
                # Chapter 1 (Hook): 1 sentence/unit per scene (do not group)
                for text_part, w_count, dur_part in processed_units:
                    scenes.append({
                        "id": f"CH{i:02d}_SC{ch_scene_id:03d}",
                        "chapter": f"{i:02d}",
                        "sentence_count": 1,
                        "duration_sec": round(dur_part, 2),
                        "text_overlay": "",
                        "visual_summary": text_part,
                        "sentences": [text_part],
                        "base_english_prompt": "A 2D cinematic editorial noir illustration"
                    })
                    ch_scene_id += 1
            else:
                # Chapters 2+: Group consecutive units up to MAX_WORDS (26 words)
                cur_group = []
                cur_words = 0
                
                for text_part, w_count, dur_part in processed_units:
                    if cur_words + w_count <= MAX_WORDS:
                        cur_group.append(text_part)
                        cur_words += w_count
                    else:
                        if cur_group:
                            group_dur = round(cur_words / WPS, 2)
                            scenes.append({
                                "id": f"CH{i:02d}_SC{ch_scene_id:03d}",
                                "chapter": f"{i:02d}",
                                "sentence_count": len(cur_group),
                                "duration_sec": group_dur,
                                "text_overlay": "",
                                "visual_summary": " ".join(cur_group),
                                "sentences": cur_group,
                                "base_english_prompt": "A 2D cinematic editorial noir illustration"
                            })
                            ch_scene_id += 1
                        cur_group = [text_part]
                        cur_words = w_count
                        
                if cur_group:
                    group_dur = round(cur_words / WPS, 2)
                    scenes.append({
                        "id": f"CH{i:02d}_SC{ch_scene_id:03d}",
                        "chapter": f"{i:02d}",
                        "sentence_count": len(cur_group),
                        "duration_sec": group_dur,
                        "text_overlay": "",
                        "visual_summary": " ".join(cur_group),
                        "sentences": cur_group,
                        "base_english_prompt": "A 2D cinematic editorial noir illustration"
                    })
                    ch_scene_id += 1

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

