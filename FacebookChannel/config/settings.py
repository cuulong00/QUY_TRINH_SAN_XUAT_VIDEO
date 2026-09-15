"""Centralized settings and environment loader for FacebookChannel."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Load .env file
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    # Also attempt loading from parent if needed
    load_dotenv()

# Meta Graph API Configuration
FB_PAGE_ID = os.getenv("FB_PAGE_ID", "").strip()
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "").strip()
FB_API_VERSION = os.getenv("FB_API_VERSION", "v20.0").strip()

# Resumable Upload Configuration
# Chunk size in MB (Default 8 MB; recommended 4MB - 16MB)
CHUNK_SIZE_MB = int(os.getenv("FB_UPLOAD_CHUNK_SIZE_MB", "8"))
CHUNK_SIZE_BYTES = CHUNK_SIZE_MB * 1024 * 1024

# Base API URLs
GRAPH_BASE_URL = f"https://graph.facebook.com/{FB_API_VERSION}"
GRAPH_VIDEO_BASE_URL = f"https://graph-video.facebook.com/{FB_API_VERSION}"

# Directories
STORAGE_DIR = BASE_DIR / "storage"
THUMBNAIL_DIR = STORAGE_DIR / "thumbnails"
LOG_DIR = STORAGE_DIR / "logs"
READY_POSTS_DIR = STORAGE_DIR / "ready_posts"

for d in [STORAGE_DIR, THUMBNAIL_DIR, LOG_DIR, READY_POSTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)
