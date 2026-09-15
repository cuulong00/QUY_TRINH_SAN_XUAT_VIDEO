import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
token_file = '../tokens/manager_token.json'

if os.path.exists(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)

    print("🔍 Đang kiểm tra tất cả các kênh liên kết với tài khoản này...")
    request = youtube.channels().list(
        part="snippet,statistics",
        mine=True
    )
    response = request.execute()

    for item in response.get('items', []):
        print(f"📺 Channel ID: {item['id']} | Title: {item['snippet']['title']}")
else:
    print("❌ Chưa tìm thấy manager_token.json")
