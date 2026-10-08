#!/usr/bin/env python3
"""
YouTube Video Description Auto-Updater (Role: Channel Manager)
Kênh: GocNhinPodcast (@GocNhin_Podcast)
Tác dụng: Tự động đăng nhập Google OAuth 2.0 với quyền Quản trị kênh (Channel Manager),
sau đó cập nhật trực tiếp Mô tả mới có chứa Disclaimer chuẩn E-E-A-T cho toàn bộ video dính cờ YMYL.
"""

import os
import sys
import re
import json
import argparse

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("❌ Thư viện Google API chưa được cài đặt.")
    print("👉 Hãy chạy lệnh sau để cài đặt: pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

# Đoạn Disclaimer chuẩn E-E-A-T & YMYL Safe
STANDARD_DISCLAIMER_BLOCK = """
--------------------------------------------------
ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:
Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và nguồn tin báo chí chính thống. Video mang tính chất phân tích phóng sự tài liệu, kiến thức kinh tế vĩ mô và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.

🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ:
- Biên tập & Nghiên cứu: Ban Biên tập GocNhinPodcast
- Định dạng: Phim tài liệu đồ họa (Editorial Vector Graphic Animation)
- Công nghệ hỗ trợ: Đồ họa và giọng đọc được tối ưu bằng công nghệ AI dưới sự kiểm duyệt và hoàn thiện 100% từ đội ngũ biên tập viên.

📚 NGUỒN TÀI LIỆU THAM KHẢO CHÍNH:
- Báo cáo tài chính đã kiểm toán / Tổng cục Thống kê / World Bank / IMF
- Nghị định / Thông tư / Văn bản quy phạm pháp luật liên quan
--------------------------------------------------
"""

def get_authenticated_service(credentials_path, token_path):
    """Xác thực Google OAuth 2.0 để lấy quyền Quản trị kênh"""
    creds = None
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception:
            creds = None
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"⚠️ Token đã hết hạn hoặc bị hủy ({e}). Đang khởi tạo lại phiên đăng nhập...")
                if os.path.exists(token_path):
                    os.remove(token_path)
                creds = None

        if not creds:
            # Tự động tìm kiếm file client_secret*.json nếu file mặc định không tồn tại
            if not os.path.exists(credentials_path):
                cred_dir = os.path.dirname(credentials_path)
                found = []
                if os.path.exists(cred_dir):
                    found = [os.path.join(cred_dir, f) for f in os.listdir(cred_dir) if f.startswith('client_secret') and f.endswith('.json')]
                if found:
                    credentials_path = found[0]
                    print(f"🔑 Đã tìm thấy tệp xác thực OAuth tại: {credentials_path}")
                else:
                    print(f"❌ Không tìm thấy tệp xác thực Google OAuth tại: {credentials_path}")
                    print("\n📌 HƯỚNG DẪN TẠO FILE TẢI VỀ CLIENT SECRET (MẤT 2 PHÚT):")
                    print("1. Truy cập: https://console.cloud.google.com/")
                    print("2. Bật API: 'YouTube Data API v3'")
                    print("3. Tạo Credentials -> 'OAuth 2.0 Client ID' (Loại: Desktop App)")
                    print(f"4. Tải file JSON về và lưu tại đường dẫn: {credentials_path}\n")
                    sys.exit(1)
                
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def update_video_descriptions(youtube, audit_report_path):
    """Đọc báo cáo audit và tự động cập nhật Mô tả video trên YouTube Studio"""
    if not os.path.exists(audit_report_path):
        print(f"❌ Không tìm thấy tệp báo cáo audit: {audit_report_path}")
        print("👉 Hãy chạy script scanner trước: python3 .agents/scripts/youtube_ymyl_scanner.py")
        sys.exit(1)
        
    with open(audit_report_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Bóc tách danh sách video cần khắc phục từ báo cáo
    pattern = r"### 📹 Video: \[(.*?)\]\(https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)\)[\s\S]*?```text\n([\s\S]*?)\n```"
    matches = re.findall(pattern, content)
    
    if not matches:
        print("🎉 Không có video nào cần cập nhật hoặc tất cả video đã an toàn!")
        return
        
    print(f"🚀 Tìm thấy {len(matches)} video cần cập nhật Mô tả trực tiếp trên YouTube Studio...\n")
    
    success_count = 0
    for title, video_id, new_description in matches:
        print(f"🔄 Đang xử lý Video: [{title}] (ID: {video_id})...")
        try:
            # 1. Lấy thông tin hiện tại của Video từ API
            video_response = youtube.videos().list(
                part='snippet',
                id=video_id
            ).execute()
            
            items = video_response.get('items', [])
            if not items:
                print(f"  ❌ Không tìm thấy video trên kênh với ID: {video_id}")
                continue
                
            snippet = items[0]['snippet']
            
            # Kiểm tra xem đã có Disclaimer chưa
            if "TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM" in snippet.get('description', ''):
                print(f"  ⏩ Video đã có Disclaimer chuẩn. Bỏ qua.")
                continue
                
            # 2. Cập nhật snippet với Mô tả mới
            snippet['description'] = new_description
            
            # 3. Gọi API Update
            youtube.videos().update(
                part='snippet',
                body={
                    'id': video_id,
                    'snippet': snippet
                }
            ).execute()
            
            print(f"  ✅ Đã cập nhật thành công Mô tả mới cho video [{title}]!")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Lỗi khi cập nhật video ID {video_id}: {e}")
            
    print(f"\n🎉 HOÀN THÀNH: Đã tự động cập nhật Mô tả an toàn YMYL cho {success_count}/{len(matches)} video!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Description Auto-Updater")
    parser.add_argument("--credentials", default=".agents/credentials/client_secret.json", help="Path to Google OAuth client_secret.json")
    parser.add_argument("--token", default=".agents/credentials/token.json", help="Path to save OAuth token")
    parser.add_argument("--report", default="episodes/youtube_ymyl_audit_report.md", help="Path to YMYL audit report")
    args = parser.parse_args()
    
    print("🔐 Khởi động Trình quản trị YouTube Studio Auto-Updater...")
    youtube_service = get_authenticated_service(args.credentials, args.token)
    update_video_descriptions(youtube_service, args.report)
