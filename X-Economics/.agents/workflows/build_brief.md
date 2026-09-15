---
description: >-
  Build the Strategy Brief (Phase 3). Requires completed 01_topic_qualification.md
  and 02_research_map.md. MUST be run after /deep_research.
---

## 🛑 HARD GATE TOÀN BỘ WORKFLOW NÀY

Trước khi thực thi BẤT KỲ bước nào, agent PHẢI dùng tool `view_file` đọc lần lượt các file sau:

1. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_editorial_strategist.md`
2. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/personas/the_policy_analyst.md`
3. `/Users/pro16/Documents/VideoProject/X-Economics/.agents/skills/script_architect/SKILL.md`

NGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc đọc.

---

## Các bước thực thi

1. Hỏi episode slug nếu chưa có.

2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/01_topic_qualification.md`, `episodes/[slug]/02_research_map.md`, và `episodes/[slug]/02_research_synthesis.md`.

3. **GIAO THỨC GHI LOG TIỀN KHỞI ĐỘNG (PRE-FLIGHT LOGGING):**
   TRƯỚC KHI tạo `03_brief.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
   ```markdown
   > 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG TẠO 03_brief.md]**
   > - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Editorial Strategist + The Policy Analyst
   > - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/build_brief` (`script_architect/SKILL.md`)
   > - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
   >   * `episodes/[slug]/01_topic_qualification.md` (Định vị chủ đề & Góc nhìn)
   >   * `episodes/[slug]/02_research_map.md` & `02_research_synthesis.md` (Dữ liệu thực chứng)
   > - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/03_brief.md`
   > - 🛡️ **Rào Cản Kiểm Toán:** Substance First — số liệu neo bất biến, cấm suy diễn ngoài phạm vi.
   ```

4. **PHA 3 — BẢN CHIẾN LƯỢC (STRATEGY BRIEF):**
   Nhập tâm Script Architect (= kết hợp Macro Strategist + Narrative Director + Policy Analyst).
   
   Tạo `episodes/[slug]/03_brief.md`. BẮT BUỘC nhúng khối Provenance Metadata ở đầu tệp:
   ```markdown
   <!--
   DOCUMENT PROVENANCE & EXECUTION LINEAGE:
   - Output Document: episodes/[slug]/03_brief.md
   - Activated Persona: The Editorial Strategist + The Policy Analyst
   - Activated Skill: script_architect/SKILL.md (/build_brief)
   - Source Documents Consulted: 01_topic_qualification.md, 02_research_map.md, 02_research_synthesis.md
   - Execution Timestamp: [YYYY-MM-DD HH:MM]
   -->
   ```
   File này **BẮT BUỘC** sử dụng dữ liệu cứng đã được thu thập từ `02_research_map.md` (Pha 2) để điền vào phần Neo Số Liệu. Không tự bịa số liệu.

   File `03_brief.md` **BẮT BUỘC** tuân thủ cấu trúc Masterpiece Chiến Lược (theo `02_templates/masterpiece_pipeline/03_brief_template.md`):

   ```
   ✅ Checklist output bắt buộc của Pha 3 (Masterpiece Strategy Brief):
   [ ] Biến cố trung tâm (Central Inciting Incident) — sự kiện/văn bản cụ thể phát nổ mở màn
   [ ] Câu hỏi lớn tối thượng (Central Dramatic Question) — câu hỏi điều tra xuyên suốt kịch bản
   [ ] Hợp đồng nhận thức (Cognitive Contract) — Lời hứa làm sáng tỏ cơ chế + Cảm xúc Grand Payoff
   [ ] Phân loại chủ đề (Classification Gate) — Phân định rõ Loại A/B/C, chọn đúng Relevance Anchor
   [ ] Giới hạn Case Study quốc tế — Tối đa 1 case đối với Loại B; không sa đà kể chuyện nước ngoài
   [ ] Lăng kính độc bản (Unique Lens) — Phân tích kinh tế/thể chế/trò chơi, không sao chép báo chí
   [ ] Mỏ neo vật lý (Physical Anchor) — Vật thể thực tế sờ thấy được làm điểm tựa trực quan
   [ ] Cấu trúc tự sự tăng tiến — Khung 3 Màn nhân quả (Therefore / But) & Mô hình Búp bê Nga 4 tầng
   [ ] Bảng mỏ neo số liệu chiến lược — Data Passport đối chiếu 1-1 với research_vault/ và vault/00_Global_Vision_Synthesis.md
   [ ] Ma trận quy đổi tiền tệ — Thống nhất tỷ giá VNĐ/Ngoại tệ cho kịch bản thoại
   [ ] Ba rào cản biên tập chống bào chữa (3 Cognitive Gates) — Khóa vị thế nhà điều tra độc lập
   [ ] Truy vết Vault (Traceability Matrix) — Danh sách link đối chiếu trực tiếp về các tệp vault gốc
   ```

   Điều chỉnh ngôn ngữ: Mọi thuật ngữ tiếng Anh phải Việt hóa theo quy tắc trong `00_core/voice_dna.md` (Mục 8).

5. Thông báo cho user duyệt Pha 3 (`03_brief.md`) trước khi chuyển sang **Pha 4: Master Outline Engine (`/build_outline` ➔ `07_outline.md`)**.
