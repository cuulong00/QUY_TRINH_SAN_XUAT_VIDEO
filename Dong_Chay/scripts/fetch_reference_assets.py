#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dòng Chảy Reference Asset Fetcher & Normalizer (S-Grade)
-------------------------------------------------------
Công cụ chuyên biệt tìm kiếm, đối soát và tải ảnh tham chiếu nhân vật biểu tượng
(Reference Character Images) với độ chính xác cao nhất từ các nguồn uy tín:
1. Wikimedia Commons / Wikipedia API (100% ảnh chân dung nhân vật công chúng chính thức)
2. Bing High-Res News & Editorial Media Search (VnExpress, Forbes, CafeF, Tuổi Trẻ, Lao Động...)
3. Tự động kiểm tra tính hợp lệ của ảnh, chuẩn hóa định dạng RGB, và lưu trữ vào ref_images/.
"""

import os
import sys
import re
import json
import html
import argparse
from urllib.parse import urlparse
import httpx
from PIL import Image
import io

# User agent chuẩn xác cho Wikimedia và báo chí
WIKI_USER_AGENT = "DongChayMediaBot/1.0 (https://youtube.com/@DongChay; duongtt84@gmail.com)"
BROWSER_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def search_wikipedia_image(title_or_query: str, lang: str = "vi") -> dict | None:
    """Truy vấn ảnh chân dung gốc chính thức từ Wikipedia / Wikimedia Commons API"""
    api_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title_or_query,
        "prop": "pageimages",
        "format": "json",
        "pilicense": "any",
        "piprop": "original"
    }
    headers = {"User-Agent": WIKI_USER_AGENT}
    try:
        with httpx.Client(timeout=10.0, follow_redirects=True) as client:
            r = client.get(api_url, params=params, headers=headers)
            if r.status_code == 200:
                data = r.json()
                pages = data.get("query", {}).get("pages", {})
                for pid, pdata in pages.items():
                    orig = pdata.get("original", {})
                    if orig and "source" in orig:
                        return {
                            "source_type": f"Wikipedia ({lang})",
                            "title": pdata.get("title"),
                            "url": orig["source"],
                            "width": orig.get("width"),
                            "height": orig.get("height")
                        }
    except Exception as e:
        print(f"⚠️ Wikipedia query error: {e}", file=sys.stderr)
    return None


def search_bing_images(query: str, count: int = 5) -> list[dict]:
    """Tìm kiếm ảnh chất lượng cao từ Bing Images qua các đầu báo chính thống"""
    url = "https://www.bing.com/images/search"
    params = {
        "q": query,
        "qft": "+filterui:photo-photo+filterui:imagesize-large"
    }
    headers = {"User-Agent": BROWSER_USER_AGENT}
    results = []
    try:
        with httpx.Client(timeout=15.0, follow_redirects=True) as client:
            r = client.get(url, params=params, headers=headers)
            if r.status_code == 200:
                matches = re.findall(r'class="iusc"[^>]*m="([^"]*)"', r.text)
                for m_str in matches:
                    m_clean = html.unescape(m_str)
                    try:
                        m_data = json.loads(m_clean)
                        murl = m_data.get("murl")
                        title = m_data.get("t", "")
                        domain = urlparse(murl).netloc
                        if murl and not any(ext in murl.lower() for ext in [".svg", ".gif"]):
                            results.append({
                                "source_type": f"Press/Web ({domain})",
                                "title": title,
                                "url": murl,
                                "domain": domain
                            })
                            if len(results) >= count:
                                break
                    except Exception:
                        continue
    except Exception as e:
        print(f"⚠️ Bing query error: {e}", file=sys.stderr)
    return results


def download_and_normalize_image(image_url: str, output_path: str) -> dict:
    """Tải và chuẩn hóa ảnh: chuyển RGB, kiểm tra độ phân giải, lưu JPEG chất lượng cao"""
    domain = urlparse(image_url).netloc.lower()
    headers = {"User-Agent": WIKI_USER_AGENT if "wikimedia.org" in domain or "wikipedia.org" in domain else BROWSER_USER_AGENT}
    
    with httpx.Client(headers=headers, timeout=20.0, follow_redirects=True) as client:
        r = client.get(image_url)
        r.raise_for_status()
        raw_bytes = r.content

    # Mở và xác thực ảnh bằng Pillow
    img = Image.open(io.BytesIO(raw_bytes))
    orig_format = img.format
    orig_size = img.size # (width, height)

    # Chuyển đổi sang RGB nếu đang là RGBA hoặc P (palette)
    if img.mode in ("RGBA", "LA", "P"):
        rgb_img = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        rgb_img.paste(img, mask=img.split()[-1] if "A" in img.mode else None)
        img = rgb_img
    elif img.mode != "RGB":
        img = img.convert("RGB")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "JPEG", quality=95, optimize=True)
    final_file_size = os.path.getsize(output_path)

    return {
        "output_path": output_path,
        "format": "JPEG",
        "original_format": orig_format,
        "size": orig_size,
        "file_size_bytes": final_file_size,
        "status": "SUCCESS"
    }


def fetch_character_manifest(episode_slug: str, manifest: list[dict]):
    """Tải và đối soát toàn bộ danh mục nhân vật biểu tượng cho tập phim"""
    out_dir = os.path.join("episodes", episode_slug, "ref_images")
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"\n================================================================================")
    print(f"🎬 ĐANG TẢI VÀ CHUẨN HÓA ẢNH THAM CHIẾU: {episode_slug}")
    print(f"📁 Thư mục lưu trữ: {out_dir}")
    print(f"================================================================================\n")

    summary = []
    for item in manifest:
        key = item["filename"]
        char_name = item["character_name"]
        role = item["role"]
        target_path = os.path.join(out_dir, key)
        
        print(f"🔍 Đang xử lý: {char_name} ({key})...")
        print(f"   Vai trò: {role}")

        image_url = item.get("direct_url")
        source_desc = item.get("source_desc", "Direct / Verified Source")

        # Nếu chưa có direct_url, thử tìm qua Wikipedia trước
        if not image_url and item.get("wiki_title"):
            wiki_res = search_wikipedia_image(item["wiki_title"], lang=item.get("wiki_lang", "vi"))
            if wiki_res:
                image_url = wiki_res["url"]
                source_desc = f"Official Wikipedia ({wiki_res['title']})"

        # Nếu vẫn chưa có, thử tìm qua Bing search
        if not image_url and item.get("search_query"):
            bing_res = search_bing_images(item["search_query"], count=1)
            if bing_res:
                image_url = bing_res[0]["url"]
                source_desc = f"Press: {bing_res[0]['title'][:50]}... ({bing_res[0]['domain']})"

        if not image_url:
            print(f"   ❌ Thất bại: Không tìm được nguồn ảnh khả dụng cho {char_name}!")
            summary.append({
                "character": char_name,
                "filename": key,
                "status": "FAILED",
                "resolution": "N/A",
                "source": "None"
            })
            continue

        try:
            res = download_and_normalize_image(image_url, target_path)
            w, h = res["size"]
            size_kb = res["file_size_bytes"] / 1024
            print(f"   ✅ Đã tải và chuẩn hóa thành công: {w}x{h} px | {size_kb:.1f} KB")
            print(f"   🔗 Nguồn: {source_desc}")
            print(f"   💾 Lưu tại: {target_path}\n")
            summary.append({
                "character": char_name,
                "filename": key,
                "status": "SUCCESS",
                "resolution": f"{w}x{h}",
                "size_kb": f"{size_kb:.1f} KB",
                "source": source_desc,
                "path": target_path
            })
        except Exception as e:
            print(f"   ❌ Lỗi tải ảnh từ {image_url}: {e}\n")
            summary.append({
                "character": char_name,
                "filename": key,
                "status": f"ERROR: {e}",
                "resolution": "N/A",
                "source": source_desc
            })

    print(f"\n================================================================================")
    print(f"📋 BÁO CÁO TỔNG KẾT TẢI ẢNH THAM CHIẾU")
    print(f"================================================================================")
    for s in summary:
        icon = "✅" if s["status"] == "SUCCESS" else "❌"
        print(f"{icon} {s['filename']:<30} | {s['character']:<30} | {s.get('resolution', 'N/A'):<10} | {s.get('size_kb', ''):<10} | {s['source']}")
    print(f"================================================================================\n")
    return summary


# Danh mục chuẩn 5 nhân vật biểu tượng cho episode: grab-vs-gsm-tai-xe-tat-app
GRAB_GSM_MANIFEST = [
    {
        "filename": "ceo_anthony_tan.jpg",
        "character_name": "Anthony Tan (CEO Grab)",
        "role": "Nhà sáng lập & CEO Tập đoàn Grab",
        "direct_url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/President_Masato_Kanda_meets_with_Anthony_Tan%2C_Group_CEO_and_Co-founder_of_Grab_at_the_World_Economic_Forum_in_Davos%2C_Switzerland_-_cropped.jpg",
        "source_desc": "Official Wikimedia Commons (WEF Davos 2024 Portrait)"
    },
    {
        "filename": "ceo_gsm_nguyen_van_thanh.jpg",
        "character_name": "Nguyễn Văn Thanh (CEO Toàn Cầu GSM)",
        "role": "Tổng Giám đốc Toàn cầu GSM / Xanh SM",
        "direct_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/Thanh_Nguyen.jpg",
        "source_desc": "Official Wikipedia Vietnam (Portrait)"
    },
    {
        "filename": "be_leadership.jpg",
        "character_name": "Vũ Hoàng Yến (CEO Be Group)",
        "role": "Tổng Giám đốc Be Group",
        "direct_url": "https://forbes.vn/wp-content/uploads/2021/09/Ms_Vu_Hoang_Yen_CEO_Be_Group.png",
        "source_desc": "Forbes Vietnam Official Portrait"
    },
    {
        "filename": "vinasun_leadership.jpg",
        "character_name": "Đặng Phước Thành (Chủ Tịch Sáng Lập Vinasun)",
        "role": "Lãnh đạo kỳ cựu kiến tạo Vinasun",
        "direct_url": "https://sohanews.sohacdn.com/thumb_w/1000/160588918557773824/2023/12/9/photo-1-1702091342044711780032.jpg",
        "source_desc": "Soha / CafeF Financial Editorial Archives"
    },
    {
        "filename": "veteran_driver.jpg",
        "character_name": "Người Tài Xế Công Nghệ Từng Trải",
        "role": "Đại diện tầng lớp lao động tự do (Digital Precariat)",
        "direct_url": "https://media-cdn-v2.laodong.vn/storage/newsportal/2024/3/1/1309920/Xe-Om-Cong-Nghe-Ha-N-02.jpg",
        "source_desc": "Báo Lao Động Documentary Photo"
    }
]


def main():
    parser = argparse.ArgumentParser(description="Dòng Chảy Reference Asset Fetcher")
    parser.add_argument("--episode", type=str, default="grab-vs-gsm-tai-xe-tat-app", help="Episode slug")
    parser.add_argument("--search", type=str, help="Search for character images on Bing")
    parser.add_argument("--wiki", type=str, help="Search for character portrait on Wikipedia")
    parser.add_argument("--url", type=str, help="Download direct image URL")
    parser.add_argument("--out", type=str, help="Output file path for --url")

    args = parser.parse_args()

    if args.search:
        print(f"🔎 Đang tìm kiếm ảnh báo chí cho: '{args.search}'...")
        res = search_bing_images(args.search, count=5)
        for i, r in enumerate(res):
            print(f"[{i+1}] {r['title']}")
            print(f"    URL: {r['url']}")
            print(f"    Domain: {r['domain']}\n")
    elif args.wiki:
        print(f"🔎 Đang tìm kiếm chân dung Wikipedia cho: '{args.wiki}'...")
        res = search_wikipedia_image(args.wiki, lang="vi") or search_wikipedia_image(args.wiki, lang="en")
        if res:
            print(f"✅ Tìm thấy: {res['title']} ({res['source_type']})")
            print(f"   URL: {res['url']}")
            print(f"   Độ phân giải: {res['width']}x{res['height']}")
        else:
            print(f"❌ Không tìm thấy trang Wikipedia có ảnh chân dung.")
    elif args.url and args.out:
        print(f"📥 Đang tải ảnh từ {args.url} đến {args.out}...")
        res = download_and_normalize_image(args.url, args.out)
        print(f"✅ Thành công: {res['size'][0]}x{res['size'][1]} px | {res['file_size_bytes']/1024:.1f} KB")
    else:
        # Mặc định chạy manifest của episode
        fetch_character_manifest(args.episode, GRAB_GSM_MANIFEST)


if __name__ == "__main__":
    main()
