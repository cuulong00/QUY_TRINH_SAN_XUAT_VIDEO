import os
import urllib.request
import xml.etree.ElementTree as ET
import json
import re
import concurrent.futures

CHANNEL_ID = "UCW_pxZ4Fl2JoTiyEab1xxDQ"
MAP_PATH = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/scripts/video_id_map.json"

all_videos = {}

# 1. Load from old video_id_map
if os.path.exists(MAP_PATH):
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        old_list = json.load(f)
        for item in old_list:
            all_videos[item["id"]] = item["title"]

# 2. Load from live RSS feed
rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
req = urllib.request.Request(rss_url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        xml_data = resp.read().decode('utf-8')
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'yt': 'http://www.youtube.com/xml/schemas/2015', 'media': 'http://search.yahoo.com/mrss/'}
    for entry in root.findall('atom:entry', ns):
        vid = entry.find('yt:videoId', ns).text
        title = entry.find('atom:title', ns).text
        all_videos[vid] = title
except Exception as e:
    print(f"RSS Error: {e}")

print(f"Total unique videos found on channel: {len(all_videos)}")

# 3. Fetch exact live views concurrently
def fetch_exact_stats(item):
    vid, title = item
    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    views = 0
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8')
        m = re.search(r'<meta itemprop="interactionCount" content="(\d+)">', html)
        if m:
            views = int(m.group(1))
        else:
            m2 = re.search(r'"viewCount":"(\d+)"', html)
            if m2:
                views = int(m2.group(1))
    except:
        pass
    return {
        "id": vid,
        "title": title,
        "views": views
    }

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    results = list(executor.map(fetch_exact_stats, all_videos.items()))

# Filter out 0 views if private/unlisted or deleted
published_results = [r for r in results if r["views"] > 0]
published_results.sort(key=lambda x: x["views"], reverse=True)

with open("/Users/pro16/Documents/VideoProject/X-Economics/.agents/scripts/live_all_videos_ranked_sep5.json", "w", encoding="utf-8") as f:
    json.dump(published_results, f, ensure_ascii=False, indent=2)

print(f"\n=== BẢNG XẾP HẠNG TOÀN BỘ VIDEO LIVE (CẬP NHẬT 05/09/2026) ===")
for idx, r in enumerate(published_results, 1):
    print(f"{idx:2d}. [{r['views']:,} views] (ID: {r['id']}) {r['title']}")
