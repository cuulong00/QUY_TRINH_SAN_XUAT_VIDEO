import os
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def main(video_id):
    token_path = os.path.join(os.path.dirname(__file__), '../tokens/token.json')
    scopes = ['https://www.googleapis.com/auth/youtube.readonly']
    creds_youtube = Credentials.from_authorized_user_file(token_path, scopes)
    
    if creds_youtube.expired and creds_youtube.refresh_token:
        print("Token expired, refreshing...")
        creds_youtube.refresh(Request())
        # Save refreshed token
        with open(token_path, 'w') as f:
            f.write(creds_youtube.to_json())
            
    youtube = build('youtube', 'v3', credentials=creds_youtube)
    
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=50,
            order='relevance'
        )
        response = request.execute()
        
        print(f"SUCCESS: Top comments for video {video_id}:")
        for item in response.get('items', []):
            top_comment = item['snippet']['topLevelComment']['snippet']
            author = top_comment['authorDisplayName']
            text = top_comment['textDisplay']
            like_count = top_comment['likeCount']
            print(f"[{like_count} likes] {author}: {text}")
    except Exception as e:
        print("Error during comment fetching:", e)
        # Try without credentials (using api key if we can find one? No, we don't have api key)
        # Let's try to query with the analytics creds just in case? No, analytics creds are different.

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '6ga9gg8Ei2A')
