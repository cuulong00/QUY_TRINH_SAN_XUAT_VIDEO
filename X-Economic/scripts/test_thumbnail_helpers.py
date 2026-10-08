import os
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
                             pill_bg=(15, 23, 42, 230), border_color=(255, 87, 34, 255),
                             text_color=(255, 255, 255), stroke_width=12):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    pad_x = 80
    pad_y = 36
    x0 = int(center_x - text_w / 2 - pad_x)
    y0 = int(center_y - text_h / 2 - pad_y)
    x1 = int(center_x + text_w / 2 + pad_x)
    y1 = int(center_y + text_h / 2 + pad_y)
    radius = (y1 - y0) // 2
    
    # Pill overlay
    pill = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pill)
    
    # Outer glow / shadow
    shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([x0 - 6, y0 - 4, x1 + 6, y1 + 16], radius=radius + 6, fill=(0, 0, 0, 220))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(shadow)
    
    # Pill body & border
    pdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=pill_bg, outline=border_color, width=5)
    base_img.alpha_composite(pill)
    
    # Text
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=text_color, stroke_width=stroke_width, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 6), shadow_blur=8)

def add_brand_badge(base_img, logo_path, center_x, center_y, target_h=90, 
                    badge_title="", font_label=None, is_left=True):
    logo = Image.open(logo_path).convert("RGBA")
    aspect = logo.width / logo.height
    new_w = int(target_h * aspect)
    logo = logo.resize((new_w, target_h), Image.Resampling.LANCZOS)
    
    pad_x = 40
    pad_y = 20
    badge_w = new_w + pad_x * 2
    badge_h = target_h + pad_y * 2
    
    x0 = center_x - badge_w // 2
    y0 = center_y - badge_h // 2
    x1 = x0 + badge_w
    y1 = y0 + badge_h
    radius = 24
    
    # Badge backdrop
    badge_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge_layer)
    # Shadow
    bdraw.rounded_rectangle([x0-4, y0-2, x1+4, y1+10], radius=radius+4, fill=(0, 0, 0, 180))
    badge_layer = badge_layer.filter(ImageFilter.GaussianBlur(12))
    base_img.alpha_composite(badge_layer)
    
    # Body
    badge_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bbdraw = ImageDraw.Draw(badge_body)
    border_col = (255, 214, 0, 220) if is_left else (255, 87, 34, 220)
    bbdraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=(15, 23, 42, 210), outline=border_col, width=3)
    base_img.alpha_composite(badge_body)
    
    # Paste logo
    lx = x0 + pad_x
    ly = y0 + pad_y
    base_img.alpha_composite(logo, (lx, ly))

print("Helper functions defined successfully.")
