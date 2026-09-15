import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Yêu cầu quyền truy cập chỉ đọc vào dữ liệu YouTube
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def main():
    creds = None
    # File token.json lưu trữ token truy cập sau khi bạn đăng nhập lần đầu thành công.
    # Nhờ file này, những lần sau script chạy ngầm sẽ không bắt bạn đăng nhập nữa.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Nếu chưa có token hợp lệ, mở trình duyệt để bạn đăng nhập và cấp quyền
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Lưu lại token cho những lần chạy sau
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Khởi tạo YouTube API client
    print("⏳ Đang kết nối với YouTube API...")
    youtube = build('youtube', 'v3', credentials=creds)

    # Lấy thông tin kênh (channel) của chính bạn
    request = youtube.channels().list(
        part="snippet,statistics",
        mine=True
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        channel = response['items'][0]
        title = channel['snippet']['title']
        stats = channel['statistics']
        
        print("\n" + "="*40)
        print("✅ KẾT NỐI VÀ ĐĂNG NHẬP THÀNH CÔNG!")
        print("="*40)
        print(f"📺 Tên kênh: {title}")
        print(f"👀 Tổng lượt xem: {stats.get('viewCount', 0)}")
        print(f"👥 Tổng Subscriber: {stats.get('subscriberCount', 0)}")
        print(f"🎬 Tổng số Video: {stats.get('videoCount', 0)}")
        print("="*40)
        print("\nTuyệt vời! Tôi đã có quyền truy cập kênh của bạn.")
    else:
        print("❌ Không tìm thấy kênh YouTube nào liên kết với tài khoản này.")

if __name__ == '__main__':
    main()
