#!/usr/bin/env python3
"""CLI Script tra cứu trạng thái mã hóa (Encoding) của video đã tải lên Facebook."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.fb_client import FacebookClient


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra trạng thái mã hóa video trên Facebook.")
    parser.add_argument("--video-id", required=True, help="Video ID nhận được sau khi upload")

    args = parser.parse_args()

    client = FacebookClient()
    try:
        data = client.get_video_status(args.video_id)
        print("==================================================")
        print(f"📹 TRẠNG THÁI VIDEO FACEBOOK: {args.video_id}")
        print("==================================================")
        print(f"Tiêu đề        : {data.get('title', 'N/A')}")
        print(f"Thời lượng (s) : {data.get('length', 'Đang xử lý')}")
        print(f"Trạng thái     : {data.get('status', {}).get('video_status', 'N/A')}")
        print(f"Xuất bản       : {data.get('published', False)}")
        if data.get('scheduled_publish_time'):
            print(f"Lên lịch lúc   : {data.get('scheduled_publish_time')}")
        print("--------------------------------------------------")
        status_detail = data.get('status', {})
        print(f"Chi tiết mã hóa: {status_detail}")
    except Exception as e:
        print(f"❌ Không thể lấy thông tin video: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
