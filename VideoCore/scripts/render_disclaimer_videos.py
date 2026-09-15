#!/usr/bin/env python3
"""
VideoCore — Master Editorial Disclaimer Video Generator
======================================================
Produces broadcast-grade, synchronized disclaimer videos for:
1. Góc Nhìn Podcast (00_core/disclaimer/)
2. Dòng Chảy (00_core/disclaimer/)

Audio Source: /Users/pro16/Documents/VideoProject/Nhac_nen/tuyenbo-trach-nhiem.wav (25.28s)
"""

import os
import sys
import math
import shutil
import textwrap
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1920, 1080
FPS = 30
DURATION_S = 25.28
TOTAL_FRAMES = int(DURATION_S * FPS)  # 758 frames

SEG_1_END_FRAME = int(11.80 * FPS)  # ~354
SEG_2_END_FRAME = int(20.80 * FPS)  # ~624

AUDIO_PATH = "/Users/pro16/Documents/VideoProject/Nhac_nen/tuyenbo-trach-nhiem.wav"
MUSIC_GOCNHIN = "/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-goc-nhin.mp3"
MUSIC_DONGCHAY = "/Users/pro16/Documents/VideoProject/Nhac_nen/nhac-nen-dong-chay.mp3"

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

# -------------------------------------------------------------
# Base Background Generators
# -------------------------------------------------------------
def generate_gocnhin_base():
    x = np.linspace(-1, 1, W)
    y = np.linspace(-1, 1, H)
    xx, yy = np.meshgrid(x, y)
    dist = np.sqrt(xx**2 + (yy * 1.1)**2)
    dist = np.clip(dist, 0, 1.2) / 1.2

    # Slate Navy #172132 to Deep Charcoal #080C14
    r = (23 * (1 - dist) + 8 * dist).astype(np.uint8)
    g = (33 * (1 - dist) + 12 * dist).astype(np.uint8)
    b = (50 * (1 - dist) + 20 * dist).astype(np.uint8)

    arr = np.stack([r, g, b], axis=-1)
    base = Image.fromarray(arr, 'RGB').convert('RGBA')

    # Amber top glow
    bloom = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bloom)
    bdraw.ellipse([(W//2 - 600, -200), (W//2 + 600, 400)], fill=(217, 119, 6, 28))
    bloom = bloom.filter(ImageFilter.GaussianBlur(80))
    base = Image.alpha_composite(base, bloom)

    # Subtle concentric rings (Dong Son motif)
    rdraw = ImageDraw.Draw(base)
    for rad in [140, 240, 380, 560, 780, 1020]:
        rdraw.ellipse([(W//2 - rad, H//2 - rad), (W//2 + rad, H//2 + rad)], outline=(210, 175, 75, 14), width=1)

    return base

def generate_dongchay_base():
    canyon_path = "/Users/pro16/Documents/VideoProject/Dong_Chay/00_core/branding/banner_gold_canyon.jpg"
    if os.path.exists(canyon_path):
        bg = Image.open(canyon_path).convert('RGBA').resize((W, H))
        overlay = Image.new('RGBA', (W, H), (8, 12, 20, 215))
        base = Image.alpha_composite(bg, overlay)
    else:
        x = np.linspace(-1, 1, W)
        y = np.linspace(-1, 1, H)
        xx, yy = np.meshgrid(x, y)
        dist = np.sqrt(xx**2 + (yy * 1.1)**2)
        dist = np.clip(dist, 0, 1.2) / 1.2

        r = (18 * (1 - dist) + 6 * dist).astype(np.uint8)
        g = (28 * (1 - dist) + 10 * dist).astype(np.uint8)
        b = (44 * (1 - dist) + 16 * dist).astype(np.uint8)
        arr = np.stack([r, g, b], axis=-1)
        base = Image.fromarray(arr, 'RGB').convert('RGBA')

    # Cyan top-center bloom
    bloom = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bloom)
    bdraw.ellipse([(W//2 - 500, -180), (W//2 + 500, 380)], fill=(0, 195, 215, 25))
    bloom = bloom.filter(ImageFilter.GaussianBlur(70))
    base = Image.alpha_composite(base, bloom)

    return base

# -------------------------------------------------------------
# Micro Particles Simulation (Drifting specks)
# -------------------------------------------------------------
np.random.seed(42)
NUM_PARTICLES = 36
P_X = np.random.uniform(80, W - 80, NUM_PARTICLES)
P_Y = np.random.uniform(60, H - 60, NUM_PARTICLES)
P_SPEED = np.random.uniform(0.15, 0.45, NUM_PARTICLES)
P_SIZE = np.random.uniform(1.5, 3.5, NUM_PARTICLES)
P_ALPHA = np.random.uniform(25, 75, NUM_PARTICLES)

def draw_particles(img, frame_idx, p_color=(245, 205, 80)):
    layer = Image.new('RGBA', (W, H), (0,0,0,0))
    pdraw = ImageDraw.Draw(layer)
    for i in range(NUM_PARTICLES):
        cur_y = (P_Y[i] - frame_idx * P_SPEED[i]) % (H - 120) + 60
        cur_x = P_X[i] + math.sin(frame_idx * 0.03 + i) * 15
        sz = P_SIZE[i]
        alpha = int(P_ALPHA[i] * (0.7 + 0.3 * math.sin(frame_idx * 0.05 + i)))
        col = (p_color[0], p_color[1], p_color[2], alpha)
        pdraw.ellipse([(cur_x - sz, cur_y - sz), (cur_x + sz, cur_y + sz)], fill=col)
    return Image.alpha_composite(img, layer)

# -------------------------------------------------------------
# Frame Render Engine
# -------------------------------------------------------------
def render_frame(channel, base_img, frame_idx, fonts, avatar_img, is_static=False):
    if is_static:
        weights = [1.0, 1.0, 1.0]
    else:
        w0, w1, w2 = 0.0, 0.0, 0.0
        fade_len = 12 # frames (~0.4s)
        
        if frame_idx < SEG_1_END_FRAME - fade_len:
            w0 = 1.0
        elif frame_idx < SEG_1_END_FRAME:
            p = (frame_idx - (SEG_1_END_FRAME - fade_len)) / fade_len
            w0 = 1.0 - p
            w1 = p
        elif frame_idx < SEG_2_END_FRAME - fade_len:
            w1 = 1.0
        elif frame_idx < SEG_2_END_FRAME:
            p = (frame_idx - (SEG_2_END_FRAME - fade_len)) / fade_len
            w1 = 1.0 - p
            w2 = p
        else:
            w2 = 1.0

        weights = [w0, w1, w2]
    img = base_img.copy()
    draw = ImageDraw.Draw(img)

    is_gocnhin = (channel == 'gocnhin')

    # Color definitions
    c_gold = (248, 212, 105)
    c_cyan = (0, 215, 230)
    c_header_accent = (215, 195, 145) if is_gocnhin else c_cyan
    c_border_outer = (190, 150, 65, 120) if is_gocnhin else (210, 165, 60, 140)
    c_corner = (245, 205, 85) if is_gocnhin else (0, 215, 230)

    # 1. Outer refined border & corners
    draw.rectangle([(50, 40), (1870, 1040)], outline=c_border_outer, width=1)
    c_len = 32
    for cx, cy in [(50, 40), (1870, 40), (50, 1040), (1870, 1040)]:
        dx = 1 if cx == 50 else -1
        dy = 1 if cy == 40 else -1
        draw.line([(cx, cy), (cx + dx * c_len, cy)], fill=c_corner, width=3)
        draw.line([(cx, cy), (cx, cy + dy * c_len)], fill=c_corner, width=3)

    # 2. Header
    title_text = "TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM"
    sub_text = "GÓC NHÌN PODCAST  —  NGHIÊN CỨU & PHÂN TÍCH ĐỘC LẬP" if is_gocnhin else "DÒNG CHẢY  —  KINH TẾ CHÍNH TRỊ & KHOA HỌC ỨNG DỤNG"
    draw.text((960, 90), title_text, font=fonts['title'], fill=c_gold, anchor='mm')
    draw.text((960, 138), sub_text, font=fonts['sub'], fill=c_header_accent, anchor='mm')

    # 3. Cards Data
    if is_gocnhin:
        cards_data = [
            (
                "1. NGUỒN DỮ LIỆU & NGHIÊN CỨU ĐỘC LẬP",
                "Toàn bộ nội dung trong video được nghiên cứu, tổng hợp và biên tập độc lập dựa trên các báo cáo tài chính, tài liệu thống kê và nguồn dữ liệu công khai từ các cơ quan chính phủ và các tổ chức kinh tế uy tín.",
                "DỮ LIỆU THỰC CHỨNG"
            ),
            (
                "2. PHI TƯ VẤN ĐẦU TƯ TÀI CHÍNH",
                "Mọi thông tin mang tính chất chia sẻ góc nhìn vĩ mô và phân tích học thuật, KHÔNG cấu thành lời khuyên đầu tư tài chính hay khuyến nghị mua bán tài sản dưới mọi hình thức.",
                "GÓC NHÌN HỌC THUẬT"
            ),
            (
                "3. QUYẾT ĐỊNH SÁNG SUỐT & BỀN VỮNG",
                "Kính chúc quý khán giả luôn có những quyết định sáng suốt và bền vững. Khán giả tự chịu trách nhiệm hoàn toàn đối với mọi quyết định tài chính và đầu tư cá nhân.",
                "TỈNH TÁO VỚI TIỀN - TỰ DO VỚI ĐỜI"
            )
        ]
    else:
        cards_data = [
            (
                "1. NGUỒN DỮ LIỆU & HỒ SƠ CÔNG KHAI",
                "Toàn bộ nội dung trong video được nghiên cứu, tổng hợp và biên tập độc lập dựa trên các báo cáo tài chính, tài liệu thống kê và nguồn dữ liệu công khai từ các cơ quan chính phủ và các tổ chức kinh tế uy tín.",
                "BÁM SÁT DỮ LIỆU THỰC CHỨNG"
            ),
            (
                "2. PHI TƯ VẤN ĐẦU TƯ TÀI CHÍNH",
                "Mọi thông tin mang tính chất chia sẻ góc nhìn vĩ mô và phân tích học thuật, KHÔNG cấu thành lời khuyên đầu tư tài chính hay khuyến nghị giao dịch vốn dưới mọi hình thức.",
                "KHOA HỌC KINH TẾ CHÍNH TRỊ"
            ),
            (
                "3. QUYẾT ĐỊNH SÁNG SUỐT & BỀN VỮNG",
                "Kính chúc quý khán giả luôn có những quyết định sáng suốt và bền vững trong quản trị dòng vốn, nhìn thấu các quy luật kinh tế và sự vận động của thị trường.",
                "GIẢI MÃ BẢN CHẤT DÒNG TIỀN"
            )
        ]

    card_w = 1560
    card_h = 190
    start_x = 180
    start_y = 205
    spacing = 30

    for i, (head, body, tag) in enumerate(cards_data):
        cy = start_y + i * (card_h + spacing)
        weight = weights[i]
        vis_weight = 1.0 if is_static else (0.35 + 0.65 * weight)

        # Dynamic glow on active card
        if weight > 0.1 or is_static:
            glow_layer = Image.new('RGBA', (W, H), (0,0,0,0))
            gdraw = ImageDraw.Draw(glow_layer)
            glow_alpha = int(38 * (1.0 if is_static else weight))
            glow_color = (217, 119, 6, glow_alpha) if is_gocnhin else (0, 195, 215, glow_alpha)
            gdraw.rounded_rectangle([(start_x - 10, cy - 8), (start_x + card_w + 10, cy + card_h + 8)], radius=18, fill=glow_color)
            glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(14))
            img = Image.alpha_composite(img, glow_layer)
            draw = ImageDraw.Draw(img)

        # Interpolated Card styling
        card_fill = lerp_color((13, 20, 32, 195), (26, 38, 58, 240) if is_gocnhin else (18, 30, 48, 235), vis_weight)
        border_active = (245, 195, 75, 255) if is_gocnhin else (0, 215, 230, 255)
        border_inactive = (65, 85, 115, 180) if is_gocnhin else (50, 80, 110, 180)
        b_color = lerp_color(border_inactive, border_active, vis_weight)
        b_width = 2 if vis_weight > 0.5 else 1

        draw.rounded_rectangle([(start_x, cy), (start_x + card_w, cy + card_h)], radius=12, fill=card_fill, outline=b_color, width=b_width)

        # Left indicator bar
        ind_active = (250, 195, 65) if is_gocnhin else (0, 220, 235)
        ind_inactive = (60, 80, 105)
        ind_color = lerp_color(ind_inactive, ind_active, vis_weight)
        draw.rounded_rectangle([(start_x + 3, cy + 12), (start_x + 9, cy + card_h - 12)], radius=3, fill=ind_color)

        # Header text color
        h_active = (255, 222, 115) if is_gocnhin else (255, 225, 120)
        h_inactive = (185, 198, 215)
        h_col = lerp_color(h_inactive, h_active, vis_weight)
        draw.text((start_x + 38, cy + 33), head, font=fonts['card_h'], fill=h_col)

        # Tag badge
        badge_fill = lerp_color((18, 26, 38), (45, 60, 85) if is_gocnhin else (25, 45, 65), vis_weight)
        tag_col = lerp_color((170, 185, 205), h_active if is_gocnhin else c_cyan, vis_weight)
        draw.rounded_rectangle([(start_x + card_w - 290, cy + 24), (start_x + card_w - 25, cy + 56)], radius=6, fill=badge_fill, outline=b_color, width=1)
        draw.text((start_x + card_w - 158, cy + 39), tag, font=fonts['tag'], fill=tag_col, anchor='mm')

        # Body text
        body_col = lerp_color((175, 185, 198), (250, 250, 255), vis_weight)
        wrapped = textwrap.fill(body, width=95)
        draw.text((start_x + 38, cy + 82), wrapped, font=fonts['card_body'], fill=body_col, spacing=10)

    # 4. Footer with circular Avatar (ABSOLUTELY NO CONTACT INFO / NO URLS)
    if avatar_img:
        av_pos = (start_x + 20, 905)
        img.paste(avatar_img, av_pos, avatar_img)
        rim_col = (220, 180, 75) if is_gocnhin else (0, 210, 225)
        draw.ellipse([(av_pos[0] - 2, av_pos[1] - 2), (av_pos[0] + 102, av_pos[1] + 102)], outline=rim_col, width=3)

    if is_gocnhin:
        draw.text((start_x + 145, 936), "GÓC NHÌN PODCAST  —  TỈNH TÁO VỚI TIỀN, TỰ DO VỚI ĐỜI", font=fonts['footer'], fill=c_gold)
        draw.text((start_x + 145, 974), "Không gian chia sẻ góc nhìn vĩ mô & Phân tích kinh tế - xã hội độc lập", font=fonts['footer_sub'], fill=c_header_accent)
    else:
        draw.text((start_x + 145, 936), "DÒNG CHẢY  —  GIẢI MÃ BẢN CHẤT THIẾT CHẾ, BÓC TRẦN ĐỊA CHÍNH TRỊ DÒNG TIỀN", font=fonts['footer'], fill=c_gold)
        draw.text((start_x + 145, 974), "Hồ sơ nghiên cứu độc lập & Khảo cứu lịch sử, thể chế, địa chính trị", font=fonts['footer_sub'], fill=c_cyan)

    # 5. Floating ambient particles
    p_col = (245, 205, 80) if is_gocnhin else (0, 210, 225)
    img = draw_particles(img, frame_idx if not is_static else 60, p_col)

    # 6. Subtle slow zoom (camera push-in 1.0 -> 1.025 for video only)
    if not is_static:
        scale = 1.0 + 0.025 * (frame_idx / TOTAL_FRAMES)
        if scale > 1.001:
            crop_w = int(W / scale)
            crop_h = int(H / scale)
            crop_x = (W - crop_w) // 2
            crop_y = (H - crop_h) // 2
            cropped = img.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
            img = cropped.resize((W, H), Image.Resampling.BILINEAR)

    return img.convert('RGB')

# -------------------------------------------------------------
# Master Rendering Routine
# -------------------------------------------------------------
def build_avatar(path):
    if not os.path.exists(path):
        return None
    av = Image.open(path).convert('RGBA').resize((100, 100))
    mask = Image.new('L', (100, 100), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 100, 100), fill=255)
    av_round = Image.new('RGBA', (100, 100), (0,0,0,0))
    av_round.paste(av, (0, 0), mask)
    return av_round

def render_channel(channel_type, out_dir):
    print(f"\n==================================================", flush=True)
    print(f"🎬 RENDERING DISCLAIMER VIDEO & IMAGES FOR: {channel_type.upper()}", flush=True)
    print(f"📁 Output Directory: {out_dir}", flush=True)
    print(f"==================================================", flush=True)

    os.makedirs(out_dir, exist_ok=True)

    fonts = {
        'title': ImageFont.truetype(FONT_BOLD, 48),
        'sub': ImageFont.truetype(FONT_BOLD, 21),
        'card_h': ImageFont.truetype(FONT_BOLD, 25),
        'card_body': ImageFont.truetype(FONT_REG, 21),
        'footer': ImageFont.truetype(FONT_BOLD, 21),
        'footer_sub': ImageFont.truetype(FONT_REG, 17),
        'tag': ImageFont.truetype(FONT_BOLD, 15)
    }

    if channel_type == 'gocnhin':
        base_img = generate_gocnhin_base()
        avatar = build_avatar("/Users/pro16/Documents/VideoProject/GocNhinPodcast/profile/avtar2.jpeg")
        music_file = MUSIC_GOCNHIN
        prefix = "tuyenbo_trachnhiem_gocnhinpodcast"
    else:
        base_img = generate_dongchay_base()
        avatar = build_avatar("/Users/pro16/Documents/VideoProject/Dong_Chay/00_core/branding/avatar_obsidian_gold.jpg")
        music_file = MUSIC_DONGCHAY
        prefix = "tuyenbo_trachnhiem_dongchay"

    # Save high-res static disclaimer images with ALL 3 CARDS fully active & illuminated (is_static=True)
    poster_static = render_frame(channel_type, base_img, 0, fonts, avatar, is_static=True)
    
    # 1. Standard poster jpg & png
    poster_path = os.path.join(out_dir, f"{prefix}_poster.jpg")
    poster_static.save(poster_path, quality=98)
    poster_png_path = os.path.join(out_dir, f"{prefix}_poster.png")
    poster_static.save(poster_png_path)
    
    # 2. Dedicated Vietnamese named files for CapCut convenience
    anh_mientru_png = os.path.join(out_dir, f"{prefix}_anh_tuyenbo_mientru.png")
    anh_mientru_jpg = os.path.join(out_dir, f"{prefix}_anh_tuyenbo_mientru.jpg")
    poster_static.save(anh_mientru_png)
    poster_static.save(anh_mientru_jpg, quality=98)
    print(f"✅ High-res static disclaimer images saved (JPG + Lossless PNG): {poster_path}", flush=True)

    # Destination paths
    out_video_clean = os.path.join(out_dir, f"{prefix}_clean_audio.mp4")
    out_video_mixed = os.path.join(out_dir, f"{prefix}.mp4")

    # 1. First encode raw video with clean voiceover
    cmd_clean = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",  # pipe from stdin
        "-i", AUDIO_PATH,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_video_clean
    ]

    print(f"🚀 Streaming {TOTAL_FRAMES} frames into FFmpeg (Clean Vocal)...", flush=True)
    proc = subprocess.Popen(cmd_clean, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for f in range(TOTAL_FRAMES):
        frame = render_frame(channel_type, base_img, f, fonts, avatar)
        proc.stdin.write(frame.tobytes())
        if f % 150 == 0:
            pct = (f / TOTAL_FRAMES) * 100
            print(f"   [{f}/{TOTAL_FRAMES}] {pct:.1f}% rendered...", flush=True)

    proc.stdin.close()
    proc.wait()
    print(f"✅ Clean audio video generated: {out_video_clean} ({os.path.getsize(out_video_clean)/1024/1024:.2f} MB)", flush=True)

    # 2. Mix with signature background music (subtle -22dB with 1s fade-in & 1.5s fade-out)
    if os.path.exists(music_file):
        print(f"🎵 Mixing signature background music ({os.path.basename(music_file)})...", flush=True)
        filter_complex = (
            f"[1:a]volume=1.0[vocal];"
            f"[2:a]volume=0.08,afade=t=in:ss=0:d=1.0,afade=t=out:st={DURATION_S - 1.5}:d=1.5[music];"
            f"[vocal][music]amix=inputs=2:duration=first:dropout_transition=2[aout]"
        )
        cmd_mixed = [
            "ffmpeg", "-y",
            "-i", out_video_clean,
            "-i", AUDIO_PATH,
            "-i", music_file,
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            out_video_mixed
        ]
        subprocess.run(cmd_mixed, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Master mixed video generated: {out_video_mixed} ({os.path.getsize(out_video_mixed)/1024/1024:.2f} MB)", flush=True)
    else:
        shutil.copy(out_video_clean, out_video_mixed)

    # 3. Copy source audio & write README documentation
    dest_audio = os.path.join(out_dir, "tuyenbo-trach-nhiem.wav")
    shutil.copy(AUDIO_PATH, dest_audio)

    readme_content = f"""# Thư Mục Quản Lý Video Tuyên Bố Trách Nhiệm (Disclaimer Assets)
**Kênh:** {channel_type.upper()}  
**Thời lượng chuẩn:** 25.28 giây (758 frames @ 30fps, 1080p Full HD)  
**Tệp âm thanh gốc:** `tuyenbo-trach-nhiem.wav`

---

## 📂 Danh Mục Tài Nguyên Thành Phẩm (Deliverables)

1. **`{prefix}.mp4`** *(Bản Master hoàn chỉnh)*:
   - Video Full HD 1080p với hiệu ứng chuyển động camera slow-zoom, card đồng bộ giọng đọc và **nhạc nền nhận diện kênh phối âm chuẩn -22dB**.
   - Dùng kéo thả trực tiếp vào cuối timeline CapCut / Premiere.

2. **`{prefix}_clean_audio.mp4`** *(Bản Vocal sạch không nhạc nền)*:
   - Video Full HD 1080p chỉ chứa giọng đọc thuyết minh gốc.
   - Thích hợp khi dựng CapCut mà dự án đã có track nhạc nền riêng chạy xuyên suốt.

3. **`{prefix}_anh_tuyenbo_mientru.png`** / **`{prefix}_poster.png`** *(Ảnh Tĩnh Độ Nét Cao Không Nén)*:
   - Ảnh tĩnh Full HD 1080p định dạng PNG Lossless, 3 khối nội dung được chiếu sáng rõ nét 100%, không chứa thông tin liên hệ.
   - Thích hợp kéo thả trực tiếp làm slide ảnh tĩnh trong CapCut/Photoshop.

4. **`{prefix}_anh_tuyenbo_mientru.jpg`** / **`{prefix}_poster.jpg`** *(Ảnh Tĩnh JPG 98% chất lượng)*:
   - Bản JPG siêu nét dung lượng nhẹ.

5. **`tuyenbo-trach-nhiem.wav`**:
   - Tệp âm thanh thuyết minh gốc (24kHz, 16-bit PCM).

---

## 🎙️ Lời Thoại Thuyết Minh & Mốc Phân Đoạn (Script Lineage)

| Phân đoạn | Thời gian | Nội dung thuyết minh | Điểm nhấn thị giác |
|---|:---:|---|---|
| **Đoạn 1** | `00:00 - 00:11.8` | *\"Toàn bộ nội dung trong video được nghiên cứu, tổng hợp và biên tập độc lập dựa trên các báo cáo tài chính, tài liệu thống kê và nguồn dữ liệu công khai từ các cơ quan chính phủ và các tổ chức kinh tế uy tín.\"* | Sáng khung Card 1 (Dữ liệu thực chứng) |
| **Đoạn 2** | `00:11.8 - 00:20.8` | *\"Mọi thông tin mang tính chất chia sẻ góc nhìn vĩ mô và phân tích học thuật, không cấu thành lời khuyên đầu tư tài chính dưới mọi hình thức.\"* | Sáng khung Card 2 (Phi tư vấn đầu tư) |
| **Đoạn 3** | `00:20.8 - 00:25.28` | *\"Kính chúc quý khán giả luôn có những quyết định sáng suốt và bền vững.\"* | Sáng khung Card 3 (Trách nhiệm & Bền vững) |
"""
    readme_path = os.path.join(out_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"✅ Documentation written: {readme_path}\n", flush=True)

if __name__ == "__main__":
    gocnhin_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/00_core/disclaimer"
    dongchay_dir = "/Users/pro16/Documents/VideoProject/Dong_Chay/00_core/disclaimer"

    render_channel("gocnhin", gocnhin_dir)
    render_channel("dongchay", dongchay_dir)
    print("🎉 ALL DISCLAIMER ASSETS SUCCESSFULLY GENERATED!")
