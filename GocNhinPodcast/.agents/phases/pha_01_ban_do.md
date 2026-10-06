# Thẻ Pha 1: Bản đồ nước đi và giả thuyết cạnh tranh

**Mục tiêu.** Thấy toàn bộ hệ thống quanh câu hỏi trung tâm, gồm các bên, thị trường, đối thủ, luật chơi, khâu phụ thuộc, bối cảnh. Đặt ít nhất ba giả thuyết cạnh tranh và biết dữ kiện nào sẽ phân biệt chúng.

## Đọc, theo thứ tự
1. `00_hien_chuong.md` (toàn bộ).
2. Báo cáo Gem Scout của tập trong `research_raw/`.
3. `.agents/workflows/build_global_vision.md`: Bước 2a "Bản Đồ Nước Đi", Bước 2b "Bản Đồ Nền → Giả Thuyết → Ma Trận", và mục "CHECKLIST NGHIỆM THU".
4. Khuôn: `02_templates/masterpiece_pipeline/01_global_vision_synthesis_template.md`, `00_bang_gia_thuyet_template.md`, `00_so_du_kien_template.md`.
5. Persona: `.agents/personas/the_macro_strategist.md` (chính); `the_critical_auditor.md` cho phần phản biện.
6. Luật sổ dữ kiện: `.agents/rules/claim-ledger.md`.

## Không cần đọc
`strategy_council` đầy đủ, các skill viết, `00_core` về giọng.

## Cách làm
- Đi theo sáu vòng của Bước 2a. Vòng nào trống thì ghi thành câu hỏi con "chưa rõ", không lấp bằng hiểu biết sẵn có của model.
- Luôn có một giả thuyết "nhàm" (chủ thể làm đúng điều nó công bố). Với mỗi giả thuyết, ghi dữ kiện nào sẽ bác nó.
- Mỗi dữ kiện vào sổ kèm **vị trí nguồn gốc** (URL kèm đoạn, hoặc `research_raw/<file>`). Manh mối Gem chưa mở được nguồn thì để ở cột "chưa rõ".
- Các câu hỏi lớn và điểm nghẽn của bản đồ cần xác định trước câu hỏi truy lùng vật chứng (quyết định, văn bản, công trình, khoảnh khắc có ngày giờ và chủ thể) để chuyển giao sang Pha 2 gom vào Kho vật chứng `VC-xx`.

## Giới hạn
`01_global_vision_synthesis.md` tối đa 3.000 từ. Bản đồ dùng để nghĩ, không phải để chép lại ở các pha sau.

## Đầu ra
`01_global_vision_synthesis.md` (Tầng 4 có nhắc định hướng vật chứng `VC-xx`), `00_bang_gia_thuyet.md`, các hàng đầu của `00_so_du_kien.md`; N1, N2, N4 điền vào hiến chương.

## Cổng và dừng
Chạy `python3 scripts/kiem_pha.py <slug> --pha 1`. User duyệt bản đồ và giả thuyết.
