#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
from collections import Counter

def analyze_prompts(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' does not exist.")
        return False, {}

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print(f"❌ Error: File '{file_path}' is empty.")
        return False, {}

    total_lines = len(lines)
    print(f"📊 Analyzing {total_lines} lines in {os.path.basename(file_path)}...")

    descriptions = []
    ids = []
    transition_errors = []
    id_rendering_errors = []
    mapping_errors = []
    
    images_seen = set()
    videos_seen = set()

    for line in lines:
        # Match ID prefix: CHXX_SCYYY [IMAGE]: or CHXX_SCYYY [VIDEO]: or old CHXX_SCYYY:
        match_id = re.match(r'^([A-Za-z0-9_]+)\s*(?:\[(IMAGE|VIDEO)\])?\s*:\s*(.*)', line)
        if not match_id:
            id_rendering_errors.append(("UNKNOWN", f"Line does not follow standard ID prefix format: '{line}'"))
            continue

        current_id = match_id.group(1)
        mode = match_id.group(2) # "IMAGE" or "VIDEO" or None
        remaining_content = match_id.group(3).strip()
        
        full_key = f"{current_id}_{mode}" if mode else current_id
        ids.append(full_key)

        if mode == "IMAGE":
            images_seen.add(current_id)
        elif mode == "VIDEO":
            videos_seen.add(current_id)

        # Clean I2V reference mapping from description
        desc_clean = remaining_content
        
        # Check simplified syntax: @CHXX_SCYYY.png -> or @reference_images/CHXX_SCYYY.png ->
        match_i2v = re.match(r'^@(?:reference_images/)?([^ \t->\n]+)\s*->\s*(.*)', remaining_content, re.IGNORECASE)
        if match_i2v:
            img_filename = match_i2v.group(1).strip()
            desc_clean = match_i2v.group(2).strip()
            
            # Check ID matching with reference image filename
            img_id = os.path.splitext(img_filename)[0]
            if img_id != current_id:
                mapping_errors.append((current_id, f"Reference image ID '{img_id}' does not match line ID '{current_id}'!"))

        # Clean camera movements for duplicate check
        desc_dup_check = re.sub(
            r'^(?:Starting with[^,]+,\s*)?(?:Starting from[^,]+,\s*)?(?:slow camera panning right showing|steady shot showing|subtle slow zoom-in showing|steady medium shot showing|the camera pans right showing|camera slowly zooms out|the camera pans down|a slow camera panning showing)\s+',
            '', desc_clean, flags=re.IGNORECASE
        ).strip()
        descriptions.append((full_key, desc_dup_check))

        # Check for raw IDs inside description text (visual text overlays exception)
        raw_id_matches = re.findall(r'\b(?:CH\d+_SC\d+[a-z0-9_]*|SC\d+[a-z0-9_]*)\b', desc_clean, re.IGNORECASE)
        raw_id_matches = [m for m in raw_id_matches if m.lower() != current_id.lower()]
        if raw_id_matches:
            id_rendering_errors.append((current_id, f"Contains raw ID references {raw_id_matches} which will cause video text rendering bugs!"))

        # Check for non-physical meta references
        meta_matches = re.findall(r'\b(?:previous scene|next scene|former scene|cảnh trước|cảnh sau)\b', desc_clean, re.IGNORECASE)
        if meta_matches:
            id_rendering_errors.append((current_id, f"Contains phi-vat-ly meta references {meta_matches} which AI video generator cannot understand!"))

        # Check transition syntax
        if "starting from" in desc_clean.lower() and "previous scene" in desc_clean.lower():
            transition_errors.append((current_id, "Transition should use physical starting syntax 'Starting with a close-up/steady shot of [object]' instead of meta 'Starting from'."))

    # Verify I2V Image and Video pairing
    for img_id in images_seen:
        if img_id not in videos_seen:
            mapping_errors.append((img_id, f"Has IMAGE prompt but is missing corresponding VIDEO prompt."))
    for vid_id in videos_seen:
        if vid_id not in images_seen:
            mapping_errors.append((vid_id, f"Has VIDEO prompt but is missing corresponding IMAGE prompt."))

    # Count frequencies of pure descriptions for duplicate check
    desc_only = [item[1] for item in descriptions]
    desc_counter = Counter(desc_only)
    duplicates = {k: v for k, v in desc_counter.items() if v > 1}

    # Check for high-frequency boilerplate substrings in KenhTamLy
    boilerplates = [
        "representing the mind storm",
        "in a dark space representing",
        "glowing digital paths representing",
        "glowing neural networks on a dark background",
        "symbolizing the dual nature"
    ]

    boilerplate_counts = {}
    for bp in boilerplates:
        count = sum(1 for line in lines if bp.lower() in line.lower())
        boilerplate_counts[bp] = (count, round(count / total_lines * 100, 1))

    # Print results
    print("\n--- 🔍 1. EXTREME REPETITION CHECK (Target: <= 2 repetitions/desc) ---")
    severe_duplicates = False
    for desc, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
        matched_keys = [item[0] for item in descriptions if item[1] == desc]
        print(f"⚠️ Repeated {count} times across {matched_keys}:")
        print(f"   \"{desc[:120]}...\"")
        if count > 2:
            severe_duplicates = True

    print("\n--- 🔍 2. BOILERPLATE PHRASE SPAM DETECTION (Target: <= 10% frequency) ---")
    severe_boilerplate = False
    for bp, (count, pct) in boilerplate_counts.items():
        status = "✅ PASS"
        if pct > 10.0:
            status = "❌ FAIL (Over 10% spam limit)"
            severe_boilerplate = True
        print(f"- '{bp}': {count} times ({pct}%) -> {status}")

    print("\n--- 🔍 3. CAMERA CONTINUITY / MATCHED MOVEMENT CHECK ---")
    if transition_errors:
        print(f"⚠️ Found {len(transition_errors)} continuity gaps/errors:")
        for scene_id, err in transition_errors[:10]:
            print(f"  - [{scene_id}]: {err}")
    else:
        print("✅ 100% of transitions have correct match cuts and semantic references!")

    print("\n--- 🔍 4. ID RENDERING RISK CHECK (Text Overlay Detection) ---")
    if id_rendering_errors:
        print(f"❌ Found {len(id_rendering_errors)} prompts with raw ID codes inside description text:")
        for scene_id, err in id_rendering_errors[:10]:
            print(f"  - [{scene_id}]: {err}")
    else:
        print("✅ 100% of prompt descriptions are clean of raw alphanumeric IDs!")

    print("\n--- 🔍 5. I2V ID MAPPING SYNC CHECK ---")
    if mapping_errors:
        print(f"❌ Found {len(mapping_errors)} mapping mismatches between prompt ID and reference image/video sync:")
        for scene_id, err in mapping_errors:
            print(f"  - [{scene_id}]: {err}")
    else:
        print("✅ 100% of I2V reference images match prompt IDs perfectly!")

    # Evaluation
    is_valid = True
    print("\n================ FINAL QUALITY REPORT ================")
    if severe_duplicates:
        print("❌ FAILED: Found severe duplicate scene descriptions (repeated > 2 times).")
        is_valid = False
    if severe_boilerplate:
        print("❌ FAILED: Boilerplate spam exceeds the 10% limit.")
        is_valid = False
    if id_rendering_errors:
        print("❌ FAILED: Found raw IDs inside description text. These will cause visual rendering bugs on screen!")
        is_valid = False
    if mapping_errors:
        print("❌ FAILED: Prompt IDs and Reference Image/Video pairing mismatches found.")
        is_valid = False
    
    if is_valid:
        print("🎉 SUCCESS: The prompt file meets all S-Grade quality thresholds!")
    else:
        print("⚠️ ACTION REQUIRED: Re-generate or edit repetitive prompts.")
        
    return is_valid, {
        "duplicates_count": len(duplicates),
        "severe_duplicates": severe_duplicates,
        "severe_boilerplate": severe_boilerplate,
        "transition_errors_count": len(transition_errors),
        "id_rendering_errors_count": len(id_rendering_errors),
        "mapping_errors_count": len(mapping_errors)
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_boilerplate.py <path_to_prompts_chXX.txt>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    success, stats = analyze_prompts(file_path)
    if not success:
        sys.exit(1)
    sys.exit(0)
