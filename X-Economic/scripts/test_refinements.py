import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_IMAGE = "/Users/pro16/.gemini/antigravity/brain/3b74c390-c043-4563-8882-01f2d464d8f8/aves_vinfast_thumb_1790005047121.jpg"
FONT_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/aves-khoi-nghiep-xe-dien/thumbnails"

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
                     solid_color=(255, 255, 255), stroke_width=32, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 22), shadow_blur=22, shadow_color=(0, 0, 0, 255)):
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

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=1800):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    # Dual layer glowing gold accent line
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.6))
        # Warm luminous gold: #FFC107 to #FFD54F
        color = (255, 215, 64, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 8)], fill=color)
    
    # Text with sharp black outline
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     stroke_width=18, stroke_color=(0,0,0),
                     shadow_offset=(0, 12), shadow_blur=14)

def run():
    base = Image.open(BASE_IMAGE).convert("RGBA").resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # Let's test Variant A: Balanced Headline
    imgA = base.copy()
    f1 = ImageFont.truetype(FONT_PATH, 225)
    f2 = ImageFont.truetype(FONT_PATH, 185)
    fsub = ImageFont.truetype(FONT_PATH, 94)
    
    draw_styled_text(imgA, "AVES VS VINFAST", f1, 1920, 165, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    draw_styled_text(imgA, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 375, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    
    draw_bottom_bar(imgA, "Cùng Nuốt Trọn 84 Triệu Xe Xăng?", fsub, 1920, 1940, 2030, line_width=1850)
    
    outA_1080 = os.path.join(OUTPUT_DIR, "thumb_variant_A_1080p.jpg")
    imgA.convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS).save(outA_1080, quality=96)
    print("Saved Variant A")

    # Let's test Variant B: With "VS" highlighted or stylized
    imgB = base.copy()
    # In Variant B, let's test UPPERCASE Subtitle for maximum mobile legibility: "CÙNG NUỐT TRỌN 84 TRIỆU XE XĂNG?"
    draw_styled_text(imgB, "AVES VS VINFAST", f1, 1920, 165, is_gradient=True,
                     top_color=(255, 240, 0), bottom_color=(255, 70, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    draw_styled_text(imgB, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 375, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    
    fsub_b = ImageFont.truetype(FONT_PATH, 88)
    draw_bottom_bar(imgB, "CÙNG NUỐT TRỌN 84 TRIỆU XE XĂNG?", fsub_b, 1920, 1940, 2030, line_width=1950)
    
    outB_1080 = os.path.join(OUTPUT_DIR, "thumb_variant_B_1080p.jpg")
    imgB.convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS).save(outB_1080, quality=96)
    print("Saved Variant B")

run()
