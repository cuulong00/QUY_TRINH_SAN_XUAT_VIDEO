import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PLATE_1 = "/Users/pro16/.gemini/antigravity/brain/3b74c390-c043-4563-8882-01f2d464d8f8/aves_vf_real_v1_1790042427499.jpg"
PLATE_2 = "/Users/pro16/.gemini/antigravity/brain/3b74c390-c043-4563-8882-01f2d464d8f8/aves_vf_real_v2_1790042461759.jpg"
FONT_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/aves-khoi-nghiep-xe-dien/thumbnails"
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
                     solid_color=(255, 255, 255), stroke_width=34, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=22, shadow_color=(0, 0, 0, 255)):
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

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=1850):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    # Luminous burnished gold line
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.6))
        color = (255, 215, 64, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 8)], fill=color)
    
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     stroke_width=18, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 12), shadow_blur=14)

def process_plate(plate_path, prefix, titlecase_sub=True):
    raw = Image.open(plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    f1 = ImageFont.truetype(FONT_PATH, 225)
    f2 = ImageFont.truetype(FONT_PATH, 185)
    
    # Line 1: AVES VS VINFAST (Gradient Yellow -> Orange)
    draw_styled_text(img, "AVES VS VINFAST", f1, 1920, 175, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=34, shadow_offset=(0, 24), shadow_blur=22)
    
    # Line 2: ĐỐI TÁC HAY ĐỐI THỦ (Pure White)
    draw_styled_text(img, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 390, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    if titlecase_sub:
        fsub = ImageFont.truetype(FONT_PATH, 92)
        draw_bottom_bar(img, "Cùng Nuốt Trọn 84 Triệu Xe Xăng?", fsub, 1920, 1940, 2030, line_width=1850)
    else:
        fsub = ImageFont.truetype(FONT_PATH, 86)
        draw_bottom_bar(img, "CÙNG NUỐT TRỌN 84 TRIỆU XE XĂNG?", fsub, 1920, 1940, 2030, line_width=1950)
        
    out_4k = os.path.join(OUTPUT_DIR, f"{prefix}_4k.jpg")
    out_1080 = os.path.join(OUTPUT_DIR, f"{prefix}_1080p.jpg")
    rgb = img.convert("RGB")
    rgb.save(out_4k, quality=98, subsampling=0)
    rgb.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_1080, quality=98, subsampling=0)
    print(f"Generated: {out_1080}")

def main():
    print("Processing Photorealistic Plate 2 (Fiery Raging Flame Borders - Gold Standard)...")
    process_plate(PLATE_2, "thumbnail_photorealistic_v2_titlecase", titlecase_sub=True)
    process_plate(PLATE_2, "thumbnail_photorealistic_v2_uppercase", titlecase_sub=False)
    
    print("Processing Photorealistic Plate 1 (Charging Station & Energy Beam)...")
    process_plate(PLATE_1, "thumbnail_photorealistic_v1_titlecase", titlecase_sub=True)
    
    # Also overwrite the canonical thumbnail files with Plate 2 (The absolute gold standard)
    shutil.copy(os.path.join(OUTPUT_DIR, "thumbnail_photorealistic_v2_titlecase_4k.jpg"),
                os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_4k.jpg"))
    shutil.copy(os.path.join(OUTPUT_DIR, "thumbnail_photorealistic_v2_titlecase_1080p.jpg"),
                os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_1080p.jpg"))
    shutil.copy(os.path.join(OUTPUT_DIR, "thumbnail_photorealistic_v2_uppercase_4k.jpg"),
                os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_variant_b_4k.jpg"))
    shutil.copy(os.path.join(OUTPUT_DIR, "thumbnail_photorealistic_v2_uppercase_1080p.jpg"),
                os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_variant_b_1080p.jpg"))
    shutil.copy(PLATE_2, os.path.join(OUTPUT_DIR, "thumbnail_clean_plate.jpg"))
    
    print("All photorealistic thumbnails rendered successfully!")

if __name__ == "__main__":
    main()
