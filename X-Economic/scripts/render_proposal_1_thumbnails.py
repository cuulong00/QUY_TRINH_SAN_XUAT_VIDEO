import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BRAIN_DIR = "/Users/pro16/.gemini/antigravity/brain/7ab0dbd3-29ef-4a68-85fe-92e8fe846dd5"
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
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255),
                     outer_glow_color=None, outer_glow_blur=24):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
    if outer_glow_color:
        glow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_img)
        gdraw.text((x, y), text, font=font, fill=outer_glow_color, 
                   stroke_width=stroke_width + 20, stroke_fill=outer_glow_color)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(outer_glow_blur))
        base_img.alpha_composite(glow_img)
    
    # Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sx = x + shadow_offset[0]
    sy = y + shadow_offset[1]
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 16, stroke_fill=shadow_color)
    if shadow_blur > 0:
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
    base_img.alpha_composite(shadow_img)
    
    # Stroke
    stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(stroke_img)
    kdraw.text((x, y), text, font=font, fill=stroke_color, stroke_width=stroke_width, stroke_fill=stroke_color)
    base_img.alpha_composite(stroke_img)
    
    # Fill
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
                                   bg_alpha=0.65, bg_color=(8, 14, 28),
                                   border_color=(255, 100, 0, 255), border_width=6,
                                   text_color=(255, 255, 255), text_stroke_width=10,
                                   pad_x=75, pad_y=24, radius=24, glow_border=True,
                                   glow_color=None):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=text_stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x0 = int(center_x - text_w / 2 - pad_x)
    y0 = int(center_y - text_h / 2 - pad_y)
    x1 = int(center_x + text_w / 2 + pad_x)
    y1 = int(center_y + text_h / 2 + pad_y)
    
    # Outer Box Shadow
    box_shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bsdraw = ImageDraw.Draw(box_shadow)
    bsdraw.rounded_rectangle([x0 - 4, y0 + 4, x1 + 4, y1 + 16], radius=radius + 4, fill=(0, 0, 0, 220))
    box_shadow = box_shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(box_shadow)
    
    # Glow Border
    if glow_border:
        glow_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_layer)
        gc = glow_color if glow_color else (border_color[0], border_color[1], border_color[2], 170)
        gdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, outline=gc, width=border_width + 8)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(14))
        base_img.alpha_composite(glow_layer)
        
    # Semi-transparent Body
    alpha_int = int(255 * bg_alpha)
    fill_rgba = (bg_color[0], bg_color[1], bg_color[2], alpha_int)
    
    body_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(body_layer)
    bdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_rgba, outline=border_color, width=border_width)
    base_img.alpha_composite(body_layer)
    
    # Text inside frame
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=text_color, stroke_width=text_stroke_width, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 4), shadow_blur=6)

# Render process
LINE1 = "HỌ SỢ PHÁ SẢN"
LINE2 = "KHÔNG SỢ TẬN THẾ!"
SUBTITLE = "MÀN KỊCH ĐỘC QUYỀN CỦA GIỚI CHÓP BU AI"

font_line1 = ImageFont.truetype(FONT_PATH, 310)
font_line2 = ImageFont.truetype(FONT_PATH, 310)
font_sub = ImageFont.truetype(FONT_PATH, 84)

PLATES = [
    {
        "id": "thumbnail_de_xuat_1_senate_noir_4k",
        "plate": os.path.join(BRAIN_DIR, "thumb_pha_san_senate_1789955511180.jpg"),
        "title_top": (255, 245, 0),
        "title_bot": (255, 45, 0),
        "glow": (255, 80, 0, 100),
        "border": (255, 100, 0, 255),
        "bg_color": (10, 10, 20),
        "enhance_color": 1.10,
        "enhance_contrast": 1.06,
        "y1": 270,
        "y2": 580,
        "y_sub": 1730
    },
    {
        "id": "thumbnail_de_xuat_1_mask_burn_4k",
        "plate": os.path.join(BRAIN_DIR, "thumb_pha_san_mask_1789955494723.jpg"),
        "title_top": (255, 240, 0),
        "title_bot": (255, 40, 0),
        "glow": (255, 100, 0, 100),
        "border": (255, 80, 0, 255),
        "bg_color": (12, 12, 22),
        "enhance_color": 1.10,
        "enhance_contrast": 1.05,
        "y1": 260,
        "y2": 570,
        "y_sub": 1730
    }
]

for p in PLATES:
    print(f"Rendering {p['id']}...")
    raw_img = Image.open(p['plate']).convert('RGB')
    img_4k = raw_img.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    if p.get("enhance_color", 1.0) != 1.0:
        img_4k = ImageEnhance.Color(img_4k).enhance(p["enhance_color"])
    if p.get("enhance_contrast", 1.0) != 1.0:
        img_4k = ImageEnhance.Contrast(img_4k).enhance(p["enhance_contrast"])
        
    canvas = img_4k.convert('RGBA')
    
    # Draw Line 1: HỌ SỢ PHÁ SẢN (Gradient Gold -> Fiery Orange)
    draw_styled_text(canvas, LINE1, font_line1, center_x=1920, center_y=p['y1'],
                     is_gradient=True, top_color=p['title_top'], bottom_color=p['title_bot'],
                     stroke_width=38, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255),
                     outer_glow_color=p['glow'], outer_glow_blur=24)
                     
    # Draw Line 2: KHÔNG SỢ TẬN THẾ! (Pure Solid White)
    draw_styled_text(canvas, LINE2, font_line2, center_x=1920, center_y=p['y2'],
                     is_gradient=False, solid_color=(255, 255, 255),
                     stroke_width=38, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255),
                     outer_glow_color=(0, 0, 0, 180), outer_glow_blur=16)
                     
    # Draw Subtitle Bar at bottom center
    draw_semi_trans_framed_subtitle(canvas, SUBTITLE, font_sub, center_x=1920, center_y=p['y_sub'],
                                   bg_alpha=0.65, bg_color=p['bg_color'],
                                   border_color=p['border'], border_width=6,
                                   text_color=(255, 255, 255), text_stroke_width=10,
                                   pad_x=70, pad_y=24, radius=24, glow_border=True)
                                   
    final_rgb = canvas.convert('RGB')
    
    # Save to Brain
    brain_path = os.path.join(BRAIN_DIR, f"{p['id']}.jpg")
    final_rgb.save(brain_path, format="JPEG", quality=96)
    
    # Save to Episodes
    ep_i2v = os.path.join(OUTPUT_DIR_I2V, f"{p['id']}.jpg")
    ep_cla = os.path.join(OUTPUT_DIR_CLASSIC, f"{p['id']}.jpg")
    shutil.copy2(brain_path, ep_i2v)
    shutil.copy2(brain_path, ep_cla)
    print(f"Successfully saved {p['id']} to {brain_path}")
