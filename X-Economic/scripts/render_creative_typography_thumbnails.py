import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/aves-khoi-nghiep-xe-dien/thumbnails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Available high quality fonts on macOS
FONTS = {
    "arial_black": "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "arial_bold": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "impact": "/System/Library/Fonts/Supplemental/Impact.ttf",
    "tahoma_bold": "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf",
    "futura_bold": "/System/Library/Fonts/Supplemental/Futura.ttc",
    "georgia_bold": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "trebuchet_bold": "/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf",
}

def create_gradient_mask(w, h, top_color, bottom_color):
    top = np.array(top_color, dtype=float)
    bottom = np.array(bottom_color, dtype=float)
    gradient = np.zeros((h, w, 4), dtype=np.uint8)
    for y in range(h):
        factor = y / max(h - 1, 1)
        c = top + factor * (bottom - top)
        gradient[y, :, 0:3] = c[:3]
        gradient[y, :, 3] = 255
    return Image.fromarray(gradient, 'RGBA')

def draw_text_advanced(base_img, text, font, pos, align="center", 
                       fill_color=(255, 255, 255), 
                       gradient_colors=None, # tuple (top, bottom)
                       stroke_width=0, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 16), shadow_blur=16, shadow_alpha=230):
    """
    Advanced typography renderer with support for:
    - Custom alignment ('left', 'center', 'right')
    - Solid or Vertical Gradient fills
    - Gaussian blurred multi-layer drop shadows
    - Sharp outer strokes
    """
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

    # 1. Soft Cinema Drop Shadow (Blurred)
    if shadow_blur > 0 and shadow_alpha > 0:
        shadow_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow_layer)
        sx = x + shadow_offset[0]
        sy = y + shadow_offset[1]
        sdraw.text((sx, sy), text, font=font, fill=(0, 0, 0, shadow_alpha),
                   stroke_width=stroke_width + 8, stroke_fill=(0, 0, 0, shadow_alpha))
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(shadow_blur))
        base_img.alpha_composite(shadow_layer)

    # 2. Outer Stroke
    if stroke_width > 0:
        stroke_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        kdraw = ImageDraw.Draw(stroke_layer)
        kdraw.text((x, y), text, font=font, fill=stroke_color,
                   stroke_width=stroke_width, stroke_fill=stroke_color)
        base_img.alpha_composite(stroke_layer)

    # 3. Fill (Gradient or Solid)
    if gradient_colors:
        pad = stroke_width * 2 + 40
        mask = Image.new('L', (text_w + pad, text_h + pad), 0)
        mdraw = ImageDraw.Draw(mask)
        mx = -bbox[0] + pad // 2
        my = -bbox[1] + pad // 2
        mdraw.text((mx, my), text, font=font, fill=255)

        grad = create_gradient_mask(mask.width, mask.height, gradient_colors[0], gradient_colors[1])
        grad.putalpha(mask)

        px = x + bbox[0] - pad // 2
        py = y + bbox[1] - pad // 2
        base_img.paste(grad, (px, py), grad)
    else:
        fill_layer = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
        fdraw = ImageDraw.Draw(fill_layer)
        fdraw.text((x, y), text, font=font, fill=fill_color)
        base_img.alpha_composite(fill_layer)

    return bbox

def save_dual_res(img, base_name):
    path_4k = os.path.join(OUTPUT_DIR, f"{base_name}_4k.jpg")
    path_1080 = os.path.join(OUTPUT_DIR, f"{base_name}_1080p.jpg")
    rgb = img.convert("RGB")
    rgb.save(path_4k, quality=98, subsampling=0)
    rgb.resize((1920, 1080), Image.Resampling.LANCZOS).save(path_1080, quality=98, subsampling=0)
    print(f"Saved: {path_1080}")

# ==============================================================================
# STYLE 1: EDITORIAL LEFT-ALIGNED (Bloomberg / The Economist Investigation)
# ==============================================================================
def render_style_1_editorial_left(clean_plate_path):
    """
    Left-aligned dramatic editorial title in the dark negative space above Thanh.
    - Kicker: AVES VS VINFAST (Small, elegant amber-gold accent)
    - Headline: ĐỐI TÁC HAY ĐỐI THỦ? (Massive crisp white with crimson accent)
    - Subtitle: Tướng cũ đánh thành cũ hay lập tiền đồn?
    """
    raw = Image.open(clean_plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)

    font_kicker = ImageFont.truetype(FONTS["arial_bold"], 85)
    font_main1 = ImageFont.truetype(FONTS["arial_black"], 185)
    font_main2 = ImageFont.truetype(FONTS["arial_black"], 185)
    font_sub = ImageFont.truetype(FONTS["tahoma_bold"], 70)

    # Negative space on left/center-left
    # Draw a soft dark vignette on the upper left to make text pop with zero interference
    vignette = Image.new('RGBA', (3840, 2160), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    vdraw.rectangle([0, 0, 2400, 850], fill=(5, 10, 18, 140))
    vignette = vignette.filter(ImageFilter.GaussianBlur(80))
    img.alpha_composite(vignette)

    # 1. Kicker: AVES VS VINFAST (Gold tag with amber pill accent)
    draw_text_advanced(img, "AVES VS VINFAST", font_kicker, (180, 140), align="left",
                       fill_color=(255, 204, 0), stroke_width=8, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 10), shadow_blur=12)

    # 2. Main Line 1: ĐỐI TÁC
    draw_text_advanced(img, "ĐỐI TÁC", font_main1, (180, 310), align="left",
                       fill_color=(255, 255, 255), stroke_width=24, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 18), shadow_blur=20)

    # 3. Main Line 2: HAY ĐỐI THỦ? (Crimson warning red)
    draw_text_advanced(img, "HAY ĐỐI THỦ?", font_main2, (180, 490), align="left",
                       fill_color=(255, 45, 60), stroke_width=24, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 18), shadow_blur=20)

    # 4. Editorial Subtitle Bar on left
    draw_text_advanced(img, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY LẬP TIỀN ĐỒN?", font_sub, (180, 640), align="left",
                       fill_color=(235, 240, 245), stroke_width=10, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 8), shadow_blur=10)

    save_dual_res(img, "opt1_editorial_left_aligned")

# ==============================================================================
# STYLE 2: WAR ROOM ARCHITECTURAL (Cinematic Dossier / Top Negative Space)
# ==============================================================================
def render_style_2_warroom_cinematic(clean_plate_path):
    """
    Positioned cleanly in the dark boardroom back wall between the lights.
    Pure, authoritative, minimalist typography without screaming cheesy colors.
    """
    raw = Image.open(clean_plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)

    font_brand = ImageFont.truetype(FONTS["arial_bold"], 90)
    font_core = ImageFont.truetype(FONTS["arial_black"], 210)
    font_sub = ImageFont.truetype(FONTS["georgia_bold"], 75)

    # Upper wall center (y ~ 240 - 550)
    # Brand line
    draw_text_advanced(img, "A V E S   x   V I N F A S T", font_brand, (1920, 210), align="center",
                       fill_color=(212, 175, 55), stroke_width=8, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 10), shadow_blur=14)

    # Main Big Question
    draw_text_advanced(img, "ĐỐI TÁC HAY ĐỐI THỦ?", font_core, (1920, 390), align="center",
                       fill_color=(255, 255, 255), stroke_width=24, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 20), shadow_blur=24)

    # Subtitle as a dignified strategic question
    draw_text_advanced(img, "Tướng Cũ Đánh Thành Cũ Hay Lập Tiền Đồn?", font_sub, (1920, 560), align="center",
                       fill_color=(200, 215, 230), stroke_width=10, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 10), shadow_blur=12)

    save_dual_res(img, "opt2_warroom_cinematic")

# ==============================================================================
# STYLE 3: ASYMMETRIC TENSION POSTER (Dual Entity Clash / High Contrast)
# ==============================================================================
def render_style_3_asymmetric_tension(clean_plate_path):
    """
    Uses Plate 1 (Citadel).
    Upper-right dark sky holds a massive, punchy block:
    Left: TƯỚNG CŨ
    Center-Right: THÀNH CŨ
    Bottom: ĐỐI TÁC HAY ĐỐI THỦ?
    """
    raw = Image.open(clean_plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)

    font_main = ImageFont.truetype(FONTS["impact"], 240)
    font_sub = ImageFont.truetype(FONTS["arial_black"], 115)
    font_kicker = ImageFont.truetype(FONTS["arial_bold"], 80)

    # Subtle darkening in upper center
    vignette = Image.new('RGBA', (3840, 2160), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    vdraw.rectangle([700, 0, 3140, 680], fill=(8, 12, 20, 160))
    vignette = vignette.filter(ImageFilter.GaussianBlur(90))
    img.alpha_composite(vignette)

    # Kicker
    draw_text_advanced(img, "CUỘC ĐỐI ĐẦU XE ĐIỆN VIỆT NAM", font_kicker, (1920, 140), align="center",
                       fill_color=(255, 215, 64), stroke_width=6, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 8), shadow_blur=10)

    # Main Headline (Impact font, ultra tall, powerful, editorial)
    draw_text_advanced(img, "ĐỐI TÁC HAY ĐỐI THỦ?", font_main, (1920, 300), align="center",
                       fill_color=(255, 255, 255), stroke_width=22, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 18), shadow_blur=22)

    # Subtitle Line
    draw_text_advanced(img, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY LẬP TIỀN ĐỒN?", font_sub, (1920, 480), align="center",
                       fill_color=(255, 60, 60), stroke_width=14, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 12), shadow_blur=14)

    save_dual_res(img, "opt3_asymmetric_tension")

# ==============================================================================
# STYLE 4: TIME / BLOOMBERG COVER (Plate 3 Editorial - Pure Luxury White & Bronze)
# ==============================================================================
def render_style_4_editorial_luxury(clean_plate_path):
    """
    Uses Plate 3 (Editorial).
    High-end, clean magazine cover look.
    No tacky yellow-orange gradients. Pure platinum white, burnished bronze accents.
    """
    raw = Image.open(clean_plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)

    font_headline = ImageFont.truetype(FONTS["arial_black"], 190)
    font_vs = ImageFont.truetype(FONTS["arial_bold"], 85)
    font_sub = ImageFont.truetype(FONTS["tahoma_bold"], 80)

    # Subtle top vignette for contrast
    vignette = Image.new('RGBA', (3840, 2160), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    vdraw.rectangle([0, 0, 3840, 600], fill=(0, 0, 0, 150))
    vignette = vignette.filter(ImageFilter.GaussianBlur(70))
    img.alpha_composite(vignette)

    # Top brand bar
    draw_text_advanced(img, "AVES  VS  VINFAST", font_vs, (1920, 130), align="center",
                       fill_color=(240, 195, 110), stroke_width=8, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 8), shadow_blur=12)

    # Main Headline
    draw_text_advanced(img, "ĐỐI TÁC HAY ĐỐI THỦ?", font_headline, (1920, 285), align="center",
                       fill_color=(255, 255, 255), stroke_width=24, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 20), shadow_blur=22)

    # Bottom dramatic statement (clean, floating in dark tarmac)
    draw_text_advanced(img, "TƯỚNG CŨ ĐÁNH THÀNH CŨ HAY LẬP TIỀN ĐỒN?", font_sub, (1920, 2010), align="center",
                       fill_color=(255, 220, 120), stroke_width=16, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 12), shadow_blur=16)

    save_dual_res(img, "opt4_editorial_luxury")

# ==============================================================================
# STYLE 5: SINGLE PUNCH WORD (Hyper-minimalist Mobile Killer)
# ==============================================================================
def render_style_5_single_punch(clean_plate_path):
    """
    Ultra-focused mobile CTR design:
    One massive, shocking word: "ĐỐI THỦ?" in giant red/white
    Followed by "HAY ĐỒNG MINH?"
    Kicker: AVES vs VINFAST
    """
    raw = Image.open(clean_plate_path).convert("RGBA")
    img = raw.resize((3840, 2160), Image.Resampling.LANCZOS)

    font_kicker = ImageFont.truetype(FONTS["arial_bold"], 80)
    font_giant = ImageFont.truetype(FONTS["impact"], 260)
    font_sub = ImageFont.truetype(FONTS["arial_black"], 105)

    vignette = Image.new('RGBA', (3840, 2160), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    vdraw.rectangle([600, 0, 3240, 680], fill=(5, 8, 15, 170))
    vignette = vignette.filter(ImageFilter.GaussianBlur(90))
    img.alpha_composite(vignette)

    # Kicker
    draw_text_advanced(img, "TƯỚNG CŨ NGUYỄN VĂN THANH  x  PHẠM NHẬT VƯỢNG", font_kicker, (1920, 120), align="center",
                       fill_color=(255, 215, 64), stroke_width=6, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 8), shadow_blur=10)

    # Line 1: Giant word
    draw_text_advanced(img, "ĐỐI TÁC HAY ĐỐI THỦ?", font_giant, (1920, 280), align="center",
                       fill_color=(255, 255, 255), stroke_width=22, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 20), shadow_blur=24)

    # Line 2: The Core Dilemma
    draw_text_advanced(img, "ĐÁNH THÀNH CŨ HAY LẬP TIỀN ĐỒN?", font_sub, (1920, 460), align="center",
                       fill_color=(255, 40, 40), stroke_width=14, stroke_color=(0, 0, 0),
                       shadow_offset=(0, 14), shadow_blur=16)

    save_dual_res(img, "opt5_single_punch")

def main():
    c1 = os.path.join(OUTPUT_DIR, "clean_plate_c1_citadel.jpg")
    c2 = os.path.join(OUTPUT_DIR, "clean_plate_c2_warroom.jpg")
    c3 = os.path.join(OUTPUT_DIR, "clean_plate_c3_editorial.jpg")

    print("Rendering Style 1 (Editorial Left-Aligned)...")
    render_style_1_editorial_left(c1)

    print("Rendering Style 2 (War Room Architectural / Minimalist)...")
    render_style_2_warroom_cinematic(c2)

    print("Rendering Style 3 (Asymmetric Tension / Impact)...")
    render_style_3_asymmetric_tension(c1)

    print("Rendering Style 4 (Editorial Luxury Platinum)...")
    render_style_4_editorial_luxury(c3)

    print("Rendering Style 5 (Single Punch Dilemma)...")
    render_style_5_single_punch(c1)

    print("ALL 5 CREATIVE TYPOGRAPHY CONCEPTS RENDERED!")

if __name__ == "__main__":
    main()
