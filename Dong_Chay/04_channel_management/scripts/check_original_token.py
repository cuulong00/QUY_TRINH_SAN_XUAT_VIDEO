import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

youtube_scopes = ['https://www.googleapis.com/auth/youtube.readonly']
token_path = '../tokens/token.json'

if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, youtube_scopes)
    youtube = build('youtube', 'v3', credentials=creds)

    res = youtube.channels().list(part='snippet,contentDetails', mine=True).execute()
    for ch in res.get('items', []):
        print(f"📺 Token.json Channel ID: {ch['id']} | Title: '{ch['snippet']['title']}'")
        uploads_playlist = ch['contentDetails']['relatedPlaylists']['uploads']
        items = youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist, maxResults=5).execute()
        print("  Gần đây:")
        for it in items.get('items', []):
            print(f"   - {it['snippet']['title']}")
