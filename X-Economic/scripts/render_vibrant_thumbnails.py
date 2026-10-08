import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

OUTPUT_DIR_I2V = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/cuoc-chien-phan-cuc-ai-i2vplus/thumbnail"
OUTPUT_DIR_CLASSIC = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/cuoc-chien-phan-cuc-ai/thumbnail"
BRAIN_DIR = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5"

os.makedirs(OUTPUT_DIR_I2V, exist_ok=True)
os.makedirs(OUTPUT_DIR_CLASSIC, exist_ok=True)

FONT_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"

def create_gradient(width, height, top_color, bottom_color):
    top = np.array(top_color, dtype=float)
    bottom = np.array(bottom_color, dtype=float)
    gradient = np.zeros((height, width, 4), dtype=np.uint8)
    for y in range(height):
        factor = y / max(height - 1, 1)
        c = top + factor * (bottom - top)
        gradient[y, :, 0:3] = c[:3]
        gradient[y, :, 3] = 255
    return Image.fromarray(gradient, 'RGBA')

def draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     top_color=(255, 240, 0), bottom_color=(255, 50, 0), 
                     solid_color=(255, 255, 255), stroke_width=38, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255),
                     outer_glow_color=None, outer_glow_blur=24):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
    # 0. Outer Glow (Optional for extreme vibrant pop)
    if outer_glow_color:
        glow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_img)
        gdraw.text((x, y), text, font=font, fill=outer_glow_color, 
                   stroke_width=stroke_width + 20, stroke_fill=outer_glow_color)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(outer_glow_blur))
        base_img.alpha_composite(glow_img)
    
    # 1. Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sx = x + shadow_offset[0]
    sy = y + shadow_offset[1]
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 16, stroke_fill=shadow_color)
    if shadow_blur > 0:
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
    base_img.alpha_composite(shadow_img)
    
    # 2. Stroke
    stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(stroke_img)
    kdraw.text((x, y), text, font=font, fill=stroke_color, stroke_width=stroke_width, stroke_fill=stroke_color)
    base_img.alpha_composite(stroke_img)
    
    # 3. Fill
    if is_gradient:
        pad = stroke_width * 2 + 60
        mask_img = Image.new('L', (text_w + pad, text_h + pad), 0)
        mdraw = ImageDraw.Draw(mask_img)
        mx = -bbox[0] + pad // 2
        my = -bbox[1] + pad // 2
        mdraw.text((mx, my), text, font=font, fill=255)
        
        grad = create_gradient(mask_img.width, mask_img.height, top_color, bottom_color)
        grad.putalpha(mask_img)
        
        paste_x = x + bbox[0] - pad // 2
        paste_y = y + bbox[1] - pad // 2
        base_img.paste(grad, (paste_x, paste_y), grad)
    else:
        fill_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        fdraw = ImageDraw.Draw(fill_img)
        fdraw.text((x, y), text, font=font, fill=solid_color)
        base_img.alpha_composite(fill_img)

def draw_semi_trans_framed_subtitle(base_img, text, font, center_x, center_y,
                                   bg_alpha=0.6, bg_color=(8, 14, 28),
                                   border_color=(255, 120, 0, 255), border_width=6,
                                   text_color=(255, 255, 255), text_stroke_width=10,
                                   pad_x=75, pad_y=26, radius=26, glow_border=True,
                                   glow_color=None):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=text_stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x0 = int(center_x - text_w / 2 - pad_x)
    y0 = int(center_y - text_h / 2 - pad_y)
    x1 = int(center_x + text_w / 2 + pad_x)
    y1 = int(center_y + text_h / 2 + pad_y)
    
    # 1. Outer Box Shadow
    box_shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bsdraw = ImageDraw.Draw(box_shadow)
    bsdraw.rounded_rectangle([x0 - 4, y0 + 4, x1 + 4, y1 + 16], radius=radius + 4, fill=(0, 0, 0, 210))
    box_shadow = box_shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(box_shadow)
    
    # 2. Outer Glow around border if enabled
    if glow_border:
        glow_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_layer)
        gc = glow_color if glow_color else (border_color[0], border_color[1], border_color[2], 160)
        gdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, outline=gc, width=border_width + 8)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(14))
        base_img.alpha_composite(glow_layer)
        
    # 3. Semi-transparent Body (alpha = 0.6)
    alpha_int = int(255 * bg_alpha)
    fill_rgba = (bg_color[0], bg_color[1], bg_color[2], alpha_int)
    
    body_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(body_layer)
    bdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_rgba, outline=border_color, width=border_width)
    base_img.alpha_composite(body_layer)
    
    # 4. Text inside frame
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=text_color, stroke_width=text_stroke_width, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 4), shadow_blur=6)

# =============================================================================
# CONFIGURATIONS FOR 5 NEW VIBRANT OPTIONS
# =============================================================================

MAIN_HEADLINE = "GIEO RẮC NỖI SỢ"
SUBTITLE_TEXT = "VÌ SAO GIỚI CHÓP BU PHẢI LÀM VẬY?"

font_title = ImageFont.truetype(FONT_PATH, 340)
font_sub = ImageFont.truetype(FONT_PATH, 86)

CONFIGS = [
    {
        "id": "vibrant_1_flaming_storm",
        "plate": os.path.join(BRAIN_DIR, "thumb_flaming_pulpit_1789879921564.jpg"),
        "title_top": (255, 245, 0),       # Electric Lemon Yellow
        "title_bot": (255, 40, 0),        # Blazing Fiery Orange
        "outer_glow": (255, 120, 0, 100), # Warm fiery aura
        "border_color": (255, 80, 0, 255),# Hot neon orange-red
        "bg_color": (12, 6, 18),          # Deep twilight obsidian
        "glow_color": (255, 80, 0, 180),
        "enhance_color": 1.08,
        "enhance_contrast": 1.05,
    },
    {
        "id": "vibrant_2_neon_cyber_puppeteers",
        "plate": os.path.join(BRAIN_DIR, "thumb_neon_puppeteers_1789879709190.jpg"),
        "title_top": (230, 255, 0),       # Acid Electric Lime
        "title_bot": (255, 90, 40),       # Coral Neon Amber
        "outer_glow": (0, 240, 255, 90),  # Electric cyan ambient glow
        "border_color": (0, 235, 255, 255),# Electric Cyan glowing frame
        "bg_color": (6, 14, 28),          # Dark cyber blue
        "glow_color": (0, 235, 255, 180),
        "enhance_color": 1.10,
        "enhance_contrast": 1.06,
    },
    {
        "id": "vibrant_3_cyber_core_hologram",
        "plate": os.path.join(BRAIN_DIR, "thumb_cyber_core_1789879983531.jpg"),
        "title_top": (255, 255, 255),     # Pure Radiant Diamond White
        "title_bot": (255, 35, 45),       # Molten Red Magma
        "outer_glow": (255, 215, 0, 95),  # Golden cyber aura
        "border_color": (255, 215, 0, 255),# Pure Neon Gold frame
        "bg_color": (8, 16, 24),          # Deep teal black
        "glow_color": (255, 215, 0, 170),
        "enhance_color": 1.08,
        "enhance_contrast": 1.05,
    },
    {
        "id": "vibrant_4_senate_noir_split",
        "plate": os.path.join(BRAIN_DIR, "thumb_senate_noir_1789880061771.jpg"),
        "title_top": (255, 225, 0),       # Imperial Gold
        "title_bot": (255, 25, 0),        # Blazing Crimson
        "outer_glow": (255, 90, 0, 90),
        "border_color": (255, 110, 0, 255),# Blazing Fire Amber
        "bg_color": (10, 10, 20),
        "glow_color": (255, 110, 0, 180),
        "enhance_color": 1.12,
        "enhance_contrast": 1.08,
    },
    {
        "id": "vibrant_5_shadow_puppets_boosted",
        "plate": os.path.join(BRAIN_DIR, "thumb_shadow_puppets_1789865549760.jpg"),
        "title_top": (255, 245, 0),       # Ultra Bright Lemon
        "title_bot": (255, 50, 0),        # Molten Orange Fire
        "outer_glow": (255, 140, 0, 110), # Amber glow matching the lantern
        "border_color": (255, 140, 0, 255),# Warm glowing lantern bronze
        "bg_color": (12, 10, 16),
        "glow_color": (255, 140, 0, 190),
        "enhance_color": 1.18,            # Boost lantern color richness
        "enhance_contrast": 1.10,
    }
]

for cfg in CONFIGS:
    name = cfg["id"]
    print(f"--> Rendering vibrant 4K thumbnail: {name}...")
    img = Image.open(cfg["plate"]).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # 0. Color & Contrast Enhancement for extra punch & visual magnetism
    if cfg.get("enhance_color", 1.0) != 1.0:
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(cfg["enhance_color"])
    if cfg.get("enhance_contrast", 1.0) != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(cfg["enhance_contrast"])
        
    # 1. Main Headline: GIEO RẮC NỖI SỢ (center_y = 290)
    draw_styled_text(img, MAIN_HEADLINE, font_title, 1920, 290, is_gradient=True,
                     top_color=cfg["title_top"], bottom_color=cfg["title_bot"],
                     stroke_width=38, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22,
                     outer_glow_color=cfg.get("outer_glow"))
    
    # 2. Subtitle: VÌ SAO GIỚI CHÓP BU PHẢI LÀM VẬY? (center_y = 1728)
    draw_semi_trans_framed_subtitle(img, SUBTITLE_TEXT, font_sub, 1920, 1728,
                                    bg_alpha=0.6, bg_color=cfg["bg_color"],
                                    border_color=cfg["border_color"], border_width=6,
                                    text_color=(255, 255, 255), text_stroke_width=10,
                                    pad_x=75, pad_y=26, radius=26, glow_border=True,
                                    glow_color=cfg.get("glow_color"))
    
    out_filename = f"thumbnail_{name}_4k.jpg"
    out_path_i2v = os.path.join(OUTPUT_DIR_I2V, out_filename)
    out_path_classic = os.path.join(OUTPUT_DIR_CLASSIC, out_filename)
    out_path_brain = os.path.join(BRAIN_DIR, out_filename)
    
    img.convert("RGB").save(out_path_i2v, quality=98, subsampling=0)
    shutil.copy(out_path_i2v, out_path_classic)
    shutil.copy(out_path_i2v, out_path_brain)
    print(f"    Saved: {out_path_i2v}")

print("All 5 vibrant thumbnails successfully rendered in 4K UHD!")
