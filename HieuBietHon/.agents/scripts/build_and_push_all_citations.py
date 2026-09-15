import os
import sys
import re
import json

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

# Verified citations map with REAL video IDs and REAL direct URLs
FULL_STAGING_DATA = [
    {
        "id": "gUQAk_R3wgs",
        "title": "VinSpace Tự Chủ Được Những Gì? Giải Phẫu Chi Tiết",
        "citations": [
            "Tuổi Trẻ Online (Bài báo gốc): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
            "SpaceX Official (Rideshare Program): https://www.spacex.com/rideshare"
        ]
    },
    {
        "id": "pOpv3INMYGM",
        "title": "Vì Sao VinSpace Phải Vội Vàng Phóng Vệ Tinh?",
        "citations": [
            "Tuổi Trẻ Online (Bài báo gốc): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
            "SpaceX Official: https://www.spacex.com/rideshare"
        ]
    },
    {
        "id": "DbrT-7btyyg",
        "title": "\"Sếu Đầu Đàn\" Đang Được Nuôi Dưỡng Thế Nào?",
        "citations": [
            "Báo Chính Phủ (Toàn văn bài phân tích Nghị quyết 79-NQ/TW): https://xaydungchinhsach.chinhphu.vn/giai-phap-dot-pha-cho-kinh-te-nha-nuoc-119250727104607733.htm",
            "Báo Chính Phủ (Bài phân tích vai trò chủ đạo): https://xaydungchinhsach.chinhphu.vn/nhan-thuc-ve-vai-tro-chu-dao-cua-kinh-te-nha-nuoc-119250727105052903.htm"
        ]
    },
    {
        "id": "3L8W6DT6Fhc",
        "title": "BYD Phá Giá Và Chiến Lược Của Vinfast",
        "citations": [
            "Federal Register (Chính phủ Mỹ - Văn bản Luật 15 CFR Part 791): https://www.federalregister.gov/documents/2024/09/26/2024-21903/securing-the-information-and-communications-technology-and-services-supply-chain-connected-vehicles",
            "European Commission (Quyết định thuế quan xe điện TQ): https://policy.trade.ec.europa.eu/news/commission-imposes-provisional-countervailing-duties-imports-battery-electric-vehicles-bev-china-2024-07-04_en"
        ]
    },
    {
        "id": "QBsQ7xFvmP4",
        "title": "Có Kịp Hóa Rồng Không?",
        "citations": [
            "World Bank (Báo cáo PDF Già hóa Dân số Việt Nam): https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf"
        ]
    },
    {
        "id": "6nBCWNke_dg",
        "title": "Phép Thuật Tài Chính Hay Sóng Gió Đã Qua?",
        "citations": [
            "U.S. SEC EDGAR (Báo cáo VinFast 20-F): https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm"
        ]
    },
    {
        "id": "TWsTsRQT8OM",
        "title": "Nội Địa Hóa 80% Và Sắp Có Lãi Trên Toàn Cầu",
        "citations": [
            "The Investor (Nhà máy pin VinES-Gotion 275 triệu USD): https://theinvestor.vn/vines-gotion-start-work-on-275-mln-battery-plant-d2664.html"
        ]
    },
    {
        "id": "L7oucqEzuWM",
        "title": "Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc?",
        "citations": [
            "Vingroup Official IR (Cam kết 2.5 tỷ USD): https://vingroup.net/en/news/detail/2845/vingroup-and-its-chairman-pledge-usd-25-billion-financial-support-package-to-vinfast"
        ]
    },
    {
        "id": "q3PBqQ1EFL8",
        "title": "Hòa Phát VS VinMetal: Ai Sẽ Là Vua Thép",
        "citations": [
            "Tập đoàn Hòa Phát (Thông cáo Dung Quất 2 HRC): https://hoaphat.com.vn/en/news/hoa-phat-dung-quat-2-completes-installation-of-hrc-rolling-mill.html"
        ]
    }
]

def format_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh HieuBietHon được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và nguồn tin báo chí chính thống. Video mang tính chất phân tích phóng sự tài liệu, kiến thức kinh tế vĩ mô và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.\n\n"
        "🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ:\n"
        "- Biên tập & Nghiên cứu: Ban Biên tập HieuBietHon\n"
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
    
    print(f"🚀 Prepared {len(FULL_STAGING_DATA)} verified video descriptions for YouTube update...\n")
    
    updated = 0
    for v in FULL_STAGING_DATA:
        vid = v['id']
        title = v['title']
        cits = v['citations']
        print(f"🔄 Updating YouTube Video: [{title}] (ID: {vid})...")
        
        try:
            res = youtube.videos().list(part='snippet', id=vid).execute()
            items = res.get('items', [])
            if not items:
                print(f"  ❌ Video ID {vid} not found.")
                continue
                
            snippet = items[0]['snippet']
            curr_desc = snippet.get('description', '')
            
            # Remove any existing disclaimer block to avoid duplication
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
            
            print(f"  ✅ SUCCESS: Updated description for Video ID {vid}")
            updated += 1
            
        except Exception as e:
            print(f"  ❌ Failed to update {vid}: {e}")
            
    print(f"\n🎉 ALL DONE: Successfully updated {updated}/{len(FULL_STAGING_DATA)} video descriptions on YouTube!")

if __name__ == "__main__":
    main()
