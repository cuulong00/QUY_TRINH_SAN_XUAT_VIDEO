# /init_episode — Khởi tạo Master Topography & Global Vision (Pha 1)

> Slash command dùng để khởi tạo một thư mục tập podcast mới và thiết lập Bản Đồ Địa Hình Bàn Cờ & Bức Tranh Toàn Cảnh (Pha 1: Master Systemic Topography & Global Vision Synthesis).

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` để đọc lần lượt các file sau. NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc:

1. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_macro_strategist.md` (👑 Chủ Tịch Hội Đồng & Tổng Công Trình Sư Hệ Thống)
2. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_policy_analyst.md`
3. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_critical_auditor.md`
4. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_viral_alchemist.md`
5. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/strategy_council/SKILL.md`

Chỉ sau khi đọc xong các file trên mới được tiếp tục các bước bên dưới.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`. Replace toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.

3. Đọc `00_core/voice_dna.md`, `00_core/channel_bible.md`, `00_core/brand_safety_guidelines.md`, `00_core/audience_personas.md`.

4. Xác định chủ đề thô hoặc tài liệu đầu vào từ user.

5. **GIAO THỚC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo `01_global_vision_synthesis.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO 01_global_vision_synthesis.md]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Strategy Council (Chủ tịch `the_macro_strategist` + `the_policy_analyst` + `the_critical_auditor` + `the_viral_alchemist`)
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/init_episode` (`strategy_council/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * Đề tài thô / Bài báo đầu vào từ User
   >   * `00_core/channel_bible.md`, `00_core/voice_dna.md`
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/01_global_vision_synthesis.md`
   > - 🛡️ **Rào Cản Kiểm Toán:** First-Principles & Systems Thinking. Bắt buộc có Sơ đồ ASCII Bàn cờ định vị 3 lực lượng cấu trúc và nghịch lý cốt lõi trước khi cho phép nghiên cứu.
   ```

6. **PHA 1 — XÂY DỰNG MASTER SYSTEMIC TOPOGRAPHY & GLOBAL VISION:**
   *   Gọi Hội đồng Chiến lược thực thi đúng quy trình tranh luận trong `strategy_council/SKILL.md`.
   *   Tạo tệp `episodes/[slug]/01_global_vision_synthesis.md`. BẮT BUỘC nhúng khối Provenance Metadata ở đầu tệp:
   ```markdown
   <!--
   DOCUMENT PROVENANCE & EXECUTION LINEAGE:
   - Output Document: episodes/[slug]/01_global_vision_synthesis.md
   - Activated Persona: The Strategy Council (Chủ tịch the_macro_strategist)
   - Activated Skill: strategy_council/SKILL.md (/init_episode)
   - Source Documents Consulted: [Nguồn tư liệu đầu vào]
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```
   *   Tệp này **BẮT BUỘC** chứa 2 phần chuẩn hóa (checklist cứng):
       - [ ] **PHẦN I: BIÊN BẢN HỘI ĐỒNG CHIẾN LƯỢC:**
         * User Intent Statement.
         * Nhật ký tranh luận đối thoại trực tiếp (Direct Debate Transcript) giữa các chuyên gia.
         * Quyết định phê duyệt đề tài (Strategy Council Verdict) của Chủ tịch `the_macro_strategist`.
       - [ ] **PHẦN II: BẢN ĐỒ ĐỊA HÌNH HIỆN THỰC 4 TẦNG (UNIVERSAL 4-TIER BLUEPRINT):**
         * *Tầng 1:* System Meta-Instructions & Compliance Guardrails.
         * *Tầng 2:* Macro Landscape & Systemic Forces (Sơ đồ ASCII Bàn cờ định vị các chủ thể, dòng tiền, rào cản).
         * *Tầng 3:* Underlying Mechanics & Central Paradoxes (Chuỗi nhân quả gốc rễ và mâu thuẫn hệ thống).
         * *Tầng 4:* Immutable Ground-Truth Data Vault (`DATA-01` đến `DATA-XX`).
         * *Phụ lục:* Kế hoạch nạp nguồn Deep Research 1-1 cho Pha 2 (3–5 Prompts nạp nguồn theo từng phân khu trên bàn cờ).
       - [ ] **VÙNG CẤM TUYỆT ĐỐI:** CẤM xuất hiện bất kỳ từ khóa cấu trúc kịch bản hoặc chia chương nào (`CH01`, `Chương 1`...).

7. Hiển thị Sơ đồ ASCII Bàn cờ và tóm tắt nghịch lý trung tâm trực tiếp trong chat.

**DỪNG và chờ user duyệt Bản Đồ Toàn Cảnh trước khi sang Pha 2 (Topographical Deep Research) — chạy `/deep_research`.**
