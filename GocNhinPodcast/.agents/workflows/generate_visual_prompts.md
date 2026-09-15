---
description: Canonical wrapper for video prompt generation. Relies on `02_templates/visual_storyboard_template.md` to create the global storyboard & Reference Asset Manifest, and `.agents/skills/visual_prompter/SKILL.md` to establish intermediate visual scripts (chapter_XX_visual.md) and dynamic 2D video prompts (prompts_chapter_XX.txt).
---

# Hướng dẫn quy trình Pha 12 — Thiết kế Phân cảnh & Prompt Video (Chuẩn I2V Lean 3-Stage Pipeline)

## 🚨 Cổng xác nhận luồng bắt buộc (Clarification Gate)
*   **BẮT BUỘC:** Trước khi bắt đầu bất kỳ bước nào trong Pha 12/12.5, nếu người dùng chưa nêu rõ yêu cầu là sử dụng luồng **Text-to-Video (T2V)** hay luồng **Image-to-Video (I2V)** cho tập phim/phân cảnh, Agent **bắt buộc phải tạm dừng và hỏi rõ ý kiến của người dùng**, cấm tự ý giả định hay tự động tạo.
*   Quy trình chuẩn mặc định của kênh hiện tại là **I2V Pipeline (Image-to-Image ➔ Video)** tích hợp ảnh tham chiếu của nhân vật biểu tượng qua công cụ `flow_batch_studio`.

---

## 🎬 Giai đoạn 1: Kịch bản Thị giác Tổng thể & Tuyển vai Biểu tượng (Phase 12)

1.  **Thiết kế Kịch bản Thị giác & Tuyển vai Biểu tượng (`visual_storyboard_blueprint.md`):**
    *   Nhập tâm vai trò **Đạo diễn Hình ảnh Kiệt xuất (Master Cinematic Visual Director)**.
    *   Sử dụng biểu mẫu mẫu [visual_storyboard_template.md](file:///02_templates/visual_storyboard_template.md) để viết bản thiết kế.
    *   Chốt rõ các **Mỏ neo thị giác xuyên suốt (Central Visual Anchors)**, **Tuyến di chuyển camera (Directorial Camera Path)**, **Tuyến màu sắc & cảm xúc (Color Arc)**, và **Mạch nối chuyển tiếp giữa các chương (Inter-chapter Visual Bridges)**.
    *   🏛️ **LẬP BẢNG DANH MỤC ẢNH THAM CHIẾU (REFERENCE ASSET MANIFEST):**
        - Rà soát toàn bộ kịch bản để xác định các **nhân vật biểu tượng có sức nặng chính luận/chiến lược** (nguyên thủ quốc gia, lãnh đạo chính phủ, bộ trưởng, thống đốc, CEO tập đoàn, chuyên gia đầu ngành, hoặc hình tượng biểu trưng).
        - **Phân cấp ưu tiên:** Ưu tiên số 1 là **Con người / Lãnh đạo**. Các công trình, địa danh hay kỳ quan thường Nano Banana đã được huấn luyện sẵn nên không bắt buộc phải có ảnh tham chiếu (trừ khi là sản phẩm/máy móc/công trình quá đặc thù).
        - Lập bảng danh mục cụ thể:
          * Tên nhân vật / Thực thể.
          * Vai trò chính luận & Cảm xúc kịch tính mang lại cho phân cảnh.
          * Các phân cảnh xuất hiện (`CHXX_SCYYY`).
          * Tên file mẫu chuẩn theo quy ước: `@tbt_tolam.jpg`, `@thutuongthailan.jpg`, `@ceo_byd_wangchuanfu.jpg`, `@lanhdao_xxx.jpg`...
          * Ghi chú tìm ảnh cho User: tư thế (đứng/ngồi), trang phục (vest/sơ mi/áo bảo hộ), góc nhìn (nhìn thẳng/nghiêng 3/4), sắc thái biểu cảm (điềm tĩnh/nghiêm nghị/tự tin).

2.  **Cổng Duyệt & Nạp Tài Nguyên Người Dùng (Human Ingestion Gate - DỪNG LẠI CHỜ USER):**
    *   Hiển thị toàn bộ **Bảng Danh Mục Ảnh Tham Chiếu (Reference Asset Manifest)** ra màn hình chat.
    *   Yêu cầu Người dùng tìm kiếm ảnh thực tế và lưu vào thư mục `episodes/[slug]/ref_images/` theo đúng tên file đã quy ước (đồng thời kéo thả vào Asset Bin trên giao diện `flow_batch_studio`).
    *   **DỪNG LẠI và chờ Người dùng xác nhận đã nạp đủ ảnh vào thư mục** trước khi bước sang Giai đoạn 2.

---

## ✍️ Giai đoạn 2: Kịch Bản Thị Giác Trung Gian (Pha 12B — `chapter_XX_visual.md`)
*   **Chuyên gia phụ trách:** **`the_scene_architect` (Kiến Trúc Sư Phân Cảnh & Biên Kịch Thị Giác)**.
*   **Tài liệu nạp vào:** `episodes/[slug]/chapter_XX.md` (chỉ nạp đúng chương này) và `visual_storyboard_blueprint.md`.
*   **Nhiệm vụ tối thượng:**
    1. **Bẻ nhịp toán học:** Phân tách thoại thành các phân cảnh $\le 26$ từ, gán ID chuẩn `CHXX_SCYYY`.
    2. **Giải phẫu cơ học 3 tầng (100% Hiện thực đời sống Việt Nam):** Trường `[BỐI CẢNH]` bắt buộc bóc tách rõ:
       - *Chủ thể:* Định danh chính xác nhân vật, đồng phục, dòng xe (VD: tài xế GrabBike áo xanh lá sọc trắng, xe Honda Wave; tài xế GrabCar polo tối màu, xe Vios; xe taxi điện Green SM VF e34, tài xế áo cyan-teal).
       - *Hành động vật lý cụ thể:* Xem điện thoại nhận cuốc, cài quai mũ, bẻ lái, mở cửa xe, quét mã QR, đếm tiền polymer Việt Nam mệnh giá nhỏ (10k, 20k).
       - *Không gian đời thực:* Ngã tư Hà Nội giờ tan tầm mưa phùn, quán trà đá vỉa hè, bàn làm việc công sở Việt Nam cổng thông tin `.gov.vn`. Tuyệt đối CẤM kiến trúc cột đá Hy Lạp/La Mã hoặc phòng xử án Mỹ.
    3. **Khử nhiễm ẩn dụ văn học 100%:** Triệt tiêu mọi từ ngữ tu từ ("không được chia một xu" ➔ ví app trừ tiền/tiền lẻ polymer, CẤM tiền xu `coins`; "tuân thủ/nghiêm khắc" ➔ văn phòng công vụ cổng .gov.vn, CẤM tòa án Mỹ; "cỗ máy" ➔ nhà xưởng/xe cộ đời thực, CẤM bánh răng; "gọng kìm/mỏ neo/bức tường" ➔ bối cảnh thị trường thực tế, CẤM vật thể siêu thực).
    4. **Text Overlay chọn lọc (Selective 20-25%):** Chỉ đặt ở các cảnh then chốt, vị trí góc trái dưới cách đáy 25%.
*   **🛑 CỔNG DUYỆT TRUNG GIAN BẮT BUỘC (INTERMEDIATE APPROVAL GATE):**
    *   Sau khi hoàn thành `chapter_XX_visual.md`, Agent **BẮT BUỘC PHẢI DỪNG LẠI**, in toàn văn ra màn hình chat và **CHỜ USER PHÊ DUYỆT CHÍNH THỨC**.
    *   Tuyệt đối KHÔNG tự ý chuyển sang Pha 12C (viết prompt) khi User chưa chốt duyệt kịch bản trung gian!

---

## 🎨 Giai đoạn 3: Soạn Thảo Prompts I2V (Pha 12C — `prompts_chapter_XX.txt`)
*   **Chuyên gia phụ trách:** **`the_image_prompt_composer` (Nhà Soạn Prompt Hình Ảnh)** dưới sự chỉ đạo của `the_visual_storyteller`.
*   **🛑 CỔNG CÁCH LY THOẠI BẮT BUỘC (ZERO-VOICEOVER ISOLATION GATE):**
    *   Agent **TUYỆT ĐỐI BỊ CẤM NẠP HOẶC ĐỌC KỊCH BẢN THOẠI GỐC `chapter_XX.md`**.
    *   Nguồn dữ liệu DUY NHẤT để dịch sang prompt tiếng Anh là cột `[BỐI CẢNH]` và `[TEXT OVERLAY]` của `chapter_XX_visual.md`.
    *   Chỉ làm nhiệm vụ lắp ghép cú pháp kỹ thuật: lấy nguyên vẹn mô tả từ `[BỐI CẢNH]` chuyển sang tiếng Anh cho dòng `[IMAGE]` và mô tả chuyển động camera/physics cho dòng `[VIDEO]`.
    *   **Nghiêm cấm tuyệt đối:** Không paraphrase, không suy diễn từ câu thoại tiếng Việt, không tự ý thêm thắt các vật thể trừu tượng.

1.  **Quy Chuẩn Định Dạng Cú Pháp Cho `flow_batch_studio`:**
    *   **Quy tắc khoảng cách:**
        - Cùng 1 phân cảnh: Dòng `[IMAGE]` và `[VIDEO]` viết **LIỀN KỀ NHAU** (tuyệt đối KHÔNG có dòng trắng ở giữa).
        - Giữa 2 phân cảnh khác nhau: Cách nhau đúng **1 DÒNG TRỐNG**.
    *   **Trường hợp A: Phân cảnh CÓ ảnh tham chiếu nhân vật/thực thể (`@[ten_anh] ->`):**
        - Dòng `[IMAGE]` áp dụng **Công thức Bảo toàn Diện mạo Trung tính (Zero-Bias Likeness Formula)**:
          ```text
          CHXX_SCYYY [IMAGE]: @[ten_file.jpg] -> A 2D warm cinematic editorial illustration of the person depicted in the reference image, faithfully preserving their exact facial likeness, facial features, bone structure, hairstyle, and attire directly from the reference photo. The subject is [Hành động vật lý & Tư thế cụ thể] inside [Bối cảnh vật lý đời thực]. In the background, [Các yếu tố đồ họa dữ liệu / Bảng biểu / Bản đồ / HUD]. Elegant graphic novel aesthetic, clean bold ink outlines, warm ivory cream ambient tone (#FAF7EE), soft golden daylight streaming in, sophisticated documentary art style, no watermarks, 16:9
          CHXX_SCYYY [VIDEO]: @CHXX_SCYYY.png -> [Camera movement: Slow push-in dolly / Slow pan / Tracking shot] toward the subject, [Ánh sáng dịch chuyển / Tương tác môi trường tinh tế], maintaining their composed facial expression and all details of the reference image exactly, 8-second continuous documentary video --ar 16:9 --dur 8s
          ```
        - *Lưu ý sống còn:* Tuyệt đối KHÔNG đưa tên riêng của người thật vào prompt tiếng Anh để tránh bị bộ lọc an toàn (Safety/Celebrity Filter) của AI từ chối. Dùng cụm từ trung tính `"the person depicted in the reference image"`.
    *   **Trường hợp B: Phân cảnh KHÔNG dùng ảnh tham chiếu (Tạo ảnh mới thuần túy):**
        ```text
        CHXX_SCYYY [IMAGE]: A 2D warm cinematic editorial illustration of [Subject & Physical Action], set in [Real-world Physical Space], minimalist graphic novel aesthetic, clean bold ink outlines, stylized flat vector textures, [sophisticated modern slate background color / warm ivory cream #FAF7EE], luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows[, compact subtle glowing [color] 3D typography text overlay positioned fixedly in the lower-left area of the frame (elevated 25% above the bottom edge), facing camera directly, perfectly horizontal with crisp edges and heavy black drop shadow reading "[TEXT]"], no watermarks, 16:9
        CHXX_SCYYY [VIDEO]: @CHXX_SCYYY.png -> [Steady camera shot / Dynamic Camera move] preserving the 2D vector noir graphic novel aesthetic and clean ink outlines, 8-second continuous documentary video --ar 16:9 --dur 8s
        ```

3.  **Quy chuẩn Typography Bắt Buộc (Selective Lower-Left 25% Rule):**
    *   **Tỷ lệ chọn lọc:** Chỉ xuất hiện ở 20% - 25% phân cảnh then chốt (mốc số liệu, thể chế, sự kiện bước ngoặt). 75% - 80% còn lại bắt buộc ghi `Không`.
    *   **Vị trí & Kích thước:** Thiết kế chữ nhỏ gọn, thanh thoát (`compact subtle`), đặt cố định tại **góc trái màn hình phía dưới, cách mép đáy 25%** (`positioned fixedly in the lower-left area of the frame, elevated 25% above the bottom edge`). CẤM đặt chữ to đùng chính giữa màn hình làm che mất chủ thể.
    *   **Khóa tĩnh chữ ở Video Prompt:** 100% cảnh có chữ thì dòng `[VIDEO]` bắt buộc dùng cú máy tĩnh: `Steady camera shot maintaining perfect focus on the lower-left typography and subject, preserving the 2D vector noir graphic novel aesthetic and clean ink outlines...`

4.  **Quy chuẩn Màu sắc & Ánh sáng Sáng sủa (Luminous High-Clarity Lighting - Không U Ám):**
    *   **Tuyệt đối CẤM phong cách u ám, tối tăm (No Pitch-Black / No Grim Shadowing):** Không dùng các câu lệnh gây đen kịt khung hình như `dramatic chiaroscuro lighting, deep noir shadows` hay nền than đen kịt `#1A1A1A`.
    *   **Ánh sáng chuẩn:** Bắt buộc dùng `luminous high-clarity editorial lighting, crisp clean contours, soft ambient shadows` hoặc `warm ivory cream ambient tone (#FAF7EE), soft golden daylight streaming in`.
    *   **Nền màu thanh lịch:** Dùng các gam màu slate hiện đại (`#2A323D`, `#2C3539`, `#1E293B`) hoặc ngà kem ấm (#FAF7EE) kết hợp điểm nhấn rực rỡ, ấm áp (`#F59E0B`, `#EF5350`).

5.  **Độ Trung Thực Thực Thể & Sản Phẩm (Entity & Product DNA Fidelity):**
    *   Khi phân cảnh nhắc đến sản phẩm, dòng xe, máy móc công nghiệp cụ thể: Bắt buộc nêu rõ tên thương hiệu và model cụ thể kèm đặc điểm nhận diện thiết kế ngoại thất. Nếu là sản phẩm đặc thù chưa phổ biến, đưa vào Reference Asset Manifest để nạp ảnh tham chiếu.

6.  **Kiểm soát chất lượng tự động & Tự sửa lỗi trước khi bàn giao (Automated Quality & Auto-Fix Gate):**
    *   Sau khi viết prompt, Agent bắt buộc phải tự động rà soát qua toàn bộ 7 nhóm lỗi cốt lõi:
        1. *Cú pháp Parser:* 100% dòng `[IMAGE]` và `[VIDEO]` viết liền kề; cách 1 dòng trắng giữa các cảnh; cờ `--ar 16:9 --dur 8s` đầy đủ.
        2. *Chuẩn hóa ID theo chương:* 100% Scene ID phải có định dạng `CHXX_SCYYY` và reset từ `001` cho từng chương.
        3. *Chống Trừu tượng hóa & Ẩn dụ siêu thực (100% Physical Realism):* 100% bối cảnh phải là không gian vật lý đời thực ngoài đời (nhà xưởng, cảng biển, bến tàu, showroom, đường phố, phòng họp, tài liệu). Tuyệt đối CẤM dịch nghĩa bóng thành vật thể siêu thực: cái cân công lý, tấm khiên rạn nứt, vòng kim cô, nút thắt cáp trong hư vô, hố sâu chi phí, bàn tay vô hình.
        4. *Chuẩn hóa Tham chiếu Nhân vật:* Cảnh có nhân vật thật phải dùng cú pháp `@<ten_anh>.jpg -> A 2D warm cinematic editorial illustration of the person depicted in the reference image...`, không để lọt tên riêng gây dính Safety Filter.
        5. *Chống Tây hóa Nhân vật Đời thường:* Các nhân vật quần chúng/kỹ sư/người dân Việt Nam phải có `Vietnamese male/female [vai trò]`. Tuyệt đối không để sót từ chung chung (`an engineer`, `a worker`).
        6. *Khóa tĩnh lớp chữ:* Mọi cảnh có Text Overlay bắt buộc dòng `[VIDEO]` dùng cú máy `Steady camera shot` khóa chữ ở góc dưới trái cách đáy 25%.
        7. *Chuẩn toán học thời lượng & Đồng bộ 1-1:* Đảm bảo 100% câu thoại $\le 26$ từ/cảnh và 100% Scene ID khớp tuyệt đối 1-1 giữa Kịch bản Thị giác (`chapter_XX_visual.md`) và Tệp Prompts (`prompts_chapter_XX.txt`).
        8. *Tuân thủ Tuyệt đối Action Blacklist (Veo 3.1 Lite Safeguards):* Quét sạch 100% các hành động gây lỗi biến dạng: KHÔNG ngón tay bấm điện thoại/đếm tiền, KHÔNG tiếp xúc cơ thể giữa 2 người, KHÔNG người đi bộ trượt chân vào camera, KHÔNG xe rẽ cua/drift/lạng lách, KHÔNG há miệng nói chuyện. Bắt buộc 100% bám theo Action Whitelist (tư thế tĩnh nghỉ, camera điện ảnh slow dolly/pan, chuyển động môi trường khí quyển, cử động vi mô).
    *   **Cổng chặn cứng:** Nếu còn bất kỳ lỗi nào, Agent **BẮT BUỘC PHẢI TỰ SỬA CHỮA XONG 100%** trước khi thông báo hoặc bàn giao cho người dùng.

---

## 🚨 HARD GATE (ANTI-BYPASS) - CỔNG DUYỆT BẮT BUỘC:
- Tuyệt đối **NGHIÊM CẤM** bỏ qua bước tạo `visual_storyboard_blueprint.md` và Bảng Danh Mục Ảnh Tham Chiếu. 
- Khi viết prompt video chi tiết, Visual Prompter bắt buộc phải đọc lại tệp blueprint để lấy cấu trúc mô tả Mỏ neo, màu sắc và chuyển động camera.
- Tổng số lượng phân cảnh trong map bắt buộc phải thỏa mãn:
  $$N_{scenes} \ge \lceil W_{total} / 26 \rceil$$
  để đảm bảo không bị hụt video clips khi ghép nối hậu kỳ.
