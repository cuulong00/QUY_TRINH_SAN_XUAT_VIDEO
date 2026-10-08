# Hệ Thống Sản Xuất Nội Dung: X-Economy

Hệ điều hành nội dung số chuyên sâu (Content OS) cho kênh **X-Economy**, phục vụ nghiên cứu và sản xuất các tác phẩm phân tích kinh tế vĩ mô toàn cầu, thị trường vốn, địa chính trị, chuỗi cung ứng công nghệ cao và tác động tới Việt Nam.

---

## 📌 Thông Tin Kênh & Nhận Diện Cốt Lõi
- **Tên Kênh:** X-Economy (https://www.youtube.com/@X-Economy)
- **YouTube Handle:** X-Economy
- **Slogan / Tagline:** DECODING THE GLOBAL ECONOMY (Giải Mã Kinh Tế Toàn Cầu)
- **Định vị nội dung:** Phóng sự phân tích chuyên sâu về kinh tế học vĩ mô, địa chính trị, thị trường vốn, tiền tệ và chuỗi cung ứng toàn cầu.
- **Phong cách thị giác:** 2D Cinematic Editorial Noir kết hợp Dữ liệu chuyển động (Motion Data Journalism).
- **Màu sắc chủ đạo:** Obsidian Midnight Navy (`#0A0E17`), Burnished Gold (`#D4AF37`), Electric Cyan (`#00E5FF`).
- **Tài sản thương hiệu:** Xem chi tiết tại [profile/](file:///Users/pro16/Documents/VideoProject/X-Economic/profile).

---

## 🏛️ Nguyên Tắc Vận Hành Cốt Lõi
1. **Dữ liệu thực chứng & Minh bạch nguồn gốc:** Mọi số liệu và luận điểm đều dựa trên báo cáo kiểm toán, dữ liệu từ các tổ chức uy tín (WB, IMF, Ngân hàng Trung ương) hoặc văn bản pháp lý chính thức. Ghi nhận mã dữ liệu `DATA-XX` và phân loại taxonomy rõ ràng.
2. **Tuân thủ pháp lý & An toàn thương hiệu:** Phân tích vĩ mô khách quan theo chuẩn *Lowe v. SEC (1985)*, tuyệt đối không khuyến nghị đầu tư tài chính. Bảo vệ phòng vệ phỉ báng doanh nghiệp, phân tích cơ chế thể chế và vận động thị trường, không phán xét đạo đức cá nhân.
3. **Quy chuẩn phát thanh tiếng Việt:** Tốc độ đọc chuẩn 223 - 235 từ/phút. Câu thoại dưới 150 ký tự (lý tưởng 100 - 120 ký tự cho tai nghe). Tuyệt đối không dùng dấu gạch ngang dài trong voiceover.
4. **Quy trình kiểm soát cổng nghiêm ngặt:** Mỗi lần một pha, dừng ở cổng để User duyệt trước khi chuyển pha tiếp theo.

---

## 📂 Cấu Trúc Thư Mục Dự Án
- `00_core/`: DNA của kênh: Voice DNA, Channel Bible, Quality Rubric, Visual Style Guide, Brand Safety, Macro Context.
- `01_management/`: Sổ cái tập phim (`episode_registry.csv`), backlog đề tài (`topic_backlog.md`), log hiệu suất tiêu đề (`title_performance_log.md`).
- `02_templates/`: Khuôn mẫu kịch bản chuẩn cho các pha sản xuất.
- `03_playbooks/`: Hướng dẫn tác chiến chuyên môn hóa.
- `.agents/`: Hiến pháp kênh (`AGENTS.md`), thẻ pha (`phases/`), kỹ năng chuyên sâu (`skills/`), nhân sự ảo (`personas/`), luồng công việc (`workflows/`), luật dự án (`rules/`).
- `.claude/`: Cấu hình tích hợp Claude Code (`settings.json`, `settings.local.json`).
- `profile/`: Bộ nhận diện thương hiệu (Avatar, Banner, Mô tả kênh, Brand Guidelines).
- `scripts/`: Bộ công cụ kiểm toán, tự động hóa và khởi tạo tập phim mới.
- `episodes/`: Thư mục lưu trữ dữ liệu sản xuất của từng tập phim.

---

## 🚀 Khởi Tạo Tập Phim Mới
```bash
bash scripts/new_episode.sh <ten-tap-phim-moi>
```
Sau đó tiến hành tuần tự theo các thẻ pha tại `.agents/phases/`, bắt đầu từ Pha 0 (`.agents/phases/pha_00_de_tai.md`).