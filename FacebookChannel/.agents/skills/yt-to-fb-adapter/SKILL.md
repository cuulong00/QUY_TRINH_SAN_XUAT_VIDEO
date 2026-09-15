---
name: yt-to-fb-adapter
description: Chuyển hóa kịch bản, tóm tắt và mô tả video từ YouTube (Dòng Chảy, GocNhinPodcast) thành gói bài đăng Facebook chuẩn thuật toán MSI và văn hóa đọc lướt.
---

# YouTube to Facebook Content Adapter Skill

## 📌 Khi nào sử dụng
Kích hoạt skill này khi người dùng muốn tái sử dụng một tập video từ `Dong_Chay` hoặc `GocNhinPodcast` để chuẩn bị đăng bài lên Facebook Fanpage.

## 🛠️ Quy trình thực hiện

1. **Xác định nguồn kịch bản:**
   - Tập `GocNhinPodcast`: Đường dẫn `/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/<ten-tap>/`
   - Tập `Dong_Chay`: Đường dẫn `/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/<ten-tap>/`

2. **Chạy công cụ chuyển hóa tự động:**
```bash
python scripts/adapt_content.py \
  --source "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kinh-te-hoc-tam-linh" \
  --channel "gocnhin"
```

3. **Nguyên tắc chuyển hóa của Agent:**
   - **Tách Hook:** Tìm 1-2 luận điểm nghịch lý nhất trong tập để dựng 3 dòng hook đầu.
   - **Visual Rhythm:** Định dạng ngắn 2 câu/đoạn, chèn bullet points.
   - **Gợi mở MSI:** Tạo 1 câu hỏi đối chiếu thực tiễn kích hoạt người đọc tranh luận.
   - **Hashtag:** Thêm 4 hashtag chuyên môn.
   - **Lưu trữ:** Lưu gói bài viết đã sinh ra vào `storage/ready_posts/<ten-tap>.txt`.
