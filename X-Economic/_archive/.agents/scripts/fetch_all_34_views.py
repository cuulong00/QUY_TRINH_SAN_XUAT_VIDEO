import urllib.request
import re
import json
import concurrent.futures

MAP_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/scripts/video_id_map.json"
with open(MAP_PATH, "r", encoding="utf-8") as f:
    videos = json.load(f)

def fetch_view(v):
    vid = v['id']
    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
        m = re.search(r'<meta itemprop="interactionCount" content="(\d+)">', html)
        if m:
            return (int(m.group(1)), v['title'], vid)
        m2 = re.search(r'"viewCount":"(\d+)"', html)
        if m2:
            return (int(m2.group(1)), v['title'], vid)
    except:
        pass
    return (0, v['title'], vid)

print("Fetching views for all 34 videos concurrently...")
results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_view, videos))

results.sort(key=lambda x: x[0], reverse=True)
print("\n=== BẢNG XẾP HẠNG VIEW TOÀN BỘ 34 VIDEO TRÊN KÊNH ===")
for idx, (count, title, vid) in enumerate(results, 1):
    print(f"{idx}. [{count:,} views] (ID: {vid}) {title}")
