# Title & Thumbnail Performance Log

> **Mục đích:** Theo dõi hiệu quả title, thumbnail, và hook strategy qua từng episode. Dữ liệu từ file này được dùng để cải thiện Metadata Strategist và Hook Engine.
> **Cập nhật:** Sau mỗi postmortem (7-14 ngày sau publish).

---

## Bảng Performance

| # | Episode Slug | Title dùng | Hook Strategy | Thumbnail Headline | CTR | AVD% | Views 7d | Bài học rút ra |
|---|-------------|-----------|---------------|-------------------|-----|------|----------|----------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

## Patterns Đã Xác Nhận

### ✅ Patterns hoạt động tốt
1. [THU THẬP DỮ LIỆU]

### ❌ Patterns hoạt động kém
1. Thuật ngữ chuyên gia trong title → CTR thấp (evidence: anti_patterns #24)

## Quy tắc
1. GHI ĐÚNG SỰ THẬT — không tô hồng, không bào chữa
2. Mỗi episode PHẢI có 1 dòng trong bảng, kể cả khi chưa có full data
3. Sau 20 episodes → rút ra 3 quy tắc title/thumbnail cứng dựa trên data
4. Metadata Strategist PHẢI đọc file này ở Bước 0 (Anti-Repetition Scan)
