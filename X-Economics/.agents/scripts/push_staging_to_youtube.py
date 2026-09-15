import os
import sys
import re

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("❌ Missing Google API libraries.")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDS_DIR = "/Users/pro16/Documents/VideoProject/X-Economics/.agents/credentials"
TOKEN_PATH = os.path.join(CREDS_DIR, "token.json")
CLIENT_SECRET_PATH = os.path.join(CREDS_DIR, "client_secret_439442313894-5vh2dak3l4lv3kii8cirk6r3rvpfshs3.apps.googleusercontent.com.json")
STAGING_FILE = "/Users/pro16/Documents/VideoProject/X-Economics/youtube_citations_staging.md"

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        except Exception as e:
            print(f"Error loading token: {e}")
            creds = None
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Token refresh failed: {e}")
                creds = None

        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def parse_staging():
    if not os.path.exists(STAGING_FILE):
        print(f"❌ Staging file not found: {STAGING_FILE}")
        return []

    with open(STAGING_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = content.split("## VIDEO: ")
    videos = []
    for b in blocks[1:]:
        lines = b.strip().split("\n")
        title = lines[0].strip()
        video_id = None
        citations = []
        for line in lines[1:]:
            if line.startswith("- **ID**:"):
                video_id = line.replace("- **ID**:", "").strip()
            elif line.strip().startswith("- ") and not line.startswith("- **"):
                citations.append(line.strip()[2:])
        
        if video_id and not video_id.startswith("TBD_"):
            videos.append({
                'title': title,
                'id': video_id,
                'citations': citations
            })
    return videos

def format_block_6(citations):
    disclaimer = (
        "--------------------------------------------------\n"
        "ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:\n"
        "Nội dung trên kênh GocNhinPodcast được nghiên cứu và tổng hợp từ các báo cáo tài chính công khai, văn bản pháp luật và nguồn tin báo chí chính thống. Video mang tính chất phân tích phóng sự tài liệu, kiến thức kinh tế vĩ mô và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.\n\n"
        "🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ:\n"
        "- Biên tập & Nghiên cứu: Ban Biên tập GocNhinPodcast\n"
        "- Định dạng: Phim tài liệu đồ họa (Editorial Vector Graphic Animation)\n"
        "- Công nghệ hỗ trợ: Đồ họa và giọng đọc được tối ưu bằng công nghệ AI dưới sự kiểm duyệt và hoàn thiện 100% từ đội ngũ biên tập viên.\n\n"
        "📚 NGUỒN TÀI LIỆU THAM KHẢO CHÍNH (VERIFIED SOURCES):\n"
    )
    for c in citations:
        disclaimer += f"• {c}\n"
    disclaimer += "--------------------------------------------------"
    return disclaimer

def main():
    print("🚀 Authenticating with YouTube API...")
    youtube = get_authenticated_service()
    videos = parse_staging()
    
    print(f"📋 Found {len(videos)} valid videos to update from staging.")
    
    success = 0
    for v in videos:
        vid = v['id']
        title = v['title']
        cits = v['citations']
        print(f"\n🔄 Processing [{title}] (ID: {vid})...")
        
        try:
            res = youtube.videos().list(part='snippet', id=vid).execute()
            items = res.get('items', [])
            if not items:
                print(f"❌ Video not found on YouTube: {vid}")
                continue
                
            snippet = items[0]['snippet']
            current_desc = snippet.get('description', '')
            
            # Remove any existing disclaimer block to avoid duplication
            cleaned_desc = re.sub(r'--------------------------------------------------[\s\S]*?--------------------------------------------------', '', current_desc).strip()
            
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
            
            print(f"✅ Updated description for: [{title}]")
            success += 1
            
        except Exception as e:
            print(f"❌ Error updating video {vid}: {e}")
            
    print(f"\n🎉 COMPLETED: Successfully updated {success}/{len(videos)} videos on YouTube!")

if __name__ == "__main__":
    main()
