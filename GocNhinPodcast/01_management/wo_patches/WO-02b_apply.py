import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append((f,old,new,tag))
PTR="danh mục lăng kính và điều kiện bật lăng kính dòng tiền: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\" (bản gốc duy nhất, WO-00 Q10)"
f='.agents/skills/compliance_council/SKILL.md'
R(f,"- **Tri-Adversarial Red Team Council:** Tra vấn kịch bản qua 3 lăng kính:\n  1. *The Market Skeptic:* Bóc trần méo mó phân bổ vốn, bao cấp, doanh nghiệp xác sống, chi phí cơ hội.\n  2. *The Institutional Realist:* Ma sát quan liêu, nhóm lợi ích, rủi ro trả đũa thuế quan/thương mại quốc tế.\n  3. *The Forensic Cash Auditor:* Dòng tiền tự do FCF âm, nợ ngắn hạn nuôi tài sản dài hạn, điểm hòa vốn viển vông.",
"- **Hội đồng Phản biện Đa diện:** tra vấn kịch bản qua các lăng kính **đã chọn trong hiến chương tập** (tối thiểu 2); kiểm thêm: lăng kính dòng tiền có bị bật cho đề tài không phải tài chính không. "+PTR+".","Q10")
R(f,"Có phản biện Steelman mạnh mẽ qua 3 lăng kính Thị trường / Thể chế / Dòng tiền không?","Có phản biện Steelman mạnh mẽ qua các lăng kính đã chọn trong hiến chương tập không (tối thiểu 2)?","Q10")
R(f,"* **Lăng kính 1 (The Market Skeptic):** [Đạt / Cần sửa — Chi tiết]\n* **Lăng kính 2 (The Institutional Realist):** [Đạt / Cần sửa — Chi tiết]\n* **Lăng kính 3 (The Forensic Cash Auditor):** [Đạt / Cần sửa — Chi tiết]",
"* **Lăng kính đã chọn (liệt kê theo hiến chương tập, tối thiểu 2):** [Tên lăng kính — Đạt / Cần sửa — Chi tiết], ...\n* **Kiểm lăng kính dòng tiền:** [Có bật không; nếu bật, đề tài có phải doanh nghiệp/thị trường vốn và luận điểm có xoay quanh sức khỏe tài chính không]","Q10")
R('.agents/skills/strategy_council/SKILL.md',
"  * `the_critical_auditor`: **LÃNH ĐẠO BAN PHẢN BIỆN ĐỐI TRỌNG (TRI-ADVERSARIAL RED TEAM)** — Kích hoạt đồng thời 3 đòn công kích cốt tử:\n    1. *Lăng kính The Market Skeptic:* Bắt bẻ về hiệu quả vốn, lãng phí nguồn lực xã hội, bóp méo thị trường và nguy cơ tạo ra các thực thể sống bám trợ cấp.\n    2. *Lăng kính The Institutional Realist:* Bóc trần ma sát thực thi ngầm, động lực bảo vệ lợi ích cục bộ, và rủi ro trả đũa thuế quan/địa chính trị từ các đối tác quốc tế lớn.\n    3. *Lăng kính The Forensic Cash Auditor:* Soi chiếu thâm hụt dòng tiền tự do (FCF âm), bẫy lấy nợ ngắn hạn nuôi dự án dài, và tính bất khả thi của điểm hòa vốn công suất.",
"  * `the_critical_auditor`: **LÃNH ĐẠO HỘI ĐỒNG PHẢN BIỆN ĐA DIỆN** — tại Pha 1 chọn tối thiểu 2 lăng kính phản biện theo nút N5 của hồ sơ đề tài, ghi vào hiến chương tập, rồi kích hoạt đồng thời; "+PTR+". Không bật lăng kính dòng tiền cho đề tài chiến lược, thể chế, công nghiệp chỉ vì có số tài chính.","Q10")
R('00_core/quality_rubric.md',
"- **Hội Đồng Phản Biện Tam Diện (Tri-Adversarial Red Team):** Kịch bản có chịu sự thử lửa đanh thép của 3 lăng kính đối kháng:\n  1. *The Market Skeptic:* Sát hạch méo mó phân bổ vốn, bao cấp làm lệch lạc thị trường, doanh nghiệp xác sống, chi phí cơ hội vĩ mô.\n  2. *The Institutional Realist:* Bóc trần ma sát thực thi quan liêu, nhóm lợi ích cố thủ, rủi ro trả đũa thuế quan/WTO.\n  3. *The Forensic Cash Auditor:* Soi thẳng vào bảng cân đối, dòng tiền tự do FCF âm, nợ ngắn hạn nuôi tài sản dài hạn, điểm hòa vốn viển vông.",
"- **Hội Đồng Phản Biện Đa Diện:** Kịch bản có chịu thử lửa của các lăng kính đã chọn trong hiến chương tập (tối thiểu 2) không; "+PTR+".","Q10")
R('02_templates/masterpiece_pipeline/01_global_vision_synthesis_template.md',
"- **1. Phản biện Lăng kính Thị trường & Chi phí cơ hội (The Market Skeptic):** [Luận điểm phản bác mạnh nhất: Méo mó phân bổ vốn, bao cấp làm triệt tiêu cạnh tranh lành mạnh, nguy cơ tạo doanh nghiệp xác sống, chi phí cơ hội của nền kinh tế].\n- **2. Phản biện Lăng kính Thể chế & Địa chính trị (The Institutional Realist):** [Luận điểm phản bác mạnh nhất: Trắc trở thực thi bộ máy, xung đột lợi ích nội bộ, rủi ro bị điều tra chống bán phá giá / trả đũa thuế quan từ các đối tác thương mại lớn].\n- **3. Phản biện Lăng kính Kế toán Dòng tiền & Thanh khoản (The Forensic Cash Auditor):** [Luận điểm phản bác mạnh nhất: Dòng tiền hoạt động kinh doanh âm kéo dài, lấy đòn bẩy nợ vay ngắn hạn tài trợ đầu tư dài hạn, áp lực tái cấp vốn và điểm hòa vốn phi thực tế].",
"- **Lăng kính đã chọn (theo nút N5 của hồ sơ đề tài, tối thiểu 2; "+PTR+"):** [Ghi tên lăng kính và lý do chọn; lăng kính dòng tiền chỉ khi đề tài là doanh nghiệp/thị trường vốn và luận điểm xoay quanh sức khỏe tài chính].\n- **Phản biện theo từng lăng kính đã chọn:** [Mỗi lăng kính một luận điểm phản bác mạnh nhất, kèm dữ kiện đối kháng có mã OBS hoặc ghi GAP].","Q10")
R('02_templates/masterpiece_pipeline/08_chapter_briefs_template.md',
"Luận điểm phản biện mạnh nhất từ 1 trong 3 lăng kính (The Market Skeptic / The Institutional Realist / The Forensic Cash Auditor) + Con số/bằng chứng đối kháng từ Contested Ledger của Pha 2.",
"Luận điểm phản biện mạnh nhất từ một lăng kính đã chọn trong hiến chương tập (danh mục: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\") + Con số/bằng chứng đối kháng từ Contested Ledger của Pha 2.","Q10")
R('.agents/personas/the_macro_strategist.md',
"nếu chưa xây dựng được luận điểm phản biện mạnh mẽ nhất từ 3 lăng kính (*Market Skeptic*, *Institutional Realist*, *Forensic Cash Auditor*).",
"nếu chưa xây dựng được luận điểm phản biện mạnh mẽ nhất từ các lăng kính đã chọn cho đề tài (tối thiểu 2; danh mục và điều kiện: `.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\").","Q10")
R('00_core/longform_blueprint.md',"| Personal Stakes (Loại A/B) | Intellectual Stakes (Loại C) |","| Personal Stakes (Loại A) / Relevance Anchor bài toán doanh nghiệp (Loại B) | Intellectual Stakes (Loại C) |","R2")
errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {tag} {f}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
