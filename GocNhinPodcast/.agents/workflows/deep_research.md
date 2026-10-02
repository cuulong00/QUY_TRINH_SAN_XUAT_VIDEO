# /deep_research — Nghiên cứu sâu NotebookLM (Góc Nhìn Podcast)

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
   - Một tập một notebook: engine `scripts/kg_registry/kb_research_run.py` tự tạo notebook khi chưa có và ghi `.notebook_id`; có rồi thì dùng lại.
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
1. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_industrial_economist.md`
2. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_policy_analyst.md`
2. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/deep_researcher/SKILL.md`
3. `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/notebooklm_librarian/SKILL.md`

### Bước 3: Lên Kế Hoạch & Thiết Kế Truy Vấn (RESEARCH PLANNING GATE)
Tác nhân phải thiết lập và xuất bản tệp `episodes/[slug]/02_research_plan.md` chứa đầy đủ kế hoạch nghiên cứu trước khi thực hiện bất kỳ lệnh gọi công cụ nào với NotebookLM.

1. **Hiển thị Log Bắt Đầu Chạy:** In ra màn hình chat thông báo: *"Bắt đầu khởi chạy Pha 2: Data Mining & Verification cho tập [slug]"*.
2. **Thiết Kế & Hiển Thị Bộ Prompts Nạp Nguồn Chuyên Sâu (Targeted Modular Ingestion Prompts):**
   - ⛔ **CẤM TUYỆT ĐỐI nhồi toàn bộ nội dung vào 1 query duy nhất** (làm phân tán và loãng nguồn của Deep Crawler).
   - Đọc `episodes/[slug]/00_bang_gia_thuyet.md` mục 2b (ô chưa phân biệt) và `01b_knowledge_audit.md` (GAP). Mỗi prompt nạp nguồn nhắm một hoặc vài ô/GAP cụ thể và ghi mã `[H?↔H? | GAP-…]`. Số prompt theo nút N1 trong hiến chương (phủ cao: ít, nhắm thẳng; phủ thấp: thêm vòng gom nền). Không viết prompt cho thứ kho đã trả lời được. Prompt phản biện (khía cạnh 5) luôn bắt buộc.
3. **Thiết kế & Hiển thị Danh sách Câu hỏi Trích xuất tối ưu (Optimized Extraction Queries):**
   - Thiết kế và hiển thị danh sách câu hỏi trích xuất, mỗi câu gắn mã ô ma trận hoặc GAP (`[H1↔H2 | GAP-L03]`), không gắn nhãn chương (Pha 2 chưa có chương). Số câu theo số ô chưa phân biệt.
4. **Lưu trữ Kế hoạch:** Ghi lại toàn bộ nội dung trên vào tệp `episodes/[slug]/02_research_plan.md`. Chạy `KB_GRAPH=kb_v2 scripts/kbaudit --check-plan [slug]` phải ĐẠT trước khi nạp nguồn.

*🛑 CHỐNG CHẠY HỜI HỢT:* Chỉ khi kế hoạch nghiên cứu và trích xuất dữ liệu trên đã được hiển thị đầy đủ trên màn hình chat và lưu lại trên đĩa, tác nhân mới được phép thực thi các bước gọi công cụ tiếp theo.

### Bước 4: Thực thi Tương tác NotebookLM (Nạp nguồn & Trích xuất)
1. **NẠP NGUỒN VÀ TRÍCH XUẤT (một engine):** Nạp nguồn và trích xuất của Pha 2 chạy qua **engine Direct RPC dùng chung** `scripts/kg_registry/kb_research_run.py` (gọi `NotebookLMClient` trực tiếp). Cách dùng nằm ở docstring đầu file: viết một file kế hoạch `01_management/kg_research/kb_plans/<slug>.json` (nguồn = prompt nạp, mỗi nguồn ghi mã ô/GAP; trích xuất = câu hỏi, mỗi câu một file vault), rồi chạy engine. Vì sao không gọi CLI từng lệnh: engine dùng lại `.notebook_id`, ghi `run_state.json` nên bị ngắt thì chạy lại là làm tiếp, chờ nghiên cứu sâu không bị cắt lượt, và vault ra đúng khuôn (bảng số trích dẫn) để nạp kho sau này. CLI `notebooklm` chỉ dùng cho kiểm tra lẻ: `auth check`, `list`, `source list`. Chạy cần `BypassSandbox: true`.
2. **ĐỐI CHIẾU:** tự mở lại nguồn gốc các câu then chốt trong vault (URL mở được, câu nguyên văn khớp, số đúng kỳ và phạm vi).
3. **CẬP NHẬT MA TRẬN VÀ SỔ DỮ KIỆN (phần E của form tư duy):** mỗi dữ kiện mới từ vault thêm một hàng `M-xx` vào `00_so_du_kien.md` (nhãn `verified_data` chỉ khi có câu nguyên văn + URL + ngày; không thì `market_analysis`). mỗi dữ kiện mới từ vault thành một hàng E trong `00_bang_gia_thuyet.md` (nguồn `vault/R0X` + câu nguyên văn + kỳ, phạm vi), chấm `+ / − / 0`; giả thuyết có bằng chứng ngược thì thu hẹp hoặc loại, ghi dòng lịch sử. Không được xóa giả thuyết mà không có hàng E ngược.
4. **SUPPLEMENT & SYNTHESIZE:** Tạo tệp `02_research_map.md` (Bản đồ tọa độ) và `02_research_synthesis.md` (Bản tóm tắt cơ chế vĩ mô). Synthesis kết bằng trạng thái ma trận: giả thuyết nào còn đứng, ô nào vẫn chưa phân biệt, bằng chứng BÁC nào còn đứng.

### Bước 5: Báo cáo kết quả
Sau khi hoàn tất, hiển thị tóm tắt:
- Số sources đã nạp vào notebook
- Số file đã tạo trong research_vault/
- Bảng data points chính (thesis + counter-thesis)
- Data gaps còn thiếu (nếu có)
- Trạng thái ma trận: số giả thuyết còn đứng / đã loại; ô chưa phân biệt còn lại; kết quả `kbaudit --check-evidence` sau Pha 2

## Human Approval Gate
Sau khi hoàn tất Research Map → DỪNG và chờ user duyệt trước khi chuyển sang pha tiếp theo.

## Tham chiếu
- SKILL: `.agents/skills/deep_researcher/SKILL.md`
- Persona: `.agents/personas/the_industrial_economist.md` + `.agents/personas/the_policy_analyst.md`
- Librarian: `.agents/skills/notebooklm_librarian/SKILL.md`
- Core: `00_core/brand_safety_guidelines.md`
