#!/usr/bin/env python3
"""
Reference Asset Ingestion Engine for X-Economics.
Automatically searches, fetches, and normalizes high-resolution reference portraits
for historical figures, politicians, and leaders using the Wikimedia Commons & Wikipedia APIs.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image

HEADERS = {
    'User-Agent': 'XEconomicsBot/1.0 (contact@xeconomics.com; educational documentary research)'
}

def search_wikipedia_pageimage(title):
    """Fetch lead official image from Wikipedia PageImages API."""
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&pithumbsize=1600&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                thumb = p.get('thumbnail', {})
                if thumb.get('source'):
                    return thumb.get('source')
    except Exception as e:
        print(f"[-] Wikipedia PageImages lookup failed for {title}: {e}")
    return None

def search_wikimedia_commons(query, limit=5):
    """Search Wikimedia Commons API for high-resolution images."""
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit={limit}&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    candidates = []
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                info = p.get('imageinfo', [{}])[0]
                mime = info.get('mime', '')
                if mime in ['image/jpeg', 'image/png']:
                    width = info.get('width', 0)
                    height = info.get('height', 0)
                    img_url = info.get('url')
                    if img_url:
                        candidates.append((width * height, width, height, img_url, p.get('title')))
    except Exception as e:
        print(f"[-] Wikimedia Commons search failed for {query}: {e}")
    
    # Sort by total pixel resolution descending
    candidates.sort(key=lambda x: x[0], reverse=True)
    if candidates:
        return candidates[0][3]
    return None

def download_and_verify(image_url, target_path):
    """Download image, verify format/dimensions with PIL, and save."""
    os.makedirs(os.path.dirname(os.path.abspath(target_path)), exist_ok=True)
    req = urllib.request.Request(image_url, headers=HEADERS)
    temp_path = target_path + ".tmp"
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            with open(temp_path, 'wb') as f:
                f.write(resp.read())
        
        with Image.open(temp_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(target_path, 'JPEG', quality=95)
            print(f"[+] Successfully saved {target_path} ({img.size[0]}x{img.size[1]} px, {img.format})")
        
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return True
    except Exception as e:
        print(f"[-] Failed to download or process {image_url}: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

def fetch_asset(entity_name, filename, target_dir):
    """Combined smart fetcher."""
    target_path = os.path.join(target_dir, filename)
    print(f"\n[*] Searching for reference asset: '{entity_name}' -> '{filename}'")
    
    # 1. Try Wikipedia lead image first
    img_url = search_wikipedia_pageimage(entity_name)
    if img_url:
        print(f"  -> Found Wikipedia Lead Portrait: {img_url}")
        if download_and_verify(img_url, target_path):
            return True
            
    # 2. Try Wikimedia Commons search
    img_url = search_wikimedia_commons(entity_name)
    if img_url:
        print(f"  -> Found Wikimedia Commons Asset: {img_url}")
        if download_and_verify(img_url, target_path):
            return True
            
    print(f"[-] Could not automatically download {filename} for {entity_name}")
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_reference_images.py <episode_dir>")
        sys.exit(1)
        
    ep_dir = sys.argv[1]
    ref_dir = os.path.join(ep_dir, "ref_images")
    os.makedirs(ref_dir, exist_ok=True)
    
    # Example manifest for the current episode
    manifest = [
        ("Henry Kissinger", "@henry_kissinger_1974.jpg"),
        ("Faisal of Saudi Arabia", "@king_faisal_1974.jpg"),
        ("William E. Simon", "@william_simon_1974.jpg"),
        ("Robert Triffin", "@robert_triffin_1960.jpg"),
        ("Brad Cooper (admiral)", "@us_navy_admiral.jpg"),
    ]
    
    print(f"=== Reference Asset Ingestion Engine ===")
    print(f"Target Directory: {ref_dir}")
    
    for entity, fname in manifest:
        fetch_asset(entity, fname, ref_dir)
        
    print("\n[✓] Asset Ingestion Task Finished.")
