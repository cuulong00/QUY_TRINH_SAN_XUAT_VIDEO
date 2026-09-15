#!/usr/bin/env python3
"""Script kiểm tra cấu hình Page ID, Access Token và kết nối Fanpage."""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN, FB_API_VERSION
from src.fb_client import FacebookClient


def main():
    print("==================================================")
    print("🔍 KIỂM TRA KẾT NỐI FACEBOOK GRAPH API")
    print("==================================================")
    print(f"API Version : {FB_API_VERSION}")
    print(f"Page ID     : {FB_PAGE_ID if FB_PAGE_ID else '[CHƯA CẤU HÌNH]'}")
    print(f"Token       : {'******' + FB_PAGE_ACCESS_TOKEN[-6:] if len(FB_PAGE_ACCESS_TOKEN) > 6 else '[CHƯA CẤU HÌNH]'}")
    print("--------------------------------------------------")

    if not FB_PAGE_ID or not FB_PAGE_ACCESS_TOKEN:
        print("❌ LỖI: Vui lòng tạo file .env từ .env.example và điền đầy đủ FB_PAGE_ID và FB_PAGE_ACCESS_TOKEN.")
        print("Xem hướng dẫn lấy token tại: 00_core/graph_api_guide.md")
        sys.exit(1)

    client = FacebookClient()
    try:
        print("Đang gọi Meta Graph API để lấy thông tin Fanpage...")
        info = client.get_page_info()
        print("✅ KẾT NỐI THÀNH CÔNG!")
        print(f"  • Tên Fanpage : {info.get('name')}")
        print(f"  • Chuyên mục  : {info.get('category')}")
        print(f"  • ID          : {info.get('id')}")
        print(f"  • Lượt theo dõi: {info.get('followers_count', 'N/A')}")
        print(f"  • Lượt thích  : {info.get('fan_count', 'N/A')}")
        print(f"  • Đường dẫn   : {info.get('link', 'N/A')}")
    except Exception as e:
        print(f"❌ KẾT NỐI THẤT BẠI: {e}")
        print("Gợi ý: Kiểm tra lại xem Page ID và Token đã đúng quyền pages_manage_posts và publish_video chưa.")
        sys.exit(1)


if __name__ == "__main__":
    main()
