import os
import json
import re

root_dir = '/Users/pro16/Downloads/thapdoisvd'
catalog = {}

for ch in sorted(os.listdir(root_dir)):
    ch_path = os.path.join(root_dir, ch)
    if not os.path.isdir(ch_path) or ch == 'assets':
        continue
    
    files = sorted([f for f in os.listdir(ch_path) if f.endswith('.mp4')])
    scene_groups = {}
    for f in files:
        m = re.match(r'^(CH\d+_SC[0-9a-zA-Z_]+?)_', f)
        sc_id = m.group(1) if m else f.replace('.mp4', '')
        size_mb = round(os.path.getsize(os.path.join(ch_path, f)) / (1024*1024), 2)
        scene_groups.setdefault(sc_id, []).append({'filename': f, 'size_mb': size_mb})
        
    catalog[ch] = {
        'total_files': len(files),
        'unique_scenes': len(scene_groups),
        'scenes': scene_groups
    }

# Write JSON manifest
with open(os.path.join(root_dir, 'video_manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

# Write Markdown Catalog
total_all = sum(c['total_files'] for c in catalog.values())
md_lines = [
    '# 🎬 Danh Mục Video Clips (Tháp Đôi Sân Vận Động)',
    '',
    'Thư mục: `/Users/pro16/Downloads/thapdoisvd`',
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

for ch, data in catalog.items():
    for sc, flist in data['scenes'].items():
        if len(flist) > 1:
            md_lines.append(f'### `{ch}` - Scene `{sc}`:')
            for item in flist:
                md_lines.append(f'- File: `{item["filename"]}` ({item["size_mb"]} MB)')
            md_lines.append('')

with open(os.path.join(root_dir, 'README_CATALOG.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines) + '\n')

print('Generated video_manifest.json and README_CATALOG.md successfully!')
