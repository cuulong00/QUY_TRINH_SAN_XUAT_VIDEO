# ⛔ PRE-FLIGHT THINKING GATE — Bắt Buộc Trước Khi Viết Bất Kỳ Chapter Nào

> **LỆnh cứng:** Nếu agent chưa trả lời đầy đủ TẤT CẢ câu hỏi trong Gate này — **NGHIÊM CẤM gõ một chữ nào vào chapter**. Vi phạm gate này là nguyên nhân số 1 dẫn đến việc phải viết lại từ đầu, tốn token vô ích.

---

## GATE 0 — ⛔ MANDATORY EXPERT PERSONA ACTIVATION (Khởi Động Căn Cước Chuyên Gia Thống Trị)

Trước khi viết bất kỳ chữ nào, Agent tự khóa vai trong khối suy luận ngầm (Thinking Process):
- [ ] **Chuyên gia Thống trị (Dominant Persona):** Đã xác định rõ ai đang tư duy chương này (`The Policy Analyst`, `The Macro Economist`, `The Critical Auditor`, `The Industrial Controller`, `The Corporate Finance Analyst`...)? Đã đọc file Persona tương ứng chưa?
- [ ] **Tiêu chuẩn Chân lý Ngành:** Chuyên gia này đánh giá sự việc bằng thước đo khoa học nào (BOM, Khấu hao, Điểm hòa vốn, Rào cản thể chế, Cấu trúc động lực lợi ích, Bảng cân đối kế toán)?
- [ ] **Bộ lọc Chống Ngây Thơ (Anti-Amateur & Anti-Strawman):** Tuyệt đối CẤM đưa ra các tiền đề ngô nghê của dân ngoại đạo (ví dụ: *tưởng chở xe tải nhanh và rẻ hơn tàu biển, rút lui vì sợ hãi thay vì điểm hòa vốn, hay nhầm lẫn giữa hủy hợp đồng và tạm hoãn dự án bồi hoàn chi phí chìm*). Bắt buộc phải phản biện phiên bản mạnh nhất, logic nhất của đối thủ (Steel-manning).

---

## GATE 0B — ⛔ TARGETED VAULT RECALL (BẢO CHỨNG TRÍCH LỤC VAULT & GVS)

Thực hiện đầy đủ quy trình Dual-Layer Data trong `chapter_writer/SKILL.md` §Kiến Trúc Dual-Layer:
- **Bước 0.1:** Nạp Tầm Nhìn Vĩ Mô & Mỏ Neo Số Liệu Toàn Cảnh từ `01_global_vision_synthesis.md` và cẩm nang phong cách chuyên biệt.
- **Bước 0.2:** Nạp Dữ Liệu Vi Mô cho CHƯƠNG ĐANG VIẾT (vault files theo trường 11 hoặc mã `DATA-01` đến `DATA-XX` trong GVS Tầng 4).

**BẮT BUỘC BẢO CHỨNG TRÍCH LỤC:** 
Agent phải trích dẫn nguyên văn ít nhất 1-2 câu quan trọng chứa dữ liệu thực tế từ file vault hoặc GVS đã mở đọc cho chương này, ghi rõ:
1. Tên file vault hoặc mã GVS (`01_global_vision_synthesis.md` hoặc `research_vault/xxx.md`)
2. Số dòng bắt đầu và kết thúc (`LXX-LXX`) hoặc Mã số liệu (`DATA-XX`)
3. Nội dung nguyên văn (Raw quote)

Tự kiểm tra:
- [ ] Đã đọc `01_global_vision_synthesis.md` (Bước 0.1)
- [ ] Đã đọc vault files cho chương này theo trường 11 (Bước 0.2)
- [ ] Đã ghi ra BẢO CHỨNG TRÍCH LỤC nguyên văn + số dòng/mã DATA ở trên
- [ ] Hiểu rõ chương này nằm ở đâu trong arc tổng thể
- [ ] Mọi con số sẽ dùng đã có trong GVS / vault files vừa đọc

**Nếu bất kỳ checkbox nào chưa tick hoặc thiếu Bảo chứng trích lục nguyên văn -> NGHIÊM CẤM viết.**

---

## GATE 1 — Kiểm tra vai trò (Role Clarity & Mandatory Pairing)

**Câu hỏi bắt buộc tự trả lời:**
- [ ] Tôi đang vận hành theo **Kiến trúc Ghép cặp Bắt buộc**: Chuyên gia Thống trị (**Dominant Persona: [Tên Persona]**) chỉ huy Khung xương cơ chế (Mechanism Wireframe), và **Narrative Director & Voice Architect** thực thi Da thịt thính giác cho đôi tai nghe.
- [ ] Mọi **CƠ CHẾ KINH TẾ/PHÁP LÝ/VẬN HÀNH** phải tuân thủ chuẩn mực chân lý của Chuyên gia Thống trị và dữ liệu thực chứng từ `research_vault/` / `02_research_map.md`.
- [ ] Tôi **TUYỆT ĐỐI KHÔNG** dùng ngụy biện bù nhìn rơm (Strawman), không bịa ra tiền đề ngô nghê của dân ngoại đạo. Tôi phản biện phiên bản mạnh nhất của đối thủ (Steel-manning).
- [ ] Mọi **LUẬN ĐIỂM** cốt lõi phải bám sát `chapter_briefs.md`. Nếu phát hiện lỗ hổng cơ chế → DÙNG CHUYÊN GIA để củng cố bằng Vault Mining, không sáng tác bừa bãi.
- [ ] Mọi **DỮ LIỆU BỔ SUNG** (manh mối, vật chứng, case study, cơ chế) từ `research_vault/` làm sáng một nhịp chuyện đã chốt → ĐƯỢC PHÉP và khuyến khích (đánh dấu `[BỔ SUNG TỪ VAULT]`). Số liệu thêm chỉ để làm dày chương thì KHÔNG thêm.

**Tự kiểm tra:** Nếu tôi đang nghĩ "mình sẽ thêm LUẬN ĐIỂM MỚI vì nó hay" → **DỪNG LẠI. Đó là lỗi vai trò.** Nhưng nếu Chuyên gia đào sâu DỮ LIỆU và CƠ CHẾ từ vault để làm rõ luận điểm đã chốt → đó là Vault Mining, ĐƯỢC PHÉP.

---

## GATE 2 — Kiểm tra tài liệu đầu vào (Input Verification)

Trước khi viết, xác nhận ĐÃ ĐỌC (không được giả định đã nhớ):

| File | Đã đọc? | Thông tin cốt lõi rút ra |
|---|---|---|
| `chapter_briefs.md` — brief của chapter đang viết | ☐ | (ghi tóm tắt luận điểm chính) |
| `07_outline.md` — vai trò của cha---

## GATE 2C — ⛔ TIÊU HÓA KIẾN THỨC (Knowledge Digestion — CHỐNG ĐỨT GÃY)

> **Rút gọn thủ tục:** Không bắt buộc viết 4 bài test cồng kềnh ra file phụ hay phản hồi dài dòng. Thay vào đó, Agent chỉ cần thực hiện **suy nghĩ nội bộ (internal reasoning)** trước khi gõ phím để trả lời 2 câu hỏi bản chất:
> 1. Nghịch lý cốt lõi của chương này là gì?
> 2. Nếu một chuyên gia đọc chương này, họ sẽ phản bác điểm nào và tôi xử lý ra sao?
>
> *(Ghi nhận câu trả lời ngắn gọn trong phần Thinking).*

---

## GATE 2D — ⛔ HỘ CHIẾU DỮ LIỆU (Data Passport — CHỐNG BỊA SỐ LIỆU)

> **Rút gọn thủ tục:** TUYỆT ĐỐI KHÔNG tạo thêm các file phụ `data_passport_chXX.md` cho từng chương, và CẤM chèn bất kỳ bảng đối chiếu nào vào cuối tệp kịch bản chính `chapter_XX.md`.
>
> **Quy trình tối giản:** 
> - Đối chiếu trực tiếp mọi con số dự định viết với file `02_research_map.md` đã được kiểm chứng của tập.
> - Lưu lại dấu vết kiểm chứng (Mã passport hoặc Vault Ref của số liệu được dùng) trực tiếp trong phần suy nghĩ ngầm (Thinking) của bạn trước khi gõ phím. Nếu phát hiện thiếu nguồn cho số liệu mới, phải dừng lại hỏi ý kiến người dùng hoặc loại bỏ số liệu đó, tuyệt đối không tự bịa số liệu.

---

## GATE 3 — ⛔ TOÀN CẢNH VIDEO (Panoramic View — CHỐNG TRÙNG LẶP)

> **Rút gọn thủ tục:** Không cần viết bản panoramic view 6 phần dài dòng. Trước khi viết chương mới, Agent bắt buộc phải dùng `view_file` đọc lại các chương đã viết trước đó và tự trả lời nhanh trong phần suy nghĩ ngầm (Thinking) 3 câu hỏi cốt lõi:
> 1. Ý chính của chương trước là gì?
> 2. Chương này mang lại giá trị/insight gì MỚI?
> 3. Dữ liệu nào chương trước đã nói mà chương này KHÔNG ĐƯỢC lặp lại?



## GATE 4 — Kiểm tra cấu trúc cảm xúc (Emotional Arc Check)

Trước khi gõ câu đầu tiên, tự hỏi:

- **Pain-first:** Câu mở chapter này có bắt đầu từ một cú lệch cụ thể (Loại A: nỗi đau của người xem; Loại B/C: nghịch lý, con số gây bất ngờ) không? Hay bắt đầu bằng luận đề trừu tượng?
- **Điểm tựa liên quan (theo loại đề tài, `00_core/content_principles.md` §3):** Chapter 2 đặc biệt. Loại A: đã nối vấn đề vĩ mô với đời sống chung của xã hội/người dân bằng lăng kính PHỔ QUÁT ("Chúng ta", "Xã hội hiện đại", "Tầng lớp lao động") chưa? Loại B: đã nối vào bài toán chi phí, quản trị, chuỗi giá trị chưa? Loại C: đã nối vào quy luật lớn, nghịch lý lịch sử chưa, không ép túi tiền? **NGHIÊM CẤM** Zoom-In cá nhân hóa cực đoan (VD: "Anh Minh 35 tuổi...").
- **Re-hook:** Nếu là chapter 3-4 — đã có data shock mới hoặc câu kéo về điểm tựa đúng loại đề tài để giữ hướng tự sự (khung chấm I, III, VIII) chưa?

---

## GATE 4B — Kiểm tra Brand Safety & High CPM (Corporate-Grade Aggression)

Trước khi viết, bạn BẮT BUỘC phải áp dụng nguyên tắc từ `00_core/brand_safety_guidelines.md`.
Tự hỏi:
- Tôi có đang dùng từ bạo lực, thảm kịch (tàn bạo, khốc liệt, đẫm máu, sụp đổ) không?
- Nếu có, PHẢI chuyển sang ngôn ngữ Business/Finance (thần tốc, bứt phá, thách thức, tái cấu trúc, rủi ro tập trung) để tối ưu hóa CPM và tránh cờ vàng (Limited Ads).
- Giọng văn phải là phân tích điềm tĩnh, có nghề, có người đang nghĩ, không phải giận dữ (kích động, mạt sát cảm tính).

---

## GATE 4C — ⛔ KIỂM TRA CHẤT LƯỢNG NỐI CHƯƠNG (Transition Quality Check — CHỐNG DEAD TRANSITION)

> **Tại sao Gate này tồn tại:** Episode LPBank (23/06/2026), toàn bộ 6 chương bị phát hiện nối chương bằng tường thuật phẳng, câu hỏi tu từ mềm, và spoil đáp án. Khán giả không có lý do cảm xúc để ở lại giữa các chương. Đây là lỗi CẤU TRÚC, không phải lỗi ngôn ngữ.

### Kiểm tra KẾT CHƯƠNG (áp dụng cho mọi chương trừ chương cuối):

| Câu hỏi | Đạt? |
|---|---|
| Có VALUE CLOSE rõ ràng? (Khán giả biết chương vừa rồi cho họ insight gì cụ thể?) | ☐ |
| Có OPEN LOOP? (Chi tiết cụ thể: con số/nhân vật/sự kiện gây tò mò, CHƯA giải đáp?) | ☐ |
| Open loop có ĐỦ CỤ THỂ? (Không phải câu hỏi tu từ chung chung kiểu "Vậy điều gì sẽ xảy ra?") | ☐ |
| Có SPOIL đáp án cho chương sau không? (Nếu có → viết lại) | ☐ |
| Có dùng lời khuyên/giáo huấn để kết ở giữa bài không? (Nếu có → viết lại) | ☐ |
| **BUT/THEREFORE TEST:** Chèn "NHƯNG" hoặc "DO ĐÓ" giữa kết chương này và mở chương sau. Nếu chỉ chèn được "VÀ SAU ĐÓ" → mối nối yếu, viết lại. | ☐ |

### Kiểm tra MỞ CHƯƠNG (áp dụng cho mọi chương trừ chương đầu):

| Câu hỏi | Đạt? |
|---|---|
| Có ANSWER HOOK từ chương trước trong 1-3 câu đầu? | ☐ |
| Đáp án có đến TRỰC TIẾP? (Không giải thích vòng vo, không bắt đầu bằng bối cảnh xa lạ?) | ☐ |
| Khán giả có cảm giác được "thưởng" vì đã ở lại? (Đáp án cụ thể, bất ngờ, xứng đáng chờ đợi?) | ☐ |
| **MỞ ĐẦU SÚC TÍCH:** Câu mở chương có vào thẳng trọng tâm, gọn gàng, tránh dông dài vòng vo không? (VD: nêu ngay chủ thể, vật chứng hoặc con số then chốt). | ☐ |

### Kiểm tra STACKING LOOPS (áp dụng cho toàn bộ kịch bản):

> **Nguyên lý Zeigarnik:** Mạch tự sự luôn duy trì câu hỏi tò mò chưa được trả lời trong đầu người nghe (khung chấm III Gieo và gặt). Không bao giờ đóng tất cả loop trước chương cuối.

| Câu hỏi | Đạt? |
|---|---|
| MACRO LOOP (câu hỏi lớn xuyên suốt video) có được mở từ Ch1 và chỉ đóng ở chương cuối? | ☐ |
| Mỗi mối nối: khi đóng 1 loop → có mở ngay 1 loop MỚI? (Không để khoảng trống "đã trả lời hết") | ☐ |
| Có các tầng loop phối hợp chặt chẽ (câu hỏi xuyên suốt toàn bài và câu hỏi điều tra riêng của từng chặng)? | ☐ |

### Bảng từ/cụm CẤM dùng để nối chương:
- "Đó chính xác là lý do..." — tường thuật phẳng
- "Câu hỏi đặt ra là..." — câu hỏi tu từ mềm
- "Chúng ta cần nhìn vào..." — giọng giáo viên
- "Và chính nhà đầu tư cần..." — lời khuyên ở giữa bài
- "Nhưng đó mới chỉ là bề mặt" — template sáo rỗng
- "Để hiểu rõ hơn, chúng ta cần..." — dắt tay, không tạo tò mò
- "Trong phần tiếp theo, chúng ta sẽ..." — mini-intro, dead air
- "Bây giờ, hãy cùng nhìn vào..." — mini-intro, dead air
- "Như đã đề cập ở phần trước..." — recap không cần thiết

> **Xem chi tiết và ví dụ tệ/tốt:** `00_core/anti_patterns.md` §Anti-pattern 12 (Dead Transition Trap).

**Nếu bất kỳ checkbox nào chưa tick → NGHIÊM CẤM submit chapter. Viết lại đoạn kết/mở.**

---

## GATE 4D — ⛔ ĐỘ DỄ HIỂU KHI NGHE (Acoustic Comprehensibility Gate)

> **Lệnh cứng:** Kịch bản viết ra phải để giải thích cho một người bình thường hiểu bằng tai, không phải để in thành văn bản học thuật.

### Bộ lọc Chuyển ngữ Khái niệm (Conceptual Translation Check):
- [ ] Không chép nguyên văn các điều khoản luật khô khan kiểu "Khoản X Điều Y". Đã chuyển ngữ thành bản chất động lực: "Đạo luật mới buộc...", "Hàng rào pháp lý dựng lên...".
- [ ] Không nhồi nhét số liệu dồn dập trong cùng một câu đơn; mỗi con số đọc lên phục vụ một nhịp.
- [ ] Không đoạn nào đọc liền nhiều con số như đọc bảng; số thừa để infographic nói. Kiểm bằng Phiếu B của `00_core/narrative_craft_rubric.md` (`SKILL.md` Bước 3b), không bằng đếm.
- [ ] Bảng nhịp chương (Chặng 2 của `SKILL.md`) đã in ra chat: mỗi nhịp có chức năng, vật chứng, số chính; chương có cú lật nhận thức được dàn dựng.
- [ ] Mọi số liệu chuyên ngành phức tạp (NIM, CIR, nợ xấu nhóm 3, trần tín dụng...) đều được giải thích đi kèm một phép ẩn dụ trực quan hoặc câu làm rõ ý nghĩa đời thường.

### Bộ lọc Nhịp nghỉ & Giải nén (Tension Release Check):
- [ ] Đoạn văn được tổ chức từ 2 đến 4 câu rõ ràng, không viết kiểu "mỗi dòng một câu".
- [ ] Độ dài mỗi câu đơn dưới 150 ký tự (khoảng 30–35 tiếng); mỗi vế giữa hai chỗ ngắt không quá khoảng 12 tiếng (`chapter_writer/SKILL.md` mục "Viết Câu Cho Tai").
- [ ] Không để phân tích lý thuyết thuần túy kéo dài khiến người nghe tự hỏi "sao còn đoạn này?" (tiêu chí VIII Nhịp); luôn làm mới bằng manh mối cụ thể, vật chứng thực tế có nguồn trong vault, phép loại suy đời thường hoặc data shock mới. Thêm số liệu không phải cách duy nhất để giải tỏa; một chuỗi số liệu dài cũng gây ngợp như lý thuyết.

**Nếu bất kỳ mục nào chưa tick -> Quay lại chỉnh sửa văn phong.**

---

## GATE 5 — Nhắc nhở nhanh trước khi viết (Quick Reminder)

> **Lưu ý:** Scan chi tiết sẽ do **Quality Czar** thực hiện ở Bước 3 (POST-WRITE). Gate này chỉ nhắc nhở nhanh các lỗi phổ biến nhất để tránh mất công viết lại.

Tự nhắc:
- Không dùng dấu `—` (TTS đọc sai)
- Không tự thêm luận điểm kinh tế ngoài brief
- Không dùng template transition — xem bảng CẤM tại Gate 4C và `anti_patterns.md` §12
- Ngày tháng phải cụ thể (không "gần nhất", "vừa qua")

---

## GATE 6 — Tuyên bố sẵn sàng (Readiness Declaration)

Chỉ được bắt đầu viết khi agent có thể điền đầy đủ vào câu sau:

> "Tôi đang tư duy với căn cước của **[Chuyên gia Thống trị: The Macro Economist / The Policy Analyst / The Industrial Controller / The Corporate Finance Analyst / The Critical Auditor / The Dialectic Architect...]** và thực thi qua lăng kính **Narrative Director & Voice Architect**. Tôi sắp viết **Chapter [số]** của episode **[slug]**. Chapter này có nhiệm vụ giải mã cơ chế **[Cơ chế kinh tế/pháp lý/vận hành cốt lõi]**, đưa khán giả từ **[trạng thái nhận thức A]** sang **[trạng thái nhận thức B]**. Tôi đã hoàn thành kích hoạt Gate 0 và bảo chứng trích lục tại Gate 0B với tệp **[Tên file vault / GVS]** dòng **[LXX-LXX hoặc mã DATA-XX]**. Tôi cam kết 100% tuân thủ kỷ luật Anti-Strawman (Steel-manning) và kiểm soát câu thoại < 150 ký tự cho đôi tai nghe. Câu đầu tiên sẽ mở bằng **[pain/cú lệch/hạt giống thu hoạch cụ thể]**, không phải luận đề trừu tượng."

Nếu không điền được → **KHÔNG ĐƯỢC VIẾT.**

---

## Lưu ý cho Agent

> Mỗi lần vi phạm Gate này là MỘT LẦN phải viết lại toàn bộ từ đầu. Viết lại = tốn token gấp đôi + phá vỡ continuity toàn episode. Chi phí của việc NGHĨ KỸ TRƯỚC là 0. Chi phí của việc VIẾT SAI là rất cao.
