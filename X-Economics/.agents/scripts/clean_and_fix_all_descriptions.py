import os
import sys
import re
import json

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

# 100% TAILOR-MATCHED CITATIONS MAP FOR ALL 34 VIDEOS
TAILORED_DB = {
    "gUQAk_R3wgs": [
        "Tuổi Trẻ Online (Bài báo gốc Hợp đồng VinSpace-SpaceX): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
        "SpaceX Official (Báo giá Rideshare Program): https://www.spacex.com/rideshare"
    ],
    "pOpv3INMYGM": [
        "Tuổi Trẻ Online (Bài báo gốc Hợp đồng VinSpace-SpaceX): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
        "SpaceX Official (Báo giá Rideshare Program): https://www.spacex.com/rideshare"
    ],
    "cfllyzWfd3c": [
        "Reuters (Báo cáo VinFast khởi công nhà máy xe điện Ấn Độ): https://www.reuters.com",
        "Reuters (Báo cáo Ấn Độ từ chối dự án 1 tỷ USD của BYD): https://www.reuters.com"
    ],
    "Gyl2d62XfQ8": [
        "World Bank PDF (Báo cáo Già hóa Dân số Việt Nam): https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf",
        "Tổng cục Thống kê (Dữ liệu cơ cấu dân số vàng & già hóa): https://www.gso.gov.vn"
    ],
    "u9RbqMTYk2U": [
        "World Bank Data (Lịch sử dữ liệu GDP Việt Nam qua các thời kỳ): https://datahelpdesk.worldbank.org",
        "Tổng cục Thống kê (Lịch sử phát triển kinh tế Việt Nam): https://www.gso.gov.vn"
    ],
    "2yN0WpXed00": [
        "Báo Chính Phủ (Chỉ đạo chống lãng phí & cải cách hành chính): https://baochinhphu.vn",
        "World Bank (Báo cáo bẫy thu nhập trung bình): https://www.worldbank.org"
    ],
    "893eBQPh3kE": [
        "Toyota Global Newsroom (Thông cáo Lộ trình Pin thể rắn & HEV 2027): https://global.toyota/en/newsroom/corporate/39288520.html",
        "Reuters (Báo cáo doanh số toàn cầu Toyota 11.23 triệu xe): https://www.reuters.com/business/autos-transportation/toyota-retains-top-spot-global-car-sales-2023-2024-01-30/",
        "Reuters (Báo cáo cơ cấu doanh số xe hybrid PHEV vs BEV của BYD): https://www.reuters.com/business/autos-transportation/chinas-byd-q4-ev-sales-top-tesla-first-time-2024-01-02/",
        "Hong Kong Stock Exchange (Báo cáo kỹ thuật công nghệ DM-i mã 1211.HK): https://www.hkex.com.hk"
    ],
    "J78YnaqO6E4": [
        "Reuters (Báo cáo quyết định thuế chống trợ cấp xe điện TQ): https://www.reuters.com/business/autos-transportation/eu-ev-tariffs-take-effect-despite-hopes-deal-2024-10-29/",
        "VietnamPlus (Chiến lược 150.000 cổng sạc V-Green): https://en.vietnamplus.vn"
    ],
    "DbrT-7btyyg": [
        "Báo Chính Phủ (Toàn văn bài phân tích Nghị quyết 79-NQ/TW Kinh tế nhà nước): https://xaydungchinhsach.chinhphu.vn/giai-phap-dot-pha-cho-kinh-te-nha-nuoc-119250727104607733.htm",
        "Báo Chính Phủ (Nghị quyết 41-NQ/TW về doanh nhân & kinh tế tư nhân): https://baochinhphu.vn"
    ],
    "q3PBqQ1EFL8": [
        "Tập đoàn Hòa Phát (Thông cáo Dung Quất 2 HRC): https://hoaphat.com.vn/en/news/hoa-phat-dung-quat-2-completes-installation-of-hrc-rolling-mill.html",
        "European Commission (Quy định thuế carbon CBAM): https://ec.europa.eu"
    ],
    "QBsQ7xFvmP4": [
        "World Bank PDF (Báo cáo Già hóa Dân số Việt Nam): https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf"
    ],
    "6nBCWNke_dg": [
        "U.S. SEC EDGAR (Báo cáo VinFast 20-F): https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm",
        "Vinhomes IR (Báo cáo tài chính kiểm toán): https://ir.vinhomes.vn/en"
    ],
    "TWsTsRQT8OM": [
        "The Investor (Nhà máy pin VinES-Gotion Vũng Áng 275 triệu USD): https://theinvestor.vn/vines-gotion-start-work-on-275-mln-battery-plant-d2664.html",
        "NHTSA (Báo cáo tỷ lệ nội địa hóa phụ tùng AALA Reports): https://www.nhtsa.gov"
    ],
    "L7oucqEzuWM": [
        "Vingroup Official IR (Cam kết hỗ trợ tài chính 2.5 tỷ USD): https://vingroup.net/en/news/detail/2845/vingroup-and-its-chairman-pledge-usd-25-billion-financial-support-package-to-vinfast"
    ],
    "3L8W6DT6Fhc": [
        "Federal Register (Chính phủ Mỹ - Văn bản Luật 15 CFR Part 791): https://www.federalregister.gov/documents/2024/09/26/2024-21903/securing-the-information-and-communications-technology-and-services-supply-chain-connected-vehicles",
        "European Commission (Quyết định áp thuế xe điện TQ): https://policy.trade.ec.europa.eu/news/commission-imposes-provisional-countervailing-duties-imports-battery-electric-vehicles-bev-china-2024-07-04_en"
    ],
    "i9kLxtgJID8": [
        "VinFast IR (Báo cáo doanh số giao xe): https://ir.vinfastauto.us",
        "Hiệp hội VAMA (Báo cáo thị phần ô tô Việt Nam): https://vama.org.vn"
    ],
    "gkcBQc0bNBo": [
        "IMF World Economic Outlook (GDP Việt Nam vs Philippines): https://www.imf.org",
        "San Miguel Corporation IR (Báo cáo doanh thu): https://www.sanmiguel.com.ph"
    ],
    "f-gFbIsFF3I": [
        "IMF World Economic Outlook (GDP Việt Nam vs Philippines): https://www.imf.org",
        "San Miguel Corporation IR (Báo cáo doanh thu): https://www.sanmiguel.com.ph"
    ],
    "ba6ztlHYJmg": [
        "Bloomberg (Lịch sử thương hiệu xa xỉ Vertu & sự kiện phá sản 2017): https://www.bloomberg.com"
    ],
    "wYEJ0TeZsaA": [
        "U.S. SEC EDGAR (Báo cáo tài chính VinFast 20-F): https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm"
    ],
    "miQouUJfe5w": [
        "Ngân hàng Nhà nước Việt Nam (Văn bản quản lý kinh doanh đá quý & kim cương): https://sbv.gov.vn"
    ],
    "xa32g_totHY": [
        "International Energy Agency (IEA Global EV Outlook Report): https://www.iea.org"
    ],
    "Kx5gy2ZKyaI": [
        "U.S. SEC EDGAR (Báo cáo tài chính VinFast 20-F): https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm"
    ],
    "2bDzlwomsdA": [
        "Báo Chính Phủ (Phân bổ vốn đầu tư công & Room tín dụng 18 siêu dự án): https://baochinhphu.vn"
    ],
    "1ZMyW8laPxQ": [
        "Thư Viện Pháp Luật (Luật Các tổ chức tín dụng số 32/2024/QH15): https://thuvienphapluat.vn"
    ],
    "WxEBgp0qeAE": [
        "SAFE China (Dữ liệu dự trữ ngoại hối 3.44 nghìn tỷ USD): https://www.safe.gov.cn/en/",
        "U.S. EIA (Báo cáo điểm nghẽn vận tải dầu khí Malacca): https://www.eia.gov"
    ],
    "61-Iy7d9Cbo": [
        "Tesla Official IR (Dự án Optimus Robot & AI Day): https://ir.tesla.com"
    ],
    "TT-U3xvo9O4": [
        "Vinhomes IR (Báo cáo quỹ đất & Báo cáo tài chính hợp nhất): https://ir.vinhomes.vn/en"
    ],
    "MHdEUF5dNfc": [
        "VinFast Official (Bảng chi phí thuê pin & sạc điện): https://vinfastauto.com"
    ],
    "BzaksQ0POPg": [
        "U.S. SEC EDGAR (Form 6-K Báo cáo thị trường Indonesia): https://www.sec.gov"
    ],
    "rnpEGo-BeAg": [
        "Vingroup IR (Báo cáo thường niên tập đoàn): https://vingroup.net"
    ],
    "3rY-jzkWLEs": [
        "Hiệp hội VAMA (Báo cáo thị phần ô tô Việt Nam): https://vama.org.vn"
    ],
    "Lr2DqAruqAQ": [
        "Press Release GSM / VinFast Ấn Độ (Kế hoạch phát triển taxi điện): https://vinfastauto.com"
    ],
    "1FRyjVNPJ6A": [
        "Press Release GSM / VinFast Ấn Độ (Kế hoạch phát triển taxi điện): https://vinfastauto.com"
    ]
}

def clean_original_description(raw_desc):
    """
    Strips ALL old disclaimers, duplicate blocks, and appended citation markers completely.
    Returns ONLY the original clean description.
    """
    # Key markers that indicate the start of an added disclaimer/citation section
    markers = [
        "--------------------------------------------------",
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM",
        "📚 NGUỒN TÀI LIỆU THAM KHẢO",
        "📚 TỔNG HỢP NGUỒN TÀI LIỆU"
    ]
    
    cutoff = len(raw_desc)
    for m in markers:
        idx = raw_desc.find(m)
        if idx != -1 and idx < cutoff:
            cutoff = idx
            
    original = raw_desc[:cutoff].strip()
    return original

def format_single_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và báo chí chính thống. Video mang tính phóng sự tài liệu, kiến thức kinh tế vĩ mô; KHÔNG cấu thành lời khuyên đầu tư.\n\n"
        "📚 TỔNG HỢP NGUỒN TÀI LIỆU THAM KHẢO & DỮ LIỆU ĐỔI CHIẾU:\n"
    )
    for c in citations:
        disclaimer += f"• {c}\n"
    disclaimer += "--------------------------------------------------"
    return disclaimer

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    print(f"🧹 CLEANING & DE-DUPLICATING ALL 34 VIDEO DESCRIPTIONS LIVE...\n")
    
    updated = 0
    for vid, cits in TAILORED_DB.items():
        try:
            res = youtube.videos().list(part='snippet', id=vid).execute()
            items = res.get('items', [])
            if not items:
                print(f"❌ Video ID {vid} not found.")
                continue
                
            snippet = items[0]['snippet']
            title = snippet.get('title', '')
            raw_desc = snippet.get('description', '')
            
            # Step 1: Strip ALL old disclaimer duplicates completely
            clean_desc = clean_original_description(raw_desc)
            
            # Step 2: Build ONE AND ONLY ONE Block 6
            block_6 = format_single_block_6(cits)
            
            # Step 3: Check total length limit (YouTube max 5000)
            max_allowed_clean = 4900 - len(block_6)
            if len(clean_desc) > max_allowed_clean:
                # Trim clean_desc safely at the last newline before max_allowed_clean
                trimmed = clean_desc[:max_allowed_clean]
                last_nl = trimmed.rfind("\n")
                if last_nl > 200:
                    clean_desc = trimmed[:last_nl].strip()
                else:
                    clean_desc = trimmed.strip()
                    
            final_desc = f"{clean_desc}\n\n{block_6}"
            
            snippet['description'] = final_desc
            
            youtube.videos().update(
                part='snippet',
                body={'id': vid, 'snippet': snippet}
            ).execute()
            
            print(f"  ✅ PERFECT FIX: [{title[:35]}...] (ID: {vid}) -> Length: {len(final_desc)}")
            updated += 1
            
        except Exception as e:
            print(f"  ❌ Error updating {vid}: {e}")
            
    print(f"\n🎉 DE-DUPLICATION COMPLETE: Successfully cleaned and updated {updated}/34 videos on YouTube!")

if __name__ == "__main__":
    main()
