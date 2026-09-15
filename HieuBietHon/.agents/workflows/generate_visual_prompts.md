---
description: Canonical wrapper for video prompt generation. Relies on the `.agents/skills/scene_timing_builder/SKILL.md` to map script to grouped scenes first, then uses `02_templates/visual_storyboard_template.md` to create the global storyboard, and finally `.agents/skills/visual_prompter/SKILL.md` to establish dynamic 2D video prompts.
---

# Hướng dẫn quy trình Pha 12 — Thiết kế Phân cảnh & Prompt Video

## 🚨 Cổng xác nhận luồng bắt buộc (Clarification Gate)
*   **BẮT BUỘC:** Trước khi bắt đầu bất kỳ bước nào trong Pha 12/12.5, nếu người dùng chưa nêu rõ yêu cầu là sử dụng luồng **Text-to-Video (T2V)** hay luồng **Image-to-Video (I2V)** cho tập phim/phân cảnh, Agent **bắt buộc phải tạm dừng và hỏi rõ ý kiến của người dùng**, cấm tự ý giả định hay tự động tạo.

## 🎬 Giai đoạn 1: Bản đồ Phân cảnh & Kịch bản Thị giác Tổng thể (Phase 12)
1.  **Tạo Bản đồ Phân cảnh (`scene_timing_map.json`):**
    *   Sử dụng kỹ năng [scene-timing-builder](file:///.agents/skills/scene_timing_builder/SKILL.md) để phân tích kịch bản thoại và phân nhóm cảnh.
    *   **Áp dụng Giao thức Đồng bộ Toán học:** Đảm bảo tối đa 28 từ thoại tiếng Việt cho mỗi phân cảnh (tương ứng video clip 8s của Google Veo 3.1 ở tốc độ 3.58 từ/giây). Phân chia và phân phối các câu thoại đều đặn vào các phân cảnh phụ.
2.  **Thiết kế Kịch bản Thị giác (`visual_storyboard_blueprint.md`):**
    *   Sử dụng biểu mẫu mẫu [visual_storyboard_template.md](file:///02_templates/visual_storyboard_template.md) để viết bản thiết kế.
    *   Chốt rõ các **Mỏ neo thị giác xuyên suốt (Central Visual Anchors)**, **Tuyến di chuyển camera (Directorial Camera Path)**, **Tuyến màu sắc & cảm xúc (Color Arc)**, và **Mạch nối chuyển tiếp giữa các chương (Inter-chapter Visual Bridges)**.
3.  **Duyệt bản thảo (Human Approval Gate):**
    *   Dừng lại trình cho người dùng duyệt bản thảo `visual_storyboard_blueprint.md` trước khi tiến hành viết prompt chi tiết.

## ✍️ Giai đoạn 2: Tạo Prompt theo từng chương (Phase 12.5 - Chapter-Isolated Prompts)
1.  **Tạo tệp Prompt cho Từng Chương (`prompts_chapter_XX.txt`):**
    *   **🛑 CHUNKING GATE (CHỐNG TRÀN NGỮ CẢNH):** Nghiêm cấm gộp chung toàn bộ các chương vào một tệp. Khi viết prompt cho Chương XX, Agent **chỉ được phép nạp kịch bản thoại của Chương XX đó** cùng với `visual_storyboard_blueprint.md`. Không đọc kịch bản của các chương khác.
    *   Tất cả prompt ảnh tĩnh và chuyển động video bắt buộc được viết trong tệp riêng biệt cho từng chương, đặt tại `episodes/[slug]/prompts_chapter_XX.txt` (VD: `prompts_chapter_01.txt`).
    *   Mỗi phân cảnh triển khai theo cấu trúc:
        ```text
        CHXX_SCYYY [IMAGE]: A flat 2D vector illustration of... , clean bold outlines, flat colors, in a minimalist graphic novel aesthetic, dramatic chiaroscuro lighting, deep noir shadows
        CHXX_SCYYY [VIDEO]: @CHXX_SCYYY.png -> [Camera move] preserving the details of the reference image, 8-second continuous documentary video --ar 16:9
        ```
    *   **NGHIÊM CẤM CHẠY BATCH HÀNG LOẠT:** AI bắt buộc viết prompt tuần tự (Stateful Flow) để giữ mạch nối camera mượt mà, bám sát cốt truyện xuyên suốt và tránh rời rạc phân cảnh.
2.  **Kiểm soát chất lượng tự động & Tự sửa lỗi trước khi bàn giao (Automated Quality & Auto-Fix Gate):**
    *   **Quy tắc Không bàn giao sản phẩm lỗi (Zero-Defect Delivery Rule):** Sau khi viết prompt, Agent bắt buộc phải tự động rà soát qua toàn bộ 5 nhóm lỗi cốt lõi:
        1. *Chống Tây hóa Nhân vật:* Kiểm tra 100% bối cảnh Việt Nam có nhân vật phải có `Vietnamese male/female [vai trò]`. Tuyệt đối không để sót từ chung chung (`an engineer`, `a worker`). Nếu có ➡️ **Sửa lại ngay**.
        2. *Chống Trừu tượng hóa & Siêu thực:* 100% bối cảnh là không gian vật lý thật. Cấm toàn bộ biểu tượng siêu thực (cái cân bay, bàn tay thép, cơn mưa tiền) ➡️ **Sửa lại thành hành động vật lý đời thực ngay**.
        3. *Khóa tĩnh lớp chữ:* Mọi cảnh có Text Overlay bắt buộc dòng `[VIDEO]` dùng cú máy `Steady camera shot` và câu lệnh khóa chữ chống méo font.
        4. *Chuẩn toán học thời lượng:* Đảm bảo 100% câu thoại $\le 26$ từ/cảnh.
        5. *Đồng bộ 1-1:* 100% Scene ID khớp tuyệt đối giữa Visual Script và Prompts File.
    *   Bắt buộc chạy script kiểm tra chất lượng chống lặp và chống cụm từ rác cho TỪNG tệp prompt:
        `python3 scripts/check_boilerplate.py episodes/[slug]/prompts_chapter_XX.txt`
    *   **Cổng chặn cứng:** Nếu script báo `FAILED` hoặc còn bất kỳ lỗi nào ở 5 bước trên, Agent **BẮT BUỘC PHẢI TỰ SỬA CHỮA XONG 100%** trước khi thông báo hoặc bàn giao cho người dùng.



---

## 🚨 HARD GATE (ANTI-BYPASS) - CỔNG DUYỆT BẮT BUỘC:
- Tuyệt đối **NGHIÊM CẤM** bỏ qua bước tạo `visual_storyboard_blueprint.md`. 
- Khi viết prompt video chi tiết, Visual Prompter bắt buộc phải đọc lại tệp blueprint để lấy cấu trúc mô tả Mỏ neo, màu sắc và chuyển động camera.
- Tổng số lượng phân cảnh trong map bắt buộc phải thỏa mãn:
  $$N_{scenes} \ge \lceil W_{total} / 28 \rceil$$
  để đảm bảo không bị hụt video clips khi ghép nối hậu kỳ.
