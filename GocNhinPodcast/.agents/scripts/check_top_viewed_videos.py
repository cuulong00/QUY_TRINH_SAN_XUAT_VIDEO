import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/credentials/token.json"
CLIENT_SECRET_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/credentials/client_secret.json"
MAP_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/scripts/video_id_map.json"

def main():
    if not os.path.exists(TOKEN_PATH):
        print("No token file found.")
        return
        
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        video_map = json.load(f)
        
    video_ids = [v["id"] for v in video_map]
    
    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    if creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open(TOKEN_PATH, "w") as token:
                token.write(creds.to_json())
            print("Token refreshed successfully!")
        except Exception as e:
            print(f"Token refresh failed: {e}")
            
    youtube = build('youtube', 'v3', credentials=creds)
    
    # Batch fetch statistics in chunks of 50
    res = youtube.videos().list(
        part='snippet,statistics',
        id=",".join(video_ids[:50])
    ).execute()
    
    results = []
    for item in res.get('items', []):
        vid = item['id']
        title = item['snippet']['title']
        stats = item.get('statistics', {})
        views = int(stats.get('viewCount', 0))
        likes = int(stats.get('likeCount', 0))
        comments = int(stats.get('commentCount', 0))
        results.append({
            'id': vid,
            'title': title,
            'views': views,
            'likes': likes,
            'comments': comments
        })
        
    results.sort(key=lambda x: x['views'], reverse=True)
    
    print("\n--- TOP 10 VIDEOS WITH HIGHEST VIEWS ON CHANNEL ---")
    for idx, r in enumerate(results[:10], 1):
        print(f"{idx}. [{r['views']:,} views] {r['title']} (Likes: {r['likes']:,}, Comments: {r['comments']:,})")

if __name__ == "__main__":
    main()
