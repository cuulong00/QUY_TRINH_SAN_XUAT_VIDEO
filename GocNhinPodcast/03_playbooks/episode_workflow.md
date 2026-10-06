# episode_workflow.md — Quy Trình Sản Xuất Video Chuẩn 16 Pha (Systems Thinking Architecture)

Đây là quy trình sản xuất video chuẩn hóa theo mô hình Tư Duy Hệ Thống (Systems Thinking), định vị bức tranh toàn cảnh trước khi đào sâu chi tiết, tuần tự từng pha một.

---

## 🏛️ Pipeline Tổng Thể 16 Pha

| Pha | Tên Pha | Output Chính | Chuyên Gia (Persona DNA) | Skill / Lệnh Thực Thi |
|---|---|---|---|---|
| **1** | **Master Systemic Topography & Global Vision** | `01_global_vision_synthesis.md` | `the_macro_strategist` (Chủ tịch) + `the_policy_analyst` + `the_critical_auditor` | `/init_episode` (Strategy Council) |
| **2** | **Topographical Deep Research** | `02_research_map.md` & `02_research_synthesis.md` | `the_policy_analyst` + `the_industrial_economist` | `/deep_research` (NotebookLM Direct RPC) |
| **3** | **Strategy Brief** | `03_brief.md` | `the_editorial_strategist` + `the_policy_analyst` | `/build_brief` |
| **4** | **Master Outline Engine (DÀN Ý TRƯỚC)** | `07_outline.md` | `the_dialectic_architect` (`the_dialectic_architect` + `the_critical_auditor`) | `/build_outline` (Orientation Frame Mandate) |
| **5** | **Hook Lab (HOOK SAU)** | `04_hook_pack.md` | `the_viral_alchemist` + `the_critical_auditor` | `/hook_lab` (May đo 3-5 Hooks bám Dàn ý) |
| **6** | **Chapter Briefs & NST** | `08_chapter_briefs.md` & `09_narrative_state_tracker.md` | `the_narrative_director` + `the_critical_auditor` | `/build_outline` (20 trường chuẩn hóa: dữ liệu + nhịp chuyện) |
| **7** | **Chapter Writing (Từng chương)** | `chapter_XX.md` | Persona chỉ định từng chương + Khóa Oral Voice | `/write_chapter` (Claim Ledger công khai) |
| **8** | **Merge Voiceover** | `voiceover.md` | `the_quality_czar` | `/merge_voiceover` |
| **9** | **Retention Bridge Audit** | `retention_bridge_audit.md` | `the_critical_auditor` | `retention_bridge_audit` SKILL |
| **10 & 11** | **Editorial, Compliance & Dialectical Audit** | `10_compliance_report.md` | `the_policy_analyst` + `the_critical_auditor` + `the_editorial_strategist` | `compliance_council` SKILL (Dialectical Rigor 25%) |
| **12A-C** | **Visual Storyboard & I2V Prompts** | `visual_storyboard_blueprint.md`, `chapter_XX_visual.md`, `prompts_chapter_XX.txt` | `the_visual_storyteller` + `the_scene_architect` + `the_image_prompt_composer` | `/generate_visual_prompts` (Chỉ khi yêu cầu) |
| **13** | **Audio Landscape** | Audio direction | `the_sonic_architect` | `music_composer` (Chỉ khi yêu cầu) |
| **14** | **Batch Video Production** | Video clips (`videos/`) | `the_visual_storyteller` + `the_scene_architect` | `/generate_videos` (Chỉ khi yêu cầu) |
| **15** | **Production Handoff** | `production_notes.md` | `the_editorial_strategist` | `/production_handoff` |
| **16** | **Postmortem & Performance Review** | `postmortem.md` & cập nhật `performance_benchmarks.md` | `the_critical_auditor` + `the_macro_strategist` | Manual / Postmortem template |

---

## Chi Tiết Tiêu Chí Từng Pha

### Pha 1 — Master Systemic Topography & Global Vision Synthesis
- **Mục tiêu:** Định vị toàn cảnh bàn cờ, xác định 3 thế lực ngầm, dòng tiền/quyền lực, cơ chế sinh tồn và nghịch lý trung tâm trước khi nghiên cứu chi tiết.
- **Output:** `01_global_vision_synthesis.md`
- **Tiêu chí qua pha:**
  - Có Sơ đồ Không gian Bàn cờ ASCII mạch lạc.
  - Lập **Ma Trận 4 Lăng Kính Đối Trọng (Multi-Stakeholder Quad-Matrix)**: Thể chế $\leftrightarrow$ Doanh nghiệp $\leftrightarrow$ Người dân $\leftrightarrow$ Học thuật/Kiểm toán độc lập.
  - Khóa chặt **Vector Đánh Đổi & Chi Phí Cơ Hội (Trade-offs & Opportunity Costs)**: Ai hưởng lợi vs Ai gánh chịu chi phí ngầm, Unintended Consequences.
  - Thiết kế bộ 5 Prompts nạp nguồn NotebookLM, trong đó **Prompt 5 BẮT BUỘC là "The Dissenting, Skeptical & Failure Case Vector"**.

### Pha 2 — Topographical Deep Research
- **Mục tiêu:** Cào dữ liệu chuyên sâu và kiểm chứng thực chứng dựa trên các tọa độ điểm nghẽn đã định vị ở Pha 1.
- **Output:** `02_research_map.md` và `02_research_synthesis.md` (kèm `research_vault/`)
- **Tiêu chí qua pha:**
  - Chạy NotebookLM với `--mode deep --import-all` và `BypassSandbox: true` (bao gồm Prompt 5 Phản biện).
  - Hoàn thành **Bảng Đối Soát Dữ Liệu Bất Đồng & Đánh Đổi (Contested Data & Trade-Offs Ledger)**, cấm liệt kê hình thức.
  - 8–12 Extraction Queries trả lời các mắt xích nhân quả gốc rễ và bóc tách bất đồng số liệu.
  - Sổ cái bằng chứng thực chứng mỏ neo (`DATA-01` đến `DATA-XX`).

### Pha 3 — Strategy Brief
- **Mục tiêu:** Lập bản Hiến pháp kịch bản, xác định đối tượng người xem, luận điểm trung tâm và lời hứa insight.
- **Output:** `03_brief.md`
- **Tiêu chí qua pha:**
  - Tiếp nhận đầy đủ Bản đồ Pha 1 và Kho dữ liệu Pha 2.
  - Phân định rõ phạm vi phân tích và ranh giới cấm drift.
  - Định hình phong cách Editorial Noir (điềm tĩnh, đĩnh đạc, ấm áp, uy tín).

### Pha 4 — Master Outline Engine (DÀN Ý TRƯỚC + BIỆN CHỨNG HEGEL)
- **Mục tiêu:** Thiết kế cấu trúc kịch bản biện chứng 3 Màn (Thesis ➔ Antithesis ➔ Synthesis) với nhịp điệu sóng lượn và khung định hướng nhận thức.
- **Output:** `07_outline.md`
- **Tiêu chí qua pha:**
  - **Khung Định Hướng Bắt Buộc (Orientation Frame Mandate):** Chương 1 PHẢI dành 45–60s để trao tấm bản đồ bối cảnh lớn và câu hỏi lớn cho khán giả; tuyệt đối KHÔNG đọc mục lục hay liệt kê các chặng dừng chân ("ba trạm").
  - **Chương Phản Đề Cốt Tử (The Devil's Advocate Chapter — CH[D] BẮT BUỘC):** Chương độc lập đóng vai phe đối lập ở phiên bản logic mạnh nhất (Steelman), dùng Contested Data từ Pha 2 để bẻ gãy giả định, phơi bày chi phí cơ hội.
  - **Hợp Đề & Kết Luận Có Điều Kiện:** Màn 3 tìm ra điểm cân bằng thực tế, không phán xét nhị nguyên đen-trắng.

### Pha 5 — Hook Lab (HOOK SAU)
- **Mục tiêu:** May đo 3–5 phương án Hook 30–45s bám sát 100% vào Dàn ý và Grand Payoff của tập.
- **Output:** `04_hook_pack.md`
- **Tiêu chí qua pha:**
  - Hook được chọn sẽ là đoạn mở đầu nguyên văn của Chương 1.
  - Không clickbait rẻ tiền, cam kết giải quyết nghịch lý trung tâm đã định vị ở Pha 1.

### Pha 6 — Chapter Briefs & NST
- **Mục tiêu:** Chuẩn hóa brief chi tiết cho từng chương (20 trường: 16 trường dữ liệu & lập luận + 4 trường nhịp chuyện) và khởi tạo Narrative State Tracker.
- **Output:** `08_chapter_briefs.md` và `09_narrative_state_tracker.md`
- **Tiêu chí qua pha:**
  - Có đủ 4 trường nhịp chuyện: `cau_hoi_dieu_tra`, `vat_chung`, `cu_lat`, `chu_the_va_dong_co`.
  - Khóa chặt `steelman_counter_thesis` và `trade_offs_and_unintended_consequences`.
  - Khóa chặt Forbidden Echoes (chống lặp luận điểm/số liệu).
  - Thiết lập giao thức Seeding $\leftrightarrow$ Harvesting giữa các chương liền kề.

### Pha 7 — Chapter Writing
- **Mục tiêu:** Viết kịch bản thoại từng chương một, tuyệt đối tuân thủ Claim Ledger và Oral Voice DNA.
- **Output:** `chapter_XX.md`
- **Tiêu chí qua pha:**
  - In Claim-to-Source Verification Ledger công khai ra màn hình chat trước khi viết.
  - **Anti-Token Syntax Ban:** Cấm phản biện giả vờ kiểu bù nhìn rơm. Bắt buộc triển khai phản biện qua Cấu trúc Steelman 3 câu.
  - Văn phong nói tự nhiên, câu ngắn nhịp thở, không sáo rỗng AI.
  - Nghiệm thu từng chương một, cấm viết hàng loạt.

### Pha 8 — Merge Voiceover
- **Mục tiêu:** Gộp kịch bản toàn tập thành tệp thoại liền mạch, áp dụng nguyên tắc Zero-Scaffolding.
- **Output:** `voiceover.md`

### Pha 9 — Retention Bridge Audit
- **Mục tiêu:** Soi chiếu các điểm rơi chú ý, cầu nối giữ chân người xem giữa các chương.
- **Output:** `retention_bridge_audit.md`

### Pha 10 & 11 — Editorial, Compliance & Dialectical Audit
- **Mục tiêu:** Kiểm toán an toàn biên tập, pháp lý, nhịp thở TTS và **Đa chiều & Khử thiên kiến (Dialectical Rigor & Bias Audit 25%)**.
- **Output:** `10_compliance_report.md`
- **Tiêu chí qua pha:**
  - Vượt qua bài test sát hạch 3 câu hỏi của Phe Đối Lập (Devil's Advocate Stress-Test).
  - Điểm tổng ≥ 8.0/10 và không có tiêu chí nào < 7.0.

### Pha 12A-C đến Pha 16
- **Pha 12A-C (Thị giác & Prompts):** Chỉ thực hiện khi có yêu cầu trực tiếp từ User.
- **Pha 13 (Audio Landscape):** Thiết kế âm nhạc và soundscapes (chỉ khi có yêu cầu).
- **Pha 14 (Batch Video Production):** Sản xuất video AI Veo 3.1 Lite (chỉ khi có yêu cầu).
- **Pha 15 (Production Handoff):** `production_notes.md`.
- **Pha 16 (Postmortem):** Ghi nhận bài học kinh nghiệm và cập nhật `performance_benchmarks.md`.
