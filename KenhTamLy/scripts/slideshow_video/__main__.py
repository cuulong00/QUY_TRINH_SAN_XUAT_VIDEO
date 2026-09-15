from __future__ import annotations

import argparse
from pathlib import Path

from .generator import SlideshowConfig, create_slideshow_video


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an FFmpeg slideshow video from an image folder.")
    parser.add_argument("image_dir", help="Folder containing input images")
    parser.add_argument("output_file", help="Output MP4 path")
    parser.add_argument("--duration", type=int, default=8, help="Seconds per image (default: 8)")
    parser.add_argument("--transition-duration", type=int, default=1, help="Seconds per transition (default: 1)")
    parser.add_argument("--fps", type=int, default=30, help="Output FPS (default: 30)")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed for deterministic effects")
    args = parser.parse_args()

    output = create_slideshow_video(
        SlideshowConfig(
            image_dir=Path(args.image_dir),
            output_file=Path(args.output_file),
            duration_per_image=args.duration,
            transition_duration=args.transition_duration,
            fps=args.fps,
            random_seed=args.seed,
        )
    )
    print(output)


if __name__ == "__main__":
    main()
