# ⛔ PRE-FLIGHT THINKING GATE — Bắt Buộc Trước Khi Viết Bất Kỳ Chapter Nào

> **LỆnh cứng:** Nếu agent chưa trả lời đầy đủ TẤT CẢ câu hỏi trong Gate này — **NGHIÊM CẤM gõ một chữ nào vào chapter**. Vi phạm gate này là nguyên nhân số 1 dẫn đến việc phải viết lại từ đầu, tốn token vô ích.

---

## GATE 0 — ⛔ TARGETED VAULT RECALL (BẢO CHỨNG TRÍCH LỤC VAULT)

Thực hiện đầy đủ quy trình Dual-Layer Data trong `chapter_writer/SKILL.md` §Kiến Trúc Dual-Layer:
- **Bước 0.1:** Nạp Tầm Nhìn Vĩ Mô & Cẩm Nang Phong Cách Chuyên Biệt (7 file kiến trúc và tệp style tương ứng trong `00_core/styles/`, MỘT LẦN đầu session)
- **Bước 0.2:** Nạp Dữ Liệu Vi Mô cho CHƯƠNG ĐANG VIẾT (vault files theo trường 11)

**BẮT BUỘC BẢO CHỨNG TRÍCH LỤC:** 
Agent phải trích dẫn nguyên văn ít nhất 1-2 câu quan trọng chứa dữ liệu thực tế từ các file vault đã mở đọc cho chương này, ghi rõ:
1. Tên file vault (`grab_vs_gsm-XX.md`)
2. Số dòng bắt đầu và kết thúc (`LXX-LXX`)
3. Nội dung nguyên văn (Raw quote)

Tự kiểm tra:
- [ ] Đã đọc 7 file kiến trúc (Bước 0.1)
- [ ] Đã đọc vault files cho chương này theo trường 11 (Bước 0.2)
- [ ] Đã ghi ra BẢO CHỨNG TRÍCH LỤC nguyên văn + số dòng ở trên
- [ ] Hiểu rõ chương này nằm ở đâu trong arc tổng thể
- [ ] Mọi con số sẽ dùng đã có trong vault files vừa đọc

**Nếu bất kỳ checkbox nào chưa tick hoặc thiếu Bảo chứng trích lục nguyên văn -> NGHIÊM CẤM viết.**

---

## GATE 1 — Kiểm tra vai trò (Role Clarity)

**Câu hỏi bắt buộc tự trả lời:**
- [ ] Tôi đang đóng vai **THE NARRATIVE DIRECTOR**, dùng lăng kính **THE DATA AUDITOR** để kiểm chứng. Giọng viết luôn là Narrative Director.
- [ ] Tôi **KHÔNG** phải nhà phân tích kinh tế. Tôi **KHÔNG** được phép sáng tác LUẬN ĐIỂM kinh tế mới.
- [ ] Mọi **LUẬN ĐIỂM** (thesis, counter-argument, góc nhìn) phải lấy từ `chapter_briefs.md`. Nếu brief thiếu luận điểm → DỪNG LẠI.
- [ ] Mọi **DỮ LIỆU BỔ SUNG** (số liệu, case study, cơ chế) từ `research_vault/` để làm DÀY luận điểm đã chốt → ĐƯỢC PHÉP và khuyến khích (đánh dấu `[BỔ SUNG TỪ VAULT]`).

**Tự kiểm tra:** Nếu tôi đang nghĩ "mình sẽ thêm LUẬN ĐIỂM MỚI vì nó hay" → **DỪNG LẠI. Đó là lỗi vai trò.** Nhưng nếu tôi thêm DỮ LIỆU từ vault để làm rõ luận điểm đã chốt → đó là Vault Mining, ĐƯỢC PHÉP.

---

## GATE 2 — Kiểm tra tài liệu đầu vào (Input Verification)

Trước khi viết, xác nhận ĐÃ ĐỌC (không được giả định đã nhớ):

| File | Đã đọc? | Thông tin cốt lõi rút ra |
|---|---|---|
| `chapter_briefs.md` — brief của chapter đang viết | ☐ | (ghi tóm tắt luận điểm chính) |
| `07_outline.md` — vai trò của chapter này trong tổng thể | ☐ | (Chapter này phải đưa khán giả từ A → B) |
| `05_continuity_packet.md` — ý nào đã dùng ở chương trước | ☐ | (Tránh lặp lại) |

**Nếu bất kỳ file nào chưa đọc → DỪNG LẠI. Đọc xong mới được tiếp tục.**

---

## GATE 2B — Xác nhận Dual-Layer Data đã nạp

Tự xác nhận:
- [ ] Gate 0 đã hoàn thành (cả Bước 0.1 + 0.2)
- [ ] Mọi con số tôi sẽ dùng đến từ vault files. Nếu không chắc → tra lại file gốc.
- [ ] Vault Mining: nếu vault có insight liên quan mà brief chưa đề cập → sẽ bổ sung (đánh dấu `[BỔ SUNG TỪ VAULT]`).

**Nếu Gate 0 chưa chạy → DỪNG LẠI. Không có ngoại lệ.**

---

## GATE 2C — ⛔ TIÊU HÓA KIẾN THỨC (Knowledge Digestion — CHỐNG ĐỨT GÃY NGHIÊN CỨU ↔ VIẾT)

> **ĐÂY LÀ GATE CHỐNG ĐỨT GÃY.** Gate 2B buộc đọc. Gate 2C buộc CHỨNG MINH ĐÃ HIỂU.

**BẮT BUỘC:** Đọc và thực thi đầy đủ 4 bài kiểm tra trong file:
`[Absolute Path: /Users/pro16/Documents/VideoProject/KenhTamLy/.agents/skills/chapter_writer/KNOWLEDGE_DIGESTION_GATE.md]`

Kết quả PHẢI GHI RA (in ra response hoặc ghi vào scratch file). Hoàn thành cả 4 bài mới được qua Gate 3. Không có ngoại lệ.

---

## GATE 2D — ⛔ HỘ CHIẾU DỮ LIỆU (Data Passport — CHỐNG BỊA SỐ LIỆU)

> **ĐÂY LÀ CƠ CHẾ CẤU TRÚC.** Gate 2B buộc đọc. Gate 2C buộc hiểu. Gate 2D buộc TRÍCH XUẤT BẰNG CHỨNG.
> Không dựa trên danh dự. Mọi con số phải để lại dấu vết kiểm chứng được.

### Quy trình bắt buộc:

1. **Tạo file `data_passport_chXX.md`** trong episode folder (format: `00_core/data_passport_template.md`)

2. **Liệt kê TỪNG con số** sẽ dùng trong chapter vào bảng passport, bao gồm:
   - Giá trị chính xác
   - File nguồn (đường dẫn trong `episodes/[slug]/`)
   - **Dòng số (LineNumber)** — lấy từ output của `view_file`
   - Trích nguyên văn câu chứa con số đó trong file nguồn

3. **Nếu con số đến từ `search_web`:** Ghi URL nguồn + ngày truy cập thay vì file + dòng

4. **Nếu KHÔNG TÌM THẤY nguồn cho một con số:** Ghi vào mục "Cần bổ sung" → HỎI USER → NGHIÊM CẤM tự bịa

5. **Số liệu tính toán (derived):** Ghi rõ phép tính + mã passport gốc (VD: DP-C1 = DP-01 / DP-02)

### Checklist trước khi qua Gate 3:

| Câu hỏi | Đạt? |
|---|---|
| File `data_passport_chXX.md` đã tạo trong episode folder? | ☐ |
| Mọi con số trong passport có nguồn (file + dòng HOẶC URL)? | ☐ |
| Không có mục nào trong "Cần bổ sung" chưa giải quyết? | ☐ |
| Trích nguyên văn đã kiểm tra khớp với file gốc? | ☐ |

**Nếu bất kỳ câu nào chưa tick → NGHIÊM CẤM viết. Không có ngoại lệ.**

> **Tại sao Gate này tồn tại:** Ngày 10/05/2026, agent đã vi phạm Gate 2B (giả vờ đã đọc tài liệu), dẫn đến bịa 4 con số sai trong 1 chapter duy nhất (PVN 30% NSNN, VinFast 50 quốc gia, VCB 12x, EVN gấp 3). Gate 2D buộc agent để lại bằng chứng vật lý (file + dòng số) — không đọc thì không có dòng số, không có dòng số thì không viết được.

---

## GATE 3 — ⛔ TOÀN CẢNH VIDEO (Panoramic View — CHỐNG TRÙNG LẶP TỪ GỐC)

> **Tại sao Gate này tồn tại:** Ngày 22/05/2026, toàn bộ 7 chương của episode samsung-viet-nam bị phát hiện trùng lặp nghiêm trọng: con số 316 triệu USD xuất hiện ở 3 chương, dự án 1.2 tỷ USD Thái Nguyên xuất hiện ở 3 chương, cơ chế Quỹ ISF được giải thích chi tiết ở 2 chương. Nguyên nhân gốc rễ: agent viết từng chương trong trạng thái "ngăn xếp" — chỉ nhìn thấy brief của chương mình, không đọc bản văn thực tế đã viết ở các chương trước. Kết quả: mỗi chương tối ưu hóa cục bộ, kéo cùng một bộ dữ liệu mạnh nhất vào để "tự đứng vững", gây ra lặp ý hệ thống.

> **Nguyên tắc:** Một biên kịch thực thụ không bao giờ viết chương 6 của cuốn sách mà không đọc lại 5 chương trước. Agent cũng vậy.

### Bước 3.1 — ĐỌC TẤT CẢ CHƯƠNG ĐÃ VIẾT

**BẮT BUỘC** dùng tool `view_file` đọc **TOÀN BỘ** nội dung các file `chapter_XX.md` đã tồn tại trong `episodes/[slug]/`, từ `chapter_01.md` đến chương ngay trước chương đang viết.

- Nếu đang viết Chương 1 → bỏ qua bước này (chưa có chương nào trước đó).
- Nếu đang viết Chương 4 → đọc `chapter_01.md`, `chapter_02.md`, `chapter_03.md`.
- **KHÔNG được giả định đã nhớ.** PHẢI đọc lại bằng tool, mỗi lần viết.

### Bước 3.2 — VIẾT BẢN TỔNG HỢP "TOÀN CẢNH VIDEO"

Sau khi đọc xong, BẮT BUỘC viết ra (in ra response) bản tổng hợp theo format sau:

```
📡 TOÀN CẢNH VIDEO — Trước khi viết Chương [số]

1. MỤC ĐÍCH CỐT LÕI CỦA VIDEO:
   (Một câu duy nhất: video này muốn khán giả hiểu điều gì khi xem xong?)

2. HÀNH TRÌNH ĐÃ ĐI QUA:
   - Ch1: [Tóm tắt 1-2 câu — ý chính, dữ liệu cốt lõi đã trình bày]
   - Ch2: [...]
   - Ch3: [...]
   (Liệt kê tất cả chương đã đọc)

3. DỮ LIỆU/SỐ LIỆU ĐÃ TRÌNH BÀY CHI TIẾT:
   (Liệt kê mọi con số, quyết định chính sách, case study đã được giải thích
    kỹ ở các chương trước. VD: "316 triệu USD — đã giải thích chi tiết ở Ch4")

4. KHÁN GIẢ ĐANG Ở ĐÂU:
   (Sau khi xem hết các chương trước, khán giả hiểu gì, cảm thấy gì,
    đang chờ đợi điều gì?)

5. CHƯƠNG NÀY PHẢI ĐÓNG GÓP GÌ MỚI:
   (Insight mới nào? Dữ liệu mới nào? Góc nhìn mới nào?
    Nếu không trả lời được → chương này đang thừa.)

6. ĐIỀU CHƯƠNG NÀY KHÔNG ĐƯỢC LÀM:
   (Dựa trên mục 3 — liệt kê những dữ liệu/khái niệm đã được trình bày
    chi tiết ở chương trước mà chương này chỉ được nhắc lướt hoặc không nhắc.)
```

### Quy tắc cứng

- **KHÔNG viết được bản Toàn Cảnh → KHÔNG được viết chương.** Không có ngoại lệ.
- Mục 6 ("Điều chương này không được làm") là cơ chế chống trùng lặp tự nhiên: agent tự nhận ra ranh giới vì đã ĐỌC bản văn thực tế, không phải vì bị cấm bằng quy tắc cứng.
- Nếu một dữ liệu đã được trình bày chi tiết ở chương trước nhưng chương hiện tại cần nhắc để giữ mạch: **chỉ được nhắc khái niệm trong 1 câu ngắn**, không lặp lại số liệu cụ thể hoặc giải thích lại cơ chế.

---

## GATE 4 — Kiểm tra cấu trúc cảm xúc (Emotional Arc Check)

Trước khi gõ câu đầu tiên, tự hỏi:

- **Pain-first:** Câu mở chapter này có bắt đầu từ nỗi đau / cú lệch của người xem không? Hay bắt đầu bằng luận đề trừu tượng?
- **Personal Stakes (PHỔ QUÁT):** Chapter 2 — tự nhiên và trực tiếp. Tuyệt đối KHÔNG được đóng khung máy móc hay ép đưa stakes cá nhân vào nếu không liên quan. Đi thẳng vào cốt lõi logic của chủ đề và liên kết bằng sự chuyển động của dữ liệu. Tránh gò bó sáng tạo.
- **Re-hook:** Nếu là chapter 3-4 — đã có data shock mới hoặc câu kéo về áp lực đời sống phổ quát trong 3 phút đầu của chapter chưa?

---

## GATE 4B — Kiểm tra Brand Safety & High CPM (Corporate-Grade Aggression)

Trước khi viết, bạn BẮT BUỘC phải áp dụng nguyên tắc từ `00_core/brand_safety_guidelines.md`.
Tự hỏi:
- Tôi có đang dùng từ bạo lực, thảm kịch (tàn bạo, khốc liệt, đẫm máu, sụp đổ) không?
- Nếu có, PHẢI chuyển sang ngôn ngữ Business/Finance (thần tốc, bứt phá, thách thức, tái cấu trúc, rủi ro tập trung) để tối ưu hóa CPM và tránh cờ vàng (Limited Ads).
- Giọng văn phải là Cold Analysis (phân tích lạnh lùng, chuyên nghiệp), KHÔNG PHẢI Anger (kích động, mạt sát cảm tính).

---

## GATE 5 — Nhắc nhở nhanh trước khi viết (Quick Reminder)

> **Lưu ý:** Scan chi tiết sẽ do **Quality Czar** thực hiện ở Bước 3 (POST-WRITE). Gate này chỉ nhắc nhở nhanh các lỗi phổ biến nhất để tránh mất công viết lại.

Tự nhắc:
- Không dùng dấu `—` (TTS đọc sai)
- Không tự thêm luận điểm kinh tế ngoài brief
- Không dùng template transition ("Đây là chỗ...", "Nhưng đó mới chỉ là bề mặt")
- Ngày tháng phải cụ thể (không "gần nhất", "vừa qua")

---

## GATE 6 — Tuyên bố sẵn sàng (Readiness Declaration)

Chỉ được bắt đầu viết khi agent có thể điền đầy đủ vào câu sau:

> "Tôi là **The Narrative Director**. Tôi sắp viết **Chapter [số]** của episode **[slug]**. Chapter này có nhiệm vụ đưa khán giả từ **[trạng thái nhận thức A]** sang **[trạng thái nhận thức B]**. Tôi đã hoàn thành bảo chứng trích lục tại Gate 0 với tệp **[Tên file vault]** dòng **[LXX-LXX]**. Tôi sẽ chỉ dùng nguyên liệu từ brief, không thêm luận điểm mới. Câu đầu tiên sẽ mở bằng **[pain/cú lệch cụ thể]**, không phải luận đề."

Nếu không điền được → **KHÔNG ĐƯỢC VIẾT.**

---

## Lưu ý cho Agent

> Mỗi lần vi phạm Gate này là MỘT LẦN phải viết lại toàn bộ từ đầu. Viết lại = tốn token gấp đôi + phá vỡ continuity toàn episode. Chi phí của việc NGHĨ KỸ TRƯỚC là 0. Chi phí của việc VIẾT SAI là rất cao.
