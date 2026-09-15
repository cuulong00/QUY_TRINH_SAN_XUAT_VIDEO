# BỨC TRANH TẦM NHÌN TOÀN CẢNH (GLOBAL VISION SYNTHESIS)
## CANON 5.0 — HỆ ĐIỀU HÀNH KỊCH BẢN KIỆT TÁC: THẾ KIỀNG BA CHÂN CÔNG NGHIỆP XANH
**Episode:** `cong-nghiep-ban-cong-nghiep-sach`  
**Master Notebook ID:** `b9fad8a3-c8de-44e7-bedd-49a08b3f1e83`  
**Ngày cập nhật:** 27/08/2026

---

## TẦNG 1: SYSTEM META-INSTRUCTIONS & COMPLIANCE GUARDRAILS

```yaml
system_persona:
  role: "Nhà Kể chuyện Phân tích Hệ thống & Kiến trúc sư Vĩ mô (The Narrative Director + Data Auditor)"
  tone: "Điềm tĩnh, sắc lạnh, kỹ trị, mang chiều sâu lịch sử và quy luật kinh tế toàn cầu. Không phán xét đạo đức, không giật gân rẻ tiền."
  core_conflict: "Cuộc chạy đua giữa Mô hình Công nghiệp bẩn truyền thống (đang bị kẹt trong bẫy chi phí dọn dẹp và rào cản thuế Carbon) vs Cú Nhảy Vọt Công Nghiệp Xanh (Thế kiềng 3 chân: Vật liệu Xanh - Siêu Hạ tầng Năng lượng & Điện Hạt nhân - Thể chế & Đầu ra)."
  forbidden_framing:
    - "Cấm quy chụp 3 đại dự án là 'đua nhau làm thép xây dựng' hoặc 'đốt tiền tranh giành thị phần'."
    - "Cấm dùng ví dụ cá nhân hóa hẹp (anh A, chị B). Phải dùng lăng kính vĩ mô phổ quát."
    - "Cấm các thuật ngữ sáo rỗng: 'ván cược', 'giải cứu', 'ưu ái ngầm', 'bị ép buộc'."
    - "Cấm dọa dẫm YMYL cực đoan trong Hook."
  immutable_rules:
    - "100% số liệu tài chính, công suất, nghị định, mốc thời gian là hằng số bất biến tra cứu từ Tầng 4."
    - "Tỷ trọng: ~30% Thép/Vật liệu làm case study thực chứng; ~70% Chiến lược Công nghiệp Xanh, Hạ tầng Năng lượng (Hạt nhân, Gió, Lưới 500kV, BESS) và Cú nhảy vọt Toàn cầu."
    - "Khắc sâu Thế Kiềng Ba Chân: Không có Thép xanh thì không có hạ tầng tự chủ; Không có Điện sạch & Điện Hạt nhân thì Thép vỡ trận nhãn xanh; Không có Thể chế DPPA/Sàn Carbon thì không giữ chân được FDI Bán dẫn & Apple/NVIDIA."
```

---

## TẦNG 2: GLOBAL ASCII ARCHITECTURE — THẾ KIỀNG BA CHÂN CÔNG NGHIỆP XANH

```
========================================================================================================
                                     BÀN CỜ ĐỊA KINH TẾ TOÀN CẦU (2026 - 2030)
  Áp lực từ ngoài: EU CBAM (75-100 EUR/tấn CO2) | Apple V5 (Net-Zero FY2029) | NVIDIA Scope 3 (+100%)
========================================================================================================
                                                  │
                                                  ▼
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
     │                      CÚ NHẢY VỌT CÔNG NGHIỆP SẠCH CỦA VIỆT NAM                         │
     │                           (THẾ KIỀNG BA CHÂN HOÀN HẢO)                                 │
     └────────────────────────────────────────────────────────────────────────────────────────┘
                                                  │
          ┌───────────────────────────────────────┼───────────────────────────────────────┐
          ▼                                       ▼                                       ▼
┌───────────────────────────┐   ┌───────────────────────────────────┐   ┌───────────────────────────┐
│ TRỤ CỘT 1: VẬT LIỆU XANH  │   │ TRỤ CỘT 2: SIÊU HẠ TẦNG NĂNG LƯỢNG│   │ TRỤ CỘT 3: THỂ CHẾ & ĐẦU  │
│     (263.000 TỶ VNĐ)      │   │    (ĐIỆN HẠT NHÂN, GIÓ & LƯỚI)    │   │            RA             │
├───────────────────────────┤   ├───────────────────────────────────┤   ├───────────────────────────┤
│• Hòa Phát Dung Quất 2:    │   │• Hồi sinh Điện Hạt nhân:          │   │• Bộ ba Thể chế:           │
│  85k tỷ, 9M tấn HRC, mẻ   │   │  Ninh Thuận 1 & 2 (QĐ 768/QĐ-TTg, │   │  - DPPA (NĐ 80 & 57)      │
│  ray 350km/h (QI/2027)    │   │  2030-2035) làm điện nền sạch 24/7│   │  - Sàn Carbon (NĐ 29/2026)│
│• VinMetal Hà Tĩnh:        │   │• Điện gió ngoài khơi & Thủy điện  │   │  - Green Taxonomy (QĐ 21) │
│  80k tỷ, thép vỏ xe điện  │   │  tích năng Bác Ái 1.200 MW        │   │• Khu công nghiệp sinh thái│
│  vượt rào CSDDD Scope 3   │   │• Pin lưu trữ BESS: 10k-16,3k MW   │   │  EIP (NĐ 35/2022)         │
│• Xuân Thiện Nam Định:     │   │• Xương sống 500kV Mạch 3 (519 km) │   │• Thị trường Đầu ra lớn:   │
│  >98k tỷ, DRI Hydro 2030, │   │  giải tỏa nghẽn mạch, tránh bài   │   │  - ĐSCT 67 tỷ USD         │
│  giảm 86% CO2             │   │  học 360 TWh lãng phí của TQ      │   │  - 11,6 tỷ USD FDI Bán dẫn│
└───────────────────────────┘   └───────────────────────────────────┘   └───────────────────────────┘
          │                                       │                                       │
          └───────────────────────────────────────┼───────────────────────────────────────┘
                                                  ▼
                     [ MỤC TIÊU VĨ MÔ: NỀN KINH TẾ 2.000 TỶ USD & NET ZERO 2050 ]
                     • Công nghiệp chế biến chế tạo >30% GDP (Nghị quyết 29-NQ/TW)
                     • Đóng góp 300 tỷ USD từ kinh tế xanh vào GDP 2050
                     • Đào tạo 50.000 kỹ sư công nghệ cao & làm chủ chuỗi giá trị
```

---

## TẦNG 3: 7 MÔ-ĐUN CHƯƠNG ĐỘC LẬP (ATOMIC CHAPTER BLUEPRINTS)

### CH01: HOOK — NGHỊCH LÝ 263.000 TỶ
- **Thesis:** Thép xây dựng dư thừa 5M tấn, BĐS đóng băng, DN thép cũ lỗ trăm tỷ, nhưng 263.000 tỷ vẫn đổ vào luyện kim mới.
- **Data Anchors:** `DATA-01` (Tồn kho >5M tấn), `DATA-22` (Tổng vốn 263k tỷ).
- **Narrative Bridge:** Mở bằng nghịch lý nội địa $\rightarrow$ Gieo câu hỏi chiến lược toàn cầu.

### CH02: CÁI GIÁ LỊCH SỬ — "BẨN TRƯỚC, DỌN DẸP SAU"
- **Thesis:** Dọn dẹp môi trường sau luôn đắt gấp hàng chục đến hàng trăm lần phòng ngừa trước. VN không đủ ngân sách để lặp lại sai lầm.
- **Data Anchors:** `DATA-27` (Superfund $1-2B $\rightarrow$ >$300B, 1.340 NPL), `DATA-28` (Emscher €5,5B, 30 năm, 51 km ngầm), `DATA-29` (Minamata 12.890 nạn nhân, 308,5 tỷ Yên), `DATA-14` (TQ cắt bỏ 360 TWh điện sạch H1/2026 do kẹt điện than).
- **Narrative Bridge:** Harvest từ CH01 $\rightarrow$ Gieo hạt: Người đi sau có thể nhảy cóc bỏ qua giai đoạn bẩn.

### CH03: QUY LUẬT NHẢY CÓC TOÀN CẦU (LEAPFROGGING)
- **Thesis:** Quốc gia đi sau không vướng chi phí di sản (Legacy Costs) có thể nhảy thẳng lên công nghệ thế hệ mới nếu có tư duy Tự xây (Builder) thay vì chỉ Đi mua (Buyer).
- **Data Anchors:** `DATA-30` (Kenya M-Pesa 50% GDP + Solar PAYG 11,6M), `DATA-31` (Ấn Độ UPI 21,7B GD/tháng + NGHM $2,2B), `DATA-32` (Morocco xuất Hydro sang EU), `DATA-33` (Indonesia cấm quặng thô $\rightarrow$ $10B+ FDI pin).
- **Narrative Bridge:** Harvest từ CH02 $\rightarrow$ Gieo hạt: VN từng nhảy cóc viễn thông và QR, giờ đang bước vào cú nhảy công nghiệp sạch.

### CH04: GIẢI MÃ 263.000 TỶ & CƠN KHÁT NĂNG LƯỢNG SẠCH
- **Thesis:** 3 đại dự án thép sạch (Hòa Phát, VinMetal, Xuân Thiện) giải quyết 3 bài toán tự chủ vật liệu (ray ĐSCT, vỏ xe điện, thép xanh tháp gió). Nhưng cả 3 không thể vận hành nếu thiếu nguồn điện sạch khổng lồ và ổn định.
- **Data Anchors:** `DATA-06` (HPG DQ2 85k tỷ, 9M HRC, tự phát >1,45 tỷ kWh), `DATA-07` (Ray HPG 350km/h QI/2027), `DATA-08` (VinMetal 80k tỷ), `DATA-09` (Xuân Thiện >98k tỷ DRI Hydro 2030), `DATA-24` (>80% quặng nhập khẩu).
- **Narrative Bridge:** Harvest từ CH03 $\rightarrow$ Gieo hạt: Lò hồ quang và nhà máy xanh cần hàng chục tỷ kWh điện sạch mỗi năm. Nguồn điện sạch và ổn định này đến từ đâu?

### CH05: SIÊU HẠ TẦNG NĂNG LƯỢNG & CUỘC ĐUA THỂ CHẾ (ĐIỆN HẠT NHÂN, GIÓ & DPPA)
- **Thesis:** Để nuôi các đại dự án vật liệu xanh và trung tâm bán dẫn, VN đang thiết lập Siêu Hạ Tầng Năng Lượng: Hồi sinh Điện Hạt nhân Ninh Thuận làm điện nền, phát triển Điện gió ngoài khơi, Mạch 3 500kV chống nghẽn mạch, kết hợp Bộ ba thể chế (DPPA, Sàn Carbon, Green Taxonomy) để đón Apple V5 và NVIDIA.
- **Data Anchors:** `DATA-38` (Điện hạt nhân Ninh Thuận 1 & 2 QĐ 768/QĐ-TTg), `DATA-39` (Điện gió ngoài khơi NĐ 272 + Thủy điện tích năng Bác Ái 1.200 MW), `DATA-40` (500kV Mạch 3 519 km Quảng Trạch - Phố Nối), `DATA-10` (Sàn Carbon NĐ 29/2026), `DATA-11` (DPPA NĐ 80 & 57), `DATA-12` (BESS 10k-16,3k MW), `DATA-34` (Apple V5 Net-Zero FY2029, 32 NM), `DATA-35` (NVIDIA Scope 3 +100%).
- **Narrative Bridge:** Harvest từ CH04 $\rightarrow$ Gieo hạt: Hạ tầng năng lượng và thể chế đã mở đường. Đầu ra thị trường cụ thể hấp thụ ở đâu?

### CH06: ĐẦU RA THỰC CHỨNG — BÁN DẪN, XE ĐIỆN & ĐƯỜNG SẮT CAO TỐC
- **Thesis:** Năng lượng sạch và vật liệu xanh tạo bệ phóng hút dòng vốn FDI chất lượng cao và phục vụ đại công trình quốc gia.
- **Data Anchors:** `DATA-17` (11,6 tỷ USD FDI bán dẫn), `DATA-18` (VinFast + V-GREEN 63 tỉnh), `DATA-19` (ĐSCT 67 tỷ USD, 6-8M tấn thép ray), `DATA-23` (50.000 kỹ sư bán dẫn).
- **Narrative Bridge:** Harvest từ CH05 $\rightarrow$ Gieo hạt: Đúc kết cú nhảy vọt và tương lai kinh tế.

### CH07: CÚ NHẢY THỨ BA & TẦM NHÌN KINH TẾ 2.000 TỶ USD
- **Thesis:** Sau Viễn thông (Cú nhảy 1) và Fintech/QR (Cú nhảy 2), VN đang thực hiện Cú nhảy thứ 3: Công nghiệp Xanh & Năng lượng Sạch. Tự chủ năng lượng và vật liệu là điều kiện tiên quyết để hóa rồng.
- **Data Anchors:** `DATA-20` (Kinh tế xanh 300 tỷ USD GDP 2050, quy mô 2.000 tỷ USD), `DATA-21` (Chế biến chế tạo >30% GDP NQ 29-NQ/TW).
- **Ending Tension:** Recontextualize câu hỏi mở đầu: 263.000 tỷ không phải làm thép thừa, mà là ván cờ kiến tạo nền móng tự chủ cho một kỷ nguyên mới.

---

## TẦNG 4: IMMUTABLE DATA VAULT (DANH MỤC 40 MỎ NEO DỮ LIỆU)

| Mã Anchor | Nội dung / Con số cốt lõi | Nguồn Kiểm chứng | Chương sử dụng |
| :--- | :--- | :--- | :--- |
| `DATA-01` | Tồn kho thép XD >5M tấn, nhập siêu 8-10M tấn HRC | `research_vault/001` | CH01 |
| `DATA-02` | Biên LN thép XD 3-5%, HRC xanh 15-22% | `research_vault/001` | CH04 |
| `DATA-03` | Phát thải BF-BOF: 1,8-2,2 tấn CO2/tấn thép | `research_vault/005` | CH04, CH05 |
| `DATA-04` | CBAM phạt 150-200 EUR/tấn thép BF-BOF | `research_vault/005` | CH05 |
| `DATA-05` | CSDDD Scope 3 bắt buộc từ 2026-2027 | `research_vault/005` | CH05 |
| `DATA-06` | HPG DQ2: 85.000 tỷ, 16M tấn, 9M HRC, tự phát >1,45 tỷ kWh | `research_vault/002` | CH04 |
| `DATA-07` | Ray HPG: 700k tấn/năm, 350 km/h, QI/2027 | `research_vault/002` | CH04, CH06 |
| `DATA-08` | VinMetal: 80.000 tỷ, GĐ1 5M, GĐ2 20M | `research_vault/003` | CH04 |
| `DATA-09` | Xuân Thiện: >98.000 tỷ, DRI Hydro T6/2030 | `research_vault/004` | CH04 |
| `DATA-10` | Sàn Carbon V-EUA: NĐ 29/2026 & QĐ 263 | `research_vault/006` | CH05 |
| `DATA-11` | DPPA: NĐ 80/2024 & NĐ 57/2025 | `research_vault/007` | CH05 |
| `DATA-12` | BESS 10.000-16.300 MW, giảm 30-40% chi phí | `research_vault/007` | CH05 |
| `DATA-13` | JETP 15,5 tỷ USD, tín dụng xanh >828.000 tỷ | `research_vault/007` | CH05 |
| `DATA-14` | TQ cắt bỏ 360 TWh điện sạch H1/2026 | `research_vault/008` | CH02 |
| `DATA-15` | Thép Hydro thế giới đắt hơn +25-30% | `research_vault/009` | CH04 |
| `DATA-16` | NQ 29-NQ/TW, QĐ 261, QĐ 165 Leapfrogging | `research_vault/008` | CH07 |
| `DATA-17` | FDI bán dẫn 11,6 tỷ USD (170 dự án) | `research_vault/008` | CH06 |
| `DATA-18` | VinFast + V-GREEN trạm sạc 63 tỉnh | `research_vault/003` | CH06 |
| `DATA-19` | ĐSCT Bắc Nam 67 tỷ USD, 6-8M tấn thép ray | `research_vault/002` | CH06 |
| `DATA-20` | Kinh tế xanh 300 tỷ USD GDP 2050, 2.000 tỷ USD | `research_vault/008` | CH07 |
| `DATA-21` | Tỷ trọng CBCC >30% GDP (NQ 29) | `research_vault/008` | CH07 |
| `DATA-22` | Tổng 263.000 tỷ vốn + 35.000 việc làm | `research_vault/002-004` | CH01, CH04 |
| `DATA-23` | Đề án 50.000 kỹ sư bán dẫn (QĐ 1018) | `research_vault/008` | CH06 |
| `DATA-24` | Quặng sắt nhập >80%, 18-20M tấn/năm | `research_vault/001` | CH04 |
| `DATA-25` | Suất giá Hydro $4-6/kg $\rightarrow$ $1,5-2/kg sau 2030 | `research_vault/009` | CH07 |
| `DATA-26` | AI Smart Grid & Twin Transition | `research_vault/007` | CH05 |
| `DATA-27` | Superfund Mỹ: $1-2B $\rightarrow$ >$300B, 1.340 NPL | `research_vault/009` | CH02 |
| `DATA-28` | Emscher Đức: €5,5B, 30 năm, 51 km ngầm | `research_vault/009` | CH02 |
| `DATA-29` | Minamata Nhật: 12.890 nạn nhân, 308,5 tỷ Yên | `research_vault/009` | CH02 |
| `DATA-30` | Kenya M-Pesa 50% GDP + Solar PAYG 11,6M | `research_vault/010` | CH03 |
| `DATA-31` | Ấn Độ UPI 21,7B GD/tháng + NGHM $2,2B | `research_vault/010` | CH03 |
| `DATA-32` | Morocco xuất Hydro/Ammonia sang EU | `research_vault/010` | CH03 |
| `DATA-33` | Indonesia cấm quặng nickel $\rightarrow$ $10B+ FDI | `research_vault/010` | CH03 |
| `DATA-34` | Apple V5: Net-Zero FY2029, 32 NM VN, $30B XK | `research_vault/011` | CH05 |
| `DATA-35` | NVIDIA Scope 3 +100%, >$6B Energy-First | `research_vault/011` | CH05 |
| `DATA-36` | Green Taxonomy QĐ 21: 45 lĩnh vực, 7 nhóm | `research_vault/011` | CH05 |
| `DATA-37` | EIP NĐ 35 + GEIPP UNIDO: 6 KCN | `research_vault/011` | CH05 |
| **`DATA-38`** | **Điện Hạt nhân Ninh Thuận 1 & 2 (QĐ 768/QĐ-TTg, 2030-2035)** | `research_vault/007`, `QĐ 768` | **CH05** |
| **`DATA-39`** | **Điện gió ngoài khơi (NĐ 272/2026) & Thủy điện tích năng Bác Ái (1.200 MW)** | `research_vault/007`, `QĐ 768` | **CH05** |
| **`DATA-40`** | **Đường dây 500kV Mạch 3 Quảng Trạch - Phố Nối (519 km, 5.000 MW)** | `research_vault/008` | **CH05** |
