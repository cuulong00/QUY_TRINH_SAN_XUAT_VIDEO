import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

youtube_scopes = ['https://www.googleapis.com/auth/youtube.readonly']
token_path = '../tokens/token.json'

creds = Credentials.from_authorized_user_file(token_path, youtube_scopes)
youtube = build('youtube', 'v3', credentials=creds)

res = youtube.channels().list(part='snippet,statistics', forHandle='dong-chay-kinh-te-chinh-tri').execute()
print("Search for @dong-chay-kinh-te-chinh-tri:")
for ch in res.get('items', []):
    print(f"📺 Channel ID: {ch['id']}")
    print(f"   Title: {ch['snippet']['title']}")
    print(f"   CustomUrl: {ch['snippet'].get('customUrl')}")
    print(f"   Subscribers: {ch['statistics'].get('subscriberCount')}")
    print(f"   Videos: {ch['statistics'].get('videoCount')}")
