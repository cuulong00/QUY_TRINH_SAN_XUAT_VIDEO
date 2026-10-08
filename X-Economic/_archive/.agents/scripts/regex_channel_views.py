import urllib.request
import re

url = "https://www.youtube.com/@GocNhin_Podcast/videos"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # Match video titles and view counts directly using regex
    # Pattern for videoRenderer titles and viewCountText
    titles = re.findall(r'"title":{"runs":\[{"text":"(.*?)"}\]', html)
    views = re.findall(r'"viewCountText":{"simpleText":"(.*?)"}', html)
    print(f"Titles found: {len(titles)}")
    print(f"Views found: {len(views)}")
    for t, v in zip(titles[:25], views[:25]):
        print(f"• [{v}] {t}")
except Exception as e:
    print(e)
