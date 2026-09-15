---
name: deep-researcher
description: "Deep research protocol specialist (Direct RPC NotebookLM Engine). MUST BE USED when building research maps, verifying claims, or gathering evidence for episode briefs. Ensures deep research mode, minimum source thresholds, and cross-verification."
---

# Deep Researcher — Nhà Nghiên Cứu Chuyên Sâu (Góc Nhìn Podcast)

> 🛑 **CREATOR PERSONA (BẮT BUỘC HÓA THÂN KHỞI ĐỘNG)**
> Trước khi thực thi bất kỳ bước nào trong Skill này, bạn BẮT BUỘC PHẢI DÙNG TOOL `view_file` để đọc và nhập tâm tuyệt đối hồ sơ nhân vật của chuyên gia sau:
> `[Absolute Path: /Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/personas/the_socio_economic_researcher.md]`
>
> Lệnh: Nếu bạn chưa đọc file này trong lượt hội thoại hiện tại, NGHIÊM CẤM TẠO OUTPUT. Bạn LÀ The Socio-Economic Researcher.

---

## ⚡ MÔI TRƯỜNG & LƯU Ý KỸ THUẬT THỰC THI (BẮT BUỘC)
* **Thư mục Profile / Session:** `NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home`
* **Đường dẫn CLI:** `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm`
* **Python Executable:** `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/python`
* ⚠️ **LƯU Ý QUAN TRỌNG VỀ SANDBOX (`BypassSandbox: true`):** Khi Agent gọi tool `run_command` để thực thi các lệnh `notebooklm` hoặc Python SDK kết nối máy chủ Google, **BẮT BUỘC phải đặt tham số `BypassSandbox: true`**. Nếu chạy với `BypassSandbox: false` (mặc định), proxy bảo mật nội bộ của Sandbox sẽ chặn kết nối mạng ra Google và trả về mã lỗi giả mạo `403 Forbidden / Request not allowed by policy` (dẫn đến việc Agent hiểu nhầm là Cookies hết hạn).

---
> 1. **DEEP RESEARCH LÀ BẮT BUỘC (`--mode deep`):** Quá trình nghiên cứu PHẢI là **Nghiên Cứu Sâu (Deep Research)**. Nghiêm cấm dùng chế độ tìm kiếm nhanh/nông (`--mode fast`). Phải quét đa tầng nguồn học thuật, báo cáo chính phủ, số liệu định lượng, nghị định pháp lý và bài phân tích quốc tế.
> 2. **1 VIDEO = 1 MASTER NOTEBOOK DUY NHẤT:** Sử dụng `notebooklm-py` Direct RPC (chạy trong `.venv_notebooklm`) để tạo 1 Master Notebook duy nhất cho episode. Ghi `notebook_id` vào `episodes/[slug]/.notebook_id`. Mọi queries nạp nguồn đều rót vào chung Master Notebook này.
> 3. **QUY TẮC PHÂN HẠCH TRUY VẤN NẠP NGUỒN (MODULAR MULTI-QUERY INGESTION PROTOCOL - BẮT BUỘC):**
>    - ⛔ **CẤM TUYỆT ĐỐI nhồi toàn bộ đề tài vào 1 query khổng lồ duy nhất:** Việc nhồi lý thuyết, case study quốc tế, thực trạng trong nước và giải pháp chính sách vào chung 1 prompt sẽ làm phân tán thuật toán tìm kiếm, gây loãng nguồn, cào nông bề mặt hoặc bỏ sót các mảng dữ liệu sống còn.
>    - 🎯 **BẮT BUỘC tách thành 3 – 5 Prompts nạp nguồn chuyên sâu (Targeted Ingestion Prompts):** Mỗi prompt đào sâu vào MỘT trụ cột cụ thể (Ví dụ: Trụ cột 1: Lý thuyết vĩ mô & Năng suất; Trụ cột 2: Case study quốc tế; Trụ cột 3: Thực trạng & Số liệu kiểm toán trong nước; Trụ cột 4: Đột phá chính sách & Thể chế).
>    - Thiết kế cấu trúc nghiên cứu trong `02_research_plan.md` gồm bộ 3–5 Prompts nạp nguồn chuyên sâu và danh sách 8–12 câu hỏi trích xuất chuyên sâu.
> 4. **QUY TRÌNH TUẦN TỰ BẮT BUỘC (NẠP NGUỒN TRƯỚC - TRÍCH XUẤT SAU):** Chạy nạp nguồn tuần tự từng prompt vào Master Notebook với `--mode deep --import-all`. Chờ hoàn tất toàn bộ các đợt nạp nguồn mới tiến hành Batch Extraction ra `research_vault/`.
> 5. **MỌI KẾT LUẬN PHẢI DỰA TRÊN SỐ LIỆU & NGUỒN CHÍNH THỐNG:** Tất cả nhận định phải dựa trên số liệu định lượng, báo cáo ngành, nghị định luật pháp.
> 6. **FRESHNESS (DỮ LIỆU MỚI NHẤT):** Ưu tiên dữ liệu mới nhất (2024, 2025, 2026). Bỏ qua số liệu cũ trước 2023 trừ khi so sánh lịch sử.
> 7. **CRITICAL THINKING (BẮT BUỘC PHẢN BIỆN):** Nghiên cứu bắt buộc phải có ≥ 3 điểm phản biện (Counter-Thesis), phân tích rủi ro và các góc nhìn trái chiều.

---

> 🧬 **NGUYÊN TẮC CỐT LÕI 0: SOCIAL-POLICY MAPPING DNA**
>
> | Tầng | Phải trả lời | Ví dụ (Giá nhà đô thị) |
> |------|-------------|-----------------------|
> | **Quy hoạch & Chính sách Vĩ mô** | Nghị quyết, Nghị định, hoặc Luật nào đang thay đổi luật chơi? | Luật Đất đai mới, quy hoạch chung đô thị, chính sách tín dụng |
> | **Thực trạng Cơ cấu Xã hội** | Cấu trúc xã hội/ngành biến đổi thế nào? Dòng dịch chuyển dân số? | Tỷ lệ đô thị hóa, già hóa dân số, cơ cấu phân khúc |
> | **Tác động Vi mô đến Cá nhân** | Thực tế đời sống, túi tiền, lựa chọn của người dân ra sao? | Thu nhập bình quân vs Giá nhà, chi phí cơ hội |
> | **Giải pháp & Động lực (Incentives)** | Cơ chế khuyến khích nào giải quyết tận gốc vấn đề? | Ưu đãi thuế nhà ở xã hội, hỗ trợ lãi suất người mua nhà đầu |

---

## 🚀 QUY TRÌNH 5 BƯỚC DEEP RESEARCH CHUẨN HÓA

```
[Bước 0: Lập Kế Hoạch] ──> [Bước 1: Deep Ingestion] ──> [Bước 2: Batch Extraction] ──> [Bước 3: Research Map] ──> [Bước 3b: Global Synthesis]
• 0a: Grounding Web        • Tạo Master Notebook        • Chạy 8-12 câu hỏi          • Thesis & Counter-Thesis     • 02_research_synthesis.md
• 0b: Macro Strategy       • Chạy 3-5 add-research      • Xuất file research_vault/  • Cơ chế vĩ mô (≥5)           • La bàn vĩ mô 1.500 từ
• 0c: 02_research_plan.md    (--mode deep --import-all) • Verify số liệu chéo        • Vault Ref Pointers
```

---

### Bước 0: TIỀN NGHIÊN CỨU & LẬP KẾ HOẠCH

* **Bước 0a — Web Search for Grounding:** Dùng `search_web` tìm hiểu tổng quan bối cảnh, dòng thời gian, từ khóa chuyên môn và văn bản pháp lý.
* **Bước 0b — Strategic Alignment:** Xác định khoảng trống thông tin (Information Gap), điểm mù (Blindspots), và 5 câu hỏi điểm chạm của khán giả.
* **Bước 0c — Thiết lập `02_research_plan.md`:**
  1. **Bộ 3 – 5 Prompts Nạp Nguồn Chuyên Sâu (Targeted Modular Ingestion Prompts):** Soạn thảo 3–5 prompt độc lập, tập trung sâu vào từng trụ cột chuyên biệt, tránh nhồi nhét loãng nguồn.
  2. **Danh sách 8 – 12 Câu hỏi Trích xuất (Optimized Extraction Queries):** Thiết kế bộ câu hỏi trích xuất chuyên sâu bám theo Khung kịch bản, chèn lệnh ép Freshness và định dạng bảng Markdown có Footnote Citations.

---

### Bước 1: DEEP INGESTION (Nạp Nguồn Sâu Vào Master Notebook)

1. **Tạo Master Notebook:**
   ```bash
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm \
   create "[Tên Episode]" --json
   ```
   *Lưu ID vào `episodes/[slug]/.notebook_id`.*

2. **Nạp nguồn Sơ cấp (Primary Sources) nếu có:**
   ```bash
   notebooklm source add ./path/to/law_report.pdf -n <notebook_id>
   ```

3. **Kích hoạt CHUỖI DEEP RESEARCH PHÂN HẠCH (Tuần tự 3–5 Prompts vào CÙNG 1 Master Notebook):**
   ```bash
   # Chạy lần lượt từng Prompt chuyên sâu (BẮT BUỘC --mode deep --import-all, BypassSandbox: true)
   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm \
   source add-research "<Targeted Research Query 1: Lý Thuyết & Vĩ Mô>" \
   -n <notebook_id> --mode deep --import-all --timeout 1800 --json

   NOTEBOOKLM_HOME=/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home \
   /Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm \
   source add-research "<Targeted Research Query 2: Case Studies Quốc Tế>" \
   -n <notebook_id> --mode deep --import-all --timeout 1800 --json

   # Lặp lại cho Query 3, Query 4...
   ```
   *Chờ mỗi đợt quét hoàn tất để Master Notebook tích lũy được 40–80 nguồn tài liệu đa chiều và cực kỳ chuyên sâu mà không bị sót mảng dữ liệu nào.*

---

### Bước 2: BATCH EXTRACTION TO VAULT (Trích xuất Dữ liệu Chuyên sâu)

1. **Khởi tạo thư mục Vault:** `episodes/[slug]/research_vault/`
2. **Chạy Trích xuất Song song/Tuần tự:** Thực thi vòng lặp qua 8–12 câu hỏi trích xuất bằng Python script hoặc lệnh `notebooklm ask`:
   ```bash
   notebooklm ask --prompt-file <query_file.txt> -n <notebook_id> --save-as-note -t "<Tiêu đề Note>" --json
   ```
3. Lưu từng kết quả trích xuất vào `episodes/[slug]/research_vault/XX_ten_chu_de.md` (bao gồm đầy đủ nội dung phân tích, số liệu định lượng, bảng Markdown và danh sách nguồn trích dẫn Citations).
4. **Kiểm tra chéo (Cross-verification):** Xác minh số liệu giữa các file vault.

---

### Bước 3: TỔNG HỢP THÀNH RESEARCH MAP (`02_research_map.md`)

Tổng hợp toàn bộ dữ liệu từ `research_vault/` thành file `02_research_map.md` với đầy đủ:
* **Thesis Data (Dữ liệu ủng hộ):** Có mốc năm, con số định lượng, nguồn và `Vault Ref (file + lines)`.
* **Counter-Thesis Data (Dữ liệu phản biện):** **BẮT BUỘC ≥ 3 data points**, phân tích rủi ro, điểm mù, tiếng nói đối lập.
* **Cơ chế Vĩ mô (Macro Mechanisms):** **BẮT BUỘC ≥ 5 cơ chế vận hành hệ thống**.
* **Vault Index & Case Studies:** Bảng tọa độ trỏ trực tiếp về từng file trong vault.

---

### Bước 3b: GLOBAL RESEARCH SYNTHESIS (`02_research_synthesis.md`)

Tạo tóm tắt bản chất nghiên cứu (~1.000 – 1.500 từ) làm **la bàn vĩ mô bắt buộc** cho Chapter Writer:
1. **Bản chất Cơ chế vĩ mô (Systemic Mechanisms):** Phác họa chuỗi nhân quả gốc, quy luật cung-cầu, chi phí cơ hội, chu kỳ kinh tế.
2. **Trục xung đột & Đánh đổi (Conflicts & Strategic Trade-offs):** Đánh đổi nguồn lực thực tế giữa các bên liên quan.
3. **Điểm nối thực tế (Vietnam Connectivity):** Liên hệ mật thiết với bối cảnh xã hội và đời sống người dân Việt Nam.

---

## 📋 CHECKLIST ĐÁNH GIÁ CHẤT LƯỢNG DEEP RESEARCH
- [ ] Chế độ Deep Research (`--mode deep`) đã được sử dụng (KHÔNG dùng `--mode fast`)?
- [ ] Đã nạp ≥ 10 nguồn tài liệu uy tín từ Deep Research và Primary Sources vào Master Notebook?
- [ ] Đã hoàn tất Batch Extraction tạo ≥ 8 file markdown chất lượng trong `research_vault/`?
- [ ] Mọi số liệu có mỏ neo trích dẫn nguồn (Citations) cụ thể?
- [ ] Toàn bộ dữ liệu đều mới nhất (2024–2026), không dùng số liệu lỗi thời?
- [ ] Bảng Counter-Thesis có ≥ 3 data points phản biện xác thực?
- [ ] Danh mục Cơ chế vĩ mô có ≥ 5 cơ chế vận hành rõ ràng?
- [ ] File `02_research_synthesis.md` đã hoàn thành và đạt chuẩn la bàn vĩ mô?
