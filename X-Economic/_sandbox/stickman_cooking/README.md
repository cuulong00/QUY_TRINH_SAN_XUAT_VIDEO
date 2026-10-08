# Stickman Cooking Demo — Motion Graphics by Code

Bản demo hoạt hình người que (stick figure) đang nấu ăn, được dựng và render 100% bằng code (Python + Pillow + FFmpeg direct pipe), không sử dụng bất kỳ engine video AI nào. Phục vụ kiểm tra năng lực dựng visual motion graphics theo chuẩn nhận diện kênh **X-Economy**.

---

## 🎨 Bảng Màu Chuẩn Nhận Diện Kênh
- **Nền (Background):** `#0A0E17` (Deep dark slate navy)
- **Nét Người Que (Stick Figure & Hat):** `#F5F0E6` (Ivory cream)
- **Lửa & Điểm Nhấn (Fire & Accent Gold):** `#D4AF37` (Muted gold / amber)
- **Hơi Nước (Steam):** `#00E5FF` (Electric cyan)

---

## ⏱️ Kịch Bản 4 Nhịp Hoạt Họa (Thời lượng: 18.0 giây / 540 frames)
1. **Nhịp 1 (0.0s – 4.5s / frames 0–134):**
   - Người que cầm chảo bước tới bếp, đặt chảo lên bếp ga.
   - Tay trái vặn núm bếp (click marker vàng), lửa vàng `#D4AF37` bốc lên rực rỡ dưới đáy chảo.
2. **Nhịp 2 (4.5s – 8.5s / frames 135–254):**
   - Tay trái cầm âu nguyên liệu thả 14 miếng thức ăn (tròn, vuông màu sắc tươi mới) vào chảo theo quỹ đạo parabol.
   - Thức ăn chạm mặt chảo nóng nảy nhẹ, khói/hơi nước `#00E5FF` bắt đầu cuộn sóng bốc lên.
3. **Nhịp 3 (8.5s – 14.0s / frames 255–419):**
   - Đảo chảo 3 nhịp tăng tiến: người que hạ gối, nhấc chảo nghiêng tới trước, hất nguyên liệu tung bay lên không trung theo đường cong trọng lực đẹp mắt, xoay đảo 360 độ rồi đón lại gọn gàng vào lòng chảo.
   - Hơi nước và lửa cuộn theo từng nhịp hất chảo.
4. **Nhịp 4 (14.0s – 18.0s / frames 420–539):**
   - Tắt bếp ga, nghiêng chảo 45° trút toàn bộ thức ăn nóng hổi sang chiếc đĩa sứ viền vàng bên cạnh.
   - Đặt chảo rỗng lại mặt bếp, người que xoay người hướng về màn hình, gật đầu tự tin và giơ ngón tay cái (**thumbs-up**) đắc thắng. Đĩa thức ăn bốc hơi nước nhẹ nhàng.

---

## 🛠️ Công Cụ & Thư Viện Sử Dụng
- **Ngôn ngữ:** Python 3.13
- **Thư viện đồ họa:** `PIL` (Pillow) với kỹ thuật **2x Supersampling** (vẽ ở độ phân giải 3840x2160, sau đó downsample bằng Bilinear filter về 1920x1080 để khử răng cưa và mượt khớp nối).
- **Trình xuất video:** `ffmpeg` (được pipe trực tiếp qua stdin rawvideo `rgb24`, mã hóa `libx264`, `-crf 18`, `-pix_fmt yuv420p`).

---

## 🚀 Lệnh Render Lại
```bash
python3 /Users/pro16/Documents/VideoProject/X-Economic/_sandbox/stickman_cooking/render_stickman.py
```

---

## 📊 Kết Quả Kiểm Nghiệm Kỹ Thuật (ffprobe Output)
```text
codec_name=h264
width=1920
height=1080
r_frame_rate=30/1
duration=18.000000
nb_frames=540
```
- **Codec:** H.264 (`yuv420p`)
- **Độ phân giải:** 1920x1080
- **Tốc độ khung hình:** 30 fps
- **Thời lượng thực tế:** 18.000000 giây (540 frames)
- **Âm thanh / Chữ:** Silent demo, 0 audio stream, 0 text watermark.

---

## 🖼️ Contact Sheet (8 Khung Hình Rải Đều)
Ảnh lưới 8 khoảnh khắc tiêu biểu được lưu tại: [`stickman_contact_sheet.png`](stickman_contact_sheet.png).
