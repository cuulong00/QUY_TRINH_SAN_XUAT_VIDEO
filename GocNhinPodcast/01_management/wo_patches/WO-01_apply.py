import sys,os
D=sys.argv[1]
E=[]  # (file, old, new, tag)
def R(f,old,new,tag): E.append((f,old,new,tag))

# Q1 — case study Loại B: tối đa 2
R('.agents/workflows/build_outline.md',
  "Giới hạn đúng 1 Case Study quốc tế điển hình;",
  "Tối đa 2 case study quốc tế, mỗi case ≤ 3 phút (luật gốc: `00_core/content_principles.md` §5);","Q1")
R('.agents/workflows/build_brief.md',
  "Giới hạn Case Study quốc tế — Tối đa 1 case đối với Loại B; không sa đà kể chuyện nước ngoài",
  "Giới hạn Case Study quốc tế — theo `00_core/content_principles.md` §5 (A/B tối đa 2, C tối đa 3, mỗi case ≤ 3 phút); không sa đà kể chuyện nước ngoài","Q1")

# Q2 + Q7 — rules/chapter-writing.md
f='.agents/rules/chapter-writing.md'
R(f,"- Chỉ đọc thêm các file upstream thật sự liên quan đến chapter đang viết: `02_research_map.md`, `02_research_synthesis.md`, `04_hook_pack.md`, hoặc 3 câu cuối của chapter liền trước để gặt seed.\n- Không mặc định đọc lại toàn bộ chapter history nếu `09_narrative_state_tracker.md` đã đủ để tránh lặp.\n",
  "- Đọc toàn bộ các chương đã viết (`chapter_01.md` đến `chapter_N-1.md`) trước khi viết chương N: kịch bản chỉ vài nghìn từ, đọc hết để giữ nhịp, chống lặp và gặt seed (user chốt 02/10/2026, WO-00 Q7).\n- Đọc thêm các file upstream thật sự liên quan đến chapter đang viết: `02_research_map.md`, `02_research_synthesis.md`, `04_hook_pack.md`.\n","Q7")
R(f,"- **Chapter 2 Contract:** BẮT BUỘC nối vĩ mô → đời sống chung của xã hội/người dân. Dùng lăng kính PHỔ QUÁT (\"Chúng ta\", \"Xã hội hiện đại\", \"Tầng lớp lao động\"). NGHIÊM CẤM Zoom-In cá nhân hóa cực đoan (VD: \"Anh Minh 35 tuổi...\").",
  "- **Chapter 2:** điểm tựa liên quan theo loại đề tài, luật gốc ở `00_core/content_principles.md` §2 (A: đời sống chung bằng lăng kính phổ quát; B: bài toán doanh nghiệp/quốc gia, không ép đời sống; C: nghịch lý, tò mò trí tuệ). Không bịa nhân vật cá nhân hóa (\"Anh Minh 35 tuổi...\").","Q2")
R(f,"- **Quy tắc 3 phút:** Không để > 3 phút liên tiếp chỉ phân tích/framework nặng mà không có liên hệ áp lực đời sống phổ quát.",
  "- **Quy tắc 3 phút:** theo `00_core/content_principles.md` §2 (quy tắc chung): không để > 3 phút liên tiếp chỉ phân tích mà không có con số mới, phép loại suy hoặc câu hỏi phản biện.","Q2")

# Q3 — chương kết (longform_blueprint)
f='00_core/longform_blueprint.md'
R(f,"#### Chương Kết Bài ($CH[N]$) — Grand Payoff & High Energy CTA\nMục tiêu:\n- Đóng toàn bộ Open Loops đã gieo từ Hook.\n- Chốt lại insight cốt lõi sắc sảo nhất toàn bài — để lại một lăng kính nhận thức có sức bám dài hạn (Mental Model).\n- Giữ năng lượng cao đến giây cuối cùng, kết bằng câu mạnh nhất, không dùng \"Tóm lại...\", \"Cuối cùng...\".\n- CTA ngắn gọn, tự nhiên, điều hướng người xem sang video phân tích liên quan tiếp theo trên kênh.",
  "#### Chương Kết Bài ($CH[N]$) — Grand Payoff\nLuật gốc: `00_core/stance_and_judgment.md` §1 và §8 (chế độ kết A/B), `.agents/skills/chapter_writer/SKILL.md` mục \"Chương kết\". Tóm tắt:\n- Trả lời các open loop phụ đã gieo; câu hỏi lớn kết theo chế độ đã chọn (A: nói thẳng lập trường một lần kèm điều kiện có thể sai; B: trao khung §1b rồi đặt câu hỏi mở nhắm đúng biến số quyết định).\n- Để lại một lăng kính nhận thức có sức bám dài hạn; câu cuối làm người xem nhìn lại câu mở đầu theo cách khác.\n- Kết bằng câu mạnh nhất, không \"Tóm lại...\", \"Cuối cùng...\", không tóm tắt lại video.\n- Không CTA ở chương kết: CTA duy nhất nằm cuối Chương 2 (`.agents/AGENTS.md` mục 4).","Q3")
R(f,"Một kết tốt nên có:\n- 1–2 câu tóm insight cốt lõi,\n- action framework rõ,\n- một câu chốt có lực nhưng không gồng,\n- CTA dẫn sang video tiếp theo,\n",
  "Một kết tốt nên có (luật gốc: `stance_and_judgment.md` §1, §8):\n- lập trường (chế độ A) hoặc khung tự nhận định (chế độ B), nói một lần,\n- Loại A: có thể kèm khung nhận thức giúp người xem tự định vị; Loại B/C: hệ quả và bài học chiến lược, không lời khuyên hành động,\n- một câu chốt có lực nhưng không gồng,\n- không tóm tắt lại video, không CTA (CTA duy nhất ở cuối Chương 2).\n","Q3")
R(f,"- [ ] Action hoặc Implication framework cụ thể, không bị hòa tan?\n- [ ] Phần kết có năng lượng cao + CTA dẫn video tiếp?",
  "- [ ] Chương kết đúng chế độ A/B đã chọn (`stance_and_judgment.md` §1), không bị hòa tan?\n- [ ] Phần kết có năng lượng cao, không tóm tắt, không CTA?","Q3")
# Q4
R(f,"Mỗi chương tối đa ~2.5 phút narration.",
  "Độ dài mỗi chương theo ngân sách [Floor – Target – Ceiling] của `07_outline.md`, trần tuyệt đối 1.050 từ (≈ 4,7 phút); vượt trần thì tách chương (`.agents/workflows/build_outline.md` Trạm 5).","Q4")
# Q5
R(f,"- Câu ngắn: 8-15 từ cho câu phân tích, 3-8 từ cho câu chốt.",
  "- Giới hạn cứng: mỗi câu dưới 150 ký tự (`.agents/skills/chapter_writer/SKILL.md` mục \"Writing for the Ear\"). Gợi ý nhịp (không bắt buộc): câu phân tích khoảng 8–15 từ, câu chốt 3–8 từ, trộn độ dài để tránh đơn điệu.","Q5")

# Q6 — cấm tả cảnh: gỡ tiêu chí gợi hình
f='00_core/masterpiece_quality_standard.md'
R(f,"4. Mang đậm **Chất Nghệ Thuật Điện Ảnh (Cinematic Artistry)**, gợi hình thị giác và giàu nhạc tính ngôn ngữ.",
  "4. Giàu nhạc tính ngôn ngữ nói; sức nặng đến từ dữ kiện cụ thể, không từ tả cảnh (user chốt 02/10/2026, WO-00 Q6).","Q6")
R(f,"   * *Nghệ thuật Tương phản Điện ảnh (Chiaroscuro Storytelling):* Đặt các thái cực sáng - tối cạnh nhau để tạo sức căng nhận thức.\n","","Q6")
R(f,"*   **5.1. Nghệ Thuật Gợi Hình Điện Ảnh (Cinematic Imagery) — 6 điểm:**\n    *   Khả năng \"vẽ hình trong tâm tưởng\" thính giả (*The Mind's Eye*). Ngôn từ mang tính điêu khắc, có màu sắc, ánh sáng, chất liệu và trọng lượng vật lý của hiện trường (khối khuôn dập triệu đô, cánh tay robot hàn, container dầm mưa nắng cảng biển, chiếc cối xay công nghiệp khổng lồ).\n    *   Tránh hoàn toàn các khái niệm trừu tượng suông sẻ không có mỏ neo hình ảnh.",
  "*   **5.1. Cụ Thể Bằng Dữ Kiện, Không Tả Cảnh (Concreteness Without Scenery) — 6 điểm:**\n    *   Khái niệm trừu tượng được neo bằng dữ kiện cụ thể có nguồn (con số, văn bản, quyết định, đối tượng có thật được nhắc tên), không bằng tả cảnh.\n    *   Cấm tả cảnh thời tiết, không khí, ánh sáng, cảm giác vật lý và mọi chi tiết minh họa không có nguồn (luật gốc: `.agents/skills/chapter_writer/SKILL.md` mục \"Writing for the Ear\" điểm 7).","Q6")
R(f,"    *   Tạo được sức căng tương phản điện ảnh (*Chiaroscuro Tension*) giữa ánh sáng thành công rực rỡ và bóng tối rủi ro sâu thẳm.\n",
  "    *   Sức căng đến từ đặt hai dữ kiện đối nghịch cạnh nhau (thành tích và cái giá), không từ tính từ hay tả cảnh.\n","Q6")
R(f,"Cơ bản đạt số liệu nhưng nhịp điệu còn khô khan hoặc thiếu chất gợi hình.","Cơ bản đạt số liệu nhưng nhịp điệu còn khô khan hoặc khái niệm chưa được neo bằng dữ kiện cụ thể.","Q6")
f='00_core/chapter_quality_standard.md'
R(f,"(ngắt nghỉ nhịp nhàng, giàu chất gợi hình, nhạc tính và câu vàng triết lý)","(ngắt nghỉ nhịp nhàng, cụ thể bằng dữ kiện, nhạc tính; câu vàng nếu có)","Q6")
R(f,"giàu nhạc điệu nói, giàu tính gợi hình thị giác (*The Mind's Eye*), không từ cấm AI.","giàu nhạc điệu nói, không tả cảnh, không từ cấm AI.","Q6")
R(f,"*   **Tiêu chuẩn 2.3: Thẩm Mỹ Gợi Hình Điện Ảnh & Sức Căng Tương Phản (Cinematic Imagery & Chiaroscuro) — 6 điểm:**",
  "*   **Tiêu chuẩn 2.3: Cụ Thể Bằng Dữ Kiện & Sức Căng Đối Nghịch (Concreteness & Contrast) — 6 điểm:**","Q6")
R(f,"    *   Khả năng \"vẽ hình trong tâm tưởng\" thính giả (*The Mind's Eye*). Ngôn từ mang tính điêu khắc, gợi mở bối cảnh vật lý thực tế (chiếc cối xay khổng lồ, tiếng dập khuôn thép, bóng dáng con tàu viễn dương giữa đêm).\n    *   Tạo được sự tương phản điện ảnh gay gắt (*Chiaroscuro Tension*) giữa ánh sáng của thành tích bên ngoài và bóng tối của áp lực rủi ro bên trong.",
  "    *   Khái niệm được neo bằng dữ kiện cụ thể có nguồn (con số, văn bản, quyết định, đối tượng có thật). Cấm tả cảnh, không khí, ánh sáng, cảm giác vật lý và chi tiết minh họa không nguồn (WO-00 Q6).\n    *   Sức căng đến từ đặt hai dữ kiện đối nghịch cạnh nhau (thành tích và cái giá), không từ tính từ.","Q6")
R(f,"Số liệu đầy đủ nhưng nhịp điệu bị chùng hoặc thiếu chất gợi hình.","Số liệu đầy đủ nhưng nhịp điệu bị chùng hoặc khái niệm chưa được neo bằng dữ kiện cụ thể.","Q6")
R(f,"| **2.3. Thẩm mỹ Gợi hình & Sức căng Tương phản** | 6 | [X]/6 | [Dẫn chứng hình ảnh gợi hình điện ảnh, phép ẩn dụ đắt giá & tương phản sáng/tối] |",
  "| **2.3. Cụ thể bằng dữ kiện & Sức căng đối nghịch** | 6 | [X]/6 | [Dẫn chứng dữ kiện neo khái niệm; xác nhận 0 câu tả cảnh / chi tiết không nguồn] |","Q6")

# Q7 — lý do đọc toàn bộ: bỏ gắn model
R('.agents/AGENTS.md',"Tuyệt đối không giới hạn trong 3 câu cuối. Tận dụng triệt để cửa sổ 1 triệu tokens của Gemini 3.8 Flash để kiểm soát nhịp điệu, chống lặp từ/lặp cấu trúc câu và tạo các liên kết gợi nhớ (callbacks) tinh tế.",
  "Tuyệt đối không giới hạn trong 3 câu cuối. Kịch bản chỉ vài nghìn từ, đọc hết để kiểm soát nhịp điệu, chống lặp từ/lặp cấu trúc câu và tạo các liên kết gợi nhớ (callbacks) tinh tế (user chốt 02/10/2026, WO-00 Q7).","Q7")
f='.agents/skills/chapter_writer/SKILL.md'
R(f,"## Kiến Trúc Rolling Context (Full Clean Script History — Tối Ưu Cho Gemini 3.8 Flash)","## Kiến Trúc Rolling Context (Full Clean Script History)","Q7")
R(f,"Để tận dụng triệt để cửa sổ 1 triệu tokens và khả năng suy luận dài hạn (Long-Horizon Reasoning) của Gemini 3.8 Flash, khi viết Chương N, Agent bắt buộc nạp các tệp sau vào ngữ cảnh làm việc:",
  "Kịch bản chỉ vài nghìn từ, nên khi viết Chương N, Agent nạp đủ các tệp sau vào ngữ cảnh làm việc (WO-00 Q7):","Q7")
R('.agents/rules/content-os-pipeline.md',"5. **Viết tuần tự & Nạp Toàn Bộ Lịch Sử Thoại Sạch (Full Clean Script History - Tối ưu cho Gemini 3.8 Flash):** Khi bắt đầu Pha 7 (Viết Chương), viết tuần tự từng chương một. Nhằm giải phóng 100% sức mạnh của cửa sổ ngữ cảnh 1 triệu tokens và năng lực suy luận dài hạn (Long-Horizon Reasoning) của Gemini 3.8 Flash:",
  "5. **Viết tuần tự & Nạp Toàn Bộ Lịch Sử Thoại Sạch (Full Clean Script History):** Khi bắt đầu Pha 7 (Viết Chương), viết tuần tự từng chương một. Kịch bản chỉ vài nghìn từ, nên nạp đủ (WO-00 Q7):","Q7")

# Q8 — hook không kết luận
R('00_core/golden_samples/golden_hook.md',
  "### 3. Lập trường rõ ràng — không trung lập giả\nHook phải cho thấy GocNhinPodcast có **quan điểm**. \"Không ai nghiêm túc có thể gọi đó là ảo giác\" mạnh hơn \"một số ý kiến cho rằng...\". Chuyên gia thật không ngồi hàng rào.",
  "### 3. Đặt câu hỏi và căng thẳng, chưa kết luận\nHook cho thấy kênh có **cách đọc riêng** qua việc chọn nghịch lý và câu hỏi sắc, nhưng chưa nói kết luận (`00_core/stance_and_judgment.md` §8: Chương 1 đặt câu hỏi, chưa kết luận). Lập trường được \"kiếm\" sau bằng chứng, nói ở chương kết.","Q8")
R('00_core/golden_samples/golden_hook.md',"[ ] Có lập trường rõ, không trung lập giả?","[ ] Có cách đọc riêng (nghịch lý, câu hỏi sắc) nhưng chưa kết luận?","Q8")

errs=0; log=[]
for f,old,new,tag in E:
    p=os.path.join(D,'new',f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); log.append(f"{tag} {f}")
print("\n".join(log)); print("số sửa:",len(log),"lỗi:",errs)
