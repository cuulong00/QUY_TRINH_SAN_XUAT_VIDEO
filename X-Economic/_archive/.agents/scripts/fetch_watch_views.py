import urllib.request
import re
import json

MAP_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/scripts/video_id_map.json"
with open(MAP_PATH, "r", encoding="utf-8") as f:
    videos = json.load(f)

print(f"Checking view counts for sample videos...")
headers = {"User-Agent": "Mozilla/5.0"}

results = []
for v in videos[:12]:
    vid = v['id']
    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
        m = re.search(r'<meta itemprop="interactionCount" content="(\d+)">', html)
        if m:
            count = int(m.group(1))
            results.append((count, v['title']))
        else:
            m2 = re.search(r'"viewCount":"(\d+)"', html)
            if m2:
                count = int(m2.group(1))
                results.append((count, v['title']))
    except Exception as e:
        pass

results.sort(key=lambda x: x[0], reverse=True)
for count, title in results:
    print(f"• [{count:,} views] {title}")
