# BẢN ĐỒ LIÊN KẾT HỆ SINH THÁI (ECOSYSTEM INTEGRATION MAP)

Tài liệu này xác định giao diện dữ liệu (Data Interfaces) và cách thức luân chuyển tài nguyên giữa các trạm sản xuất:

---

## 🔄 Dòng Chảy Dữ Liệu Khép Kín (Data Flow)

```mermaid
sequenceDiagram
    autonumber
    actor Creator as Trần Tuấn Dương (Creator)
    participant S1 as Station 1: TroLyCaNhan / NotebookLM
    participant S2 as Station 2: Channel Episodes (Kịch bản)
    participant S3 as Station 3: VideoCore (Footage AI)
    participant S4 as Station 4: Code/TTS (Audio)
    participant S5 as Station 5: AutoCapCut (Dựng phim)
    participant S6 as Station 6: FacebookChannel & YouTube

    Creator->>S1: Đề tài & Báo cáo kiểm toán/dữ liệu vĩ mô
    S1->>S2: Cấu trúc luận điểm & Bức tranh toàn cảnh (buc_tranh_toan_canh.md)
    S2->>S2: Bẻ kịch bản thành phân cảnh (prompts_chapter_XX.txt)
    S2->>S3: Nạp prompt phân cảnh & ảnh tham chiếu
    S3->>S3: Veo 3.1 Lite render clips (.mp4) sạch bản quyền 100%
    S2->>S4: Nạp văn bản kịch bản
    S4->>S4: Sinh audio giọng đọc AI (.wav/.mp3)
    S3->>S5: Nạp toàn bộ footage phân cảnh
    S4->>S5: Nạp audio giọng đọc
    S5->>S5: AutoCapCut lắp timeline, bắn sub, render Master Video
    S5->>S6: Chuyển Master Video (5-11 GB)
    S6->>S6: Chuyển hóa kịch bản (The Meta Strategist) & Upload Resumable
```

---

## 📌 Quy Ước Đường Dẫn Chuẩn Của Mỗi Tập (Standard Episode Contract)

Mỗi tập video thuộc các kênh (`Dong_Chay`, `GocNhinPodcast`, `X-Economics`) đều tuân thủ cấu trúc chuẩn:

```text
episodes/[slug]/
├── buc_tranh_toan_canh.md              # Khung nghiên cứu, luận điểm phản biện, dữ liệu đối chứng
├── README.md                           # Metadata, trạng thái sản xuất, checklist
├── prompts/                            # Hoặc prompts_chapter_XX.txt (Dành cho VideoCore)
│   ├── chapter_01.txt
│   └── chapter_02.txt
├── ref_images/                         # Ảnh tham chiếu nhân vật/phong cách (@avatar.jpg)
├── videos/                             # Nơi chứa các clip footage MP4 do VideoCore sinh ra
└── audio/                              # File voiceover từ hệ thống TTS
```
