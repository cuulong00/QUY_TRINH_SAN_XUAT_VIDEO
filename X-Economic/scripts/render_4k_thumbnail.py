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
                     top_color=(255, 214, 0), bottom_color=(255, 75, 20), 
                     solid_color=(255, 255, 255), stroke_width=28, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 18), shadow_blur=16, shadow_color=(0, 0, 0, 250)):
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
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 10, stroke_fill=shadow_color)
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
        pad = stroke_width * 2 + 50
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

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=1800):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(240 * factor)
        color = (255, 205, 50, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 5)], fill=color)
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     stroke_width=16, shadow_offset=(0, 10), shadow_blur=10)

# Paths to the 2 generated clean plates
BG_V1 = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_clean_bg_v1_1789860867531.jpg"
BG_V2 = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_clean_bg_v2_1789860885388.jpg"

font_title_4k = ImageFont.truetype(FONT_PATH, 280)
font_sub_4k = ImageFont.truetype(FONT_PATH, 92)

# -------------------------------------------------------------
# RENDER PHIÊN BẢN 1: BÀN HỘI NGHỊ / BÁO CHÍ (SAM ALTMAN & DARIO AMODEI)
# -------------------------------------------------------------
print("Rendering Variant 1 (4K)...")
img1 = Image.open(BG_V1).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
# DỌA DẪM - Center Upper
draw_styled_text(img1, "DỌA DẪM", font_title_4k, 1920, 360, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 65, 0), stroke_width=32)
# Bottom subtitle
draw_bottom_bar(img1, "VÌ SAO HỌ PHẢI GIEO RẮC NỖI SỢ?", font_sub_4k, 1920, 1940, 2030, line_width=2200)

v1_out_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v1_doa_dam_hearing_4k.jpg")
img1.convert("RGB").save(v1_out_4k, quality=98, subsampling=0)
shutil.copy(v1_out_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v1_doa_dam_hearing_4k.jpg"))

# -------------------------------------------------------------
# RENDER PHIÊN BẢN 2: TUYÊN THỆ THƯỢNG VIỆN (SAM ALTMAN OATH & DARIO AMODEI)
# -------------------------------------------------------------
print("Rendering Variant 2 (4K)...")
img2 = Image.open(BG_V2).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
# DỌA DẪM - Center Upper
draw_styled_text(img2, "DỌA DẪM", font_title_4k, 1920, 340, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 65, 0), stroke_width=32)
# Bottom subtitle
draw_bottom_bar(img2, "VÌ SAO HỌ PHẢI GIEO RẮC NỖI SỢ?", font_sub_4k, 1920, 1940, 2030, line_width=2200)

v2_out_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v2_doa_dam_oath_4k.jpg")
img2.convert("RGB").save(v2_out_4k, quality=98, subsampling=0)
shutil.copy(v2_out_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v2_doa_dam_oath_4k.jpg"))

print("Rendering complete!")
print("Saved to:")
print(" -", v1_out_4k)
print(" -", v2_out_4k)
