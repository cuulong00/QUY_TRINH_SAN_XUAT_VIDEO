import json
import os

with open("scene_timing_map.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

angles = [
    "A WIDE STILL SHOT of",
    "An EXTREME CLOSE-UP of",
    "A LOW ANGLE SHOT of",
    "A SYMMETRICAL COMPOSITION showing"
]
style = "modern lively 2D animation style, Vietnamese aesthetic, vibrant colors, flat cel shading, highly detailed background, cinematic lighting, culturally authentic Vietnamese elements --ar 16:9"

out_lines = []
for idx, sc in enumerate(scenes):
    text = sc["visual_summary"].lower()
    
    # Default
    subject = "a Vietnamese businessman in a modern suit standing stoically"
    env = "a sleek modern office overlooking a cyberpunk Asian metropolis"
    light = "Cinematic dramatic lighting"
    
    if "bình ngô đại cáo" in text or "dân tộc" in text or "hùng vương" in text:
        subject = "a historic Vietnamese scroll parchment seamlessly morphing into a futuristic glowing digital blueprint"
        env = "a mystical high-tech vault"
        light = "Golden ethereal glowing light"
    elif "chip" in text or "bán dẫn" in text:
        subject = "a colossal glowing blue microchip core pulsating with digital data networks"
        env = "a hyper-modern subterranean tech lab"
        light = "Intense neon blue rim lighting"
    elif "tata" in text or "samsung" in text or "hyundai" in text or "foxconn" in text:
        subject = "a massive metaphorical chessboard where glowing Asian corporate emblems replace the chess pieces"
        env = "a dark void illuminated by neon grids"
        light = "High contrast chiaroscuro lighting"
    elif "tài xế" in text or "grab" in text:
        subject = "a Vietnamese ride-hail driver looking thoughtfully at a passing futuristic autonomous vehicle"
        env = "a vibrant neon-lit modern Vietnamese night street"
        light = "Neon city ambient glow"
    elif "mì gói" in text or "ukraine" in text or "10.000 usd" in text or "khởi nghiệp" in text:
        subject = "a young Vietnamese entrepreneur holding a single glowing package of instant noodles"
        env = "a cold snowy European street corner"
        light = "High contrast crisp dramatic lighting"
    elif "sụp đổ" in text or "rủi ro" in text or "vỡ nợ" in text or "ảo tưởng" in text or "lehman" in text:
        subject = "a stack of official financial documents bursting into frozen flames"
        env = "a dark void with descending data streams"
        light = "Harsh red warning lighting"
    elif "gia đình" in text or "gia tộc" in text or "chủ tịch" in text or "con trai" in text or "cổ phiếu" in text or "sở hữu" in text:
        subject = "a Vietnamese businessman standing before a massive glowing hologram of a complex family tree architecture"
        env = "a dark minimalist ultra-luxury boardroom"
        light = "High contrast directional spotlighting"
    elif "thể thao" in text or "sân vận động" in text or "olympic" in text or "135.000" in text:
        subject = "a colossal ultra-modern stadium shaped like a traditional Vietnamese bronze drum, glowing brilliantly"
        env = "a massive Asian metropolis at night"
        light = "Epic grand stadium spotlighting"
    elif "đường sắt" in text or "cao tốc" in text or "hạ tầng" in text or "cầu vượt" in text or "vinspeed" in text:
        subject = "a futuristic high-speed bullet train hovering perfectly still over an ultra-modern bridge"
        env = "a vast lush tropical Vietnamese landscape"
        light = "Bright vivid daylight"
    elif "thép" in text or "nhà máy" in text or "công nghiệp" in text or "luyện kim" in text or "vinmetal" in text:
        subject = "massive industrial robotic arms pouring glowing molten steel, frozen in action"
        env = "a colossal hyper-modern industrial factory"
        light = "Dramatic fiery orange lighting"
    elif "trạm sạc" in text or "năng lượng" in text or "vinenergo" in text or "v-green" in text:
        subject = "a sleek futuristic glowing electric charging station enveloped by neon green data vines"
        env = "a bustling modern Vietnamese city street corner"
        light = "Vibrant green ambient lighting"
    elif "robot" in text or "ai" in text or "trí tuệ nhân tạo" in text or "công nghệ" in text or "dữ liệu" in text:
        subject = "a glowing holographic brain suspended above a futuristic assembly line of androids"
        env = "a pristine high-tech corporate laboratory"
        light = "Cool blue neon rim lighting"
    elif "xe điện" in text or "ô tô" in text or "vinfast" in text or "xanh sm" in text:
        subject = "a futuristic sleek electric vehicle frozen at high speed, leaving a trail of glowing light"
        env = "a vibrant neon-lit modern Vietnamese overpass"
        light = "Neon cyberpunk city glow lighting"
    elif "nhân viên" in text or "việc làm" in text or "y tế" in text or "giáo dục" in text or "vinhomes" in text or "vinschool" in text or "thuê nhà" in text:
        subject = "an ordinary Vietnamese citizen looking up in awe at floating digital data menus representing essential services"
        env = "a bustling modern Vietnamese urban apartment complex"
        light = "Soft cinematic street lighting"
    elif "quốc gia" in text or "chính phủ" in text or "nền tảng" in text or "kiến tạo" in text or "động lực" in text or "gdp" in text or "doanh thu" in text or "thuế" in text:
        subject = "a giant glowing map of Vietnam overlaid with futuristic digital nodes and massive golden pillars representing economic growth"
        env = "a high-tech panoramic command center"
        light = "Epic volumetric glowing light rays"
    
    angle = angles[idx % 4]
    prompt = f"{idx+1}. {angle} {subject} in {env}. {light}. {style}"
    out_lines.append(prompt)

with open("image_prompts.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(out_lines))

print(f"Generated {len(out_lines)} static image prompts covering the visual metaphors successfully to image_prompts.txt")
