#!/usr/bin/env python3
"""CLI Script đăng bài viết văn bản hoặc hình ảnh lên Fanpage Facebook."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.fb_client import FacebookClient
from src.post_manager import PostManager


def main():
    parser = argparse.ArgumentParser(description="Đăng bài viết hoặc ảnh lên Facebook Fanpage.")
    parser.add_argument("--message", default="", help="Nội dung bài viết")
    parser.add_argument("--message-file", default="", help="Đọc nội dung bài viết từ file .txt / .md")
    parser.add_argument("--photo", default=None, help="Đường dẫn tới ảnh tải lên (nếu có)")
    parser.add_argument("--link", default=None, help="Đường dẫn liên kết đính kèm")

    args = parser.parse_args()

    message = args.message
    if args.message_file:
        p = Path(args.message_file)
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                message = f.read().strip()
        else:
            print(f"❌ Không tìm thấy file: {args.message_file}")
            sys.exit(1)

    if not message and not args.photo:
        print("❌ Vui lòng cung cấp nội dung (--message hoặc --message-file) hoặc hình ảnh (--photo).")
        sys.exit(1)

    client = FacebookClient()
    post_manager = PostManager(client=client)

    try:
        if args.photo:
            print(f"Đang tải ảnh: {args.photo} ...")
            res = client.upload_photo(photo_path=args.photo, caption=message)
            post_id = res.get("id") or res.get("post_id")
            print(f"✅ Đăng ảnh thành công! ID: {post_id}")
        else:
            print("Đang đăng bài viết lên Fanpage...")
            res = client.publish_feed_post(message=message, link=args.link)
            post_id = res.get("id")
            print(f"✅ Đăng bài viết thành công! Post ID: {post_id}")

        post_manager.log_published({
            "type": "photo" if args.photo else "post",
            "post_id": post_id,
            "message_snippet": message[:100],
        })

    except Exception as e:
        print(f"❌ Đăng bài thất bại: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
