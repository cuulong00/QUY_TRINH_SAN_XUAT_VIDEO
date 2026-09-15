#!/usr/bin/env python3
"""
Script tự động cập nhật khai báo AI (Synthetic Media / Altered Content) cho toàn bộ video trên kênh HieuBietHon qua YouTube Data API v3.
"""

import os
import sys
import argparse

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("❌ Thư viện Google API chưa được cài đặt.")
    print("👉 Hãy chạy: pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service(credentials_path, token_path):
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
            if not os.path.exists(credentials_path):
                cred_dir = os.path.dirname(credentials_path)
                found = []
                if os.path.exists(cred_dir):
                    found = [os.path.join(cred_dir, f) for f in os.listdir(cred_dir) if f.startswith('client_secret') and f.endswith('.json')]
                if found:
                    credentials_path = found[0]
                else:
                    print(f"❌ Không tìm thấy tệp client_secret tại: {credentials_path}")
                    sys.exit(1)
                
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            print("\n🔑 Vui lòng mở trình duyệt và đăng nhập nếu chưa tự mở...")
            creds = flow.run_local_server(port=8090)
            
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def update_ai_flag_for_all_videos(youtube):
    print("🔍 Đang lấy danh sách tất cả video từ kênh...")
    
    # 1. Lấy Uploads Playlist ID của channel
    channels_response = youtube.channels().list(
        mine=True,
        part='contentDetails'
    ).execute()
    
    if not channels_response.get('items'):
        print("❌ Không tìm thấy thông tin kênh!")
        return
        
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    # 2. Lấy toàn bộ video IDs từ Uploads Playlist
    video_ids = []
    next_page_token = None
    
    while True:
        playlist_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in playlist_response.get('items', []):
            video_ids.append((item['snippet']['title'], item['snippet']['resourceId']['videoId']))
            
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
            
    print(f"📹 Tổng số video tìm thấy trên kênh: {len(video_ids)}\n")
    
    success_count = 0
    for title, video_id in video_ids:
        print(f"🔄 Đang xử lý: [{title}] (ID: {video_id})...")
        try:
            # Lấy thông tin video hiện tại
            video_response = youtube.videos().list(
                part='status,snippet',
                id=video_id
            ).execute()
            
            items = video_response.get('items', [])
            if not items:
                print(f"  ❌ Không tìm thấy video ID: {video_id}")
                continue
                
            video_item = items[0]
            status = video_item.get('status', {})
            
            # Cập nhật cờ containsSyntheticMedia = True
            status['containsSyntheticMedia'] = True
            
            youtube.videos().update(
                part='status',
                body={
                    'id': video_id,
                    'status': status
                }
            ).execute()
            
            print(f"  ✅ Đã bật cờ 'Sử dụng AI / Synthetic Media' thành công!")
            success_count += 1
        except Exception as e:
            print(f"  ⚠️ Lỗi hoặc API chưa hỗ trợ ghi đè trực tiếp trường này qua API v3: {e}")
            print(f"  ℹ️ Vui lòng kiểm tra lại thiết lập trên Studio nếu API trả về lỗi thuộc tính.")

    print(f"\n🎉 HOÀN THÀNH: Đã quét và cập nhật cho {success_count}/{len(video_ids)} video!")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cred_dir = os.path.join(script_dir, "..", "credentials")
    cred_file = os.path.join(cred_dir, "client_secret_439442313894-5vh2dak3l4lv3kii8cirk6r3rvpfshs3.apps.googleusercontent.com.json")
    token_file = os.path.join(cred_dir, "token.json")
    
    print("🔐 Đang kết nối YouTube Data API v3...")
    youtube_service = get_authenticated_service(cred_file, token_file)
    update_ai_flag_for_all_videos(youtube_service)
