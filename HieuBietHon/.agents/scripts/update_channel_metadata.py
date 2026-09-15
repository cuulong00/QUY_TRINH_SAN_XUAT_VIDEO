#!/usr/bin/env python3
"""
YouTube Channel Metadata Auto-Updater
Kênh: Hiểu Biết Hơn (@HieuBietHon_az)
Tác dụng: Đăng nhập Google OAuth 2.0 và tự động cập nhật trực tiếp Mô tả kênh (Description) & Keywords lên YouTube.
"""

import os
import sys
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube'
]

CREDS_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/credentials"
CLIENT_SECRET_FILE = os.path.join(CREDS_DIR, "client_secret_439442313894-5vh2dak3l4lv3kii8cirk6r3rvpfshs3.apps.googleusercontent.com.json")
TOKEN_FILE = os.path.join(CREDS_DIR, "token.json")

NEW_DESCRIPTION = """Hiểu Biết Hơn — Giải mã những câu hỏi tò mò nhất thế giới!

Kênh Edutainment tri thức & khoa học kịch tính hàng đầu: Khám phá những kịch bản giả định "What-If" nghẹt thở, kỹ năng sinh tồn cực hạn, so sánh sức mạnh quân sự đỉnh cao, giải phẫu những nhà tù tối mật, giải mã tội phạm bí ẩn và khám phá giới hạn cơ thể con người.

Chúng tôi mang đến:
🔹 Kịch bản What-If & Khoa học tận thế: Điều gì xảy ra nếu Trái Đất ngừng quay?
🔹 Sinh tồn cực hạn: 24h thoát khỏi những tử địa khắc nghiệt nhất.
🔹 So sánh Quân sự & Vũ khí tối thượng: Đối đầu chiến thuật và hỏa lực thực tế.
🔹 Giới hạn Cơ thể & Y học kỳ bí: Những phản ứng sinh học ít ai ngờ tới.

Tôn chỉ: Khoa học chính xác 100% — Trực quan sống động — Mở mang tầm mắt từng giây!

👉 Đăng ký kênh ngay: https://www.youtube.com/@HieuBietHon_az"""

NEW_KEYWORDS = '"hiểu biết hơn" "hieu biet hon" "the infographics show vietnam" "khoa học kịch tính" "kịch bản what if" "sinh tồn cực hạn" "so sánh quân sự" "nhà tù tối mật" "giới hạn cơ thể" "bí ẩn khoa học" "edutainment"'

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"⚠️ Token hết hạn ({e}), khởi tạo lại phiên đăng nhập OAuth...")
                if os.path.exists(TOKEN_FILE):
                    os.remove(TOKEN_FILE)
                creds = None
                
        if not creds:
            if not os.path.exists(CLIENT_SECRET_FILE):
                print(f"❌ Không tìm thấy file client_secret tại: {CLIENT_SECRET_FILE}", flush=True)
                sys.exit(1)
            print("\n🔑 ĐANG KHỞI TẠO PHIÊN XÁC THỰC GOOGLE OAUTH 2.0...", flush=True)
            print("👉 Trình duyệt sẽ tự động mở trang đăng nhập Google.", flush=True)
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0, prompt='consent')
            
            with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
                f.write(creds.to_json())
            print(f"✅ Đã lưu token mới thành công vào: {TOKEN_FILE}", flush=True)

    return build('youtube', 'v3', credentials=creds)

def main():
    print("🚀 Bắt đầu quá trình cập nhật thông tin kênh trực tiếp qua YouTube API...")
    youtube = get_authenticated_service()
    
    # 1. Lấy thông tin kênh hiện tại
    ch_res = youtube.channels().list(mine=True, part='id,snippet,brandingSettings').execute()
    if not ch_res.get('items'):
        print("❌ Không tìm thấy thông tin kênh của tài khoản hiện tại.")
        return
        
    channel = ch_res['items'][0]
    ch_id = channel['id']
    ch_title = channel['snippet']['title']
    print(f"📺 Đã kết nối kênh: {ch_title} (Channel ID: {ch_id})")
    
    # 2. Cập nhật brandingSettings (Description & Keywords)
    branding_settings = channel.get('brandingSettings', {})
    if 'channel' not in branding_settings:
        branding_settings['channel'] = {}
        
    branding_settings['channel']['description'] = NEW_DESCRIPTION
    branding_settings['channel']['keywords'] = NEW_KEYWORDS
    
    print("\n📝 Đang gửi yêu cầu cập nhật Mô tả kênh và Keywords...")
    update_res = youtube.channels().update(
        part='brandingSettings',
        body={
            'id': ch_id,
            'brandingSettings': branding_settings
        }
    ).execute()
    
    print("🎉 CẬP NHẬT THÀNH CÔNG 100% LÊN YOUTUBE!")
    print(f"✅ Tên kênh: {update_res.get('snippet', {}).get('title', ch_title)}")
    print(f"✅ Mô tả mới đã được áp dụng:\n{NEW_DESCRIPTION[:200]}...\n")
    print(f"✅ Keywords mới: {NEW_KEYWORDS}")

if __name__ == "__main__":
    main()
