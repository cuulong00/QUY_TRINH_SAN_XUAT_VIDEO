# 🌐 FacebookChannel — Trung Tâm Tuyển Chọn & Phân Phối Video Facebook

Dự án chuyên biệt trong hệ sinh thái của **Trần Tuấn Dương**, đảm nhận vai trò:
1. **Tuyển chọn & Tái phân phối (Curate & Repurpose):** Chọn lọc các video dài chất lượng cao nhất từ 2 kênh YouTube cốt lõi:
   - 🌊 **Dòng Chảy** (Địa chính trị, chu kỳ lịch sử, hưng vong thể chế).
   - 🎙️ **Góc Nhìn Podcast** (Xã hội học, kinh tế học vi mô/vĩ mô, chính sách công).
2. **Chuyển hóa văn phong chuẩn Meta (`The Meta Strategist`):** Không copy nguyên xi mô tả YouTube. Tái cấu trúc thành bài đăng Facebook đạt chuẩn *Meaningful Social Interactions (MSI)*: Hook 3 dòng đầu cuốn hút trước nút "Xem thêm", ngắt nhịp thị giác thoáng mắt, câu hỏi kích hoạt thảo luận đa chiều.
3. **Resumable Chunked Video Uploader:** Upload các file video master lớn (5 GB – 11 GB) từ CapCut lên Fanpage an toàn, không lo đứt cáp, tự động retry và có thanh tiến trình (progress bar).
4. **Tích hợp sâu Antigravity (`.agents/`):** Tự động nhận diện Agent, nạp persona chuyên gia, quy tắc phân phối và kỹ năng thao tác.

---

## 📂 Cấu trúc thư mục

```
FacebookChannel/
├── .agents/                    # [Antigravity Brain] Agent tự động đọc khi mở workspace
│   ├── AGENTS.md               # Chỉ dẫn tổng thể cho Agent
│   ├── personas/               # Persona The Meta Strategist
│   ├── rules/                  # Luật bài viết Facebook
│   ├── skills/                 # Kỹ năng upload video GB & chuyển hóa kịch bản
│   └── workflows/              # SOP quy trình tái chế nội dung
├── 00_core/                    # Hướng dẫn kỹ thuật & Định vị kênh
├── 01_management/              # Bảng backlog tuyển chọn video & log xuất bản
├── 02_templates/               # Mẫu bài đăng chuẩn Facebook
├── config/                     # Cấu hình nạp biến môi trường
├── src/                        # Engine Python (Client, Uploader, Adapter)
├── scripts/                    # Các lệnh CLI thực thi nhanh
└── storage/                    # Thumbnails và logs upload
```

---

## ⚡ Bắt đầu nhanh (Quick Start)

### 1. Cài đặt môi trường
```bash
cd /Users/pro16/Documents/VideoProject/FacebookChannel
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Cấu hình Fanpage
Copy file `.env.example` thành `.env` và điền thông tin:
```bash
cp .env.example .env
```
Xem hướng dẫn chi tiết lấy token vĩnh viễn tại `00_core/graph_api_guide.md`.

### 3. Kiểm tra kết nối Fanpage
```bash
python scripts/check_page.py
```

### 4. Chuyển đổi nội dung từ tập YouTube sang gói bài Facebook
```bash
python scripts/adapt_content.py \
  --source "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kinh-te-hoc-tam-linh" \
  --channel "gocnhin"
```

### 5. Upload Video dài lên Facebook
```bash
python scripts/upload_video.py \
  --file "/Users/pro16/Movies/CapCut/SieuCongTrinh_BatCom_Master/SieuCongTrinh_BatCom_Master.mp4" \
  --title "Siêu Công Trình Và Bát Cơm Dân Tộc" \
  --desc-file "storage/ready_posts/sieu_cong_trinh.txt" \
  --thumb "storage/thumbnails/sieu_cong_trinh.jpg"
```
