#!/usr/bin/env python3
"""CLI Script chuyển hóa kịch bản từ tập YouTube sang bài đăng Facebook chuẩn Meta."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import READY_POSTS_DIR
from src.content_adapter import ContentAdapter


def main():
    parser = argparse.ArgumentParser(description="Chuyển đổi kịch bản tập YouTube sang bài đăng chuẩn Facebook.")
    parser.add_argument("--source", required=True, help="Đường dẫn tới thư mục tập YouTube nguồn (ví dụ: episodes/kinh-te-hoc-tam-linh)")
    parser.add_argument("--channel", default="gocnhin", choices=["gocnhin", "dong_chay"], help="Kênh nguồn: gocnhin hoặc dong_chay")
    parser.add_argument("--save", action="store_true", default=True, help="Lưu kết quả ra file trong storage/ready_posts/")

    args = parser.parse_args()

    adapter = ContentAdapter(channel=args.channel)
    try:
        result = adapter.adapt_from_folder(args.source)
    except Exception as e:
        print(f"❌ Lỗi khi đọc thư mục: {e}")
        sys.exit(1)

    print("==================================================")
    print("✨ GÓI BÀI ĐĂNG FACEBOOK CHUẨN META STRATEGIST")
    print("==================================================")
    print(f"Tiêu đề: {result['title']}")
    print("--------------------------------------------------")
    print("[NỘI DUNG CAPTION]:")
    print(result['caption'])
    print("--------------------------------------------------")
    print(f"[BÌNH LUẬN ĐẦU TIÊN (FIRST COMMENT)]:")
    print(result['first_comment'])
    print("==================================================")

    if args.save:
        source_name = Path(args.source).name
        output_file = READY_POSTS_DIR / f"{source_name}_fb_post.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"TIÊU ĐỀ: {result['title']}\n\n")
            f.write("--- CAPTION ---\n")
            f.write(result['caption'] + "\n\n")
            f.write("--- FIRST COMMENT ---\n")
            f.write(result['first_comment'] + "\n")
        print(f"📁 Đã lưu gói bài viết tại: {output_file}")


if __name__ == "__main__":
    main()
