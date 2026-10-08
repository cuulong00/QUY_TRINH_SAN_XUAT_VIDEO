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
    
    # Make pure crisp white with smooth alpha
    c_arr = np.array(cropped)
    white = np.zeros_like(c_arr)
    white[:, :, 0:3] = 255
    white[:, :, 3] = c_arr[:, :, 3]
    return Image.fromarray(white, 'RGBA')

def extract_clean_thaco():
    th = Image.open(THACO_LOGO_PATH).convert('RGBA')
    arr = np.array(th)
    th_mask = (arr[:, :, 0] < 100) & (arr[:, :, 1] < 150) & (arr[:, :, 2] > 100)
    rows = np.any(th_mask, axis=1)
    cols = np.any(th_mask, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    cropped = th.crop((xmin, ymin, xmax + 1, ymax + 1))
    
    c_arr = np.array(cropped)
    white = np.zeros_like(c_arr)
    white[:, :, 0:3] = 255
    dist = np.sqrt((c_arr[:, :, 0] - 0)**2 + (c_arr[:, :, 1] - 85)**2 + (c_arr[:, :, 2] - 166)**2)
    alpha = np.clip((180 - dist) * 2.5, 0, 255).astype(np.uint8)
    white[:, :, 3] = alpha
    return Image.fromarray(white, 'RGBA')

def add_style(logo_img, target_h, stroke_w=12, shadow_off=(0, 14), shadow_blur=16):
    # Resize keeping aspect ratio
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
    s_fill = Image.new('RGBA', (w, target_h), (0, 0, 0, 230))
    shadow.paste(s_fill, (pad + shadow_off[0], pad + shadow_off[1]), s_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
    
    # 2. Black Stroke
    stroke_layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    k_fill = Image.new('RGBA', (w, target_h), (0, 0, 0, 255))
    stroke_layer.paste(k_fill, (pad, pad), s_mask)
    
    # 3. Main Fill
    fill_layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    # Slight warm ivory white
    main_fill = Image.new('RGBA', (w, target_h), (252, 252, 255, 255))
    fill_layer.paste(main_fill, (pad, pad), alpha)
    
    out = Image.alpha_composite(shadow, stroke_layer)
    out = Image.alpha_composite(out, fill_layer)
    
    bbox = out.getbbox()
    return out.crop(bbox)

def render_option(opt_type, filename_base):
    base = Image.open(BASE_4K_PATH).convert('RGBA')
    W, H = base.size # 3840, 2160
    
    hp_clean = extract_clean_hp()
    th_clean = extract_clean_thaco()
    
    # In HP, text height is about 60% of total height (because of the tall 3-triangle icon)
    # Target total height for HP: 155px in 4K
    # Target height for THACO: 95px in 4K (so text sizes match optically!)
    hp_styled = add_style(hp_clean, target_h=150, stroke_w=12)
    th_styled = add_style(th_clean, target_h=92, stroke_w=12)
    
    center_y = 215 # Middle of the 0-430 top area
    
    # Positions
    # Center X is 1920
    # Let's space them symmetrically around 1920
    # Gap in middle for connector: around 350-450px
    connector_half_w = 260
    
    hp_x = int(1920 - connector_half_w - hp_styled.width)
    hp_y = int(center_y - hp_styled.height / 2)
    
    th_x = int(1920 + connector_half_w)
    th_y = int(center_y - th_styled.height / 2)
    
    # Draw Connector
    conn_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(conn_layer)
    
    # Glowing gold line connecting them
    line_y = center_y
    line_start_x = hp_x + hp_styled.width + 30
    line_end_x = th_x - 30
    
    if opt_type == 'diamond':
        # Glowing gold lines with diamond in center
        # Left segment
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (1920 - 45, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(1920 + 45, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
        
        # Center Diamond ◆
        d_size = 28
        diamond_pts = [(1920, line_y - d_size), (1920 + d_size, line_y), (1920, line_y + d_size), (1920 - d_size, line_y)]
        # Outer glow
        cdraw.polygon(diamond_pts, fill=(255, 215, 64, 255), outline=(0, 0, 0, 255))
        # Inner diamond
        in_size = 14
        in_pts = [(1920, line_y - in_size), (1920 + in_size, line_y), (1920, line_y + in_size), (1920 - in_size, line_y)]
        cdraw.polygon(in_pts, fill=(255, 255, 255, 255))

    elif opt_type == 'exchange':
        # Two lines with a circular bidirectional badge ⇄
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (1920 - 75, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(1920 + 75, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
        
        # Circular badge
        r = 60
        cdraw.ellipse([(1920 - r, line_y - r), (1920 + r, line_y + r)], fill=(20, 26, 38, 240), outline=(255, 215, 64, 255), width=4)
        # Draw ⇄ arrows
        font_arrow = ImageFont.truetype(FONT_PATH, 56)
        abbox = cdraw.textbbox((0, 0), "⇄", font=font_arrow)
        aw = abbox[2] - abbox[0]
        ah = abbox[3] - abbox[1]
        cdraw.text((1920 - aw/2 - abbox[0], line_y - ah/2 - abbox[1]), "⇄", font=font_arrow, fill=(255, 220, 80, 255))

    elif opt_type == 'pill_badge':
        # Minimalist editorial badge: 'NGHỊCH LÝ'
        font_pill = ImageFont.truetype(FONT_PATH, 38)
        pill_text = "NGHỊCH LÝ"
        pbbox = cdraw.textbbox((0, 0), pill_text, font=font_pill)
        pw = pbbox[2] - pbbox[0]
        ph = pbbox[3] - pbbox[1]
        
        pad_x = 35
        pad_y = 16
        pill_w = pw + pad_x * 2
        pill_h = ph + pad_y * 2
        
        pill_left = 1920 - pill_w / 2
        pill_right = 1920 + pill_w / 2
        pill_top = line_y - pill_h / 2
        pill_bottom = line_y + pill_h / 2
        
        # Lines
        for dy in [-2, -1, 0, 1, 2]:
            alpha = int(255 * (1.0 - abs(dy)/3.0))
            cdraw.line([(line_start_x, line_y + dy), (pill_left - 15, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            cdraw.line([(pill_right + 15, line_y + dy), (line_end_x, line_y + dy)], fill=(255, 215, 64, alpha), width=1)
            
        # Draw rounded rectangle
        cdraw.rounded_rectangle([pill_left, pill_top, pill_right, pill_bottom], radius=16, fill=(18, 24, 38, 245), outline=(255, 215, 64, 255), width=3)
        cdraw.text((1920 - pw/2 - pbbox[0], line_y - ph/2 - pbbox[1]), pill_text, font=font_pill, fill=(255, 255, 255, 255))

    # Add soft glow to connector
    glow = conn_layer.filter(ImageFilter.GaussianBlur(12))
    base.alpha_composite(glow)
    base.alpha_composite(conn_layer)
    
    # Paste logos
    base.alpha_composite(hp_styled, (hp_x, hp_y))
    base.alpha_composite(th_styled, (th_x, th_y))
    
    # Save outputs
    out_4k = os.path.join(OUTPUT_DIR, f"{filename_base}_4k.jpg")
    out_1080 = os.path.join(OUTPUT_DIR, f"{filename_base}_1080p.jpg")
    
    rgb = base.convert('RGB')
    rgb.save(out_4k, quality=96)
    rgb.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_1080, quality=96)
    print(f"Rendered {filename_base} successfully!")

render_option('diamond', 'thumb_option_1_diamond_horizon')
render_option('exchange', 'thumb_option_2_bidirectional_node')
render_option('pill_badge', 'thumb_option_3_editorial_badge')
