# AutoCapCut — Tự Động Hóa Dựng Video CapCut Trên macOS

Hệ thống tự động hóa đưa tài nguyên từ kịch bản phân cảnh (`scene_timing_map.json`), audio thuyết minh và video clips 8s lên Timeline của **CapCut Desktop (macOS)** với 3 Track chuẩn xác: Audio giọng đọc, Video cắt gọt khít thoại không drift, và Subtitle phụ đề tiếng Việt.

Sử dụng độc quyền engine **`capcut-cli` (renezander030)** — dự án mã nguồn mở hàng đầu thế giới về tương tác trực tiếp với draft store của CapCut.

---

## Cấu Trúc Thư Mục

```
AutoCapCut/
├── source/philipin/               # Dữ liệu nguồn (Audio, Video 8s, Timing Map)
├── tools/capcut-cli/              # Engine mã nguồn mở Node.js/TypeScript
├── scripts/
│   ├── sync_timing_engine.py      # Thuật toán tính toán nhịp thời gian & cắt gọt video
│   ├── generate_capcut_spec.py    # Sinh file spec.json declarative cho capcut-cli
│   └── run_autocapcut.py          # CLI điều phối quy trình
├── output_drafts/                 # Các dự án CapCut được tạo ra
└── docs/SETUP_GUIDE.md            # Hướng dẫn kỹ thuật chi tiết
```

---

## Sử Dụng Nhanh

1. **Kiểm tra môi trường:**
   ```bash
   node tools/capcut-cli/dist/index.js doctor
   ```

2. **Chạy thử nghiệm kiểm tra tính toàn vẹn (Dry-run):**
   ```bash
   python3 scripts/run_autocapcut.py --chapter 01 --dry-run
   ```

3. **Dựng dự án CapCut cho 1 chương (ví dụ Chương 01):**
   ```bash
   python3 scripts/run_autocapcut.py --chapter 01
   ```

4. **Xem thông tin dự án vừa tạo:**
   ```bash
   node tools/capcut-cli/dist/index.js info output_drafts/GocNhin_Philipine_Ch01 -H
   ```

---

## Điểm Nổi Bật Kỹ Thuật

- **Zero Heavy Dependencies:** Chạy trên Python chuẩn và Node.js có sẵn trên máy, không đòi hỏi thư viện bên ngoài phức tạp.
- **Đồng bộ hóa Master-Slave Clock:** Âm thanh giọng đọc làm Master Clock, các clip video 8s tự động cắt gọt theo độ dài câu thoại, tổng thời lượng khớp chuẩn xác từng microsecond.
- **Tương thích hoàn hảo CapCut macOS:** Tự động sinh `draft_info.json` và `draft_content.json`, sẵn sàng mở và xuất video trong CapCut Desktop.
