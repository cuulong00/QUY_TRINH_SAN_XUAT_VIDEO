# /deep_research — Nghiên cứu sâu NotebookLM

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
// turbo
1. `view_file` → `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/personas/the_macro_financial_researcher.md`
2. `view_file` → `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/skills/deep_researcher/SKILL.md`
3. `view_file` → `/Users/pro16/Documents/VideoProject/Dong_Chay/.agents/skills/notebooklm_librarian/SKILL.md`

### Bước 3: Lên Kế Hoạch & Thiết Kế Truy Vấn (RESEARCH PLANNING GATE)
Tác nhân phải thiết lập và xuất bản tệp `episodes/[slug]/02_research_plan.md` chứa đầy đủ kế hoạch nghiên cứu trước khi thực hiện bất kỳ lệnh nạp nguồn nào.

1. **Hiển thị Log Bắt Đầu Chạy:** In ra màn hình chat thông báo: *"Bắt đầu khởi chạy Pha 2: Data Mining & Verification cho tập [slug]"*.
2. **Thiết kế & Hiển thị Prompt Nạp nguồn Cấu trúc (Structured Ingestion Prompt Design):**
   - Thiết kế 1 Prompt nạp nguồn cấu trúc chuyên sâu bằng tiếng Anh/Việt bao quát 4 Dòng Chảy Vĩ Mô (Dòng vốn, Dòng hàng hóa, Dòng nhân khẩu học, Dòng thể chế) để nạp vào lệnh Deep Research.
3. **Thiết kế & Hiển thị Danh sách Câu hỏi Trích xuất (Extraction Queries List):**
   - Thiết kế 8–12 câu hỏi trích xuất tọa độ cụ thể để bóc tách dữ liệu thực chứng (chỉ số, mốc năm, cơ chế thủy lực/địa chính trị/tài chính).
   - Thêm câu hỏi trích xuất nhắm vào vật chứng cho những câu hỏi lớn của Pha 1, không chỉ nhắm vào con số.
4. **Lưu trữ Kế hoạch:** Ghi lại toàn bộ nội dung trên vào tệp `episodes/[slug]/02_research_plan.md`.

*🛑 CHỐNG CHẠY HỜI HỢT:* Phải hoàn thành `02_research_plan.md` trước khi gọi CLI nạp nguồn.

### Bước 4: Thực thi NotebookLM Direct RPC CLI (Nạp nguồn & Trích xuất)
Tuyệt đối KHÔNG dùng tool MCP giao diện web cũ. BẮT BUỘC sử dụng CLI Direct RPC trên môi trường `.venv`:
* Python: `/Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/python`
* CLI: `NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home /Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm`

1. **Tạo Master Notebook (nếu chưa có):**
   ```bash
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm create "[Tên Episode]" --json
   ```
   Lưu notebook ID vào `episodes/[slug]/.notebook_id` và URL vào `.notebook_url`.

2. **DEEP RESEARCH INGESTION (Nạp nguồn sâu — BẮT BUỘC `--mode deep`):**
   Chạy lệnh nạp nguồn bằng Deep Research:
   ```bash
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm \
   source add-research "<Structured Research Prompt>" \
   -n <notebook_id> \
   --mode deep \
   --import-all \
   --timeout 1800 \
   --json
   ```
   *LƯU Ý: Lệnh Deep Research mất từ 10 đến 25 phút. ĐỢI lệnh hoàn thành hoặc kiểm tra trạng thái background task. TUYỆT ĐỐI CẤM nhảy cóc sinh file giả khi lệnh chưa kết thúc!*

3. **VERIFY INGESTION GATE (Kiểm toán số lượng nguồn):**
   Chạy lệnh kiểm tra danh sách nguồn:
   ```bash
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm source list -n <notebook_id> --json
   ```
   *Yêu cầu bắt buộc: Phải có ít nhất ≥ 10 nguồn ở trạng thái `ready`.*

4. **BATCH EXTRACTION TO VAULT (Trích xuất Dữ liệu Chuyên sâu):**
   Duyệt qua danh sách 8–12 câu hỏi trích xuất bằng lệnh `notebooklm ask` và lưu kết quả vào `episodes/[slug]/research_vault/XX_ten_file.md`:
   ```bash
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/Dong_Chay/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/Dong_Chay/.venv/bin/notebooklm ask \
   -n <notebook_id> \
   --save-as-note -t "<Tiêu đề Note>" \
   "<Câu hỏi trích xuất cụ thể>"
   ```
   Mỗi file trong `research_vault/` phải có Document Provenance ghi rõ ID nguồn và số liệu kiểm chứng.

5. **TỔNG HỢP MAP & SYNTHESIS & CẬP NHẬT KHO VẬT CHỨNG:**
   - Thu thập các vật chứng thực tế vào Kho vật chứng (`VC-01` đến `VC-XX`) trong `02_research_map.md`: một quyết định, văn bản, công trình, khoảnh khắc có ngày giờ, chủ thể đứng sau và nguồn mở được; cấm cảnh dựng lại hay nhân vật bịa. Không bắt buộc với tập đang chạy trước ngày 06/10/2026.
   - Tạo `episodes/[slug]/02_research_map.md` (Bản đồ dữ liệu chứng cứ, Thesis, Counter-thesis ≥ 3, Cơ chế vĩ mô ≥ 5, và Kho vật chứng `VC-xx`).
   - Tạo `episodes/[slug]/02_research_synthesis.md` (La bàn định hướng vĩ mô ~1.500 từ).

### Bước 5: Chạy Script Kiểm Toán Cứng (Gatekeeper Verification)
Chạy script kiểm tra tự động trước khi báo cáo hoàn thành:
```bash
python3 scripts/verify_phase_gate.py --phase 2 --episode [slug]
```
Nếu script báo lỗi (FAIL) $\to$ BẮT BUỘC khắc phục, không được phép chuyển sang Pha 3.

### Bước 6: Báo cáo kết quả & Human Approval Gate
Hiển thị tóm tắt:
- Số sources đã nạp vào notebook (kèm link notebook)
- Danh sách các file đã trích xuất trong `research_vault/`
- Bảng đối chiếu Thesis vs Counter-Thesis
- Kho vật chứng (VC-xx) đã thu thập (vật chứng, ngày giờ, chủ thể, nguồn mở được)
- DỪNG và chờ user duyệt trước khi chuyển sang Pha 3 (`/build_brief`).

## Tham chiếu
- SKILL: `.agents/skills/deep_researcher/SKILL.md`
- Persona: `.agents/personas/the_macro_financial_researcher.md`
- Librarian: `.agents/skills/notebooklm_librarian/SKILL.md`
- Core: `00_core/financial_boundaries.md`
