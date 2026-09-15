import urllib.request
import re
import json

def fetch_channel_videos(handle):
    clean_handle = handle.replace('@', '')
    url = f"https://www.youtube.com/@{clean_handle}/videos"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
    })
    
    videos = []
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            raw_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
            
            # also look in shorts if needed, but the user said "videos"
            seen = set()
            unique_ids = []
            for vid in raw_ids:
                if vid not in seen:
                    seen.add(vid)
                    unique_ids.append(vid)
            
            for vid in unique_ids:
                videos.append({
                    'id': vid,
                    'url': f"https://www.youtube.com/watch?v={vid}"
                })
    except Exception as e:
        print(f"Error fetching channel videos: {e}")
    
    return videos

def fetch_video_details(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    title = ""
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            title_m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
            if title_m:
                title = title_m.group(1)
    except Exception:
        pass
    return title

def main():
    print("Fetching videos...")
    videos = fetch_channel_videos("GocNhin_Podcast")
    results = []
    for idx, v in enumerate(videos, 1):
        title = fetch_video_details(v['id'])
        v['title'] = title
        results.append(v)
        print(f"{idx}. {title}")
    
    output_path = "/Users/pro16/.gemini/antigravity/brain/a2f192c2-5fac-4bd4-b831-6ee2ba87e45b/scratch/scanned_videos.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Done. Saved to {output_path}")

if __name__ == "__main__":
    main()
