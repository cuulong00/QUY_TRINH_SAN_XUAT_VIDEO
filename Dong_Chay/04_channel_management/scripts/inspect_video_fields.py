import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
token_file = '../tokens/manager_token.json'

creds = Credentials.from_authorized_user_file(token_file, SCOPES)
youtube = build('youtube', 'v3', credentials=creds)

ch = youtube.channels().list(part='contentDetails', mine=True).execute()['items'][0]
uploads_playlist_id = ch['contentDetails']['relatedPlaylists']['uploads']

items = youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist_id, maxResults=1).execute()['items']
v_id = items[0]['snippet']['resourceId']['videoId']

res = youtube.videos().list(part='snippet,status,contentDetails,recordingDetails,topicDetails', id=v_id).execute()
print(json.dumps(res, indent=2, ensure_ascii=False))
