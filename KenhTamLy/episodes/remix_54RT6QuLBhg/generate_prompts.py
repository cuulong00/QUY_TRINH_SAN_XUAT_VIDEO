import json
import os

os.chdir('/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/remix_54RT6QuLBhg')

with open('b_scenes.json', 'r') as f:
    scenes = json.load(f)

scene_timing_map = []
visual_prompts = []

# Đổi toàn bộ các tag monochrome thành full color, vibrant, sinh động
themes = {
    1: [
        "2D sketch illustration, vibrant colors, expressive watercolor splashes, a dark bedroom illuminated by a glowing neon light, highly detailed, vivid drawing style",
        "2D sketch illustration, expressive colored line art, a tense hand gripping a coffee cup, dramatic colorful shading, vivid psychological feeling",
        "2D sketch illustration, rich colors, a solitary figure standing by a rainy window at night, colorful city lights reflecting on wet glass, atmospheric",
        "2D sketch illustration, close up of a ticking analog clock in shadows, warm glowing accents, vivid colors, pencil and digital painting blend"
    ],
    2: [
        "2D sketch illustration, vibrant colors, looking into a cracked mirror in a dimly lit bathroom, intense neon highlights reflecting off the glass, expressive",
        "2D sketch illustration, a bright red pen resting on an exam paper, surrounded by glowing abstract thought symbols, vivid colors, dynamic composition",
        "2D sketch illustration, an empty hospital corridor painted with surreal vivid sunset colors filtering through the windows, atmospheric painted sketch",
        "2D sketch illustration, a prestigious glowing golden trophy covered in dust on a dark shelf, rich cinematic colors, expressive shading"
    ],
    3: [
        "2D sketch illustration, richly colored pencil sketch, an ornate open notebook emitting a magical golden glow in a cafe, vivid colors",
        "2D sketch illustration, a messy room with a perfectly clean desk illuminated by a warm, vibrant sunlight beam, colorful painting style",
        "2D sketch illustration, dark coffee stains mingling with vibrant watercolor splatters on a project plan, colorful psychological tension",
        "2D sketch illustration, a computer screen glowing with intense neon blue and pink illuminating an empty chair, vivid cinematic sketch"
    ],
    4: [
        "2D sketch illustration, vibrant colors, vintage pendulum swinging with colorful motion blur lines, dynamic expressive drawing",
        "2D sketch illustration, a child's wooden toy painted in bright primary colors abandoned on a dark floor, dramatic colorful lighting",
        "2D sketch illustration, a porcelain mask starting to crack with bright glowing light spilling from the cracks, vivid colors, highly detailed",
        "2D sketch illustration, a silhouette backed into a colored neon-lit corner, rich purples and reds in the shadows, expressive line art"
    ],
    5: [
        "2D sketch illustration, a zen garden with vividly colored autumn leaves scattered chaotically, expressive vibrant painting style",
        "2D sketch illustration, a bright blue yoga mat unrolled in a dark room illuminated by a strong, warm sunbeam, colorful and atmospheric",
        "2D sketch illustration, burning incense sticks with swirling colorful smoke next to a glowing laptop, vivid colors, expressive sketch",
        "2D sketch illustration, looking through a gap in a door into a room glowing with intense warm orange light, colorful storytelling"
    ],
    6: [
        "2D sketch illustration, vibrant colors, a label maker printing out brightly colored text tape in the dark, expressive drawing",
        "2D sketch illustration, a hand hesitating over a neon-glowing 'Send' button, intense colorful contrast, dramatic painting style",
        "2D sketch illustration, an open door revealing a rainy street illuminated by vibrant neon signs and colorful reflections, atmospheric",
        "2D sketch illustration, a crumpled brightly colored paper being flattened out on a desk, expressive colorful shading, high impact"
    ],
    7: [
        "2D sketch illustration, a heavy brass lock glowing warmly under a cinematic light, rich colors, expressive detailed sketch",
        "2D sketch illustration, first rays of golden dawn piercing through blinds, casting vivid warm colors across a dark room",
        "2D sketch illustration, a figure stepping out into a foggy morning street painted with soft pastel sunrise colors, atmospheric sketch",
        "2D sketch illustration, a journaling pen resting on a vividly painted page, warm glowing morning light, beautiful colored pencil style"
    ]
}

def add_variation(prompt, idx):
    variations = ["highly vivid", "expressive digital coloration", "rich gradients", "vibrant colored pencil style"]
    var = variations[idx % len(variations)]
    return prompt + f", {var}"

for i, s in enumerate(scenes):
    ch = s.get('chapter', 1)
    if ch not in themes: ch = 1
    
    prompt_base = themes[ch][i % len(themes[ch])]
    prompt_base = add_variation(prompt_base, i)
    
    summary = prompt_base.split(',')[2].strip().capitalize()
    
    count = s.get('sentence_count', 1)
    dur = count * 5
    
    sc_id = f"SC{i+1:03d}"
    
    scene_timing_map.append({
        "id": sc_id,
        "sentence_count": count,
        "duration_sec": dur,
        "visual_summary": summary + " - 2D sketch illustration, vivid colors."
    })
    
    visual_prompts.append(f"[{sc_id}] {prompt_base} --ar 16:9 --v 6.0")

with open('scene_timing_map.json', 'w') as f:
    json.dump(scene_timing_map, f, ensure_ascii=False, indent=4)

with open('visual_prompts.txt', 'w') as f:
    f.write('\n'.join(visual_prompts))

print(f"Generated {len(scene_timing_map)} FULL COLOR 2D sketch scenes successfully.")
