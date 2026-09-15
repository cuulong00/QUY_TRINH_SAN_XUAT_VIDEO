# Kế Hoạch Deep Research Chuyên Sâu: Sự Lụi Tàn Của Tiki (2010 – 2025)

episode_slug: su-lui-tan-cua-tiki
phase: 2 — Data Mining & Verification
status: active_deep_research

---

## 1. Nhật Ký Khởi Chạy & Mục Tiêu Nghiên Cứu
- **Thời gian lập kế hoạch:** 2026-08-28T23:00:00+07:00
- **Mục tiêu tối thượng:** Thu thập, kiểm chứng chéo và chuẩn hóa 100% số liệu thực chứng mới nhất (cập nhật đến 2024 – 2026) về hành trình tài chính, cấu trúc vận hành, cuộc chiến đốt tiền và sự sa sút thị phần của Tiki tại Việt Nam.
- **Tiêu chuẩn dữ liệu:** Tuyệt đối không sử dụng số liệu phỏng đoán, tin đồn mạng xã hội, hoặc số liệu chưa qua kiểm chứng chéo từ các báo cáo kiểm toán độc lập, cơ quan thống kê thị trường uy tín (YouNet ECI, Metric, Tech in Asia, DealStreetAsia, BCTC VNG).

---

## 2. Hệ Thống 4 Trục Prompt Nạp Nguồn Cấu Trúc (Master Ingestion Prompts)

### Trục 1: Báo Cáo Tài Chính, Lỗ Lũy Kế & Cơ Cấu Gọi Vốn (Financial Forensics & Capital Structure)
```text
Thực hiện Deep Research toàn diện về lịch sử tài chính của Tiki (Công ty Cổ phần Ti Ki / Tiki Global Pte. Ltd.) từ năm 2010 đến 2025:
1. Thống kê chi tiết toàn bộ các vòng gọi vốn từ Seed (2010), Series A (CyberAgent 2012), Series B (Sumitomo 2013), Series C (VNG 2016 rót 384 tỷ đồng, JD.com 2017-2018), Series D (Northstar Group 2020), Series E (258 triệu USD năm 2021 do AIA dẫn đầu), đến Shinhan Financial Group (2022). Xác định chính xác số tiền huy động, tỷ lệ cổ phần và định giá công ty qua từng vòng.
2. Trích xuất số liệu doanh thu thuần, lợi nhuận/lỗ ròng sau thuế hàng năm từ 2016 đến 2023 qua các BCTC kiểm toán (công bố bởi VNG, Tech in Asia, DealStreetAsia, Vietdata). Xác minh con số lỗ lũy kế chính thức tính đến hết năm tài chính 2023 (vượt 10.000 tỷ VNĐ).
3. Diễn biến đầu tư của VNG: Bóc tách khoản đầu tư 510,1 tỷ đồng của VNG, thời điểm VNG trích lập dự phòng 100% (Q1/2019) và trích dẫn văn bản BCTC Hợp nhất Quý 4/2024 của VNG về việc chính thức miễn nhiệm đại diện trong Ban Giám đốc Tiki Global vào ngày 28/10/2024.
```

### Trục 2: Giải Phẫu Mô Hình Vận Hành & Logistics (Operational Anatomy: 1P vs 3P & TikiNOW)
```text
Nghiên cứu sâu sắc về kinh tế học đơn vị (Unit Economics) và chi phí vận hành kho vận của Tiki:
1. Mô hình 1P (Tiki Trading) vs 3P Marketplace: Bóc tách cơ cấu chi phí cố định (CAPEX kho bãi, nhân sự kho, quản lý SKU, rủi ro đọng vốn tồn kho) của Tiki so với mô hình sàn tài sản nhẹ (Asset-light) của Shopee.
2. Dịch vụ giao hàng 2 giờ TikiNOW: Cơ chế vận hành hệ thống kho vệ tinh nội thành (Micro-fulfillment centers) tại Hà Nội, TP.HCM, Đà Nẵng; lý do TikiNOW không thể tối ưu hóa gom đơn (Batching) dẫn đến chi phí giao hàng chặng cuối (Last-mile delivery cost) bị âm nặng trên từng đơn hàng.
3. Chi phí tiếp thị & Xây dựng thương hiệu: Báo cáo hiệu quả chiến dịch "Tiki Đi Cùng Sao Việt" (tài trợ 100 MV ca nhạc năm 2019-2020) so sánh với hiệu quả trợ giá vận chuyển trực tiếp (FreeShip Xtra) và Game hóa (Gamification) của Shopee.
```

### Trục 3: Cú Sốc Vĩ Mô Toàn Cầu & Sự Đứt Gãy Dòng Vốn Mạo Hiểm (Macro VC Shock & Capital Asymmetry)
```text
Phân tích sự khác biệt về cấu trúc tài chính và tác động của chu kỳ kinh tế vĩ mô năm 2022:
1. So sánh nguồn vốn: Cơ chế trợ cấp dòng tiền chéo từ mảng Game (Garena Free Fire của Sea Group) cho Shopee và hơn 7 tỷ USD Alibaba rót cho Lazada vs. Sự phụ thuộc 100% vào vốn mạo hiểm (VC) của Tiki.
2. Cú sốc Fed tăng lãi suất từ tháng 3/2022: Kỷ nguyên tiền rẻ (ZIRP) chấm dứt, các quỹ đầu tư mạo hiểm chuyển từ "tăng trưởng bằng mọi giá" sang "thắt lưng buộc bụng", làm sụp đổ kế hoạch IPO tại Mỹ qua hình thức SPAC của Tiki Global.
3. Hệ quả của việc phanh gấp: Cắt giảm ngân sách trợ giá, tăng phí sàn 3P, đóng cửa kho vệ tinh dẫn đến sự suy giảm đột ngột lưu lượng truy cập (Traffic) và giá trị giao dịch (GMV).
```

### Trục 4: Đòn Giáng Shoppertainment & Bản Đồ Thị Phần 2020 – 2025 (TikTok Shop & Market Share Collapse)
```text
Nghiên cứu về cuộc cách mạng thương mại giải trí và sự dịch chuyển thị phần TMĐT tại Việt Nam:
1. Sự chuyển dịch hành vi người dùng: Từ "E-commerce tìm kiếm chủ động" (Search-based) sang "E-commerce khám phá qua video ngắn và livestream" (Discovery-based / Shoppertainment) do TikTok Shop dẫn dắt từ tháng 4/2022.
2. Bản đồ thị phần GMV TMĐT Việt Nam (2020 - 2025): Thống kê số liệu thị phần chính xác của Shopee, TikTok Shop, Lazada, Tiki qua các báo cáo thường niên của YouNet ECI và Metric.vn. Xác minh con số thị phần Tiki rơi từ đỉnh cao 15% xuống 2,2% (đầu 2023) và 0,8% (cuối 2024).
3. Diễn biến nhân sự và tái cấu trúc: Mốc thời gian ông Trần Ngọc Thái Sơn từ chức CEO (tháng 7/2023), bổ nhiệm Richard Triều Phạm, sa thải nhân sự 30-50%, sự thất bại của các dự án xoay trục như Token Astra (Web3) và bán bảo hiểm AIA.
```

---

## 3. Danh Sách 12 Câu Hỏi Trích Xuất Tối Ưu (Extraction Queries Q01 – Q12)

| Mã Query | Target Chapter | Trọng Tâm Trích Xuất Dữ Liệu | Tiêu Chuẩn Nguồn Bắt Buộc | Vault Target File |
| :--- | :--- | :--- | :--- | :--- |
| **Q01** | Chương 1 | **Thị phần GMV 2021 – 2025:** Tỷ lệ thị phần của Tiki, Shopee, TikTok Shop, Lazada qua các năm 2021, 2022, 2023, 2024. | Báo cáo YouNet ECI, Metric.vn, iPrice | `tiktok_shop_shoppertainment.md` |
| **Q02** | Chương 1 & 6 | **Báo cáo Lỗ lũy kế & Thoái vốn VNG:** Lỗ ròng theo năm (2016-2023), tổng lỗ lũy kế vượt 10.000 tỷ VNĐ, BCTC VNG Q4/2024 (ngày 28/10/2024). | BCTC kiểm toán VNG (VNZ), Tech in Asia | `tiki_financials_losses.md` |
| **Q03** | Chương 2 | **Khởi nghiệp & Triết lý ban đầu (2010-2015):** 5.000 USD vốn từ garage, bán sách, quy trình bọc sách Bookcare, dịch vụ TikiCare, vòng CyberAgent (500k$) & Sumitomo (1M$). | Phỏng vấn ông Trần Ngọc Thái Sơn, Crunchbase | `tiki_history_founding.md` |
| **Q04** | Chương 2 | **Lịch sử các vòng gọi vốn lớn (2016-2022):** VNG rót 384 tỷ (2016), JD.com rót vốn, Northstar (130M$ 2020), Series E (258M$ 2021 dẫn đầu bởi AIA), Shinhan (2022). | DealStreetAsia, Tech in Asia, Báo ĐT Chứng Khoán | `tiki_funding_rounds.md` |
| **Q05** | Chương 2 | **Giải phẫu Bẫy Chi phí Cố định 1P:** Cấu trúc chi phí thuê kho bãi, nhân sự, dòng vốn lưu động bị chôn vào hàng tồn kho của Tiki Trading so với mô hình 3P Shopee. | Phân tích chuyên gia tài chính, Vietdata | `tiki_1p_vs_3p_logistics.md` |
| **Q06** | Chương 2 & 3 | **Thế tiến thoái lưỡng nan của 3P Marketplace:** Rào cản kiểm duyệt giấy tờ/phí sàn khiến người bán bỏ sang Shopee; nới lỏng thì hàng giả lọt vào làm loãng thương hiệu. | Báo cáo thị trường TMĐT VECOM, Vietnambiz | `tiki_1p_vs_3p_logistics.md` |
| **Q07** | Chương 3 | **Kinh tế học đơn hàng TikiNOW 2 Giờ:** Chi phí kho vệ tinh nội thành, vận chuyển chặng cuối đơn lẻ (không thể Batching), Unit Economics âm trên từng đơn giao 2h. | Tài liệu Logistics TMĐT, VnExpress Kinh Doanh | `tiki_1p_vs_3p_logistics.md` |
| **Q08** | Chương 3 | **Chiến dịch "Tiki Đi Cùng Sao Việt":** Số lượng 100 MV tài trợ, 1,6 tỷ view, 13 Top 1 Trending, tại sao Branding không tạo ra Switching Costs trước mã FreeShip Shopee. | Tiki Brand Communications Report, Advertising Vietnam | `tiki_marketing_burn_rate.md` |
| **Q09** | Chương 4 | **Bất đối xứng nguồn vốn (Sea Group/Alibaba vs VC):** Dòng tiền mặt game Garena Free Fire nuôi Shopee, Alibaba rót >7 tỷ$ cho Lazada vs. Sự phụ thuộc vốn VC của Tiki. | SEC Form 20-F Sea Ltd, Báo cáo thường niên Alibaba | `macro_vc_shock_2022.md` |
| **Q10** | Chương 4 | **Cú sốc Fed tăng lãi suất 2022 & Đổ vỡ IPO Mỹ:** Fed tăng lãi suất >5%, mùa đông gọi vốn VC, việc hủy bỏ kế hoạch SPAC niêm yết tại Mỹ và cú phanh gấp cắt trợ giá. | Bloomberg, Financial Times, DealStreetAsia | `macro_vc_shock_2022.md` |
| **Q11** | Chương 5 | **Đòn giáng Shoppertainment từ TikTok Shop:** Mô hình M2C xưởng Trung Quốc, livestream KOC, thuật toán video ngắn chuyển dịch từ Search sang Discovery, chiếm 25% thị phần. | Báo cáo YouNet ECI, Tech in Asia, CafeF | `tiktok_shop_shoppertainment.md` |
| **Q12** | Chương 6 & 7 | **Timeline Lãnh đạo, Thử nghiệm Web3 & Bài học vĩ mô:** Ông Sơn từ chức (7/2023), Richard Triều Phạm, token Astra, bảo hiểm AIA, sa thải nhân sự, 3 bài học kinh tế nền tảng. | DealStreetAsia, CafeF, VietnamNet, HBR | `tiki_leadership_vng_exit.md` & `business_lessons.md` |

---

## 4. Giao Thức Kiểm Toán Dữ Liệu Chống Ảo Giác (Anti-Hallucination & Verification Protocol)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     QUY TRÌNH KIỂM CHỨNG DỮ LIỆU ĐỘC LẬP 3 BƯỚC                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 1: XÁC LẬP NGUỒN CẤP 1 (TIER-1 PRIMARY SOURCES)                                  │
│ • Báo cáo tài chính kiểm toán hợp nhất đã công bố (BCTC VNG kiểm toán bởi PwC/EY).     │
│ • Hồ sơ pháp lý chứng khoán (SEC Form 20-F của Sea Group).                             │
│ • Báo cáo đo lường thị trường độc lập định lượng (YouNet ECI, Metric.vn).              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 2: ĐỐI CHIẾU CHÉO TĂNG CƯỜNG (CROSS-VERIFICATION TRIANGULATION)                  │
│ • Mọi con số tài chính (như lỗ lũy kế 10.000 tỷ, vốn 258M$) bắt buộc phải xuất hiện   │
│   đồng thời trên tối thiểu 2 nguồn báo chí tài chính quốc tế uy tín (Tech in Asia,     │
│   DealStreetAsia, Bloomberg) hoặc khớp 1-1 với BCTC doanh nghiệp.                      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 3: RÀNG BUỘC KHÓA CỨNG HẰNG SỐ (IMMUTABLE DATA LOCK)                             │
│ • Khi một số liệu đã được xác minh (DATA-01 đến DATA-20), nó được khóa cứng vào       │
│   `00_Global_Vision_Synthesis.md` và `02_research_map.md`.                             │
│ • Nghiêm cấm mọi hành vi tự ý sửa đổi số liệu trong các khâu viết kịch bản tiếp theo. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Danh Mục Cảnh Báo "Vùng Cấm Dữ Liệu" (Red-Flag Data Policy)

1. **Tuyệt đối cấm dùng từ "Tiki phá sản" hay "Tiki đóng cửa":** Tiki vẫn đang duy trì hoạt động với tư cách một sàn TMĐT thu hẹp, tái cấu trúc tập trung vào các danh mục thế mạnh (sách, hàng chính hãng). Phải dùng chính xác: *"suy thoái thị phần nghiêm trọng"*, *"co cụm quy mô"*, *"ngạt thở tài chính"*.
2. **Tuyệt đối cấm quy kết sai lệch nguyên nhân thất bại:** Không đổ lỗi một chiều cho tâm lý người tiêu dùng Việt Nam ("ham rẻ"), mà phải phân tích bằng **bản chất cấu trúc chi phí (Fixed Cost Trap)**, **hiệu ứng mạng lưới hai chiều (Two-Sided Network Effects)** và **sự dịch chuyển hạ tầng công nghệ (Shoppertainment)**.
3. **Tuyệt đối cấm trích dẫn số liệu ước đoán không có đơn vị đo lường:** Mọi số liệu về thị phần phải ghi rõ là **Thị phần theo Tổng giá trị giao dịch hàng hóa (GMV)** dựa trên báo cáo của đơn vị nào (YouNet ECI hay Metric) tại mốc thời gian cụ thể (quý nào, năm nào).
