import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

THUMBNAILS_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/hoa-phat-thaco-nghich-ly-cong-nong/thumbnails"
PLATE_V1 = os.path.join(THUMBNAILS_DIR, "clean_plate_v1_cinematic.jpg")
PLATE_V2 = os.path.join(THUMBNAILS_DIR, "clean_plate_v2_balanced.jpg")

HOA_PHAT_LOGO = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/seu-dau-dan/references/logos/hoa_phat_logo.png"
THACO_LOGO = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/seu-dau-dan/references/logos/thaco_logo.png"

FONT_TAHOMA_BOLD = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"

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
                     top_color=(255, 240, 20), bottom_color=(255, 100, 0), 
                     solid_color=(255, 255, 255), stroke_width=36, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 24), shadow_blur=24, shadow_color=(0, 0, 0, 255)):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = int(center_x - text_w / 2 - bbox[0])
    y = int(center_y - text_h / 2 - bbox[1])
    
    # 1. Dual-Layer Heavy Black Drop Shadow
    shadow_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow_img)
    sx = x + shadow_offset[0]
    sy = y + shadow_offset[1]
    sdraw.text((sx, sy), text, font=font, fill=shadow_color, stroke_width=stroke_width + 18, stroke_fill=shadow_color)
    if shadow_blur > 0:
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(shadow_blur))
    base_img.alpha_composite(shadow_img)
    
    # 2. Crisp Black Outer Stroke
    stroke_img = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(stroke_img)
    kdraw.text((x, y), text, font=font, fill=stroke_color, stroke_width=stroke_width, stroke_fill=stroke_color)
    base_img.alpha_composite(stroke_img)
    
    # 3. Inner Fill
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
    for dx in range(line_width):
        factor = 1.0 - abs(dx - line_width / 2) / (line_width / 2)
        alpha = int(255 * (factor ** 0.6))
        color = (255, 215, 64, alpha)
        ldraw.line([(start_x + dx, line_y), (start_x + dx, line_y + 8)], fill=color)
        glow_alpha = int(140 * (factor ** 0.8))
        ldraw.line([(start_x + dx, line_y - 3), (start_x + dx, line_y + 11)], fill=(255, 200, 40, glow_alpha))
    
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False, 
                     solid_color=(255, 255, 255),
                     stroke_width=20, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 14), shadow_blur=16)

def draw_bottom_bar_badge(base_img, text, font, center_x, center_y, border_color=(255, 215, 64, 255), pad_x=85, pad_y=28):
    dummy = ImageDraw.Draw(base_img)
    bbox = dummy.textbbox((0, 0), text, font=font, stroke_width=18)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    badge_w = text_w + pad_x * 2
    badge_h = text_h + pad_y * 2
    x0 = int(center_x - badge_w / 2)
    y0 = int(center_y - badge_h / 2)
    x1 = x0 + badge_w
    y1 = y0 + badge_h
    
    # 1. Badge Drop shadow
    badge_shadow = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(badge_shadow)
    sdraw.rounded_rectangle([x0 - 6, y0 + 10, x1 + 6, y1 + 18], radius=28, fill=(0, 0, 0, 240))
    badge_shadow = badge_shadow.filter(ImageFilter.GaussianBlur(16))
    base_img.alpha_composite(badge_shadow)
    
    # 2. Badge Body
    badge_body = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge_body)
    bdraw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(10, 16, 24, 240), outline=border_color, width=5)
    base_img.alpha_composite(badge_body)
    
    # 3. Badge Text
    draw_styled_text(base_img, text, font, center_x, center_y, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=18, stroke_color=(0, 0, 0),
                     shadow_offset=(0, 12), shadow_blur=14)

def overlay_brand_logos(base_img):
    """Overlay Hoa Phat & THACO logos with polished 3D drop shadow and white container pill"""
    # 1. Hoa Phat Logo (Left side)
    hp_raw = Image.open(HOA_PHAT_LOGO).convert("RGBA")
    # Hoa Phat logo is wide: 1200x320. Resize to width ~450
    hp_w = 460
    hp_h = int(hp_raw.height * (hp_w / hp_raw.width))
    hp_resized = hp_raw.resize((hp_w, hp_h), Image.Resampling.LANCZOS)
    
    # Create white pill plate for Hoa Phat
    pad = 18
    pill_w = hp_w + pad * 2
    pill_h = hp_h + pad * 2
    pill_x = 1380
    pill_y = 1150
    
    pill_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pill_layer)
    # Shadow
    pdraw.rounded_rectangle([pill_x - 4, pill_y + 8, pill_x + pill_w + 4, pill_y + pill_h + 14], radius=16, fill=(0, 0, 0, 220))
    pill_layer = pill_layer.filter(ImageFilter.GaussianBlur(12))
    # Body
    pdraw2 = ImageDraw.Draw(pill_layer)
    pdraw2.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], radius=16, fill=(255, 255, 255, 235), outline=(255, 204, 0, 220), width=3)
    base_img.alpha_composite(pill_layer)
    base_img.paste(hp_resized, (pill_x + pad, pill_y + pad), hp_resized)
    
    # 2. THACO Logo (Right side)
    tc_raw = Image.open(THACO_LOGO).convert("RGBA")
    tc_w = 380
    tc_h = int(tc_raw.height * (tc_w / tc_raw.width))
    tc_resized = tc_raw.resize((tc_w, tc_h), Image.Resampling.LANCZOS)
    
    tc_pill_w = tc_w + pad * 2
    tc_pill_h = tc_h + pad * 2
    tc_pill_x = 2000
    tc_pill_y = 1150
    
    tc_pill_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
    tcdraw = ImageDraw.Draw(tc_pill_layer)
    tcdraw.rounded_rectangle([tc_pill_x - 4, tc_pill_y + 8, tc_pill_x + tc_pill_w + 4, tc_pill_y + tc_pill_h + 14], radius=16, fill=(0, 0, 0, 220))
    tc_pill_layer = tc_pill_layer.filter(ImageFilter.GaussianBlur(12))
    tcdraw2 = ImageDraw.Draw(tc_pill_layer)
    tcdraw2.rounded_rectangle([tc_pill_x, tc_pill_y, tc_pill_x + tc_pill_w, tc_pill_y + tc_pill_h], radius=16, fill=(255, 255, 255, 235), outline=(0, 114, 206, 220), width=3)
    base_img.alpha_composite(tc_pill_layer)
    base_img.paste(tc_resized, (tc_pill_x + pad, tc_pill_y + pad), tc_resized)

def render_all_variants():
    print("Loading 4K base plates...")
    raw_v1 = Image.open(PLATE_V1).convert("RGBA")
    base_v1_4k = raw_v1.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    raw_v2 = Image.open(PLATE_V2).convert("RGBA")
    base_v2_4k = raw_v2.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    font_l1 = ImageFont.truetype(FONT_TAHOMA_BOLD, 245)
    font_l2 = ImageFont.truetype(FONT_TAHOMA_BOLD, 205)
    font_sub = ImageFont.truetype(FONT_TAHOMA_BOLD, 92)
    
    t1 = "THÉP ĐI NUÔI HEO?"
    t2 = "Ô TÔ ĐI TRỒNG CHUỐI?"
    tsub = "PHÒNG THỦ HAY CHIẾC BẪY?"
    
    # -------------------------------------------------------------
    # VARIANT 1: FLAGSHIP GOLD BADGE (Chuẩn Mẫu Phú Quốc)
    # -------------------------------------------------------------
    print("1. Rendering Variant 1 (Flagship Gold Badge)...")
    v1 = base_v2_4k.copy()
    draw_styled_text(v1, t1, font_l1, 1920, 260, is_gradient=True,
                     top_color=(255, 235, 10), bottom_color=(255, 95, 0),
                     stroke_width=36, shadow_offset=(0, 24), shadow_blur=24)
    draw_styled_text(v1, t2, font_l2, 1920, 490, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=34, shadow_offset=(0, 22), shadow_blur=22)
    draw_bottom_bar_badge(v1, tsub, font_sub, 1920, 1935, border_color=(255, 215, 64, 255), pad_x=85, pad_y=28)
    save_thumbnail(v1, "variant_1_flagship_gold_badge")

    # -------------------------------------------------------------
    # VARIANT 2: GOLD LINE ACCENT (Chuẩn Mẫu BYD)
    # -------------------------------------------------------------
    print("2. Rendering Variant 2 (BYD Gold Line Accent)...")
    v2 = base_v2_4k.copy()
    draw_styled_text(v2, t1, font_l1, 1920, 260, is_gradient=True,
                     top_color=(255, 235, 10), bottom_color=(255, 95, 0),
                     stroke_width=36, shadow_offset=(0, 24), shadow_blur=24)
    draw_styled_text(v2, t2, font_l2, 1920, 490, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=34, shadow_offset=(0, 22), shadow_blur=22)
    draw_bottom_bar_gold_line(v2, tsub, font_sub, 1920, 1930, 2025, line_width=2300)
    save_thumbnail(v2, "variant_2_byd_goldline")

    # -------------------------------------------------------------
    # VARIANT 3: CRIMSON RED WARNING BADGE (Cảnh Báo Kịch Tính)
    # -------------------------------------------------------------
    print("3. Rendering Variant 3 (Crimson Red Warning Badge)...")
    v3 = base_v2_4k.copy()
    draw_styled_text(v3, t1, font_l1, 1920, 260, is_gradient=True,
                     top_color=(255, 235, 10), bottom_color=(255, 95, 0),
                     stroke_width=36, shadow_offset=(0, 24), shadow_blur=24)
    draw_styled_text(v3, t2, font_l2, 1920, 490, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=34, shadow_offset=(0, 22), shadow_blur=22)
    draw_bottom_bar_badge(v3, tsub, font_sub, 1920, 1935, border_color=(235, 40, 40, 255), pad_x=85, pad_y=28)
    save_thumbnail(v3, "variant_3_crimson_badge")

    # -------------------------------------------------------------
    # VARIANT 4: DUAL BRAND LOGOS (Hòa Phát vs THACO)
    # -------------------------------------------------------------
    print("4. Rendering Variant 4 (Dual Brand Logos)...")
    v4 = base_v2_4k.copy()
    overlay_brand_logos(v4)
    draw_styled_text(v4, t1, font_l1, 1920, 260, is_gradient=True,
                     top_color=(255, 235, 10), bottom_color=(255, 95, 0),
                     stroke_width=36, shadow_offset=(0, 24), shadow_blur=24)
    draw_styled_text(v4, t2, font_l2, 1920, 490, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=34, shadow_offset=(0, 22), shadow_blur=22)
    draw_bottom_bar_badge(v4, tsub, font_sub, 1920, 1935, border_color=(255, 215, 64, 255), pad_x=85, pad_y=28)
    save_thumbnail(v4, "variant_4_dual_logos")

    # -------------------------------------------------------------
    # VARIANT 5: CINEMATIC CLOSE-UP (Plate V1)
    # -------------------------------------------------------------
    print("5. Rendering Variant 5 (Cinematic Close-up)...")
    v5 = base_v1_4k.copy()
    top_vignette = Image.new('RGBA', (3840, 2160), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(top_vignette)
    vdraw.rectangle([0, 0, 3840, 750], fill=(5, 10, 18, 160))
    top_vignette = top_vignette.filter(ImageFilter.GaussianBlur(90))
    v5.alpha_composite(top_vignette)
    
    draw_styled_text(v5, t1, font_l1, 1920, 240, is_gradient=True,
                     top_color=(255, 235, 10), bottom_color=(255, 95, 0),
                     stroke_width=36, shadow_offset=(0, 24), shadow_blur=24)
    draw_styled_text(v5, t2, font_l2, 1920, 470, is_gradient=False,
                     solid_color=(255, 255, 255),
                     stroke_width=34, shadow_offset=(0, 22), shadow_blur=22)
    draw_bottom_bar_badge(v5, tsub, font_sub, 1920, 1935, border_color=(255, 215, 64, 255), pad_x=85, pad_y=28)
    save_thumbnail(v5, "variant_5_cinematic_closeup")

    print("ALL 5 POLISHED THUMBNAIL VARIANTS COMPLETED SUCCESSFULLY!")

def save_thumbnail(img, base_name):
    path_4k = os.path.join(THUMBNAILS_DIR, f"{base_name}_4k.jpg")
    path_1080 = os.path.join(THUMBNAILS_DIR, f"{base_name}_1080p.jpg")
    
    rgb = img.convert("RGB")
    rgb.save(path_4k, quality=98, subsampling=0)
    print(f"Saved 4K: {path_4k}")
    
    rgb_1080 = rgb.resize((1920, 1080), Image.Resampling.LANCZOS)
    rgb_1080.save(path_1080, quality=98, subsampling=0)
    print(f"Saved 1080p: {path_1080}")

if __name__ == "__main__":
    render_all_variants()
