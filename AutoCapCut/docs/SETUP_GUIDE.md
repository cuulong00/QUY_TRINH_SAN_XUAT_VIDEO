# Hướng Dẫn Kỹ Thuật & Cấu Trúc Dự Án AutoCapCut (macOS)

Tài liệu này mô tả chi tiết kiến trúc, cấu hình môi trường và hướng dẫn vận hành hệ thống tự động hóa dựng video trên **CapCut Desktop (macOS)** sử dụng độc quyền engine mã nguồn mở **`capcut-cli` (renezander030)**.

---

## 1. Kiến Trúc Tổng Thể

```
AutoCapCut/
├── source/
│   └── philipin/
│       ├── audio/                 # 8 file chapter_01.wav ... chapter_08.wav
│       ├── video/                 # 8 thư mục chứa 314 clip MP4 (8s/clip)
│       └── scene_timing_map.json  # Kịch bản phân cảnh và câu thoại
├── tools/
│   └── capcut-cli/                # Engine lõi Node.js/TypeScript (v0.22.0)
├── scripts/
│   ├── sync_timing_engine.py      # Engine tính toán nhịp thời gian & cắt gọt video
│   ├── generate_capcut_spec.py    # Trình sinh cấu hình declarative spec.json
│   └── run_autocapcut.py          # CLI điều phối chính toàn bộ pipeline
├── output_drafts/                 # Thư mục chứa các dự án CapCut được tạo ra
└── docs/
    └── SETUP_GUIDE.md             # Hướng dẫn này
```

---

## 2. Các Thành Phần Lõi

### A. Engine Dựng Phim: `tools/capcut-cli` (v0.22.0)
- **Cơ chế:** Đọc và ghi trực tiếp vào tệp nháp của CapCut. Trên macOS, nó tự động sinh và đồng bộ song song cả `draft_info.json` (chuẩn macOS) và `draft_content.json` (chuẩn Windows).
- **Lệnh biên dịch (`compile`):** Chuyển đổi file kịch bản `spec.json` thành project CapCut hoàn chỉnh với 3 Track chỉ trong ~0.15 giây.
- **Kiểm toán (`lint`):** Tự động quét lỗi hở timeline, phụ đề tràn màn hình hoặc file media bị thiếu.
- **Xuất video (`export-batch`):** Tích hợp sẵn AppleScript để tự động mở dự án trong CapCut macOS và kích hoạt Export.

### B. Module Đồng Bộ Nhịp: `scripts/sync_timing_engine.py`
- **Master Clock (Audio):** Dùng module `wave` chuẩn của Python để đo thời lượng file âm thanh chính xác đến từng microsecond ($1\text{s} = 1.000.000\mu\text{s}$).
- **Slave Clock (Video Clips 8s):** Tự động phân bổ thời lượng hiển thị cho từng clip dựa trên tỷ trọng số lượng ký tự/từ của câu thoại trong phân cảnh đó. Cắt gọt clip gốc từ $0\text{s}$ đến $\Delta t_i$ với tốc độ gốc $1.0\times$.
- **Phụ đề (Subtitles):** Tự động căn chỉnh mốc xuất hiện và thời lượng của từng câu thoại khít theo giọng đọc.

### C. CLI Điều Phối: `scripts/run_autocapcut.py`
Giao diện dòng lệnh tập trung để người dùng hoặc AI Agent dễ dàng kích hoạt mọi tác vụ.

---

## 3. Hướng Dẫn Vận Hành (Command Line)

### Kiểm tra môi trường (Doctor Check)
```bash
node tools/capcut-cli/dist/index.js doctor
```

### Chạy thử nghiệm kiểm tra tính hợp lệ kịch bản (Dry Run)
Kiểm tra xem toàn bộ file video, audio và kịch bản có khớp nhau không mà không ghi đè file:
```bash
python3 scripts/run_autocapcut.py --chapter 01 --dry-run
```

### Chỉ sinh file kịch bản Spec JSON (để xem trước cấu trúc)
```bash
python3 scripts/run_autocapcut.py --chapter 01 --spec-only
```

### Dựng một chương cụ thể (ví dụ Chương 01)
```bash
python3 scripts/run_autocapcut.py --chapter 01
```
Dự án hoàn chỉnh sẽ được tạo tại: `output_drafts/GocNhin_Philipine_Ch01/`.

### Dựng toàn bộ 8 chương
```bash
python3 scripts/run_autocapcut.py --all-chapters
```

### Dựng và tự động cài đặt thẳng vào CapCut Desktop macOS
```bash
python3 scripts/run_autocapcut.py --chapter 01 --install-to-capcut
```
Dự án sẽ xuất hiện ngay lập tức trên màn hình chính của ứng dụng CapCut Desktop.
