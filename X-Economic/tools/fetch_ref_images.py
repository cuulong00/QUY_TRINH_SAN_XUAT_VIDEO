import json
import os
import re
import sys
import urllib.parse
import urllib.request

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

OUTPUT_DIR = "episodes/sieu-cong-trinh-va-bat-com/ref_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DIRECT_URLS = {
    "le_minh_hung.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0f/L%C3%AA_Minh_H%C6%B0ng_%26_Putin_2026_ASEAN-Russian_Summit_%28cropped%29.jpg",
    "tbt_tolam.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/23/T%C3%B4_L%C3%A2m_20260519_%28cropped%29.jpg",
}

def download_file(url, dest_path):
    print(f"Downloading {url} -> {dest_path}")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        with open(dest_path, "wb") as f:
            f.write(content)
    print(f"Saved {dest_path} ({len(content)} bytes)")

def search_ddg_images(query):
    # Step 1: get vqd token
    url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            m = re.search(r'vqd=([0-9-_]+)', html)
            if not m:
                m = re.search(r'vqd=["\']([0-9-_]+)["\']', html)
            if not m:
                return []
            vqd = m.group(1)
            
            # Step 2: query i.js
            img_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
            req2 = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                data = json.loads(resp2.read().decode("utf-8", errors="ignore"))
                results = [item["image"] for item in data.get("results", []) if "image" in item]
                return results
    except Exception as e:
        print(f"Search error for {query}: {e}")
        return []

SEARCH_QUERIES = {
    "prof_bent_flyvbjerg.jpg": "Bent Flyvbjerg Oxford professor portrait",
    "mtr_ceo_jacobkam.jpg": "Jacob Kam CEO MTR Hong Kong portrait",
    "longthanh_terminal.jpg": "nha ga san bay Long Thanh ket cau thep hoa sen cong truong",
    "cong_cailon_caibe.jpg": "cong thuy loi Cai Lon Cai Be flycam",
    "duongday_500kv_cotthep.jpg": "cot thep duong day 500kV mach 3 lap dung",
}

def main():
    # 1. Download known direct URLs
    for filename, url in DIRECT_URLS.items():
        dest = os.path.join(OUTPUT_DIR, filename)
        try:
            download_file(url, dest)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

    # 2. Search and download remaining
    for filename, query in SEARCH_QUERIES.items():
        dest = os.path.join(OUTPUT_DIR, filename)
        print(f"\nSearching for {filename} with query: '{query}'...")
        urls = search_ddg_images(query)
        if not urls:
            print(f"No results found for {query}")
            continue
        
        downloaded = False
        for img_url in urls[:5]:
            try:
                download_file(img_url, dest)
                downloaded = True
                break
            except Exception as e:
                print(f"Failed to download candidate {img_url}: {e}")
        if not downloaded:
            print(f"Could not download any image for {filename}")

if __name__ == "__main__":
    main()
