# /init_episode — Khởi tạo Episode Mới (Hiểu Biết Hơn)

> Slash command dùng để khởi tạo một thư mục tập podcast mới và xác thực chủ đề (Pha 1: Topic Qualification).

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` để đọc lần lượt bốn file sau. NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc:

1. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/personas/the_viral_alchemist.md`
2. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/personas/the_policy_analyst.md`
3. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/personas/the_critical_auditor.md`
4. `/Users/pro16/Documents/VideoProject/HieuBietHon/.agents/skills/strategy_council/SKILL.md`

Chỉ sau khi đọc xong cả bốn file trên mới được tiếp tục các bước bên dưới.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`. Replace toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.

3. Đọc `00_core/voice_dna.md`, `00_core/channel_bible.md`, `00_core/brand_safety_guidelines.md`, `00_core/audience_personas.md`.

4. Xác định chủ đề thô hoặc tài liệu đầu vào từ user.

5. **PHA 1 — XÁC THỰC CHỦ ĐỀ (Kích hoạt Hội đồng Chiến lược):**
   *   Gọi Hội đồng Chiến lược thực thi đúng quy trình tranh luận 5 bước trong `strategy_council/SKILL.md`.
   *   Tạo tệp `episodes/[slug]/01_topic_qualification.md`. Tệp này **BẮT BUỘC** chứa các phần sau (checklist cứng):
       - [ ] **Nguồn tư liệu tham chiếu:** Liệt kê các tệp hoặc đường dẫn đã sử dụng.
       - [ ] **Champion Angle (Góc tiếp cận tối ưu nhất):** Tên góc khai thác, tiêu đề dự kiến và One-line Summary.
       - [ ] **Nhật ký Tranh luận của Hội đồng (Detailed Debate Transcript):** Đối đáp trực tiếp mang tính cá tính của 3 chuyên gia.
       - [ ] **Khung Tuyến Kịch Bản Dự Kiến (Trajectory Outline):** Phác thảo cấu trúc 4 Hồi chia thành 7-10 chương cụ thể.
       - [ ] **Kế hoạch Nghiên cứu chuyển giao (Research Planning):** Thiết kế Prompt nạp nguồn cấu trúc và danh sách câu hỏi trích xuất sơ bộ.

6. Hiển thị bảng tóm tắt góc tiếp cận đã chọn và khung tuyến kịch bản trực tiếp trong chat.

**Dừng và chờ user duyệt góc khai thác trước khi sang Pha 2 (Data Mining & Verification) — chạy `/deep_research`.**
