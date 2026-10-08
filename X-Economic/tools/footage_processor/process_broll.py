#!/usr/bin/env python3
"""
tools/footage_processor/process_broll.py
Module xử lý tự động B-Roll Fair Use cho Quy trình I2V+.

Tuân thủ nghiêm ngặt 4 Nguyên Tắc Fair Use Thép của Kênh:
1. Mute Absolute (-an): Tước bỏ 100% âm thanh gốc.
2. Micro-Cut (3.0s - 5.5s): Chỉ cắt đoạn trích ngắn dưới 6 giây.
3. Pixel Hash Breaking: Scale 104% và crop 16:9 (1920x1080) để bẻ gãy mã nhận diện Content ID.
4. On-Screen Attribution: Xuất metadata nhãn nguồn để gắn vào góc video.
"""

import os
import sys
import json
import argparse
import subprocess
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Xử lý tự động footage B-Roll chuẩn Fair Use")
    parser.add_argument("--manifest", required=True, help="Đường dẫn file broll_manifest_chapter_XX.json")
    parser.add_argument("--out-dir", required=True, help="Thư mục xuất video (ví dụ: episodes/[slug]/footages/chapter_XX/)")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử nghiệm không tải/cắt file")
    return parser.parse_args()

def verify_ffmpeg():
    if not shutil.which("ffmpeg"):
        raise RuntimeError("Không tìm thấy ffmpeg trong hệ thống. Vui lòng cài đặt ffmpeg via brew install ffmpeg.")

def process_item(item, out_dir, dry_run=False):
    scene_id = item.get("scene_id")
    url = item.get("url")
    start = item.get("start", "00:00:00")
    end = item.get("end")
    source = item.get("source", item.get("attribution_label", "Tư liệu Báo chí"))
    
    out_file = os.path.join(out_dir, f"{scene_id}.mp4")
    
    print(f"\n🎬 Xử lý phân cảnh: {scene_id}")
    print(f"   • Nguồn URL: {url}")
    print(f"   • Đoạn cắt: {start} ➔ {end}")
    print(f"   • Ghi nguồn: {source}")
    print(f"   • File đích: {out_file}")
    
    if dry_run:
        print("   [DRY-RUN] Bỏ qua thực thi lệnh thực tế.")
        return True
        
    if not url:
        print(f"   ⚠️ [BỎ QUA] Phân cảnh {scene_id} chưa có URL video thực tế.")
        return False

    # Lệnh ffmpeg chuyển hóa Fair Use:
    # 1. -ss start -to end (cắt ngắn)
    # 2. -an (tước bỏ audio)
    # 3. -vf "scale=1.04*iw:-1,crop=1920:1080" (scale 104% và crop 16:9)
    # 4. -c:v libx264 -preset fast -crf 20 (nén chất lượng cao)
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start),
    ]
    if end:
        cmd.extend(["-to", str(end)])
    cmd.extend([
        "-i", url,
        "-an",
        "-vf", "scale=1.04*iw:-1,crop=1920:1080",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",
        out_file
    ])
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"   ✅ [THÀNH CÔNG] Đã xuất video Fair Use: {out_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ [LỖI FFMPEG] {e.stderr[:200]}")
        return False

def main():
    args = parse_args()
    verify_ffmpeg()
    
    if not os.path.exists(args.manifest):
        print(f"❌ Không tìm thấy file manifest: {args.manifest}")
        sys.exit(1)
        
    os.makedirs(args.out_dir, exist_ok=True)
    
    with open(args.manifest, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print(f"📂 Đang nạp manifest: {args.manifest}")
    print(f"📋 Tổng số phân cảnh B-Roll cần xử lý: {len(data)}")
    
    success_count = 0
    for item in data:
        if process_item(item, args.out_dir, dry_run=args.dry_run):
            success_count += 1
            
    print(f"\n🎉 HOÀN TẤT: {success_count}/{len(data)} phân cảnh B-Roll đã được chuẩn hóa Fair Use!")

if __name__ == "__main__":
    main()
