import os
import json
import glob
import subprocess
import argparse
from pathlib import Path


def create_concat_slideshow(episode_slug, fps=30, image_dir=None):
    base_dir = Path(f"episodes/{episode_slug}")
    scene_map_path = base_dir / "scene_map.json"
    
    if image_dir:
        image_dir = Path(image_dir)
    else:
        image_dir = base_dir / "images_final"
        
    video_dir = base_dir / "video"
    output_video = video_dir / "slideshow_base.mp4"
    concat_file = video_dir / "slideshow_concat.txt"

    if not scene_map_path.exists():
        print(f"Lỗi: Không tìm thấy file {scene_map_path}")
        return

    if not image_dir.exists():
        print(f"Lỗi: Không tìm thấy thư mục ảnh {image_dir}")
        return

    with open(scene_map_path, "r", encoding="utf-8") as f:
        scenes = json.load(f)

    images = sorted(glob.glob(str(image_dir / "*.[jp][pn]g"))) + sorted(glob.glob(str(image_dir / "*.webp")))

    if not images:
        print(f"Lỗi: Không có file ảnh nào trong {image_dir}")
        return

    if len(images) != len(scenes):
        print(f"Cảnh báo: Số lượng ảnh ({len(images)}) không khớp với số lượng cảnh trong json ({len(scenes)})")

    video_dir.mkdir(parents=True, exist_ok=True)

    with open(concat_file, "w", encoding="utf-8") as f:
        for i, scene in enumerate(scenes):
            if i < len(images):
                img_path = os.path.abspath(images[i])
                duration = scene.get("duration_sec", 5)
                f.write(f"file '{img_path}'\n")
                f.write(f"duration {duration}\n")

        if images:
            f.write(f"file '{os.path.abspath(images[-1])}'\n")

    ffmpeg_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-vf", f"fps={fps},scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,format=yuv420p",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        str(output_video),
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Render thành công! Output: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi render FFmpeg: {e}")


def create_kenburns_slideshow(episode_slug, duration=8, transition_duration=1, fps=30, seed=None, image_dir=None):
    from slideshow_video import SlideshowConfig, create_slideshow_video
    import json

    base_dir = Path(f"episodes/{episode_slug}")
    scene_map_path = base_dir / "scene_map.json"
    
    if image_dir:
        image_dir = Path(image_dir)
    else:
        image_dir = base_dir / "images_final"
        
    output_video = base_dir / "video" / "slideshow_base.mp4"

    if not image_dir.exists():
        print(f"Lỗi: Không tìm thấy thư mục ảnh {image_dir}")
        return

    output_video.parent.mkdir(parents=True, exist_ok=True)
    
    durations = None
    if scene_map_path.exists():
        with open(scene_map_path, "r", encoding="utf-8") as f:
            scenes = json.load(f)
            durations = [scene.get("duration_sec", duration) for scene in scenes]

    output = create_slideshow_video(
        SlideshowConfig(
            image_dir=image_dir,
            output_file=output_video,
            duration_per_image=duration,
            transition_duration=transition_duration,
            fps=fps,
            random_seed=seed,
            durations=durations,
        )
    )
    print(f"Render Ken Burns thành công! Output: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Tên thư mục episode (vd: nghich-ly-ma-sat-thoi-quen)")
    parser.add_argument("--mode", choices=["concat", "kenburns"], default="concat", help="Chế độ render")
    parser.add_argument("--image-dir", type=str, default=None, help="Đường dẫn trỏ đến thư mục ảnh")
    parser.add_argument("--duration", type=int, default=8, help="Seconds per image for kenburns mode")
    parser.add_argument("--transition-duration", type=int, default=1, help="Transition seconds for kenburns mode")
    parser.add_argument("--fps", type=int, default=30, help="Output FPS")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for kenburns mode")
    args = parser.parse_args()

    if args.mode == "concat":
        create_concat_slideshow(args.slug, fps=args.fps, image_dir=args.image_dir)
    else:
        create_kenburns_slideshow(
            args.slug,
            duration=args.duration,
            transition_duration=args.transition_duration,
            fps=args.fps,
            seed=args.seed,
            image_dir=args.image_dir,
        )
