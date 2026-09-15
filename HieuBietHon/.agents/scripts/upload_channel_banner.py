#!/usr/bin/env python3
"""
Upload YouTube Channel Banner via YouTube Data API v3
"""

import os
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/youtube'
]

CREDS_DIR = "/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/credentials"
TOKEN_FILE = os.path.join(CREDS_DIR, "token.json")
BANNER_FILE = "/Users/pro16/Documents/VideoProject/HieuBietHon/profile/banner_hieubiethon_2560x1440.jpg"

def main():
    print("🚀 Bắt đầu quá trình upload và cập nhật Ảnh Bìa (Banner) qua YouTube API...", flush=True)
    if not os.path.exists(TOKEN_FILE):
        print(f"❌ Không tìm thấy file token tại: {TOKEN_FILE}", flush=True)
        return
        
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)
    
    # 1. Lấy thông tin kênh
    ch_res = youtube.channels().list(mine=True, part='id,snippet,brandingSettings').execute()
    if not ch_res.get('items'):
        print("❌ Không tìm thấy thông tin kênh của tài khoản hiện tại.", flush=True)
        return
        
    channel = ch_res['items'][0]
    ch_id = channel['id']
    ch_title = channel['snippet']['title']
    print(f"📺 Kênh: {ch_title} (ID: {ch_id})", flush=True)
    
    # 2. Upload banner image
    print(f"📤 Đang upload tệp banner: {BANNER_FILE}...", flush=True)
    media = MediaFileUpload(BANNER_FILE, mimetype='image/jpeg', resumable=True)
    
    banner_res = youtube.channelBanners().insert(
        body={},
        media_body=media
    ).execute()
    
    banner_url = banner_res.get('url')
    print(f"✅ Banner đã được upload lên máy chủ YouTube: {banner_url}", flush=True)
    
    # 3. Cập nhật brandingSettings của kênh
    branding = channel.get('brandingSettings', {})
    if 'image' not in branding:
        branding['image'] = {}
    branding['image']['bannerExternalUrl'] = banner_url
    
    print("🔄 Đang gán Banner mới vào Kênh YouTube...", flush=True)
    update_res = youtube.channels().update(
        part='brandingSettings',
        body={
            'id': ch_id,
            'brandingSettings': branding
        }
    ).execute()
    
    print("🎉 CẬP NHẬT ẢNH BÌA YOUTUBE THÀNH CÔNG 100%!", flush=True)

if __name__ == "__main__":
    main()
