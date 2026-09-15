from __future__ import annotations

import random
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
TRANSITIONS = [
    "fade", "wipeleft", "wiperight", "wipeup", "wipedown", "slideleft", "slideright",
    "slideup", "slidedown", "smoothleft", "smoothright", "smoothup", "smoothdown",
    "circleopen", "circleclose", "vertopen", "vertclose", "horzopen", "horzclose",
    "dissolve", "pixelize", "diagbl", "diagbr", "diagtl", "diagtr", "hlslice",
    "hrslice", "vuslice", "vdslice",
]


@dataclass
class SlideshowConfig:
    image_dir: Path
    output_file: Path
    duration_per_image: int = 8
    transition_duration: int = 1
    fps: int = 30
    durations: list[int] | None = None
    random_seed: int | None = None
    no_zoom: bool = False


import re
def _list_images(image_dir: Path) -> list[Path]:
    def natural_keys(path: Path):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', path.name)]
        
    images = sorted(
        (path for path in image_dir.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS),
        key=natural_keys
    )
    if not images:
        raise ValueError(f"No images found in {image_dir}")
    return images


def _probe_resolution(image_path: Path) -> tuple[int, int]:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height",
        "-of",
        "csv=s=x:p=0",
        str(image_path),
    ]
    output = subprocess.check_output(cmd).decode("utf-8").strip()
    width_str, height_str = output.split("x")
    width = int(width_str)
    height = int(height_str)
    if width % 2 != 0:
        width -= 1
    if height % 2 != 0:
        height -= 1
    return width, height


def _build_effects(width: int, height: int, frames: int, fps: int) -> list[str]:
    return [
        f"zoompan=z='min(zoom+0.0015,1.15)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={width}x{height}:fps={fps}",
        f"zoompan=z='if(eq(on,1),1.15,zoom-0.0015)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={width}x{height}:fps={fps}",
        f"zoompan=z=1.15:x='if(eq(on,1),0,x+1)':y='ih/2-(ih/zoom/2)':d={frames}:s={width}x{height}:fps={fps}",
        f"zoompan=z=1.15:x='if(eq(on,1),iw,x-1)':y='ih/2-(ih/zoom/2)':d={frames}:s={width}x{height}:fps={fps}",
    ]


def _build_ffmpeg_command(images: Iterable[Path], config: SlideshowConfig) -> list[str]:
    image_list = list(images)
    width, height = _probe_resolution(image_list[0])
    rng = random.Random(config.random_seed)
    
    durations = config.durations if config.durations else [config.duration_per_image] * len(image_list)
    if len(durations) != len(image_list):
        raise ValueError(f"Number of durations ({len(durations)}) does not match images ({len(image_list)})")

    inputs: list[str] = []
    filter_parts: list[str] = []

    for index, image_path in enumerate(image_list):
        inputs.extend(["-i", str(image_path)])
        scale_crop = (
            f"scale={width}:{height}:force_original_aspect_ratio=increase,"
            f"crop={width}:{height}"
        )
        if config.no_zoom:
            filter_parts.append(
                f"[{index}:v]{scale_crop},format=yuv420p,setsar=1[v{index}]"
            )
        else:
            frames = int(durations[index] * config.fps)
            chosen_effect = rng.choice(_build_effects(width, height, frames, config.fps))
            filter_parts.append(
                f"[{index}:v]{scale_crop},{chosen_effect},format=yuv420p,setsar=1[v{index}]"
            )

    if len(image_list) > 1:
        prev_node = "v0"
        current_offset = 0.0
        for index in range(1, len(image_list)):
            transition = rng.choice(TRANSITIONS)
            offset = current_offset + durations[index - 1] - config.transition_duration
            out_node = f"out{index}"
            filter_parts.append(
                f"[{prev_node}][v{index}]xfade=transition={transition}:duration={config.transition_duration}:offset={offset}[{out_node}]"
            )
            prev_node = out_node
            current_offset = offset
        final_node = f"[{prev_node}]"
    else:
        final_node = "[v0]"

    config.output_file.parent.mkdir(parents=True, exist_ok=True)
    return [
        "ffmpeg",
        "-y",
        *inputs,
        "-filter_complex",
        ";".join(filter_parts),
        "-map",
        final_node,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-r",
        str(config.fps),
        "-loglevel",
        "warning",
        str(config.output_file),
    ]


def create_slideshow_video(config: SlideshowConfig) -> Path:
    image_dir = Path(config.image_dir)
    output_file = Path(config.output_file)
    normalized = SlideshowConfig(
        image_dir=image_dir,
        output_file=output_file,
        duration_per_image=config.duration_per_image,
        transition_duration=config.transition_duration,
        fps=config.fps,
        random_seed=config.random_seed,
        durations=config.durations,
        no_zoom=config.no_zoom,
    )
    images = _list_images(normalized.image_dir)
    command = _build_ffmpeg_command(images, normalized)
    subprocess.run(command, check=True)
    return normalized.output_file
