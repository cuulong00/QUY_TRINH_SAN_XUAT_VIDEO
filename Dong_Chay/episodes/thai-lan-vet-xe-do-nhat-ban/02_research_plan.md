# 02_research_plan.md — Kế Hoạch Nghiên Cứu Chuyên Sâu (Deep Research Plan)

> **Tập phim:** Cú Trượt Dài Của Con Hổ Đông Nam Á: Nợ Ngập Đầu, Lãi Suất 1% Và Nguy Cơ Đi Vào Vết Xe Đổ Nhật Bản  
> **Mã tập:** `thai-lan-vet-xe-do-nhat-ban`  
> **Master Notebook ID:** `b2b49222-8024-438f-9d67-db8951a5fdf5`  
> **Phương thức thực thi:** Google NotebookLM Direct RPC Native Engine (`notebooklm-py`) kết hợp RAG & Nguồn Kiểm Chứng Đa Tầng

---

## 1. Mục Tiêu & Phương Pháp Luận Nghiên Cứu

### A. Mục tiêu cốt lõi
* **Không thỏa hiệp với số liệu chung chung:** Mọi nhận định về khủng hoảng, nợ nần, bẫy thanh khoản và đứt gãy công nghiệp phải có số liệu định lượng chính xác (%, mốc năm, cơ quan công bố chính thức).
* **Bóc trần cơ chế ngầm:** Không chỉ mô tả hiện tượng "kinh tế khó khăn" mà phải giải phẫu cơ chế: tại sao lãi suất 1% không kích cầu được? tại sao nợ hộ gia đình 90% GDP lại làm tê liệt truyền dẫn tiền tệ? tại sao xe điện Trung Quốc lại làm đứt gãy chuỗi cung ứng linh kiện Thái Lan?
* **Đối chiếu lịch sử sắc lạnh:** Phân tích điểm giống và điểm khác biệt sống còn giữa kịch bản "Nhật Bản hóa" của Thái Lan và "Thập kỷ mất mát" thực tế của Nhật Bản thập niên 1990.

### B. Kiến trúc Nguồn lực & Master Notebook
* **Master Notebook duy nhất:** `b2b49222-8024-438f-9d67-db8951a5fdf5`
* **Quy mô nguồn nạp:** 61 nguồn tài liệu quốc tế và sơ cấp (trong đó 49 nguồn sẵn sàng), bao gồm:
  1. *Báo cáo chính sách tiền tệ & ngân hàng:* Bank of Thailand (BoT MPC Decisions 1/2026, 2/2026, 3/2026; Banking Sector Briefs Q4/2025, Q1/2026).
  2. *Định chế quốc tế:* World Bank (Long-Term Growth Scenarios for Thailand), IMF (Article IV Consultations & Regional Briefings), OECD (Economic Surveys Thailand 2025, Active Ageing in SEA).
  3. *Nghiên cứu tài chính & đầu tư:* HSBC ASEAN Research (Aris Dacanay), Oxford Economics (Louise Loo), Bangkok Bank Research (Bnomics), Rhodium Group (How Chinese Cars Took Over Thailand).
  4. *Tài liệu thời sự & báo chí phân tích:* Financial Times (Bài điều tra gốc 28/8/2026), Người Quan Sát, VietnamBiz, Bangkok Post, The Star, Nation Thailand.

---

## 2. Danh Mục 10 Truy Vấn Nghiên Cứu Sâu & Bộ Câu Hỏi Trích Xuất (Extraction Queries)

| Mã chuyên đề | Tên tệp Vault trích xuất | Trọng tâm truy vấn trích xuất |
| :---: | :--- | :--- |
| **Q01** | `01_macro_growth_and_interest_rate_trap.md` | Tăng trưởng GDP đình trệ (1,9% - 2,3%), Lãi suất chính sách 1% của BoT, Chuỗi giảm phát kéo dài, và Bẫy thanh khoản. Đảo ngược vị thế với Nhật Bản. |
| **Q02** | `02_household_debt_and_monetary_impotence.md` | Quả bom nợ hộ gia đình 86-91% GDP, nợ mua ô tô/tiêu dùng, nợ phi chính quy (40% GDP), nợ xấu SM loans 7,0% và sự tê liệt truyền dẫn tín dụng ngân hàng. |
| **Q03** | `03_demographic_crisis_old_before_rich.md` | Khủng hoảng nhân khẩu học: TFR 1,2 con/phụ nữ, tỷ lệ người cao tuổi (>65 tuổi) tăng vọt lên 26% vào 2040, nguy cơ giảm dân số từ 67 triệu xuống 30 triệu người, bi kịch "Chưa giàu đã già" (GDP đầu người chỉ ~8.000 USD). |
| **Q04** | `04_automotive_hub_disruption_chinese_ev_shock.md` | Sự thất thủ của "Detroit Đông Nam Á": Chuỗi cung ứng ô tô đốt trong Nhật Bản bị xe điện Trung Quốc (BYD, MG, GWM) nghiền nát; làn sóng đóng cửa nhà máy và Điều 75 Luật Lao động. |
| **Q05** | `05_export_manufacturing_and_vietnam_competition.md` | Sản xuất xuất khẩu mất lợi thế trước hàng giá rẻ Trung Quốc; dòng vốn FDI chuyển dịch mạnh mẽ sang Việt Nam (điện tử, bán dẫn, AI, hạ tầng xanh). |
| **Q06** | `06_tourism_limitations_and_service_economy.md` | Giới hạn của ngành du lịch: Không thể tạo giá trị gia tăng công nghệ, sự sụt giảm chi tiêu của du khách, tính dễ bị tổn thương trước các cú sốc bên ngoài. |
| **Q07** | `07_fiscal_cliff_public_debt_and_digital_wallet.md` | Vực thẳm tài khóa: Nợ công 66,1% GDP tiến sát trần 70%; canh bạc phát tiền mặt Ví số 10.000 Baht (157 - 450 tỷ Baht) và sự kiệt quệ ngân sách. |
| **Q08** | `08_political_instability_and_institutional_deadlock.md` | Bất ổn thể chế: Chuỗi đảo chính quân sự, giải tán đảng phái, thay đổi thủ tướng liên tục làm tê liệt các chính sách phát triển dài hạn. |
| **Q09** | `09_japanification_comparison_and_systemic_mechanisms.md` | So sánh giải phẫu đa chiều: Thái Lan vs Nhật Bản — Sự giống nhau về bẫy thanh khoản/giảm phát và sự khác biệt chí tử (vị thế tiền tệ, thặng dư tài sản ròng, công nghệ lõi). |
| **Q10** | `10_strategic_lessons_and_implications_for_vietnam.md` | Bài học chiến lược sống còn cho Việt Nam: Tận dụng cửa sổ dân số vàng, cảnh giác đòn bẩy nợ tiêu dùng/bất động sản, xây dựng doanh nghiệp dẫn đầu và nâng cấp chuỗi giá trị. |

---

## 3. Bảng Kiểm Soát Dữ Liệu Bắt Buộc (Research Control Checklist)

> ⚠️ **Quy định:** Pha 2 chỉ được coi là hoàn tất khi mỗi mục dưới đây đã được ánh xạ với ít nhất 1 nguồn tài liệu kiểm chứng kèm tọa độ dòng trích dẫn trong `02_research_map.md`.

| STT | Dữ liệu / Cơ chế bắt buộc kiểm chứng | Tiêu chí số liệu tối thiểu | Nguồn đối chiếu dự kiến | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Lãi suất chính sách BoT vs BOJ | BoT 1,00% (3 kỳ liên tiếp); BOJ tăng lên 1,00% tháng 6/2026 | BoT MPC Decision 3/2026, FT, Bangkok Post | [x] Đã nạp |
| **2** | Tốc độ tăng trưởng GDP thực tế | Q2/2026 đạt 1,9%, bình quân 2022-2024 đạt 2,3%, đỉnh lịch sử 11-13% | NESDC, World Bank, IMF | [x] Đã nạp |
| **3** | Tỷ lệ nợ hộ gia đình / GDP | 86% - 91% GDP (cao nhất nhóm Upper-Middle-Income) | HSBC ASEAN Research, BoT, NESDC | [x] Đã nạp |
| **4** | Tỷ lệ nợ cần chú ý (SM loans) & Tín dụng | Nợ nhóm 2 ở mức 7,0%; tăng trưởng dư nợ toàn hệ thống chỉ 0,2% Q1/2026 | BoT Banking Sector Brief Q1/2026 | [x] Đã nạp |
| **5** | Chỉ số nhân khẩu học (TFR & Già hóa) | TFR 1,2 con/phụ nữ; người >65 tuổi tăng từ 13% lên 26% năm 2040 | World Bank, OECD, Policy Brief Thailand | [x] Đã nạp |
| **6** | Thu nhập bình quân đầu người | GDP/người Thái Lan ~8.110 USD vs Nhật Bản >33.000 USD | World Bank Data, NESDC | [x] Đã nạp |
| **7** | Tác động của xe điện Trung Quốc lên ngành ô tô | Tỷ lệ thâm nhập EV, đóng cửa nhà máy, tạm đình chỉ theo Điều 75 | Rhodium Group, Marketplace, The Star | [x] Đã nạp |
| **8** | So sánh FDI & Xuất khẩu với Việt Nam | Tỷ trọng FDI sản xuất, tăng trưởng xuất khẩu công nghệ cao | OECD FDI Review, Nation Thailand | [x] Đã nạp |
| **9** | Trần nợ công & Ngân sách Ví số | Nợ công 66,1% GDP (trần 70%); quy mô gói ví số 157 - 450 tỷ Baht | Bangkok Bank Research, Time, RSIS | [x] Đã nạp |
| **10** | Bản chất lý thuyết "Suy thoái bảng cân đối kế toán" | Richard Koo model, Liquidity Trap, Hoán đổi vị thế tài chính | Oxford Economics, SCB EIC, IMF eLibrary | [x] Đã nạp |

---

## 4. Kế Hoạch Chuyển Tiếp Pha
Sau khi rà soát và xác nhận toàn bộ 10 mục trong Bảng kiểm soát dữ liệu đều có tài liệu kiểm chứng trong `research_vault/`, Agent sẽ tiến hành tổng hợp toàn diện thành tệp **Bản Đồ Nghiên Cứu Tổng Thể (`02_research_map.md`)** làm cơ sở pháp lý và dữ liệu vững chắc cho Pha 3 (Strategy Brief) và Pha 7 (Outline).
