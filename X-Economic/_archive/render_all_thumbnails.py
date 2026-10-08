import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/ngoai-giao-cay-tre/thumbnail"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_TAHOMA = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"

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
                     top_color=(255, 225, 0), bottom_color=(255, 69, 0), 
                     solid_color=(255, 255, 255), stroke_width=16, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 10), shadow_blur=10, shadow_color=(0, 0, 0, 240)):
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
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 6, stroke_fill=shadow_color)
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
        mask_img = Image.new('L', (text_w + stroke_width * 2 + 30, text_h + stroke_width * 2 + 30), 0)
        mdraw = ImageDraw.Draw(mask_img)
        mx = -bbox[0] + stroke_width + 15
        my = -bbox[1] + stroke_width + 15
        mdraw.text((mx, my), text, font=font, fill=255)
        
        grad = create_gradient(mask_img.width, mask_img.height, top_color, bottom_color)
        grad.putalpha(mask_img)
        
        paste_x = x + bbox[0] - stroke_width - 15
        paste_y = y + bbox[1] - stroke_width - 15
        base_img.paste(grad, (paste_x, paste_y), grad)
    else:
        fill_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        fdraw = ImageDraw.Draw(fill_img)
        fdraw.text((x, y), text, font=font, fill=solid_color)
        base_img.alpha_composite(fill_img)

def draw_bottom_bar(base_img, text, font, center_x, center_y, line_y, line_width=950):
    ldraw = ImageDraw.Draw(base_img)
    start_x = int(center_x - line_width / 2)
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(240 * factor)
        color = (255, 205, 50, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 3)], fill=color)
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, stroke_width=10)

# Paths to background assets
BG_PANORAMA = "/Users/pro16/.gemini/antigravity/brain/216ccfdc-88df-44b0-9abe-c2444a4b0591/thumb_v5_epic_panorama_1789549201141.jpg"
BG_FLAME = "/Users/pro16/.gemini/antigravity/brain/216ccfdc-88df-44b0-9abe-c2444a4b0591/thumb_v2_dynamic_flame_1789549152431.jpg"
BG_TECH = "/Users/pro16/.gemini/antigravity/brain/216ccfdc-88df-44b0-9abe-c2444a4b0591/thumb_v4_tech_resilience_1789549182712.jpg"

font_title1_pano = ImageFont.truetype(FONT_TAHOMA, 92)
font_title2_pano = ImageFont.truetype(FONT_TAHOMA, 75)
font_sub_pano = ImageFont.truetype(FONT_TAHOMA, 48)

font_title1_flame = ImageFont.truetype(FONT_TAHOMA, 88)
font_title2_flame = ImageFont.truetype(FONT_TAHOMA, 72)
font_sub_flame = ImageFont.truetype(FONT_TAHOMA, 46)

# =========================================================================
# 1. VERSION 1: PANORAMA MASTER (Khuyên dùng) - AI CÓ THỂ ÉP VIỆT NAM CHỌN BÊN?
# =========================================================================
print("Rendering V1 (Panorama Master)...")
img1 = Image.open(BG_PANORAMA).convert("RGBA").resize((1920, 1080), Image.Resampling.LANCZOS)
draw_styled_text(img1, "NGOẠI GIAO CÂY TRE", font_title1_pano, 1040, 130, is_gradient=True, stroke_width=16)
draw_styled_text(img1, "DĨ BẤT BIẾN — ỨNG VẠN BIẾN", font_title2_pano, 1040, 240, is_gradient=False, stroke_width=15)
draw_bottom_bar(img1, "AI CÓ THỂ ÉP VIỆT NAM CHỌN BÊN?", font_sub_pano, 755, 955, 1005, line_width=950)
v1_path = os.path.join(OUTPUT_DIR, "thumbnail_v1_panorama_ai_ep_viet_nam.jpg")
img1.convert("RGB").save(v1_path, quality=98, subsampling=0)

# Bản Master mặc định
shutil.copy(v1_path, os.path.join(OUTPUT_DIR, "thumbnail_master.jpg"))

# =========================================================================
# 2. VERSION 2: PANORAMA MASTER - CÂY TRE CÓ ĐỨNG VỮNG TRƯỚC SỨC ÉP CHỌN PHE?
# =========================================================================
print("Rendering V2 (Panorama - Câu hỏi cây tre đứng vững)...")
img2 = Image.open(BG_PANORAMA).convert("RGBA").resize((1920, 1080), Image.Resampling.LANCZOS)
draw_styled_text(img2, "NGOẠI GIAO CÂY TRE", font_title1_pano, 1040, 130, is_gradient=True, stroke_width=16)
draw_styled_text(img2, "DĨ BẤT BIẾN — ỨNG VẠN BIẾN", font_title2_pano, 1040, 240, is_gradient=False, stroke_width=15)
draw_bottom_bar(img2, "CÂY TRE CÓ ĐỨNG VỮNG TRƯỚC SỨC ÉP CHỌN PHE?", font_sub_pano, 755, 955, 1005, line_width=1150)
v2_path = os.path.join(OUTPUT_DIR, "thumbnail_v2_panorama_cay_tre_dung_vung.jpg")
img2.convert("RGB").save(v2_path, quality=98, subsampling=0)

# =========================================================================
# 3. VERSION 3: DYNAMIC FLAME - CÂY TRE CÓ ĐỨNG VỮNG TRƯỚC SỨC ÉP CHỌN PHE?
# =========================================================================
print("Rendering V3 (Dynamic Flame - Sức ép chọn phe)...")
img3 = Image.open(BG_FLAME).convert("RGBA").resize((1920, 1080), Image.Resampling.LANCZOS)
draw_styled_text(img3, "NGOẠI GIAO CÂY TRE", font_title1_flame, 620, 100, is_gradient=True, stroke_width=16)
draw_styled_text(img3, "DĨ BẤT BIẾN — ỨNG VẠN BIẾN", font_title2_flame, 620, 195, is_gradient=False, stroke_width=15)
draw_bottom_bar(img3, "CÂY TRE CÓ ĐỨNG VỮNG TRƯỚC SỨC ÉP CHỌN PHE?", font_sub_flame, 925, 955, 1005, line_width=1150)
v3_path = os.path.join(OUTPUT_DIR, "thumbnail_v3_flame_suc_ep_chon_phe.jpg")
img3.convert("RGB").save(v3_path, quality=98, subsampling=0)

# =========================================================================
# 4. VERSION 4: DYNAMIC FLAME - AI CÓ THỂ ÉP VIỆT NAM CHỌN BÊN?
# =========================================================================
print("Rendering V4 (Dynamic Flame - Ai có thể ép)...")
img4 = Image.open(BG_FLAME).convert("RGBA").resize((1920, 1080), Image.Resampling.LANCZOS)
draw_styled_text(img4, "NGOẠI GIAO CÂY TRE", font_title1_flame, 620, 100, is_gradient=True, stroke_width=16)
draw_styled_text(img4, "DĨ BẤT BIẾN — ỨNG VẠN BIẾN", font_title2_flame, 620, 195, is_gradient=False, stroke_width=15)
draw_bottom_bar(img4, "AI CÓ THỂ ÉP VIỆT NAM CHỌN BÊN?", font_sub_flame, 925, 955, 1005, line_width=950)
v4_path = os.path.join(OUTPUT_DIR, "thumbnail_v4_flame_ai_ep_viet_nam.jpg")
img4.convert("RGB").save(v4_path, quality=98, subsampling=0)

# =========================================================================
# 5. VERSION 5: TECH RESILIENCE - BẢN LĨNH TRƯỚC SỨC ÉP CHỌN PHE
# =========================================================================
print("Rendering V5 (Tech Resilience - Bản lĩnh tự cường)...")
img5 = Image.open(BG_TECH).convert("RGBA").resize((1920, 1080), Image.Resampling.LANCZOS)
draw_styled_text(img5, "NGOẠI GIAO CÂY TRE", font_title1_flame, 1320, 130, is_gradient=True, stroke_width=16)
draw_styled_text(img5, "DĨ BẤT BIẾN — ỨNG VẠN BIẾN", font_title2_flame, 1320, 235, is_gradient=False, stroke_width=15)
draw_bottom_bar(img5, "BẢN LĨNH TRƯỚC SỨC ÉP CHỌN PHE", font_sub_flame, 775, 955, 1005, line_width=900)
v5_path = os.path.join(OUTPUT_DIR, "thumbnail_v5_tech_ban_linh_tu_cuong.jpg")
img5.convert("RGB").save(v5_path, quality=98, subsampling=0)

print("\n🎉 HOÀN TẤT RENDER 5 PHIÊN BẢN THUMBNAIL CHUẨN KÊNH!")
for f in sorted(os.listdir(OUTPUT_DIR)):
    if f.endswith(".jpg"):
        sz = os.path.getsize(os.path.join(OUTPUT_DIR, f)) // 1024
        print(f" - {f} ({sz} KB)")
