import os
import shutil
import re

source_dir = "/Users/pro16/Downloads/chonkhomalam"
target_dir = "/Users/pro16/Documents/VideoProject/HieuBietHon/episodes/nghich-ly-gia-xang-viet-nam/images_final"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

files = [f for f in os.listdir(source_dir) if f.endswith(".png") or f.endswith(".jpg")]

for f in files:
    # Match the starting number
    match = re.match(r"^(\d+)_", f)
    if match:
        num = int(match.group(1))
        # pad to 3 digits
        new_name = f"{num:03d}_{f}"
        source_path = os.path.join(source_dir, f)
        target_path = os.path.join(target_dir, new_name)
        shutil.copy2(source_path, target_path)
    else:
        # If no number at start, just copy as is
        shutil.copy2(os.path.join(source_dir, f), os.path.join(target_dir, f))

print(f"Copied and padded {len(files)} files into {target_dir}")
