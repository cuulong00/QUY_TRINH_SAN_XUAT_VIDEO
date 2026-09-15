import os, json, re
from pathlib import Path
from difflib import SequenceMatcher

ep_dir = Path("/Users/pro16/Documents/VideoProject/X-Economics/episodes/byd-vs-toyota-no-america-strategy")
archive_dir = ep_dir / "archive_v1_8chapters"

# Load archive scenes
st_map = json.load(open(archive_dir / "scene_timing_map.json"))
old_scenes_by_ch = {}
for ch in range(1, 9):
    ch_str = f"{ch:02d}"
    items = [s for s in st_map if s["chapter"] == ch_str]
    txt_file = archive_dir / f"prompts_chapter_{ch_str}.txt"
    blocks = [b.strip() for b in txt_file.read_text(encoding="utf-8").split("\n\n") if b.strip()] if txt_file.exists() else []
    old_scenes_by_ch[ch] = []
    for i, item in enumerate(items):
        if i < len(blocks):
            lines = blocks[i].splitlines()
            img = next((l for l in lines if l.startswith("[IMAGE]")), None)
            vid = next((l for l in lines if l.startswith("[VIDEO]")), None)
            old_scenes_by_ch[ch].append({
                "item": item,
                "image": img,
                "video": vid,
                "sentence": item["sentences"][0]
            })

STYLE_PREFIX = "A 2D warm cinematic editorial illustration in high-prestige corporate noir luxury aesthetic. Somber raw slate tones (#1E2229), dark industrial charcoal (#252A34), and brushed titanium textures. Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, authentic 35mm organic film grain, Panavision anamorphic lens with shallow depth of field."

CH_TITLES = {
    1: "The 82% Gambit",
    2: "The 70-Year Fortress",
    3: "The Vertical Weapon",
    4: "The Southern Blitz",
    5: "Cracks & The Solid-State Trap",
    6: "The Fractured Highway"
}

ch_mapping = {
    1: [1],
    2: [2, 3],
    3: [4],
    4: [5],
    5: [6, 7],
    6: [8]
}

blacklist = ["war", "battle", "bomb", "kill", "blood", "weapon", "explosion", "destroy", "strike", "attack"]

def sanitize_ascii_and_blacklist(text):
    # sanitize non-ascii
    text = text.encode("ascii", "ignore").decode("ascii")
    for b in blacklist:
        # replace standalone word
        text = re.sub(r'\b' + b + r'\b', 'contest' if b in ['war', 'battle', 'strike'] else 'disruption', text, flags=re.IGNORECASE)
    return text

all_scenes_json = []
master_prompts = []

for ch in range(1, 7):
    ch_str = f"{ch:02d}"
    text = (ep_dir / f"chapter_{ch_str}_en.md").read_text(encoding="utf-8")
    paras = [p.strip() for p in text.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    sentences = []
    for p in paras:
        for s in re.split(r'(?<=[.?!])\s+', p):
            s = s.strip()
            if s: sentences.append(s)
            
    candidates = []
    for oc in ch_mapping[ch]:
        candidates.extend(old_scenes_by_ch.get(oc, []))
        
    ch_prompts = []
    ch_visual_rows = []
    
    for idx, s in enumerate(sentences, 1):
        sc_id = f"CH{ch_str}_SC{idx:03d}"
        
        # Calculate duration
        words = s.split()
        dur = round(max(len(words) * 0.38, 1.5), 2)
        
        # Find best matching candidate
        best_cand = None
        best_score = 0
        for c in candidates:
            score = SequenceMatcher(None, s.lower(), c["sentence"].lower()).ratio()
            if score > best_score:
                best_score = score
                best_cand = c
                
        if best_cand and best_score >= 0.4 and best_cand["image"] and best_cand["video"]:
            img_prompt = best_cand["image"]
            vid_prompt = best_cand["video"]
            text_overlay = best_cand["item"].get("text_overlay", "")
            flow_type = "I2V" if "@" in img_prompt else "T2V"
            desc = best_cand["item"].get("visual_summary", s)
        else:
            # Generate custom high-end prompt
            flow_type = "T2V"
            text_overlay = ""
            desc = s
            # Extract key visual concept
            img_prompt = f"[IMAGE] {STYLE_PREFIX} Atmospheric cinematic composition depicting: {s} Dramatic perspective, high-end editorial lighting, organic shadows."
            vid_prompt = f"[VIDEO] Slow tracking camera movement highlighting the scene with subtle cinematic push-in --ar 16:9 --dur 8s"

        # Enforce Veo duration and clean ASCII
        if not vid_prompt.endswith("--ar 16:9 --dur 8s"):
            vid_prompt = re.sub(r'--ar\s+16:9.*$', '', vid_prompt).strip()
            vid_prompt += " --ar 16:9 --dur 8s"
            
        img_prompt = sanitize_ascii_and_blacklist(img_prompt)
        vid_prompt = sanitize_ascii_and_blacklist(vid_prompt)
        
        # Collect prompt pair
        prompt_block = f"{img_prompt}\n{vid_prompt}"
        ch_prompts.append(prompt_block)
        master_prompts.append(prompt_block)
        
        # Collect json item
        scene_item = {
            "id": sc_id,
            "chapter": ch_str,
            "sentence_count": 1,
            "duration_sec": dur,
            "text_overlay": text_overlay,
            "visual_summary": s,
            "sentences": [s],
            "base_english_prompt": "A 2D cinematic editorial noir illustration"
        }
        all_scenes_json.append(scene_item)
        
        # Collect visual markdown table row
        overlay_col = f"`{text_overlay}`" if text_overlay else "`Khong`"
        ch_visual_rows.append(f"| **{sc_id}** | {dur}s | {s} | {desc} | {overlay_col} | **{flow_type}** |")
        
    # Write prompts_chapter_XX.txt
    (ep_dir / f"prompts_chapter_{ch_str}.txt").write_text("\n\n".join(ch_prompts) + "\n", encoding="utf-8")
    
    # Write chapter_XX_visual.md
    vis_md_content = f"""# Chapter {ch_str} Visual Script — {CH_TITLES[ch]}

Ban kich ban phan doan thi giac chi tiet cho Chuong {ch}, dong bo toan hoc 1-1 voi {len(sentences)} phan canh trong `scene_timing_map.json` va tep prompt `prompts_chapter_{ch_str}.txt`.

- **Vu tru My thuat:** The Geoeconomic Chessboard & Industrial Noir Luxury.
- **Bang mau:** Somber raw slate tones (#1E2229), dark industrial charcoal (#252A34), brushed titanium, warm champagne gold (#D4AF37), luminous amber (#F59E0B).
- **Anh sang:** Luminous low-key warm directional lighting, soft golden tungsten rim lights, deep velvety ambient shadows, crisp clean contours, 35mm film grain.

---

| Ma Scene | Thoi Luong | Cau Thoai Tieng Anh Goc | Boi Canh Vat Ly & Hanh Dong Dien Anh | Text Overlay (Lower-Left 25%) | Luong Tao Hinh |
| :---: | :---: | :--- | :--- | :---: | :---: |
""" + "\n".join(ch_visual_rows) + "\n"
    (ep_dir / f"chapter_{ch_str}_visual.md").write_text(vis_md_content, encoding="utf-8")
    print(f"Generated Chapter {ch_str}: {len(sentences)} scenes.")

# Write master prompts
(ep_dir / "prompts_master.txt").write_text("\n\n".join(master_prompts) + "\n", encoding="utf-8")
print(f"Generated prompts_master.txt: {len(master_prompts)} total scenes.")

# Write scene_timing_map.json
with open(ep_dir / "scene_timing_map.json", "w", encoding="utf-8") as f:
    json.dump(all_scenes_json, f, indent=2, ensure_ascii=False)
total_dur = sum(s["duration_sec"] for s in all_scenes_json)
print(f"Generated scene_timing_map.json: {len(all_scenes_json)} scenes, total duration: {total_dur:.1f}s ({total_dur/60:.2f} mins).")

