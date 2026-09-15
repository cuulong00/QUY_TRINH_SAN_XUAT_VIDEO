# Visual Style Guide — Kênh Đạo & Khoa Học (S-Grade Video Generation)

> **Kênh:** Đạo & Khoa Học — Hiểu cơ chế, ngộ lý Đạo, sống tự tại.
> **Phiên bản:** 2.0 — Cập nhật 18/06/2026 (S-Grade World-Class Video Generation)
> **Áp dụng cho:** Tất cả các phân cảnh video (Video Generation Prompts) trong video long-form.

---

## 🛠️ QUY TRÌNH TẠO MEDIA (Bắt buộc tuân thủ)

### Bước 1: Phân tích Cảnh & Phân nhóm Động (Dynamic AI Grouping)
*   **Không áp dụng bất kỳ quy tắc fix cứng cơ học nào về số lượng câu trên một cảnh.**
*   Mô hình AI tự động đọc và phân tích logic ngữ nghĩa để phân nhóm cảnh trong file `scene_timing_map.json` (Scene Architect).
*   **GIỚI HẠN VEO 3.1:** Thời lượng mỗi phân cảnh (`duration_sec`) tuyệt đối **không được vượt quá 8 giây**.
*   **Quy tắc phân cảnh phụ (Sub-scenes):** Nếu tổng thời lượng cụm thoại cùng ngữ cảnh lớn hơn 8 giây, bắt buộc chia nhỏ thành các phân cảnh phụ nối tiếp nhau: `SC001a`, `SC001b`, `SC001c`... với visual nối tiếp mượt mà.

### Bước 2: Thiết kế Prompt Video S-Grade
*   Mỗi phân cảnh được dịch thành một prompt video 2D phẳng mượt mà dài tối đa 8 giây, kết hợp giữa camera chậm, ẩn dụ vật lý và hệ màu thương hiệu (Visual Prompter).
*   Lưu kết quả vào file `video_prompts.txt` tại thư mục episode.

### Bước 3: Dựng và Ghép Video Thủ Công (Manual CapCut Stitching)
*   Sau khi các clip `.mp4` được sinh ra từ prompt, lưu chúng vào thư mục `videos_final/`.
*   **Không sử dụng script ghép tự động.** Người dựng (Operator) sẽ nhập (import) thủ công các video clip từ `videos_final/` vào phần mềm **CapCut** (hoặc Premiere/DaVinci) để dựng hậu kỳ.
*   Căn chỉnh thời lượng từng phân cảnh khớp hoàn hảo với nhịp điệu của file voiceover đã thu âm.
*   Xuất video base hoàn chỉnh ở định dạng 1080p, 30fps, codec H.264, tỷ lệ 16:9 và lưu vào đường dẫn `video/slideshow_base.mp4` để phục vụ các bước kiểm tra tiếp theo.

---

## 🎨 HỆ MÀU THƯƠNG HIỆU & PHONG CÁCH CHỐT HẠ (60-30-10 Rule)

Tuyệt đối cấm sử dụng các dải màu cầu vồng tự do hoặc cụm từ "vibrant color palette". Chỉ sử dụng công thức phối màu 3 tone:
- **Chủ đạo (60% - Background):** Gam màu tối sâu thẳm: `absolute black background (#0A0A0A)`, `deep midnight blue background`, `dark indigo gradient background`.
- **Bổ trợ (30% - Outlines/Main Subject):** Nét vẽ và chủ thể: `stark white outlines`, `light silver grey vector details`, `solid black silhouette`.
- **Màu nhấn (10% - Key Metaphor):** Chỉ dùng 1 màu nhấn duy nhất để dẫn mắt người xem tùy thuộc ngữ cảnh:
  *   *Khoa học / Thần kinh học / Cơ chế sinh lý:* `glowing electric cyan` (`#00E5FF`).
  *   *Đạo / Triết học / Thiền / Vô vi:* `glowing saffron yellow` (`#FFD600`) hoặc `glowing warm amber` (`#FFAB00`).
  *   *Cảnh báo / Ảo tưởng / Bẫy tâm lý:* `glowing crimson red` (`#FF1744`).

### Phong cách 1: Minimalist Silhouette & Ink Style (Cảm xúc, triết lý, thiền định)
*   **Mô tả:** Nhân vật/chủ thể hiển thị dạng bóng đen tối giản (silhouette) hoặc nét vẽ mực sạch tương phản cao trên phông nền màu gradient tối. Triệt tiêu hoàn toàn chi tiết thừa.
*   **Suffix:** `minimalist graphic novel ink style, high contrast, clean bold outlines, flat colors, [signature color scheme], cinematic lighting, 8-second continuous documentary video --ar 16:9`

### Phong cách 2: Flat Vector & Motion Graphics Style (Số liệu, biểu đồ, quy trình, mô hình thần kinh)
*   **Mô tả:** Đồ họa vector phẳng 2D, đường nét sạch viền đen đậm, màu phẳng không đổ bóng. Phù hợp nhất để chạy biểu đồ, mô hình liên kết thần kinh, quy trình.
*   **Suffix:** `flat 2D vector illustration style, clean bold outlines, flat colors, [signature color scheme], cinematic lighting, 8-second continuous documentary video --ar 16:9`

---

## 🧠 TƯ DUY ẨN DỤ TÂM LÝ & TRIẾT HỌC (Deep Visual Metaphor)

Tuyệt đối cấm mô tả nghĩa đen thô sơ. Hãy chuyển hóa các cơ chế hành vi/trạng thái tinh thần thành các hiện tượng chuyển động vật lý hoặc hình học:
- **Mất kiểm soát ý chí (Dopamine Loop):** Một bóng đen silhouette đang bị cuốn vào một vòng xoáy ốc vector màu đỏ phát sáng thu nhỏ dần.
- **Quan sát chánh niệm (Mindfulness):** Một bóng đen silhouette ngồi thiền tĩnh lặng ở trung tâm, camera từ từ zoom-out ra xa để lộ ra một khoảng không tối giản khổng lồ màu chàm sâu thẳm, với duy nhất một luồng sáng neon cyan chiếu thẳng đứng.

---

## ✍️ QUY CHUẨN ĐỊNH VỊ CHỮ TRÊN MÀN HÌNH (Cinema Typography Layout)

*   **Ngôn ngữ:** Tất cả chữ viết hiển thị trong video **bắt buộc là tiếng Anh không dấu** (`English text`). Tên riêng, địa danh viết không dấu.
*   **Bố cục & Vị trí:** Phải định vị tọa độ hiển thị rõ ràng trong prompt để AI vẽ đúng vị trí, tránh đè lên chủ thể:
    *   `aligned to the bottom-right corner`
    *   `centered in the upper third`
    *   `displayed on a clean digital card on the left side`
*   **Mô tả chữ:** `the English text "EGO" displaying in a clean bold minimal sans-serif font with a subtle neon glow`.

---

## 🎥 CHUYỂN ĐỘNG & CAMERA TRONG PROMPT VIDEO
*   Mô tả chuyển động mượt mà, tốc độ chậm rãi của vật thể/chủ thể trong video (ví dụ: "a neural path slowly lighting up", "a silhouette walking forward in slow motion"). Hành động phải đơn giản và hoàn thành tự nhiên trong vòng 8 giây.
*   Sử dụng chuyển động camera chuyên nghiệp: `slow camera panning`, `subtle slow zoom-in`, `subtle slow zoom-out`, `steady shot`, `subtle slow pan right/left`.

---

## 🔒 QUY TẮC PHÒNG TRÁNH LỖI CHÍNH SÁCH AI (Safety & Policy Rules)
*   **TUYỆT ĐỐI KHÔNG** đưa tên người thật còn sống (ví dụ "Elon Musk") hoặc các tác giả/nhà sáng lập lịch sử (ví dụ "Napoleon Hill", "Thomas Edison", "Socrates") trực tiếp vào prompt để tránh bị AI chặn.
*   **Thay thế bằng danh từ mô tả chung:** "a visionary tech billionaire in a suit", "a legendary self-help author", "a Greek philosopher in a toga", "an American president".
*   Quy tắc này giúp lách qua bộ lọc An toàn (Safety Filter) cực kỳ nghiêm ngặt của các mô hình AI Video lớn như Google Veo 3.1.
