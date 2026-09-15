import os
import sys
import re
import json

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")
MAP_PATH = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/scripts/video_id_map.json"

# Categorized Verified Direct Citations
CITATIONS_DB = {
    "VINSPACE": [
        "Tuổi Trẻ Online (Bài báo gốc): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
        "SpaceX Official (Rideshare Program): https://www.spacex.com/rideshare"
    ],
    "VINFAST_FINANCE": [
        "U.S. SEC EDGAR (Báo cáo VinFast 20-F): https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm",
        "Vingroup Official IR (Cam kết 2.5 tỷ USD): https://vingroup.net/en/news/detail/2845/vingroup-and-its-chairman-pledge-usd-25-billion-financial-support-package-to-vinfast",
        "The Investor (Nhà máy pin VinES-Gotion 275 triệu USD): https://theinvestor.vn/vines-gotion-start-work-on-275-mln-battery-plant-d2664.html"
    ],
    "BYD_EV": [
        "Federal Register (Chính phủ Mỹ - Luật 15 CFR Part 791): https://www.federalregister.gov/documents/2024/09/26/2024-21903/securing-the-information-and-communications-technology-and-services-supply-chain-connected-vehicles",
        "European Commission (Quyết định thuế quan xe điện TQ): https://policy.trade.ec.europa.eu/news/commission-imposes-provisional-countervailing-duties-imports-battery-electric-vehicles-bev-china-2024-07-04_en"
    ],
    "MACRO_VN": [
        "Báo Chính Phủ (Nghị quyết 79-NQ/TW Kinh tế nhà nước): https://xaydungchinhsach.chinhphu.vn/giai-phap-dot-pha-cho-kinh-te-nha-nuoc-119250727104607733.htm",
        "World Bank (Báo cáo PDF Già hóa Dân số Việt Nam): https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf"
    ],
    "STEEL_HPG": [
        "Tập đoàn Hòa Phát (Thông cáo Dung Quất 2 HRC): https://hoaphat.com.vn/en/news/hoa-phat-dung-quat-2-completes-installation-of-hrc-rolling-mill.html"
    ]
}

def get_citations_for_title(title):
    t_upper = title.upper()
    if "VINSPACE" in t_upper or "VỆ TINH" in t_upper:
        return CITATIONS_DB["VINSPACE"]
    elif "HÒA PHÁT" in t_upper or "VINMETAL" in t_upper or "THÉP" in t_upper:
        return CITATIONS_DB["STEEL_HPG"]
    elif "BYD" in t_upper or "TOYOTA" in t_upper:
        return CITATIONS_DB["BYD_EV"]
    elif "VINFAST" in t_upper or "VINGROUP" in t_upper or "XANH SM" in t_upper or "VINHOMES" in t_upper or "LPBANK" in t_upper:
        return CITATIONS_DB["VINFAST_FINANCE"]
    else:
        return CITATIONS_DB["MACRO_VN"]

def format_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và nguồn tin báo chí chính thống. Video mang tính chất phân tích phóng sự tài liệu, kiến thức kinh tế vĩ mô và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.\n\n"
        "🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ:\n"
        "- Biên tập & Nghiên cứu: Ban Biên tập GocNhinPodcast\n"
        "- Định dạng: Phim tài liệu đồ họa (Editorial Vector Graphic Animation)\n"
        "- Công nghệ hỗ trợ: Đồ họa và giọng đọc được tối ưu bằng công nghệ AI dưới sự kiểm duyệt và hoàn thiện 100% từ đội ngũ biên tập viên.\n\n"
        "📚 NGUỒN TÀI LIỆU THAM KHẢO CHÍNH (VERIFIED DEEP SOURCES):\n"
    )
    for c in citations:
        disclaimer += f"• {c}\n"
    disclaimer += "--------------------------------------------------"
    return disclaimer

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        video_list = json.load(f)
        
    print(f"🚀 Updating ALL {len(video_list)} videos on channel @GocNhin_Podcast via YouTube API...\n")
    
    success = 0
    for idx, v in enumerate(video_list, 1):
        vid = v['id']
        title = v['title']
        cits = get_citations_for_title(title)
        
        print(f"[{idx}/{len(video_list)}] 🔄 Updating: [{title[:40]}...] (ID: {vid})")
        
        try:
            res = youtube.videos().list(part='snippet', id=vid).execute()
            items = res.get('items', [])
            if not items:
                print(f"  ❌ Video ID {vid} not found.")
                continue
                
            snippet = items[0]['snippet']
            curr_desc = snippet.get('description', '')
            
            # Remove old disclaimer block if present
            cleaned_desc = re.sub(r'--------------------------------------------------[\s\S]*?--------------------------------------------------', '', curr_desc).strip()
            
            block_6 = format_block_6(cits)
            new_desc = f"{cleaned_desc}\n\n{block_6}"
            
            snippet['description'] = new_desc
            
            youtube.videos().update(
                part='snippet',
                body={
                    'id': vid,
                    'snippet': snippet
                }
            ).execute()
            
            print(f"  ✅ SUCCESS: Updated {vid}")
            success += 1
            
        except Exception as e:
            print(f"  ❌ Error updating {vid}: {e}")
            
    print(f"\n🎉 COMPLETED: Successfully updated {success}/{len(video_list)} videos on YouTube!")

if __name__ == "__main__":
    main()
