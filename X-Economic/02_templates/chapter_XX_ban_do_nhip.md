# Bản Đồ Nhịp Ý & Danh Mục Shot — Chương [XX]

> Tài liệu này là nguồn sự thật duy nhất (Single Source of Truth) định vị phân cảnh theo nhịp ý của Chương XX cho kênh **X-Economy**.
> Tuân thủ nghiêm ngặt Hợp đồng Kiến trúc Phân cảnh theo Nhịp Ý tại `.agents/contracts/i2v_nhip_y.md`.

---

## 🗺️ Bản Đồ Nhịp Ý (Beat-to-Shot Mapping)

<!--
Mỗi nhịp là một khối mở đầu bằng ### CHXX_NYY.
Các trường bắt buộc:
- cau_thoai: chép nguyên văn các câu thoại thuộc nhịp từ chapter_XX.md (dùng blockquote >). Nối toàn bộ cau_thoai phải khớp 100% toàn văn chương.
- y: một câu tóm tắt ý chính của nhịp (không chép lại lời thoại).
- thoi_luong_uoc: số giây ước tính (tổng số từ chia tốc độ đọc chuẩn của kênh 223–235 từ/phút). Khi có audio thật sẽ được cập nhật từ Whisper.
- shots: danh sách 1 hoặc nhiều shot phân rã từ nhịp ý:
  - CHXX_NYY_SZ | [LOẠI_SHOT] | tu: "[vài từ đầu câu thoại nơi shot bắt đầu]" | ly_do: [vì sao chọn loại hình này hoặc chuyển cảnh ở đây] | so: [con số hiển thị kèm mã claim F-XX, hoặc 'không']
  (Thêm '| chuyen_dong: [mô tả]' nếu shot > 10s; thêm '| lien_mach: [mô tả]' nếu shot nối tiếp)
Loại shot hợp lệ: VIDEO_AI | BROLL | INFOGRAPHIC_TINH | INFOGRAPHIC_DONG | BAO_CHI
-->

### CHXX_N01
- cau_thoai:
  > [Câu thoại mở đầu của nhịp ý thứ nhất...]
  > [Câu thoại tiếp theo cùng nằm trong nhịp ý...]
- y: [Ý chính cốt lõi của nhịp 1]
- thoi_luong_uoc: [Số giây ước tính, ví dụ 6]
- shots:
  - CHXX_N01_S1 | VIDEO_AI | tu: "[Vài từ đầu]" | ly_do: [Lý do chọn loại này] | so: không

### CHXX_N02
- cau_thoai:
  > [Câu thoại của nhịp ý thứ hai chứa số liệu hoặc bằng chứng lịch sử/pháp lý...]
- y: [Ý chính cốt lõi của nhịp 2]
- thoi_luong_uoc: [Số giây ước tính, ví dụ 8]
- shots:
  - CHXX_N02_S1 | INFOGRAPHIC_TINH | tu: "[Vài từ đầu]" | ly_do: [So sánh số liệu / bản đồ địa chính trị] | so: [Con số kèm mã claim, ví dụ: 15,1% (F-XX)]

---

## 📋 Kiểm Tra Tính Toàn Vẹn Trước Khi Bàn Giao
1. Toàn bộ `cau_thoai` ghép lại khớp 100% văn bản sạch của `chapter_XX.md`.
2. Không có shot nào dưới sàn thời lượng (Sàn: VIDEO_AI ≥ 4s, BROLL ≥ 5s, INFOGRAPHIC_TINH ≥ 4s, BAO_CHI ≥ 5s; riêng Hook ≥ 2.5s).
3. 100% con số hiển thị đều có mã claim tương ứng trong `10_compliance_report.md`.
4. Mỗi shot trong bản đồ có đúng một khối đặc tả tương ứng trong 4 file track (`chapter_XX_video_ai.md`, `chapter_XX_broll.json`, `chapter_XX_infographic.md`, `chapter_XX_bao_chi.md`).
