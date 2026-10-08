---
description: Flagship workflow for I2V+ Multimodal Hybrid Visual Production Pipeline on X-Economic. Combines Real-world Fair-Use B-Roll, Forensic Callout (Clean Press & Archives), Macro Data & Map Infographics, and AI cinematic video based on narrative beat architecture and cognitive ontology.
---

> 🧭 **Cổng vào:** Xem `.agents/phases/pha_12_14_san_xuat.md`. Toàn bộ quy trình này tuân thủ nghiêm ngặt **Hợp đồng chung**: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_nhip_y.md` và skill dẫn đường: `.agents/skills/visual_prompter_plus/SKILL.md`.

# Hướng Dẫn Quy Trình Pha 12+ — Thiết Kế Phân Cảnh Thị Giác Theo Nhịp Ý (I2V+ Pipeline)

## 📌 Tổng Quan & Triết Lý Đạo Diễn

Quy trình **I2V+** của kênh **X-Economy** được vận hành trên nguyên tắc **Nhịp Ý (Narrative Beat)**:
1. **Đơn vị phân tích cơ sở là Nhịp Ý (Beat):** Mỗi nhịp là một đơn vị suy nghĩ trọn vẹn (khoảng 30–100 từ, tương đương 8–30 giây thoại theo tốc độ đọc 223–235 từ/phút của kênh). Tuyệt đối không dùng câu văn hay trần số từ cơ học làm đơn vị phân cảnh.
2. **Một nhịp có từ 1 đến 4 shot:** Số lượng shot phụ thuộc vào nhu cầu nhận thức của khán giả và thời lượng nói, không xoay vòng quota máy móc.
3. **5 loại shot bản thể luận:**
   - `BROLL`: Tư liệu thực tế ngoài đời, tư liệu lưu trữ lịch sử, thời sự chính thống, hiện trường công nghiệp, đại công trường (tối thiểu 5 giây/shot, chuẩn 5.5s–7.0s).
   - `BAO_CHI`: Bằng chứng bài báo thật, tài liệu lưu trữ, văn kiện, hiệp định pháp lý thật có highlight/zoom vào luận điểm.
   - `INFOGRAPHIC_TINH`: Thẻ đồ họa tĩnh hiển thị số liệu, bảng biểu đối chiếu hoặc bản đồ địa chính trị rõ ràng.
   - `INFOGRAPHIC_DONG`: Sơ đồ động hiện dần theo mạch phân tích thể chế, luồng hàng hải, dòng vốn hoặc cơ cấu vĩ mô.
   - `VIDEO_AI`: Tái hiện bối cảnh lịch sử xưa cũ không có camera, phòng họp cơ mật, đại cảnh sử thi hoặc không gian nội tâm.
4. **Quy tắc số liệu thép:** Mọi con số xuất hiện trên màn hình BẮT BUỘC phải được nhắc tới trong lời thoại của nhịp và có mã claim kiểm chứng trong sổ kiểm định. Tuyệt đối không tự bịa thêm số liệu để trang trí.

---

## 🎬 Giai Đoạn 1: Lập Blueprint Đa Thức Tổng Thể (Pha 12+A — `visual_storyboard_blueprint_plus.md`)
* **Chuyên gia phụ trách:** **`the_visual_storyteller`**.
* **Kỹ năng dẫn đường:** `.agents/skills/visual_prompter_plus/SKILL.md` và `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_nhip_y.md`.
* **Tài liệu nạp vào:** Các tệp kịch bản chương `episodes/[slug]/chapter_XX.md` (đọc toàn bộ các chương để nắm tổng thể; **tuyệt đối không đọc `voiceover.md`**), `07_outline.md`, biểu mẫu `02_templates/visual_storyboard_plus_template.md`.
* **Nhiệm vụ cốt lõi:**
  1. Xác định vũ trụ thị giác và bảng màu nhận diện 60-30-10 của tập phim (`#FAF7EE`, Slate `#1E293B`, `#2A323D`, Obsidian `#080C14`, Hổ phách `#F59E0B`, Cyan `#00C2CB`).
  2. Xác định bối cảnh địa lý nơi câu chuyện thực tế diễn ra để chỉ đạo tạo hình nhân vật và không gian chính xác theo niên đại lịch sử.
  3. Lập danh sách ảnh tham chiếu nhân vật (`ref_images/`) nếu có nhân vật lịch sử hoặc chính khách cụ thể.
  4. Xác định trọng tâm nhận thức và cao trào thị giác của từng chương.

---

## ✍️ Giai Đoạn 2: Bản Đồ Nhịp Ý Từng Chương (Pha 12+B — `chapter_XX_ban_do_nhip.md`)
* **Chuyên gia phụ trách:** **`the_scene_architect`** phối hợp cùng **`the_footage_hunter`**.
* **Kỹ năng dẫn đường:** `.agents/skills/visual_prompter_plus/SKILL.md`.
* **Tài liệu nạp vào:** `episodes/[slug]/chapter_XX.md` (chỉ nạp chương đang làm) và `visual_storyboard_blueprint_plus.md`.
* **Quy trình 6 bước thực thi:**
  - **Bước 1 (Đọc trọn văn bản chương):** Nắm mạch lập luận, cảm xúc và cấu trúc các luận điểm.
  - **Bước 2 (Bẻ nhịp ý):** Chia chương thành các nhịp ý trọn vẹn (`CHXX_N01`, `CHXX_N02`,...). Mỗi nhịp gồm các câu thoại mang cùng một ý nghĩ, gán ý tóm tắt và tính thời lượng ước tính.
  - **Bước 3 (Đặt câu hỏi nhận thức):** Với nhịp này, khán giả cần thấy gì để hiểu bản chất và tin vào lập luận?
  - **Bước 4 (Chọn loại shot):** Áp dụng cây quyết định 5 loại shot bản thể luận. Phân bổ từ 1 đến 4 shot cho mỗi nhịp theo đúng bảng 11 trường hợp trong hợp đồng.
  - **Bước 5 (Viết 4 file track song song bằng tay):**
    - `chapter_XX_broll.md`: Ghi rõ từ khóa tìm kiếm, nguồn uy tín, góc máy, thời lượng (sàn 5s).
    - `chapter_XX_bao_chi.md`: Ghi rõ nguồn báo/văn kiện, tiêu đề thật, câu cần highlight, hiệu ứng zoom/pan.
    - `chapter_XX_infographic.md`: Ghi rõ dạng biểu đồ/bản đồ, chỉ số định lượng có mã claim, màu nhấn.
    - `chapter_XX_video_ai.md`: Ghi rõ prompt ảnh và prompt video chuyển động camera (Delta-motion), tuân thủ Action Whitelist và Zero-Metaphor Mandate.
  - **Bước 6 (Tự kiểm soát):** Đối chiếu với bộ tiêu chí định lượng (sàn/trần thời lượng, tỷ lệ loại shot) và định tính (chống ngụy biện, mỏ neo cảm xúc).

---

## 🎨 Giai Đoạn 3: Chuyển Giao Dữ Liệu Sản Xuất (Pha 12+C)
* **Quy tắc thi hành bằng tay và script hỗ trợ:**
  - 4 file track (`chapter_XX_broll.md`, `chapter_XX_bao_chi.md`, `chapter_XX_infographic.md`, `chapter_XX_video_ai.md`) **bắt buộc do agent biên soạn bằng tay**.
  - Script chỉ được dùng để kiểm tra tính toàn vẹn cú pháp hoặc chuyển đổi cấu trúc Markdown sang JSON phục vụ downstream (nếu cần), tuyệt đối không dùng script để tự sinh cảnh, tự cắt câu hay tự chế prompt.
* **4 luồng dữ liệu chuẩn bị cho khâu dựng:**
  1. *Video AI:* Nạp prompt vào cỗ máy VideoCore hoặc Google Vids/Veo sinh video độ phân giải cao.
  2. *B-Roll Fair Use:* Chuyển cho FootageHunter tải và cắt các đoạn tư liệu thực chứng (đảm bảo thời lượng >= 5s, tước audio gốc).
  3. *Forensic Callout:* Chụp ảnh bài báo hoặc văn bản gốc có kiểm chứng và xuất clip highlight văn bản sắc nét.
  4. *Infographics:* Thiết kế đồ họa dữ liệu dựa trên các điểm số liệu có mã claim.
