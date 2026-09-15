import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Khối YMYL Disclaimer & AI Disclosure tiêu chuẩn của kênh Dòng Chảy
DISCLAIMER_AND_AI_BLOCK = """

--------------------------------------------------
ℹ️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM & TÍNH KHÁCH QUAN:
Mọi nội dung trên kênh được nghiên cứu và biên tập độc lập từ các báo cáo tài chính công khai, văn bản quy phạm pháp luật và nguồn tin chính thống. Video mang tính chất phóng sự tài liệu, chia sẻ kiến thức kinh tế và giáo dục tri thức; KHÔNG cấu thành lời khuyên đầu tư, tài chính hay pháp lý dưới mọi hình thức.

🎙️ THÔNG TIN SẢN XUẤT & ĐỘI NGŨ (AI DISCLOSURE):
- Biên tập & Nghiên cứu: Ban Biên tập Dòng Chảy
- Định dạng: Phim tài liệu đồ họa (Editorial Vector Graphic Animation)
- Đồ họa và giọng đọc được tạo/tối ưu bằng công nghệ AI tổng hợp dưới sự kiểm duyệt 100% của đội ngũ biên tập viên.

📚 NGUỒN TÀI LIỆU THAM KHẢO CHÍNH:
- Báo cáo tài chính đã kiểm toán / Tổng cục Thống kê / World Bank / IMF / Nghị định & Thông tư liên quan.
--------------------------------------------------"""

def update_channel_videos():
    token_file = '../tokens/manager_token.json'
    if not os.path.exists(token_file):
        print("❌ Không tìm thấy manager_token.json")
        return

    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    youtube = build('youtube', 'v3', credentials=creds)

    ch_res = youtube.channels().list(part='snippet,contentDetails', mine=True).execute()
    if not ch_res.get('items'):
        print("❌ Không tìm thấy kênh nào.")
        return

    channel = ch_res['items'][0]
    ch_title = channel['snippet']['title']
    uploads_playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']

    print(f"\n🚀 ĐANG TIẾN HÀNH CẬP NHẬT TỰ ĐỘNG METADATA & CỜ AI CHIẾN LƯỢC CHO KÊNH: '{ch_title}'")
    print("="*60)

    video_list = []
    next_page_token = None

    while True:
        pl_req = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_resp = pl_req.execute()

        for item in pl_resp.get('items', []):
            v_id = item['snippet']['resourceId']['videoId']
            v_title = item['snippet']['title']
            video_list.append({'id': v_id, 'title': v_title})

        next_page_token = pl_resp.get('nextPageToken')
        if not next_page_token:
            break

    print(f"📋 Tìm thấy tổng cộng {len(video_list)} video cần kiểm tra và cập nhật.\n")

    updated_count = 0

    for idx, v in enumerate(video_list):
        video_id = v['id']
        title = v['title']

        v_res = youtube.videos().list(part='snippet,status', id=video_id).execute()
        if not v_res.get('items'):
            continue

        item = v_res['items'][0]
        snippet = item['snippet']
        status = item['status']
        current_desc = snippet.get('description', '')

        # 1. Đảm bảo Mô tả có khối YMYL & AI Disclosure
        if "TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM" not in current_desc or "THÔNG TIN SẢN XUẤT & ĐỘI NGŨ" not in current_desc:
            new_desc = current_desc.strip() + DISCLAIMER_AND_AI_BLOCK
        else:
            new_desc = current_desc

        # 2. Đặt cờ containsSyntheticMedia = True trực tiếp trong status
        status['containsSyntheticMedia'] = True

        body = {
            'id': video_id,
            'snippet': {
                'title': snippet['title'],
                'description': new_desc,
                'categoryId': snippet.get('categoryId', '22'),
                'tags': snippet.get('tags', [])
            },
            'status': status
        }

        try:
            youtube.videos().update(part='snippet,status', body=body).execute()
            print(f"✅ [{idx+1}/{len(video_list)}] ĐÃ CẬP NHẬT THÀNH CÔNG (AI Flag = True & Metadata): {title}")
            updated_count += 1
        except Exception as e:
            print(f"❌ [{idx+1}/{len(video_list)}] Lỗi khi cập nhật {title}: {e}")

    print("\n" + "="*60)
    print(f"🎉 HOÀN THÀNH TỰ ĐỘNG CẬP NHẬT METADATA & CỜ AI (containsSyntheticMedia = True):")
    print(f"  - Thành công: {updated_count}/{len(video_list)} video")
    print("="*60)

if __name__ == '__main__':
    update_channel_videos()
