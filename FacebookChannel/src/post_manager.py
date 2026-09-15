"""Post Manager for FacebookChannel.
Handles post preparation, schedule calculation, and backlog status recording.
"""

import sys
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config.settings import BASE_DIR
from src.fb_client import FacebookClient

logger = logging.getLogger("PostManager")


class PostManager:
    """Manages publishing operations and status logs."""

    def __init__(self, client: Optional[FacebookClient] = None):
        self.client = client or FacebookClient()
        self.log_file = BASE_DIR / "01_management" / "published_log.jsonl"

    def log_published(self, entry: Dict[str, Any]):
        """Ghi nhận lịch sử bài/video đã đăng vào file JSONL."""
        entry["timestamp"] = datetime.now(timezone.utc).isoformat()
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.info(f"Đã lưu lịch sử xuất bản: {entry.get('title', 'N/A')}")

    @staticmethod
    def parse_schedule_time(schedule_str: str) -> int:
        """Chuyển chuỗi datetime (YYYY-MM-DD HH:MM) thành Unix timestamp."""
        dt = datetime.strptime(schedule_str.strip(), "%Y-%m-%d %H:%M")
        timestamp = int(dt.timestamp())
        now = int(datetime.now().timestamp())
        if timestamp < now + 600:
            raise ValueError("Thời gian hẹn giờ phải cách thời điểm hiện tại ít nhất 10 phút.")
        return timestamp
