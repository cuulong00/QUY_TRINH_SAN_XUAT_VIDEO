import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

THUMBNAILS_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/hoa-phat-thaco-nghich-ly-cong-nong/thumbnails"
PLATE_H1 = os.path.join(THUMBNAILS_DIR, "plate_huong_1_investigative.jpg")
PLATE_H2 = os.path.join(THUMBNAILS_DIR, "plate_huong_2_metaphor.jpg")
PLATE_H3 = os.path.join(THUMBNAILS_DIR, "plate_huong_3_dualtitan.jpg")

FONT_TAHOMA_BOLD = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"
FONT_ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

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

def draw_text(base_img, text, font, pos, align="center", 
              fill_color=(255, 255, 255), gradient_colors=None,
              stroke_width=28, stroke_color=(0, 0, 0),
              shadow_offset=(0, 20), shadow_blur=20, shadow_alpha=255):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    ref_x, ref_y = pos
    if align == "center":
        x = int(ref_x - text_w / 2 - bbox[0])
    elif align == "left":
        x = int(ref_x - bbox[0])
    elif align == "right":
        x = int(ref_x - text_w - bbox[0])
    else:
        x = int(ref_x - bbox[0])
    y = int(ref_y - text_h / 2 - bbox[1])
    
    # 1. Shadow Layer
    if shadow_blur > 0 and shadow_alpha > 0:
        shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow_img)
        sx = x + shadow_offset[0]
        sy = y + shadow_offset[1]
        sdraw.text((sx, sy), text, font=font, fill=(0, 0, 0, shadow_alpha),
                   stroke_width=stroke_width + 16, stroke_fill=(0, 0, 0, shadow_alpha))
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
        base_img.alpha_composite(shadow_img)
        
    # 2. Outer Stroke Layer
    if stroke_width > 0:
        stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        kdraw = ImageDraw.Draw(stroke_img)
        kdraw.text((x, y), text, font=font, fill=stroke_color,
                   stroke_width=stroke_width, stroke_fill=stroke_color)
        base_img.alpha_composite(stroke_img)
        
    # 3. Fill Layer
    if gradient_colors:
        pad = stroke_width * 2 + 80
        mask_img = Image.new('L', (text_w + pad, text_h + pad), 0)
        mdraw = ImageDraw.Draw(mask_img)
        mx = -bbox[0] + pad // 2
        my = -bbox[1] + pad // 2
        mdraw.text((mx, my), text, font=font, fill=255)
        
        grad = create_gradient(mask_img.width, mask_img.height, gradient_colors[0], gradient_colors[1])
        grad.putalpha(mask_img)
        
        paste_x = x + bbox[0] - pad // 2
        paste_y = y + bbox[1] - pad // 2
        base_img.paste(grad, (paste_x, paste_y), grad)
    else:
        fill_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        fdraw = ImageDraw.Draw(fill_img)
        fdraw.text((x, y), text, font=font, fill=fill_color)
        base_img.alpha_composite(fill_img)

def save_dual_res(img, filename_prefix):
    path_4k = os.path.join(THUMBNAILS_DIR, f"{filename_prefix}_4k.jpg")
    path_1080p = os.path.join(THUMBNAILS_DIR, f"{filename_prefix}_1080p.jpg")
    
    rgb = img.convert("RGB")
    rgb.save(path_4k, quality=98, subsampling=0)
    print(f"Saved 4K: {path_4k}")
    
    rgb_1080 = rgb.resize((1920, 1080), Image.Resampling.LANCZOS)
    rgb_1080.save(path_1080p, quality=98, subsampling=0)
    print(f"Saved 1080p: {path_1080p}")

# ==============================================================================
# HƯỚNG 1: BÌA TẠP CHÍ ĐIỀU TRA TỐI GIẢN (Bloomberg / Financial Times Style)
# ==============================================================================
def render_huong_1():
    print("--- Rendering Hướng 1: Bìa Tạp Chí Điều Tra Tối Giản ---")
    raw = Image.open(PLATE_H1).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    font_kicker = ImageFont.truetype(FONT_ARIAL_BOLD, 75)
    font_line1 = ImageFont.truetype(FONT_TAHOMA_BOLD, 225)
    font_line2 = ImageFont.truetype(FONT_TAHOMA_BOLD, 225)
    font_sub = ImageFont.truetype(FONT_ARIAL_BOLD, 85)
    
    # Kicker
    draw_text(img, "HỒ SƠ ĐIỀU TRA ĐẶC BIỆT", font_kicker, (220, 360), align="left",
              fill_color=(255, 214, 0), stroke_width=6, stroke_color=(0, 0, 0),
              shadow_offset=(0, 8), shadow_blur=10)
    
    # Line 1: THÉP ĐI NUÔI HEO?
    draw_text(img, "THÉP ĐI NUÔI HEO?", font_line1, (220, 580), align="left",
              fill_color=(255, 255, 255), stroke_width=32, stroke_color=(0, 0, 0),
              shadow_offset=(0, 22), shadow_blur=22)
    
    # Line 2: Ô TÔ TRỒNG CHUỐI?
    draw_text(img, "Ô TÔ TRỒNG CHUỐI?", font_line2, (220, 840), align="left",
              gradient_colors=((255, 235, 30), (255, 140, 0)),
              stroke_width=32, stroke_color=(0, 0, 0),
              shadow_offset=(0, 22), shadow_blur=22)
    
    # Subtitle Line
    draw_text(img, "Nghịch Lý Sinh Tồn Sau Đỉnh Cao Công Nghiệp", font_sub, (220, 1080), align="left",
              fill_color=(220, 228, 238), stroke_width=12, stroke_color=(0, 0, 0),
              shadow_offset=(0, 10), shadow_blur=12)
    
    save_dual_res(img, "thumbnail_huong_1_editorial_cover")

# ==============================================================================
# HƯỚNG 2: ẨN DỤ ĐIỆN ẢNH BIỂU TƯỢNG (The Economist / Time Style)
# ==============================================================================
def render_huong_2():
    print("--- Rendering Hướng 2: Ẩn Dụ Điện Ảnh Biểu Tượng ---")
    raw = Image.open(PLATE_H2).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    font_main = ImageFont.truetype(FONT_TAHOMA_BOLD, 260)
    font_sub = ImageFont.truetype(FONT_ARIAL_BOLD, 105)
    
    # Line 1: CHIẾC BẪY SINH TỒN?
    draw_text(img, "CHIẾC BẪY SINH TỒN?", font_main, (1920, 320), align="center",
              fill_color=(255, 255, 255), stroke_width=36, stroke_color=(0, 0, 0),
              shadow_offset=(0, 24), shadow_blur=26)
    
    # Line 2: THÉP NUÔI HEO & Ô TÔ TRỒNG CHUỐI
    draw_text(img, "THÉP NUÔI HEO & Ô TÔ TRỒNG CHUỐI", font_sub, (1920, 560), align="center",
              fill_color=(255, 215, 64), stroke_width=16, stroke_color=(0, 0, 0),
              shadow_offset=(0, 14), shadow_blur=16)
    
    save_dual_res(img, "thumbnail_huong_2_cinematic_metaphor")

# ==============================================================================
# HƯỚNG 3: CHÂN DUNG TINH HOA BẤT ĐỐI XỨNG (Dual Titan Profile Noir)
# ==============================================================================
def render_huong_3():
    print("--- Rendering Hướng 3: Chân Dung Tinh Hoa Bất Đối Xứng ---")
    raw = Image.open(PLATE_H3).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    font_l1 = ImageFont.truetype(FONT_TAHOMA_BOLD, 235)
    font_l2 = ImageFont.truetype(FONT_TAHOMA_BOLD, 205)
    font_sub = ImageFont.truetype(FONT_ARIAL_BOLD, 88)
    
    # Line 1: THÉP ĐI NUÔI HEO? (Center Top)
    draw_text(img, "THÉP ĐI NUÔI HEO?", font_l1, (1920, 270), align="center",
              gradient_colors=((255, 240, 30), (255, 120, 0)),
              stroke_width=34, stroke_color=(0, 0, 0),
              shadow_offset=(0, 22), shadow_blur=24)
    
    # Line 2: Ô TÔ ĐI TRỒNG CHUỐI?
    draw_text(img, "Ô TÔ ĐI TRỒNG CHUỐI?", font_l2, (1920, 510), align="center",
              fill_color=(255, 255, 255), stroke_width=32, stroke_color=(0, 0, 0),
              shadow_offset=(0, 20), shadow_blur=22)
    
    # Elegant Bottom Subtitle (No cheesy box, fine luminous gold line)
    line_w = 2100
    line_y = 2025
    sub_y = 1940
    ldraw = ImageDraw.Draw(img)
    start_x = int(1920 - line_w / 2)
    for dx in range(line_w):
        factor = 1.0 - abs(dx - line_w / 2) / (line_w / 2)
        alpha = int(220 * (factor ** 0.7))
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 6)], fill=(255, 215, 64, alpha))
        
    draw_text(img, "PHÒNG THỦ HAY CHIẾC BẪY?", font_sub, (1920, sub_y), align="center",
              fill_color=(255, 255, 255), stroke_width=18, stroke_color=(0, 0, 0),
              shadow_offset=(0, 12), shadow_blur=14)
    
    save_dual_res(img, "thumbnail_huong_3_dual_titan_noir")

def main():
    render_huong_1()
    render_huong_2()
    render_huong_3()
    print("ALL 3 DISTINCT THUMBNAIL DIRECTIONS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
