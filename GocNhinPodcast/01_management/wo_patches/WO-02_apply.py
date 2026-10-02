import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append((f,old,new,tag))
LENS=("**Danh mục lăng kính phản biện** (chọn ở Pha 1 theo nút N5 của hồ sơ đề tài, ghi vào hiến chương tập; tối thiểu 2 lăng kính, không mặc định lăng kính nào):\n"
"  1. *Thị trường & Chi phí cơ hội (The Market Skeptic):* méo mó giá cả do trợ cấp/hành chính, phân bổ vốn kém, chi phí cơ hội của nền kinh tế.\n"
"  2. *Thể chế & Thực thi (The Institutional Realist):* ma sát thực thi, nhóm lợi ích cố thủ, rủi ro điều tra, trả đũa thuế quan, luật chơi thay đổi.\n"
"  3. *Cạnh tranh & Phản ứng của đối thủ (The Competitive Realist):* đối thủ hóa giải lợi thế bằng M&A, hợp tác, hiệu ứng mạng lưới; lợi thế được cho là bền có thật không.\n"
"  4. *Kỹ thuật & Chuỗi cung ứng (The Supply-Chain Engineer):* giới hạn vật lý, công suất, đầu vào, logistics, công nghệ thay thế.\n"
"  5. *Dòng tiền & Thanh khoản (The Forensic Cash Auditor):* FCF, cấu trúc nợ, điểm hòa vốn, thanh khoản. **Chỉ bật khi đề tài là doanh nghiệp hoặc thị trường vốn và luận điểm xoay quanh sức khỏe tài chính** (user chốt 02/10/2026, WO-00 Q10); không bật cho đề tài chiến lược, thể chế, công nghiệp chỉ vì có số tài chính.")

# 1. AGENTS.md — bản gốc duy nhất của hội đồng phản biện
R('.agents/AGENTS.md',
"- **Tôn chỉ Tối thượng:** Triệt tiêu hoàn toàn tư duy đơn tuyến, bệnh \"Yes-Man\", và sự xác nhận thiên lệch (Confirmation Bias). Mọi phân tích mô hình, chính sách hoặc chiến lược BẮT BUỘC phải chịu sự thử lửa khắt khe của **Hội đồng Phản biện Đa diện (The Tri-Adversarial Red Team Council)** do `the_critical_auditor` chủ trì:\n  1. *Lăng kính Thị trường & Chi phí cơ hội (The Market Skeptic):* Sát hạch tính hiệu quả của việc phân bổ nguồn lực. Vạch trần méo mó giá cả do trợ cấp/hành chính, rủi ro tạo doanh nghiệp xác sống (zombie firms), và chi phí cơ hội của toàn bộ nền kinh tế.\n  2. *Lăng kính Thể chế & Trắc trở thực thi (The Institutional Realist):* Sát hạch ma sát thực thi quan liêu, sự phản kháng của các nhóm lợi ích cố thủ, rủi ro bị điều tra chống bán phá giá và trả đũa thuế quan từ các đối tác thương mại quốc tế (Mỹ, EU, Trung Quốc).\n  3. *Lăng kính Kế toán Dòng tiền & Sức ép thanh khoản (The Forensic Cash Auditor):* Bóc trần ảo tưởng doanh thu danh nghĩa. Soi thẳng vào dòng tiền tự do FCF âm kéo dài, cấu trúc lấy nợ ngắn hạn nuôi tài sản dài hạn, điểm hòa vốn viển vông và nguy cơ sập bẫy thanh khoản khi chu kỳ tiền tệ đảo chiều.",
"- **Tôn chỉ Tối thượng:** Triệt tiêu tư duy đơn tuyến, bệnh \"Yes-Man\" và xác nhận thiên lệch (Confirmation Bias). Mọi phân tích mô hình, chính sách hoặc chiến lược phải chịu thử lửa của **Hội đồng Phản biện Đa diện (Multi-Lens Red Team)** do `the_critical_auditor` chủ trì. **Đây là bản gốc duy nhất của danh mục lăng kính; mọi file khác chỉ trỏ về đây.**\n"+LENS, "Q10")
# 2. content-os-pipeline — trỏ
R('.agents/rules/content-os-pipeline.md',
"    *   **Hội Đồng Phản Biện Đa Diện (The Tri-Adversarial Red Team Council):** Mọi đề tài bắt buộc phải trải qua cuộc sát hạch đối kháng của 3 lăng kính độc lập do `the_critical_auditor` chủ trì:\n        1. *The Market Skeptic (Thị trường & Chi phí cơ hội):* Bóc trần méo mó phân bổ vốn, bao cấp làm lệch lạc thị trường, doanh nghiệp xác sống, chi phí cơ hội vĩ mô.\n        2. *The Institutional Realist (Thể chế & Địa chính trị):* Bóc trần ma sát quan liêu, nhóm lợi ích cố thủ, rủi ro trả đũa thuế quan/chuỗi cung ứng quốc tế.\n        3. *The Forensic Cash Auditor (Kế toán Dòng tiền & Thanh khoản):* Soi dòng tiền tự do FCF âm, tỷ lệ nợ ngắn hạn/dài hạn, điểm hòa vốn viển vông, áp lực thanh khoản.",
"    *   **Hội Đồng Phản Biện Đa Diện (Multi-Lens Red Team):** mọi đề tài qua sát hạch của ít nhất 2 lăng kính do `the_critical_auditor` chủ trì, chọn theo đề tài ở Pha 1 và ghi vào hiến chương. Danh mục lăng kính và điều kiện bật lăng kính dòng tiền: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\" (bản gốc duy nhất, WO-00 Q10).", "Q10")
# 3. personas
R('.agents/personas/the_critical_auditor.md',
"### Mô hình 2: Hội Đồng Phản Biện Đối Trọng 3 Lăng Kính (The Tri-Adversarial Red Team Council)\nTrước khi phê duyệt bất kỳ luận điểm hay phân cảnh nào, Kiểm toán viên bắt buộc phải kích hoạt 3 \"quái kiệt phản biện\":\n1. **The Market Skeptic (Kẻ Hoài Nghi Thị Trường & Hiệu Quả Vốn):**\n   * *Mũi khoan:* Tấn công vào các giải pháp trợ cấp hành chính, độc quyền nhóm, nguy cơ lãng phí vốn và chi phí cơ hội bị tước đoạt của khu vực tư nhân.\n2. **The Institutional Realist (Nhà Hiện Thực Thể Chế & Địa Chính Trị):**\n   * *Mũi khoan:* Vạch trần sự lệch pha giữa văn bản luật và năng lực thực thi thực tế, động lực sinh tồn của các nhóm lợi ích, và nguy cơ kích hoạt các biện pháp trả đũa thuế quan/thương mại.\n3. **The Forensic Cash Auditor (Kiểm Toán Viên Dòng Tiền & Rủi Ro Phá Sản):**\n   * *Mũi khoan:* Bóc trần thâm hụt dòng tiền tự do (FCF âm), bẫy lấy nợ ngắn hạn nuôi tài sản dài hạn, tính bất khả thi của công suất hòa vốn và nguy cơ cạn kiệt thanh khoản khi lãi suất đảo chiều.",
"### Mô hình 2: Hội Đồng Phản Biện Đa Diện (Multi-Lens Red Team)\nTrước khi phê duyệt luận điểm, Kiểm toán viên kích hoạt các lăng kính phản biện **đã chọn trong hiến chương tập** (tối thiểu 2). Danh mục 5 lăng kính và điều kiện bật lăng kính dòng tiền: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\" (bản gốc duy nhất). Kiểm toán viên không tự thêm lăng kính dòng tiền cho đề tài chiến lược, thể chế, công nghiệp chỉ vì có số tài chính (WO-00 Q10).", "Q10")
R('.agents/personas/the_dialectic_architect.md',
"  * **Cao trào Màn 2 (`[THE DEVIL'S CHAPTER]`):** Đây là tâm chấn của Phản đề, nơi kịch bản kích hoạt Ban Phản Biện Đối Trọng 3 Lăng Kính (Tri-Adversarial Red Team):\n    1. *The Market Skeptic:* Lãng phí vốn, bóp méo giá cả, chi phí cơ hội bị tước đoạt của nền kinh tế.\n    2. *The Institutional Realist:* Động lực sinh tồn của nhóm lợi ích, sự lệch pha giữa văn bản luật và thực địa, rủi ro trả đũa địa chính trị.\n    3. *The Forensic Cash Auditor:* Thâm hụt dòng tiền tự do (FCF âm), bẫy lấy nợ ngắn hạn nuôi tài sản dài hạn, tính bất khả thi của công suất hòa vốn.",
"  * **Cao trào Màn 2 (`[THE DEVIL'S CHAPTER]`):** tâm chấn của Phản đề, nơi kịch bản kích hoạt các lăng kính phản biện đã chọn trong hiến chương tập (danh mục và điều kiện: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\").", "Q10")
R('.agents/skills/script_architect/SKILL.md',
"do Hội đồng Phản biện Đối trọng 3 Lăng Kính (Market Skeptic, Institutional Realist, Forensic Cash Auditor) trực tiếp tra vấn.",
"do Hội đồng Phản biện Đa diện tra vấn bằng các lăng kính đã chọn trong hiến chương tập (danh mục: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\").", "Q10")
R('.agents/skills/chapter_writer/SKILL.md',
"(dựa trên 1 trong 3 lăng kính: Thị trường / Thể chế / Dòng tiền).","(dựa trên một lăng kính đã chọn trong hiến chương tập; danh mục: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\").","Q10")
# template outline
f='02_templates/masterpiece_pipeline/07_outline_template.md'
R(f,"[Thách thức từ 1 trong 3 lăng kính Thị trường / Thể chế / Dòng tiền đối với giả định khởi nguồn]","[Thách thức từ một lăng kính đã chọn trong hiến chương tập đối với giả định khởi nguồn]","Q10")
R(f,"[Chỉ định 1 lăng kính đối kháng: The Market Skeptic HOẶC The Institutional Realist HOẶC The Forensic Cash Auditor]","[Chỉ định 1 lăng kính đối kháng trong số các lăng kính đã chọn ở hiến chương tập]","Q10")
R(f,"kích hoạt **Hội đồng Phản biện Đa diện (Tri-Adversarial Red Team)** ở phiên bản Steelman mạnh nhất. Tấn công trực diện vào tính khả thi, sự bền vững và tính chính danh của mô hình hiện tại qua 3 mũi nhọn:\n  1. *The Market Skeptic:* Bóc trần méo mó phân bổ vốn, bao cấp làm lệch lạc thị trường, nguy cơ tạo zombie enterprises.\n  2. *The Institutional Realist:* Bóc trần ma sát hành chính, xung đột lợi ích cố thủ, rủi ro đối đầu chính sách và trả đũa quốc tế.\n  3. *The Forensic Cash Auditor:* Soi bảng cân đối tài chính, dòng tiền tự do FCF âm, lấy nợ ngắn hạn nuôi tài sản dài hạn, điểm hòa vốn viển vông.",
"kích hoạt **Hội đồng Phản biện Đa diện** ở phiên bản Steelman mạnh nhất, qua các lăng kính đã chọn trong hiến chương tập (tối thiểu 2; danh mục: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\"). Mỗi mũi nhọn ghi: lăng kính, bằng chứng đối kháng (mã mắt xích), và luận điểm chính phải đổi gì nếu mũi nhọn đứng vững.","Q10")
R(f,"- **Mỏ neo vật lý (Physical Anchor):** [Báo cáo kiểm toán chỉ trích, bảng cân đối thâm hụt, hình ảnh hiện trường đối lập...].","- **Mỏ neo vật lý (Physical Anchor):** [Văn bản, quyết định, số liệu đối kháng có nguồn; không bịa chi tiết].","Q10")
R(f,"[Tấn công đồng thời cả 3 lăng kính: Thị trường, Thể chế và Dòng tiền]","[Tấn công đồng thời bằng mọi lăng kính đã chọn trong hiến chương tập]","Q10")
# 4. hook_engine biến thể 2
R('.agents/skills/hook_engine/SKILL.md',
"*   **Biến thể 2 (The Forensic Balance Sheet Collision — Va Chạm Bảng Cân Đối):**  \n    Đặt hai triết lý tài chính và hai mô hình tư bản đối lập cạnh nhau $\\rightarrow$ Dùng các con số kiểm toán thực chứng để làm lộ ra sự đánh đổi $\\rightarrow$ Đặt ra câu hỏi về chiếc bẫy lây nhiễm và bài toán dòng tiền.",
"*   **Biến thể 2 (The Two-Model Collision — Va Chạm Hai Mô Hình):**  \n    Đặt hai cách làm đối lập cạnh nhau (hai chiến lược, hai mô hình vận hành, hai luật chơi) $\\rightarrow$ Dùng dữ kiện có nguồn để làm lộ ra sự đánh đổi của mỗi bên $\\rightarrow$ Đặt câu hỏi: ai trả giá, và điều gì quyết định bên nào đứng vững. Chỉ dùng số tài chính khi đề tài là tài chính (WO-00 Q10).","R2")
# 5. retention gate
f='00_core/retention_gate_checklist.md'
R(f,"Loại B: Áp lực chi phí & chuỗi giá trị;","Loại B: bài toán doanh nghiệp/quốc gia (cơ chế vận hành, cạnh tranh, thể chế, chuỗi giá trị);","R2")
R(f,"  - *Loại B (Doanh nghiệp/Kinh tế ngành):* Có phân tích rõ áp lực chi phí, dòng tiền, biên lợi nhuận hoặc bài toán sinh tồn của doanh nghiệp/người tiêu dùng.",
"  - *Loại B (Doanh nghiệp/Kinh tế ngành):* Có phân tích rõ bài toán cơ chế của doanh nghiệp/quốc gia (cạnh tranh, thể chế, chuỗi giá trị, đánh đổi chiến lược); chi phí, dòng tiền chỉ khi đề tài là tài chính (WO-00 Q10).","R2")
# 6. rubric
R('00_core/masterpiece_quality_standard.md',"đều phải được giải thích bằng bài toán lợi ích, rủi ro, điểm hòa vốn và dòng tiền.","đều phải được giải thích bằng động lực lợi ích, rủi ro, chi phí cơ hội và đánh đổi (dòng tiền, điểm hòa vốn chỉ khi đề tài là tài chính).","R2")
R('00_core/chapter_quality_standard.md',"    *   Giải thích mọi hiện tượng bằng động lực lợi ích, chi phí và điểm hòa vốn, không phán xét đạo đức cảm tính.","    *   Giải thích mọi hiện tượng bằng động lực lợi ích, chi phí cơ hội và đánh đổi, không phán xét đạo đức cảm tính.","R2")
# 7. build_outline Loại B Ch.2
R('.agents/workflows/build_outline.md',"Chương 2 = Cơ chế chi phí và lớp phân tích logic tiếp theo (KHÔNG ép túi tiền cá nhân);","Chương 2 = bài toán doanh nghiệp/quốc gia (cơ chế vận hành, cạnh tranh, thể chế) và lớp phân tích logic tiếp theo (KHÔNG ép túi tiền cá nhân);","R2")
# 8. golden_hook #5
f='00_core/golden_samples/golden_hook.md'
R(f,"### 5. Gắn túi tiền / đời sống cá nhân\nHook phải có ít nhất 1 cụm kết nối với đời sống thật: tiền, lãi vay, giá nhà, việc làm, khoản vay, tài sản, quyết định mua bán. Không có cụm này → người xem không thấy lý do ở lại.",
"### 5. Điểm tựa liên quan theo loại đề tài\nHook phải có ít nhất 1 điểm tựa cho thấy lý do ở lại, chọn theo `00_core/content_principles.md` §2: Loại A là đời sống chung (thu nhập, chi phí, việc làm, tài sản); Loại B là bài toán doanh nghiệp/quốc gia (ai thắng ai thua, luật chơi nào đang đổi); Loại C là nghịch lý hoặc cú sốc dữ liệu. Không ép \"túi tiền của bạn\" vào đề tài B/C.","R2")
R(f,"[ ] Có gắn túi tiền / đời sống thật?","[ ] Có điểm tựa liên quan đúng loại đề tài A/B/C?","R2")
# 9. longform §2, §15
f='00_core/longform_blueprint.md'
R(f,"## 2. Nguyên tắc nền: PERSONAL-FIRST\nLong-form mạnh không đến từ sự sâu sắc của chuyên gia.\nNó mạnh ở chỗ người xem **thấy mình** trong video ngay từ đầu.",
"## 2. Nguyên tắc nền: ĐIỂM TỰA LIÊN QUAN SỚM (theo loại đề tài)\nLong-form mạnh không đến từ sự sâu sắc của chuyên gia.\nNó mạnh ở chỗ người xem thấy **lý do để ở lại** ngay từ đầu: với Loại A là thấy mình; với Loại B là thấy một bài toán doanh nghiệp/quốc gia đáng theo; với Loại C là một nghịch lý chưa có lời giải. Luật gốc: `00_core/content_principles.md` §2.","R2")
R(f,"### Nguyên tắc Personal-First (LINH HOẠT theo chủ đề)\nMục tiêu cốt lõi KHÔNG THAY ĐỔI: người xem phải thấy mình liên quan trong 5 phút đầu.",
"### Điểm tựa liên quan (LINH HOẠT theo chủ đề)\nMục tiêu cốt lõi KHÔNG THAY ĐỔI: người xem phải thấy lý do ở lại trong 5 phút đầu.","R2")
R(f,"> - **Loại A và B:** Không bao giờ để quá 4 phút video mà không có ít nhất 1 câu kéo về đời sống cá nhân người xem (Zoom-In). Personal Stakes là nhịp thở xuyên suốt, không phải hộp cứng.",
"> - **Loại A:** Không để quá 4 phút mà không có ít nhất 1 câu kéo về đời sống chung của người xem (Zoom-In bằng lăng kính phổ quát).\n> - **Loại B:** Không để quá 4 phút mà không có ít nhất 1 điểm neo bài toán doanh nghiệp/quốc gia (ai trả giá, luật chơi đổi thế nào, đối thủ phản ứng ra sao). KHÔNG ép đời sống cá nhân.","R2")
R(f,"> Nếu video là Loại A hoặc B → dùng Personal-First doctrine tiêu chuẩn (Section 5).","> Nếu video là Loại A hoặc B → dùng điểm tựa liên quan theo loại (§2 và §3).","R2")
R(f,"- giúp người nghe thấy mình trong vấn đề **ngay từ phút 2** (Loại A/B) hoặc thấy tò mò đủ để ở lại (Loại C),",
"- giúp người nghe thấy lý do ở lại **ngay từ phút 2**: thấy mình trong vấn đề (Loại A), thấy một bài toán doanh nghiệp/quốc gia đáng theo (Loại B), hoặc một nghịch lý chưa có lời giải (Loại C),","R2")
R(f,"- và giúp người nghe rời video với một cách đọc mới **và một bước hành động cụ thể** (Loại A/B) hoặc một góc nhìn mới về thế giới (Loại C).",
"- và giúp người nghe rời video với một cách đọc mới: Loại A có thể kèm khung tự định vị; Loại B kèm bài học chiến lược và cái giá đã trả; Loại C kèm góc nhìn mới về thế giới. Không lời khuyên hành động cho B/C.","R2")
R(f,"- **Loại A/B:** Nếu một người xem chỉ ở lại 5 phút đầu, họ đã thấy video này nói về CHÍNH HỌ chưa? Nếu chưa — kịch bản đã thất bại.",
"- **Loại A:** Nếu một người xem chỉ ở lại 5 phút đầu, họ đã thấy video này nói về CHÍNH HỌ chưa? Nếu chưa — kịch bản đã thất bại.\n- **Loại B:** Nếu chỉ ở lại 5 phút đầu, họ đã thấy bài toán doanh nghiệp/quốc gia nào đang được đặt ra, và vì sao chưa có đáp án? Nếu chưa — kịch bản đã thất bại.","R2")

errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {tag} {f}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
