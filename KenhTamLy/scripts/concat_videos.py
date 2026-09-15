#!/usr/bin/env python3
"""
KenhTamLy Video Concatenator
=============================
Stitches a folder of video clips (from Runway/Veo 3.1) into a single base video
using FFmpeg. Decodes, rescales to 1080p, and forces 30fps for robustness.

Usage:
    python3 scripts/concat_videos.py <input_dir> <output_file> [--fps 30]
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm"}

def natural_keys(path: Path):
    """Key for sorting strings with embedded numbers naturally."""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', path.name)]

def list_videos(input_dir: Path) -> list[Path]:
    """Finds and naturally sorts all video files in the target directory."""
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")
        
    videos = sorted(
        (path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS),
        key=natural_keys
    )
    if not videos:
        raise ValueError(f"No video files found in {input_dir}")
    return videos

def concatenate_videos(videos: list[Path], output_file: Path, fps: int = 30):
    """
    Stitches a list of video files together using FFmpeg's concat filter.
    Ensures all clips are scaled to 1920x1080 and run at a uniform FPS.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    inputs = []
    filter_complex = []
    
    # 1. Build input list and prepare formatting filter for each video clip
    for idx, video_path in enumerate(videos):
        inputs.extend(["-i", str(video_path)])
        # Scale with padding to maintain 16:9 aspect ratio, set uniform FPS, format to yuv420p
        video_filter = (
            f"[{idx}:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            f"fps={fps},format=yuv420p[v{idx}]"
        )
        filter_complex.append(video_filter)
        
    # 2. Concat all formatted video streams (a=0 meaning no audio concatenation)
    concat_inputs = "".join(f"[v{i}]" for i in range(len(videos)))
    concat_filter = f"{concat_inputs}concat=n={len(videos)}:v=1:a=0[outv]"
    filter_complex.append(concat_filter)
    
    cmd = [
        "ffmpeg",
        "-y",
        *inputs,
        "-filter_complex",
        ";".join(filter_complex),
        "-map",
        "[outv]",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-r",
        str(fps),
        "-loglevel",
        "warning",
        str(output_file)
    ]
    
    print(f"🎬 Concatenating {len(videos)} clips into {output_file}...")
    print(f"Running FFmpeg...")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ FFmpeg concatenation failed!")
        print(result.stderr)
        sys.exit(result.returncode)
        
    print(f"✅ Video stitching completed successfully: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Concatenate video clips using FFmpeg.")
    parser.add_argument("input_dir", help="Directory containing input video clips.")
    parser.add_argument("output_file", help="Path to output stitched video file.")
    parser.add_argument("--fps", type=int, default=30, help="Output video frame rate (default: 30).")
    
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    output_file = Path(args.output_file)
    
    try:
        videos = list_videos(input_dir)
        concatenate_videos(videos, output_file, args.fps)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
