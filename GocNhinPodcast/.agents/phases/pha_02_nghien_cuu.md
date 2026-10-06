# Thẻ Pha 2: Nghiên cứu sâu

**Mục tiêu.** Trả lời các ô ma trận chưa phân biệt được giả thuyết và các câu hỏi con "chưa rõ" có ảnh hưởng cao, bằng nguồn gốc kiểm được; đồng thời thu thập Kho vật chứng (`VC-xx`) có ngày giờ, chủ thể và nguồn mở được cho các câu hỏi lớn của Pha 1. Không nghiên cứu lại thứ đã có nguồn.

## Đọc, theo thứ tự
1. `00_bang_gia_thuyet.md` mục 2b (ô chưa phân biệt) và cây câu hỏi trong `01_global_vision_synthesis.md`.
2. `.agents/workflows/deep_research.md` và `.agents/skills/deep_researcher/SKILL.md` (Bước 1–2: cách dùng engine, tư duy viết file kế hoạch).
3. `03_playbooks/deep_research_orchestration.md`: checklist Claude duyệt kế hoạch.
4. Persona: `the_policy_analyst.md`, `the_industrial_economist.md`; thêm `the_capital_markets_analyst.md` nếu đề tài thuộc thị trường vốn.

## Không cần đọc
Skill viết, outline, `00_core` về giọng.

## Cách làm
- `02_research_plan.md`: mỗi prompt ghi mã ô `[H?↔H?]` hoặc mã câu hỏi `[CH??]`. Luôn có nguồn phản biện. Nguồn sơ cấp (PDF luật, quyết định, hồ sơ) thì thêm vào notebook trước khi trích xuất.
- Kế hoạch nghiên cứu thêm câu hỏi trích xuất nhắm vào vật chứng (`VC-xx`) cho những câu hỏi lớn của Pha 1, không chỉ nhắm vào con số.
- Chạy NotebookLM bằng engine `scripts/notebooklm_engine/research_run.py`. Báo cáo do NotebookLM tự sinh **không** tính là nguồn.
- Con số và vật chứng quan trọng (quyết định, văn bản, công trình, khoảnh khắc có ngày giờ và chủ thể đứng sau) phải mở nguồn gốc và lưu câu nguyên văn kèm URL, ngày vào `research_raw/`. Vault có thể trích sai (ví dụ v4: vault ghi 10:00–20:00, phán quyết gốc ghi 8:00–20:00). Cấm cảnh dựng lại hay nhân vật bịa.
- Lập Kho vật chứng (`VC-01` đến `VC-XX`) trong `02_research_map.md` (và sổ `00_so_du_kien.md`), không bắt buộc với tập đang chạy trước ngày 06/10/2026.

## Đầu ra
`02_research_plan.md`, `research_vault/`, `research_raw/`, `02_research_map.md` (có Kho vật chứng `VC-xx`), `02_research_synthesis.md` (tối đa 3.000 từ), hàng mới trong sổ kèm vị trí nguồn.

## Cổng và dừng
Chạy `python3 scripts/kiem_pha.py <slug> --pha 2` (kế hoạch phải ĐẠT trước khi nạp nguồn). User duyệt research map.
