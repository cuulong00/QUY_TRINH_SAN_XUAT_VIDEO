import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/aves-khoi-nghiep-xe-dien/thumbnails"
FONT_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0), 
                     solid_color=(255, 255, 255), stroke_width=32, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 22), shadow_blur=20, shadow_color=(0, 0, 0, 255)):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
    # 1. Heavy Black Drop Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sx = x + shadow_offset[0]
    sy = y + shadow_offset[1]
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 16, stroke_fill=shadow_color)
    if shadow_blur > 0:
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
    base_img.alpha_composite(shadow_img)
    
    # 2. Crisp Black Stroke
    stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(stroke_img)
    kdraw.text((x, y), text, font=font, fill=stroke_color, stroke_width=stroke_width, stroke_fill=stroke_color)
    base_img.alpha_composite(stroke_img)
    
    # 3. Fill
    if is_gradient:
        pad = stroke_width * 2 + 80
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

def draw_bottom_gold_line(base_img, text, font, center_x, center_y, line_y, line_width=2500):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.6))
        color = (255, 215, 64, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 8)], fill=color)
    
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     solid_color=(255, 255, 255),
                     stroke_width=18, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 12), shadow_blur=14)

def draw_bottom_badge(base_img, text, font, center_x, center_y, pad_x=70, pad_y=26):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=16)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    badge_w = text_w + pad_x * 2
    badge_h = text_h + pad_y * 2
    x0 = int(center_x - badge_w / 2)
    y0 = int(center_y - badge_h / 2)
    x1 = x0 + badge_w
    y1 = y0 + badge_h
    
    badge_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge_layer)
    bdraw.rounded_rectangle([x0 - 4, y0 + 6, x1 + 4, y1 + 14], radius=24, fill=(0, 0, 0, 220))
    badge_layer = badge_layer.filter(ImageFilter.GaussianBlur(12))
    base_img.alpha_composite(badge_layer)
    
    badge_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bbdraw = ImageDraw.Draw(badge_body)
    bbdraw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(10, 15, 22, 230), outline=(255, 215, 64, 255), width=4)
    base_img.alpha_composite(badge_body)
    
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=16, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 10), shadow_blur=12)

def render_concept(base_path, prefix, title_y1=165, title_y2=375, sub_y=1940, line_y=2030):
    print(f"--- Rendering: {prefix} ---")
    raw = Image.open(base_path).convert("RGBA")
    base_4k = raw.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    f1 = ImageFont.truetype(FONT_PATH, 225)
    f2 = ImageFont.truetype(FONT_PATH, 185)
    f_sub = ImageFont.truetype(FONT_PATH, 78)
    
    # 1. Gold Line Variant
    img_line = base_4k.copy()
    draw_styled_text(img_line, "AVES VS VINFAST", f1, 1920, title_y1, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    draw_styled_text(img_line, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, title_y2, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    draw_bottom_gold_line(img_line, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN?", f_sub, 1920, sub_y, line_y, line_width=2550)
    
    out_4k_line = os.path.join(OUTPUT_DIR, f"{prefix}_goldline_4k.jpg")
    out_1080_line = os.path.join(OUTPUT_DIR, f"{prefix}_goldline_1080p.jpg")
    rgb_line = img_line.convert("RGB")
    rgb_line.save(out_4k_line, quality=98, subsampling=0)
    rgb_line.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_1080_line, quality=98, subsampling=0)
    print(f"Saved: {out_1080_line}")

    # 2. Badge Variant
    img_badge = base_4k.copy()
    draw_styled_text(img_badge, "AVES VS VINFAST", f1, 1920, title_y1, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    draw_styled_text(img_badge, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, title_y2, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    draw_bottom_badge(img_badge, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN", f_sub, 1920, sub_y + 10)
    
    out_4k_badge = os.path.join(OUTPUT_DIR, f"{prefix}_badge_4k.jpg")
    out_1080_badge = os.path.join(OUTPUT_DIR, f"{prefix}_badge_1080p.jpg")
    rgb_badge = img_badge.convert("RGB")
    rgb_badge.save(out_4k_badge, quality=98, subsampling=0)
    rgb_badge.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_1080_badge, quality=98, subsampling=0)
    print(f"Saved: {out_1080_badge}")

def main():
    c1 = os.path.join(OUTPUT_DIR, "clean_plate_c1_citadel.jpg")
    c2 = os.path.join(OUTPUT_DIR, "clean_plate_c2_warroom.jpg")
    c3 = os.path.join(OUTPUT_DIR, "clean_plate_c3_editorial.jpg")
    
    render_concept(c1, "concept_1_citadel", title_y1=165, title_y2=375, sub_y=1940, line_y=2030)
    render_concept(c2, "concept_2_warroom", title_y1=180, title_y2=390, sub_y=1950, line_y=2035)
    render_concept(c3, "concept_3_editorial", title_y1=165, title_y2=375, sub_y=1940, line_y=2030)
    print("ALL 3 CREATIVE CONCEPTS RENDERED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
