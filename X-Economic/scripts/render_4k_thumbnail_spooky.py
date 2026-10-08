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

def apply_bottom_scrim(base_img, height_px=320, max_alpha=180):
    scrim = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scrim)
    img_h = base_img.height
    start_y = img_h - height_px
    for y in range(start_y, img_h):
        factor = (y - start_y) / height_px
        alpha = int(max_alpha * (factor ** 1.5))
        sdraw.line([(0, y), (base_img.width, y)], fill=(0, 0, 0, alpha))
    base_img.alpha_composite(scrim)

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=2200):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(245 * factor)
        color = (255, 215, 60, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 6)], fill=color)
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     stroke_width=18, shadow_offset=(0, 12), shadow_blur=12)

# Paths to the plates
BG_SPOOKY_1 = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_spooky_boo_v1_1789861190509.jpg"
BG_SPOOKY_4 = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_spooky_boo_v4_1789861256728.jpg"

font_title_massive = ImageFont.truetype(FONT_PATH, 420)
font_sub_titlecase = ImageFont.truetype(FONT_PATH, 110)

# =========================================================================
# 1. RENDER OPTION 1 (SPOOKY CLOSE-UP / HÙ DỌA CẬN CẢNH)
# =========================================================================
print("Rendering Spooky Variant 1 (Medium Close-Up)...")
img1 = Image.open(BG_SPOOKY_1).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
apply_bottom_scrim(img1, height_px=380, max_alpha=190)

# DỌA DẪM - Center Upper
draw_styled_text(img1, "DỌA DẪM", font_title_massive, 1920, 360, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=40)

# Bottom subtitle
draw_bottom_bar(img1, "Vì Sao Họ Phải Gieo Rắc Nỗi Sợ?", font_sub_titlecase, 1920, 1990, 2075, line_width=2400)

out1_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v3_doa_dam_spooky_closeup_4k.jpg")
img1.convert("RGB").save(out1_4k, quality=98, subsampling=0)
shutil.copy(out1_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v3_doa_dam_spooky_closeup_4k.jpg"))

# =========================================================================
# 2. RENDER OPTION 2 (SPOOKY GRAND CHAMBER / HÙ DỌA ĐIỀU TRẦN TOÀN CẢNH)
# =========================================================================
print("Rendering Spooky Variant 2 (Grand Chamber)...")
img2 = Image.open(BG_SPOOKY_4).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
apply_bottom_scrim(img2, height_px=380, max_alpha=190)

# DỌA DẪM - Center Upper (positioned slightly lower to fit high ceiling)
draw_styled_text(img2, "DỌA DẪM", font_title_massive, 1920, 430, is_gradient=True, 
                 top_color=(255, 225, 0), bottom_color=(255, 60, 0), stroke_width=40)

# Bottom subtitle
draw_bottom_bar(img2, "Vì Sao Họ Phải Gieo Rắc Nỗi Sợ?", font_sub_titlecase, 1920, 1990, 2075, line_width=2400)

out2_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v4_doa_dam_spooky_chamber_4k.jpg")
img2.convert("RGB").save(out2_4k, quality=98, subsampling=0)
shutil.copy(out2_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v4_doa_dam_spooky_chamber_4k.jpg"))

print("Successfully rendered Spooky 4K thumbnails!")
