import os
import re
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def parse_iso8601_duration(duration_str):
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', duration_str)
    if not match:
        return 0
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds

def main():
    try:
        youtube_scopes = ['https://www.googleapis.com/auth/youtube.readonly']
        analytics_scopes = ['https://www.googleapis.com/auth/yt-analytics.readonly']
        
        token_path = os.path.join(os.path.dirname(__file__), '../tokens/token.json')
        analytics_token_path = os.path.join(os.path.dirname(__file__), '../tokens/analytics_token.json')
        
        creds_youtube = Credentials.from_authorized_user_file(token_path, youtube_scopes)
        creds_analytics = Credentials.from_authorized_user_file(analytics_token_path, analytics_scopes)
        
        youtube = build('youtube', 'v3', credentials=creds_youtube)
        youtubeAnalytics = build('youtubeAnalytics', 'v2', credentials=creds_analytics)

        request = youtube.channels().list(part='contentDetails,statistics', mine=True)
        response = request.execute()
        
        channel_stats = response['items'][0]['statistics']
        total_videos = int(channel_stats.get('videoCount', 0))
        print(f"Total videos on channel: {total_videos}")
        
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Fetch up to 50 videos
        playlist_request = youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist_id, maxResults=50)
        playlist_response = playlist_request.execute()

        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d') # 1 year back

        video_reports = []

        for idx, item in enumerate(playlist_response.get('items', [])):
            video_id = item['snippet']['resourceId']['videoId']

            video_request = youtube.videos().list(part='snippet,statistics,contentDetails', id=video_id)
            video_response = video_request.execute()
            
            if not video_response.get('items'):
                continue
                
            video_item = video_response['items'][0]
            title = video_item['snippet']['title']
            published_at = video_item['snippet']['publishedAt']
            views = int(video_item['statistics'].get('viewCount', 0))
            likes = int(video_item['statistics'].get('likeCount', 0))
            comments = int(video_item['statistics'].get('commentCount', 0))
            duration_iso = video_item['contentDetails']['duration']
            duration_sec = parse_iso8601_duration(duration_iso)

            # Query AVD from analytics
            request_analytics = youtubeAnalytics.reports().query(
                startDate=start_date,
                endDate=end_date,
                ids='channel==MINE',
                filters=f'video=={video_id}',
                metrics='averageViewDuration'
            )
            analytics_response = request_analytics.execute()

            avd_seconds = 0.0
            avd_text = "N/A"
            retention_text = "N/A"
            retention_pct = 0.0
            
            if 'rows' in analytics_response and len(analytics_response['rows']) > 0 and analytics_response['rows'][0] is not None:
                avd_seconds = float(analytics_response['rows'][0][0])
                if avd_seconds > 0:
                    avd_min = int(avd_seconds // 60)
                    avd_sec = int(avd_seconds % 60)
                    retention_pct = (avd_seconds / duration_sec) * 100 if duration_sec > 0 else 0
                    avd_text = f"{avd_min}m {avd_sec}s"
                    retention_text = f"{retention_pct:.1f}%"
            
            dur_min = int(duration_sec // 60)
            dur_sec = int(duration_sec % 60)
            duration_formatted = f"{dur_min}m {dur_sec}s"
            
            video_reports.append({
                'index': idx + 1,
                'title': title,
                'id': video_id,
                'published_at': published_at[:10],
                'views': views,
                'likes': likes,
                'comments': comments,
                'duration': duration_formatted,
                'duration_sec': duration_sec,
                'avd': avd_text,
                'avd_sec': avd_seconds,
                'retention': retention_text,
                'retention_pct': retention_pct,
                'is_short': duration_sec < 60
            })
            print(f"Processed: {title} ({duration_formatted}) -> Views: {views}, Retention: {retention_text}")

        # Write to md
        report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../all_video_health_report.md'))
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Toàn bộ chỉ số các video trên kênh Dòng Chảy (Tối đa 50 video gần nhất)\n\n")
            f.write("| STT | Tên Video | Phân Loại | Lượt Xem | Like | Comment | Độ Dài | AVD | Giữ Chân |\n")
            f.write("|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n")
            for r in video_reports:
                category = "Shorts" if r['is_short'] else "Long-form"
                clean_title = r['title'].replace('|', '\\|')
                f.write(f"| {r['index']} | [{clean_title}](https://youtu.be/{r['id']}) | {category} | {r['views']:,} | {r['likes']:,} | {r['comments']:,} | {r['duration']} | {r['avd']} | {r['retention']} |\n")
        print(f"Report written to {report_path}")

    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
