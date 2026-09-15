"""Meta Graph API Client wrapper for Facebook Page operations."""

import sys
import logging
import requests
from typing import Dict, Any, Optional
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config.settings import GRAPH_BASE_URL, GRAPH_VIDEO_BASE_URL, FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("FBClient")


class FacebookClient:
    """Handles communication with Facebook Graph API."""

    def __init__(self, page_id: Optional[str] = None, access_token: Optional[str] = None):
        self.page_id = page_id or FB_PAGE_ID
        self.access_token = access_token or FB_PAGE_ACCESS_TOKEN
        self.timeout = 60

        if not self.page_id or not self.access_token:
            logger.warning("FB_PAGE_ID hoặc FB_PAGE_ACCESS_TOKEN chưa được cấu hình đầy đủ.")

    def get_page_info(self) -> Dict[str, Any]:
        """Lấy thông tin cơ bản của Fanpage và kiểm tra tính hợp lệ của Token."""
        url = f"{GRAPH_BASE_URL}/{self.page_id}"
        params = {
            "fields": "id,name,category,link,followers_count,fan_count",
            "access_token": self.access_token,
        }
        resp = requests.get(url, params=params, timeout=self.timeout)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"Meta Graph API Error: {data['error'].get('message')} (Code: {data['error'].get('code')})")
        return data

    def check_permissions(self) -> Dict[str, Any]:
        """Kiểm tra quyền hạn được cấp cho Access Token hiện tại."""
        url = f"{GRAPH_BASE_URL}/debug_token"
        params = {
            "input_token": self.access_token,
            "access_token": self.access_token,
        }
        resp = requests.get(url, params=params, timeout=self.timeout)
        return resp.json()

    def publish_feed_post(self, message: str, link: Optional[str] = None, scheduled_publish_time: Optional[int] = None) -> Dict[str, Any]:
        """Đăng một bài viết thông thường (text hoặc kèm link) lên Fanpage."""
        url = f"{GRAPH_BASE_URL}/{self.page_id}/feed"
        payload: Dict[str, Any] = {
            "message": message,
            "access_token": self.access_token,
        }
        if link:
            payload["link"] = link
        if scheduled_publish_time:
            payload["published"] = False
            payload["scheduled_publish_time"] = scheduled_publish_time

        resp = requests.post(url, data=payload, timeout=self.timeout)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"Lỗi đăng bài viết: {data['error'].get('message')}")
        return data

    def upload_photo(self, photo_path: str, caption: Optional[str] = None) -> Dict[str, Any]:
        """Tải ảnh lên Fanpage."""
        url = f"{GRAPH_BASE_URL}/{self.page_id}/photos"
        path = Path(photo_path)
        if not path.exists():
            raise FileNotFoundError(f"Không tìm thấy ảnh tại: {photo_path}")

        payload: Dict[str, Any] = {"access_token": self.access_token}
        if caption:
            payload["caption"] = caption

        with open(path, "rb") as img_file:
            files = {"source": img_file}
            resp = requests.post(url, data=payload, files=files, timeout=self.timeout)

        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"Lỗi tải ảnh: {data['error'].get('message')}")
        return data

    def get_video_status(self, video_id: str) -> Dict[str, Any]:
        """Tra cứu trạng thái xử lý mã hóa của video trên Facebook."""
        url = f"{GRAPH_VIDEO_BASE_URL}/{video_id}"
        params = {
            "fields": "id,title,description,status,published,scheduled_publish_time,length",
            "access_token": self.access_token,
        }
        resp = requests.get(url, params=params, timeout=self.timeout)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"Lỗi kiểm tra video: {data['error'].get('message')}")
        return data
