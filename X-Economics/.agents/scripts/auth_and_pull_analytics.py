import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube.force-ssl'
]

CLIENT_SECRET = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials/client_secret.json"
TOKEN_PATH = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials/token.json"

def authenticate_and_pull():
    print("Khởi động xác thực Google OAuth2 để lấy dữ liệu Analytics bảo mật...")
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
    creds = flow.run_local_server(port=8080)
    
    with open(TOKEN_PATH, "w") as token:
        token.write(creds.to_json())
    print("Xác thực thành công! Token đã được lưu.")
    
    analytics = build('youtubeAnalytics', 'v2', credentials=creds)
    # Fetch last 30 days
    from datetime import datetime, timedelta
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    
    res = analytics.reports().query(
        ids='channel==MINE',
        startDate=start_date,
        endDate=end_date,
        metrics='views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage',
        dimensions='video',
        sort='-views',
        maxResults=50
    ).execute()
    
    with open("/Users/pro16/Documents/VideoProject/X-Economics/.agents/scripts/full_analytics_data.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
        
    print("Đã kéo toàn bộ số liệu AVD, Tỷ lệ xem trung bình của kênh về máy!")

if __name__ == "__main__":
    authenticate_and_pull()
