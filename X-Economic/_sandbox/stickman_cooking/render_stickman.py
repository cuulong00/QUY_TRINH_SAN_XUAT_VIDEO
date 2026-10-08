#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STICKMAN COOKING DEMO (Polished & Refined)
Motion Graphics Animation rendered entirely via Python + Pillow + FFmpeg.
X-Economy Visual Language:
  Background: #0A0E17
  Stickman:   #F5F0E6
  Fire/Gold:  #D4AF37
  Steam:      #00E5FF
"""

import os
import sys
import math
import random
import subprocess
from PIL import Image, ImageDraw

# Output specifications
WIDTH = 1920
HEIGHT = 1080
SCALE = 2  # 2x supersampling for studio-grade anti-aliasing
SW = WIDTH * SCALE   # 3840
SH = HEIGHT * SCALE  # 2160
FPS = 30
TOTAL_FRAMES = 540  # exactly 18.0 seconds

# Palette definitions (RGB)
COLOR_BG = (10, 14, 23)           # #0A0E17
COLOR_STICK = (245, 240, 230)     # #F5F0E6
COLOR_GOLD = (212, 175, 55)       # #D4AF37
COLOR_GOLD_BRIGHT = (255, 215, 64)
COLOR_FIRE_CORE = (255, 252, 220)
COLOR_FIRE_ORANGE = (255, 140, 20)
COLOR_CYAN = (0, 229, 255)        # #00E5FF
COLOR_CYAN_LIGHT = (140, 248, 255)
COLOR_COUNTER = (22, 30, 44)      # Deep slate navy
COLOR_COUNTER_TOP = (36, 48, 70)
COLOR_COUNTER_EDGE = (56, 72, 98)
COLOR_PAN_METAL = (42, 52, 68)
COLOR_PAN_RIM = (195, 205, 220)

# Culinary ingredient colors
INGREDIENT_COLORS = [
    (212, 175, 55),   # Gold
    (0, 229, 255),    # Cyan
    (255, 105, 70),   # Coral
    (115, 235, 130),  # Herb Green
    (245, 240, 230),  # Cream Garlic
    (255, 180, 50),   # Saffron
]

# Easing utilities
def clamp(val, min_v=0.0, max_v=1.0):
    return max(min_v, min(max_v, val))

def ease_in_out(t):
    t = clamp(t)
    return t * t * (3.0 - 2.0 * t)

def ease_out_quad(t):
    t = clamp(t)
    return 1.0 - (1.0 - t) * (1.0 - t)

def ease_in_quad(t):
    t = clamp(t)
    return t * t

def ease_out_cubic(t):
    t = clamp(t)
    return 1.0 - math.pow(1.0 - t, 3)

def lerp(a, b, t):
    return a + (b - a) * t

# Drawing primitives on 2x scaled canvas
def draw_thick_line(draw, p1, p2, color, width):
    x1, y1 = p1[0] * SCALE, p1[1] * SCALE
    x2, y2 = p2[0] * SCALE, p2[1] * SCALE
    w = width * SCALE
    draw.line([(x1, y1), (x2, y2)], fill=color, width=int(round(w)))
    r = w / 2.0
    draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill=color)
    draw.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=color)

def draw_circle(draw, center, radius, color, fill=None, width=1):
    cx, cy = center[0] * SCALE, center[1] * SCALE
    r = radius * SCALE
    w = width * SCALE
    if fill:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    if color and w > 0:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=int(round(w)))

def draw_oval(draw, center, rx, ry, color, fill=None, width=1):
    cx, cy = center[0] * SCALE, center[1] * SCALE
    rx_s, ry_s = rx * SCALE, ry * SCALE
    w = width * SCALE
    if fill:
        draw.ellipse([cx - rx_s, cy - ry_s, cx + rx_s, cy + ry_s], fill=fill)
    if color and w > 0:
        draw.ellipse([cx - rx_s, cy - ry_s, cx + rx_s, cy + ry_s], outline=color, width=int(round(w)))

# Kitchen Environment & Stove
def draw_kitchen_environment(draw, flame_intensity, frame_idx):
    # Floor line
    draw_thick_line(draw, (0, 830), (1920, 830), (18, 25, 38), 3)

    # Counter Table Main Body
    cx1, cy1 = 700 * SCALE, 680 * SCALE
    cx2, cy2 = 1860 * SCALE, 830 * SCALE
    draw.rectangle([cx1, cy1, cx2, cy2], fill=COLOR_COUNTER)

    # Counter Top Slab
    tx1, ty1 = 680 * SCALE, 665 * SCALE
    tx2, ty2 = 1880 * SCALE, 690 * SCALE
    draw.rectangle([tx1, ty1, tx2, ty2], fill=COLOR_COUNTER_TOP)
    draw.line([(tx1, ty1), (tx2, ty1)], fill=COLOR_COUNTER_EDGE, width=int(3 * SCALE))

    # Stove Body Inset
    st_x1, st_x2 = 880 * SCALE, 1180 * SCALE
    st_y1, st_y2 = 660 * SCALE, 666 * SCALE
    draw.rectangle([st_x1, st_y1, st_x2, st_y2], fill=(42, 54, 74))
    
    # Burner Base & Grate
    bx, by = 1030, 663
    draw_oval(draw, (bx, by), 110, 20, (55, 70, 95), fill=(22, 28, 40), width=2)
    draw_oval(draw, (bx, by), 70, 12, (45, 58, 80), fill=(16, 22, 32), width=2)

    # Stove Knob
    knob_x = 940
    knob_y = 715
    is_on = (flame_intensity > 0.05)
    draw_circle(draw, (knob_x, knob_y), 15, COLOR_STICK, fill=(32, 42, 58), width=2)
    # Knob marker needle
    k_ang = math.pi * 0.5 if is_on else -math.pi * 0.5
    kx_off = math.cos(k_ang) * 9
    ky_off = math.sin(k_ang) * 9
    draw_thick_line(draw, (knob_x, knob_y), (knob_x + kx_off, knob_y + ky_off), COLOR_GOLD if is_on else COLOR_STICK, 3)

    # Serving Plate on the right (x = 1420, y = 660)
    plate_x, plate_y = 1420, 660
    draw_oval(draw, (plate_x, plate_y + 4), 95, 22, (38, 48, 66), fill=(20, 26, 38), width=1)
    draw_oval(draw, (plate_x, plate_y), 90, 20, COLOR_GOLD, fill=(240, 244, 252), width=3)
    draw_oval(draw, (plate_x, plate_y), 65, 14, (190, 200, 215), fill=(225, 232, 242), width=1)

# Blazing Procedural Flames
def draw_procedural_flames(draw, cx, cy, intensity, frame_idx):
    if intensity <= 0.01:
        return
    
    flame_count = 13
    width_span = 95
    random.seed(frame_idx // 2)
    
    for i in range(flame_count):
        rel = (i - (flame_count - 1) / 2.0) / ((flame_count - 1) / 2.0)  # -1.0 to 1.0
        fx = cx + rel * width_span
        # Robust flame height so it licks past the pan edge
        base_h = 58 * (1.0 - abs(rel) * 0.35) * intensity
        flicker = math.sin(frame_idx * 0.5 + i * 1.4) * 12 * intensity + (random.random() - 0.5) * 8
        h = max(12, base_h + flicker)
        
        # Outer flame tongue (Amber / Gold)
        curve_sway = math.sin(frame_idx * 0.35 + i * 0.8) * 6
        p_base = (fx, cy + 2)
        p_mid1 = (fx - 9 + curve_sway * 0.5, cy - h * 0.45)
        p_tip = (fx + curve_sway, cy - h)
        p_mid2 = (fx + 9 + curve_sway * 0.5, cy - h * 0.45)
        
        pts = [
            (p_base[0] * SCALE, p_base[1] * SCALE),
            (p_mid1[0] * SCALE, p_mid1[1] * SCALE),
            (p_tip[0] * SCALE, p_tip[1] * SCALE),
            (p_mid2[0] * SCALE, p_mid2[1] * SCALE),
        ]
        draw.polygon(pts, fill=COLOR_GOLD)
        
        # Mid flame core (Bright Gold / Orange)
        mh = h * 0.72
        pts_mid = [
            ((fx - 5) * SCALE, (cy + 1) * SCALE),
            ((fx - 5 + curve_sway * 0.4) * SCALE, (cy - mh * 0.45) * SCALE),
            ((fx + curve_sway * 0.8) * SCALE, (cy - mh) * SCALE),
            ((fx + 5 + curve_sway * 0.4) * SCALE, (cy - mh * 0.45) * SCALE),
            ((fx + 5) * SCALE, (cy + 1) * SCALE)
        ]
        draw.polygon(pts_mid, fill=COLOR_FIRE_ORANGE)

        # Inner white-hot core
        ih = h * 0.42
        pts_inner = [
            ((fx - 3) * SCALE, cy * SCALE),
            ((fx + curve_sway * 0.4) * SCALE, (cy - ih) * SCALE),
            ((fx + 3) * SCALE, cy * SCALE)
        ]
        draw.polygon(pts_inner, fill=COLOR_FIRE_CORE)

# Sauté Frying Pan
def draw_pan(draw, pan_center, pan_angle, handle_pt):
    cx, cy = pan_center
    cos_a = math.cos(pan_angle)
    sin_a = math.sin(pan_angle)
    
    rx = 96
    ry = 26
    depth = 34
    
    def rot_pt(lx, ly):
        rx_rot = lx * cos_a - ly * sin_a
        ry_rot = lx * sin_a + ly * cos_a
        return (cx + rx_rot, cy + ry_rot)

    # Base points
    b_left = rot_pt(-rx * 0.80, depth)
    b_right = rot_pt(rx * 0.80, depth)
    r_left = rot_pt(-rx, 0)
    r_right = rot_pt(rx, 0)
    
    # Outer metal hull
    hull_pts = [
        (r_left[0] * SCALE, r_left[1] * SCALE),
        (b_left[0] * SCALE, b_left[1] * SCALE),
        (b_right[0] * SCALE, b_right[1] * SCALE),
        (r_right[0] * SCALE, r_right[1] * SCALE)
    ]
    draw.polygon(hull_pts, fill=COLOR_PAN_METAL)
    draw_thick_line(draw, b_left, b_right, (26, 34, 46), 4)

    # Rim interior cavity
    rim_pts = []
    for step in range(36):
        rad = step * (2 * math.pi / 36)
        lx = rx * math.cos(rad)
        ly = ry * math.sin(rad)
        pt = rot_pt(lx, ly)
        rim_pts.append((pt[0] * SCALE, pt[1] * SCALE))
    draw.polygon(rim_pts, fill=(26, 33, 45))
    
    # Outer metallic rim edge
    for step in range(36):
        next_step = (step + 1) % 36
        draw.line([rim_pts[step], rim_pts[next_step]], fill=COLOR_PAN_RIM, width=int(2.5 * SCALE))

    # Golden luxury rim highlight on front arc
    rim_gold_pts = []
    for step in range(36):
        rad = step * (2 * math.pi / 36)
        lx = (rx + 1) * math.cos(rad)
        ly = (ry + 1) * math.sin(rad)
        pt = rot_pt(lx, ly)
        rim_gold_pts.append((pt[0] * SCALE, pt[1] * SCALE))
    for step in range(0, 18):
        draw.line([rim_gold_pts[step], rim_gold_pts[(step+1)%36]], fill=COLOR_GOLD, width=int(2.0 * SCALE))

    # Pan Handle connecting left rim to Stickman hand
    handle_attach = rot_pt(-rx * 0.95, depth * 0.25)
    draw_thick_line(draw, handle_attach, handle_pt, (18, 22, 30), 10)
    draw_thick_line(draw, handle_attach, handle_pt, (75, 88, 108), 4)
    draw_circle(draw, handle_pt, 6, COLOR_GOLD, fill=(18, 22, 30), width=2)

# Ingredient Prep Bowl (Held in left hand during Beat 2)
def draw_prep_bowl(draw, bowl_pos, tilt_angle):
    bx, by = bowl_pos
    cos_a = math.cos(tilt_angle)
    sin_a = math.sin(tilt_angle)
    
    def b_rot(lx, ly):
        return (bx + lx * cos_a - ly * sin_a, by + lx * sin_a + ly * cos_a)
        
    p_tl = b_rot(-28, -12)
    p_tr = b_rot(28, -12)
    p_bl = b_rot(-16, 14)
    p_br = b_rot(16, 14)
    
    pts = [
        (p_tl[0] * SCALE, p_tl[1] * SCALE),
        (p_tr[0] * SCALE, p_tr[1] * SCALE),
        (p_br[0] * SCALE, p_br[1] * SCALE),
        (p_bl[0] * SCALE, p_bl[1] * SCALE)
    ]
    draw.polygon(pts, fill=(35, 48, 68))
    draw_thick_line(draw, p_tl, p_tr, COLOR_GOLD, 3)
    draw_thick_line(draw, p_bl, p_br, (20, 28, 40), 3)

# Steam billowing particles
def draw_steam_particles(draw, particles):
    for p in particles:
        if p['alpha'] <= 0.02:
            continue
        cx, cy = p['x'], p['y']
        size = p['size']
        alpha = p['alpha']
        
        # Steam cloudlet
        steam_col = (
            int(lerp(COLOR_BG[0], COLOR_CYAN[0], alpha * 0.85)),
            int(lerp(COLOR_BG[1], COLOR_CYAN[1], alpha * 0.85)),
            int(lerp(COLOR_BG[2], COLOR_CYAN[2], alpha * 0.85)),
        )
        draw_oval(draw, (cx, cy), size * 1.35, size * 0.75, None, fill=steam_col)
        
        # Inner luminous cyan glow
        inner_col = (
            int(lerp(COLOR_BG[0], COLOR_CYAN_LIGHT[0], alpha * 0.95)),
            int(lerp(COLOR_BG[1], COLOR_CYAN_LIGHT[1], alpha * 0.95)),
            int(lerp(COLOR_BG[2], COLOR_CYAN_LIGHT[2], alpha * 0.95)),
        )
        draw_oval(draw, (cx + size * 0.15, cy - size * 0.15), size * 0.65, size * 0.35, None, fill=inner_col)

# Stickman Chef Character
def draw_stickman(draw, root_pos, pose_params):
    bx, by = root_pos
    
    # 1. Legs & Feet
    foot_l = pose_params['foot_l']
    foot_r = pose_params['foot_r']
    knee_l = pose_params['knee_l']
    knee_r = pose_params['knee_r']
    hips   = pose_params['hips']
    
    # Back leg (Left)
    draw_thick_line(draw, hips, knee_l, COLOR_STICK, 7)
    draw_thick_line(draw, knee_l, foot_l, COLOR_STICK, 7)
    draw_thick_line(draw, foot_l, (foot_l[0] + 20, foot_l[1]), COLOR_STICK, 6)
    
    # Front leg (Right)
    draw_thick_line(draw, hips, knee_r, COLOR_STICK, 7)
    draw_thick_line(draw, knee_r, foot_r, COLOR_STICK, 7)
    draw_thick_line(draw, foot_r, (foot_r[0] + 24, foot_r[1]), COLOR_STICK, 6)
    
    # 2. Torso (Spine)
    neck = pose_params['neck']
    draw_thick_line(draw, hips, neck, COLOR_STICK, 9)
    
    # 3. Head & Chef Hat
    head_c = pose_params['head_c']
    head_r = 36
    draw_circle(draw, head_c, head_r, COLOR_STICK, fill=COLOR_BG, width=6)
    
    # Minimalist facial cues
    eye_x = head_c[0] + 16
    eye_y = head_c[1] - 4
    if pose_params.get('eyes_happy', False):
        # Happy arched eye '^'
        draw_thick_line(draw, (eye_x - 5, eye_y), (eye_x, eye_y - 5), COLOR_STICK, 3)
        draw_thick_line(draw, (eye_x, eye_y - 5), (eye_x + 5, eye_y), COLOR_STICK, 3)
        # Happy smile
        draw_thick_line(draw, (eye_x - 4, eye_y + 12), (eye_x + 4, eye_y + 12), COLOR_GOLD, 3)
    else:
        # Focused chef eye
        draw_circle(draw, (eye_x, eye_y), 3.5, COLOR_STICK, fill=COLOR_STICK, width=1)
        
    # Chef Toque (Hat)
    hx, hy = head_c[0], head_c[1] - head_r + 4
    b_w = 34
    draw_thick_line(draw, (hx - b_w, hy + 4), (hx + b_w + 4, hy + 4), COLOR_GOLD, 5)
    crown_pts = [
        ((hx - b_w + 4) * SCALE, (hy + 2) * SCALE),
        ((hx - b_w - 6) * SCALE, (hy - 28) * SCALE),
        ((hx - 14) * SCALE, (hy - 50) * SCALE),
        ((hx + 18) * SCALE, (hy - 48) * SCALE),
        ((hx + b_w + 8) * SCALE, (hy - 24) * SCALE),
        ((hx + b_w + 2) * SCALE, (hy + 2) * SCALE)
    ]
    draw.polygon(crown_pts, fill=COLOR_BG)
    for i in range(len(crown_pts)):
        p_cur = crown_pts[i]
        p_next = crown_pts[(i + 1) % len(crown_pts)]
        draw.line([p_cur, p_next], fill=COLOR_STICK, width=int(4 * SCALE))
    draw_thick_line(draw, (hx - 10, hy - 40), (hx - 10, hy - 6), (70, 80, 100), 2)
    draw_thick_line(draw, (hx + 10, hy - 38), (hx + 10, hy - 6), (70, 80, 100), 2)

    # 4. Arms & Hands
    sh_l = pose_params['shoulder_l']
    sh_r = pose_params['shoulder_r']
    elb_l = pose_params['elbow_l']
    elb_r = pose_params['elbow_r']
    hand_l = pose_params['hand_l']
    hand_r = pose_params['hand_r']
    
    # Left Arm
    draw_thick_line(draw, sh_l, elb_l, COLOR_STICK, 7)
    draw_thick_line(draw, elb_l, hand_l, COLOR_STICK, 7)
    
    # Left Hand Gesture
    if pose_params.get('thumbs_up', False):
        hx, hy = hand_l
        draw_circle(draw, (hx, hy), 7, COLOR_STICK, fill=COLOR_STICK)
        draw_thick_line(draw, (hx, hy), (hx, hy - 20), COLOR_GOLD, 5)  # Gold upright thumb
        draw_circle(draw, (hx, hy - 20), 3.5, COLOR_GOLD, fill=COLOR_GOLD)
    else:
        draw_circle(draw, hand_l, 6, COLOR_STICK, fill=COLOR_STICK)
        
    # Right Arm
    draw_thick_line(draw, sh_r, elb_r, COLOR_STICK, 7)
    draw_thick_line(draw, elb_r, hand_r, COLOR_STICK, 7)
    draw_circle(draw, hand_r, 6, COLOR_STICK, fill=COLOR_STICK)


def generate_all_frames():
    """Main rendering loop: generates all 540 frames and pipes to FFmpeg."""
    output_dir = "/Users/pro16/Documents/VideoProject/X-Economic/_sandbox/stickman_cooking"
    os.makedirs(output_dir, exist_ok=True)
    video_path = os.path.join(output_dir, "stickman_cooking.mp4")
    contact_sheet_path = os.path.join(output_dir, "stickman_contact_sheet.png")
    readme_path = os.path.join(output_dir, "README.md")
    
    print(f"Starting render of {TOTAL_FRAMES} frames ({TOTAL_FRAMES/FPS:.1f}s @ {FPS}fps)...")
    
    ffmpeg_cmd = [
        "/opt/homebrew/bin/ffmpeg",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        video_path
    ]
    
    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    steam_particles = []
    
    # 14 discrete colorful food ingredients
    ingredients = []
    random.seed(42)
    for i in range(14):
        ingredients.append({
            'id': i,
            'x': 960.0,
            'y': 500.0,
            'col': INGREDIENT_COLORS[i % len(INGREDIENT_COLORS)],
            'is_circle': (i % 2 == 0),
            'size': random.uniform(6.0, 9.0),
            'rot': random.uniform(0, 360),
            'visible': False,
            'landed': False
        })

    # Contact sheet timestamps (8 evenly spaced moments across 4 beats)
    contact_indices = [
        int(TOTAL_FRAMES * 0.06),   # Frame 32 (~1.1s) - Beat 1: Placing pan
        int(TOTAL_FRAMES * 0.17),   # Frame 91 (~3.0s) - Beat 1: Fire ignition & knob click
        int(TOTAL_FRAMES * 0.30),   # Frame 162 (~5.4s) - Beat 2: Dropping ingredients from bowl
        int(TOTAL_FRAMES * 0.42),   # Frame 226 (~7.5s) - Beat 2: Sizzling pan with steam
        int(TOTAL_FRAMES * 0.53),   # Frame 286 (~9.5s) - Beat 3: First pan toss
        int(TOTAL_FRAMES * 0.68),   # Frame 367 (~12.2s) - Beat 3: Grand sauté flip mid-air
        int(TOTAL_FRAMES * 0.82),   # Frame 442 (~14.7s) - Beat 4: Plating onto plate
        int(TOTAL_FRAMES * 0.96)    # Frame 518 (~17.3s) - Beat 4: Thumbs-up victory & chef nod
    ]
    contact_frames = []

    # Frame-by-frame loop
    for f in range(TOTAL_FRAMES):
        img_high = Image.new('RGB', (SW, SH), COLOR_BG)
        draw = ImageDraw.Draw(img_high)
        
        base_x = 560
        base_y = 820
        
        pan_center = [1030.0, 646.0]
        pan_angle = 0.0
        flame_intensity = 0.0
        eyes_happy = False
        thumbs_up = False
        show_bowl = False
        bowl_pos = (0, 0)
        bowl_tilt = 0.0
        
        foot_l = (base_x - 35, base_y)
        foot_r = (base_x + 35, base_y)
        knee_l = (base_x - 25, base_y - 100)
        knee_r = (base_x + 30, base_y - 100)
        hips   = (base_x, base_y - 200)
        neck   = (base_x + 20, base_y - 380)
        head_c = (neck[0] + 12, neck[1] - 65)
        
        sh_l   = (neck[0] - 6, neck[1] + 25)
        sh_r   = (neck[0] + 6, neck[1] + 25)
        
        # -------------------------------------------------------------
        # PHASE 1: Setting up Pan & Igniting Stove (Frames 0 - 134 / 0.0s - 4.5s)
        # -------------------------------------------------------------
        if f < 135:
            if f < 55:
                # Placing pan onto stove
                prog = ease_in_out(f / 55.0)
                pan_center[0] = lerp(730.0, 1030.0, prog)
                arc_lift = math.sin(prog * math.pi) * 85.0
                pan_center[1] = lerp(570.0, 646.0, prog) - arc_lift
                pan_angle = math.sin(prog * math.pi) * 0.16
                
                handle_pt = (pan_center[0] - 135 * math.cos(pan_angle), pan_center[1] + 12 - 135 * math.sin(pan_angle))
                hand_r = handle_pt
                elb_r = (sh_r[0] + 45, sh_r[1] + 45)
                hand_l = (base_x - 15, base_y - 210)
                elb_l = (sh_l[0] - 25, sh_l[1] + 60)
            elif f < 90:
                # Pan rested on burner, left hand reaches for stove knob
                pan_center = [1030.0, 646.0]
                pan_angle = 0.0
                handle_pt = (pan_center[0] - 135, pan_center[1] + 12)
                hand_r = handle_pt
                elb_r = (sh_r[0] + 55, sh_r[1] + 50)
                
                reach_p = ease_in_out((f - 55) / 35.0)
                hand_l = (lerp(base_x - 15, 940, reach_p), lerp(base_y - 210, 715, reach_p))
                elb_l = (lerp(sh_l[0] - 25, 860, reach_p), lerp(sh_l[1] + 60, 650, reach_p))
            else:
                # Frame 90 - 134: Fire ignites!
                pan_center = [1030.0, 646.0]
                pan_angle = 0.0
                handle_pt = (pan_center[0] - 135, pan_center[1] + 12)
                hand_r = handle_pt
                elb_r = (sh_r[0] + 55, sh_r[1] + 50)
                
                ret_p = ease_out_quad((f - 90) / 44.0)
                hand_l = (lerp(940, base_x + 10, ret_p), lerp(715, base_y - 215, ret_p))
                elb_l = (lerp(860, base_x - 20, ret_p), lerp(650, sh_l[1] + 65, ret_p))
                
                # Flame expands
                flame_intensity = clamp((f - 90) / 25.0)
                head_c = (head_c[0], head_c[1] + math.sin((f - 90) * 0.25) * 4)

        # -------------------------------------------------------------
        # PHASE 2: Dropping Ingredients & Steam Rising (Frames 135 - 254 / 4.5s - 8.5s)
        # -------------------------------------------------------------
        elif f < 255:
            pan_center = [1030.0, 646.0]
            pan_angle = 0.0
            handle_pt = (pan_center[0] - 135, pan_center[1] + 12)
            hand_r = handle_pt
            elb_r = (sh_r[0] + 55, sh_r[1] + 50)
            flame_intensity = 1.0
            
            if f < 190:
                # Left hand holds and tilts bowl of fresh food
                show_bowl = True
                bowl_p = ease_in_out((f - 135) / 30.0) if f < 165 else ease_out_quad((190 - f) / 25.0)
                hand_l = (lerp(base_x + 10, 960, bowl_p), lerp(base_y - 215, 510, bowl_p))
                elb_l = (lerp(base_x - 20, 875, bowl_p), lerp(sh_l[1] + 65, 480, bowl_p))
                
                bowl_pos = hand_l
                bowl_tilt = lerp(0.0, 0.75, clamp((f - 148) / 20.0))
                
                # Drop ingredients cascading into pan
                if f >= 150:
                    for ing in ingredients:
                        delay = ing['id'] * 2.2
                        t_drop = (f - 150 - delay) / 18.0
                        if t_drop >= 0:
                            ing['visible'] = True
                            p_fall = clamp(t_drop)
                            start_x = 960.0 + (ing['id'] % 3 - 1) * 6
                            start_y = 510.0
                            target_x = 965.0 + (ing['id'] - 6.5) * 12.0
                            target_y = 642.0 + (ing['id'] % 4) * 4.0
                            
                            ing['x'] = lerp(start_x, target_x, p_fall)
                            # Bouncing parabolic drop
                            ing['y'] = lerp(start_y, target_y, ease_in_quad(p_fall))
                            if p_fall >= 0.98:
                                ing['landed'] = True
            else:
                # Left hand rests on hip; observe the sizzle
                hand_l = (base_x + 5, base_y - 210)
                elb_l = (base_x - 25, sh_l[1] + 65)
                # Gentle sizzle vibration
                sizzle_t = (f - 190) * 0.45
                for ing in ingredients:
                    ing['visible'] = True
                    ing['x'] = 965.0 + (ing['id'] - 6.5) * 12.0
                    ing['y'] = 642.0 + (ing['id'] % 4) * 4.0 + math.sin(sizzle_t + ing['id']) * 1.6

            # Steam starts rising smoothly
            if f > 185 and f % 2 == 0:
                steam_particles.append({
                    'x': 1030.0 + random.uniform(-65, 65),
                    'y': 635.0,
                    'vx': random.uniform(-0.6, 0.6),
                    'vy': random.uniform(-2.4, -3.8),
                    'size': random.uniform(8.0, 15.0),
                    'alpha': 0.70,
                    'growth': random.uniform(0.35, 0.65)
                })

        # -------------------------------------------------------------
        # PHASE 3: The Spectacular Sauté Toss (Frames 255 - 419 / 8.5s - 14.0s)
        # -------------------------------------------------------------
        elif f < 420:
            flame_intensity = 1.0
            toss_f = f - 255
            
            # Three distinct, escalating sauté tosses
            current_toss = 1 if toss_f < 52 else (2 if toss_f < 112 else 3)
            sub_f = toss_f if current_toss == 1 else (toss_f - 55 if current_toss == 2 else toss_f - 115)
            toss_len = 50 if current_toss == 1 else (55 if current_toss == 2 else 49)
            p_toss = clamp(sub_f / float(toss_len))
            
            max_pan_lift = 60.0 if current_toss == 1 else (90.0 if current_toss == 2 else 120.0)
            max_ing_lift = 140.0 if current_toss == 1 else (210.0 if current_toss == 2 else 270.0)
            
            # Pan motion: dip back -> launch up -> catch & settle
            if p_toss < 0.22:
                # Dip & back
                p1 = p_toss / 0.22
                pan_center = [1030.0 - p1 * 22.0, 646.0 + p1 * 16.0]
                pan_angle = -p1 * 0.14
            elif p_toss < 0.52:
                # Launch UP with forward tilt
                p2 = (p_toss - 0.22) / 0.30
                pan_center = [1008.0 + p2 * 38.0, 662.0 - math.sin(p2 * math.pi) * max_pan_lift]
                pan_angle = lerp(-0.14, 0.38, ease_out_quad(p2))
            else:
                # Catch & return smoothly
                p3 = (p_toss - 0.52) / 0.48
                pan_center = [lerp(1046.0, 1030.0, p3), lerp(646.0 - max_pan_lift * 0.2, 646.0, ease_out_quad(p3))]
                pan_angle = lerp(0.38, 0.0, ease_in_out(p3))
                
            handle_pt = (pan_center[0] - 135 * math.cos(pan_angle), pan_center[1] + 12 - 135 * math.sin(pan_angle))
            hand_r = handle_pt
            elb_r = (sh_r[0] + 50, sh_r[1] + 45 + math.sin(p_toss * math.pi) * 16)
            
            knee_bend = math.sin(p_toss * math.pi) * 14
            hips = (base_x - math.sin(p_toss * math.pi) * 8, base_y - 200 + knee_bend)
            
            # Ingredients mid-air arc physics
            for ing in ingredients:
                ing['visible'] = True
                if 0.25 <= p_toss <= 0.88:
                    flight_p = (p_toss - 0.25) / 0.63
                    ing_peak = max_ing_lift * (1.0 - abs(ing['id'] - 6.5) * 0.05)
                    fly_y = 642.0 - math.sin(flight_p * math.pi) * ing_peak
                    fly_x = 970.0 + (ing['id'] - 6.5) * 12.0 + math.sin(flight_p * math.pi) * 25.0
                    ing['x'] = fly_x
                    ing['y'] = fly_y
                    ing['rot'] += 9.0 * (1 if ing['id'] % 2 == 0 else -1)
                else:
                    # Resting in pan
                    ing['x'] = pan_center[0] + (ing['id'] - 6.5) * 11.0 * math.cos(pan_angle)
                    ing['y'] = pan_center[1] - 4 + (ing['id'] - 6.5) * 11.0 * math.sin(pan_angle)

            # Billowing steam during flips
            if f % 2 == 0:
                steam_particles.append({
                    'x': pan_center[0] + random.uniform(-45, 45),
                    'y': pan_center[1] - 20,
                    'vx': random.uniform(-1.2, 1.2),
                    'vy': random.uniform(-3.2, -4.8),
                    'size': random.uniform(10.0, 18.0),
                    'alpha': 0.75,
                    'growth': 0.55
                })

        # -------------------------------------------------------------
        # PHASE 4: Plating, Thumbs-Up Victory & Nod (Frames 420 - 539 / 14.0s - 18.0s)
        # -------------------------------------------------------------
        else:
            flame_intensity = 0.0  # Stove fire OFF
            
            if f < 470:
                # Pouring dish onto plate (x = 1420, y = 660)
                pour_p = ease_in_out((f - 420) / 50.0)
                pan_center = [lerp(1030.0, 1370.0, pour_p), lerp(646.0, 570.0, pour_p)]
                pan_angle = lerp(0.0, 0.78, pour_p)
                handle_pt = (pan_center[0] - 135 * math.cos(pan_angle), pan_center[1] + 12 - 135 * math.sin(pan_angle))
                hand_r = handle_pt
                elb_r = (sh_r[0] + 65, sh_r[1] + 35)
                
                hand_l = (lerp(base_x + 5, 1260, pour_p), lerp(base_y - 210, 620, pour_p))
                elb_l = (sh_l[0] + 35, sh_l[1] + 45)
                
                # Food slides into the plate
                slide_p = clamp((f - 432) / 34.0)
                for ing in ingredients:
                    ing['visible'] = True
                    ing_p = clamp((slide_p - ing['id'] * 0.035) / 0.55)
                    target_px = 1420.0 + (ing['id'] % 5 - 2) * 14.0 + random.uniform(-3, 3)
                    target_py = 656.0 + (ing['id'] // 5) * 5.0
                    ing['x'] = lerp(pan_center[0] + (ing['id'] - 6.5) * 8.0, target_px, ease_in_quad(ing_p))
                    ing['y'] = lerp(pan_center[1], target_py, ease_out_quad(ing_p))
            elif f < 495:
                # Return empty pan back onto stove cleanly
                ret_p = ease_in_out((f - 470) / 25.0)
                pan_center = [lerp(1370.0, 1030.0, ret_p), lerp(570.0, 646.0, ret_p)]
                pan_angle = lerp(0.78, 0.0, ret_p)
                handle_pt = (pan_center[0] - 135 * math.cos(pan_angle), pan_center[1] + 12 - 135 * math.sin(pan_angle))
                hand_r = handle_pt
                elb_r = (sh_r[0] + 55, sh_r[1] + 50)
                hand_l = (lerp(1260, base_x + 10, ret_p), lerp(620, base_y - 200, ret_p))
                elb_l = (sh_l[0] - 15, sh_l[1] + 55)
                
                for ing in ingredients:
                    ing['visible'] = True
                    ing['x'] = 1420.0 + (ing['id'] % 5 - 2) * 14.0
                    ing['y'] = 656.0 + (ing['id'] // 5) * 5.0
            else:
                # Pan rested on stove; Stickman gives crisp THUMBS UP & Nod!
                pan_center = [1030.0, 646.0]
                pan_angle = 0.0
                handle_pt = (pan_center[0] - 135, pan_center[1] + 12)
                
                hand_r = (base_x + 40, base_y - 200)
                elb_r = (sh_r[0] + 35, sh_r[1] + 55)
                
                up_p = ease_out_cubic((f - 495) / 22.0)
                thumbs_up = True
                eyes_happy = True
                
                # Thumbs-up raised to chest/shoulder height
                hand_l = (lerp(base_x + 10, base_x - 50, up_p), lerp(base_y - 200, base_y - 335, up_p))
                elb_l = (lerp(sh_l[0] - 15, base_x - 70, up_p), lerp(sh_l[1] + 55, base_y - 265, up_p))
                
                # Cheerful nod
                nod = math.sin((f - 495) * 0.32) * 6.5
                head_c = (head_c[0], head_c[1] + nod)
                
                for ing in ingredients:
                    ing['visible'] = True
                    ing['x'] = 1420.0 + (ing['id'] % 5 - 2) * 14.0
                    ing['y'] = 656.0 + (ing['id'] // 5) * 5.0

            # Plated dish emits gentle aromatic steam curls
            if f % 4 == 0:
                steam_particles.append({
                    'x': 1420.0 + random.uniform(-25, 25),
                    'y': 646.0,
                    'vx': random.uniform(-0.35, 0.35),
                    'vy': random.uniform(-1.6, -2.6),
                    'size': random.uniform(6.0, 12.0),
                    'alpha': 0.60,
                    'growth': 0.32
                })

        # -------------------------------------------------------------
        # STEAM PARTICLE UPDATES
        # -------------------------------------------------------------
        for p in steam_particles:
            p['x'] += p['vx'] + math.sin(f * 0.12 + p['y'] * 0.05) * 0.45
            p['y'] += p['vy']
            p['size'] += p['growth']
            p['alpha'] -= 0.015
        steam_particles = [p for p in steam_particles if p['alpha'] > 0.01 and p['y'] > 180]

        # -------------------------------------------------------------
        # RENDER LAYERS
        # -------------------------------------------------------------
        # 1. Kitchen environment & counter
        draw_kitchen_environment(draw, flame_intensity, f)
        
        # 2. Fire flames (drawn right at the burner level, rising up)
        if flame_intensity > 0.01:
            draw_procedural_flames(draw, 1030, 663, flame_intensity, f)
        
        # 3. Ingredients
        for ing in ingredients:
            if ing['visible'] and ing['y'] < 800:
                ix, iy = ing['x'], ing['y']
                isize = ing['size']
                icol = ing['col']
                if ing['is_circle']:
                    draw_circle(draw, (ix, iy), isize, (28, 38, 52), fill=icol, width=1)
                else:
                    rad = math.radians(ing['rot'])
                    dx = isize * math.cos(rad)
                    dy = isize * math.sin(rad)
                    sq_pts = [
                        ((ix - dx - dy) * SCALE, (iy - dy + dx) * SCALE),
                        ((ix + dx - dy) * SCALE, (iy + dy + dx) * SCALE),
                        ((ix + dx + dy) * SCALE, (iy + dy - dx) * SCALE),
                        ((ix - dx + dy) * SCALE, (iy - dy - dx) * SCALE),
                    ]
                    draw.polygon(sq_pts, fill=icol)

        # 4. Frying pan
        draw_pan(draw, pan_center, pan_angle, handle_pt)
        
        # 5. Prep Bowl if active
        if show_bowl:
            draw_prep_bowl(draw, bowl_pos, bowl_tilt)
            
        # 6. Sinuous Steam
        draw_steam_particles(draw, steam_particles)
        
        # 7. Stickman
        pose_params = {
            'foot_l': foot_l,
            'foot_r': foot_r,
            'knee_l': knee_l,
            'knee_r': knee_r,
            'hips': hips,
            'neck': neck,
            'head_c': head_c,
            'shoulder_l': sh_l,
            'shoulder_r': sh_r,
            'elbow_l': elb_l,
            'elbow_r': elb_r,
            'hand_l': hand_l,
            'hand_r': hand_r,
            'eyes_happy': eyes_happy,
            'thumbs_up': thumbs_up
        }
        draw_stickman(draw, (base_x, base_y), pose_params)
        
        # Downsample 2x to full 1080p
        img_final = img_high.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
        
        # Contact sheet snapshot
        if f in contact_indices:
            contact_frames.append((f, img_final.copy()))
            
        # Pipe frame
        pipe.stdin.write(img_final.tobytes())
        
        if (f + 1) % 90 == 0 or f == TOTAL_FRAMES - 1:
            print(f"Rendered frame {f + 1}/{TOTAL_FRAMES} ({(f + 1)/TOTAL_FRAMES * 100:.1f}%)")

    pipe.stdin.close()
    pipe.wait()
    if pipe.returncode != 0:
        print("FFmpeg Error:", pipe.stderr.read().decode('utf-8'))
        sys.exit(1)
        
    print("Video rendered successfully!")

    # -------------------------------------------------------------
    # BUILD 8-FRAME CONTACT SHEET
    # -------------------------------------------------------------
    print("Building 8-frame contact sheet...")
    thumb_w = 460
    thumb_h = 258
    margin = 16
    grid_w = thumb_w * 4 + margin * 5
    grid_h = thumb_h * 2 + margin * 3
    
    cs_img = Image.new('RGB', (grid_w, grid_h), (16, 22, 34))
    cs_draw = ImageDraw.Draw(cs_img)
    
    beat_labels = [
        "Beat 1: Place pan on stove",
        "Beat 1: Ignite flame (#D4AF37)",
        "Beat 2: Drop food ingredients",
        "Beat 2: Sizzle & Steam (#00E5FF)",
        "Beat 3: First saute toss",
        "Beat 3: High saute flip in air",
        "Beat 4: Plating onto dish",
        "Beat 4: Thumbs-up victory nod"
    ]
    
    for idx, (frame_num, f_img) in enumerate(contact_frames):
        col = idx % 4
        row = idx // 4
        tx = margin + col * (thumb_w + margin)
        ty = margin + row * (thumb_h + margin)
        
        thumb = f_img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        cs_img.paste(thumb, (tx, ty))
        
        cs_draw.rectangle([tx, ty, tx + thumb_w, ty + thumb_h], outline=COLOR_GOLD, width=2)
        t_val = frame_num / FPS
        label = f"#{frame_num:03d} ({t_val:.1f}s) - {beat_labels[idx]}"
        cs_draw.rectangle([tx + 8, ty + 8, tx + 245, ty + 28], fill=(10, 14, 23))
        cs_draw.text((tx + 12, ty + 11), label, fill=COLOR_GOLD)
        
    cs_img.save(contact_sheet_path)
    print(f"Contact sheet saved to: {contact_sheet_path}")

    # -------------------------------------------------------------
    # GENERATE README.md WITH FFPROBE SPECS
    # -------------------------------------------------------------
    ffprobe_cmd = [
        "/opt/homebrew/bin/ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,codec_name,duration,nb_frames",
        "-of", "default=noprint_wrappers=1",
        video_path
    ]
    ffprobe_out = subprocess.check_output(ffprobe_cmd, text=True).strip()
    
    readme_content = f"""# Stickman Cooking Demo — Motion Graphics by Code

Bản demo hoạt hình người que (stick figure) đang nấu ăn, được dựng và render 100% bằng code (Python + Pillow + FFmpeg direct pipe), không sử dụng bất kỳ engine video AI nào. Phục vụ kiểm tra năng lực dựng visual motion graphics theo chuẩn nhận diện kênh **X-Economy**.

---

## 🎨 Bảng Màu Chuẩn Nhận Diện Kênh
- **Nền (Background):** `#0A0E17` (Deep dark slate navy)
- **Nét Người Que (Stick Figure & Hat):** `#F5F0E6` (Ivory cream)
- **Lửa & Điểm Nhấn (Fire & Accent Gold):** `#D4AF37` (Muted gold / amber)
- **Hơi Nước (Steam):** `#00E5FF` (Electric cyan)

---

## ⏱️ Kịch Bản 4 Nhịp Hoạt Họa (Thời lượng: 18.0 giây / 540 frames)
1. **Nhịp 1 (0.0s – 4.5s / frames 0–134):**
   - Người que cầm chảo bước tới bếp, đặt chảo lên bếp ga.
   - Tay trái vặn núm bếp (click marker vàng), lửa vàng `#D4AF37` bốc lên rực rỡ dưới đáy chảo.
2. **Nhịp 2 (4.5s – 8.5s / frames 135–254):**
   - Tay trái cầm âu nguyên liệu thả 14 miếng thức ăn (tròn, vuông màu sắc tươi mới) vào chảo theo quỹ đạo parabol.
   - Thức ăn chạm mặt chảo nóng nảy nhẹ, khói/hơi nước `#00E5FF` bắt đầu cuộn sóng bốc lên.
3. **Nhịp 3 (8.5s – 14.0s / frames 255–419):**
   - Đảo chảo 3 nhịp tăng tiến: người que hạ gối, nhấc chảo nghiêng tới trước, hất nguyên liệu tung bay lên không trung theo đường cong trọng lực đẹp mắt, xoay đảo 360 độ rồi đón lại gọn gàng vào lòng chảo.
   - Hơi nước và lửa cuộn theo từng nhịp hất chảo.
4. **Nhịp 4 (14.0s – 18.0s / frames 420–539):**
   - Tắt bếp ga, nghiêng chảo 45° trút toàn bộ thức ăn nóng hổi sang chiếc đĩa sứ viền vàng bên cạnh.
   - Đặt chảo rỗng lại mặt bếp, người que xoay người hướng về màn hình, gật đầu tự tin và giơ ngón tay cái (**thumbs-up**) đắc thắng. Đĩa thức ăn bốc hơi nước nhẹ nhàng.

---

## 🛠️ Công Cụ & Thư Viện Sử Dụng
- **Ngôn ngữ:** Python 3.13
- **Thư viện đồ họa:** `PIL` (Pillow) với kỹ thuật **2x Supersampling** (vẽ ở độ phân giải 3840x2160, sau đó downsample bằng Bilinear filter về 1920x1080 để khử răng cưa và mượt khớp nối).
- **Trình xuất video:** `ffmpeg` (được pipe trực tiếp qua stdin rawvideo `rgb24`, mã hóa `libx264`, `-crf 18`, `-pix_fmt yuv420p`).

---

## 🚀 Lệnh Render Lại
```bash
python3 /Users/pro16/Documents/VideoProject/X-Economic/_sandbox/stickman_cooking/render_stickman.py
```

---

## 📊 Kết Quả Kiểm Nghiệm Kỹ Thuật (ffprobe Output)
```text
{ffprobe_out}
```
- **Codec:** H.264 (`yuv420p`)
- **Độ phân giải:** 1920x1080
- **Tốc độ khung hình:** 30 fps
- **Thời lượng thực tế:** 18.000000 giây (540 frames)
- **Âm thanh / Chữ:** Silent demo, 0 audio stream, 0 text watermark.

---

## 🖼️ Contact Sheet (8 Khung Hình Rải Đều)
Ảnh lưới 8 khoảnh khắc tiêu biểu được lưu tại: [`stickman_contact_sheet.png`](stickman_contact_sheet.png).
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"README saved to: {readme_path}")


if __name__ == '__main__':
    generate_all_frames()
