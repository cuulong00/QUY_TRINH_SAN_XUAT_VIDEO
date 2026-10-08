import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/hoa-phat-thaco-nghich-ly-cong-nong/thumbnails'
BASE_4K_PATH = os.path.join(OUTPUT_DIR, 'thumbnail_official_no_vs_4k.jpg')
HP_LOGO_PATH = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/seu-dau-dan/references/logos/hoa_phat_logo.png'
THACO_LOGO_PATH = '/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/seu-dau-dan/references/logos/thaco_logo.png'
FONT_PATH = '/System/Library/Fonts/Supplemental/Tahoma Bold.ttf'

def extract_clean_hp():
    hp = Image.open(HP_LOGO_PATH).convert('RGBA')
    arr = np.array(hp)
    mask = arr[:, :, 3] > 30
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    cropped = hp.crop((xmin, ymin, xmax + 1, ymax + 1))
    
    # White logo with smooth alpha
    c_arr = np.array(cropped)
    white = np.zeros_like(c_arr)
    white[:, :, 0:3] = 255
    white[:, :, 3] = c_arr[:, :, 3]
    return Image.fromarray(white, 'RGBA')

def extract_clean_thaco():
    th = Image.open(THACO_LOGO_PATH).convert('RGB')
    arr = np.array(th)
    # Background is white (255, 255, 255), letters are blue
    # Create high-precision inverted lightness mask for blue ink
    # Blue has low R (<120), low G (<160)
    # Darkness = 255 - grayscale
    gray = np.mean(arr, axis=2)
    # Threshold and smooth
    alpha = np.clip((240 - gray) * 3.5, 0, 255).astype(np.uint8)
    
    # Crop to blue letters
    is_blue = alpha > 40
    rows = np.any(is_blue, axis=1)
    cols = np.any(is_blue, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    
    alpha_cropped = alpha[ymin:ymax+1, xmin:xmax+1]
    
    h, w = alpha_cropped.shape
    white = np.zeros((h, w, 4), dtype=np.uint8)
    white[:, :, 0:3] = 255
    white[:, :, 3] = alpha_cropped
    return Image.fromarray(white, 'RGBA')

def add_style(logo_img, target_h, stroke_w=12, shadow_off=(0, 14), shadow_blur=16):
    aspect = logo_img.width / logo_img.height
    w = int(target_h * aspect)
    resized = logo_img.resize((w, target_h), Image.Resampling.LANCZOS)
    
    pad = stroke_w * 2 + shadow_blur * 2 + 40
    cw = w + pad * 2
    ch = target_h + pad * 2
    
    alpha = resized.split()[3]
    
    # 1. Shadow
    shadow = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    s_mask = alpha.filter(ImageFilter.MaxFilter(stroke_w * 2 + 1))
    s_fill = Image.new('RGBA', (w, target_h), (0, 0, 0, 235))
    shadow.paste(s_fill, (pad + shadow_off[0], pad + shadow_off[1]), s_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
    
    # 2. Black Stroke
    stroke_layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    k_fill = Image.new('RGBA', (w, target_h), (0, 0, 0, 255))
    stroke_layer.paste(k_fill, (pad, pad), s_mask)
    
    # 3. Main Fill
    fill_layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    main_fill = Image.new('RGBA', (w, target_h), (255, 255, 255, 255))
    fill_layer.paste(main_fill, (pad, pad), alpha)
    
    out = Image.alpha_composite(shadow, stroke_layer)
    out = Image.alpha_composite(out, fill_layer)
    
    bbox = out.getbbox()
    return out.crop(bbox)

def render_option(opt_type, filename_base, label_text=None):
    base = Image.open(BASE_4K_PATH).convert('RGBA')
    W, H = base.size # 3840, 2160
    
    hp_clean = extract_clean_hp()
    th_clean = extract_clean_thaco()
    
    # Optical height balancing:
    # HP contains icon (190px) + text (114px). Total ratio icon/text is 1.66
    # If we set HP target_h = 160, its text height is ~96px.
    # THACO is purely text (93px), so setting THACO target_h = 98 makes text heights match identically!
    hp_styled = add_style(hp_clean, target_h=158, stroke_w=12)
    th_styled = add_style(th_clean, target_h=96, stroke_w=12)
    
    center_y = 205
    connector_half_w = 320
    
    hp_x = int(1920 - connector_half_w - hp_styled.width)
    hp_y = int(center_y - hp_styled.height / 2)
    
    th_x = int(1920 + connector_half_w)
    th_y = int(center_y - th_styled.height / 2)
    
    conn_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(conn_layer)
    
    line_y = center_y
    line_start_x = hp_x + hp_styled.width + 35
    line_end_x = th_x - 35
    
    if opt_type == 'diamond':
        # Glowing gold lines with diamond in center
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (1920 - 40, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(1920 + 40, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
        
        # Center Diamond ◆
        d_size = 28
        diamond_pts = [(1920, line_y - d_size), (1920 + d_size, line_y), (1920, line_y + d_size), (1920 - d_size, line_y)]
        cdraw.polygon(diamond_pts, fill=(255, 215, 64, 255), outline=(0, 0, 0, 255))
        in_size = 14
        in_pts = [(1920, line_y - in_size), (1920 + in_size, line_y), (1920, line_y + in_size), (1920 - in_size, line_y)]
        cdraw.polygon(in_pts, fill=(255, 255, 255, 255))

    elif opt_type == 'exchange':
        # Two lines with a circular bidirectional badge ⇄
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (1920 - 75, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(1920 + 75, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
        
        r = 55
        cdraw.ellipse([(1920 - r, line_y - r), (1920 + r, line_y + r)], fill=(16, 22, 34, 245), outline=(255, 215, 64, 255), width=4)
        font_arrow = ImageFont.truetype(FONT_PATH, 52)
        abbox = cdraw.textbbox((0, 0), "⇄", font=font_arrow)
        aw = abbox[2] - abbox[0]
        ah = abbox[3] - abbox[1]
        cdraw.text((1920 - aw/2 - abbox[0], line_y - ah/2 - abbox[1]), "⇄", font=font_arrow, fill=(255, 220, 80, 255))

    elif opt_type == 'pill_badge':
        font_pill = ImageFont.truetype(FONT_PATH, 42)
        pill_text = label_text or "NGHỊCH LÝ"
        pbbox = cdraw.textbbox((0, 0), pill_text, font=font_pill)
        pw = pbbox[2] - pbbox[0]
        ph = pbbox[3] - pbbox[1]
        
        pad_x = 42
        pad_y = 18
        pill_w = pw + pad_x * 2
        pill_h = ph + pad_y * 2
        
        pill_left = 1920 - pill_w / 2
        pill_right = 1920 + pill_w / 2
        pill_top = line_y - pill_h / 2
        pill_bottom = line_y + pill_h / 2
        
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (pill_left - 20, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(pill_right + 20, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            
        cdraw.rounded_rectangle([pill_left, pill_top, pill_right, pill_bottom], radius=18, fill=(15, 20, 30, 245), outline=(255, 215, 64, 255), width=3)
        cdraw.text((1920 - pw/2 - pbbox[0], line_y - ph/2 - pbbox[1]), pill_text, font=font_pill, fill=(255, 255, 255, 255))

    glow = conn_layer.filter(ImageFilter.GaussianBlur(14))
    base.alpha_composite(glow)
    base.alpha_composite(conn_layer)
    
    base.alpha_composite(hp_styled, (hp_x, hp_y))
    base.alpha_composite(th_styled, (th_x, th_y))
    
    out_4k = os.path.join(OUTPUT_DIR, f"{filename_base}_4k.jpg")
    out_1080 = os.path.join(OUTPUT_DIR, f"{filename_base}_1080p.jpg")
    
    rgb = base.convert('RGB')
    rgb.save(out_4k, quality=96)
    rgb.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_1080, quality=96)
    print(f"Rendered {filename_base} successfully!")

# Render the 3 refined options
render_option('diamond', 'thumb_option_A_gold_diamond')
render_option('exchange', 'thumb_option_B_exchange_node')
render_option('pill_badge', 'thumb_option_C_editorial_nghichly', label_text="NGHỊCH LÝ")
render_option('pill_badge', 'thumb_option_D_editorial_haideche', label_text="HAI ĐẾ CHẾ")
