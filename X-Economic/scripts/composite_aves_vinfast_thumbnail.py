import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_IMAGE = "/Users/pro16/.gemini/antigravity/brain/3b74c390-c043-4563-8882-01f2d464d8f8/aves_vinfast_thumb_1790005047121.jpg"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/aves-khoi-nghiep-xe-dien/thumbnails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
                     top_color=(255, 214, 0), bottom_color=(255, 87, 34), 
                     solid_color=(255, 255, 255), stroke_width=32, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 20), shadow_blur=18, shadow_color=(0, 0, 0, 255)):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
    # 1. Heavy Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sx = x + shadow_offset[0]
    sy = y + shadow_offset[1]
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 12, stroke_fill=shadow_color)
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

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=1700):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    # Draw glowing gold accent line
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.8))
        color = (255, 204, 51, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 6)], fill=color)
    
    # Text
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     stroke_width=16, shadow_offset=(0, 10), shadow_blur=12)

def render():
    print("Loading base plate and resizing to 4K (3840x2160)...")
    base = Image.open(BASE_IMAGE).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # Fonts
    font_l1 = ImageFont.truetype(FONT_PATH, 250)
    font_l2 = ImageFont.truetype(FONT_PATH, 215)
    font_sub = ImageFont.truetype(FONT_PATH, 88)
    
    # Dòng 1: AVES VS VINFAST (Gradient Vàng chanh -> Cam lửa)
    print("Rendering Line 1: AVES VS VINFAST...")
    draw_styled_text(base, "AVES VS VINFAST", font_l1, 1920, 310, is_gradient=True,
                     top_color=(255, 220, 0), bottom_color=(255, 75, 20),
                     stroke_width=32, shadow_offset=(0, 20), shadow_blur=20)
    
    # Dòng 2: ĐỐI TÁC HAY ĐỐI THỦ (Pure White)
    print("Rendering Line 2: ĐỐI TÁC HAY ĐỐI THỦ...")
    draw_styled_text(base, "ĐỐI TÁC HAY ĐỐI THỦ", font_l2, 1920, 560, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 18), shadow_blur=18)
    
    # Bottom Subtitle: Cùng Nuốt Trọn 84 Triệu Xe Xăng?
    print("Rendering Subtitle: Cùng Nuốt Trọn 84 Triệu Xe Xăng?...")
    draw_bottom_bar(base, "Cùng Nuốt Trọn 84 Triệu Xe Xăng?", font_sub, 1920, 1940, 2025, line_width=1800)
    
    out_4k = os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_4k.jpg")
    out_1080p = os.path.join(OUTPUT_DIR, "thumbnail_aves_vs_vinfast_1080p.jpg")
    
    final_rgb = base.convert("RGB")
    final_rgb.save(out_4k, quality=98, subsampling=0)
    print(f"Saved 4K: {out_4k}")
    
    final_1080p = final_rgb.resize((1920, 1080), Image.Resampling.LANCZOS)
    final_1080p.save(out_1080p, quality=98, subsampling=0)
    print(f"Saved 1080p: {out_1080p}")

if __name__ == "__main__":
    render()
