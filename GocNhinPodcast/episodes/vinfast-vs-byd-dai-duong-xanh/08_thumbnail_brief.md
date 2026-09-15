# Kế hoạch Thiết kế Thumbnail — VINFAST / BYD CHỈ LÀ CÁI TÊN (Đồng bộ Nhận diện Thương hiệu)

Tài liệu này định hình headline, cấu trúc thiết kế và 5 phiên bản prompt tạo ảnh YouTube Thumbnail phục vụ A/B testing tối ưu CTR cho tập phim "VinFast vs BYD: Đại Dương Xanh".

*   **Tiêu đề Video dự kiến:** VinFast vs BYD: Đại Dương Xanh - Chiến Lược Con Tắc Kè và Hệ Sinh Thái Năng Lượng
*   **Headline Chốt trên Thumbnail (Đồng bộ chuẩn nhận diện):** 
    *   Dòng 1: `VinFast` (màu vàng cam gradient, viết hoa chữ V và F theo đúng thương hiệu)
    *   Dòng 2: `BYD CHỈ LÀ CÁI TÊN` (màu trắng tuyền, viết hoa toàn bộ chữ BYD và chữ Việt có dấu)

---

## 🎨 Phân tích Ý tưởng Mỹ thuật (Tư duy Visual Hook Director)

Dựa trên mẫu tham chiếu `Generated Image July 13, 2026 - 3_40PM.jpg` và triết lý thiết kế của kênh:
1.  **Bảng màu & Cấu trúc chữ thương hiệu:** 
    *   Dòng 1 "VinFast" sử dụng sắc cam-vàng lửa gradient rực rỡ (`#FFD600` loang dần sang `#FF5722`). Chữ viết đúng chính tả thương hiệu: chữ V viết hoa, chữ F viết hoa, các chữ còn lại viết thường.
    *   Dòng 2 "BYD CHỈ LÀ CÁI TÊN" dùng màu trắng tuyền đặc (`#FFFFFF`). Chữ BYD viết hoa toàn bộ.
    *   Toàn bộ chữ có viền đen sắc nét cực dày (`thick sharp black outline`) và bóng đổ đen đậm (`heavy black drop-shadow`) để hiển thị cực tốt trên di động.
2.  **Bố cục & Chủ thể:** Bố cục đối xứng kịch tính (Split-screen).
    *   **Bên trái (Đại diện VinFast):** Chân dung tỷ phú Phạm Nhật Vượng (diện vest đen, cà vạt đỏ, thần thái tự tin, điềm tĩnh). Phía sau ông là 2 chiếc xe điện VinFast màu xanh lục bảo/teal-cyan (mẫu SUV VF8/VF9 đại diện cho dòng xe Lạc Hồng) có logo chữ "V" bạc trên lưới tản nhiệt.
    *   **Bên phải (Đại diện BYD):** Chân dung CEO BYD Wang Chuanfu (diện vest đen, cà vạt xanh navy, thần thái sắc sảo, nghiêm nghị). Phía sau ông là 1 chiếc sedan điện BYD Seal màu xám có logo "BYD" ở mũi xe.
    *   **Ranh giới chia đôi:** Một vệt sáng phân cách đứng ở giữa (gradient chuyển từ xanh ngọc turquoise của VinFast sang đỏ crimson của BYD). Hậu cảnh bao trùm là lửa đỏ và tàn lửa bắn tung tóe đại diện cho đại dương đỏ khốc liệt.

---

## 📦 5 Phiên bản Prompt Tạo ảnh cho NanoBanana 2.0 (Midjourney/Imagen)

Mỗi prompt được thiết kế dạng văn xuôi liên tục 16:9 gốc, chỉ định rõ case chữ và kết cấu vật lý của text overlay.

### Phiên bản 1: Chuẩn Brand GocNhinPodcast (Split-screen Đối xứng)
> A dramatic 8K cinematic YouTube thumbnail in 16:9 widescreen format, featuring a split-screen composition. On the left side, a realistic portrait of a prominent Vietnamese billionaire with Asian features, wearing a sharp business suit with a red tie, looking confident and calm. Behind him, two sleek electric SUVs painted in vibrant electric cyan-teal color, showing the silver metallic VinFast "V" logo on their front grilles. On the right side, a realistic portrait of the Chinese billionaire CEO of BYD, Wang Chuanfu, wearing a sharp dark suit with a navy tie, looking serious. Behind him, one sleek grey BYD electric sedan with the official BYD logo on the front. The background is filled with deep noir shadows, intense red-orange flames and flying orange sparks. In the upper center, a massive, highly legible 3D typography text overlay reads the brand name "VinFast" on the first line in a gradient of bright yellow and fire orange, written in its custom sleek geometric sans-serif typeface with capital letter "V" and capital letter "F" and all other letters in lowercase, and "BYD CHỈ LÀ CÁI TÊN" on the second line in solid clean white, with the word "BYD" in all-uppercase letters and the Vietnamese text with proper accents, both rendered with a thick sharp black outline and a heavy black drop-shadow. No neon text, no blurred card backgrounds, 8K resolution, high contrast, dramatic studio lighting. --ar 16:9

### Phiên bản 2: Cyber-Minimalism (Trực diện Tương lai)
> A minimalist yet high-impact 8K cinematic YouTube thumbnail, 16:9 widescreen. In the dark warm charcoal background, two powerful Asian billionaire CEOs in business suits stand facing each other in profile: the Vietnamese founder of VinFast on the left and the founder of BYD on the right. In the center between them, two cyan-teal electric cars with silver VinFast "V" logos face a single grey BYD electric sedan under intense spotlights. Neon light trails of turquoise and crimson slice through the dark empty space. Large, bold 3D metallic text overlay reading the brand name "VinFast" on the first line in glossy yellow-gold metal, with capital letter "V" and capital letter "F" and all other letters in lowercase in its custom sleek geometric typeface, and "BYD CHỈ LÀ CÁI TÊN" on the second line in brushed white steel, with "BYD" in all-uppercase and the Vietnamese text with proper accents, placed on the left side with a thick crisp black outline and a heavy black drop-shadow. Chiaroscuro lighting, deep noir shadows, hyper-realistic, extremely clean and legible on mobile. --ar 16:9

### Phiên bản 3: Economic Editorial Cover (Bìa Tạp chí Phóng sự)
> An editorial-style 8K YouTube thumbnail in 16:9 widescreen format. The background is a clean, dark slate-grey world map graphic with glowing red and cyan data points. In the foreground, a detailed portrait of the Vietnamese billionaire founder of VinFast on the left, and the BYD CEO Wang Chuanfu on the right, both looking forward. At their feet, two sleek VinFast teal-cyan electric cars and one grey BYD car are arranged in a dynamic overlapping layout. On the left side, a heavy, flat-designed typography overlay reads the brand name "VinFast" on the first line in solid warning orange, with capital letter "V" and capital letter "F" and all other letters in lowercase, and "BYD CHỈ LÀ CÁI TÊN" on the second line in solid white, with the word "BYD" in all-uppercase and the Vietnamese text with proper accents, using a heavy geometric sans-serif typeface with a thick black drop shadow for maximum mobile readability. Premium magazine cover aesthetic, high contrast, clean shapes, no cartoon, no messy details. --ar 16:9

### Phiên bản 4: Dramatic Chiaroscuro (Tương phản Vùng tối)
> A dramatic chiaroscuro 8K YouTube thumbnail, 16:9 widescreen. The composition is heavily shadowed, with single key lights illuminating the facial features of the Vietnamese founder of VinFast on the left and the Chinese CEO of BYD on the right. Below them, two glowing cyan-teal VinFast cars and one grey BYD car emerge from the deep noir shadows. Gold sparks drift through the air. A massive text overlay in the upper third reads the brand name "VinFast" on the first line in a glowing solid yellow color, with capital letter "V" and capital letter "F" and all other letters in lowercase, and "BYD CHỈ LÀ CÁI TÊN" on the second line in solid pure white, with the word "BYD" in all-uppercase and the Vietnamese text with proper accents, both with a heavy black outline and a deep black drop shadow. Extremely high legibility at small sizes, bold and clean, dramatic dark mood. --ar 16:9

### Phiên bản 5: High-speed Highway Battle (Cuộc rượt đuổi trên Cao tốc)
> A high-action 8K cinematic YouTube thumbnail, 16:9 widescreen. A nighttime highway battle scene where two electric cyan-teal VinFast cars with glowing silver "V" logos are flanking and overtaking a single grey BYD electric car. In the sky above, transparent ghost-like portraits of the Vietnamese billionaire founder of VinFast on the left and the BYD CEO on the right look down onto the highway with intense focus. Massive bold text overlay reading the brand name "VinFast" on the first line in vibrant fire orange, with capital letter "V" and capital letter "F" and all other letters in lowercase in its custom sleek geometric typeface, and "BYD CHỈ LÀ CÁI TÊN" on the second line in stark solid white, with the word "BYD" in all-uppercase and the Vietnamese text with proper accents, using a heavy blocky sans-serif font with a thick sharp black outline, positioned on the left side over a darkened area of the road. High dynamic range, motion blur on the road, dramatic headlights, intense red and blue rim lighting. --ar 16:9
