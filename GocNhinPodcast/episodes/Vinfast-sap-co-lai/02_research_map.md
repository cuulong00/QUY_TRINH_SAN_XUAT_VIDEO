# Research Map — VinFast Asset-Light Restructuring & Component Architecture

> **Mã thư mục:** `episodes/Vinfast-sap-co-lai`  
> **Kênh:** GocNhinPodcast  
> **Chuyên gia:** The Socio-Economic Researcher (GocNhinPodcast)  
> **Trạng thái:** Đã nạp 58 Nguồn dữ liệu vào Master Notebook & Trích xuất 100% (15/15 Tệp Vault Thực chứng)

---

## 1. Thesis Data (Dữ liệu hỗ trợ luận đề chính)

| # | Data Point | Con số định lượng | Nguồn chính thức | Năm/Kỳ | Vault Ref (Tệp & Dòng) | Cross-verified |
|---|-----------|-------------------|------------------|--------|-----------------------|----------------|
| 1 | **Doanh thu hợp nhất 2025** | **90.427,6 tỷ VNĐ** (~3,6 tỷ USD) | BCTC VinFast Auto / SEC | 2025 | `002-tom-tat-du-lieu-tai-chinh...md` L10-L45 | ✅ |
| 2 | **Lỗ ròng hợp nhất 2025** | **97.245,7 tỷ VNĐ** (~3,9 tỷ USD) | BCTC VinFast Auto / SEC | 2025 | `002-tom-tat-du-lieu-tai-chinh...md` L50-L80 | ✅ |
| 3 | **Lỗ ròng hợp nhất 2024** | **77.354,9 tỷ VNĐ** (~3,18 tỷ USD) | BCTC VinFast Auto / SEC | 2024 | `002-tom-tat-du-lieu-tai-chinh...md` L85-L110 | ✅ |
| 4 | **Sản lượng giao ô tô điện 2025** | **196.919 xe** (tăng 102% YoY) | Báo cáo Vận hành VinFast | 2025 | `002-tom-tat-du-lieu-tai-chinh...md` L120-L150 | ✅ |
| 5 | **Sản lượng giao H1/2026** | **115.916 ô tô điện** | Báo cáo Vận hành H1/2026 | H1/2026 | `002-tom-tat-du-lieu-tai-chinh...md` L155-L180 | ✅ |
| 6 | **Biên lợi nhuận gộp (Gross Margin)** | **-57,4% (2024) ➔ -42,5% (2025) ➔ -39,9% (Q4/2025)** | BCTC niêm yết NASDAQ | 2024-2025 | `007-tac-ong-chi-tiet-en-bao-cao...md` L20-L60 | ✅ |
| 7 | **Giá nhượng cổ phần VFTP** | **13.309,6 tỷ VNĐ** (~530 triệu USD) | Hồ sơ SEC Form 6-K Ex-99.1 | 05/2026 | `003-chi-tiet-ho-so-nop-sec...md` L15-L40 | ✅ |
| 8 | **Giá trị nợ chuyển giao** | **~182.000 tỷ VNĐ** (~7,2 tỷ USD) | Hồ sơ SEC Form 6-K | 05/2026 | `004-phan-inh-ranh-gioi-tai-san...md` L10-L100 | ✅ |
| 9 | **Mục tiêu sản lượng 2026** | **~300.000 xe toàn cầu** | Kế hoạch Kinh doanh | 2026 | `001-buc-tranh-tuong-lai-2026-2030...md` L10-L50 | ✅ |
| 10 | **Mốc điểm hòa vốn** | **Năm 2027 (Việt Nam), có lãi toàn cầu** | Tuyên bố Chủ tịch Vingroup | 2027 | `006-giai-thich-co-che-trich-khau-hao...md` L50-L120 | ✅ |

---

## 2. Research Vault Index (Bản đồ Tọa độ 15 Tệp Vault Thực chứng)

| Tên tệp Vault | Tóm tắt Nội dung Cốt lõi | Nguồn Kiểm chứng |
|---------------|--------------------------|-------------------|
| `001-boc-tach-chi-tiet-cau-phan-chiec-xe-o-to-vinfast...md` | Bóc tách BOM xe VinFast trước vs sau tách: Pin 30-40%, Chip/ADAS 18-22%, IP 10-15%, Khung vỏ 25-30%. | BCTC & Báo cáo Kỹ thuật NotebookLM |
| `002-tom-tat-du-lieu-tai-chinh-doanh-so-moi-nhat...md` | Số liệu kiểm toán 2024-2026: Doanh thu 90.4k tỷ, Lỗ ròng 97.2k tỷ, sản lượng 196.9k xe 2025. | BCTC SEC Filing Ex-99.1 |
| `003-chi-tiet-ho-so-nop-sec-form-6-k...md` | Chi tiết hồ sơ SEC 05/2026: thoái vốn VFTP 530M USD, chuyển nợ 182k tỷ cho Công ty Tương Lai. | SEC Form 6-K Ex-99.1 |
| `004-phan-inh-ranh-gioi-tai-san-sec...md` | Phân định ranh giới SEC: VFVN giữ 100% IP/phần mềm/brand; VFTP giữ hạ tầng dập/sơn/hàn & nợ. | Hồ sơ SEC Tái cấu trúc |
| `005-co-che-hop-ong-gia-cong-tolling-agreement...md` | Cơ chế hợp đồng Tolling Fee: Phí gia công biến đổi tính theo xe xuất xưởng. | Hồ sơ Hợp đồng Tái cấu trúc |
| `006-giai-thich-co-che-trich-khau-hao-nha-may...md` | Giải mã bẫy khấu hao cố định khi nhà máy chạy <40% công suất; giải phóng capex dồn vào R&D/Pin. | Báo cáo Phân tích Kế toán |
| `007-tac-ong-chi-tiet-en-bao-cao-ket-qua-kinh-doanh...md` | Tác động COGS & P&L: Biên lợi nhuận gộp cải thiện từ -57,4% (2024) lên -42,5% (2025) và -39,9% (Q4/2025). | BCTC VinFast Auto Ltd |
| `001-mang-luoi-nha-cung-cap-tier-1-chuoi-cung-ung-toan-cau...md` | Mạng lưới Tier-1: NVIDIA, Qualcomm, VinAI, Bosch, ZF, CATL, Gotion, StoreDot, ProLogium. | Thông tin Đối tác Chính thức |
| `009-giai-ma-ban-chat-tai-cau-truc-noi-bo...md` | Bản chất giao dịch nội bộ: Đưa VinFast Auto về mô hình Asset-Light chuẩn công nghệ trên NASDAQ. | SEC Audit Protocol |
| `010-ai-thuc-su-ganh-khoan-no-182000-ty...md` | Ai gánh nợ 182k tỷ? Dòng tiền từ Tolling Fee, vốn Công ty Tương Lai (122k tỷ) & tài sản bảo lãnh Vingroup. | BCTC Hợp nhất Vingroup |
| `002-phan-tich-rui-ro-gia-giao-dich-lien-ket...md` | Rủi ro chuyển giá (Transfer Pricing) theo nguyên tắc Arm's Length của SEC & Cơ quan Thuế. | Quy định Kiểm toán SEC |
| `003-ty-le-phu-thuoc-doanh-so-vao-gsm...md` | Độ phụ thuộc taxi GSM (2024-2025) và bài toán chuyển dịch B2C cá nhân (VF 3, VF 5) năm 2026. | SSI Research / Vietcap |
| `002-chi-tiet-ban-o-rd-cong-nghe-hop-tac-phan-mem...md` | Bản đồ R&D: Thuật toán BMS độc quyền, AI VinAI (DOMS, ASVM, MirrorSense), tự lái L4 Robotaxi. | VinFast R&D Disclosure |
| `005-phan-tich-ban-chat-nen-mong-inh-iem-rui-ro...md` | Lý do tách mảng sản xuất giữa năm 2026: Đã xong móng Hải Phòng, sản lượng tiệm cận 200k xe. | Báo cáo Phân tích Ngành |
| `001-buc-tranh-tuong-lai-2026-2030-4-tru-cot-chien-luoc...md` | Bức tranh 2026-2030: 4 Trụ cột chiến lược & 2 Kịch bản tài chính sinh tử (Win-Win vs Stress Scenario). | VinFast Strategy 2030 |
