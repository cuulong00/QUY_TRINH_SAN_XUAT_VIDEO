import os
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def main():
    creds = None
    token_file = '../tokens/manager_token.json'
    credentials_file = '../tokens/credentials.json'

    if os.path.exists(token_file):
        try:
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        except Exception:
            creds = None
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES)
            
            prompt_msg = (
                "\n" + "="*60 + "\n"
                "🔑 VUI LÒNG MỞ TRÌNH DUYỆT VÀ TRUY CẬP ĐƯỜNG DẪN SAU ĐỂ CẤP QUYỀN:\n\n"
                "{url}\n"
                + "="*60 + "\n"
            )
            
            # Use prompt='select_account consent' so Google forces the Account / Brand Account selection screen
            creds = flow.run_local_server(port=0, authorization_prompt_message=prompt_msg, prompt='select_account consent')
        
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    print("⏳ Đang kết nối với YouTube API bằng quyền Quản lý...")
    youtube = build('youtube', 'v3', credentials=creds)

    request = youtube.channels().list(
        part="snippet,statistics",
        mine=True
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        channel = response['items'][0]
        title = channel['snippet']['title']
        stats = channel['statistics']
        
        print("\n" + "="*50)
        print("✅ KẾT NỐI VÀ ĐĂNG NHẬP THÀNH CÔNG VỚI QUYỀN QUẢN LÝ!")
        print("="*50)
        print(f"📺 Tên kênh: {title}")
        print(f"👀 Quyền truy cập: Full Access (Đọc & Cập nhật video)")
        print(f"👥 Subscribers: {stats.get('subscriberCount', 0)}")
        print("="*50)
    else:
        print("❌ Không tìm thấy kênh YouTube liên kết.")

if __name__ == '__main__':
    main()
