# Thư Viện Template Chuẩn Hóa CapCut — Góc Nhìn Podcast

Hệ thống template chuẩn hóa dành riêng cho CapCut Desktop, kế thừa và tối ưu từ các dự án mã nguồn mở hàng đầu thế giới (**cutcli-cookbook**, **pyJianYingDraft**) và hệ quy chuẩn thị giác **Góc Nhìn Podcast DNA (v3.0)**.

---

## 1. Danh Mục Subtitle Styles (`templates/subtitle_styles/`)

| File Template | Phong Cách | Đặc Điểm Nhận Diện | Trường Hợp Sử Dụng |
| :--- | :--- | :--- | :--- |
| `vox_documentary_card.json` | **The Vox / Bloomberg Card** | Hộp đen mờ bán trong suốt bo tròn 8px (`alpha: 0.65`), chữ trắng/vàng thanh lịch 11pt, căn giữa 1/3 dưới. | Khuyên dùng cho toàn bộ video phóng sự, phân tích vĩ mô, đảm bảo dễ đọc 100% trên mọi nền sáng tối. |
| `johnny_harris_minimal.json` | **Johnny Harris Minimalist Stroke** | Chữ Vàng Hổ Phách (`#FFD700`) 12pt, viền nét đen sắc nét 0.12, đổ bóng mềm góc -45°, không hộp đen. | Dùng cho các thước phim điện ảnh sâu lắng, muốn khung hình mở rộng tối đa và tôn vinh tranh vẽ. |
| `keyword_highlight_gold.json` | **Bloomberg Keyword Highlight** | Chữ trắng chạy nhịp nhàng, tự động sáng bừng từ khóa số liệu, mốc năm hoặc danh từ riêng sang màu Vàng Hổ Phách. | Dùng cho các phân đoạn chứa nhiều dữ liệu kinh tế, con số tài chính chấn động. |
| `cinematic_title.json` | **Cinematic Title Overlay** | Chữ lớn 22pt, xuất hiện mờ dần (`fade-in 0.6s`) và tan biến êm ái. | Dùng ở đầu mỗi Chương (Chapter Title) hoặc mốc chuyển đề mục lớn. |
| `lower_third_callout.json` | **Documentary Lower-Third Callout** | Chữ ngọc xanh (`#26A69A`) trên nền Slate (`#1E293B`) góc dưới bên trái cách đáy 25% (chuẩn Lower-Left 25% Rule). | Dùng để chú thích danh tính nhân vật biểu tượng (nguyên thủ, CEO), địa danh, trích dẫn đạo luật. |

---

## 2. Danh Mục Motion & Transition Presets (`templates/motion_presets/`)

| File Template | Loại | Thuộc Tính / Slug | Hiệu Ứng |
| :--- | :--- | :--- | :--- |
| `smooth_fade_transition.json` | Transition | `black-fade` (400ms) | Chuyển cảnh Mờ đen nhẹ nhàng, tạo nhịp thở điện ảnh giữa các phân cảnh. |
| `dissolve_transition.json` | Transition | `dissolve` (400ms) | Chuyển cảnh hòa tan chéo hình ảnh mượt mà. |
| `ken_burns_push_in.json` | Keyframe Motion | Scale `1.0` $\rightarrow$ `1.12` (Ease-out) | Tạo chuyển động thu hút thị giác nhẹ nhàng cho tranh vẽ hoặc clip tĩnh. |

---

## 3. Quy Chuẩn Đồng Bộ & Pacing (Master Clock Rule)

1. **Rhythmic Subtitle Pacing:**
   - Mỗi câu thoại được chia nhỏ thành các cụm từ **3 đến 5 từ** (1.0s – 1.8s/cụm, tối đa 24 ký tự).
   - Tuyệt đối không để nguyên 1 câu dài 20 từ đứng yên trơ trọi suốt 5-7 giây.
2. **Audio Stripping Mandate:**
   - Tất cả video clip đưa vào dựng phải được tách sạch luồng âm thanh gốc (`ffmpeg -c:v copy -an`) để bảo đảm không có hiện tượng chồng âm lên voiceover.
