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
                     top_color=(255, 230, 0), bottom_color=(255, 60, 0), 
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

def draw_transparent_subtitle(base_img, text, font, center_x, center_y,
                              text_color=(255, 255, 255), stroke_width=14, stroke_color=(0, 0, 0),
                              shadow_blur=20, shadow_offset=(0, 8), add_subtle_scrim=True):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    x = int(center_x - w / 2 - bbox[0])
    y = int(center_y - h / 2 - bbox[1])
    
    # Subtle soft dark gradient scrim behind text for flawless legibility without boxiness
    if add_subtle_scrim:
        scrim = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(scrim)
        pad_x = 140
        pad_y = 35
        x0 = center_x - w // 2 - pad_x
        y0 = center_y - h // 2 - pad_y
        x1 = center_x + w // 2 + pad_x
        y1 = center_y + h // 2 + pad_y
        # Soft dark oval/capsule with high blur
        sdraw.rounded_rectangle([x0, y0, x1, y1], radius=35, fill=(0, 0, 0, 150))
        scrim = scrim.filter(ImageFilter.GaussianBlur(28))
        base_img.alpha_composite(scrim)
        
    # Deep Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sdraw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, 
               fill=(0, 0, 0, 255), stroke_width=stroke_width + 16, stroke_fill=(0, 0, 0, 255))
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
    base_img.alpha_composite(shadow_img)
    
    # Stroke
    stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(stroke_img)
    kdraw.text((x, y), text, font=font, fill=stroke_color, stroke_width=stroke_width, stroke_fill=stroke_color)
    base_img.alpha_composite(stroke_img)
    
    # Fill (Pure White)
    fill_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    fdraw = ImageDraw.Draw(fill_img)
    fdraw.text((x, y), text, font=font, fill=text_color)
    base_img.alpha_composite(fill_img)

PLATE_V1_TSHIRT = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_tshirt_titans_v1_1789863716097.jpg"
PLATE_V2_TSHIRT = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_tshirt_titans_v2_1789863751552.jpg"

font_title = ImageFont.truetype(FONT_PATH, 400)
font_sub = ImageFont.truetype(FONT_PATH, 92)

SUBTITLE_TEXT = "VÌ SAO GIỚI CHÓP BU PHẢI GIEO RẮC NỖI SỢ?"

# Position for subtitle: 20% from bottom edge (2160 * 0.80 = 1728)
# At 1700-1728, it sits right at ~20-21% from bottom edge, perfectly balanced above the people!
SUB_Y_20PCT = 1710

# =========================================================================
# THUMBNAIL V10: DUAL TITANS IN T-SHIRTS (PLATE 2 - OPENAI & ANTHROPIC LOGOS ON SHIRTS)
# =========================================================================
print("Rendering Thumbnail V10 (Plate 2 with T-shirts, transparent bottom subtitle)...")
img10 = Image.open(PLATE_V2_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

# Headline DỌA DẪM at top center
draw_styled_text(img10, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)

# Subtitle at bottom (~20% from bottom edge) with transparent background
draw_transparent_subtitle(img10, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                          text_color=(255, 255, 255), stroke_width=14)

out10_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v10_doa_dam_tshirt_titans_4k.jpg")
img10.convert("RGB").save(out10_4k, quality=98, subsampling=0)
shutil.copy(out10_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v10_doa_dam_tshirt_titans_4k.jpg"))

# =========================================================================
# THUMBNAIL V11: DUAL TITANS IN T-SHIRTS (PLATE 1 - LOGO ICONS ON SHIRTS)
# =========================================================================
print("Rendering Thumbnail V11 (Plate 1 with T-shirts, transparent bottom subtitle)...")
img11 = Image.open(PLATE_V1_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

# Headline DỌA DẪM at top center
draw_styled_text(img11, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)

# Subtitle at bottom (~20% from bottom edge) with transparent background
draw_transparent_subtitle(img11, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                          text_color=(255, 255, 255), stroke_width=14)

out11_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v11_doa_dam_tshirt_titans_4k.jpg")
img11.convert("RGB").save(out11_4k, quality=98, subsampling=0)
shutil.copy(out11_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v11_doa_dam_tshirt_titans_4k.jpg"))

# =========================================================================
# THUMBNAIL V12: PURE TRANSPARENT (NO SCRIM AT ALL, STRICTLY RAW TEXT + SHADOW)
# =========================================================================
print("Rendering Thumbnail V12 (Plate 2 with strictly raw transparent subtitle)...")
img12 = Image.open(PLATE_V2_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)

draw_styled_text(img12, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)

draw_transparent_subtitle(img12, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                          text_color=(255, 255, 255), stroke_width=14, add_subtle_scrim=False)

out12_4k = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v12_doa_dam_tshirt_rawtrans_4k.jpg")
img12.convert("RGB").save(out12_4k, quality=98, subsampling=0)
shutil.copy(out12_4k, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v12_doa_dam_tshirt_rawtrans_4k.jpg"))

print("All T-shirt 4K thumbnails (v10, v11, v12) rendered successfully!")
