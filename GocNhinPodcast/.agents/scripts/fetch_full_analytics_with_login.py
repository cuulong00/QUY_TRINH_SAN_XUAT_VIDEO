import os
import sys
import json
from datetime import datetime, timedelta

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube.force-ssl'
]

CREDS_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/credentials"
CLIENT_SECRET = os.path.join(CREDS_DIR, "client_secret_439442313894-5vh2dak3l4lv3kii8cirk6r3rvpfshs3.apps.googleusercontent.com.json")
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"⚠️ Refresh token không còn hiệu lực ({e}). Đang mở trình duyệt để xác thực lại...")
                creds = None
        if not creds:
            print("🚀 Đang mở trình duyệt để bạn xác thực tài khoản Google...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(TOKEN_PATH, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
            print("✅ Đã xác thực thành công và lưu token mới!")
    return creds

def fetch_and_report():
    creds = get_credentials()
    analytics = build('youtubeAnalytics', 'v2', credentials=creds)
    youtube = build('youtube', 'v3', credentials=creds)

    print("\n⏳ Đang truy vấn YouTube Analytics API cho kênh...")
    
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
    
    # Query video performance metrics
    res = analytics.reports().query(
        ids='channel==MINE',
        startDate=start_date,
        endDate=end_date,
        metrics='views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained',
        dimensions='video',
        sort='-views',
        maxResults=50
    ).execute()
    
    headers = [col['name'] for col in res.get('columnHeaders', [])]
    rows = res.get('rows', [])
    
    # Also fetch video titles from youtube Data API
    video_ids = [r[0] for r in rows]
    titles_map = {}
    for i in range(0, len(video_ids), 50):
        chunk = video_ids[i:i+50]
        v_res = youtube.videos().list(part='snippet', id=",".join(chunk)).execute()
        for it in v_res.get('items', []):
            titles_map[it['id']] = it['snippet']['title']
            
    print(f"\n📊 BÁO CÁO CHI TIẾT TỶ LỆ XEM TRUNG BÌNH (AVD & APV) CỦA {len(rows)} VIDEO:")
    print("-" * 105)
    print(f"{'STT':<4} | {'Views':<10} | {'AVD (Phút:Giây)':<16} | {'APV (%)':<10} | {'Sub +':<6} | Tiêu đề Video")
    print("-" * 105)
    
    report_data = []
    for idx, row in enumerate(rows, 1):
        vid = row[0]
        views = row[1]
        watch_mins = row[2]
        avd_sec = row[3]
        apv_pct = row[4]
        subs = row[5]
        
        mins = int(avd_sec // 60)
        secs = int(avd_sec % 60)
        avd_str = f"{mins:02d}:{secs:02d}"
        title = titles_map.get(vid, vid)
        
        print(f"{idx:<4} | {views:<10,d} | {avd_str:<16} | {apv_pct:<9.1f}% | {subs:<6} | {title[:48]}")
        report_data.append({
            "id": vid,
            "title": title,
            "views": views,
            "avd": avd_str,
            "avd_sec": avd_sec,
            "apv": apv_pct,
            "subs": subs
        })
        
    with open("/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/scripts/youtube_analytics_report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print("-" * 105)
    print("🎉 Hoàn tất! Dữ liệu đã được lưu vào youtube_analytics_report.json")

if __name__ == "__main__":
    fetch_and_report()
