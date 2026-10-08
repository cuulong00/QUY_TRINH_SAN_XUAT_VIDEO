# BÁO CÁO TỔNG KẾT TÁI CẤU TRÚC HỆ THỐNG THỊ GIÁC & SĂN B-ROLL (VISUAL PIPELINE REDESIGN V1)

> **Mã công việc:** `VISUAL-PIPELINE-REDESIGN-V1`  
> **Ngữ cảnh:** `x-economy-master` (Dự án `X-Economic`)  
> **Đơn vị thực thi:** Antigravity (Heavy Technical Executor)  
> **Đơn vị điều phối & phê duyệt:** Claude Code & Người dùng (User)  
> **Ngày hoàn tất:** 28/09/2026  

---

## 📌 TỔNG QUAN KẾT QUẢ THỰC HIỆN

Thực hiện chỉ đạo dứt khoát của Người dùng và các phát hiện gốc rễ từ hai báo cáo kiểm toán trước đó ([`i2v_pipeline_audit.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/01_management/i2v_pipeline_audit.md) và [`footage_hunter_deepdive.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/01_management/footage_hunter_deepdive.md)), toàn bộ hệ thống thị giác của kênh **X-Economy** đã được tái cấu trúc triệt để theo 3 quyết định chiến lược:

1. **Quyết định 1 (3 Trụ Cột — Bỏ hoàn toàn VEO_AI):** Loại bỏ 100% video AI tạo chuyển động có nhân vật minh họa. Hệ thống thị giác chuẩn hóa về **3 Trụ Cột Nhận Thức**: `B_ROLL_FOOTAGE` (Hiện trường vật lý thực tế), `FORENSIC_CALLOUT` (Bằng chứng hồ sơ & báo chí thực chứng), và `INFOGRAPHIC_DATA` (Ảnh tĩnh AI Nano Banana 2 + hiệu ứng pan/zoom vi chuyển động trong CapCut, 0đ GPU cloud, không dùng I2V video engine). Deprecate nhánh Classic I2V (Pha 12A-C) và các cỗ máy điều khiển Google Flow qua Chrome Canary CDP / MiniMax H3.
2. **Quyết định 2 (Sửa gốc rễ Search Query B-Roll):** Tách bạch triệt để giữa `visual_intent` (ý đồ nghệ thuật chi tiết, chỉ dùng cho audit/người đọc) và `search_query` (công thức tối giản: `[Macro Entity / Event] + [Context Keyword] + [Tier 1 Source]`). Bổ sung danh sách phản-ví dụ thực tế cần tránh vào hướng dẫn. Ban hành từ điển bối cảnh chuẩn hóa [`00_core/context_tier_vocabulary.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/context_tier_vocabulary.md).
3. **Quyết định 3 (Contact Sheet Audit thành Cổng Bắt Buộc):** Thiết lập việc chấm lưới ảnh tiếp xúc (Contact Sheet) thành cổng chặn cứng (`Hard Blocking Gate`) bắt buộc trước khi đưa clip vào dựng timeline chính thức. Chấm một lượt duy nhất `FIT / BORDERLINE / REJECT` cho cả chương dựa trên bầu không khí/ngữ cảnh, tối ưu chi phí token.

---

## 🛠️ CHI TIẾT CÁC THAY ĐỔI THEO TỪNG QUYẾT ĐỊNH

### 1. QUYẾT ĐỊNH 1 — CHUẨN HÓA 3 TRỤ CỘT & LOẠI BỎ VEO_AI

#### A. Cập nhật Kỹ Năng Thị Giác Đa Thức ([`.agents/skills/visual_prompter_plus/SKILL.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/skills/visual_prompter_plus/SKILL.md))
- **Hệ quy chiếu 3 trụ cột:** Cây quyết định nhận thức loại bỏ hoàn toàn nhánh `VEO_AI`. Việc lựa chọn trụ cột dựa trên bản chất phân tích và cảm xúc cụ thể của từng cảnh:
  - *Bước 1 (Hồ sơ/Báo chí):* Phát ngôn, thanh tra, quyết định pháp lý, số liệu kiểm toán $\rightarrow$ `FORENSIC_CALLOUT`.
  - *Bước 2 (Cơ chế vô hình):* Cấu trúc toán học, đối kháng nợ, sơ đồ dòng tiền $\rightarrow$ `INFOGRAPHIC_DATA`.
  - *Bước 3 (Thế giới vật lý):* Con người lao động thật, nhà máy, công trường, cảng biển $\rightarrow$ `B_ROLL_FOOTAGE`.
- **Cấm ngặt hạn ngạch số học cơ học:** Không gán tỷ lệ % cứng nhắc (như B-Roll 50%, Infographic 30%). Giữ nguyên quy tắc cân bằng cảm giác định tính: không quá 2 cảnh Infographic/Forensic liên tiếp; không quá 3–4 cảnh B-roll liên tiếp mà không có chuyển nhịp.
- **Tái cấu trúc Infographic:** Đổi từ Motion Infographics (video I2V) sang **ảnh tĩnh AI (Nano Banana 2)** theo phong cách Data Sculpture (nền Slate `#1E293B`, đường nét `#F5F0E6`, điểm nhấn `#FFD600`) kết hợp hiệu ứng pan/zoom nhẹ nhàng trong CapCut.
- **Rà soát & Đánh dấu Deprecated các luật né lỗi AI-video-người:**
  - `Celebrity / Safety Filter Defense` $\rightarrow$ Đánh dấu *DEPRECATED* kèm lý do: không còn sinh video có mặt người nổi tiếng.
  - `Anthropological Fidelity Gate` $\rightarrow$ Đánh dấu *DEPRECATED* cho video chuyển động; chỉ giữ lại phiên bản tĩnh tinh gọn khi vẽ tranh minh họa bối cảnh lịch sử nếu có.
  - `Action Blacklist Veo` $\rightarrow$ Đánh dấu *DEPRECATED*: không còn nạp prompt video vào Veo.
  - Nhánh Classic I2V (Pha 12A/12B/12C sinh `prompts_chapter_XX.txt` và `prompts_chapter_XX_veo.txt`) $\rightarrow$ Đánh dấu *DEPRECATED*, thay thế hoàn toàn bằng I2V+ 3 TrỤ Cột.

#### B. Cập nhật Quy Trình & Biểu Mẫu
- [`.agents/workflows/generate_visual_prompts_plus.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/workflows/generate_visual_prompts_plus.md): Rút gọn 4 Harvest Manifests xuống 3 Manifests hoạt động (`broll_manifest_chapter_XX.json`, `forensic_manifest_chapter_XX.json`, `infographics_manifest_chapter_XX.json`); loại bỏ toàn bộ quy trình sinh file `prompts_chapter_XX_veo.txt`.
- [`02_templates/visual_storyboard_plus_template.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/02_templates/visual_storyboard_plus_template.md): Bỏ mục `Reference Asset Manifest (Cho Veo AI)` và loại bỏ Veo AI khỏi bảng ma trận nhận thức.

#### C. Cập nhật Tài Liệu Vận Hành Pha 14
- [`.agents/rules/content-os-pipeline.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/rules/content-os-pipeline.md), [`CLAUDE.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/CLAUDE.md), và [`03_playbooks/episode_workflow.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/03_playbooks/episode_workflow.md):
  - Định nghĩa lại Pha 14: **Footage & Asset Processing & Assembly**.
  - Loại bỏ hoàn toàn 2 cỗ máy gắn với Veo AI: Điều khiển Chrome Canary CDP cổng 9222/9223 tự động hóa Google Flow và ComfyUI MiniMax H3 GPU cloud.
  - Pha 14 tập trung vào: Săn B-roll thật (bắt buộc qua Contact Sheet Audit), Render Forensic MP4 callout, Sinh ảnh tĩnh Infographic AI và ráp nối timeline CapCut.

---

### 2. QUYẾT ĐỊNH 2 — SỬA GỐC RỄ KHÂU SINH SEARCH QUERY B-ROLL

#### A. Tách bạch `visual_intent` và `search_query` trong Manifest Schema
Trong `.agents/skills/visual_prompter_plus/SKILL.md` và `.agents/workflows/generate_visual_prompts_plus.md`, cấu trúc `broll_manifest_chapter_XX.json` đã được tách cứng:
```json
{
  "scene_id": "CH01_SC001",
  "voiceover_chunk": "Khi lò cao Dung Quất rực lửa...",
  "duration_sec": 4.5,
  "visual_intent": "Ý đồ thị giác chi tiết: Dòng kim loại nóng chảy tuôn trào trong đêm, công nhân trong bộ đồ bảo hộ nhiệt quan sát từ xa, phản ánh quy mô luyện kim khổng lồ. (CHỈ DÙNG CHO AUDIT / HUMAN - TUYỆT ĐỐI CẤM DÙNG LÀM QUERY)",
  "search_query": "Hòa Phát Dung Quất nhà máy thép cán nóng VTV24",
  "context_tier": "INDUSTRIAL_HEAVY",
  "source_priority": ["VTV24", "Hòa Phát Group Official", "VnExpress"],
  "visual_alternatives": ["Cảng biển chuyên dụng Hòa Phát Dung Quất xuất khẩu thép", "Khu liên hợp gang thép Dung Quất flycam toàn cảnh"],
  "fair_use_rule": "Mute 100% audio, cut 3.0s-5.5s, Warm Slate 10%, source watermark"
}
```

#### B. Đưa Phản-Ví Dụ Thực Tế Vào Quy Chuẩn
Tại [`00_core/footage_hunting_standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/footage_hunting_standard.md) (Mục 4) và [`.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md) (Mục I.1 & I.2), các phản-ví dụ thật vừa audit đã được cắm biển cảnh báo trực tiếp:

| Loại lỗi phát hiện qua Audit | Ví dụ lỗi THỰC TẾ đã sinh | Hậu quả tìm kiếm | Cách sửa chuẩn xác (Search Query) |
|---|---|---|---|
| **Nhồi thuật ngữ kỹ thuật sâu** | `"SCADA điều độ lưới điện"` | YouTube không có video nào đặt tên SCADA $\rightarrow$ 0 kết quả | `"Trung tâm điều độ hệ thống điện quốc gia VTV24"` |
| **Dịch thô ẩn dụ kinh tế** | `"Đóng bó thanh khoản ngân hàng"` | Không có phóng sự nào mang tên này | `"Ngân hàng Nhà nước họp chính sách tiền tệ"` |
| **Nhồi số liệu phần trăm** | `"Lãi suất 50 percent tăng vọt"` | Trả về video dạy toán hoặc tài chính cá nhân | `"Cục Dự trữ Liên bang Mỹ tăng lãi suất VTV24"` |
| **Thuật ngữ góc máy điện ảnh** | `"Close up công nhân hàn ray"` | Bị loãng kết quả vào video dạy quay phim | `"Thi công đường sắt Bắc Nam hiện trường VTV24"` |
| **Liệt kê hành động chi tiết** | `"Xe lu máy ủi san gạt nền đất"` | Rơi vào video giới thiệu thiết bị cơ giới | `"Đại công trường cao tốc Bắc Nam tiến độ thi công VTV1"` |

#### C. Ban Hành Từ Điển Bối Cảnh Chuẩn Hóa ([`00_core/context_tier_vocabulary.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/context_tier_vocabulary.md))
Đã tạo tài liệu dùng chung định nghĩa **7 Nhóm Bối Cảnh Vĩ Mô (Context Archetypes)**:
1. `MACRO_FINANCE_GOVERNANCE` (Tài chính, Ngân hàng, Cơ quan Điều hành).
2. `INDUSTRIAL_HEAVY_MANUFACTURING` (Công nghiệp nặng, Luyện kim, Chế tạo).
3. `INFRASTRUCTURE_MEGAPROJECTS` (Đại công trường, Cao tốc, Cầu cảng).
4. `RAILWAY_TRANSPORT_CORRIDOR` (Đường sắt đô thị, Hành lang vận tải Bắc - Nam).
5. `MARITIME_LOGISTICS_PORTS` (Cảng biển nước sâu, Chuỗi cung ứng hàng hải).
6. `URBAN_MARKET_REALESTATE` (Bất động sản, Đô thị, Nhà ở xã hội).
7. `HIGH_TECH_SEMICONDUCTOR` (Bán dẫn, Vi mạch, Phòng sạch công nghệ cao).

Mỗi nhóm cung cấp sẵn danh mục từ khóa bối cảnh tiếng Việt & tiếng Anh đã kiểm chứng hiệu quả với `ytsearch`.

---

### 3. QUYẾT ĐỊNH 3 — CONTACT SHEET AUDIT THÀNH CỔNG BẮT BUỘC

Tại [`00_core/footage_hunting_standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/footage_hunting_standard.md) (Mục 5) và [`.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md) (Mục VI.1):
- **Cơ chế Hard Gate:** Sau khi tải xong các clip ứng viên của một chương, hệ thống tự động chạy `python3 tools/footage_processor/core/audit_matrix.py` để ghép toàn bộ thumbnail đại diện thành một ảnh lưới (Contact Sheet Grid).
- **Quy tắc chấm 1 lượt:** LLM hoặc Auditor chỉ đọc ảnh lưới một lần duy nhất, chấm từng ô theo 3 mức:
  - `FIT`: Đúng bối cảnh vĩ mô, màu sắc điện ảnh nghiêm túc, không vi phạm vùng chết MC phòng thu.
  - `BORDERLINE`: Hơi lệch góc nhìn nhưng chấp nhận được nếu thiếu tư liệu thay thế.
  - `REJECT`: Sai bối cảnh (ví dụ hình đồ chơi, máy móc công trường nhỏ lẻ, MC phòng thu nói chuyện, phóng sự giật gân rẻ tiền).
- **Rào cản tuyệt đối:** Nghiêm cấm đưa clip vào thư mục `videos_final/` hoặc timeline dựng nếu chưa có xác nhận duyệt qua Contact Sheet. Tiết kiệm 95% token so với việc soi từng clip hay full video.

---

## 📋 BẢNG ĐỐI CHIẾU DANH MỤC TỆP TIN ĐÃ THAY ĐỔI

| STT | Tệp tin tác động | Phạm vi thay đổi |
|:---:|---|---|
| 1 | [`00_core/context_tier_vocabulary.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/context_tier_vocabulary.md) | **Tạo mới:** Từ điển 7 nhóm bối cảnh vĩ mô và từ khóa Tier 1 dùng chung cross-episode. |
| 2 | [`00_core/footage_hunting_standard.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/00_core/footage_hunting_standard.md) | **Cập nhật:** Thêm phản-ví dụ audit, tách `visual_intent` vs `search_query`, thiết lập Contact Sheet Audit Gate bắt buộc, xóa Veo AI khỏi fallback. |
| 3 | [`.agents/rules/broll-production-standard.md`](file:///Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md) | **Cập nhật Master Rule:** Đưa phản-ví dụ RCA vào Mục I.1 & I.2, đưa Contact Sheet Audit Gate vào Mục VI.1, loại bỏ Veo AI circuit breaker. |
| 4 | [`.agents/skills/visual_prompter_plus/SKILL.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/skills/visual_prompter_plus/SKILL.md) | **Cập nhật Skill:** Chuyển sang 3 Trụ Cột, đổi Infographic sang ảnh tĩnh AI + CapCut pan/zoom, deprecate Classic I2V và Veo AI safety rules, cập nhật schema 3-rail export. |
| 5 | [`.agents/workflows/generate_visual_prompts_plus.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/workflows/generate_visual_prompts_plus.md) | **Cập nhật Workflow:** Chuẩn hóa quy trình 3 giai đoạn theo 3 Trụ Cột, bỏ Veo AI prompt generation, loại bỏ `prompts_chapter_XX_veo.txt`. |
| 6 | [`02_templates/visual_storyboard_plus_template.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/02_templates/visual_storyboard_plus_template.md) | **Cập nhật Biểu Mẫu:** Rút gọn còn 3 Harvest Manifests, loại bỏ Reference Asset Manifest của Veo AI. |
| 7 | [`.agents/rules/content-os-pipeline.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/.agents/rules/content-os-pipeline.md) | **Cập nhật Pipeline Master:** Đánh dấu Pha 12A-C Classic là Deprecated; định nghĩa Pha 14 là Asset Processing & CapCut Assembly. |
| 8 | [`CLAUDE.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/CLAUDE.md) | **Cập nhật Bảng Pipeline:** Cập nhật Pha 12 thành I2V+ Flagship 3 Trụ Cột, Pha 14 bỏ Veo batch render. |
| 9 | [`03_playbooks/episode_workflow.md`](file:///Users/pro16/Documents/VideoProject/X-Economic/03_playbooks/episode_workflow.md) | **Cập nhật Playbook:** Đồng bộ mô tả Pha 12 và Pha 14 loại bỏ hoàn toàn Veo AI. |
| 10 | [`_agent_chat/tasks/VISUAL-PIPELINE-REDESIGN-V1.json`](file:///Users/pro16/Documents/VideoProject/X-Economic/_agent_chat/tasks/VISUAL-PIPELINE-REDESIGN-V1.json) | **Cập nhật Tiến độ:** Chuyển trạng thái từ `working` sang `completed`. |
| 11 | [`_agent_chat/mailbox.jsonl`](file:///Users/pro16/Documents/VideoProject/X-Economic/_agent_chat/mailbox.jsonl) | **Ghi nhận sự kiện:** Append tin nhắn `seq: 8` báo cáo `completed` kèm artifact. |

---

## 💡 KHUYẾN NGHỊ ĐỒNG BỘ DÀNH CHO CÔNG CỤ FOOTAGEHUNTER DÙNG CHUNG

Tuân thủ nghiêm ngặt lưu ý của Claude Code: `/Users/pro16/Documents/VideoProject/FootageHunter/` là công cụ dùng chung toàn hệ thống nên **không tự ý sửa code trong task này**. Tuy nhiên, để 3 quyết định trên phát huy tối đa hiệu quả trong thực tế, Antigravity kiến nghị Claude Code xem xét một task độc lập tiếp theo để đồng bộ:

1. **Cập nhật `FootageHunter/core/visual_query_planner.py`:**
   - Thay vì tiếp tục cơ chế chắp vá `hardcode entity keywords` cho từng nhân vật/tập, hãy cập nhật parser đọc trực tiếp trường `search_query` từ manifest JSON mới.
   - Khi trường `search_query` đã chuẩn hóa qua `Context Tier Vocabulary`, script chỉ việc chuyển thẳng câu này sang lệnh `yt-dlp "ytsearchN:..."` mà không cần xử lý ngắt từ/regex phức tạp.
2. **Kích hoạt tự động Contact Sheet Generation trong `process_broll.py`:**
   - Sau khi hoàn tất vòng tải các video ứng viên của một chương, tự động gọi module `audit_matrix.py` để sinh ngay file `audit_contact_sheet_CHXX.jpg` vào thư mục chương.
   - Dừng luồng xử lý và in thông báo yêu cầu kiểm toán xác nhận trước khi tiếp tục cắt ghép vào timeline.

---
*Báo cáo được khởi tạo và lưu trữ độc bản tại `01_management/visual_pipeline_redesign_v1.md`.*
