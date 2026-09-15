# /deep_research — Nghiên cứu sâu NotebookLM (Đạo & Khoa Học)

> Slash command độc lập cho Deep Research. Kích hoạt chuyên gia Deep Researcher để nghiên cứu đa chiều trên NotebookLM.

## Khi nào dùng
- Khi cần nghiên cứu sâu một chủ đề cho episode (Pha 2)
- Khi cần bổ sung data cho episode đang viết
- Khi cần fact-check hoặc cross-verify số liệu
- Khi user gõ `/deep_research [chủ đề]` hoặc `/research [chủ đề]`

## Quy trình thực thi

### Bước 1: Xác định Episode & Notebook
1. Xác định episode folder `episodes/[slug]/`
   - Nếu user chỉ định episode → dùng episode đó
   - Nếu không → hỏi user episode nào
2. **ĐỌC file `episodes/[slug]/.notebook_url`** để lấy Master Notebook URL
   - ⛔ **CẤM:** Tuyệt đối KHÔNG ĐƯỢC dùng tool `create_notebook` để tạo notebook mới mỗi khi research. Nếu đã có file `.notebook_url`, BẮT BUỘC dùng URL trong đó cho mọi tool (deep_research, ask_question).
   - Nếu file chưa tồn tại → HỎI user cung cấp URL notebook để lưu vào file. KHÔNG tự động tạo notebook mới.
3. Hiển thị banner kích hoạt chuyên gia:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎭 CHUYÊN GIA: Deep Researcher
📋 PHA: 2 — Data Mining & Verification
🎬 EPISODE: [tên episode]
📂 SKILL: deep_researcher/SKILL.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Bước 2: Đọc Persona & SKILL (BẮT BUỘC)
1. `view_file` → `/Users/pro16/Documents/VideoProject/KenhTamLy/.agents/personas/the_research_scientist.md`
2. `view_file` → `/Users/pro16/Documents/VideoProject/KenhTamLy/.agents/skills/deep_researcher/SKILL.md`
3. `view_file` → `/Users/pro16/Documents/VideoProject/KenhTamLy/.agents/skills/notebooklm_librarian/SKILL.md`

### Bước 3: Lên Kế Hoạch & Thiết Kế Truy Vấn (RESEARCH PLANNING GATE)
Tác nhân phải thiết lập và xuất bản tệp `episodes/[slug]/02_research_plan.md` chứa đầy đủ kế hoạch nghiên cứu trước khi thực hiện bất kỳ lệnh gọi công cụ nào với NotebookLM.

1. **Hiển thị Log Bắt Đầu Chạy:** In ra màn hình chat thông báo: *"Bắt đầu khởi chạy Pha 2: Data Mining & Verification cho tập [slug]"*.
2. **Thiết Kiết & Hiển thị Prompt Nạp nguồn Cấu trúc (Structured Ingestion Prompt):**
   - Thiết kế và hiển thị một Prompt tìm kiếm tổng hợp duy nhất bằng ngôn ngữ tự nhiên, được cấu trúc bằng các đề mục và phân dòng rõ ràng để hướng dẫn NotebookLM tự động quét web tìm tài liệu cho mọi góc tiếp cận (thực trạng, chính sách vĩ mô, đối sánh lịch sử).
3. **Thiết kế & Hiển thị Danh sách Câu hỏi Trích xuất tối ưu (Optimized Extraction Queries):**
   - Thiết kế và hiển thị danh sách 8-12 câu hỏi trích xuất cụ thể tương ứng với từng chương của Khung tuyến kịch bản, đính kèm nhãn chương (`Target Chapter`) và áp dụng các quy chuẩn kiểm toán.
4. **Lưu trữ Kế hoạch:** Ghi lại toàn bộ nội dung trên vào tệp `episodes/[slug]/02_research_plan.md`.

*🛑 CHỐNG CHẠY HỜI HỢT:* Chỉ khi kế hoạch nghiên cứu và trích xuất dữ liệu trên đã được hiển thị đầy đủ trên màn hình chat và lưu lại trên đĩa, tác nhân mới được phép thực thi các bước gọi công cụ tiếp theo.

### Bước 4: Thực thi Tương tác NotebookLM (Nạp nguồn & Trích xuất)
1. **DEEP RESEARCH EXECUTION (Nạp nguồn):** Chạy duy nhất một công cụ `mcp_notebooklm-mcp_deep_research` với tham số `query` là Prompt nạp nguồn cấu trúc đã thiết kế ở Bước 3.
2. **EXTRACTION & VERIFICATION (Trích xuất):** Chạy `mcp_notebooklm-mcp_batch_to_vault` để trích xuất dữ liệu theo danh sách câu hỏi đã thiết kế, lưu vào `episodes/[slug]/research_vault/` và tiến hành đối chiếu số liệu.
3. **SUPPLEMENT & SYNTHESIZE:** Tạo tệp `02_research_map.md` (Bản đồ tọa độ) và `02_research_synthesis.md` (Bản tóm tắt cơ chế vĩ mô).

### Bước 5: Báo cáo kết quả
Sau khi hoàn tất, hiển thị tóm tắt:
- Số sources đã nạp vào notebook
- Số file đã tạo trong research_vault/
- Bảng data points chính (thesis + counter-thesis)
- Data gaps còn thiếu (nếu có)

## Human Approval Gate
Sau khi hoàn tất Research Map → DỪNG và chờ user duyệt trước khi chuyển sang pha tiếp theo.

## Tham chiếu
- SKILL: `.agents/skills/deep_researcher/SKILL.md`
- Persona: `.agents/personas/the_research_scientist.md`
- Librarian: `.agents/skills/notebooklm_librarian/SKILL.md`
- Core: `00_core/brand_safety_guidelines.md`
