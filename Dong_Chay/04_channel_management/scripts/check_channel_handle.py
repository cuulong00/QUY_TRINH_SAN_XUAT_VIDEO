import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

youtube_scopes = ['https://www.googleapis.com/auth/youtube.readonly']
token_path = '../tokens/token.json'

if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, youtube_scopes)
    youtube = build('youtube', 'v3', credentials=creds)

    res = youtube.channels().list(part='snippet', mine=True).execute()
    for ch in res.get('items', []):
        print(f"📺 ID: {ch['id']}")
        print(f"   Title: {ch['snippet']['title']}")
        print(f"   CustomUrl: {ch['snippet'].get('customUrl')}")
