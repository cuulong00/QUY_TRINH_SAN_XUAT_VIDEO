#!/usr/bin/env python3
import os
import sys
import re
import shutil

def organize_folder(target_dir):
    target_dir = os.path.expanduser(target_dir.strip())
    
    if not os.path.exists(target_dir):
        print(f"❌ Lỗi: Thư mục không tồn tại: {target_dir}")
        sys.exit(1)
        
    if not os.path.isdir(target_dir):
        print(f"❌ Lỗi: Đường dẫn không phải là thư mục: {target_dir}")
        sys.exit(1)

    print(f"\n🚀 Đang quét và phân loại file trong: {target_dir}\n" + "="*50)

    # Regex nhận diện các mẫu tên: CH01, CH1, ch01, ch1, chapter_01, chapter1, c01, c1
    chapter_regex = re.compile(r'(?:CH(?:APTER)?|c)[-_]?0*(\d+)', re.IGNORECASE)

    moved_stats = {}
    unmatched_files = []
    total_files = 0

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # Bỏ qua nếu là thư mục con (ví dụ ch1, ch2 đã tạo sẵn) hoặc file ẩn hệ thống
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue

        total_files += 1
        match = chapter_regex.search(filename)

        if match:
            ch_num = int(match.group(1))
            ch_folder_name = f"ch{ch_num}"
            dest_dir = os.path.join(target_dir, ch_folder_name)
            
            # Tạo thư mục chX nếu chưa có
            os.makedirs(dest_dir, exist_ok=True)
            
            dest_file_path = os.path.join(dest_dir, filename)
            shutil.move(file_path, dest_file_path)
            
            moved_stats[ch_folder_name] = moved_stats.get(ch_folder_name, 0) + 1
            print(f"  📦 Đã chuyển: {filename} ➔ {ch_folder_name}/")
        else:
            unmatched_files.append(filename)

    print("\n" + "="*50)
    print(f"🎉 HOÀN TẤT PHÂN LOẠI ({total_files} files)")
    print("="*50)
    
    # In thống kê từng chương theo thứ tự
    for folder in sorted(moved_stats.keys(), key=lambda x: int(x.replace('ch', '')) if x.replace('ch', '').isdigit() else 999):
        print(f"  📁 Thư mục [{folder}]: {moved_stats[folder]} files")
        
    if unmatched_files:
        print(f"\n⚠️ Các file không nhận diện được chương ({len(unmatched_files)} files):")
        for uf in unmatched_files:
            print(f"  - {uf}")
    print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách sử dụng:")
        print("  python3 scripts/tools/organize_chapters.py \"/đường/dẫn/thư/mục\"")
        print("\nVí dụ:")
        print("  python3 scripts/tools/organize_chapters.py \"/Users/pro16/Downloads/longgiamvutru\"")
        sys.exit(1)
        
    organize_folder(sys.argv[1])
