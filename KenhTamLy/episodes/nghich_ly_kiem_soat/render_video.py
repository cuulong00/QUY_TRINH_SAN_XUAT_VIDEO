#!/usr/bin/env python3
"""
render_video.py — Render final video for 'Nghich ly kiem soat'
Approach: scale+crop Ken Burns (no zoompan → much faster + reliable)
Author: Antigravity (rebuilt fresh)
"""

import json, os, subprocess, sys

FFMPEG  = "/opt/homebrew/bin/ffmpeg"
PROJECT = "/Users/pro16/Documents/VideoProject/KenhTamLy/episodes/nghich_ly_kiem_soat"
MAP     = os.path.join(PROJECT, "scene_timing_map.json")
IMGS    = os.path.join(PROJECT, "images_final")
AUDIO   = os.path.join(PROJECT, "audio/full_voiceover.mp3")
TMPDIR  = os.path.join(PROJECT, "temp_renders")
OUTPUT  = os.path.join(PROJECT, "final_video.mp4")

FPS    = 30
OUT_W  = 1920
OUT_H  = 1080
KB_W   = 2688   # 1.4× so pan/zoom doesn't go out of bounds
KB_H   = 1512

# ── Ken Burns helper ─────────────────────────────────────────────────────────
def ken_burns_filter(mode: int, duration: int) -> str:
    """
    Use scale+crop with time variable `t`.
    Modes rotate through: zoom-in, zoom-out, pan-right, pan-left
    """
    t = max(duration, 1)

    if mode == 0:   # slow drift: top-left → center (zoom-in feel)
        cx = f"({KB_W}-{OUT_W})*min(t/{t},1)*0.5"
        cy = f"({KB_H}-{OUT_H})*min(t/{t},1)*0.5"
    elif mode == 1: # slow drift: center → bottom-right (zoom-out feel)
        cx = f"({KB_W}-{OUT_W})*(0.5+0.5*min(t/{t},1))"
        cy = f"({KB_H}-{OUT_H})*(0.5+0.5*min(t/{t},1))"
    elif mode == 2: # pan left → right
        cx = f"({KB_W}-{OUT_W})*min(t/{t},1)"
        cy = f"({KB_H}-{OUT_H})*0.4"
    else:           # pan right → left
        cx = f"({KB_W}-{OUT_W})*(1-min(t/{t},1))"
        cy = f"({KB_H}-{OUT_H})*0.6"

    return (
        f"scale={KB_W}:{KB_H}:force_original_aspect_ratio=increase,"
        f"crop={OUT_W}:{OUT_H}:{cx}:{cy},"
        f"fps={FPS},format=yuv420p"
    )

def simple_scale_filter() -> str:
    """Fallback: scale + letterbox/pillarbox."""
    pad_color = "0x1a1a1a"  # dark bg matching channel aesthetic
    return (
        f"scale={OUT_W}:{OUT_H}:force_original_aspect_ratio=decrease,"
        f"pad={OUT_W}:{OUT_H}:(ow-iw)/2:(oh-ih)/2:color={pad_color},"
        f"fps={FPS},format=yuv420p"
    )

# ── Render one scene clip ────────────────────────────────────────────────────
def render_scene(sid: str, img: str, dur: int, out: str) -> bool:
    mode = int(sid[2:]) % 4
    vf   = ken_burns_filter(mode, dur)

    cmd = [
        FFMPEG, "-y",
        "-loop", "1", "-t", str(dur),
        "-i", img,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast",
        "-pix_fmt", "yuv420p", "-crf", "20",
        out
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        print(f"  ✓ {sid}  ({dur}s)")
        return True

    # Fallback to simple scale
    print(f"  ⚠ {sid} Ken Burns failed — using simple scale")
    vf2 = simple_scale_filter()
    cmd2 = [
        FFMPEG, "-y",
        "-loop", "1", "-t", str(dur),
        "-i", img,
        "-vf", vf2,
        "-c:v", "libx264", "-preset", "fast",
        "-pix_fmt", "yuv420p", "-crf", "20",
        out
    ]
    r2 = subprocess.run(cmd2, capture_output=True, text=True)
    if r2.returncode == 0:
        print(f"  ✓ {sid}  ({dur}s) [simple scale]")
        return True

    print(f"  ✗ {sid} FAILED completely — skipping\n{r2.stderr[-300:]}")
    return False


# ── Assemble segments ────────────────────────────────────────────────────────
def assemble(rendered: list, assembled: str) -> bool:
    concat_txt = os.path.join(TMPDIR, "concat.txt")
    with open(concat_txt, "w") as f:
        for p in rendered:
            f.write(f"file '{p}'\n")
    r = subprocess.run(
        [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
         "-c", "copy", assembled],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print("Assembly error:", r.stderr[-500:])
    return r.returncode == 0


# ── Mux audio ───────────────────────────────────────────────────────────────
def mux(assembled: str, audio: str, output: str) -> bool:
    r = subprocess.run(
        [FFMPEG, "-y",
         "-i", assembled, "-i", audio,
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
         "-shortest", output],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print("Mux error:", r.stderr[-500:])
    return r.returncode == 0


# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(TMPDIR, exist_ok=True)

    with open(MAP) as f:
        scenes = json.load(f)

    print(f"\n🎬 Rendering {len(scenes)} scenes …\n")
    rendered = []

    for scene in scenes:
        sid = scene["id"]
        dur = scene["duration_sec"]
        img = os.path.join(IMGS, f"{sid}.png")
        out = os.path.join(TMPDIR, f"{sid}.mp4")

        if not os.path.exists(img):
            print(f"  ⚠ Missing: {sid}.png — skipping")
            continue

        if os.path.exists(out):
            print(f"  ↩ {sid} cached")
            rendered.append(out)
            continue

        ok = render_scene(sid, img, dur, out)
        if ok:
            rendered.append(out)

    if not rendered:
        print("No scenes rendered. Aborting.")
        sys.exit(1)

    print(f"\n🔗 Assembling {len(rendered)} segments …")
    assembled = os.path.join(TMPDIR, "assembled.mp4")
    if not assemble(rendered, assembled):
        print("Assembly failed. Aborting.")
        sys.exit(1)

    print("🎵 Muxing audio …")
    if mux(assembled, AUDIO, OUTPUT):
        size_mb = os.path.getsize(OUTPUT) / 1024 / 1024
        print(f"\n✅ Done!  →  {OUTPUT}  ({size_mb:.0f} MB)")
    else:
        print("Mux failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
