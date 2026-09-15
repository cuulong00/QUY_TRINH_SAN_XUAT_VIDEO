import os
import sys

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    # Get channel uploads playlist ID
    ch_res = youtube.channels().list(mine=True, part='contentDetails').execute()
    uploads_id = ch_res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    # List all items in uploads playlist
    res = youtube.playlistItems().list(
        playlistId=uploads_id,
        part='snippet',
        maxResults=50
    ).execute()
    
    items = res.get('items', [])
    print(f"Total videos found on channel: {len(items)}\n")
    
    video_map = []
    for item in items:
        vid = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        video_map.append({'id': vid, 'title': title})
        print(f"ID: {vid} | Title: {title}")
        
    with open(".agents/scripts/video_id_map.json", "w", encoding="utf-8") as f:
        import json
        json.dump(video_map, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
