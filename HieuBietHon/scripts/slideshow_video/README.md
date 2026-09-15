# Slideshow Video

Tính năng tạo video slideshow từ thư mục ảnh bằng FFmpeg, đóng gói riêng để tái sử dụng ở project khác hoặc cho model/code khác gọi lại.

## Cấu trúc

- `slideshow_video/generator.py` — API Python chính
- `slideshow_video/__main__.py` — CLI: chạy bằng `python -m slideshow_video`
- `slideshow_video/__init__.py` — export API tiện dụng

## Yêu cầu

- Python 3.11+
- `ffmpeg` và `ffprobe` có trong `PATH`

## Dùng từ CLI

```bash
python -m slideshow_video \
  "/path/to/images_final" \
  "/path/to/output.mp4" \
  --duration 8 \
  --transition-duration 1 \
  --fps 30
```

### Tùy chọn

- `--duration`: số giây cho mỗi ảnh
- `--transition-duration`: thời lượng chuyển cảnh
- `--fps`: frame rate video đầu ra
- `--seed`: random seed để cố định hiệu ứng random

Ví dụ deterministic:

```bash
python -m slideshow_video \
  "/path/to/images_final" \
  "/path/to/output.mp4" \
  --duration 8 \
  --seed 42
```

## Dùng từ Python

```python
from pathlib import Path
from slideshow_video import SlideshowConfig, create_slideshow_video

output = create_slideshow_video(
    SlideshowConfig(
        image_dir=Path("/path/to/images_final"),
        output_file=Path("/path/to/output.mp4"),
        duration_per_image=8,
        transition_duration=1,
        fps=30,
        random_seed=None,
    )
)

print(output)
```

## Hành vi

- Tự quét ảnh theo thứ tự tên file
- Tự lấy resolution từ ảnh đầu tiên bằng `ffprobe`
- Mỗi ảnh được gán hiệu ứng chuyển động ngẫu nhiên kiểu Ken Burns
- Mỗi điểm chuyển ảnh dùng `xfade` với transition ngẫu nhiên
- Xuất ra `mp4` bằng `libx264`

## Cách dùng cho model/code khác

Nếu bạn là model khác và cần tái sử dụng tính năng này, hãy ưu tiên gọi API sau:

```python
from slideshow_video import SlideshowConfig, create_slideshow_video
```

Chỉ cần truyền:
- thư mục ảnh
- đường dẫn video output
- số giây mỗi ảnh
- thời lượng transition
- fps
- seed nếu muốn reproducible

## Lưu ý

- Nếu thư mục không có ảnh hợp lệ (`.png`, `.jpg`, `.jpeg`, `.webp`) hàm sẽ báo lỗi
- Nếu máy chưa cài `ffmpeg` / `ffprobe`, lệnh sẽ fail
- Các cảnh báo kiểu `deprecated pixel format used` từ ffmpeg thường không chặn render thành công
