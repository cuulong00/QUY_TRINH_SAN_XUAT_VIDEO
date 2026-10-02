import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append((f,old,new,tag))
BGT="`00_bang_gia_thuyet.md`"
# --- Template 01 (Pha 1)
f='02_templates/masterpiece_pipeline/01_global_vision_synthesis_template.md'
R(f,"### 2. Nhật Ký Tranh Biện Đối Thoại Trực Tiếp (Direct Debate Transcript)",
"""### 1.4. Bản Đồ Nền Từ Kho Tri Thức (phần B của form tư duy — BẮT BUỘC trước khi tranh biện)
*(Nguồn duy nhất: `scripts/kbq` và `kbaudit`, lệnh theo `.agents/rules/orchestration-protocol.md` mục "Kho tri thức dùng chung". Mọi dòng có mã OBS. Hiểu biết sẵn có của model KHÔNG tính là "đã biết".)*
| Thực thể / quan hệ | Dữ kiện nền đã có (mã OBS) | Chưa biết (→ GAP) |
|---|---|---|
| [thực thể trọng tâm 1] | [tóm 1 dòng + `OBS-…`] | [GAP-…] |
| [quan hệ A ↔ B] | [`kbq evidence A B` + `OBS-…`] | |
- Dấu thời điểm tra kho: [YYYY-MM-DD HH:MM]. Trước khi nộp Pha 1, chạy lại để lấy phần kho đổi.
- Kết quả `kbaudit`: __% thực thể trọng tâm có dữ kiện, __ GAP P1 → điền nút N1 vào hiến chương.

### 1.5. Giả Thuyết Cạnh Tranh (phần C) → `00_bang_gia_thuyet.md`
- Đặt **tối thiểu 3 giả thuyết** trả lời câu hỏi trung tâm, trong đó luôn có giả thuyết "nhàm" (chủ thể làm đúng điều họ công bố). Nếu sau phần B chỉ thấy một lời giải (N2 = 1) thì bắt buộc ép thêm hai giả thuyết đối lập.
- Mỗi giả thuyết ghi trước "dữ kiện nào sẽ bác tôi". Lập ma trận bằng chứng ban đầu từ các OBS ở mục 1.4. Khuôn: `02_templates/masterpiece_pipeline/00_bang_gia_thuyet_template.md`.
- Hội đồng tranh biện (mục 2) tranh luận trên các giả thuyết này, không tranh luận trên một luận điểm đã chọn sẵn.

### 2. Nhật Ký Tranh Biện Đối Thoại Trực Tiếp (Direct Debate Transcript)""","form")
R(f,"- **Core Paradox:** [Mâu thuẫn hệ thống cốt lõi]",
"- **Core Paradox:** [Mâu thuẫn hệ thống cốt lõi]\n- **Giả thuyết dẫn đầu tạm thời và các giả thuyết còn sống:** [H? dẫn đầu vì ít bằng chứng ngược nhất tới giờ; H?, H? còn sống; không coi là kết luận — kết luận là việc của Pha 3 sau khi ma trận được lấp]","form")
R(f,"- **Phản biện theo từng lăng kính đã chọn:** [Mỗi lăng kính một luận điểm phản bác mạnh nhất, kèm dữ kiện đối kháng có mã OBS hoặc ghi GAP].",
"- **Phản biện theo từng lăng kính đã chọn:** [Mỗi lăng kính một luận điểm phản bác mạnh nhất, kèm dữ kiện đối kháng có mã OBS hoặc ghi GAP]. Mỗi phản biện phải trỏ tới giả thuyết nó tấn công (H?) và được ghi thành hàng E trong "+BGT+".","form")
R(f,"""## PHẦN III: KẾ HOẠCH NGHIÊN CỨU ĐỊA HÌNH ÁNH XẠ 1-1 VỚI BỘ 5 CÂU HỎI BẢN THỂ HỌC (TOPOGRAPHICAL RESEARCH BLUEPRINT)

*(Các Query nạp nguồn BẮT BUỘC ánh xạ 1-1 với 5 Câu Hỏi Bản Thể Học Phổ Quát đã xác lập ở Phần I)*

### 1. Bộ 5 Targeted Ingestion Prompts cho NotebookLM (Deep Mode) — BẮT BUỘC ĐỦ 5 PROMPTS""",
"""## PHẦN III: KẾ HOẠCH NGHIÊN CỨU ĐI TỪ MA TRẬN BẰNG CHỨNG (TOPOGRAPHICAL RESEARCH BLUEPRINT)

*(Nghiên cứu Pha 2 chỉ nhắm vào các ô "chưa phân biệt được" trong `00_bang_gia_thuyet.md` mục 2b và các GAP của `kbaudit`. Ô mà kho đã trả lời được thì không nghiên cứu lại. Mỗi prompt và mỗi câu trích xuất ghi mã ô (H?↔H?) hoặc mã GAP nó lấp. Số lượng prompt theo nút N1: độ phủ cao → ít prompt, nhắm thẳng; độ phủ thấp → thêm vòng gom nền trước. Danh mục 5 khía cạnh dưới đây là **danh sách kiểm độ phủ**, không phải khuôn để sinh prompt.)*

### 1. Prompts nạp nguồn cho NotebookLM (Deep Mode) — mỗi prompt ghi ô ma trận / GAP nó lấp; prompt phản biện (khía cạnh 5) luôn bắt buộc""","form")
R(f,"""### 2. Danh Sách Câu Hỏi Trích Xuất (Batch Extraction Queries)
- [Query 1: Giải mã mắt xích nhân quả 1...]""",
"""### 2. Danh Sách Câu Hỏi Trích Xuất (Batch Extraction Queries) — mỗi câu ghi `[H?↔H? | GAP-…]`
- [Query 1 `[H1↔H2]`: Dữ kiện nào phân biệt được hai giả thuyết này...]""","form")
# --- build_global_vision.md (Pha 1 workflow)
f='.agents/workflows/build_global_vision.md'
R(f,"### Bước 1: Xác định Slug & Đọc Tài Liệu Nguồn\n- Xác định `episodes/[slug]/`.\n- Đọc các tệp bắt buộc:",
"### Bước 1: Xác định Slug & Đọc Tài Liệu Nguồn\n- Xác định `episodes/[slug]/`.\n- Đọc `episodes/[slug]/00_hien_chuong.md` trước (câu hỏi trung tâm, chỉ đạo user, điều đã loại, Hồ sơ đề tài N1–N5). Chưa có thì dừng, tạo theo `02_templates/masterpiece_pipeline/00_hien_chuong_template.md` cùng user.\n- Đọc các tệp bắt buộc:","form")
R(f,"### Bước 3: Đúc Khung Tư Duy 4 Tầng Phổ Quát (The 4-Tier Blueprint)",
"""### Bước 2b: Bản Đồ Nền Từ Kho → Giả Thuyết Cạnh Tranh → Ma Trận (form tư duy, phần B–C–D)
1. Hỏi kho theo thứ tự trong `.agents/rules/orchestration-protocol.md` mục "Kho tri thức dùng chung" (`kbq evidence` trước, rồi `entity`, `links`, `facts`), chạy `kbaudit`. Điền mục 1.4 của template: mọi dòng có mã OBS; ghi dấu thời điểm tra kho; điền N1 vào hiến chương.
2. Đặt **≥ 3 giả thuyết** cho câu hỏi trung tâm (luôn có giả thuyết "nhàm"); nếu chỉ thấy một lời giải thì ép thêm hai giả thuyết đối lập (N2). Mỗi giả thuyết ghi "dữ kiện nào sẽ bác tôi".
3. Tạo `episodes/[slug]/00_bang_gia_thuyet.md` theo `02_templates/masterpiece_pipeline/00_bang_gia_thuyet_template.md`: hàng E từ các OBS ở bước 1, chấm `+ / − / 0` cho từng giả thuyết, liệt kê ô chưa phân biệt (mục 2b) để Pha 2 nhắm vào.
4. Hội đồng tranh biện (Bước 3, Phần I.2) tranh luận trên các giả thuyết, không trên một luận điểm chọn sẵn. Phản biện của mỗi lăng kính đã chọn (N5) ghi thành hàng E.

### Bước 3: Đúc Khung Tư Duy 4 Tầng Phổ Quát (The 4-Tier Blueprint)""","form")
R(f,"- [ ] Mọi con số trong Tầng 4 đều có mã `DATA-XX` định danh?",
"- [ ] Mọi con số trong Tầng 4 đều có mã `DATA-XX` định danh?\n- [ ] Mục 1.4 có bản đồ nền từ kho, mọi dòng có `OBS-…`, có dấu thời điểm tra kho; N1 đã điền vào hiến chương?\n- [ ] `00_bang_gia_thuyet.md` có ≥ 3 giả thuyết (có giả thuyết \"nhàm\"), mỗi giả thuyết ghi dữ kiện bác, ma trận có ≥ 1 hàng phân biệt được (có cả `+` và `−`), mục 2b liệt kê ô chưa phân biệt?\n- [ ] Phần III: mỗi prompt và câu trích xuất ghi mã ô ma trận hoặc GAP; không có prompt cho thứ kho đã trả lời?\n- [ ] Đã chạy `KB_GRAPH=kb_v2 scripts/kbaudit --check-evidence [slug]` ngay sau Pha 1 và trả lời nhóm BÁC (V25, V26)?","form")
# --- deep_research.md (Pha 2 workflow)
f='.agents/workflows/deep_research.md'
R(f,"   - Thiết kế và hiển thị bộ **3–5 Prompts nạp nguồn chuyên sâu độc lập**, mỗi prompt tập trung cào sâu vào một mảng đề tài trọng điểm (1. Lý thuyết vĩ mô & Năng suất; 2. Case studies quốc tế; 3. Thực trạng kiểm toán trong nước; 4. Đột phá chính sách/thể chế).",
"   - Đọc `episodes/[slug]/00_bang_gia_thuyet.md` mục 2b (ô chưa phân biệt) và `01b_knowledge_audit.md` (GAP). Mỗi prompt nạp nguồn nhắm một hoặc vài ô/GAP cụ thể và ghi mã `[H?↔H? | GAP-…]`. Số prompt theo nút N1 trong hiến chương (phủ cao: ít, nhắm thẳng; phủ thấp: thêm vòng gom nền). Không viết prompt cho thứ kho đã trả lời được. Prompt phản biện (khía cạnh 5) luôn bắt buộc.","form")
R(f,"   - Thiết kế và hiển thị danh sách 8-12 câu hỏi trích xuất cụ thể tương ứng với từng chương của Khung tuyến kịch bản, đính kèm nhãn chương (`Target Chapter`) và áp dụng các quy chuẩn kiểm toán.",
"   - Thiết kế và hiển thị danh sách câu hỏi trích xuất, mỗi câu gắn mã ô ma trận hoặc GAP (`[H1↔H2 | GAP-L03]`), không gắn nhãn chương (Pha 2 chưa có chương). Số câu theo số ô chưa phân biệt.","form")
R(f,"4. **Lưu trữ Kế hoạch:** Ghi lại toàn bộ nội dung trên vào tệp `episodes/[slug]/02_research_plan.md`.",
"4. **Lưu trữ Kế hoạch:** Ghi lại toàn bộ nội dung trên vào tệp `episodes/[slug]/02_research_plan.md`. Chạy `KB_GRAPH=kb_v2 scripts/kbaudit --check-plan [slug]` phải ĐẠT trước khi nạp nguồn.","form")
R(f,"3. **SUPPLEMENT & SYNTHESIZE:** Tạo tệp `02_research_map.md` (Bản đồ tọa độ) và `02_research_synthesis.md` (Bản tóm tắt cơ chế vĩ mô).",
"3. **CẬP NHẬT MA TRẬN (phần E của form tư duy):** mỗi dữ kiện mới từ vault thành một hàng E trong `00_bang_gia_thuyet.md` (nguồn `vault/R0X` + câu nguyên văn + kỳ, phạm vi), chấm `+ / − / 0`; giả thuyết có bằng chứng ngược thì thu hẹp hoặc loại, ghi dòng lịch sử. Không được xóa giả thuyết mà không có hàng E ngược.\n4. **SUPPLEMENT & SYNTHESIZE:** Tạo tệp `02_research_map.md` (Bản đồ tọa độ) và `02_research_synthesis.md` (Bản tóm tắt cơ chế vĩ mô). Synthesis kết bằng trạng thái ma trận: giả thuyết nào còn đứng, ô nào vẫn chưa phân biệt, bằng chứng BÁC nào còn đứng.","form")
R(f,"- Data gaps còn thiếu (nếu có)","- Data gaps còn thiếu (nếu có)\n- Trạng thái ma trận: số giả thuyết còn đứng / đã loại; ô chưa phân biệt còn lại; kết quả `kbaudit --check-evidence` sau Pha 2","form")
# --- deep_researcher/SKILL.md
f='.agents/skills/deep_researcher/SKILL.md'
R(f,">    - Thiết kế cấu trúc nghiên cứu trong `02_research_plan.md` gồm các Prompt nạp nguồn phủ đủ 5 khía cạnh trên và danh sách câu hỏi trích xuất (Extraction Queries). Số prompt và số câu trích xuất do độ phức tạp đề tài quyết định, phải nêu lý do chọn số lượng trong kế hoạch; mỗi câu trích xuất gắn với một claim chịu lực hoặc một mục Target Evidence Checklist.",
">    - Thiết kế cấu trúc nghiên cứu trong `02_research_plan.md` **đi từ ma trận bằng chứng** (`00_bang_gia_thuyet.md` mục 2b) và GAP của `kbaudit`: mỗi prompt và mỗi câu trích xuất ghi mã ô `[H?↔H?]` hoặc mã GAP nó lấp; không nghiên cứu thứ kho đã trả lời. 5 khía cạnh trên là danh sách kiểm độ phủ, không phải khuôn sinh prompt. Số prompt theo nút N1 của hiến chương, nêu lý do chọn số lượng trong kế hoạch.","form")
# --- strategy_council/SKILL.md
f='.agents/skills/strategy_council/SKILL.md'
R(f,"### Bước 3: Lập Kế Hoạch Nghiên Cứu Địa Hình Ánh Xạ 1-1 Với 5 Câu Hỏi Bản Thể Học (Topographical Research Blueprint)\n* Không chia query nghiên cứu tùy tiện. Hội đồng thiết kế:",
"### Bước 2c: Bản Đồ Nền Từ Kho → Giả Thuyết Cạnh Tranh → Ma Trận Bằng Chứng\n* Trước Bước 2, hội đồng đọc bản đồ nền từ kho (template 01 mục 1.4, mọi dòng có OBS) và đặt ≥ 3 giả thuyết cho câu hỏi trung tâm (luôn có giả thuyết \"nhàm\"; N2 = 1 thì ép thêm hai giả thuyết đối lập). Tranh biện Bước 2 diễn ra trên các giả thuyết này. Kết quả ghi vào `00_bang_gia_thuyet.md` (khuôn: `02_templates/masterpiece_pipeline/00_bang_gia_thuyet_template.md`). Quy trình chi tiết: `.agents/workflows/build_global_vision.md` Bước 2b.\n\n### Bước 3: Lập Kế Hoạch Nghiên Cứu Đi Từ Ma Trận Bằng Chứng (Topographical Research Blueprint)\n* Kế hoạch nhắm vào ô \"chưa phân biệt\" của ma trận và GAP của `kbaudit`; mỗi prompt ghi mã ô hoặc GAP; số prompt theo N1. Danh mục 5 khía cạnh dưới đây chỉ dùng để kiểm độ phủ. Hội đồng thiết kế:","form")
R(f,"3. **Phần III: Kế Hoạch Nghiên Cứu Địa Hình 1-1 Cho Pha 2 (Topographical Research Blueprint):**",
"3. **Phần III: Kế Hoạch Nghiên Cứu Đi Từ Ma Trận Bằng Chứng Cho Pha 2 (Topographical Research Blueprint):**\n   - Mỗi prompt / câu trích xuất ghi mã ô ma trận `[H?↔H?]` hoặc GAP; không nghiên cứu thứ kho đã trả lời.","form")
R(f,"   - Quyết định phê duyệt (Strategy Council Verdict) có chữ ký của Chủ tịch `the_macro_strategist` (Áp dụng nguyên tắc \"No Steelman, No Go\").",
"   - Quyết định phê duyệt (Strategy Council Verdict) có chữ ký của Chủ tịch `the_macro_strategist` (Áp dụng nguyên tắc \"No Steelman, No Go\" và \"No 3 Hypotheses, No Go\": chưa có ≥ 3 giả thuyết cạnh tranh trong `00_bang_gia_thuyet.md` thì không duyệt).","form")
# --- the_macro_strategist
R('.agents/personas/the_macro_strategist.md',"Deep research ở Pha 2 chỉ đắp phần kho còn thiếu. Dữ kiện lấy từ kho ghi kèm mã `OBS-...`.",
"Deep research ở Pha 2 chỉ đắp phần kho còn thiếu. Dữ kiện lấy từ kho ghi kèm mã `OBS-...`.\n- **Giả thuyết cạnh tranh, không luận điểm chọn sẵn:** sau bản đồ nền, đặt ≥ 3 giả thuyết (luôn có giả thuyết \"nhàm\"), lập ma trận bằng chứng trong `00_bang_gia_thuyet.md`, và chỉ cho nghiên cứu nhắm vào ô chưa phân biệt. Chủ tịch không duyệt đề tài có một giả thuyết duy nhất (\"No 3 Hypotheses, No Go\").","form")
# --- 03_brief_template (Pha 3): phần F kết luận + tách cách kể
f='02_templates/masterpiece_pipeline/03_brief_template.md'
R(f,"- **Grand Payoff (Aufhebung):** Cú nhảy nhận thức ở Màn 3 — Giải pháp thích ứng vượt thoát và sự thừa nhận đánh đổi sòng phẳng.",
"""- **Grand Payoff (Aufhebung):** Cú nhảy nhận thức ở Màn 3 — Giải pháp thích ứng vượt thoát và sự thừa nhận đánh đổi sòng phẳng.

### 1b. Kết Luận Từ Ma Trận Bằng Chứng (phần F của form tư duy — chép từ `00_bang_gia_thuyet.md` mục 4, không viết lại)
- **Giả thuyết còn đứng:** `H?` — vì có ít bằng chứng ngược nhất (liệt kê mã E ngược còn lại); các giả thuyết bị loại/thu hẹp và hàng E đã loại chúng.
- **Phạm vi được khẳng định:** chỉ phần có bằng chứng phân biệt (N4). Phần chưa phân biệt được ghi là điều kiện sai, không ghi là khẳng định.
- **Chế độ kết (N3):** A / B, lý do theo `00_core/stance_and_judgment.md` §1. Điều kiện khiến kết luận sai (§6): …
- **Bằng chứng BÁC còn đứng mà kịch bản phải chung sống:** mã E, và luận điểm thu hẹp thế nào vì chúng.
- Cách nghĩ (mục này) tách khỏi cách kể (mục 3): kết luận có thể nói thẳng ở đây, nhưng trong kịch bản chỉ lộ dần theo cấu trúc tò mò.""","form")
R(f,"| Mã | Dữ Liệu Thực Chứng | Nguồn Gốc File Trong `research_vault/` | Mã Footnote & Trích Dẫn Gốc (≤ 15 từ) | Ý Nghĩa Phân Tích |\n|---|---|---|---|---|",
"| Mã | Dữ Liệu Thực Chứng | Nguồn: `OBS-…` hoặc file `research_vault/` | Mã Footnote & Trích Dẫn Gốc (≤ 15 từ) | Kỳ, phạm vi, đơn vị | Nhãn mắt xích (`verified_data` / `market_analysis` / `opinion_commentary`) và mã E trong `00_bang_gia_thuyet.md` | Ý Nghĩa Phân Tích |\n|---|---|---|---|---|---|---|","form")
R(f,"| `DATA-01` | `[Con số 1]` | `[File nguồn 1]` | `[Footnote X]` - `\"...\"` | `[Ý nghĩa]` |\n| `DATA-02` | `[Con số 2]` | `[File nguồn 2]` | `[Footnote Y]` - `\"...\"` | `[Ý nghĩa]` |\n| `DATA-03` | `[Con số 3]` | `[File nguồn 3]` | `[Footnote Z]` - `\"...\"` | `[Ý nghĩa]` |",
"| `DATA-01` | `[Con số 1]` | `OBS-…` / `R01.md` | `[Footnote X]` - `\"...\"` | `[2025, hợp nhất, tỷ VND]` | `verified_data` · `E03` | `[Ý nghĩa]` |\n| `DATA-02` | `[Con số 2]` | … | … | … | `market_analysis` · `E07` | `[Ý nghĩa]` |","form")
R(f,"  * CẤM phân cực thiện ác; mọi hành vi kinh doanh phải giải thích bằng bài toán điểm hòa vốn và rủi ro.",
"  * CẤM phân cực thiện ác; mọi hành vi kinh doanh phải giải thích bằng động lực, chi phí cơ hội và đánh đổi (`script_architect` §1 mục 8).\n  * CẤM viết suy luận thành dữ kiện: mọi mắt xích trong brief mang nhãn theo `00_bang_gia_thuyet.md`; câu nào không có mã E/OBS thì không được viết như dữ kiện.","form")
# --- build_brief.md (Pha 3 workflow)
f='.agents/workflows/build_brief.md'
R(f,"2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/01_global_vision_synthesis.md`, `episodes/[slug]/02_research_map.md`, và `episodes/[slug]/02_research_synthesis.md`.",
"2. Đọc: `episodes/[slug]/00_hien_chuong.md` (đề bài khóa, N1–N5), `episodes/[slug]/00_bang_gia_thuyet.md` (giả thuyết còn đứng, ma trận, bằng chứng BÁC), `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/01_global_vision_synthesis.md`, `episodes/[slug]/02_research_map.md`, và `episodes/[slug]/02_research_synthesis.md`.","form")
R(f,"   [ ] Biến cố trung tâm (Central Inciting Incident) — sự kiện/văn bản cụ thể phát nổ mở màn",
"   [ ] Câu hỏi trung tâm và tiêu đề đúng nguyên văn `00_hien_chuong.md`; từ khóa đã loại không xuất hiện\n   [ ] Mục 1b: giả thuyết còn đứng chép từ `00_bang_gia_thuyet.md` mục 4 (ít bằng chứng ngược nhất), phạm vi khẳng định theo N4, bằng chứng BÁC còn đứng được nêu; chế độ kết khớp N3\n   [ ] Mọi chân đỡ của giả thuyết dẫn đầu ở Pha 1 còn mặt trong Data Passport, hoặc có dòng lý do bỏ\n   [ ] Biến cố trung tâm (Central Inciting Incident) — sự kiện/văn bản cụ thể phát nổ mở màn","form")
R(f,"   [ ] Bảng mỏ neo số liệu chiến lược — Data Passport đối chiếu 1-1 với research_vault/ và 01_global_vision_synthesis.md",
"   [ ] Bảng mỏ neo số liệu chiến lược — Data Passport: mỗi dòng có `OBS-…` hoặc file vault, kỳ/phạm vi/đơn vị, nhãn mắt xích và mã E","form")
# --- orchestration-protocol mục 1 Pha 1: thêm bước giả thuyết
f='.agents/rules/orchestration-protocol.md'
R(f,"Mỗi dữ kiện nối tới mọi bên tham gia (cạnh INVOLVES), nên `facts` của một thực thể có cả dữ kiện của bên khác mà nó tham gia.",
"Mỗi dữ kiện nối tới mọi bên tham gia (cạnh INVOLVES), nên `facts` của một thực thể có cả dữ kiện của bên khác mà nó tham gia. Sau bản đồ nền: đặt ≥ 3 giả thuyết cạnh tranh và lập ma trận bằng chứng trong `00_bang_gia_thuyet.md` (`.agents/workflows/build_global_vision.md` Bước 2b); chạy `kbaudit --check-evidence` ngay sau Pha 1, không đợi Pha 4.","form")
errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: {n} lần :: {old[:60]!r}"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {f}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
