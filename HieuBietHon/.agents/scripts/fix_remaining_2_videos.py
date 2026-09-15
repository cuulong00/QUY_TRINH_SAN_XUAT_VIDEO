import os
import sys
import re

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")

FIX_VIDEOS = [
    {
        "id": "pOpv3INMYGM",
        "title": "Vì Sao VinSpace Phải Vội Vàng Phóng Vệ Tinh?",
        "citations": [
            "Tuổi Trẻ Online (Bài báo gốc Hợp đồng VinSpace-SpaceX): https://tuoitre.vn/vinspace-bat-tay-spacex-phong-ve-tinh-vao-nam-2027-100260811093243012.htm",
            "SpaceX Official (Rideshare Program): https://www.spacex.com/rideshare",
            "EUSPA (Báo cáo thị trường Vũ trụ): https://www.euspa.europa.eu",
            "Thư Viện Pháp Luật (Luật Viễn thông 2023): https://thuvienphapluat.vn"
        ]
    },
    {
        "id": "DbrT-7btyyg",
        "title": "\"Sếu Đầu Đàn\" Đang Được Nuôi Dưỡng Thế Nào?",
        "citations": [
            "Báo Chính Phủ (Nghị quyết 79-NQ/TW): https://xaydungchinhsach.chinhphu.vn/giai-phap-dot-pha-cho-kinh-te-nha-nuoc-119250727104607733.htm",
            "Báo Chính Phủ (Kinh tế nhà nước): https://xaydungchinhsach.chinhphu.vn/nhan-thuc-ve-vai-tro-chu-dao-cua-kinh-te-nha-nuoc-119250727105052903.htm",
            "World Bank PDF (Già hóa Dân số): https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf"
        ]
    }
]

def format_short_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh HieuBietHon được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và báo chí chính thống. Video mang tính phóng sự tài liệu, kiến thức kinh tế vĩ mô; KHÔNG cấu thành lời khuyên đầu tư.\n\n"
        "📚 NGUỒN TÀI LIỆU THAM KHẢO (VERIFIED DEEP SOURCES):\n"
    )
    for c in citations:
        disclaimer += f"• {c}\n"
    disclaimer += "--------------------------------------------------"
    return disclaimer

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    for v in FIX_VIDEOS:
        vid = v['id']
        title = v['title']
        cits = v['citations']
        print(f"🔄 Fixing overflow description for [{title}] ({vid})...")
        
        res = youtube.videos().list(part='snippet', id=vid).execute()
        items = res.get('items', [])
        if not items:
            continue
            
        snippet = items[0]['snippet']
        curr_desc = snippet.get('description', '')
        cleaned_desc = re.sub(r'--------------------------------------------------[\s\S]*?--------------------------------------------------', '', curr_desc).strip()
        
        block_6 = format_short_block_6(cits)
        new_desc = f"{cleaned_desc}\n\n{block_6}"
        
        # Ensure total length <= 4900 chars
        if len(new_desc) > 4900:
            allowed_len = 4900 - len(block_6) - 10
            cleaned_desc = cleaned_desc[:allowed_len] + "..."
            new_desc = f"{cleaned_desc}\n\n{block_6}"
            
        snippet['description'] = new_desc
        
        youtube.videos().update(
            part='snippet',
            body={'id': vid, 'snippet': snippet}
        ).execute()
        
        print(f"  ✅ SUCCESS: Fixed and updated {vid} (Length: {len(new_desc)})")

if __name__ == "__main__":
    main()
