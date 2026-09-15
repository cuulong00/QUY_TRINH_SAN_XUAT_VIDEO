#!/usr/bin/env python3
import os
import shutil
import re
from pathlib import Path

downloads_dir = Path('/Users/pro16/Downloads/kemtrangtien')
episode_dir = Path(__file__).parent.resolve()
video_dir = episode_dir / 'video'

chapter_names = {
    '01': 'Chương 01',
    '02': 'Chương 02',
    '03': 'Chương 03',
    '04': 'Chương 04',
    '05': 'Chương 05',
    '06': 'Chương 06',
}

scene_pattern = re.compile(r'CH(\d{2})_SC\d{3}')
moved_count = 0

if downloads_dir.exists():
    for f in downloads_dir.iterdir():
        if f.is_file() and f.suffix == '.mp4':
            m = scene_pattern.search(f.name)
            if m:
                ch_num = m.group(1)
                if ch_num in chapter_names:
                    target_folder = video_dir / chapter_names[ch_num]
                    target_file = target_folder / f.name
                    shutil.move(str(f), str(target_file))
                    print(f"Moved: {f.name} -> {chapter_names[ch_num]}")
                    moved_count += 1

print(f"Total moved: {moved_count} files.")
