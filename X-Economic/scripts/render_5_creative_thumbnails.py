import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR_I2V = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/cuoc-chien-phan-cuc-ai-i2vplus/thumbnail"
OUTPUT_DIR_CLASSIC = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/cuoc-chien-phan-cuc-ai/thumbnail"
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
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255)):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
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
                                   bg_alpha=0.6, bg_color=(10, 16, 32),
                                   border_color=(255, 140, 0, 255), border_width=6,
                                   text_color=(255, 255, 255), text_stroke_width=10,
                                   pad_x=70, pad_y=24, radius=26, glow_border=True):
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
    bsdraw.rounded_rectangle([x0 - 4, y0 + 4, x1 + 4, y1 + 16], radius=radius + 4, fill=(0, 0, 0, 200))
    box_shadow = box_shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(box_shadow)
    
    # 2. Outer Glow around border if enabled (makes it pop dramatically)
    if glow_border:
        glow_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_layer)
        glow_color = (border_color[0], border_color[1], border_color[2], 140)
        gdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, outline=glow_color, width=border_width + 8)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(12))
        base_img.alpha_composite(glow_layer)
        
    # 3. Semi-transparent Body (alpha = 0.6 -> int(255 * 0.6) = 153)
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

def add_brand_badge(base_img, logo_path, center_x, center_y, target_h=70, border_col=(255, 214, 0, 240)):
    if not os.path.exists(logo_path):
        return
    logo = Image.open(logo_path).convert("RGBA")
    aspect = logo.width / logo.height
    new_w = int(target_h * aspect)
    logo = logo.resize((new_w, target_h), Image.Resampling.LANCZOS)
    
    pad_x = 44
    pad_y = 18
    badge_w = new_w + pad_x * 2
    badge_h = target_h + pad_y * 2
    
    x0 = center_x - badge_w // 2
    y0 = center_y - badge_h // 2
    x1 = x0 + badge_w
    y1 = y0 + badge_h
    radius = 22
    
    # Shadow
    badge_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge_layer)
    bdraw.rounded_rectangle([x0 - 4, y0 - 2, x1 + 4, y1 + 12], radius=radius + 4, fill=(0, 0, 0, 200))
    badge_layer = badge_layer.filter(ImageFilter.GaussianBlur(12))
    base_img.alpha_composite(badge_layer)
    
    # Body
    badge_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bbdraw = ImageDraw.Draw(badge_body)
    bbdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=(10, 16, 32, 225), outline=border_col, width=4)
    base_img.alpha_composite(badge_body)
    
    # Paste logo
    lx = x0 + pad_x
    ly = y0 + pad_y
    base_img.alpha_composite(logo, (lx, ly))

# =============================================================================
# ASSETS & CONFIG
# =============================================================================
LOGO_OPENAI = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch/openai_logo_white.png"
LOGO_ANTHROPIC = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/scratch/anthropic_flawless_white.png"

# Plates
PLATES = {
    "v1_tshirt_boo": "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_tshirt_titans_v2_1789863751552.jpg",
    "v2_shadow_puppets": "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_shadow_puppets_1789865549760.jpg",
    "v3_demon_masks": "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_demon_masks_1789865577015.jpg",
    "v4_looming_claws": "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_looming_claws_v1_1789863262021.jpg",
    "v5_central_overlord": "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_looming_claws_v2_1789863313584.jpg",
}

MAIN_HEADLINE = "GIEO RẮC NỖI SỢ"
SUBTITLE_TEXT = "VÌ SAO GIỚI CHÓP BU PHẢI LÀM VẬY?"

# Font definitions
# Main headline font: 350px - 380px ensures "GIEO RẮC NỖI SỢ" (14 chars with spaces) spans ~3100px across 3840px
font_title = ImageFont.truetype(FONT_PATH, 340)
font_sub = ImageFont.truetype(FONT_PATH, 86)

# High-impact vibrant gradient: Electric Lemon Yellow -> Fiery Blazing Orange Red
COLOR_TOP_ELECTRIC = (255, 235, 0)
COLOR_BOT_FIRE = (255, 45, 0)

# Render each version
for key, plate_path in PLATES.items():
    print(f"--> Rendering 4K Thumbnail: {key}...")
    img = Image.open(plate_path).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # 1. Main Headline: GIEO RẮC NỖI SỢ (Upper Center, center_y = 290)
    # Extra vibrant electric gold-fire gradient with thick outline and deep shadow
    # Corner badges omitted to eliminate clutter and give 100% breathing room to the massive headline
    draw_styled_text(img, MAIN_HEADLINE, font_title, 1920, 290, is_gradient=True,
                     top_color=COLOR_TOP_ELECTRIC, bottom_color=COLOR_BOT_FIRE,
                     stroke_width=38, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22)
    
    # 3. Subtitle: VÌ SAO GIỚI CHÓP BU PHẢI LÀM VẬY?
    # Positioned at 20% distance from bottom edge: y = 2160 * 0.8 = 1728!
    # Enclosed in 0.6 opacity semi-transparent box with glowing warm bronze/orange border
    draw_semi_trans_framed_subtitle(img, SUBTITLE_TEXT, font_sub, 1920, 1728,
                                    bg_alpha=0.6, bg_color=(8, 14, 28),
                                    border_color=(255, 120, 0, 255), border_width=6,
                                    text_color=(255, 255, 255), text_stroke_width=10,
                                    pad_x=75, pad_y=26, radius=26, glow_border=True)
    
    out_file_name = f"thumbnail_{key}_4k.jpg"
    out_path_i2v = os.path.join(OUTPUT_DIR_I2V, out_file_name)
    out_path_classic = os.path.join(OUTPUT_DIR_CLASSIC, out_file_name)
    
    img.convert("RGB").save(out_path_i2v, quality=98, subsampling=0)
    shutil.copy(out_path_i2v, out_path_classic)
    print(f"    Saved: {out_path_i2v}")

print("All 5 creative thumbnails successfully rendered in 4K UHD!")
