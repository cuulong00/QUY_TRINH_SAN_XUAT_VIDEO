# /init_episode — Khởi tạo Episode Mới (Góc Nhìn Podcast)

> Slash command dùng để khởi tạo một thư mục tập podcast mới và xác thực chủ đề (Pha 1: Topic Qualification).

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` để đọc lần lượt bốn file sau. NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc:

1. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_viral_alchemist.md`
2. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_policy_analyst.md`
3. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_critical_auditor.md`
4. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/skills/strategy_council/SKILL.md`

Chỉ sau khi đọc xong cả bốn file trên mới được tiếp tục các bước bên dưới.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`. Replace toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.

3. Đọc `00_core/voice_dna.md`, `00_core/channel_bible.md`, `00_core/brand_safety_guidelines.md`, `00_core/audience_personas.md`.

4. Xác định chủ đề thô hoặc tài liệu đầu vào từ user.

5. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo `01_topic_qualification.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO 01_topic_qualification.md]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Strategy Council (Viral Alchemist + Policy Analyst + Critical Auditor)
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/init_episode` (`strategy_council/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * Đề tài thô / Bài báo đầu vào từ User
   >   * `00_core/channel_bible.md`, `00_core/voice_dna.md`
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/01_topic_qualification.md`
   > - 🛡️ **Rào Cản Kiểm Toán:** Hội đồng tranh luận phản biện 3 chiều, chọn Champion Angle không rỗng tuếch.
   ```

6. **PHA 1 — XÁC THỰC CHỦ ĐỀ (Kích hoạt Hội đồng Chiến lược):**
   *   Gọi Hội đồng Chiến lược thực thi đúng quy trình tranh luận 5 bước trong `strategy_council/SKILL.md`.
   *   Tạo tệp `episodes/[slug]/01_topic_qualification.md`. BẮT BUỘC nhúng khối Provenance Metadata ở đầu tệp:
   ```markdown
   <!--
   DOCUMENT PROVENANCE & EXECUTION LINEAGE:
   - Output Document: episodes/[slug]/01_topic_qualification.md
   - Activated Persona: Strategy Council (Viral Alchemist + Policy Analyst + Critical Auditor)
   - Activated Skill: strategy_council/SKILL.md (/init_episode)
   - Source Documents Consulted: [Nguồn tư liệu đầu vào]
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```
   *   Tệp này **BẮT BUỘC** chứa các phần sau (checklist cứng):
       - [ ] **Nguồn tư liệu tham chiếu:** Liệt kê các tệp hoặc đường dẫn đã sử dụng.
       - [ ] **Champion Angle (Góc tiếp cận tối ưu nhất):** Tên góc khai thác, tiêu đề dự kiến và One-line Summary.
       - [ ] **Nhật ký Tranh luận của Hội đồng (Detailed Debate Transcript):** Đối đáp trực tiếp mang tính cá tính của 3 chuyên gia.
       - [ ] **Tuyến Luận Điểm Dự Kiến (Projected Narrative Arc):** Phác thảo các chặng nhận thức theo diễn tiến tự nhiên, không tiền định số chương cứng (việc chia chương thuộc đặc quyền của Pha 4).
       - [ ] **Kế hoạch Nghiên cứu chuyển giao (Research Planning):** Thiết kế Prompt nạp nguồn cấu trúc và danh sách câu hỏi trích xuất sơ bộ.

7. Hiển thị bảng tóm tắt góc tiếp cận đã chọn và khung tuyến kịch bản trực tiếp trong chat.

**Dừng và chờ user duyệt góc khai thác trước khi sang Pha 2 (Data Mining & Verification) — chạy `/deep_research`.**
