---
name: notebooklm-librarian
description: "High-speed NotebookLM Direct RPC Agent Skill (powered by notebooklm-py). The central deep research hub and knowledge synthesizer. MUST BE USED to create master notebooks, run deep research, ingest sources, and batch extract grounded insights to research_vault."
---

# NotebookLM Librarian — Quản Gia Tri Thức & Deep Research Engine (RPC Native)

> 🛑 **MANDATORY INSTRUCTION (LƯU Ý CỐT LÕI):**
> NotebookLM là **Trái Tim Dữ Liệu (Central Research Hub)** của toàn bộ tập video.
> Hệ thống sử dụng **Giao thức Direct RPC API (`notebooklm-py`)** chạy trên môi trường `.venv_notebooklm` (không qua trình duyệt Playwright chậm chạp) để đảm bảo tốc độ phản hồi tính bằng giây, độ ổn định tuyệt đối và khả năng chống ảo giác 100%.

---

## ⚡ MÔI TRƯỜNG & BIẾN MÔI TRƯỜNG CỐ ĐỊNH (BẮT BUỘC)
* **Thư mục Profile / Session:** `NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/HieuBietHon/.notebooklm_home`
* **Đường dẫn CLI:** `/Users/pro16/Documents/VideoProject/HieuBietHon/.venv_notebooklm/bin/notebooklm`
* **Python Executable:** `/Users/pro16/Documents/VideoProject/HieuBietHon/.venv_notebooklm/bin/python`
* ⚠️ **LƯU Ý QUAN TRỌNG VỀ SANDBOX (`BypassSandbox: true`):** Khi Agent gọi lệnh `run_command` để thực thi CLI `notebooklm` hoặc Python SDK, **BẮT BUỘC phải bật `BypassSandbox: true`** để cho phép kết nối mạng ra máy chủ Google, tránh bị proxy sandbox chặn trả về lỗi giả mạo `403 Forbidden`.

---

## 🧭 NGUYÊN TẮC CỐT LÕI

### Quy tắc 0: 1 VIDEO = 1 MASTER NOTEBOOK DUY NHẤT (BẮT BUỘC)
* **CẤM:** Không tạo nhiều notebook vụn vặt cho cùng một tập phim.
* **BẮT BUỘC:** Mỗi episode chỉ có **MỘT (01) Master Notebook**.
* **Cross-Session Persistence:**
  1. Khi tạo notebook: Lưu `notebook_id` vào tệp `episodes/[slug]/.notebook_id` (và URL vào `episodes/[slug]/.notebook_url`).
  2. Trước mọi lần thao tác: Đọc `notebook_id` từ file để truyền cờ `-n <notebook_id>` vào mọi lệnh CLI/SDK.

---

### Quy tắc 1: CHẾ ĐỘ NGHIÊN CỨU SÂU BẮT BUỘC (`--mode deep`)
> ⛔ **MANDATE: NGHIÊM CẤM DÙNG TÌM KIẾM NHANH/NÔNG (`--mode fast`) KHI LÀM DEEP RESEARCH CHO VIDEO.**
> Quá trình nghiên cứu chuyên sâu bắt buộc phải dùng **`--mode deep`** để Google NotebookLM quét đa tầng qua hàng chục nguồn học thuật, báo cáo chính phủ, văn bản pháp lý, tổ chức thống kê quốc tế và bài báo phân tích chuyên sâu.

* **Cú pháp Lệnh Deep Research & Auto-Import:**
  ```bash
  NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/HieuBietHon/.notebooklm_home \
  /Users/pro16/Documents/VideoProject/HieuBietHon/.venv_notebooklm/bin/notebooklm \
  source add-research "<Structured Research Query>" \
  -n <notebook_id> \
  --mode deep \
  --import-all \
  --timeout 1800 \
  --json
  ```
* **Thời gian xử lý Deep Mode:** Chế độ `deep` thường kéo dài từ 2 đến 15 phút tùy độ phức tạp của đề tài. Nếu chạy nền, dùng cờ `--no-wait` và theo dõi qua `notebooklm research wait -n <notebook_id> --timeout 1800`.

---

### Quy tắc 2: ĐỊNH DẠNG TRÍCH XUẤT NGHIÊM NGẶT (Strict Grounding & Citations)
* **CẤM:** Không bao giờ hỏi NotebookLM những câu chung chung như "Hãy tóm tắt tất cả".
* **BẮT BUỘC:** Phải hỏi có tính định hướng, bóc tách cơ chế vĩ mô, số liệu thực chứng, mâu thuẫn chính sách.
* **Citations & Footnotes:** Luôn dùng `--json` hoặc `--save-as-note` để NotebookLM trả về danh sách trích dẫn nguồn (references / citations) xác thực từng số liệu.

---

### Quy tắc 3: QUY TRÌNH BATCH EXTRACTION TO VAULT (Xuất Dữ liệu ra Vault)
1. **Khởi tạo thư mục Vault:** `episodes/[slug]/research_vault/`
2. **Bộ câu hỏi trích xuất (8 – 12 câu):** Bám sát Khung tuyến kịch bản (Trajectory Outline). Mỗi câu hỏi bắt buộc chèn lệnh ép Freshness:
   > *"Ưu tiên dữ liệu mới nhất (2024–2026). Bỏ qua dữ liệu cũ trước 2023 trừ khi so sánh lịch sử. Trình bày dưới dạng báo cáo chuyên nghiệp: H2/H3, bảng biểu số liệu, trích dẫn nguồn cụ thể. Không lấy văn bản rác."*
3. **Thực thi trích xuất:** Gọi script Python hoặc vòng lặp CLI `notebooklm ask --prompt-file ... -n <notebook_id> --json` để lưu trực tiếp từng câu trả lời thành các file `research_vault/XX_topic.md`.

---

### Quy tắc 4: QUẢN LÝ NGUỒN SƠ CẤP (Primary Sources Injection)
Ngoài tính năng Deep Research từ Web, Agent có thể nạp trực tiếp tài liệu nội bộ, PDF báo cáo, đường link YouTube hoặc URL báo chí:
```bash
# Nạp file PDF / Văn bản
notebooklm source add ./path/to/report.pdf -n <notebook_id>

# Nạp URL bài báo chuyên ngành
notebooklm source add https://baochinhphu.vn/... -n <notebook_id>
```

---

## 🛠️ DANH MỤC LỆNH CLI PHỔ BIẾN CHO AGENT

| Hành động | Lệnh CLI (`NOTEBOOKLM_HOME` bắt buộc) |
| :--- | :--- |
| **Kiểm tra Auth** | `notebooklm auth check --test` |
| **Tạo Master Notebook** | `notebooklm create "Tên Episode" --json` |
| **Liệt kê Notebooks** | `notebooklm list --json` |
| **Deep Research (Sâu)** | `notebooklm source add-research "<Query>" -n <id> --mode deep --import-all --timeout 1800` |
| **Kiểm tra Danh sách Nguồn** | `notebooklm source list -n <id> --json` |
| **Truy vấn RAG & Lưu Note** | `notebooklm ask --prompt-file <file.txt> -n <id> --save-as-note -t "<Tiêu đề>" --json` |
| **Sinh Artifacts (Báo cáo)** | `notebooklm generate report -n <id> --language vi` |
