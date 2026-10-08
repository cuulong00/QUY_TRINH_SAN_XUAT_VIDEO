import urllib.request
import re
import json

url = "https://www.youtube.com/@GocNhin_Podcast/videos"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # Extract ytInitialData
    match = re.search(r'var ytInitialData = ({.*?});</script>', html)
    if match:
        data = json.loads(match.group(1))
        # Navigate through tabs to find video items
        tabs = data.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [])
        videos = []
        for tab in tabs:
            tab_renderer = tab.get('tabRenderer', {})
            if tab_renderer.get('title') in ['Video', 'Videos']:
                contents = tab_renderer.get('content', {}).get('richGridRenderer', {}).get('contents', [])
                for c in contents:
                    item = c.get('richItemRenderer', {}).get('content', {}).get('videoRenderer', {})
                    if item:
                        title = item.get('title', {}).get('runs', [{}])[0].get('text', '')
                        view_text = item.get('viewCountText', {}).get('simpleText', '')
                        published = item.get('publishedTimeText', {}).get('simpleText', '')
                        vid_id = item.get('videoId', '')
                        videos.append({
                            'id': vid_id,
                            'title': title,
                            'views': view_text,
                            'published': published
                        })
        print(f"Found {len(videos)} videos on channel page:")
        for v in videos[:20]:
            print(f"• [{v['views']}] {v['title']} ({v['published']})")
    else:
        print("ytInitialData not found in HTML.")
except Exception as e:
    print(f"Error: {e}")
