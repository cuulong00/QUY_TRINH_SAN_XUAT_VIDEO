import urllib.request
import re
import json

def get_channel_videos():
    url = "https://www.youtube.com/@GocNhin_Podcast/videos"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    })
    
    videos = []
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            match = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
            if match:
                data = json.loads(match.group(1))
                tabs = data.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [])
                for tab in tabs:
                    tab_renderer = tab.get('tabRenderer', {})
                    if tab_renderer.get('title') in ['Videos', 'Video']:
                        items = tab_renderer.get('content', {}).get('richGridRenderer', {}).get('contents', [])
                        for item in items:
                            v_renderer = item.get('richItemRenderer', {}).get('content', {}).get('videoRenderer', {})
                            if v_renderer:
                                vid = v_renderer.get('videoId')
                                title = v_renderer.get('title', {}).get('runs', [{}])[0].get('text', '')
                                videos.append({'id': vid, 'title': title})
    except Exception as e:
        print(f"Error: {e}")
    return videos

videos = get_channel_videos()
print(f"Total videos fetched: {len(videos)}")
for v in videos:
    print(f"ID: {v['id']} | Title: {v['title']}")
