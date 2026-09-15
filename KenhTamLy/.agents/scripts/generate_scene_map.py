#!/usr/bin/env python3
import sys
import os
import re
import json

def clean_text(text):
    text = re.sub(r"\[CẢNH QUAY:.*?\]", "", text)
    text = re.sub(r"\[CẢNH:.*?\]", "", text)
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"#{1,3}\s+.*", "", text)
    text = text.strip()
    return text

def split_sentences(text):
    text = clean_text(text)
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    return sents

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_scene_map.py <episode_dir>")
        sys.exit(1)
    
    episode_dir = sys.argv[1]
    
    scenes = []
    
    for ch_num in range(1, 8):
        ch_file = os.path.join(episode_dir, f"chapter_{ch_num:02d}.md")
        if not os.path.exists(ch_file):
            continue
        
        with open(ch_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        sents = split_sentences(content)
        scene_counter = 10
        
        if ch_num == 1:
            for s in sents:
                w_count = count_words(s)
                if w_count == 0:
                    continue
                if w_count > 26:
                    words = s.split()
                    sub_groups = []
                    current_sub = []
                    current_sub_count = 0
                    for w in words:
                        current_sub.append(w)
                        current_sub_count += 1
                        if current_sub_count >= 20:
                            sub_groups.append(" ".join(current_sub))
                            current_sub = []
                            current_sub_count = 0
                    if current_sub:
                        sub_groups.append(" ".join(current_sub))
                    
                    for sub_idx, sub_s in enumerate(sub_groups):
                        sub_w_count = count_words(sub_s)
                        suffix = chr(97 + sub_idx)  # 'a', 'b', 'c'...
                        scenes.append({
                            "id": f"CH{ch_num:02d}_SC{scene_counter:03d}{suffix}",
                            "sentence_count": 1,
                            "duration_sec": round(sub_w_count / 3.81, 2),
                            "visual_summary": f"Mô tả phân cảnh phụ {suffix.upper()}",
                            "sentences": [sub_s],
                            "base_english_prompt": ""
                        })
                    scene_counter += 10
                else:
                    scenes.append({
                        "id": f"CH{ch_num:02d}_SC{scene_counter:03d}",
                        "sentence_count": 1,
                        "duration_sec": round(w_count / 3.81, 2),
                        "visual_summary": "Mô tả phân cảnh",
                        "sentences": [s],
                        "base_english_prompt": ""
                    })
                    scene_counter += 10
        else:
            current_group = []
            current_word_count = 0
            for s in sents:
                w_count = count_words(s)
                if w_count == 0:
                    continue
                
                if w_count > 26:
                    if current_group:
                        scenes.append({
                            "id": f"CH{ch_num:02d}_SC{scene_counter:03d}",
                            "sentence_count": len(current_group),
                            "duration_sec": round(current_word_count / 3.81, 2),
                            "visual_summary": "Mô tả phân cảnh",
                            "sentences": current_group,
                            "base_english_prompt": ""
                        })
                        scene_counter += 10
                        current_group = []
                        current_word_count = 0
                    
                    words = s.split()
                    sub_groups = []
                    current_sub = []
                    current_sub_count = 0
                    for w in words:
                        current_sub.append(w)
                        current_sub_count += 1
                        if current_sub_count >= 20:
                            sub_groups.append(" ".join(current_sub))
                            current_sub = []
                            current_sub_count = 0
                    if current_sub:
                        sub_groups.append(" ".join(current_sub))
                        
                    for sub_idx, sub_s in enumerate(sub_groups):
                        sub_w_count = count_words(sub_s)
                        suffix = chr(97 + sub_idx)  # 'a', 'b'...
                        scenes.append({
                            "id": f"CH{ch_num:02d}_SC{scene_counter:03d}{suffix}",
                            "sentence_count": 1,
                            "duration_sec": round(sub_w_count / 3.81, 2),
                            "visual_summary": f"Mô tả phân cảnh phụ {suffix.upper()}",
                            "sentences": [sub_s],
                            "base_english_prompt": ""
                        })
                    scene_counter += 10
                else:
                    if len(current_group) >= 3 or current_word_count + w_count > 26:
                        scenes.append({
                            "id": f"CH{ch_num:02d}_SC{scene_counter:03d}",
                            "sentence_count": len(current_group),
                            "duration_sec": round(current_word_count / 3.81, 2),
                            "visual_summary": "Mô tả phân cảnh",
                            "sentences": current_group,
                            "base_english_prompt": ""
                        })
                        scene_counter += 10
                        current_group = [s]
                        current_word_count = w_count
                    else:
                        current_group.append(s)
                        current_word_count += w_count
            
            if current_group:
                scenes.append({
                    "id": f"CH{ch_num:02d}_SC{scene_counter:03d}",
                    "sentence_count": len(current_group),
                    "duration_sec": round(current_word_count / 3.81, 2),
                    "visual_summary": "Mô tả phân cảnh",
                    "sentences": current_group,
                    "base_english_prompt": ""
                })
                scene_counter += 10
                
    output_file = os.path.join(episode_dir, "scene_timing_map.json")
    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(scenes, out, indent=2, ensure_ascii=False)
        
    print("✅ SUCCESS")
    print(f"Total scenes generated: {len(scenes)}")

if __name__ == "__main__":
    main()
