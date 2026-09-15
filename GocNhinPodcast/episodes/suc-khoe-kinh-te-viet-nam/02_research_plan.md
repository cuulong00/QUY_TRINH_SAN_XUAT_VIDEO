<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/suc-khoe-kinh-te-viet-nam/02_research_plan.md
- Activated Persona: 
  * The Policy Analyst (.agents/personas/the_policy_analyst.md)
  * The Industrial Economist (.agents/personas/the_industrial_economist.md)
  * The Socio-Economic Researcher (.agents/personas/the_socio_economic_researcher.md)
- Activated Skill: deep_researcher (.agents/skills/deep_researcher/SKILL.md) + notebooklm (.agents/skills/notebooklm/SKILL.md)
- Source Documents Consulted:
  * episodes/suc-khoe-kinh-te-viet-nam/01_topic_qualification.md
  * Master Notebook: 6e6f9ab0-ef1e-4429-8843-dacc4043e35f
  * Tổng cục Thống kê (GSO), Ngân hàng Nhà nước Việt Nam (SBV), Bộ Tài chính, World Bank, IMF
- Execution Timestamp: 2026-09-07 10:10
-->

# 02. Research Plan: Kế Hoạch Nghiên Cứu & Trích Xuất Dữ Liệu Sức Khỏe Kinh Tế Việt Nam

## I. Mục Tiêu Nghiên Cứu Định Lượng (Quantitative Research Objectives)
1. Xác thực độ rộng của khoảng cách **GDP vs. GNI** và dòng **Chi trả sở hữu thuần ra nước ngoài (Net Primary Income Outflows)** của Việt Nam hàng năm.
2. Đo lường tỷ lệ **Giá trị gia tăng nội địa (Domestic Value Added - DVA)** trong kim ngạch xuất khẩu hàng hóa công nghiệp chế biến chế tạo.
3. Thu thập dữ liệu thực tế về **Tỷ lệ Tín dụng / GDP (134% - 146%)**, cơ cấu nợ ngắn hạn vs trung dài hạn, và quy mô nợ xấu thực tế toàn hệ thống ngân hàng (bao gồm nợ nhóm 2 và nợ giãn hoãn theo Thông tư 02).
4. Xác minh quy mô **Dự trữ ngoại hối (FX Reserves)**, số tháng nhập khẩu tương ứng (2,4 - 2,5 tháng so với chuẩn 3 tháng của IMF) và mức độ tổn thương của tỷ giá USD/VND.
5. Đánh giá cơ cấu **Nợ công / GDP (34,7% - 36%)** và tỷ trọng nguồn thu từ đất đai (tiền sử dụng đất, thuê đất) trong ngân sách địa phương.
6. Xác nhận tỷ trọng đóng góp của **Năng suất nhân tố tổng hợp (TFP ~47%)** và mốc thời gian chính thức kết thúc thời kỳ dân số vàng (năm 2036).

---

## II. Master NotebookLM Configuration
- **Notebook Title:** Sức Khỏe Nền Kinh Tế Việt Nam: Phân Tích Thực Chứng Vĩ Mô 2024-2026
- **Notebook ID:** `6e6f9ab0-ef1e-4429-8843-dacc4043e35f`
- **Notebook URL:** `https://notebooklm.google.com/notebook/6e6f9ab0-ef1e-4429-8843-dacc4043e35f`
- **Chế độ nạp:** `--mode deep --import-all`

---

## III. Danh Sách 10 Câu Hỏi Trích Xuất Chuyên Sâu (Extraction Queries)

1. **QUERY_01 (GDP vs GNI Gap):**  
   *Câu hỏi:* Khoảng cách giữa GDP danh nghĩa và GNI của Việt Nam giai đoạn 2020–2025 là bao nhiêu tỷ USD? Dòng tiền chi trả sở hữu thuần ra nước ngoài (Net Primary Income Outflow - chủ yếu là lợi nhuận chuyển về nước của khối FDI) chiếm bao nhiêu % GDP hàng năm?

2. **QUERY_02 (Domestic Value Added - DVA):**  
   *Câu hỏi:* Theo dữ liệu của OECD TiVA, World Bank và Tổng cục Thống kê, tỷ lệ Giá trị gia tăng nội địa (DVA) trong kim ngạch xuất khẩu công nghiệp chế biến chế tạo của Việt Nam (đặc biệt là điện tử, máy tính, dệt may) là bao nhiêu %? Khối FDI chiếm bao nhiêu % tổng kim ngạch xuất khẩu?

3. **QUERY_03 (Credit to GDP & Maturity Mismatch):**  
   *Câu hỏi:* Tỷ lệ Tín dụng / GDP của Việt Nam trong các năm 2023, 2024 và 2025-2026 đạt bao nhiêu %? Cơ cấu kỳ hạn nguồn vốn (tỷ lệ vốn huy động ngắn hạn cho vay trung và dài hạn) và cảnh báo của Ngân hàng Nhà nước/World Bank về rủi ro thanh khoản?

4. **QUERY_04 (Real Non-Performing Loans):**  
   *Câu hỏi:* Tỷ lệ nợ xấu nội bảng của hệ thống ngân hàng Việt Nam là bao nhiêu? Nếu cộng gộp cả nợ nhóm 2 (nợ cần chú ý), nợ tái cơ cấu theo Thông tư 02/2023/TT-NHNN và nợ tiềm ẩn liên quan đến trái phiếu doanh nghiệp, tổng tỷ lệ nợ xấu ước tính là bao nhiêu %?

5. **QUERY_05 (FX Reserves & Import Cover):**  
   *Câu hỏi:* Quy mô dự trữ ngoại hối của Việt Nam biến động ra sao từ đỉnh hơn 111,8 tỷ USD (tháng 1/2022) đến giai đoạn 2024–2026? Số tháng nhập khẩu tương ứng hiện tại là bao nhiêu tháng (so với ngưỡng khuyến nghị tối thiểu 3 tháng của IMF)?

6. **QUERY_06 (Impossible Trinity & Exchange Rate):**  
   *Câu hỏi:* Ngân hàng Nhà nước Việt Nam đã điều hành chính sách tiền tệ như thế nào trước "Bộ ba bất khả thi" khi chênh lệch lãi suất VND-USD nới rộng do Fed neo lãi suất cao? Tỷ giá USD/VND đã mất giá bao nhiêu % trong các đợt biến động 2024–2025?

7. **QUERY_07 (Public Debt & Fiscal Space):**  
   *Câu hỏi:* Tỷ lệ Nợ công / GDP của Việt Nam các năm 2024, 2025 và 2026 là bao nhiêu % so với trần 60% của Quốc hội? Nghĩa vụ trả nợ trực tiếp của Chính phủ so với tổng thu ngân sách nhà nước là bao nhiêu?

8. **QUERY_08 (Land Revenue Dependency):**  
   *Câu hỏi:* Trong cơ cấu thu ngân sách địa phương, nguồn thu từ tiền sử dụng đất, thuê đất và đấu giá quyền sử dụng đất chiếm tỷ trọng bao nhiêu % (ví dụ tại một số tỉnh thành như Nghệ An, Đà Nẵng, TP.HCM)? Khi thị trường bất động sản đóng băng, nguồn chi đầu tư phát triển của các địa phương bị ảnh hưởng ra sao?

9. **QUERY_09 (TFP & Labor Productivity):**  
   *Câu hỏi:* Đóng góp của Năng suất nhân tố tổng hợp (TFP) vào tăng trưởng GDP của Việt Nam giai đoạn 2021–2025 đạt bao nhiêu % (so với mục tiêu 50-55%)? Tốc độ tăng năng suất lao động của Việt Nam so với các nước ASEAN-4 (Thái Lan, Malaysia, Indonesia, Philippines) thế nào?

10. **QUERY_10 (Demographic Golden Window Ending):**  
    *Câu hỏi:* Thời kỳ "cơ cấu dân số vàng" của Việt Nam được dự báo chính thức kết thúc vào năm nào (năm 2036 hay 2039)? Tốc độ già hóa dân số của Việt Nam nhanh như thế nào so với thế giới và áp lực lên quỹ bảo hiểm xã hội, chi phí y tế trong thập kỷ tới?
