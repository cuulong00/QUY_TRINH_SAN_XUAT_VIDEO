---
name: fb-video-uploader
description: Upload video dài dung lượng lớn (5-11 GB) lên Facebook Page qua giao thức Resumable Chunked Upload API. Hỗ trợ resume, retry, custom thumbnail và lên lịch phát sóng.
---

# Facebook Resumable Video Uploader Skill

## 📌 Khi nào sử dụng
Kích hoạt skill này khi cần:
- Tải các file video dài (MP4/MOV từ vài trăm MB đến hàng chục GB) lên Fanpage Facebook.
- Đặt thumbnail tùy chỉnh cho video Facebook.
- Lên lịch phát sóng (Scheduling) video trong tương lai.
- Kiểm tra trạng thái mã hóa (Encoding / Processing status) của video trên Meta.

## 🚀 Cách thực thi

### 1. Upload video trực tiếp bằng CLI:
```bash
python scripts/upload_video.py \
  --file "/Users/pro16/Movies/CapCut/SieuCongTrinh_BatCom_Master/SieuCongTrinh_BatCom_Master.mp4" \
  --title "Tiêu đề video chuẩn Facebook" \
  --desc-file "storage/ready_posts/sieu_cong_trinh.txt" \
  --thumb "storage/thumbnails/sieu_cong_trinh.jpg"
```

### 2. Upload và hẹn giờ phát sóng:
```bash
python scripts/upload_video.py \
  --file "/path/to/video.mp4" \
  --title "Tiêu đề" \
  --desc "Nội dung caption..." \
  --schedule "2026-09-20 20:00"
```

### 3. Kiểm tra trạng thái video:
```bash
python scripts/check_video_status.py --video-id "<VIDEO_ID>"
```
