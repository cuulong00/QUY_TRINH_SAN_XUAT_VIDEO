import os
import sys
import json
from datetime import datetime, timedelta

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/youtube.readonly'
]
CREDS_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

def main():
    if not os.path.exists(TOKEN_PATH):
        print("No token file found.")
        return
        
    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    try:
        analytics = build('youtubeAnalytics', 'v2', credentials=creds)
        
        # Query last 30 days
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
        
        res = analytics.reports().query(
            ids='channel==MINE',
            startDate=start_date,
            endDate=end_date,
            metrics='views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage',
            dimensions='video',
            sort='-views',
            maxResults=10
        ).execute()
        
        print("YouTube Analytics Query Success:")
        print(json.dumps(res, indent=2))
    except Exception as e:
        print(f"Analytics API Error: {e}")

if __name__ == "__main__":
    main()
