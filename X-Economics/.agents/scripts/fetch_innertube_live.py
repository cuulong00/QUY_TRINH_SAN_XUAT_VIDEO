import urllib.request
import json
import re

CHANNEL_ID = "UCW_pxZ4Fl2JoTiyEab1xxDQ"

# We can query InnerTube browse API directly using web client
url = "https://www.youtube.com/youtubei/v1/browse?prettyPrint=false"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

body = {
    "context": {
        "client": {
            "clientName": "WEB",
            "clientVersion": "2.20260902.07.00",
            "hl": "vi",
            "gl": "VN"
        }
    },
    "browseId": CHANNEL_ID,
    "params": "Egl2aWRlb3PyBgQKAjoA" # videos tab
}

req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        
    videos = []
    tabs = res.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [])
    for tab in tabs:
        tab_renderer = tab.get('tabRenderer', {})
        if tab_renderer.get('selected'):
            contents = tab_renderer.get('content', {}).get('richGridRenderer', {}).get('contents', [])
            for c in contents:
                item = c.get('richItemRenderer', {}).get('content', {}).get('videoRenderer', {})
                if item:
                    vid_id = item.get('videoId')
                    title = item.get('title', {}).get('runs', [{}])[0].get('text', '')
                    view_text = item.get('viewCountText', {}).get('simpleText', '')
                    pub = item.get('publishedTimeText', {}).get('simpleText', '')
                    
                    # parse view count number if available
                    views_num = 0
                    m = re.search(r'([\d.,]+)', view_text)
                    if m:
                        num_str = m.group(1).replace('.', '').replace(',', '')
                        views_num = int(num_str) if num_str.isdigit() else 0
                        if 'N' in view_text or 'Tr' in view_text:
                            # if format like 176 N lượt xem
                            pass
                    videos.append({
                        'id': vid_id,
                        'title': title,
                        'view_text': view_text,
                        'views_num': views_num,
                        'published': pub
                    })
                    
    print(f"Total videos fetched live via InnerTube: {len(videos)}")
    # Also fetch exact interactionCount from each video page for precise sorting
    import concurrent.futures
    def get_exact_view(v):
        v_url = f"https://www.youtube.com/watch?v={v['id']}"
        try:
            r = urllib.request.Request(v_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(r, timeout=5) as p:
                html = p.read().decode('utf-8')
            m = re.search(r'<meta itemprop="interactionCount" content="(\d+)">', html)
            if m:
                v['exact_views'] = int(m.group(1))
            else:
                v['exact_views'] = v['views_num']
        except:
            v['exact_views'] = v['views_num']
        return v

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        videos = list(ex.map(get_exact_view, videos))

    videos.sort(key=lambda x: x['exact_views'], reverse=True)
    
    with open("/Users/pro16/Documents/VideoProject/X-Economics/.agents/scripts/live_channel_videos.json", "w", encoding="utf-8") as out:
        json.dump(videos, out, ensure_ascii=False, indent=2)
        
    print("\n=== TOP 15 VIDEO CÓ VIEW CAO NHẤT KÊNH (DỮ LIỆU LIVE 05/09/2026) ===")
    for idx, v in enumerate(videos[:15], 1):
        print(f"{idx}. [{v['exact_views']:,} views] {v['title']} ({v['published']})")

except Exception as e:
    print(f"Error: {e}")
