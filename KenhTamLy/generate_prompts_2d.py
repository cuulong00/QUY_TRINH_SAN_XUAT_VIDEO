import json
import os

with open("episodes/nghich-ly-ma-sat-thoi-quen/scene_map.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

def generate_prompt(scene):
    vi_text = scene["visual_summary"]
    vi_lower = vi_text.lower()
    
    camera = "WIDE SHOT"
    if "cận cảnh" in vi_lower or "macro" in vi_lower or "zoom" in vi_lower:
        camera = "EXTREME CLOSE-UP SHOT"
    elif "góc rộng" in vi_lower or "toàn cảnh" in vi_lower:
        camera = "WIDE SHOT"
    elif "góc nhìn từ trên cao" in vi_lower or "nhìn xuống" in vi_lower:
        camera = "HIGH ANGLE SHOT"
    elif "góc quay qua vai" in vi_lower or "over the shoulder" in vi_lower:
        camera = "OVER-THE-SHOULDER SHOT"

    # We map specific subjects based on keywords, but also INCLUDE the Vietnamese text 
    # to guide the generator if it supports multi-lang, or at least keep the vibe.
    subject_map = {
        "điện thoại": "a person mindlessly scrolling on a glowing smartphone in a pitch-black room",
        "giường": "a person hiding under heavy blankets in bed at dawn",
        "bàn làm việc": "an obsessively clean aesthetic study desk that is completely empty",
        "tủ lạnh": "a person breaking their diet, desperately eating junk food lit only by the open fridge at midnight",
        "thẻ tập": "expensive gym membership card and running shoes left unused gathering dust in the dark",
        "router": "a person locking a wifi router inside a dark drawer",
        "mì tôm": "a person eating instant noodles greedily at 11 PM",
        "quyết tâm": "a torn piece of paper with failed plans and goals written on it",
        "cạn kiệt": "a person completely exhausted and burnt out, slumping over a desk",
        "thói quen xấu": "a person sliding effortlessly down a frictionless slippery slope into darkness",
        "thói quen tốt": "a person painfully carrying a giant heavy boulder up a rocky mountain",
        "luật sư": "the shadow of a strict businessman fighting against a lazy giant beast limit",
        "ông chủ lười": "a massive lazy beast shadow taking control over the brain",
        "kế hoạch": "a blank planner notebook covered in dust",
        "não bộ": "a glowing artificial human brain model",
        "ma sát": "heavy iron chains and razor wires blocking a path",
        "rượu": "a messy table filled with empty beer cans and overflowing ashtrays",
        "thuốc lá": "a messy table filled with empty beer cans and overflowing ashtrays",
    }
    
    english_subject = ""
    for k, v in subject_map.items():
        if k in vi_lower:
            english_subject = v
            break
            
    if not english_subject:
        english_subject = "abstract psychological metaphor of mental friction and inner struggle"
        
    prompt = f"An EXPRESSIVE 2D DIGITAL SKETCH {camera}, highly vibrant and vivid colors, striking dynamic color palette, saturated lighting, psychological art of {english_subject}. Concept: {vi_text}. Chiaroscuro, psychological thriller vibe, highly detailed --ar 16:9 --v 6.0"
    
    # Strip newline
    prompt = prompt.replace("\n", " ")
    return prompt

with open("episodes/nghich-ly-ma-sat-thoi-quen/visual_prompts.txt", "w", encoding="utf-8") as f_txt, \
     open("episodes/nghich-ly-ma-sat-thoi-quen/visual_prompts.md", "w", encoding="utf-8") as f_md:
    
    f_md.write("# Visual Prompts - Nghịch Lý Ma Sát\n\n")
    
    for scene in scenes:
        prompt = generate_prompt(scene)
        scene_id = scene["id"]
        
        # Write format
        f_txt.write(f"[{scene_id}] {prompt}\n")
        f_md.write(f"### {scene_id}\n")
        f_md.write(f"**Visual Summary**: {scene['visual_summary']}\n\n")
        f_md.write(f"**Prompt**: `{prompt}`\n\n")

print(f"Generated successfully: 185 prompts mapped to visual_prompts.txt and visual_prompts.md")
