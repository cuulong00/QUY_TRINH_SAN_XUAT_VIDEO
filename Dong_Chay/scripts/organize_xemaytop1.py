import os
import shutil
import json
import re

root_dir = '/Users/pro16/Downloads/xemaytop1'
files = [f for f in os.listdir(root_dir) if f.endswith('.mp4') and os.path.isfile(os.path.join(root_dir, f))]

moved_counts = {}

for f in files:
    m = re.match(r'^(CH\d+)_', f, re.IGNORECASE)
    if m:
        ch_num = int(m.group(1).upper().replace('CH', ''))
        ch_dir_name = f'chapter_{ch_num:02d}'
        target_dir = os.path.join(root_dir, ch_dir_name)
        os.makedirs(target_dir, exist_ok=True)
        
        src = os.path.join(root_dir, f)
        dst = os.path.join(target_dir, f)
        shutil.move(src, dst)
        moved_counts[ch_dir_name] = moved_counts.get(ch_dir_name, 0) + 1

print('Move completed:')
for ch, count in sorted(moved_counts.items()):
    print(f'  Moved {count} files -> {ch}/')

# Build Catalog & Manifest
catalog = {}
for ch in sorted(os.listdir(root_dir)):
    ch_path = os.path.join(root_dir, ch)
    if not os.path.isdir(ch_path):
        continue
    
    ch_files = sorted([f for f in os.listdir(ch_path) if f.endswith('.mp4')])
    scene_groups = {}
    for f in ch_files:
        m = re.match(r'^(CH\d+_SC[0-9a-zA-Z_]+?)_', f)
        sc_id = m.group(1) if m else f.replace('.mp4', '')
        size_mb = round(os.path.getsize(os.path.join(ch_path, f)) / (1024*1024), 2)
        scene_groups.setdefault(sc_id, []).append({'filename': f, 'size_mb': size_mb})
        
    catalog[ch] = {
        'total_files': len(ch_files),
        'unique_scenes': len(scene_groups),
        'scenes': scene_groups
    }

# Write JSON manifest
with open(os.path.join(root_dir, 'video_manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

# Write Markdown Catalog
total_all = sum(c['total_files'] for c in catalog.values())
md_lines = [
    '# 🎬 Danh Mục Video Clips (Khi Nào Xe Máy VinFast Lên Top 1)',
    '',
    'Thư mục: `/Users/pro16/Downloads/xemaytop1`',
    f'Tổng số video: {total_all} clips',
    '',
    '## 📊 Bảng Thống Kê Theo Chương',
    '',
    '| Thư Mục | Số Lượng Clips | Số Scene Duy Nhất | Ghi Chú / Duplicate Takes |',
    '| :--- | :---: | :---: | :--- |'
]

for ch, data in catalog.items():
    dups = [sc for sc, flist in data['scenes'].items() if len(flist) > 1]
    dup_note = f'⚠️ {len(dups)} scene có nhiều take: ' + ', '.join(dups) if dups else '✅ 100% Khớp'
    md_lines.append(f'| `{ch}/` | **{data["total_files"]}** | {data["unique_scenes"]} | {dup_note} |')

md_lines.extend([
    '',
    '---',
    '',
    '## 🔍 Chi Tiết Các Scene Có Nhiều Take Để Chọn Lọc',
    ''
])

has_dups = False
for ch, data in catalog.items():
    for sc, flist in data['scenes'].items():
        if len(flist) > 1:
            has_dups = True
            md_lines.append(f'### `{ch}` - Scene `{sc}`:')
            for item in flist:
                md_lines.append(f'- File: `{item["filename"]}` ({item["size_mb"]} MB)')
            md_lines.append('')

if not has_dups:
    md_lines.append('*Không có phân cảnh nào bị trùng take. Tất cả phân cảnh đều là 1-1.*')

with open(os.path.join(root_dir, 'README_CATALOG.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines) + '\n')

print('Catalog & Manifest created successfully!')
