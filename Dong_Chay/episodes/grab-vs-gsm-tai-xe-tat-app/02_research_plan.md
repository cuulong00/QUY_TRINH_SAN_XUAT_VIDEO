<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/grab-vs-gsm-tai-xe-tat-app/02_research_plan.md
- Activated Persona: The Macro Economist + The Corporate Finance Analyst + The Critical Auditor
- Activated Skill: script-architect (.agents/skills/script_architect/SKILL.md)
- Source Documents Consulted:
  * episodes/grab-vs-gsm-tai-xe-tat-app/01_topic_qualification.md
  * deep_query_2026.txt
- Execution Timestamp: 2026-09-09 09:33
-->

# 02_research_plan.md — KẾ HOẠCH DEEP RESEARCH TOÀN DIỆN 2026 (SYSTEMIC RESEARCH PLAN)

## TẬP PHIM: TIẾNG KÊU CỨU DƯỚI LÒNG ĐƯỜNG: VÌ SAO TÀI XẾ CÔNG NGHỆ TẮT APP ĐÌNH CÔNG?
**Chế độ thực thi:** Google NotebookLM Direct RPC (Bắt buộc `--mode deep --import-all`, `BypassSandbox: true`)

---

## 1. Mục Tiêu Nghiên Cứu Hệ Thống (4 Trụ Cột)
Nghiên cứu được thiết kế để giải phẫu toàn diện 4 mắt xích của bài toán kinh tế gọi xe công nghệ năm 2026:
1. **Trụ cột 1:** Làn sóng tài xế Grab kêu gọi tắt app ngày 12-13/9/2026, cơ chế Dynamic Fare, tăng phí nền tảng 28/4/2026 và cách thuật toán Surge Pricing bẻ gãy đình công.
2. **Trụ cột 2:** Bóc trần Unit Economics thực tế và bẫy khấu hao nợ xe của tài xế GrabCar & GrabBike năm 2026.
3. **Trụ cột 3:** Cục diện thị phần Q1/2026 (Xanh SM 54.51%, Grab 40.92%, Gojek rút lui), doanh thu GSM 17.400 tỷ và cú sốc cạn kiệt cuốc xe đẩy tài xế vào chân tường.
4. **Trụ cột 4:** Ảo tưởng tháo chạy sang xe điện, Quyết định 876, bức tường trạm sạc V-GREEN, vòng kim cô kỷ luật 5 sao, phạt đỗ 1.000đ/phút, và sự chuyển dịch tất yếu sang Xanh SM Platform để IPO Hong Kong 2027.

---

## 2. Lệnh Thực Thi NotebookLM Direct RPC
- **Tệp prompt nguồn:** `episodes/grab-vs-gsm-tai-xe-tat-app/deep_query_2026.txt`
- **Lệnh CLI:**
  ```bash
  .venv/bin/notebooklm source add-research \
    --prompt-file episodes/grab-vs-gsm-tai-xe-tat-app/deep_query_2026.txt \
    -n 0c6bc1a7-7f75-4254-b521-6b4a79f7912c \
    --mode deep \
    --import-all \
    --timeout 1800
  ```

---

## 3. Danh Mục 5 Hồ Sơ Trích Xuất Vào `research_vault/`
1. `01_september_2026_grab_strike_and_dynamic_fare.md` (Đợt tắt app 12-13/9/2026, Dynamic Fare, tăng phí nền tảng 28/4/2026, Surge Pricing).
2. `02_market_triumvirate_and_gsm_shock_2026.md` (Thị phần Q1/2026 Xanh SM 54.51%, Gojek rút lui 9/2024, GSM 17.400 tỷ).
3. `03_unit_economics_realities_ice_vs_ev.md` (Đối soát 100km xăng vs điện, bẫy nợ xe ô tô, thu nhập thực nhận GrabBike).
4. `04_escape_illusion_and_gsm_platform_discipline.md` (Kỷ luật 5 sao, phạt trạm sạc V-GREEN 1.000đ/phút, Xanh SM Platform, IPO Hong Kong).
5. `05_precariat_sociology_and_the_grand_payoff.md` (Lao động bấp bênh Precariat, sự bất lực của bãi công tự phát, kết cục hội tụ).
