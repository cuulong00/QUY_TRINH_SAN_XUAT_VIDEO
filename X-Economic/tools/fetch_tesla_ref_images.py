import json
import os
import re
import urllib.parse
import urllib.request

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

OUTPUT_DIR = "/Users/pro16/Documents/VideoProject/X-Economic/episodes/tesla-vao-viet-nam/ref_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DIRECT_URLS = {
    "elon_musk.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/99/Elon_Musk_Colorado_2022_%28cropped2%29.jpg",
    "pham_nhat_vuong.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pham_Nhat_Vuong_2020.jpg/800px-Pham_Nhat_Vuong_2020.jpg",
}

SEARCH_QUERIES = {
    "david_feinstein.jpg": "David Jon Feinstein Tesla",
    "isabel_fan.jpg": "Isabel Fan Tesla regional director",
    "tesla_model_3_2026.jpg": "Tesla Model 3 Highland white exterior",
    "tesla_model_y.jpg": "Tesla Model Y electric SUV exterior",
    "vgreen_charging_station.jpg": "tram sac v-green vinfast cao toc",
    "tesla_megapack_bess.jpg": "Tesla Megapack BESS battery energy storage substation",
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
            
            img_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
            req2 = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                data = json.loads(resp2.read().decode("utf-8", errors="ignore"))
                results = [item["image"] for item in data.get("results", []) if "image" in item]
                return results
    except Exception as e:
        print(f"Search error for {query}: {e}")
        return []

def main():
    # 1. Download known direct URLs
    for filename, url in DIRECT_URLS.items():
        dest = os.path.join(OUTPUT_DIR, filename)
        try:
            download_file(url, dest)
        except Exception as e:
            print(f"Failed direct download for {filename}: {e}")
            # Add to search queries if direct fails
            if filename == "pham_nhat_vuong.jpg":
                SEARCH_QUERIES["pham_nhat_vuong.jpg"] = "Pham Nhat Vuong Vingroup portrait"
            elif filename == "elon_musk.jpg":
                SEARCH_QUERIES["elon_musk.jpg"] = "Elon Musk portrait suit"

    # 2. Search and download remaining
    for filename, query in SEARCH_QUERIES.items():
        dest = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(dest) and os.path.getsize(dest) > 10000:
            print(f"File {filename} already exists ({os.path.getsize(dest)} bytes), skipping.")
            continue

        print(f"\nSearching for {filename} with query: '{query}'...")
        urls = search_ddg_images(query)
        if not urls:
            print(f"No results found for {query}")
            continue
        
        downloaded = False
        for img_url in urls[:8]:
            try:
                download_file(img_url, dest)
                if os.path.exists(dest) and os.path.getsize(dest) > 5000:
                    downloaded = True
                    break
            except Exception as e:
                print(f"Failed to download candidate {img_url}: {e}")
        if not downloaded:
            print(f"Could not download any valid image for {filename}")

if __name__ == "__main__":
    main()
