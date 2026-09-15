---
description: Tuyến Remix — Tạo kịch bản mới từ video YouTube có sẵn, viết lại sáng tạo theo voice KenhTamLy
---

Dưới đây là Meta-Workflow tự động hóa quy trình **Remix Episode**: nhận link YouTube → bóc băng → phân tích → sáng tạo kịch bản mới không trùng lặp → thu âm.

**Chỉ thị cho AI (Antigravity):**
Bạn (Assistant) PHẢI liên tục thực hiện tuần tự các bước dưới đây. Bạn KHÔNG ĐƯỢC dừng lại hoặc tự ý kết thúc trừ khi gặp các điểm 🛑 **CHECKPOINT**. Tại checkpoint, bạn phải gọi `notify_user` để chờ người dùng duyệt rồi mới chạy tiếp.

---

### BƯỚC 1: BÓC BĂNG (TRANSCRIPT EXTRACTION)
1. Nhận URL YouTube từ user.
2. Xác định Video ID → tạo slug: `remix_[videoID]`.
3. Tạo thư mục `episodes/[slug]/`.
4. Chạy lệnh:
   ```bash
   node scripts/tools/extract_transcript.cjs "[URL]" "./episodes/[slug]"
   ```
5. Kiểm tra bộ artifact transcript:
   - `00_raw_transcript.txt`
   - `00_transcript_meta.json`
   - `00_transcript_segments.json`
6. Nếu không có transcript, kiểm tra:
   - `00_transcript_status.md`
   - `00_transcript_error.json`
7. KHÔNG được suy đoán nội dung video từ URL nếu transcript không lấy được. Khi transcript fail, phải dùng status/meta artifact để quyết định: thử lại, đổi video, hoặc xin transcript thủ công từ user.

---

### BƯỚC 2: AI ĐỌC HIỂU & PHÂN TÍCH
1. Đọc toàn bộ `00_raw_transcript.txt` (đọc kỹ, KHÔNG lướt).
2. **Bắt buộc tham chiếu**: `00_core/remix_differentiation_guide.md`.
3. Lập bảng phân tích theo template trong guide:
   - Chủ đề chính
   - Liệt kê 3-7 luận điểm chính
   - Số liệu & dữ liệu được dùng (có nguồn? có cập nhật?)
   - Điểm mạnh (giữ cảm hứng)
   - Điểm yếu / thiếu sót (cơ hội sáng tạo — thiếu data, thiếu case study, thiếu action plan)
   - So sánh đối tượng video gốc vs đối tượng KenhTamLy
4. Lưu vào `episodes/[slug]/01_source_analysis.md`.

---

### BƯỚC 3: DEEP DIFFERENTIATION & BRIEF
1. Áp dụng **ít nhất 2 trong 5 kỹ thuật** differentiation (xem guide).
2. Kích hoạt kỹ năng `script_architect`.
3. **Chạy Topic Depth Score** — xác định thời lượng phù hợp dựa trên độ sâu CỦA GÓC MỚI.
4. **DATA VALIDATION PLAN**: Liệt kê số liệu cần bổ sung + case study dự kiến cho mỗi chương.
5. Tạo `01_brief.md` theo template, bao gồm:
   - Nguồn cảm hứng (URL gốc)
   - Differentiation Strategy (kỹ thuật nào? góc mới là gì?)
   - Điểm khác biệt chính (ít nhất 3 điểm)
   - Depth Score
   - Data validation plan
6. 🛑 **CHECKPOINT 1:** Gửi `01_source_analysis.md` + `01_brief.md` cho user. Đợi user duyệt hướng đi sáng tạo.

---

### BƯỚC 4: SÁNG TẠO HOOK & DÀN Ý
1. Kích hoạt kỹ năng `hook_engine`.
2. Tạo 5-7 hooks — PHẢI khác hoàn toàn cách mở bài của video gốc. Ưu tiên hooks có con số gây sốc.
3. Lưu `02_hook_pack.md`.
4. 🛑 **CHECKPOINT 2:** Gửi hooks cho user chọn.
5. Sau khi user chọn hook → Kích hoạt `script_architect`.
6. Dựng `03_thesis_map.md` + `04_outline.md`.
7. **Luận điểm và cấu trúc PHẢI khác video gốc** — kiểm tra chéo với `01_source_analysis.md`.
8. 🛑 **CHECKPOINT 3:** Gửi outline cho user duyệt.

---

### BƯỚC 5: VIẾT KỊCH BẢN SÁNG TẠO (AUTOPILOT)
1. Kích hoạt kỹ năng `chapter_writer`.
2. **QUY TẮC ĐẶC BIỆT CHO REMIX:**
   - PHẢI đọc `00_raw_transcript.txt` để hiểu ý gốc, nhưng TUYỆT ĐỐI KHÔNG sao chép câu
   - Viết lại hoàn toàn bằng voice KenhTamLy
   - Tất cả case study, số liệu bổ sung phải MỚI (không lấy từ transcript gốc)
   - **TRANSITION BRIDGES:** Không viết tiêu đề chương. Thay bằng 2-3 câu chuyển tiếp mượt mà
4. Tuần tự viết `chapter_01.md` → `chapter_N.md`.
5. Cập nhật 3 file state sau mỗi chương: `05_continuity_packet.md`, `06_claim_ledger.md`, `07_golden_lines.md`.
6. Sau khi viết xong tất cả → kiểm tra tổng số từ vs Depth Score target.
*Tuyệt đối không dừng hỏi giữa chừng.*

---

### BƯỚC 6: POLISH & MERGE
1. Kích hoạt kỹ năng `oral_polisher`.
2. Gộp tất cả chapter thành `final_voiceover.md`.
3. **QUY TẮC MERGE REMIX:**
   - LOẠI BỎ hoàn toàn mọi tiêu đề chương, heading markdown
   - GIỮ NGUYÊN transition bridges
   - Output: 1 file text liền mạch, đọc từ đầu đến cuối không có đánh số
4. Kiểm tra: đọc liền 2 chương liên tiếp → transition bridge có mượt không?

---

### BƯỚC 7: QA + KIỂM TRA TRÙNG LẶP
1. Kích hoạt kỹ năng `financial_qa`.
2. **Kiểm tra trùng lặp BỔ SUNG:**
   - So sánh `final_voiceover.md` với `00_raw_transcript.txt`
   - Không có câu nào giống > 7 từ liên tiếp
   - Không có case study nào trùng
   - Cấu trúc luận điểm khác video gốc
4. Chạy Checklist 7 điểm chống trùng lặp (trong `remix_differentiation_guide.md`).
5. Sinh báo cáo `production_notes.md`.
6. 🛑 **CHECKPOINT 4:** Gửi `final_voiceover.md` + QA + báo cáo trùng lặp cho user. Đợi lệnh "Chốt / Thu âm đi".

---

### BƯỚC 8: SEO + THUMBNAIL + TTS
1. **YouTube Metadata:**
   - Tham chiếu `00_core/youtube_seo_guide.md`
   - Tạo `09_youtube_metadata.md` (tiêu đề viral + mô tả 5 block + hashtag 3 tầng)
2. **Thumbnail:**
   - Tham chiếu `00_core/thumbnail_style_guide.md`
   - Tạo `08_thumbnail_brief.md` (từ khóa + prompt)
3. **Thu âm:**
   - Kích hoạt `/record_voiceover`
   - Chạy: `node scripts/tts/record_episode.js [slug]`
4. Thông báo hoàn thành cho user.
