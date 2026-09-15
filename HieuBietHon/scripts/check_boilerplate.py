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

    total_prompts = len(lines)
    print(f"📊 Analyzing {total_prompts} prompts in {os.path.basename(file_path)}...")

    descriptions = []
    ids = []
    transition_errors = []
    id_rendering_errors = []
    mapping_errors = []
    
    for line in lines:
        # Match ID prefix: CHXX_SCYYY: or [CHXX_SCYYY]: or [CHXX_SCYYY]
        match_id = re.match(r'^(?:\[?([A-Za-z0-9_]+)\]?:?)\s*(.*)', line)
        if not match_id:
            id_rendering_errors.append(("UNKNOWN", f"Line does not follow standard ID prefix format: '{line}'"))
            continue

        current_id = match_id.group(1)
        remaining_content = match_id.group(2).strip()
        ids.append(current_id)

        # Clean I2V reference mapping from description
        desc_clean = remaining_content
        match_i2v = re.match(r'^(?:\[reference_images/([^\]]+)\]|@([a-zA-Z0-9_\-\.]+))\s*->\s*(.*)', remaining_content, re.IGNORECASE)
        if match_i2v:
            img_filename = (match_i2v.group(1) or match_i2v.group(2)).strip()
            desc_clean = match_i2v.group(3).strip()
            
            # Check ID matching with reference image filename (e.g. c1-5.png or CH01_SC010.png)
            img_id = os.path.splitext(img_filename)[0]
            if img_id != current_id:
                mapping_errors.append((current_id, f"Reference image ID '{img_id}' does not match line ID '{current_id}'!"))

        # Clean camera movements for duplicate check
        desc_dup_check = re.sub(
            r'^(?:Starting with[^,]+,\s*)?(?:Starting from[^,]+,\s*)?(?:slow camera panning right showing|steady shot showing|subtle slow zoom-in showing|steady medium shot showing|the camera pans right showing|camera slowly zooms out|the camera pans down|a slow camera panning showing)\s+',
            '', desc_clean, flags=re.IGNORECASE
        ).strip()
        descriptions.append((current_id, desc_dup_check))

        # Check for raw IDs inside description text (visual text overlays exception)
        # Avoid matching the prefix ID itself which was stripped.
        # Find raw IDs like CH01_SC010, SC003
        raw_id_matches = re.findall(r'\b(?:CH\d+_SC\d+[a-z0-9_]*|SC\d+[a-z0-9_]*)\b', desc_clean, re.IGNORECASE)
        # Exclude correct on-screen text declarations in quotes like "DEBT" or matching ID strings
        raw_id_matches = [m for m in raw_id_matches if m.lower() != current_id.lower()]
        if raw_id_matches:
            id_rendering_errors.append((current_id, f"Contains raw ID references {raw_id_matches} which will cause video text rendering bugs!"))

        # Check for non-physical meta references
        meta_matches = re.findall(r'\b(?:previous scene|next scene|former scene|cảnh trước|cảnh sau)\b', desc_clean, re.IGNORECASE)
        if meta_matches:
            id_rendering_errors.append((current_id, f"Contains phi-vat-ly meta references {meta_matches} which AI video generator cannot understand!"))

        # Check transition syntax (should start with "Starting with" instead of "Starting from previous scene")
        if "starting from" in desc_clean.lower() and "previous scene" in desc_clean.lower():
            transition_errors.append((current_id, "Transition should use physical starting syntax 'Starting with a close-up/steady shot of [object]' instead of meta 'Starting from'."))

    # Count frequencies of pure descriptions for duplicate check
    desc_only = [item[1] for item in descriptions]
    desc_counter = Counter(desc_only)
    duplicates = {k: v for k, v in desc_counter.items() if v > 1}

    # Check for high-frequency boilerplate substrings
    boilerplates = [
        "representing the shadow financial system",
        "in a dark space representing",
        "glowing digital paths representing",
        "transaction flows on a dark grid",
        "massive brick bank vault door"
    ]

    boilerplate_counts = {}
    for bp in boilerplates:
        count = sum(1 for line in lines if bp.lower() in line.lower())
        boilerplate_counts[bp] = (count, round(count / total_prompts * 100, 1))

    # Print results
    print("\n--- 🔍 1. EXTREME REPETITION CHECK (Target: <= 2 repetitions/desc) ---")
    severe_duplicates = False
    for desc, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
        matched_ids = [item[0] for item in descriptions if item[1] == desc]
        print(f"⚠️ Repeated {count} times across {matched_ids}:")
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
        print(f"❌ Found {len(mapping_errors)} mapping mismatches between prompt ID and reference image filename:")
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
        print("❌ FAILED: Prompt IDs and Reference Image filenames do not match.")
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
        print("Usage: python3 check_boilerplate.py <path_to_video_prompts.txt>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    success, stats = analyze_prompts(file_path)
    if not success:
        sys.exit(1)
    sys.exit(0)
