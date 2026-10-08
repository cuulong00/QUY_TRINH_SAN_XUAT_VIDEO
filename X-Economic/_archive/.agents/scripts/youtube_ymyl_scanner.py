#!/usr/bin/env python3
"""
YouTube YMYL Channel Scanner & Auditor
Kênh: GocNhinPodcast (@GocNhin_Podcast)
Tác dụng: Tự động kết nối kênh YouTube, bóc tách metadata toàn bộ video,
chấm điểm rủi ro YMYL và xuất báo cáo kiểm toán kèm đoạn text khắc phục.
"""

import urllib.request
import re
import json
import os
import sys
import argparse

# Từ khóa nhạy cảm / giật gân trong tiêu đề
ALARMIST_TITLE_KEYWORDS = [
    'sụp đổ', 'vỡ nợ', 'mất trắng', 'thảm họa', 'bẫy lừa', 
    'khủng hoảng', 'phím mã', 'nhân đôi', 'làm giàu', 'biến cố',
    'bán tháo', 'sụp hầm', 'nguy cơ sụp', 'tiêu tùng', 'cháy tài khoản'
]

# Từ khóa kiểm tra Disclaimer trong Mô tả
DISCLAIMER_KEYWORDS = [
    'tuyên bố miễn trừ', 'không cấu thành lời khuyên', 'không phải lời khuyên đầu tư',
    'mang tính chất phân tích', 'phóng sự tài liệu', 'disclaimer', 'kiến thức kinh tế vĩ mô'
]

# Từ khóa kiểm tra Trích dẫn Nguồn trong Mô tả
CITATION_KEYWORDS = [
    'nguồn tài liệu', 'báo cáo tài chính', 'tham khảo', 'citations', 'nguồn:', 'nguồn tham khảo'
]

# Đoạn Disclaimer chuẩn E-E-A-T & YMYL Safe
STANDARD_DISCLAIMER_BLOCK = """
--------------------------------------------------
ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:
Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và nguồn tin báo chí chính thống. Video mang tính chất phân tích phóng sự tài liệu, kiến thức kinh tế vĩ mô và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.

🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ:
- Biên tập & Nghiên cứu: Ban Biên tập GocNhinPodcast
- Định dạng: Phim tài liệu đồ họa (Editorial Vector Graphic Animation)
- Công nghệ hỗ trợ: Đồ họa và giọng đọc được tối ưu bằng công nghệ AI dưới sự kiểm duyệt và hoàn thiện 100% từ đội ngũ biên tập viên.

📚 NGUỒN TÀI LIỆU THAM KHẢO CHÍNH:
- Báo cáo tài chính đã kiểm toán / Tổng cục Thống kê / World Bank / IMF
- Nghị định / Thông tư / Văn bản quy phạm pháp luật liên quan
--------------------------------------------------
"""

def fetch_channel_videos(handle):
    """Lấy danh sách video từ kênh YouTube bằng handle"""
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
            
            # Tìm danh sách Video ID bằng regex từ ytInitialData
            raw_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
            seen = set()
            unique_ids = []
            for vid in raw_ids:
                if vid not in seen:
                    seen.add(vid)
                    unique_ids.append(vid)
            
            for vid in unique_ids:
                videos.append({
                    'id': vid,
                    'title': '', # Sẽ được bổ sung chi tiết bằng fetch_video_details
                    'url': f"https://www.youtube.com/watch?v={vid}",
                    'published': 'N/A',
                    'views': 'N/A'
                })
    except Exception as e:
        print(f"Error fetching channel videos: {e}")
    
    return videos

def fetch_video_details(video_id):
    """Lấy tiêu đề và mô tả chi tiết của video"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    title = ""
    description = ""
    
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            match = re.search(r'var ytInitialData = (\{.*?\});</script>', html)
            if match:
                data = json.loads(match.group(1))
                primary = data.get('contents', {}).get('twoColumnWatchNextResults', {}).get('results', {}).get('results', {}).get('contents', [])
                for c in primary:
                    vr = c.get('videoPrimaryInfoRenderer', {})
                    if vr and not title:
                        runs = vr.get('title', {}).get('runs', [])
                        if runs:
                            title = runs[0].get('text', '')
                    sec = c.get('videoSecondaryInfoRenderer', {})
                    if sec and not description:
                        attr = sec.get('attributedDescription', {}).get('content', '')
                        if attr:
                            description = attr
                        else:
                            runs = sec.get('description', {}).get('runs', [])
                            description = ''.join([r.get('text', '') for r in runs])
            
            if not title or not description:
                title_m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
                desc_m = re.search(r'<meta property="og:description" content="([^"]+)"', html)
                if title_m and not title:
                    title = title_m.group(1)
                if desc_m and not description:
                    description = desc_m.group(1)
    except Exception as e:
        print(f"Error fetching details for video {video_id}: {e}")
        
    return title, description

def analyze_ymyl_risk(title, description):
    """Phân tích và chấm điểm rủi ro YMYL (0 - 100)"""
    score = 0
    flags = []
    
    title_lower = title.lower()
    desc_lower = description.lower()
    
    # Check 1: Tiêu đề giật gân
    found_alarmist = [kw for kw in ALARMIST_TITLE_KEYWORDS if kw in title_lower]
    if found_alarmist:
        score += 40
        flags.append(f"Tiêu đề chứa từ khóa giật gân/bẫy YMYL: `{', '.join(found_alarmist)}`")
        
    # Check 2: Thiếu Legal Disclaimer trong Mô tả
    has_disclaimer = any(kw in desc_lower for kw in DISCLAIMER_KEYWORDS)
    if not has_disclaimer:
        score += 40
        flags.append("Mô tả thiếu Tuyên bố Miễn trừ Trách nhiệm Tài chính (Legal Disclaimer)")
        
    # Check 3: Thiếu Nguồn trích dẫn (Citations)
    has_citation = any(kw in desc_lower for kw in CITATION_KEYWORDS)
    if not has_citation:
        score += 20
        flags.append("Mô tả thiếu Khung Trích dẫn Nguồn Tham khảo (Citations Block)")
        
    # Xếp loại rủi ro
    if score >= 60:
        risk_level = "🔴 HIGH RISK"
    elif score >= 30:
        risk_level = "🟡 MEDIUM RISK"
    else:
        risk_level = "🟢 SAFE"
        
    return score, risk_level, flags

def generate_remediation_description(existing_description):
    """Tạo đoạn mô tả khắc phục (Giữ nội dung cũ và bổ sung Disclaimer chuẩn)"""
    if "TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM" in existing_description:
        return existing_description
    
    return existing_description.strip() + "\n\n" + STANDARD_DISCLAIMER_BLOCK.strip()

def run_audit(handle="GocNhin_Podcast", output_file="episodes/youtube_ymyl_audit_report.md"):
    print(f"🔍 Bắt đầu kết nối và quét kênh YouTube: @{handle}...")
    videos = fetch_channel_videos(handle)
    
    if not videos:
        print("❌ Không tìm thấy video nào hoặc không kết nối được tới kênh.")
        return
    
    print(f"✅ Đã tìm thấy {len(videos)} video trên kênh. Tiến hành phân tích sâu YMYL...")
    
    audit_results = []
    high_risk_count = 0
    medium_risk_count = 0
    safe_count = 0
    
    for idx, v in enumerate(videos, 1):
        v_title, v_desc = fetch_video_details(v['id'])
        if not v_title:
            v_title = v['title']
            
        score, risk_level, flags = analyze_ymyl_risk(v_title, v_desc)
        
        if risk_level == "🔴 HIGH RISK":
            high_risk_count += 1
        elif risk_level == "🟡 MEDIUM RISK":
            medium_risk_count += 1
        else:
            safe_count += 1
            
        remedied_desc = generate_remediation_description(v_desc)
        
        audit_results.append({
            'index': idx,
            'id': v['id'],
            'title': v_title,
            'url': v['url'],
            'published': v['published'],
            'views': v['views'],
            'description': v_desc,
            'score': score,
            'risk_level': risk_level,
            'flags': flags,
            'remedied_desc': remedied_desc
        })
        print(f"[{idx}/{len(videos)}] {risk_level} (Score: {score}) - {v_title[:45]}...")

    # Sắp xếp theo score giảm dần (High Risk lên đầu)
    audit_results.sort(key=lambda x: x['score'], reverse=True)
    
    # Tạo thư mục đầu ra nếu chưa có
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Tạo báo cáo Markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# 🛡️ Báo Cáo Kiểm Toán Rủi Ro YMYL Kênh YouTube: @{handle}\n\n")
        f.write(f"*Thời gian kiểm toán:* `2026-07-29` | *Kênh:* `https://www.youtube.com/@{handle}`\n\n")
        
        f.write("## 📊 TỔNG QUAN TÌNH TRẠNG KÊNH (EXECUTIVE DASHBOARD)\n\n")
        f.write(f"- **Tổng số video kiểm tra:** `{len(videos)}`\n")
        f.write(f"- 🔴 **Rủi ro cao (HIGH RISK):** `{high_risk_count}` video\n")
        f.write(f"- 🟡 **Rủi ro trung bình (MEDIUM RISK):** `{medium_risk_count}` video\n")
        f.write(f"- 🟢 **An toàn (SAFE):** `{safe_count}` video\n\n")
        
        f.write("---\n\n")
        f.write("## 📋 DANH SÁCH CHI TIẾT & ĐÁNH GIÁ RỦI RO\n\n")
        f.write("| STT | Tiêu Đề Video | Cấp Đồ Rủi Ro | Điểm Số | Các Vấn Đề Phát Hiện | Action Plan |\n")
        f.write("|:---:|:---|:---:|:---:|:---|:---|\n")
        
        for item in audit_results:
            flags_str = "<br>".join([f"• {fl}" for fl in item['flags']]) if item['flags'] else "Không dính cờ"
            action = "Cập nhật Description ngay" if item['score'] >= 30 else "Giữ nguyên"
            title_link = f"[{item['title']}]({item['url']})"
            f.write(f"| {item['index']} | {title_link} | {item['risk_level']} | {item['score']}/100 | {flags_str} | **{action}** |\n")
            
        f.write("\n---\n\n")
        f.write("## 🛠️ ĐOẠN MÃ KHẮC PHỤC MẪU (COPY-PASTE CHO YOUTUBE STUDIO)\n\n")
        f.write("Đối với các video dính cờ 🔴 HIGH RISK hoặc 🟡 MEDIUM RISK, hãy mở YouTube Studio, sửa phần **Mô tả (Description)** bằng cách dán đoạn văn bản đã được bổ sung Disclaimer chuẩn dưới đây:\n\n")
        
        for item in audit_results:
            if item['score'] >= 30:
                f.write(f"### 📹 Video: [{item['title']}]({item['url']})\n")
                f.write(f"- **ID Video:** `{item['id']}`\n")
                f.write(f"- **Mức độ rủi ro:** {item['risk_level']} (Score: {item['score']})\n")
                f.write("```text\n")
                f.write(item['remedied_desc'])
                f.write("\n```\n\n")
                
    print(f"\n🎉 Đã xuất hoàn tất Báo cáo Kiểm toán YMYL tại: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube YMYL Channel Scanner")
    parser.add_argument("--handle", default="GocNhin_Podcast", help="YouTube Channel Handle")
    parser.add_argument("--output", default="episodes/youtube_ymyl_audit_report.md", help="Output Audit Report Markdown File")
    args = parser.parse_args()
    
    run_audit(args.handle, args.output)
