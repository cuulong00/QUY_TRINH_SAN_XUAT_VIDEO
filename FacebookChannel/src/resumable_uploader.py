"""Meta Graph Video Resumable Chunked Uploader.
Designed to handle multi-gigabyte (5GB - 15GB) video uploads safely with progress reporting and auto-retries.
"""

import os
import sys
import time
import logging
import requests
from pathlib import Path
from typing import Optional, Dict, Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config.settings import GRAPH_VIDEO_BASE_URL, CHUNK_SIZE_BYTES, FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ResumableUploader")


class ResumableVideoUploader:
    """Manages chunked resumable video uploads to Facebook Graph Video API."""

    def __init__(
        self,
        page_id: Optional[str] = None,
        access_token: Optional[str] = None,
        chunk_size: int = CHUNK_SIZE_BYTES,
        max_retries: int = 5,
    ):
        self.page_id = page_id or FB_PAGE_ID
        self.access_token = access_token or FB_PAGE_ACCESS_TOKEN
        self.chunk_size = chunk_size
        self.max_retries = max_retries
        self.upload_url = f"{GRAPH_VIDEO_BASE_URL}/{self.page_id}/videos"

    def upload(
        self,
        video_path: str,
        title: str,
        description: str,
        thumb_path: Optional[str] = None,
        published: bool = True,
        scheduled_publish_time: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Executes full 3-phase resumable video upload protocol."""
        path = Path(video_path)
        if not path.exists():
            raise FileNotFoundError(f"File video không tồn tại: {video_path}")

        file_size = path.stat().st_size
        logger.info(f"Bắt đầu quy trình tải video: {path.name}")
        logger.info(f"Dung lượng: {file_size / (1024 * 1024):.2f} MB ({file_size / (1024 * 1024 * 1024):.2f} GB)")

        # Phase 1: Start
        session_data = self._start_upload_session(file_size)
        session_id = session_data["upload_session_id"]
        video_id = session_data["video_id"]
        start_offset = int(session_data.get("start_offset", 0))

        logger.info(f"Khởi tạo phiên thành công. Video ID: {video_id}, Session ID: {session_id}")

        # Phase 2: Transfer chunks
        self._transfer_chunks(path, session_id, file_size, start_offset)

        # Phase 3: Finish
        logger.info("Đang hoàn tất phiên tải lên (Phase 3: Finish)...")
        result = self._finish_upload(
            session_id=session_id,
            title=title,
            description=description,
            thumb_path=thumb_path,
            published=published,
            scheduled_publish_time=scheduled_publish_time,
        )

        logger.info(f"✅ Tải lên video thành công! Video ID: {video_id}")
        return {"video_id": video_id, "result": result}

    def _start_upload_session(self, file_size: int) -> Dict[str, Any]:
        """Phase 1: Khởi tạo upload session với Meta."""
        params = {
            "upload_phase": "start",
            "file_size": str(file_size),
            "access_token": self.access_token,
        }
        resp = requests.post(self.upload_url, data=params, timeout=60)
        data = resp.json()
        if "error" in data:
            raise RuntimeError(f"Lỗi khởi tạo upload session: {data['error'].get('message')}")
        return data

    def _transfer_chunks(self, path: Path, session_id: str, file_size: int, start_offset: int):
        """Phase 2: Cắt nhỏ file và stream các chunks tuần tự."""
        try:
            from tqdm import tqdm
            use_tqdm = True
        except ImportError:
            use_tqdm = False

        pbar = None
        if use_tqdm:
            pbar = tqdm(total=file_size, initial=start_offset, unit="B", unit_scale=True, desc="Uploading")

        with open(path, "rb") as f:
            while start_offset < file_size:
                f.seek(start_offset)
                chunk = f.read(self.chunk_size)
                chunk_len = len(chunk)

                if chunk_len == 0:
                    break

                # Transfer with retry logic
                success = False
                for attempt in range(1, self.max_retries + 1):
                    try:
                        data = {
                            "upload_phase": "transfer",
                            "upload_session_id": session_id,
                            "start_offset": str(start_offset),
                            "access_token": self.access_token,
                        }
                        files = {
                            "video_file_chunk": ("chunk.bin", chunk, "application/octet-stream")
                        }
                        resp = requests.post(self.upload_url, data=data, files=files, timeout=120)
                        res_json = resp.json()

                        if "error" in res_json:
                            raise RuntimeError(res_json["error"].get("message"))

                        new_start_offset = int(res_json.get("start_offset", start_offset + chunk_len))
                        if pbar:
                            pbar.update(new_start_offset - start_offset)

                        start_offset = new_start_offset
                        success = True
                        break

                    except Exception as exc:
                        logger.warning(f"Lỗi gửi chunk tại offset {start_offset} (Lần thử {attempt}/{self.max_retries}): {exc}")
                        if attempt == self.max_retries:
                            raise RuntimeError(f"Thất bại khi gửi chunk tại offset {start_offset} sau {self.max_retries} lần thử.")
                        time.sleep(2 ** attempt)

                if not success:
                    break

        if pbar:
            pbar.close()

    def _finish_upload(
        self,
        session_id: str,
        title: str,
        description: str,
        thumb_path: Optional[str] = None,
        published: bool = True,
        scheduled_publish_time: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Phase 3: Gắn metadata và xuất bản video."""
        data: Dict[str, Any] = {
            "upload_phase": "finish",
            "upload_session_id": session_id,
            "title": title,
            "description": description,
            "access_token": self.access_token,
        }

        if scheduled_publish_time:
            data["published"] = False
            data["scheduled_publish_time"] = scheduled_publish_time
        else:
            data["published"] = published

        files = {}
        thumb_file_handle = None
        if thumb_path and Path(thumb_path).exists():
            thumb_file_handle = open(thumb_path, "rb")
            files["thumb"] = thumb_file_handle

        try:
            resp = requests.post(self.upload_url, data=data, files=files if files else None, timeout=120)
            res_json = resp.json()
            if "error" in res_json:
                raise RuntimeError(f"Lỗi hoàn tất upload video: {res_json['error'].get('message')}")
            return res_json
        finally:
            if thumb_file_handle:
                thumb_file_handle.close()
