import os
import sys
import re

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

VIDEO_ID = "893eBQPh3kE"

MATCHING_CITATIONS = [
    "Toyota Global Newsroom (Thông cáo Lộ trình Pin thể rắn & HEV 2027): https://global.toyota/en/newsroom/corporate/39288520.html",
    "Reuters (Báo cáo doanh số toàn cầu Toyota 11.23 triệu xe & 83% thị trường quốc tế): https://www.reuters.com/business/autos-transportation/toyota-retains-top-spot-global-car-sales-2023-2024-01-30/",
    "Reuters (Báo cáo cơ cấu doanh số xe hybrid PHEV vs BEV của BYD): https://www.reuters.com/business/autos-transportation/chinas-byd-q4-ev-sales-top-tesla-first-time-2024-01-02/",
    "Hong Kong Stock Exchange (Báo cáo kỹ thuật công nghệ DM-i thế hệ 5 - Hiệu suất nhiệt 46.06% mã 1211.HK): https://www.hkex.com.hk"
]

def format_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và báo chí chính thống. Video mang tính phóng sự tài liệu, kiến thức kinh tế vĩ mô; KHÔNG cấu thành lời khuyên đầu tư.\n\n"
        "📚 TỔNG HỢP NGUỒN TÀI LIỆU THAM KHẢO & DỮ LIỆU ĐỔI CHIẾU (EXACT MATCHING SOURCES):\n"
    )
    for c in citations:
        disclaimer += f"• {c}\n"
    disclaimer += "--------------------------------------------------"
    return disclaimer

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    print(f"🔄 Correcting mismatched citations for Video ID {VIDEO_ID} (Toyota vs BYD)...")
    res = youtube.videos().list(part='snippet', id=VIDEO_ID).execute()
    items = res.get('items', [])
    if not items:
        print("❌ Video not found!")
        return
        
    snippet = items[0]['snippet']
    curr_desc = snippet.get('description', '')
    cleaned_desc = re.sub(r'--------------------------------------------------[\s\S]*?--------------------------------------------------', '', curr_desc).strip()
    
    block_6 = format_block_6(MATCHING_CITATIONS)
    new_desc = f"{cleaned_desc}\n\n{block_6}"
    
    if len(new_desc) > 4800:
        max_len = 4800 - len(block_6) - 10
        cleaned_desc = cleaned_desc[:max_len] + "..."
        new_desc = f"{cleaned_desc}\n\n{block_6}"
        
    snippet['description'] = new_desc
    
    youtube.videos().update(
        part='snippet',
        body={'id': VIDEO_ID, 'snippet': snippet}
    ).execute()
    
    print(f"✅ SUCCESS: Fixed description for Video ID {VIDEO_ID} (Length: {len(new_desc)})")

if __name__ == "__main__":
    main()
