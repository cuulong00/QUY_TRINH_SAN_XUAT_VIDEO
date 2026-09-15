# 🎬 QUY TRÌNH SẢN XUẤT VIDEO (Video Production Operating System — VPOS)

Hệ thống điều phối sản xuất nội dung video/podcast trí tuệ cao, phân tích chuyên sâu đa kênh của **Trần Tuấn Dương**. 

Hệ thống kết nối 6 trạm sản xuất khép kín, từ nghiên cứu dữ liệu định lượng, sinh kịch bản phân cảnh, tạo footage độc bản bằng AI (Veo 3.1 Lite), tổng hợp giọng đọc, dựng phim tự động qua CapCut, đến phân phối đa nền tảng (YouTube & Facebook).

---

## 🏛️ Kiến Trúc Hệ Sinh Thái 6 Trạm Sản Xuất

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               VPOS: HỆ ĐIỀU HÀNH SẢN XUẤT VIDEO (CHIEF ORCHESTRATOR)                   │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
   ┌────────────────────────────────────────┴────────────────────────────────────────┐
   ▼                                                                                 ▼
[STATION 1: NGHIÊN CỨU & DỮ LIỆU]                                      [STATION 4: GIỌNG ĐỌC AI]
• TroLyCaNhan & NotebookLM CLI                                         • Code/TTS System
• Báo cáo kiểm toán, GSO, World Bank                                   • Giọng đọc AI chuyên nghiệp
• Markdown Research Vaults                                             • Xử lý audio, nhịp điệu
   │                                                                                 │
   ▼                                                                                 ▼
[STATION 2: KỊCH BẢN PHÂN CẢNH]                                        [STATION 5: DỰNG PHIM TỰ ĐỘNG]
• X-Economics: Kinh tế học vĩ mô & thể chế                             • AutoCapCut Automation Engine
• GocNhinPodcast: Xã hội học & chính sách công                         • Ráp timeline, audio, subtitle
• Dong_Chay: Địa chính trị & chu kỳ lịch sử                            • Hiệu ứng, chuyển cảnh, cover
• Prompts phân cảnh: prompts_chapter_XX.txt                                         │
   │                                                                                 ▼
   ▼                                                                   [STATION 6: PHÂN PHỐI ĐA KÊNH]
[STATION 3: SẢN XUẤT FOOTAGE ĐIỆN ẢNH]                                 • YouTube Official Channels
• VideoCore: Nano Banana 2 & Veo 3.1 Lite                              • FacebookChannel:
• Điều khiển qua Chrome Canary CDP:9222                                  - Resumable Chunked Upload (GB)
• Footage độc bản 2K-4K sạch 100% bản quyền                              - Chuẩn thuật toán The Meta Strategist
```

---

## 📂 Danh Mục Các Repository Thành Phần

| Thư mục | Trạm / Vai trò | Bản chất & Chức năng cốt lõi |
| :--- | :--- | :--- |
| **`TroLyCaNhan/`** | Station 1: Research & Agents | Khung quản trị các Siêu Trợ Lý AI chuyên môn hóa, kịch bản & prompt standards |
| **`X-Economics/`** | Station 2: Channel Core | Kênh nghiên cứu kinh tế học vĩ mô, thị trường vốn, chu kỳ tiền tệ và thể chế |
| **`GocNhinPodcast/`** | Station 2: Channel Core | Kênh phân tích xã hội học, chính sách công, giáo dục và kinh tế đô thị |
| **`Dong_Chay/`** | Station 2: Channel Core | Dự án video tài liệu lịch sử vĩ mô, địa chính trị và sự hưng vong của các thể chế |
| **`VideoCore/`** | Station 3: Footage Engine | Cỗ máy sản xuất video theo phân cảnh (Veo 3.1 Lite qua Chrome Canary CDP:9222) |
| **`AutoCapCut/`** | Station 5: Assembly Plant | Hệ thống tự động hóa dựng video, ghép timeline, subtitle và hiệu ứng CapCut |
| **`FacebookChannel/`** | Station 6: Distribution Hub | Kênh vệ tinh tuyển chọn video dài, Resumable Chunked Uploader (5-11 GB) |

---

## ⚡ Lệnh Điều Phối Master (Chief Orchestrator CLI)

Hệ thống tích hợp công cụ điều phối trung tâm `orchestrator.py`:

```bash
# 1. Kiểm toán sức khỏe và tiến độ toàn bộ hệ thống
python3 orchestrator.py status

# 2. Khởi tạo một tập video mới đồng bộ trên một kênh
python3 orchestrator.py new-episode --channel gocnhin --slug "ten-tap-moi" --title "Tiêu Đề Tập Mới"

# 3. Quét các tập đã sẵn sàng để chuyển sang trạm tiếp theo
python3 orchestrator.py scan-pipeline
```

---

## 🧠 Bộ Chỉ Huy Antigravity (`.agents/`)
Repository này chứa bộ não tối cao của **Antigravity (Chief Production Orchestrator)**. Khi mở bất kỳ dự án nào trong cây thư mục này, Agent sẽ tự động nạp vai trò Tổng Quản Lý, tuân thủ các quy tắc bản quyền sạch, quy chuẩn kịch bản phản biện cao và quy trình sản xuất khép kín.
