import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
token_file = '../tokens/manager_token.json'

creds = Credentials.from_authorized_user_file(token_file, SCOPES)
youtube = build('youtube', 'v3', credentials=creds)

print("--- KIỂM TRA VIDEO CHÍNH XÁC CỦA DÒNG CHẢY ---")
v_res = youtube.videos().list(part='snippet,status', id='LLE9HxjCd6A').execute()
if v_res.get('items'):
    v = v_res['items'][0]
    print(f"📌 Video VinFast (LLE9HxjCd6A): Channel Title = '{v['snippet']['channelTitle']}', Channel ID = '{v['snippet']['channelId']}'")
else:
    print("❌ Không tìm thấy video LLE9HxjCd6A")

print("\n--- DANH SÁCH 16 VIDEO HIỆN TẠI TRÊN TOKEN NÀY ---")
channel = youtube.channels().list(part='contentDetails', mine=True).execute()['items'][0]
uploads_playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']

pl_req = youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist_id, maxResults=50)
pl_resp = pl_req.execute()

for idx, item in enumerate(pl_resp.get('items', [])):
    v_id = item['snippet']['resourceId']['videoId']
    v_title = item['snippet']['title']
    print(f"{idx+1}. [{v_id}] {v_title}")
