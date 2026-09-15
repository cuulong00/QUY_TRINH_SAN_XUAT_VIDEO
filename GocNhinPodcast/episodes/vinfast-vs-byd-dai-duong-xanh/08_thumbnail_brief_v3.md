# Kế hoạch Thiết kế Thumbnail V3 — BYD PHÁ GIÁ / TRIỆT HẠ VINFAST (Không banner phụ)

Tài liệu này định hình headline, cấu trúc thiết kế và 5 phiên bản prompt tạo ảnh YouTube Thumbnail phiên bản V3 phục vụ A/B testing tối ưu CTR cho tập phim "VinFast vs BYD: Đại Dương Xanh". Phiên bản này tham chiếu chặt chẽ bố cục mỹ thuật của tệp ảnh gốc [Generated Image July 13, 2026 - 3_40PM.jpg](file:///Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/vinfast-vs-byd-dai-duong-xanh/Generated Image July 13, 2026 - 3_40PM.jpg) nhưng rút ngắn tiêu đề và loại bỏ hoàn toàn dải banner phụ ở chân để bố cục thoáng đãng, tập trung tối đa vào chủ thể.

*   **Tiêu đề Video dự kiến:** VinFast vs BYD: Bản chất cuộc đấu không nằm ở chiếc xe
*   **Headline Chốt trên Thumbnail V3 (Rút ngắn & Tối giản):** 
    *   Dòng 1: `BYD PHÁ GIÁ` (màu vàng-cam gradient rực rỡ như ảnh gốc)
    *   Dòng 2: `TRIỆT HẠ VINFAST` (màu trắng tuyền, thay thế cho cụm từ "HÒNG ĐÈ BẸP VINFAST" để ngắn gọn và trực diện hơn)
    *   *(Đã loại bỏ hoàn toàn dải banner "ĐÔNG NAM Á RẤT CĂNG THẲNG" ở chân ảnh)*

---

## 🎨 Phân tích Ý tưởng Mỹ thuật V3 (Tối giản hóa từ ảnh tham chiếu)

Kế thừa trọn vẹn bố cục đã được kết xuất thành công trong tệp ảnh gốc, loại bỏ banner chân:
1.  **Bố cục đối xứng kịch tính (Split-screen):**
    *   Không gian được chia đôi bằng một vạch sáng mờ thẳng đứng màu cam-đỏ ở chính giữa.
    *   **Phần bên trái (VinFast):** Chân dung cận cảnh ông Phạm Nhật Vượng diện vest đen, sơ mi trắng, cà vạt đỏ hoa văn với vẻ mặt điềm tĩnh, tự tin. Phía sau ông là chiếc SUV VinFast VF8 màu xanh dương đậm (blue). Hậu cảnh là ngọn lửa cháy rực rỡ màu vàng-cam.
    *   **Phần bên phải (BYD):** Chân dung cận cảnh ông Wang Chuanfu đeo kính, diện vest đen, sơ mi trắng, cà vạt xanh chấm bi với vẻ mặt nghiêm nghị. Phía sau ông là chiếc sedan BYD Seal màu xám xanh. Hậu cảnh cũng là ngọn lửa cháy đỏ rực cùng tàn lửa bay.
2.  **Hệ thống Logo thương hiệu:**
    *   Góc trên bên trái: Logo chữ "V" bạc đặc trưng của VinFast với chữ "VINFAST" màu trắng ngay phía dưới.
    *   Góc trên bên phải: Logo chữ "BYD" màu trắng đặt trong khung hình elip nằm ngang của hãng.
3.  **Typography & Hiệu ứng chữ:**
    *   Dòng 1 "BYD PHÁ GIÁ" sử dụng sắc vàng-cam gradient lửa rực rỡ.
    *   Dòng 2 "TRIỆT HẠ VINFAST" sử dụng màu trắng tuyền đặc.
    *   Cả hai dòng đều dùng font sans-serif cực đậm, viết hoa toàn bộ, có viền đen sắc nét cực dày (`thick sharp black outline`) và bóng đổ đen đậm (`heavy black drop-shadow`), đứng tự do ở phần trên của ảnh.

---

## 📦 5 Phiên bản Prompt Tạo ảnh cho NanoBanana 2.0 (Midjourney/Imagen)

Các prompt dưới đây sử dụng kỹ thuật mô tả trực quan chi tiết để tái tạo lại cấu trúc của ảnh tham chiếu, thay đổi tiêu đề chữ và loại bỏ banner chân.

### Phiên bản 1: Bản sao hoàn hảo tối giản (Chỉ đổi chữ, không banner)
> A dramatic 8K cinematic YouTube thumbnail in 16:9 widescreen format, featuring a split-screen composition divided by a vertical red-orange light beam in the center. On the left side, a realistic portrait of the Vietnamese billionaire founder of VinFast with Asian features, wearing a black suit with a red patterned tie, looking calm. Behind him is a blue VinFast VF8 SUV against intense yellow-orange flames. On the right side, a realistic portrait of the Chinese CEO of BYD, Wang Chuanfu, wearing glasses and a dark suit with a navy dotted tie, looking serious. Behind him is a grey-blue BYD Seal sedan against red-orange flames. In the upper-left corner, the silver "V" VinFast logo with white text "VINFAST" below it. In the upper-right corner, the white oval "BYD" logo. A massive 3D text overlay is placed in the upper center, reading "BYD PHÁ GIÁ" on the first line in a gradient of bright yellow and fire orange, and "TRIỆT HẠ VINFAST" on the second line in solid white, using a heavy geometric sans-serif typeface with a thick sharp black outline and heavy black drop shadow. No bottom banner, no text at the bottom. --ar 16:9

### Phiên bản 2: Tăng cường tương phản và tàn lửa (Cinematic Noir, không banner)
> A highly dramatic 8K cinematic YouTube thumbnail, 16:9 widescreen. Split-screen layout divided by a vertical glowing orange line. On the left: close-up portrait of the Vietnamese founder of VinFast looking calm in a dark suit with a red tie; behind him is a glossy electric-blue VinFast VF8 SUV and raging gold flames. On the right: close-up portrait of the glasses-wearing BYD CEO looking serious; behind him is a grey BYD Seal sedan and deep red flames with glowing embers flying. Left upper corner displays silver VinFast logo; right upper corner displays white BYD logo. Massive, highly legible 3D typography in the upper third reading "BYD PHÁ GIÁ" on the first line in electric yellow-to-orange gradient, and "TRIỆT HẠ VINFAST" on the second line in clean solid white, both with heavy black outlines and deep drop shadows. Clear and clean bottom with no banners or text. High contrast, cinematic studio lighting. --ar 16:9

### Phiên bản 3: Phong cách đồ họa phẳng (2D Flat Graphic Novel, không banner)
> A 2D flat vector-style editorial illustration in 16:9 widescreen format, based on a split-screen layout. On the left side, a minimalist vector portrait of the Vietnamese founder of VinFast with a blue SUV and stylized yellow fire. On the right side, a vector portrait of the Chinese CEO of BYD with a grey sedan and stylized red fire. In the upper center, bold flat 3D text reads "BYD PHÁ GIÁ" on the first line in a bright yellow-to-orange gradient, and "TRIỆT HẠ VINFAST" on the second line in solid white, using a heavy blocky sans-serif font with a thick sharp black outline. Muted colors, strong outlines, dramatic chiaroscuro shadows, high legibility. No text or banners at the bottom. --ar 16:9

### Phiên bản 4: Góc nghiêng đối đầu kịch tính (Dynamic Clash, không banner)
> A dynamic 8K cinematic YouTube thumbnail, 16:9 widescreen. A split-screen composition where the camera is slightly angled. On the left, the calm Vietnamese founder of VinFast looking towards the center, with his blue VF8 SUV angled forward. On the right, the serious Chinese CEO of BYD looking towards the center, with his grey BYD Seal angled forward. A glowing crack of orange energy separates them. Silver VinFast logo on top-left, white BYD logo on top-right. Massive text overlay reading "BYD PHÁ GIÁ" on the first line in bright fire-yellow gradient, and "TRIỆT HẠ VINFAST" on the second line in stark white, with a thick black outline and deep drop shadow. No banners, clean bottom area. Dynamic action feel, sparks flying, high contrast. --ar 16:9

### Phiên bản 5: Chiaroscuro Vùng tối (Dramatic Shadow Focus, không banner)
> A dramatic chiaroscuro 8K YouTube thumbnail, 16:9 widescreen. The scene is cast in deep noir shadows, with bright rim lighting outlining the profiles of the Vietnamese billionaire on the left and the Chinese CEO on the right. In the center, a blue VinFast SUV and a grey BYD sedan are partially lit by the orange glow of a vertical flame divider. Silver VinFast logo on the top-left, white BYD logo on the top-right. The bold typography overlay reads "BYD PHÁ GIÁ" on the first line in glossy yellow-orange gradient, and "TRIỆT HẠ VINFAST" on the second line in solid pure white, both with heavy black outlines and deep drop shadows. No bottom text or horizontal bars. Extreme mobile legibility, premium dark cinematic mood. --ar 16:9
