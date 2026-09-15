# /generate_videos Workflow

Tự động hóa toàn bộ quy trình sản xuất video (Phase 14 — Batch Video Production) bằng Google Flow Tool Builder (Nano Banana 2 & Veo 3.1 Lite) qua giao thức Chrome CDP port 9222.

---

## 🚀 Các Bước Thực Hiện Của Agent

### Bước 1: Kiểm toán tiến độ cảnh hiện có
Chạy lệnh kiểm tra số cảnh đã render và các cảnh còn thiếu:
```bash
python3 scripts/check_video_progress.py --episode <slug>
```

### Bước 2: Kiểm tra Chrome Remote Debugger
Đảm bảo Chrome đang lắng nghe tại port 9222:
```bash
curl -s http://127.0.0.1:9222/json/version
```
Nếu chưa bật, hiển thị lệnh hướng dẫn khởi động Chrome Debugger cho người dùng:
```bash
open -na "Google Chrome" --args \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome-Debug" \
  --profile-directory="Profile 2" \
  "https://flow.google.com/project/23e2de09-56ca-4203-bae0-c56f811bde25/tool/cb0f557c-bd15-4f1a-af4a-9a790b69d0c7?fromViewSource=tools&mode=EDIT"
```

### Bước 3: Khởi động quy trình sản xuất tự động
Khởi chạy lệnh sản xuất cấp cao (tự động lọc cảnh thiếu, nạp ảnh tham chiếu `@avatar.jpg`, nạp prompt, bấm Launch Matrix, watchdog 300s, tự tải và chuyển file về thư mục đích):
```bash
python3 scripts/produce_episode_videos.py --episode <slug>
```

### Bước 4: Kiểm toán hoàn tất (Production Sign-off)
Sau khi batch hoàn tất, chạy lại lệnh kiểm toán để xác nhận 100% cảnh đã có mặt với dung lượng hợp lệ:
```bash
python3 scripts/check_video_progress.py --episode <slug>
```
