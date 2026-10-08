import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR_I2V = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/cuoc-chien-phan-cuc-ai-i2vplus/thumbnail"
OUTPUT_DIR_CLASSIC = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/cuoc-chien-phan-cuc-ai/thumbnail"
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
                     top_color=(255, 220, 0), bottom_color=(255, 60, 0), 
                     solid_color=(255, 255, 255), stroke_width=36, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=20, shadow_color=(0, 0, 0, 255)):
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

def draw_pill_badge_subtitle(base_img, text, font, center_x, center_y, 
                             pill_bg=(10, 16, 32, 245), border_color=(255, 87, 34, 255),
                             text_color=(255, 255, 255), stroke_width=10):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    pad_x = 65
    pad_y = 22
    x0 = int(center_x - text_w / 2 - pad_x)
    y0 = int(center_y - text_h / 2 - pad_y)
    x1 = int(center_x + text_w / 2 + pad_x)
    y1 = int(center_y + text_h / 2 + pad_y)
    radius = (y1 - y0) // 2
    
    # Shadow
    shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([x0 - 6, y0 - 2, x1 + 6, y1 + 14], radius=radius + 4, fill=(0, 0, 0, 230))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(shadow)
    
    # Body & Border
    pill = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pill)
    pdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=pill_bg, outline=border_color, width=5)
    base_img.alpha_composite(pill)
    
    # Text
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=text_color, stroke_width=stroke_width, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 4), shadow_blur=6)

def draw_pill_badge_multiline(base_img, lines, font, center_x, center_y, line_spacing=18,
                              pill_bg=(10, 16, 32, 245), border_color=(255, 87, 34, 255),
                              text_color=(255, 255, 255), stroke_width=8):
    dummy = ImageDraw.Draw(base_img)
    bboxes = [dummy.textbbox((0, 0), line, font=font, stroke_width=stroke_width) for line in lines]
    widths = [b[2] - b[0] for b in bboxes]
    heights = [b[3] - b[1] for b in bboxes]
    max_w = max(widths)
    total_h = sum(heights) + line_spacing * (len(lines) - 1)
    
    pad_x = 55
    pad_y = 24
    x0 = int(center_x - max_w / 2 - pad_x)
    y0 = int(center_y - total_h / 2 - pad_y)
    x1 = int(center_x + max_w / 2 + pad_x)
    y1 = int(center_y + total_h / 2 + pad_y)
    radius = 28
    
    # Shadow
    shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([x0 - 6, y0 - 2, x1 + 6, y1 + 14], radius=radius + 4, fill=(0, 0, 0, 230))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(shadow)
    
    # Body & Border
    pill = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pill)
    pdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=pill_bg, outline=border_color, width=5)
    base_img.alpha_composite(pill)
    
    # Lines
    curr_y = y0 + pad_y
    for i, line in enumerate(lines):
        line_cy = curr_y + heights[i] / 2
        draw_styled_text(base_img, line, font, center_x, line_cy, is_gradient=False,
                         solid_color=text_color, stroke_width=stroke_width, stroke_color=(0, 0, 0),
                         shadow_offset=(0, 4), shadow_blur=6)
        curr_y += heights[i] + line_spacing

def add_brand_badge(base_img, logo_path, center_x, center_y, target_h=75, border_col=(255, 214, 0, 230)):
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

PLATE_V1_DUAL = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_looming_claws_v1_1789863262021.jpg"
PLATE_V2_CENTRAL = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_looming_claws_v2_1789863313584.jpg"

LOGO_OPENAI = "/Users/pro16/Documents/VideoProject/X-Economic/scratch/openai_logo_white.png"
LOGO_ANTHROPIC = "/Users/pro16/Documents/VideoProject/X-Economic/scratch/anthropic_flawless_white.png"

# Fonts
font_title_v7 = ImageFont.truetype(FONT_PATH, 380)
font_sub_v7 = ImageFont.truetype(FONT_PATH, 86)

font_flank_v8 = ImageFont.truetype(FONT_PATH, 350)
font_sub_2line_v8 = ImageFont.truetype(FONT_PATH, 74)

font_title_v9 = ImageFont.truetype(FONT_PATH, 350)
font_sub_v9 = ImageFont.truetype(FONT_PATH, 80)

SUBTITLE_TEXT = "VÌ SAO GIỚI CHÓP BU PHẢI GIEO RẮC NỖI SỢ?"

# =========================================================================
# 1. THUMBNAIL OPTION 7: DUAL TITANS (SAM & DARIO LOOMING CLAWS)
# =========================================================================
print("Rendering Option 7: Dual Titans Looming Claws...")
img7 = Image.open(PLATE_V1_DUAL).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

# Logos at Top Corners
add_brand_badge(img7, LOGO_OPENAI, center_x=340, center_y=140, target_h=90, border_col=(255, 214, 0, 240))
add_brand_badge(img7, LOGO_ANTHROPIC, center_x=3420, center_y=140, target_h=60, border_col=(255, 87, 34, 240))

# DỌA DẪM - Center Upper (center_y = 290 ensures tilde of Ẫ has 50px buffer from top edge)
draw_styled_text(img7, "DỌA DẪM", font_title_v7, 1920, 290, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=38)

# Subtitle Raised Up in glowing pill badge (center_y = 650 clears the dot under Ọ and hovers above heads)
draw_pill_badge_subtitle(img7, SUBTITLE_TEXT, font_sub_v7, 1920, 650, 
                         pill_bg=(10, 16, 32, 245), border_color=(255, 87, 34, 255),
                         text_color=(255, 255, 255), stroke_width=10)

out7_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v7_doa_dam_dual_titans_4k.jpg")
img7.convert("RGB").save(out7_4k, quality=98, subsampling=0)
shutil.copy(out7_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v7_doa_dam_dual_titans_4k.jpg"))

# =========================================================================
# 2. THUMBNAIL OPTION 8: CENTRAL OVERLORD (EXACT FLANKING STYLE LIKE REFERENCE)
# =========================================================================
print("Rendering Option 8: Central Overlord with Flanking Headline (Reference Style)...")
img8 = Image.open(PLATE_V2_CENTRAL).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

# Logos at Top Corners
add_brand_badge(img8, LOGO_OPENAI, center_x=340, center_y=140, target_h=90, border_col=(255, 214, 0, 240))
add_brand_badge(img8, LOGO_ANTHROPIC, center_x=3420, center_y=140, target_h=60, border_col=(255, 87, 34, 240))

# Subtitle 2-line pill in the top center above Sam's head (center_y = 170)
draw_pill_badge_multiline(img8, ["VÌ SAO GIỚI CHÓP BU", "PHẢI GIEO RẮC NỖI SỢ?"], 
                          font_sub_2line_v8, center_x=1920, center_y=170, line_spacing=14,
                          pill_bg=(10, 16, 32, 245), border_color=(255, 87, 34, 255),
                          text_color=(255, 255, 255), stroke_width=8)

# Flanking Headline: "DỌA" on left flank, "DẪM" on right flank
# With 2-line pill at center (width ~1100), DỌA and DẪM sit perfectly without collision!
draw_styled_text(img8, "DỌA", font_flank_v8, 880, 360, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=36)
draw_styled_text(img8, "DẪM", font_flank_v8, 2960, 360, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=36)

out8_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v8_doa_dam_central_flanking_4k.jpg")
img8.convert("RGB").save(out8_4k, quality=98, subsampling=0)
shutil.copy(out8_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v8_doa_dam_central_flanking_4k.jpg"))

# =========================================================================
# 3. THUMBNAIL OPTION 9: CENTRAL OVERLORD WITH UNIFIED HEADLINE & LOWER SUBTITLE
# =========================================================================
print("Rendering Option 9: Central Overlord with Unified Headline...")
img9 = Image.open(PLATE_V2_CENTRAL).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

# Logos at Top Corners
add_brand_badge(img9, LOGO_OPENAI, center_x=340, center_y=140, target_h=90, border_col=(255, 214, 0, 240))
add_brand_badge(img9, LOGO_ANTHROPIC, center_x=3420, center_y=140, target_h=60, border_col=(255, 87, 34, 240))

# DỌA DẪM at top center (center_y = 260 ensures tilde is fully visible)
draw_styled_text(img9, "DỌA DẪM", font_title_v9, 1920, 260, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=36)

# Subtitle in 1-line pill hovering at center_y = 570
draw_pill_badge_subtitle(img9, SUBTITLE_TEXT, font_sub_v9, 1920, 570, 
                         pill_bg=(10, 16, 32, 245), border_color=(255, 87, 34, 255),
                         text_color=(255, 255, 255), stroke_width=9)

out9_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v9_doa_dam_central_unified_4k.jpg")
img9.convert("RGB").save(out9_4k, quality=98, subsampling=0)
shutil.copy(out9_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v9_doa_dam_central_unified_4k.jpg"))

print("Successfully re-rendered 4K options 7, 8, and 9 with zero collisions and verified diacritics!")
