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

## ✍️ Giai đoạn 2: Tạo Prompt Video Trực Tiếp Theo Chương (Phase 12.5)
1.  **Thiết lập tệp tin đầu ra:**
    *   Mỗi chương $XX$ sẽ có duy nhất một tệp tin **`prompts_chXX.txt`** chứa toàn bộ các prompt Text-to-Video (T2V) trực tiếp của chương đó.
2.  **Sinh Prompt Video tuần tự (Stateful Flow):**
    *   Sử dụng thông tin của `visual_storyboard_blueprint.md` + Nội dung kịch bản chương tương ứng.
    *   **NGHIÊM CẤM CHẠY BATCH HÀNG LOẠT:** AI bắt buộc viết prompt tuần tự từng phân cảnh theo dòng chảy (Stateful Flow) để giữ mạch nối camera mượt mà, bám sát cốt truyện xuyên suốt và tránh rời rạc phân cảnh.
    *   Cú pháp bắt buộc cho từng dòng:
        `CHXX_SCYYY: [Prompt T2V 5 lớp: Camera Movement + Chủ thể đồ họa 2D + Chuyển động vật lý + Bối cảnh tối giản + Màu sắc/Ánh sáng], cinematic editorial illustration style, minimalist graphic novel aesthetic, clean ink outlines, dramatic chiaroscuro lighting, deep noir shadows, highly detailed atmospheric background, 8-second continuous documentary video --ar 16:9`
3.  **Kiểm soát chất lượng tự động (Automated Quality Gate):**
    *   Bắt buộc chạy script kiểm tra chất lượng chống lặp và chống cụm từ rác:
        `python3 scripts/check_boilerplate.py episodes/[slug]/prompts_chXX.txt`
    *   **Cổng chặn cứng:** Nếu script báo `FAILED` (do tỷ lệ cụm từ rác > 10%, lỗi mạch nối camera hoặc lỗi ID không khớp), Agent bắt buộc phải viết lại hoặc tinh chỉnh các prompt bị lỗi trước khi tiến hành bàn giao.

---

## 🚨 HARD GATE (ANTI-BYPASS) - CỔNG DUYỆT BẮT BUỘC:
- Tuyệt đối **NGHIÊM CẤM** bỏ qua bước tạo `visual_storyboard_blueprint.md`. 
- Khi viết prompt video chi tiết, Visual Prompter bắt buộc phải đọc lại tệp blueprint để lấy cấu trúc mô tả Mỏ neo, màu sắc và chuyển động camera.
- Tổng số lượng phân cảnh trong map bắt buộc phải thỏa mãn:
  $$N_{scenes} \ge \lceil W_{total} / 26 \rceil$$
  để đảm bảo không bị hụt video clips khi ghép nối hậu kỳ.
