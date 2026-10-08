import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_IMAGE = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/aves-khoi-nghiep-xe-dien/thumbnails/clean_plate_pnv_thanh.jpg"
FONT_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"
OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/aves-khoi-nghiep-xe-dien/thumbnails"
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
                     top_color=(255, 235, 0), bottom_color=(255, 65, 0), 
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

def draw_bottom_bar_gold_line(base_img, text, font, center_x, center_y, line_y, line_width=2400):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    # Dual layer glowing gold accent line
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.6))
        color = (255, 215, 64, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 8)], fill=color)
    
    # Text with sharp black outline
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     solid_color=(255, 255, 255),
                     stroke_width=18, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 12), shadow_blur=14)

def draw_bottom_bar_badge(base_img, text, font, center_x, center_y, pad_x=60, pad_y=24):
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
    
    # Badge backdrop layer (Semi-translucent black with red/gold border)
    badge_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge_layer)
    
    # Drop shadow of badge
    bdraw.rounded_rectangle([x0 - 4, y0 + 6, x1 + 4, y1 + 14], radius=24, fill=(0, 0, 0, 220))
    badge_layer = badge_layer.filter(ImageFilter.GaussianBlur(12))
    base_img.alpha_composite(badge_layer)
    
    # Badge body
    badge_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bbdraw = ImageDraw.Draw(badge_body)
    bbdraw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(10, 15, 22, 230), outline=(255, 215, 64, 255), width=4)
    base_img.alpha_composite(badge_body)
    
    # Text
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=16, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 10), shadow_blur=12)

def main():
    print("Loading clean base plate...")
    raw_base = Image.open(BASE_IMAGE).convert("RGBA")
    base_4k = raw_base.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # Shared Fonts
    f1 = ImageFont.truetype(FONT_PATH, 225)
    f2 = ImageFont.truetype(FONT_PATH, 185)
    
    # -------------------------------------------------------------
    # VARIANT A: Thanh Accent Line Vàng Kim (Chuẩn Mẫu BYD)
    # Tiêu đề phụ: TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN?
    # -------------------------------------------------------------
    print("Rendering Variant A (Thanh Line Vàng Kim - Chuẩn BYD)...")
    imgA = base_4k.copy()
    draw_styled_text(imgA, "AVES VS VINFAST", f1, 1920, 165, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    draw_styled_text(imgA, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 375, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    
    fsub_a = ImageFont.truetype(FONT_PATH, 78)
    draw_bottom_bar_gold_line(imgA, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN?", fsub_a, 1920, 1940, 2030, line_width=2550)
    
    outA_4k = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_goldline_4k.jpg")
    outA_1080 = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_goldline_1080p.jpg")
    rgbA = imgA.convert("RGB")
    rgbA.save(outA_4k, quality=98, subsampling=0)
    rgbA.resize((1920, 1080), Image.Resampling.LANCZOS).save(outA_1080, quality=98, subsampling=0)
    print(f"Saved Variant A: {outA_4k} and {outA_1080}")

    # -------------------------------------------------------------
    # VARIANT B: Khung Badge Bo Góc Sang Trọng (Chuẩn Mẫu Phú Quốc)
    # Tiêu đề phụ: TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN
    # -------------------------------------------------------------
    print("Rendering Variant B (Badge Bo Góc Sang Trọng - Chuẩn Phú Quốc)...")
    imgB = base_4k.copy()
    draw_styled_text(imgB, "AVES VS VINFAST", f1, 1920, 165, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    draw_styled_text(imgB, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 375, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    
    fsub_b = ImageFont.truetype(FONT_PATH, 76)
    draw_bottom_bar_badge(imgB, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY TƯỚNG CŨ LẬP TIỀN ĐỒN", fsub_b, 1920, 1950, pad_x=70, pad_y=26)
    
    outB_4k = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_badge_4k.jpg")
    outB_1080 = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_badge_1080p.jpg")
    rgbB = imgB.convert("RGB")
    rgbB.save(outB_4k, quality=98, subsampling=0)
    rgbB.resize((1920, 1080), Image.Resampling.LANCZOS).save(outB_1080, quality=98, subsampling=0)
    print(f"Saved Variant B: {outB_4k} and {outB_1080}")

    # -------------------------------------------------------------
    # VARIANT C: Titlecase Thanh Lịch Báo Chí (Chuẩn The Economist / Bloomberg)
    # Tiêu đề phụ: Tướng Cũ Đánh Thành Cũ Hay Tướng Cũ Lập Tiền Đồn?
    # -------------------------------------------------------------
    print("Rendering Variant C (Titlecase Thanh Lịch)...")
    imgC = base_4k.copy()
    draw_styled_text(imgC, "AVES VS VINFAST", f1, 1920, 165, is_gradient=True,
                     top_color=(255, 235, 0), bottom_color=(255, 60, 0),
                     stroke_width=32, shadow_offset=(0, 22), shadow_blur=20)
    
    draw_styled_text(imgC, "ĐỐI TÁC HAY ĐỐI THỦ", f2, 1920, 375, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=30, shadow_offset=(0, 20), shadow_blur=18)
    
    fsub_c = ImageFont.truetype(FONT_PATH, 80)
    draw_bottom_bar_gold_line(imgC, "Tướng Cũ Đánh Thành Cũ Hay Tướng Cũ Lập Tiền Đồn?", fsub_c, 1920, 1940, 2030, line_width=2550)
    
    outC_4k = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_titlecase_4k.jpg")
    outC_1080 = os.path.join(OUTPUT_DIR, "thumbnail_pnv_vs_thanh_titlecase_1080p.jpg")
    rgbC = imgC.convert("RGB")
    rgbC.save(outC_4k, quality=98, subsampling=0)
    rgbC.resize((1920, 1080), Image.Resampling.LANCZOS).save(outC_1080, quality=98, subsampling=0)
    print(f"Saved Variant C: {outC_4k} and {outC_1080}")

    print("All renders complete successfully!")

if __name__ == "__main__":
    main()
