import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
token_file = '../tokens/manager_token.json'

if not os.path.exists(token_file):
    print("❌ Không tìm thấy manager_token.json")
    exit(1)

creds = Credentials.from_authorized_user_file(token_file, SCOPES)
youtube = build('youtube', 'v3', credentials=creds)

ch = youtube.channels().list(part='contentDetails,snippet', mine=True).execute()['items'][0]
ch_title = ch['snippet']['title']
uploads_playlist_id = ch['contentDetails']['relatedPlaylists']['uploads']

print(f"🚀 TIẾN HÀNH CẬP NHẬT 'containsSyntheticMedia = True' CHO KÊNH: '{ch_title}'")
print("="*60)

video_list = []
next_page_token = None

while True:
    pl_req = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )
    pl_resp = pl_req.execute()
    for item in pl_resp.get('items', []):
        video_list.append({
            'id': item['snippet']['resourceId']['videoId'],
            'title': item['snippet']['title']
        })
    next_page_token = pl_resp.get('nextPageToken')
    if not next_page_token:
        break

print(f"📋 Tìm thấy {len(video_list)} video cần cập nhật thuộc tính containsSyntheticMedia = True...\n")

success_count = 0

for idx, v in enumerate(video_list):
    video_id = v['id']
    title = v['title']
    
    # Read current status
    v_res = youtube.videos().list(part='status', id=video_id).execute()
    if not v_res.get('items'):
        continue
        
    status = v_res['items'][0]['status']
    status['containsSyntheticMedia'] = True
    
    body = {
        'id': video_id,
        'status': status
    }
    
    try:
        up_res = youtube.videos().update(part='status', body=body).execute()
        print(f"✅ [{idx+1}/{len(video_list)}] Cập nhật thành công 'containsSyntheticMedia = True' cho: {title}")
        success_count += 1
    except Exception as e:
        print(f"❌ [{idx+1}/{len(video_list)}] Lỗi khi cập nhật {title}: {e}")

print("\n" + "="*60)
print(f"🎉 KẾT QUẢ CẬP NHẬT THUỘC TÍNH AI (containsSyntheticMedia = True):")
print(f"  - Thành công: {success_count}/{len(video_list)} video")
print("="*60)
