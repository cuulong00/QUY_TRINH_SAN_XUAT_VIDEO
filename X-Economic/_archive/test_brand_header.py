import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_styled_logo(logo_img, target_color=(255, 255, 255), stroke_width=8, stroke_color=(0, 0, 0), shadow_offset=(0, 8), shadow_blur=10):
    # logo_img is RGBA where alpha defines the shape
    w, h = logo_img.size
    pad = stroke_width * 2 + shadow_blur * 2 + 30
    canvas_w = w + pad * 2
    canvas_h = h + pad * 2
    
    # 1. Shadow
    shadow = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
    s_alpha = logo_img.split()[3]
    # Expand alpha for stroke on shadow
    s_mask = s_alpha.filter(ImageFilter.MaxFilter(stroke_width * 2 + 1))
    s_fill = Image.new('RGBA', (w, h), (0, 0, 0, 220))
    shadow.paste(s_fill, (pad + shadow_offset[0], pad + shadow_offset[1]), s_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
    
    # 2. Black Stroke
    stroke_layer = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
    k_mask = s_alpha.filter(ImageFilter.MaxFilter(stroke_width * 2 + 1))
    k_fill = Image.new('RGBA', (w, h), stroke_color + (255,))
    stroke_layer.paste(k_fill, (pad, pad), k_mask)
    
    # 3. Main Fill
    fill_layer = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
    main_fill = Image.new('RGBA', (w, h), target_color + (255,))
    fill_layer.paste(main_fill, (pad, pad), s_alpha)
    
    # Composite together
    out = Image.alpha_composite(shadow, stroke_layer)
    out = Image.alpha_composite(out, fill_layer)
    
    # Crop tight with some padding
    bbox = out.getbbox()
    return out.crop(bbox), (pad, pad)

print("Helper defined")
