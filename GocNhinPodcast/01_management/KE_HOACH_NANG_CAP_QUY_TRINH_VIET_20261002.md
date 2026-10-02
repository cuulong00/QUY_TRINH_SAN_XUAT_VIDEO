# Kế hoạch nâng cấp quy trình viết kịch bản (02/10/2026)

Phạm vi: DNA, rule, skill và workflow viết kịch bản của GocNhinPodcast (Pha 1–11). Phần I2V (Pha 12) chỉ gồm giao thức khung mở đầu.
Đầu vào:
- Soát file `.agents/` và `00_core/`.
- Lỗi thật của tập gsm-chau-au (`01_management/kg_research/SO_VAN_DE_GSM_CHAU_AU.md`).
- Nghiên cứu cộng đồng nhà sáng tạo về hook và Ch.1.

Kế hoạch này mới liệt kê việc cần làm, chưa sửa file nào. Mỗi bước sửa xong dừng lại cho user duyệt.

---

## Phần 1. Phát hiện: tám bản chất, mỗi bản chất có bằng chứng

### R1. Một luật nằm ở nhiều nơi và các nơi nói khác nhau
DNA nói có "nguồn sự thật duy nhất", nhưng cùng một luật lặp ở 3–5 file với nội dung lệch nhau. Agent gặp bản nào thì làm theo bản đó.

| Luật | Chỗ nói A | Chỗ nói B |
|---|---|---|
| Số case study quốc tế cho bài Loại B | `build_outline.md:123` "đúng 1" | `content_principles.md §5`, `longform_blueprint §3`, `chapter_writer` "tối đa 2" |
| Ch.2 với bài Loại B | `rules/chapter-writing.md` "BẮT BUỘC nối vĩ mô → đời sống người dân" | `content_principles §2`, `longform_blueprint §3`: cấm ép đời sống vào bài B |
| Chương kết | `longform_blueprint §3`: "đóng toàn bộ open loops", "action framework" | `chapter_writer` chương kết: "không giải quyết hoàn toàn, giữ tension"; bài B: cấm lời khuyên kiểu 3 bước |
| Độ dài chương | `longform_blueprint §11`: tối đa khoảng 2,5 phút | `build_outline`: trần 1.050 từ (khoảng 4,7 phút) |
| Độ dài câu | `longform_blueprint §12`: 8–15 từ | `chapter_writer`, `masterpiece`: dưới 150 ký tự (20–25 từ) |
| Gợi hình | `masterpiece §5.1`, `chapter_quality 2.3`: "ngôn từ có màu sắc, ánh sáng, chất liệu" | `chapter_writer` mục 7: "cấm tả cảnh, không khí, cảm giác vật lý" |
| Đọc lại các chương trước | `AGENTS.md` Pha 7, `chapter_writer`: đọc toàn bộ | `rules/chapter-writing.md`: không mặc định đọc lại nếu NST đã đủ |
| Lập trường trong hook | `golden_samples/golden_hook.md #3`: "hook phải có lập trường rõ" | `stance_and_judgment §8`: Ch.1 chưa kết luận |

### R2. DNA nghiêng về bài Loại A và về khung tài chính
- `golden_samples/golden_hook.md #5` buộc mọi hook "gắn túi tiền / đời sống cá nhân", dù bài B đã cấm điều này.
- `longform_blueprint §2` (Personal-First): "Loại A **và B**: không quá 4 phút mà không kéo về đời sống cá nhân". Câu kiểm cuối §15 hỏi bài A/B đã "nói về CHÍNH HỌ" chưa.
- Hội đồng phản biện 3 lăng kính (`AGENTS.md`, `content-os-pipeline.md`) bắt buộc lăng kính "Forensic Cash Auditor" (FCF âm, điểm hòa vốn) cho **mọi** Devil's chapter.
- Hook engine có hẳn biến thể 2 "Va chạm bảng cân đối".
- Cụm "BCTC / điểm hòa vốn / dòng tiền" xuất hiện như tiêu chí chấm ở 18 file (masterpiece 2.1, chapter_quality 2.2, retention Gate 2 Loại B…).
- Hậu quả trong tập GSM: Pha 1 bị kéo về khung "canh bạc đốt tiền"; Pha 3 còn "điểm hòa vốn"; Pha 4 còn "bảng cân đối kế toán" (sổ vấn đề V15).

### R3. Ví dụ trong DNA dính đề tài thật và chưa được kiểm
- `stance_and_judgment.md` dùng chính đề GSM làm ví dụ.
  - "Mỗi ngày lãi vay tập đoàn 113 tỷ": không có trong kho, và cùng kiểu so sánh lệch phạm vi mà agent mắc ở Pha 1 ("80 tỷ/ngày").
  - "SEC gọi đội taxi là phòng lái thử di động": nói quá so với nguồn.
- Ví dụ kết bài còn dùng "bảng cân đối Vingroup trả tiền bao lâu", tức lại là khung tài chính.
- `hook_engine/examples/golden_hook.md`, `chapter_writer/examples/golden_chapter.md` vẫn là placeholder chưa từng được điền.
- Hậu quả: agent học theo cả khung lẫn con số của ví dụ (V29).

### R4. Cổng chất lượng đo hình thức, và người viết tự chấm mình
- Thang 100 điểm (MSB) và 50 điểm (CHQB) do chính agent viết tự chấm. Danh sách 14 tiêu chí tự kiểm nằm "trong khối thinking ngầm", không ai thấy được.
- Hard-fail cấp kịch bản (masterpiece §4) không có lỗi "bịa chi tiết" hay "suy luận viết như dữ kiện". Đây lại là lỗi gặp nhiều nhất trong tập GSM (V12, V13, V16, V22, V23).
- Mẫu báo cáo chương (`chapter_quality_standard §6`) chỉ liệt kê 5 cổng, **bỏ mất Gate 0 (ZUI)**, dù phần thân văn bản nói có 6 cổng.
- `kbaudit --check-plan` chỉ kiểm cú pháp tham chiếu GAP (V08). Agent báo "đã sửa", "đã đọc" khi chưa làm (V07, V14).

### R5. Template ép viết câu nén, làm rơi nhãn suy luận
- Outline có 12 ô bắt buộc cho mỗi chương (Key Insight, Causal Exit, Physical Anchor, Grand Payoff…).
- Các ô "câu tóm đắt" buộc agent nén ý, và nhãn suy luận rơi đúng ở đó (V22).
- Ô "mỏ neo vật lý" đẩy agent tự bịa chi tiết cảnh (V23).

### R6. Thiếu hai mắt xích nối các pha
- **Hiến chương tập:** chỉ đạo của user chỉ nằm trong tin nhắn. Không có file khóa tiêu đề, câu hỏi trung tâm, các điều cấm, nên agent trôi đề ở Pha 1 và Pha 3 (V15).
- **Sổ dữ kiện xuyên tập:**
  - Claim ledger tới Pha 10 mới có.
  - Mỗi pha chỉ đọc pha liền trước, nên dữ kiện của Pha 1 rơi mất ở Pha 3 (V11).
  - Chapter writer chỉ đọc vault, không đọc kho.

### R7. Hook và Ch.1 thiếu chuẩn 30 giây đầu
- Không có chuẩn nối thumbnail với câu đầu.
- Không có cấu trúc 0–30 giây.
- Không có quy tắc "mở, đóng, mở" (trả phần thưởng nhỏ, giữ câu hỏi lớn).
- Hook Lab và skill lệch số: 7 góc/10 câu/top 3 so với 3 biến thể.
- Luồng hình ảnh không có giao thức khung mở đầu. I2V+ còn ghi ngược với nghiên cứu: "Hook ưu tiên VEO_AI lắng đọng".

### R8. Quá dài và quá nhiều mệnh lệnh
- Khoảng 8.700 dòng trong `.agents/` (không tính tools) cộng 4.800 dòng `00_core/`.
- Gần như mọi đoạn đều có "BẮT BUỘC / TUYỆT ĐỐI / CẤM", nên agent không phân biệt được luật nào quan trọng hơn.
- Agent có giới hạn đọc file, thường chỉ đọc phần đầu (V06, V07).
- Có các khẳng định gắn theo model đã lỗi thời ("Gemini 3.8 Flash, 1 triệu token", 8 chỗ).

---

## Phần 2. Nguyên tắc khi sửa
1. **Mỗi luật một nơi.** Các file khác chỉ trỏ tới, không chép lại. Sửa bằng cách xóa bản trùng, không thêm bản mới.
2. **Gỡ trước, thêm sau.** Phần lớn lỗi là do luật thừa hoặc mâu thuẫn, không phải do thiếu luật.
3. **Cổng kiểm phải chạy được bằng máy hoặc do người khác chấm.** Không dùng tự chấm, không chấm "trong suy nghĩ".
4. **Ví dụ trung tính về đề tài**, hoặc có mã nguồn đã kiểm.
5. **Mỗi bước sửa được đo** bằng cách chạy lại trên một tập thật, trước và sau. Không đánh giá theo cảm nhận.
6. **Dong_Chay:** chuyển theo nghĩa, giữ luật riêng của kênh. Không chép nguyên văn.

---

## Phần 3. Các bước sửa (theo thứ tự, mỗi bước một gate)

| Bước | Nội dung | Khắc phục | File chính | Cách kiểm đạt |
|---|---|---|---|---|
| **B0** | Lập bảng đủ mọi luật trùng và mâu thuẫn; user chốt từng mâu thuẫn (ví dụ: bài B dùng 1 hay 2 case; chương kết đóng loop hay giữ tension) | R1 | (bảng mới, chưa sửa DNA) | User chốt hết các dòng |
| **B1** | Gom về một nơi: hằng số, luật viết theo loại A/B/C, luật Ch.1/Ch.2/chương kết. Các file khác chỉ trỏ tới | R1 | `AGENTS.md`, `content_principles`, `longform_blueprint`, `rules/chapter-writing`, `chapter_writer`, `build_outline`, `retention_gate` | Quét lại: 0 mâu thuẫn |
| **B2** | Gỡ thiên lệch Loại A và tài chính: Personal-First chỉ cho A; lăng kính dòng tiền thành tùy chọn theo đề; bỏ BCTC/điểm hòa vốn khỏi tiêu chí chấm chung; thay biến thể hook "bảng cân đối" | R2 | `golden_hook`, `longform_blueprint §2/§15`, Hội đồng phản biện, `hook_engine`, rubric | Chạy lại Pha 1 trên một đề B: không trôi về khung lỗ lãi |
| **B3** | Làm sạch ví dụ: thay ví dụ GSM trong `stance_and_judgment` bằng ví dụ trung tính; điền hoặc xóa các file placeholder | R3 | `stance_and_judgment`, `examples/*` | 0 số không nguồn trong ví dụ |
| **B4** | Thêm **hiến chương tập** (khóa đề bài, chỉ đạo user, điều đã loại) và **sổ dữ kiện xuyên tập** (mắt xích kèm nhãn, dùng từ Pha 1 tới Pha 10) | R6 | template mới, workflow Pha 1–7 | Chạy thử: Pha 3 giữ đủ chân đỡ của Pha 1 |
| **B5** | Hook, Ch.1 và khung mở đầu: nối thumbnail, cấu trúc 0–30 giây, mở-đóng-mở, re-hook; thống nhất Hook Lab với skill; thêm giao thức khung mở đầu cho I2V/I2V+ | R7 | `hook_engine`, `hook_lab`, `golden_hook`, `visual_prompter(_plus)` | Hook tập GSM qua phép thử tắt tiếng + đặt cạnh thumbnail |
| **B6** | Template outline và brief: bỏ các ô câu tóm bắt nén; câu tóm phải trỏ mã mắt xích; "mỏ neo" phải có nguồn hoặc nhãn minh họa | R5 | `07_outline_template`, `08_chapter_briefs_template`, `script_architect` | Outline mới: 0 nhãn suy luận bị rơi |
| **B7** | Cổng chấm: tách người viết và người chấm; thêm máy kiểm (mã OBS khớp câu, số có nguồn, câu so sánh nhất, nhãn suy luận, đọc đủ file); rút gọn rubric; thêm hard-fail "bịa / suy luận như dữ kiện"; sửa mẫu báo cáo thiếu Gate 0 | R4 | `masterpiece`, `chapter_quality`, `compliance_council`, script kiểm mới | Chạy trên outline GSM: bắt lại đúng các lỗi tôi đã bắt tay |
| **B8** | Rút gọn và đổi giọng: bỏ mệnh lệnh thừa, bỏ khẳng định gắn theo model, tách phần "nguyên tắc" với phần "thủ tục" | R8 | toàn bộ | Tổng dung lượng giảm rõ; agent đọc hết trong một lượt |
| **B9** | Chuyển sang Dong_Chay theo nghĩa; kiểm trên 2 đề khác loại | tất cả | Dong_Chay `.agents/` | Hai tập thử đạt cổng mới |

---

## Phần 4. Đề xuất cách chạy cùng tập GSM đang làm
- Tập GSM vẫn đi tiếp với DNA hiện tại, vì nó là lượt thử sinh ra bài học. Mọi lỗi mới tiếp tục ghi vào sổ vấn đề.
- Những lỗi đang làm sai tập ngay bây giờ (khung tài chính, chuẩn hook/Ch.1, nhãn suy luận) thì tôi đưa vào phiếu giao việc của từng pha, không chờ sửa DNA.
- Sửa DNA bắt đầu từ B0 ngay khi user duyệt kế hoạch. B0–B3 không ảnh hưởng tập đang chạy. B4–B7 áp dụng từ tập sau, hoặc từ pha kế tiếp nếu user muốn.
- Kế hoạch bộ nhớ (kho, kbq, chỉ mục) chạy song song và nối với B4 (sổ dữ kiện xuyên tập).
