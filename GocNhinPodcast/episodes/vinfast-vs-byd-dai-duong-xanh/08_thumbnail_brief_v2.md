# Kế hoạch Thiết kế Thumbnail V2 — BYD PHÁ GIÁ / HÒNG TRIỆT HẠ VINFAST (Bản màu vàng)

Tài liệu này định hình headline, cấu trúc thiết kế và 5 phiên bản prompt tạo ảnh YouTube Thumbnail phiên bản V2 phục vụ A/B testing tối ưu CTR cho tập phim "VinFast vs BYD: Đại Dương Xanh". Phiên bản này tập trung vào khía cạnh giật gân, kịch tính của cuộc chiến giá với tiêu đề chính được thể hiện bằng các sắc độ màu vàng nổi bật khác nhau.

*   **Tiêu đề Video dự kiến:** VinFast vs BYD: Bản chất cuộc đấu không nằm ở chiếc xe
*   **Headline Chốt trên Thumbnail V2:** 
    *   Dòng 1: `BYD PHÁ GIÁ` (đổi sang **màu vàng** rực rỡ với các tông sắc thái khác nhau qua từng phiên bản để kích thích thị giác tối đa)
    *   Dòng 2: `HÒNG TRIỆT HẠ VINFAST` (đổi sang **màu trắng tuyền** `#FFFFFF` để tạo độ tương phản, làm nổi bật tiêu đề chính màu vàng)

---

## 🎨 Phân tích Ý tưởng Mỹ thuật V2 (Tư duy Visual Hook Director)

Để truyền tải thông điệp "Phá giá / Triệt hạ" một cách rõ ràng và chuyên nghiệp:
1.  **Bảng màu chữ (Typography Color):** 
    *   Dòng 1 "BYD PHÁ GIÁ" sử dụng các tông màu vàng nổi bật (như vàng điện rực rỡ, vàng kim loại gold, vàng chanh sáng, vàng hổ phách ấm, vàng cát lì).
    *   Dòng 2 "HÒNG TRIỆT HẠ VINFAST" sử dụng màu trắng tuyền đặc (`#FFFFFF`) để tạo điểm nghỉ thị giác và làm bật tiêu đề chính.
    *   Toàn bộ chữ có viền đen sắc nét cực dày (`thick sharp black outline`) và bóng đổ đen đậm (`heavy black drop-shadow`) để hiển thị cực tốt trên di động, đứng tự do trên nền tối.
2.  **Bố cục & Chủ thể (Visual Conflict):**
    *   **Bên phải (Gã khổng lồ áp đảo):** Một chiếc sedan điện BYD Seal màu xám lông chuột với thiết kế sắc nhọn, hầm hố đang lao đi với tốc độ cao, tạo ra vệt mờ chuyển động kịch tính và tàn lửa đỏ. Phía sau là bóng mờ chân dung khổng lồ của CEO BYD với ánh mắt nghiêm nghị, sắc sảo.
    *   **Bên trái (Hào thủ thế):** Chiếc SUV VinFast VF8 màu xanh lục bảo/electric cyan đặc trưng đứng vững chãi, được che chắn bởi một hào sáng xanh ngọc bảo phát ra từ một trụ sạc V-Green bên cạnh. Phía sau là bóng mờ chân dung tỷ phú Phạm Nhật Vượng với vẻ mặt điềm tĩnh, tự tin.
    *   **Hậu cảnh:** Tông màu tối ấm áp (charcoal noir) kết hợp với những tia sét đỏ và biểu đồ đường giá xe điện đang cắm đầu lao dốc xé đôi không gian ở giữa.

---

## 📦 5 Phiên bản Prompt Tạo ảnh cho NanoBanana 2.0 (Midjourney/Imagen)

Mỗi prompt được thiết kế dạng văn xuôi liên tục 16:9 gốc, chỉ định rõ case chữ tiếng Việt có dấu, sắc thái màu vàng khác nhau của dòng 1 và màu trắng tương phản của dòng 2.

### Phiên bản 1: Sắc vàng điện rực rỡ (Electric Yellow) - Split-screen Đối xứng
> A dramatic 8K cinematic YouTube thumbnail in 16:9 widescreen format. In the dark charcoal background, a fast-moving, aggressive grey BYD electric sedan on the right side is rushing forward, creating dynamic motion blur and red sparks. On the left side, a sleek electric SUV VinFast painted in vibrant electric cyan-teal color stands steady next to a glowing cyan V-Green charging station casting a protective light dome. In the background, transparent portraits of the Asian founder of VinFast looking calm on the left, and the BYD CEO Wang Chuanfu looking intense on the right. A massive, highly legible 3D typography text overlay is placed on the left side, reading "BYD PHÁ GIÁ" on the first line in solid electric yellow, and "HÒNG TRIỆT HẠ VINFAST" on the second line in solid clean white, both using a heavy geometric sans-serif typeface with a thick sharp black outline and a heavy black drop shadow. --ar 16:9

### Phiên bản 2: Sắc vàng kim loại bóng (Glossy Gold Metal) - Biểu đồ sụp đổ
> An editorial-style 8K YouTube thumbnail in 16:9 widescreen. The background features a dark slate-grey grid pattern with a glowing red line graph plunging sharply downward. In the foreground on the right, a large grey BYD sedan sits under a harsh red spotlight. On the left, a vibrant electric cyan VinFast SUV is illuminated by a cool turquoise light. In the upper center, a heavy 3D metallic text overlay reads "BYD PHÁ GIÁ" on the first line in glossy gold-yellow metal, and "HÒNG TRIỆT HẠ VINFAST" on the second line in brushed white steel, using a heavy blocky sans-serif font with a thick crisp black outline and a deep black drop-shadow. The portraits of the two Asian CEOs are faintly visible in the dark background, separated by the red graph line. Premium magazine cover vibe, extremely clean and legible on mobile. --ar 16:9

### Phiên bản 3: Sắc vàng chanh sáng (Lemon Yellow) - Sức ép khổng lồ
> A dramatic chiaroscuro 8K YouTube thumbnail, 16:9 widescreen. The right half of the image is dominated by a giant, shadowed portrait of the Chinese CEO of BYD looking down sternly, with a fleet of grey BYD cars below him. The left half shows a smaller but bright portrait of the Vietnamese billionaire founder of VinFast looking determined, backed by a glowing green grid of 150,000 charging ports. In the middle, a glowing crack of red energy splits the scene. On the left side, massive 3D text reads "BYD PHÁ GIÁ" on the first line in solid bright lemon yellow, and "HÒNG TRIỆT HẠ VINFAST" on the second line in solid pure white, both with a heavy black outline and a deep black drop shadow for maximum mobile readability. High contrast, dark mood. --ar 16:9

### Phiên bản 4: Sắc vàng hổ phách ấm (Amber Yellow) - Cuộc chiến trên xa lộ
> A high-action 8K cinematic YouTube thumbnail, 16:9 widescreen. A nighttime highway scene where a grey BYD electric car is aggressively tailing and trying to cut off an electric cyan VinFast SUV. The VinFast car has a glowing silver "V" logo and is heading towards a bright, illuminated tollgate with V-Green logo in the distance. The overall lighting is dark charcoal with neon red trails from the BYD car and green light from the VinFast. On the left side, a massive bold text overlay reads "BYD PHÁ GIÁ" on the first line in warm amber yellow, and "HÒNG TRIỆT HẠ VINFAST" on the second line in stark solid white, using a heavy geometric sans-serif typeface with a thick sharp black outline, placed over a darkened area of the road. High dynamic range, motion blur. --ar 16:9

### Phiên bản 5: Sắc vàng cát lì (Matte Sand-Gold) - Tranh minh họa báo chí
> A minimalist 8K vector-style illustration for an economic journal, 16:9 widescreen. In a dark slate-blue background, a massive shadow of a dragon-shaped robotic arm painted in red (representing BYD's vertical integration) is reaching down to grab a stylized cyan-teal car representing VinFast. The VinFast car is protected by a solid green shield shape (representing the charging ecosystem). Large, flat 3D typography text overlay on the left reads "BYD PHÁ GIÁ" on the first line in solid matte sand-gold, and "HÒNG TRIỆT HẠ VINFAST" on the second line in solid matte white, both with a thick sharp black drop shadow. Clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, dramatic chiaroscuro lighting, deep noir shadows. --ar 16:9
