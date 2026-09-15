import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Lần này chúng ta cần quyền truy cập vào Analytics (Dữ liệu phân tích bí mật)
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

def main():
    creds = None
    analytics_token_path = os.path.join(os.path.dirname(__file__), '../tokens/analytics_token.json')
    credentials_path = os.path.join(os.path.dirname(__file__), '../tokens/credentials.json')
    # Dùng file token riêng cho Analytics để không đè lên file cũ
    if os.path.exists(analytics_token_path):
        creds = Credentials.from_authorized_user_file(analytics_token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(analytics_token_path, 'w') as token:
            token.write(creds.to_json())

    print("⏳ Đang kéo dữ liệu AVD từ YouTube Analytics...")
    youtubeAnalytics = build('youtubeAnalytics', 'v2', credentials=creds)

    # Lấy dữ liệu của 28 ngày gần nhất
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=28)).strftime('%Y-%m-%d')

    request = youtubeAnalytics.reports().query(
        startDate=start_date,
        endDate=end_date,
        ids="channel==MINE",
        metrics="averageViewDuration", # Chỉ số AVD
    )
    response = request.execute()

    if 'rows' in response and len(response['rows']) > 0:
        avd_seconds = response['rows'][0][0]
        avd_minutes = int(avd_seconds // 60)
        avd_secs_remainder = int(avd_seconds % 60)
        
        print("\n" + "="*40)
        print("📊 DỮ LIỆU RETENTION KÊNH DÒNG CHẢY (28 Ngày Qua)")
        print("="*40)
        print(f"⏱️ Thời lượng xem trung bình (AVD): {avd_minutes} phút {avd_secs_remainder} giây")
        print("="*40)
    else:
        print("Không có dữ liệu analytics trong 28 ngày qua.")

if __name__ == '__main__':
    main()
