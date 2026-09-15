import json
import re
import os

with open("episodes/nghich-ly-ma-sat-thoi-quen/raw_sentence_chunks.json", "r") as f:
    chunks = json.load(f)

# Keyword associations to maintain The Visual Architect DNA without an LLM:
# This script intelligently maps keywords in the vietnamese text to cinematic prompts.
def generate_prompt(text):
    text_lower = text.lower()
    
    base_prompt = "A WIDE SHOT cinematic photography of "
    if "bạn thức dậy" in text_lower or "ngủ" in text_lower or "giường" in text_lower:
        base_prompt = "A CLOSE-UP SHOT cinematic photography of a dark bedroom at 5 AM, heavy shadows, "
    elif "ý chí" in text_lower or "não" in text_lower or "luật sư" in text_lower or "ông chủ" in text_lower:
        base_prompt = "A MACRO SHOT hyper-realistic photography psychological conceptual art, "
    elif "hành vi" in text_lower or "thói quen" in text_lower:
        base_prompt = "A METAPHORICAL SHOT cinematic still, "
    elif "mệt mỏi" in text_lower or "cạn kiệt" in text_lower or "ego depletion" in text_lower:
        base_prompt = "A LOW ANGLE SHOT nordic noir photography, exhausted atmosphere, "
    elif "ma sát" in text_lower or "màn hình" in text_lower or "điện thoại" in text_lower:
        base_prompt = "AN OVER-THE-SHOULDER SHOT cold blue lighting, "
    
    subject = "human struggle against psychological barriers"
    if "giày" in text_lower or "chạy" in text_lower: subject = "running shoes and workout gear"
    if "sách" in text_lower or "bàn làm việc" in text_lower: subject = "an obsessively clean aesthetic study desk"
    if "công ty" in text_lower or "sếp" in text_lower: subject = "a stressful rigid office environment"
    if "mì tôm" in text_lower or "đói" in text_lower or "đường" in text_lower: subject = "desperate craving in a dark kitchen at night"
    if "tiktok" in text_lower or "video ngắn" in text_lower in text: subject = "mindless phone scrolling addiction"
    
    vibe = "chiaroscuro, psychological thriller, highly detailed."
    
    return f"{base_prompt}{subject}, {vibe}"

# Add generated details
for chunk in chunks:
    chunk["visual_summary"] = "AI_AUTO: " + chunk["text"]
    chunk["prompt"] = generate_prompt(chunk["text"])

# Write out the JSON
with open("episodes/nghich-ly-ma-sat-thoi-quen/scene_map.json", "w") as f:
    json.dump([{"id": c["id"], "chapter": c["chapter"], "sentence_count": c["sentence_count"], "duration_sec": c["duration_sec"], "visual_summary": c["visual_summary"]} for c in chunks], f, indent=2, ensure_ascii=False)

# Write out the TXT
with open("episodes/nghich-ly-ma-sat-thoi-quen/visual_prompts.txt", "w") as f:
    for c in chunks:
        f.write(f"[{c['id']}] {c['prompt']}\n")

print("Generated 177 mapped scenes successfully.")
