# THUMBNAIL DESIGN BRIEF — EPISODE: SẾU ĐẦU ĐÀN (CHÍNH SÁCH KIẾN TẠO)
> Kênh: GocNhinPodcast — Phân Tích Kinh Tế Vĩ Mô & Chính Sách Công
> Persona: The Visual Hook Director & Compliance Specialist
> Headline Chốt: "SẾU ĐẦU ĐÀN / ĐANG ĐƯỢC NUÔI DƯỠNG THẾ NÀO?"

---

## 🎯 1. TƯ DUY HEADLINE CHÍNH THỨC & AN TOÀN TRUYỀN THÔNG

### Lý Do Chọn Tiêu Đề Mới:
- **Tiêu đề cũ:** Có từ nhạy cảm có nguy cơ bị lôi kéo bởi đối tượng cực đoan/tiêu cực.
- **Tiêu đề mới:**
  - Dòng 1 (Màu đỏ rực 3D): `SẾU ĐẦU ĐÀN`
  - Dòng 2 (Màu vàng rực 3D): `ĐANG ĐƯỢC NUÔI DƯỠNG THẾ NÀO?`
- **Định vị:** Mang tính kiến tạo, phóng sự tài liệu chuyên sâu, giải mã cơ chế thể chế (Nghị quyết 79, tín dụng xanh, hạ tầng lõi) mà Nhà nước và nền kinh tế đang dồn lực cho các đại doanh nghiệp dân tộc cản gió.

---

## 🎨 2. BỐ CỤC NGHỆ THUẬT & HÌNH ẢNH THAM CHIẾU CEO

* **3 Vị Chủ Tịch/CEO Tham Chiếu Thực Tế:**
  - **Phạm Nhật Vượng** (Vingroup) - Vị trí đứng đầu trung tâm.
  - **Trương Gia Bình** (FPT) - Bên trái.
  - **Trần Đình Long** (Hòa Phát) - Bên phải.
* **Logo Chính Thức:** Vingroup/VinFast, FPT, Hòa Phát HPG xếp dọc header phía trên.
* **Hạ Tầng Biểu Tượng Phía Sau:** Đường sắt tốc độ cao VinSpeed, hạm đội ô tô điện VinFast, nhà máy thép Hòa Phát, phòng lab vi mạch FPT.
* **Chữ 3D Đỏ & Vàng Mobile-First:** Font chữ khổng lồ, viền và bóng đổ đen dày sắc nét trên di động.

---

## 📦 3. PROMPT TẠO ẢNH CHO NANOBANANA 2.0 (16:9)

```
An ultra-dramatic 8K widescreen 16:9 YouTube thumbnail featuring the exact title "SẾU ĐẦU ĐÀN" on line one in fiery red 3D metallic text with heavy black drop-shadow, and "ĐANG ĐƯỢC NUÔI DƯỠNG THẾ NÀO?" on line two in solid gold 3D metallic text. Features the three chairmen (Pham Nhat Vuong of Vingroup in center, Truong Gia Binh of FPT on left, and Tran Dinh Long of Hoa Phat on right) using their exact facial likenesses from the reference photos in /Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/seu-dau-dan/ceo/. Across the top, clean official logos of Vingroup/VinFast, FPT, and Hoa Phat are displayed. Behind them, high-speed rail lines, steel blast furnaces, VinFast electric cars, and semiconductor microchip foundries glow under dark midnight charcoal lighting. High contrast, mobile-first legibility, editorial financial cover style. No cartoon.
```

---

## 🔄 4. LỆNH UPSCALE 4K (POST-PROCESSING)

```bash
ffmpeg -i thumbnail_nuoi_duong_raw.jpg -vf "scale=4096:2304:flags=lanczos,unsharp=3:3:1.0:3:3:0.0" thumbnail_nuoi_duong_4k.png -y
```
