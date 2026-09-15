#!/usr/bin/env python3
"""CLI Script tải video dung lượng lớn (GB) lên Facebook bằng Resumable Chunked Upload."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.resumable_uploader import ResumableVideoUploader
from src.post_manager import PostManager


def main():
    parser = argparse.ArgumentParser(description="Upload video dài lên Fanpage Facebook (Chunked Resumable Upload).")
    parser.add_argument("--file", required=True, help="Đường dẫn tuyệt đối tới file video MP4/MOV")
    parser.add_argument("--title", required=True, help="Tiêu đề video hiển thị trên Facebook")
    parser.add_argument("--desc", default="", help="Nội dung mô tả / caption trực tiếp")
    parser.add_argument("--desc-file", default="", help="Đọc mô tả từ file văn bản (.txt / .md)")
    parser.add_argument("--thumb", default=None, help="Đường dẫn tới ảnh thumbnail tùy chỉnh (.jpg/.png)")
    parser.add_argument("--schedule", default=None, help="Hẹn giờ phát sóng (Định dạng: YYYY-MM-DD HH:MM)")
    parser.add_argument("--draft", action="store_true", help="Lưu dưới dạng bản nháp (không xuất bản ngay)")

    args = parser.parse_args()

    description = args.desc
    if args.desc_file:
        desc_path = Path(args.desc_file)
        if desc_path.exists():
            with open(desc_path, "r", encoding="utf-8") as f:
                description = f.read().strip()
        else:
            print(f"❌ Không tìm thấy file mô tả: {args.desc_file}")
            sys.exit(1)

    if not description:
        description = args.title

    scheduled_timestamp = None
    if args.schedule:
        try:
            scheduled_timestamp = PostManager.parse_schedule_time(args.schedule)
            print(f"🕒 Đã lên lịch phát sóng vào: {args.schedule} (Unix: {scheduled_timestamp})")
        except Exception as e:
            print(f"❌ Lỗi định dạng thời gian: {e}")
            sys.exit(1)

    published = not (args.draft or bool(args.schedule))

    uploader = ResumableVideoUploader()
    post_manager = PostManager()

    try:
        res = uploader.upload(
            video_path=args.file,
            title=args.title,
            description=description,
            thumb_path=args.thumb,
            published=published,
            scheduled_publish_time=scheduled_timestamp,
        )

        video_id = res["video_id"]
        post_manager.log_published({
            "type": "video",
            "video_id": video_id,
            "title": args.title,
            "file": args.file,
            "scheduled": args.schedule if args.schedule else "Instant",
            "published": published,
        })

        print("\n🎉 HOÀN TẤT TẢI LÊN!")
        print(f"Video ID: {video_id}")
        print("Facebook đang tiến hành xử lý và mã hóa video (SD/HD).")
        print(f"Để kiểm tra tiến độ, chạy: python scripts/check_video_status.py --video-id {video_id}")

    except Exception as e:
        print(f"\n❌ TẢI LÊN THẤT BẠI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
