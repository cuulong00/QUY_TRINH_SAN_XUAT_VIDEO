#!/usr/bin/env python3
"""
Tạo file kịch bản biên dịch declarative spec_base.json cho Timeline Video + Audio + Transitions.
Tuân thủ chuẩn capcut-cli compile:
- Video track: 69 clips từ Chương 01 sạch không âm thanh, gán ref v_000 đến v_068.
- Audio track: Giọng đọc master chapter_01.wav, duration = 331.14s, volume = 1.0.
- Operations: 68 chuyển cảnh Mix (0.8s) hòa tan chéo giữa các clip.
"""

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "scripts"))

from sync_timing_engine import SyncTimingEngine

def main():
    source_dir = PROJECT_ROOT / "source" / "kem-trang-tien"
    engine = SyncTimingEngine(str(source_dir))
    timeline = engine.compute_chapter_timeline("01")

    video_items = []
    for i, item in enumerate(timeline["video_items"]):
        video_items.append({
            "ref": f"v_{i:03d}",
            "path": str(Path(item["path"]).resolve()),
            "start": item["start"],
            "duration": item["duration"],
            "sourceStart": item.get("sourceStart", 0.0),
            "speed": item.get("speed", 1.0),
            "volume": 0.0
        })

    audio_items = [
        {
            "path": str(Path(timeline["audio_path"]).resolve()),
            "start": 0.0,
            "duration": timeline["total_duration"],
            "volume": 1.0
        }
    ]

    # Gán 68 chuyển cảnh Mix (0.8s) giữa tất cả các clip liền kề
    operations = []
    for i in range(len(video_items) - 1):
        operations.append({
            "op": "transition",
            "target": f"v_{i:03d}",
            "slug": "mix",
            "duration": 0.8
        })

    spec = {
        "name": "KemTrangTien_Ch01",
        "width": 1920,
        "height": 1080,
        "fps": 30,
        "ratio": "16:9",
        "tracks": [
            {
                "type": "video",
                "name": "Main_Video",
                "items": video_items
            },
            {
                "type": "audio",
                "name": "Voiceover",
                "items": audio_items
            }
        ],
        "operations": operations
    }

    out_file = PROJECT_ROOT / "output_drafts" / "spec_base.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

    print(f"[✓] Đã tạo spec_base.json thành công tại: {out_file}")
    print(f"    - Clips video: {len(video_items)}")
    print(f"    - Voiceover audio: {timeline['total_duration']:.2f}s")
    print(f"    - Chuyển cảnh Mix: {len(operations)}")

if __name__ == "__main__":
    main()
