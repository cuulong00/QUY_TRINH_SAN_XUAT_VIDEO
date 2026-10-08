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

def draw_semi_trans_framed_subtitle(base_img, text, font, center_x, center_y,
                                   bg_alpha=0.6, bg_color=(8, 14, 28),
                                   border_color=(255, 87, 34, 255), border_width=6,
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
    
    # 2. Outer Glow around border
    if glow_border:
        glow_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_layer)
        glow_color = (border_color[0], border_color[1], border_color[2], 140)
        gdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, outline=glow_color, width=border_width + 8)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(12))
        base_img.alpha_composite(glow_layer)
        
    # 3. Semi-transparent Pill Body (alpha = 0.6 -> int(255 * 0.6) = 153)
    alpha_int = int(255 * bg_alpha)
    fill_rgba = (bg_color[0], bg_color[1], bg_color[2], alpha_int)
    
    pill_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pill_body)
    pdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_rgba, outline=border_color, width=border_width)
    base_img.alpha_composite(pill_body)
    
    # 4. Text inside pill with crisp stroke and shadow
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=text_color, stroke_width=text_stroke_width, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 4), shadow_blur=6)

PLATE_V2_TSHIRT = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_tshirt_titans_v2_1789863751552.jpg"
PLATE_V1_TSHIRT = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5/thumb_tshirt_titans_v1_1789863716097.jpg"

font_title = ImageFont.truetype(FONT_PATH, 400)
font_sub = ImageFont.truetype(FONT_PATH, 92)

SUBTITLE_TEXT = "VÌ SAO GIỚI CHÓP BU PHẢI GIEO RẮC NỖI SỢ?"
SUB_Y_20PCT = 1710  # 20.8% from bottom edge

# =========================================================================
# V10: Plate 2 (Full Brand Names on T-Shirts) + Fiery Orange Frame (Alpha 0.6)
# =========================================================================
print("Rendering V10: Plate 2 + Fiery Orange Frame (Alpha 0.6)...")
im10 = Image.open(PLATE_V2_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
draw_styled_text(im10, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)
draw_semi_trans_framed_subtitle(im10, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                                bg_alpha=0.6, bg_color=(10, 16, 30),
                                border_color=(255, 87, 34, 255), border_width=6, glow_border=True)
out10 = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v10_doa_dam_tshirt_orange_4k.jpg")
im10.convert("RGB").save(out10, quality=98, subsampling=0)
shutil.copy(out10, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v10_doa_dam_tshirt_orange_4k.jpg"))

# =========================================================================
# V11: Plate 2 (Full Brand Names on T-Shirts) + Golden Amber Frame (Alpha 0.6)
# =========================================================================
print("Rendering V11: Plate 2 + Golden Amber Frame (Alpha 0.6)...")
im11 = Image.open(PLATE_V2_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
draw_styled_text(im11, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)
draw_semi_trans_framed_subtitle(im11, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                                bg_alpha=0.6, bg_color=(10, 16, 30),
                                border_color=(255, 193, 7, 255), border_width=6, glow_border=True)
out11 = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v11_doa_dam_tshirt_gold_4k.jpg")
im11.convert("RGB").save(out11, quality=98, subsampling=0)
shutil.copy(out11, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v11_doa_dam_tshirt_gold_4k.jpg"))

# =========================================================================
# V12: Plate 1 (Icon T-Shirts) + Fiery Orange Frame (Alpha 0.6)
# =========================================================================
print("Rendering V12: Plate 1 (Icon T-Shirts) + Fiery Orange Frame (Alpha 0.6)...")
im12 = Image.open(PLATE_V1_TSHIRT).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
draw_styled_text(im12, "DỌA DẪM", font_title, 1920, 290, is_gradient=True, 
                 top_color=(255, 230, 0), bottom_color=(255, 60, 0), stroke_width=40)
draw_semi_trans_framed_subtitle(im12, SUBTITLE_TEXT, font_sub, 1920, SUB_Y_20PCT,
                                bg_alpha=0.6, bg_color=(10, 16, 30),
                                border_color=(255, 87, 34, 255), border_width=6, glow_border=True)
out12 = os.path.join(OUTPUT_DIR_I2V, "thumbnail_v12_doa_dam_tshirt_plate1_4k.jpg")
im12.convert("RGB").save(out12, quality=98, subsampling=0)
shutil.copy(out12, os.path.join(OUTPUT_DIR_CLASSIC, "thumbnail_v12_doa_dam_tshirt_plate1_4k.jpg"))

print("Successfully rendered all 4K production thumbnails (V10, V11, V12)!")
