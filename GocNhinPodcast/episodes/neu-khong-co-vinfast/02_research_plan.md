# 02 — Research Plan: "Nếu Không Có VinFast"

> **Phương pháp:** Web Search có mục tiêu (Targeted Web Search)
> **Lý do:** Tài liệu gốc đã rất giàu (5 tệp, 54 nguồn). Không cần NotebookLM Deep Research. Cần xác minh số liệu + lấp lỗ hổng dữ liệu cụ thể.
> **Ngày:** 2026-07-10

---

## Chiến lược Web Search

### Nguyên tắc
1. **Verify-first:** Xác minh các con số cốt lõi trong tài liệu gốc trước khi tin dùng.
2. **Gap-fill:** Bổ sung dữ liệu mà tài liệu gốc nhắc đến nhưng chưa có số cứng.
3. **Freshness:** Ưu tiên 2025–Q2/2026. Không dùng số trước 2024 trừ so sánh lịch sử.
4. **1 query = 1 target:** Mỗi truy vấn nhắm 1 con số hoặc 1 sự kiện cụ thể.

---

## Cụm 1: XÁC MINH SỐ LIỆU CỐT LÕI (Verify)

> Mục tiêu: Confirm các con số quan trọng nhất mà toàn bộ kịch bản dựa vào.

| # | Số liệu cần verify | Nguồn gốc (tài liệu) | Query Web Search | Chương |
|---|---|---|---|---|
| V1 | VinFast bán 175.099 ô tô năm 2025 | Tài liệu chính, cite 1,7 | `VinFast doanh số ô tô 2025 tổng năm` | Ch.1, Ch.2 |
| V2 | VinFast 406.453 xe máy điện 2025, 56% thị phần xe điện 2 bánh | Tài liệu chính, cite 38 | `VinFast xe máy điện doanh số 2025 thị phần` | Ch.1, Ch.3 |
| V3 | Tổng thị trường ô tô 2025 >600.000 xe | Tài liệu chính, cite 2,23 | `tổng doanh số ô tô Việt Nam 2025 VAMA` | Ch.2 |
| V4 | Q1/2026: VinFast 53.684 xe, 33,13% thị phần | Tài liệu chính, cite 11 | `VinFast doanh số quý 1 2026 thị phần` | Ch.2 |
| V5 | 150.000+ cổng sạc V-Green, chiếm 98% | Tài liệu chính, cite 9,13 | `V-Green số cổng sạc 2025 2026 tỷ lệ thị phần` | Ch.3 |
| V6 | Xanh SM thị phần >50% Q4/2025 (Mordor Intelligence) | Bổ sung mảng 1 | `Xanh SM thị phần gọi xe 2025 Mordor Intelligence` | Ch.4 |
| V7 | Chi phí logistics 16,8% GDP Việt Nam | Bổ sung mảng 2 | `chi phí logistics Việt Nam tỷ lệ GDP 2024 2025` | Ch.4 |
| V8 | VinFast 700+ nhà cung ứng nội địa vs Toyota 13 | Tài liệu chính, cite 17 | `VinFast nhà cung ứng nội địa 700 Toyota 13 so sánh` | Ch.5 |
| V9 | Nội địa hóa VinFast 60%, mục tiêu 84% năm 2026 | Tài liệu chính, cite 4,44 | `VinFast tỷ lệ nội địa hóa 2025 2026 mục tiêu` | Ch.5 |
| V10 | QĐ 876/QĐ-TTg lộ trình xanh hóa giao thông | net-zero1.md | `Quyết định 876 QĐ-TTg lộ trình giao thông xanh xe điện 2030 2050` | Ch.6 |

---

## Cụm 2: LẤP LỖ HỔNG DỮ LIỆU (Gap-fill)

> Mục tiêu: Bổ sung dữ liệu mà tài liệu gốc nhắc đến nhưng chưa có số cứng hoặc cần chi tiết hơn.

| # | Lỗ hổng dữ liệu | Tại sao cần | Query Web Search | Chương |
|---|---|---|---|---|
| G1 | Giá lăn bánh thực tế VF3, VF5 vs Grand i10, Morning (2026) | So sánh chi phí sở hữu nếu không có VinFast | `giá lăn bánh VinFast VF3 VF5 2026` + `giá lăn bánh Hyundai Grand i10 Kia Morning 2026` | Ch.2 |
| G2 | Doanh số từng hãng ô tô 2025: Toyota, Hyundai, Ford, Mitsubishi | Verify bảng thị phần giả định | `doanh số ô tô Toyota Hyundai Ford Mitsubishi Việt Nam 2025` | Ch.2 |
| G3 | Honda ICON e: và Yamaha NEO's — thông số, giá, ngày ra mắt VN | Chi tiết xe máy điện đối thủ | `Honda ICON e: Việt Nam 2025 2026 giá thông số` + `Yamaha NEO's Việt Nam` | Ch.3 |
| G4 | Số tủ đổi pin VinFast-Vietnam Post (cập nhật 2026) | Verify con số 16.000 tủ | `VinFast đổi pin Vietnam Post số tủ 2026` | Ch.3 |
| G5 | Green SM Van — số xe EC Van đang hoạt động, tuyến phủ | Tài liệu chỉ nêu specs, chưa có quy mô | `Green SM Van EC Van số lượng xe thành phố 2026` | Ch.4 |
| G6 | VinBus — số tuyến, lượt khách, Door-to-Door rollout | Tài liệu nêu tính năng nhưng thiếu quy mô | `VinBus số tuyến lượt khách 2025 2026 Door to Door` | Ch.4 |
| G7 | Tỷ lệ xe VinFast bán cho GSM (Xanh SM) vs cá nhân | Phản biện "tay trái bán tay phải" | `VinFast bán cho GSM Xanh SM tỷ lệ cá nhân doanh nghiệp 2025` | Ch.2, Ch.7 |
| G8 | ESG Scope 3 và yêu cầu kiểm toán chuỗi cung ứng xanh cho FDI | Chi tiết cơ chế mất FDI | `ESG Scope 3 supply chain audit FDI Vietnam manufacturing` | Ch.6 |
| G9 | Cơ cấu nguồn điện Việt Nam 2025 — tỷ lệ nhiệt điện than vs tái tạo | Phản biện "xanh hóa hình thức" | `cơ cấu nguồn điện Việt Nam 2025 nhiệt điện than năng lượng tái tạo` | Ch.6 |
| G10 | Mô hình Thái Lan: BYD/Great Wall — doanh số, nhà máy, Net Zero | So sánh quốc tế | `BYD Great Wall Motor Thailand sales factory 2024 2025 EV policy` | Ch.6 |

---

## Cụm 3: BỔ SUNG GÓC PHẢN BIỆN (Counter-thesis)

> Mục tiêu: Tăng tính phản biện — tìm dữ liệu cho chiều "Không VinFast cũng tốt".

| # | Góc phản biện cần data | Query Web Search | Chương |
|---|---|---|---|
| C1 | Toyota Hybrid (Yaris Cross, Corolla Cross HEV) doanh số + mức giảm phát thải vs thuần điện | `Toyota Hybrid Yaris Cross Corolla Cross Việt Nam doanh số 2025` + `hybrid vs electric emission reduction comparison` | Ch.6, Ch.7 |
| C2 | Wuling kế hoạch 30.000 trạm sạc — tiến độ thực tế? | `Wuling trạm sạc Việt Nam 2025 2026 kế hoạch tiến độ` | Ch.3, Ch.6 |
| C3 | BYD doanh số Việt Nam 2025 — có bán chạy dù thiếu sạc? | `BYD doanh số Việt Nam 2025 mẫu xe bán chạy` | Ch.3, Ch.6 |
| C4 | Ô nhiễm không khí Hà Nội TP.HCM — AQI + tỷ lệ từ giao thông | `AQI Hà Nội TP HCM 2025 ô nhiễm không khí giao thông tỷ lệ` | Ch.3, Ch.4 |
| C5 | Ngân sách thất thu từ miễn trước bạ xe điện — con số thực | `ngân sách thất thu lệ phí trước bạ xe điện 0% ước tính` | Ch.7 |

---

## Trình tự thực hiện

```
Bước 1: Chạy Cụm 1 (Verify) — 10 queries
  → Ghi kết quả vào research_vault/verify_results.md
  → Đánh dấu ✅/❌ từng con số

Bước 2: Chạy Cụm 2 (Gap-fill) — 10 queries  
  → Ghi kết quả vào research_vault/gap_fill_results.md
  → Bổ sung data mới vào outline nếu cần

Bước 3: Chạy Cụm 3 (Counter-thesis) — 5 queries
  → Ghi kết quả vào research_vault/counter_thesis_results.md
  → Đảm bảo ≥3 data points phản biện cứng

Bước 4: Tổng hợp
  → Tạo 02_research_map.md (bảng tọa độ data)
  → Tạo 02_research_synthesis.md (tóm tắt cơ chế vĩ mô)
  → Cập nhật outline nếu phát hiện lệch thực tế
```

---

## Tiêu chí đạt

- [ ] 100% số liệu cốt lõi (Cụm 1) được verify hoặc gắn cờ cần điều chỉnh
- [ ] ≥80% lỗ hổng (Cụm 2) được lấp bằng data mới
- [ ] ≥3 data points phản biện cứng (Cụm 3) cho Ch.6–Ch.7
- [ ] Mọi con số ghi rõ năm/quý + URL nguồn
- [ ] Không data point nào >2 năm tuổi (trừ so sánh lịch sử)
