---
description: >-
  MANDATORY first step for any new episode. MUST be used before any content
  creation when episode folder does not exist. Creates Phase 1 (Topic Qualification).
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` để đọc lần lượt các file sau. NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc:

1. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_viral_alchemist.md`
2. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_macro_analyst.md`
3. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/personas/the_critical_auditor.md`
4. `/Users/pro16/Documents/VideoProject/Dòng Chảy/.agents/skills/strategy_council/SKILL.md`

Chỉ sau khi đọc xong cả bốn file trên mới được tiếp tục các bước bên dưới.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`. Replace toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.

3. Đọc `00_core/voice_dna.md`, `00_core/channel_bible.md`, `00_core/financial_boundaries.md`, `00_core/audience_personas.md`.

4. Xác định chủ đề thô từ user.

5. **PHA 1 — HỘI ĐỒNG CHIẾN LƯỢC NỘI DUNG (CONTENT STRATEGY COUNCIL):**

   Thực thi đúng quy trình tranh biện 5 bước quy định tại `strategy_council/SKILL.md`:
   - **Bước 1.0:** Khảo sát Web sơ bộ (`search_web`) để lấy bối cảnh thực tế mới nhất.
   - **Bước 1.1:** Đề xuất 3 Góc tiếp cận độc lập tương ứng với 3 vai trò (Viral Alchemist, Macro Analyst, Critical Auditor).
   - **Bước 1.2:** Chạy Vòng Tranh luận & Phản biện chéo để chỉ ra điểm mù, rủi ro, và gạt bỏ clichés.
   - **Bước 1.3:** Dung hợp các phản biện để chọn ra **Champion Angle** tối ưu nhất.
   - **Bước 1.4:** Xuất đề án thảo luận và Champion Angle dưới dạng tệp `episodes/[slug]/01_topic_qualification.md`.

   Tệp `01_topic_qualification.md` **BẮT BUỘC** chứa đủ cấu trúc 6 mục quy định tại tệp kỹ năng của Hội đồng.

   **Dừng và chờ user duyệt Champion Angle tại Gate 1 trước khi chạy Pha 2 (`/deep_research`).**