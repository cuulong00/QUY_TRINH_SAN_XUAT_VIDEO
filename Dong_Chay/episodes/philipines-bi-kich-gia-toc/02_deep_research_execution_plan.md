<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/philipines-bi-kich-gia-toc/02_deep_research_execution_plan.md
- Activated Persona: the_macro_financial_researcher (.agents/personas/the_macro_financial_researcher.md) + the_critical_auditor (.agents/personas/the_critical_auditor.md)
- Activated Skill: deep_researcher / notebooklm (.agents/skills/deep_researcher/SKILL.md)
- Source Documents Consulted:
  * episodes/philipines-bi-kich-gia-toc/.notebook_id (e57ae0dd-22e8-4cd2-926b-9db5ad26844a)
  * episodes/philipines-bi-kich-gia-toc/02_research_plan.md
  * episodes/philipines-bi-kich-gia-toc/trajectory_outline.md
- Execution Timestamp: 2026-09-05 12:45
-->

# 02_deep_research_execution_plan.md — Kế Hoạch Thực Thi Deep Research Qua NotebookLM API

> **Tập phim:** Bi Kịch Của "Đứa Trẻ Dân Số Vàng": Căn Bệnh Nhảy Cóc Công Nghiệp, Bẫy Địa Tô Gia Tộc Và Bàn Cờ Sinh Tử Philippines  
> **Mã tập:** `philipines-bi-kich-gia-toc`  
> **Master Notebook ID:** `e57ae0dd-22e8-4cd2-926b-9db5ad26844a`  
> **Master Notebook URL:** `https://notebooklm.google.com/notebook/e57ae0dd-22e8-4cd2-926b-9db5ad26844a`  
> **Công nghệ thực thi:** Google NotebookLM Direct RPC Native Engine (`notebooklm-py` v0.8.1) chạy trên môi trường Python `.venv`.

---

## 1. Kiến Trúc Vận Hành & Nguyên Tắc Bất Biến

1. **Quy tắc 1 Video = 1 Master Notebook:** Toàn bộ nguồn tài liệu và các truy vấn trích xuất chỉ nạp và thực thi trên duy nhất một Master Notebook (`e57ae0dd-22e8-4cd2-926b-9db5ad26844a`). Nghiêm cấm phân mảnh notebook làm hỏng khả năng đối chiếu chéo (Cross-referencing RAG).
2. **Chế độ Deep Research Bắt buộc:** Tất cả lệnh nạp nguồn qua Google NotebookLM API bắt buộc phải kích hoạt 2 cờ:
   - `--mode deep`: Kích hoạt mô hình AI đa tầng quét sâu vào tài liệu hàn lâm, báo cáo chính phủ và sách trắng.
   - `--import-all`: Tự động nạp toàn bộ các nguồn kiểm chứng tìm được vào sổ tay Master.
3. **Môi trường BypassSandbox:** Mọi lệnh CLI `notebooklm` thực thi qua hệ thống bắt buộc chạy với `BypassSandbox: true` để tránh proxy sandbox nội bộ chặn kết nối tới máy chủ Google.

---

## 2. Danh Mục 8 Truy Vấn Deep Research Nạp Nguồn (Ingestion Batch)

Dưới đây là 8 truy vấn tiếng Anh chuẩn học thuật được thiết kế để nạp hơn 50–70 nguồn tài liệu sơ cấp từ World Bank, IMF, ADB, BSP, PSA, USDA, DOE, Lowy Institute, CSIS và truyền thông quốc tế vào Master Notebook:

```bash
# 1. Macroeconomics & Căn bệnh Nhảy cóc (Premature Deindustrialization)
.venv/bin/notebooklm source add-research "Philippines macroeconomic structure GDP growth demographic dividend premature deindustrialization manufacturing share Dani Rodrik PSA World Bank IMF" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 2. Bãi thu Địa tô & 100 Gia tộc Tài phiệt (Oligarchic Dynasties)
.venv/bin/notebooklm source add-research "Philippines political dynasties oligarchs conglomerates Sy SM Prime Ayala Gokongwei Lopez Villar Ramon Ang San Miguel crony capitalism rent-seeking" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 3. Tử huyệt Giá điện & Đạo luật EPIRA 2001 (Power Chokehold)
.venv/bin/notebooklm source add-research "Philippines electricity prices tariffs Meralco EPIRA 2001 power generation cartels kWh rates industrial manufacturing competitiveness DOE" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 4. Khủng hoảng Lúa gạo & Nghịch lý Cái nôi IRRI (Rice Import Trap)
.venv/bin/notebooklm source add-research "Philippines rice imports world largest importer USDA IRRI Los Banos CARP agrarian reform Vietnam rice trade DA BPI food inflation" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 5. Kiều hối OFW & Cơn địa chấn AI đe dọa BPO (BPO vs Generative AI)
.venv/bin/notebooklm source add-research "Philippines BPO IT-BPM industry IBPAP generative AI voice agents impact customer service OFW personal cash remittances BSP" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 6. Quả bom Nợ công & Tranh cãi Quỹ Maharlika (Fiscal Cliff & Debt)
.venv/bin/notebooklm source add-research "Philippines national debt 19 trillion peso debt-to-GDP ratio Bureau of Treasury Maharlika Investment Fund LandBank DBP fiscal strain" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 7. Nội chiến Vương triều Marcos Jr. vs Duterte (Dynastic Civil War)
.venv/bin/notebooklm source add-research "Marcos Duterte feud UniTeam split Sara Duterte impeachment Senate trial Rodrigo Duterte ICC The Hague confidential funds" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait

# 8. Bàn cờ Biển Đông & 9 Căn cứ Quân sự EDCA (Geopolitical Meat Grinder)
.venv/bin/notebooklm source add-research "Philippines EDCA US military bases Cagayan Isabela Palawan South China Sea West Philippine Sea Ayungin Scarborough shoal tensions China MDT 1951" -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --mode deep --import-all --no-wait
```

---

## 3. Quy Trình Giám Sát & Quản Lý Tiến Trình Nghiên Cứu (Research Monitor)

Khi kích hoạt các lệnh `--no-wait`, hệ thống quản lý tiến trình của NotebookLM hoạt động ngầm. Sử dụng các lệnh sau để theo dõi:

```bash
# Kiểm tra trạng thái các tác vụ nghiên cứu đang chạy:
.venv/bin/notebooklm research status -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a

# Chờ đợi đến khi tất cả các nguồn nạp hoàn tất:
.venv/bin/notebooklm research wait -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --timeout 1800

# Liệt kê toàn bộ danh sách nguồn tài liệu đã được nạp vào Master Notebook:
.venv/bin/notebooklm source list -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a
```

---

## 4. Kế Hoạch Trích Xuất 10 Chuyên Đề Vĩ Mô Vào `research_vault/`

Sau khi toàn bộ nguồn tài liệu được đồng bộ vào Master Notebook, hệ thống sẽ thực thi tự động script Python (`scripts/extract_philippines_vault.py`) để gửi các prompt phân tích chuyên sâu qua lệnh `notebooklm ask -n e57ae0dd-22e8-4cd2-926b-9db5ad26844a --json` và lưu thành 10 tệp chuyên đề vĩ mô độc lập:

1. `research_vault/01_demographic_dividend_vs_poverty_trap.md`: Giải phẫu cơ cấu dân số vàng 115 triệu dân, tuổi trung vị 25,3 và nghịch lý xuất khẩu lao động.
2. `research_vault/02_premature_deindustrialization_dani_rodrik.md`: Mổ xẻ lý thuyết phi công nghiệp hóa sớm, sự co cụm của ngành chế tạo (<18% GDP) và bài học so sánh với Việt Nam (~25% GDP).
3. `research_vault/03_oligarchic_cartels_and_rent_seeking.md`: Bóc trần sự thao túng của 100 gia tộc (Sy, Ayala, Gokongwei, Lopez, Villar, San Miguel) và cơ chế bòn rút địa tô.
4. `research_vault/04_electricity_cost_chokehold_meralco_epira.md`: Phân tích Đạo luật EPIRA 2001, biểu giá điện Meralco (14,78 PHP/kWh) và sự hủy hoại năng lực cạnh tranh FDI.
5. `research_vault/05_rice_crisis_and_agricultural_abandonment.md`: Giải mã nghịch lý cái nôi IRRI nhập khẩu gạo số 1 thế giới (5,0–5,7 triệu tấn) và sự phụ thuộc 75% vào nông dân Việt Nam.
6. `research_vault/06_bpo_under_ai_siege_and_ofw_remittance_loop.md`: Báo động cơn địa chấn Generative AI xóa sổ việc làm tổng đài BPO ($40B) và vòng lặp kiều hối ($39,6B).
7. `research_vault/07_sovereign_debt_cliff_and_maharlika_fund.md`: Quả bom nợ công 19,39 nghìn tỷ Peso (66% GDP Q2/2026) và tranh cãi rút vốn ngân hàng nhà nước của Quỹ Maharlika.
8. `research_vault/08_dynastic_civil_war_marcos_vs_duterte.md`: Toàn cảnh phiên tòa luận tội Phó Tổng thống Sara Duterte (7/2026), Rodrigo Duterte hầu tòa ICC tại The Hague (11/2026) và cuộc chiến vương triều.
9. `research_vault/09_south_china_sea_edca_frontline_trap.md`: Bàn cờ Biển Đông, 9 căn cứ quân sự EDCA và sự đối lập sâu sắc với trường phái "Ngoại giao cây tre" Việt Nam.
10. `research_vault/10_systemic_synthesis_and_vietnam_comparison.md`: Bản tổng hợp ma trận đối soát vĩ mô toàn diện và bài học chiến lược sống còn cho các quốc gia đang phát triển.

---

## 5. Tiêu Chuẩn Nghiệm Thu Pha Nghiên Cứu (Acceptance Criteria)

* [ ] Master Notebook `e57ae0dd-22e8-4cd2-926b-9db5ad26844a` tích lũy tối thiểu **40–60 nguồn tài liệu** được kiểm chứng chính thức.
* [ ] 10 tệp trong `research_vault/` được trích xuất hoàn tất với đầy đủ số liệu định lượng, mốc thời gian và luận cứ phản biện.
* [ ] Cập nhật tọa độ tham chiếu trích dẫn 1-1 (`Vault Ref`) trong `02_research_map.md`.
