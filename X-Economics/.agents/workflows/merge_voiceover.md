---
description: >-
  Merge and compile all written chapters into a single master clean script (Phase 8: voiceover.md).
  Integrates the selected Master Hook and all chapter_XX.md files into a 100% clean voiceover text.
  Requires completed 04_hook_pack.md and all chapter_XX.md files.
---

# /merge_voiceover — Gộp Toàn Bộ Kịch Bản Thành Tệp Thoại Hoàn Chỉnh (Pha 8)

> 🛑 **CREATOR PERSONA:** `the_quality_czar` + `the_voice_architect`  
> 🛑 **MỤC TIÊU PHA 8:** Tạo ra tệp `episodes/[slug]/voiceover.md` duy nhất, chứa 100% văn bản thoại sạch hoàn chỉnh của toàn bộ tập phim (từ Hook mở đầu đến Outro kết thúc) để làm đầu vào chuẩn cho:
> 1. Kiểm toán Giữ chân Toàn bài (`retention_bridge_audit`)
> 2. Báo cáo Kiểm duyệt & An toàn (`10_compliance_report.md`)
> 3. Tối ưu Thuật toán & SEO (`metadata.md`)
> 4. Thu âm Giọng đọc (`/record_voiceover` hoặc Google TTS)
> 5. Phân cảnh & Trực quan hóa (`scene_timing_builder` ➔ `visual_map.csv`)

---

## 🛑 HARD GATE ĐẦU VÀO BẮT BUỘC

Trước khi chạy Pha 8, Agent PHẢI xác nhận sự tồn tại của:
- `episodes/[slug]/04_hook_pack.md` (chứa Master Hook được chọn) ✅
- `episodes/[slug]/07_outline.md` (chứa tổng ngân sách từ $W_{\text{target}}$) ✅
- Tất cả các tệp `episodes/[slug]/chapter_01.md` đến `chapter_XX.md` theo danh sách chương trong outline ✅

Nếu thiếu bất kỳ chương nào ➔ **DỪNG LẠI**, yêu cầu hoàn thành Pha 7 (`/write_chapter`) trước.

---

## CÁC BƯỚC THỰC THI

### Bước 1: Giao Thức Ghi Log Tiền Khởi Động (Pre-Flight Logging)
TRƯỚC KHI tạo `voiceover.md`, Agent BẮT BUỘC in hộp log ra màn hình chat:
```markdown
> 🚀 **[PRE-FLIGHT LOG: TIỀN KHỞI ĐỘNG PHA 8 — MERGE VOICEOVER]**
> - 🧠 **Chuyên Gia (Persona DNA) Kích Hoạt:** The Quality Czar + The Voice Architect
> - ⚙️ **Kỹ Năng (Skill) Dẫn Đường:** `/merge_voiceover` (`chapter_writer/SKILL.md`)
> - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**
>   * `episodes/[slug]/04_hook_pack.md` (Master Hook)
>   * `episodes/[slug]/chapter_01.md` đến `chapter_XX.md` (Toàn bộ kịch bản các chương)
>   * `episodes/[slug]/07_outline.md` (Ngân sách từ và nhịp điệu)
> - 🎯 **Tài Liệu Đích Xuất Ra:** `episodes/[slug]/voiceover.md`
> - 🛡️ **Rào Cản Kiểm Toán:** 100% văn bản thoại sạch, khử sạch tiêu đề rác, kiểm đếm tổng số từ và thời lượng thực tế so với mục tiêu.
```

### Bước 2: Tích Hợp & Thanh Lọc Văn Bản Thoại (Prose Sanitization)
1. **Lấy Master Hook:** Trích xuất đoạn văn bản thoại của Master Hook đã được phê duyệt từ `04_hook_pack.md`.
2. **Gộp Tuần Tự:**
   - Đặt Master Hook ở đầu (hoặc tích hợp mượt mà vào đầu Chương 1 nếu Chương 1 chưa có Hook).
   - Nối tiếp lần lượt toàn bộ nội dung thoại từ `chapter_01.md`, `chapter_02.md`, ..., `chapter_XX.md`.
3. **Thanh Lọc Kỹ Thuật (Sanitization Gate):**
   - Xóa bỏ 100% các tiêu đề markdown kỹ thuật (`# chapter_01.md`, `## Chương 1: ...`, `[CH01_SC001]`).
   - Xóa bỏ mọi ghi chú hình ảnh, visual cues, timestamps thô hoặc metadata vận hành.
   - Giữ lại phân cách giữa các chương bằng 1 dòng kẻ ngang `---` hoặc 1 khoảng trống đoạn văn rõ ràng.
   - Đảm bảo 100% câu thoại sạch, tự nhiên, không chứa dấu gạch ngang dài (`—`) và không chứa từ cấm AI (`anti_ai_isms.md`).

### Bước 3: Kiểm Kê Ngân Sách & Thống Kê Thông Số Thực Tế
Tính toán các chỉ số kỹ thuật và in bảng nghiệm thu ra chat:
- **Tổng số từ thực tế ($W_{\text{actual}}$):** Đếm chính xác số từ của `voiceover.md`.
- **Tổng số từ mục tiêu ($W_{\text{target}}$):** So sánh với ngân sách từ trong `07_outline.md`.
- **Độ lệch ngân sách ($\Delta W$):** Đảm bảo nằm trong dung sai cho phép $\pm 10\%$.
- **Thời lượng ước tính (@ 220 WPM):**
  $$\text{Thời lượng (phút)} = \frac{W_{\text{actual}}}{220}$$

### Bước 3.5: Kiểm Toán Cấu Trúc Phân Đoạn (Paragraph Integrity Hard Gate)
Trước khi ghi tệp, Agent BẮT BUỘC kiểm toán tính toàn vẹn của các đoạn văn:
- **Nguyên tắc cốt lõi:** Văn bản thoại cho voiceover PHẢI viết dưới dạng các đoạn văn văn xuôi tự nhiên (prose paragraphs), mỗi đoạn gồm 2 đến 4 câu liên kết chặt chẽ về nội dung và logic nhân quả.
- **TUYỆT ĐỐI CẤM NGẮT DÒNG TỪNG CÂU:** Cấm tuyệt đối việc xuống dòng `\n\n` sau mỗi câu đơn lẻ làm vỡ vụn kịch bản thành danh sách rời rạc.
- **Chỉ số kiểm toán $S/P$ Bắt buộc:**
  $$S/P = \frac{\text{Tổng số câu}}{\text{Tổng số đoạn văn}} \ge 1.8$$
  * Nếu $S/P < 1.5$: Tệp kịch bản bị đánh rớt ngay lập tức vì mắc lỗi "ngắt dòng cụt lủn". Agent bắt buộc phải gom các câu liên quan thành đoạn văn hoàn chỉnh trước khi lưu tệp.
  * Tách bạch 100%: Phân cảnh thị giác (Scene timing map) có thể là 1 câu/scene, nhưng văn bản thoại trong `voiceover.md` PHẢI là đoạn văn tự nhiên.

### Bước 4: Lưu Tệp
Ghi toàn bộ văn bản thoại sạch đã thanh lọc vào `episodes/[slug]/voiceover.md`.
Thông báo hoàn tất và sẵn sàng chuyển giao cho **Pha 9: Retention Bridge Audit** và **Pha 10-11: Compliance Council**.
