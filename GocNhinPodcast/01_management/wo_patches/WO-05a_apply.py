import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append((f,old,new,tag))
SA="`.agents/skills/script_architect/SKILL.md` §1"
# A. script_architect §1 = bản gốc duy nhất của luật cấu trúc (Q13): thêm mục 7–9
R('.agents/skills/script_architect/SKILL.md',
"6. **Thích Ứng Bản Thể Học Đa Hình Thái (Polymorphic Adaptation Heuristic):**\n   - Cấu trúc kịch bản phải tuân theo đúng hình thái của chủ thể (Thể chế, Ý niệm, Xã hội, Không gian, Doanh nghiệp/Vốn), không gượng ép mọi đề tài vào một khuôn mẫu máy móc.",
"6. **Thích Ứng Bản Thể Học Đa Hình Thái (Polymorphic Adaptation Heuristic):**\n   - Cấu trúc kịch bản phải tuân theo đúng hình thái của chủ thể (Thể chế, Ý niệm, Xã hội, Không gian, Doanh nghiệp/Vốn), không gượng ép mọi đề tài vào một khuôn mẫu máy móc.\n7. **Steelman & Tam Đoạn Luận 3 Nhịp:** phản đề luôn ở dạng mạnh nhất của phe đối lập, có dữ kiện đối kháng; cấm bù nhìn rơm và phản biện hình thức một câu. Mỗi luận điểm then chốt đi qua 3 nhịp: (1) công kích bằng dữ kiện đối kháng, (2) thừa nhận cái lý và áp lực sinh tồn của phe phản biện, (3) hợp đề bằng quy luật khách quan và thừa nhận đánh đổi (`admitted_trade_offs`). Thủ tục viết và khẩu ngữ: `.agents/skills/chapter_writer/SKILL.md` §2.1. Lăng kính phản biện: theo hiến chương tập (`.agents/AGENTS.md` mục \"Thể Chế Hóa Hội Đồng Phản Biện Đa Diện\").\n8. **Đánh đổi & Kết luận có điều kiện:** mọi mô hình, chính sách, chiến lược phải chỉ rõ ai hưởng lợi, ai gánh chi phí, chi phí cơ hội và hệ lụy phụ 3–5 năm; cấm kết luận nhị nguyên tốt-xấu; kết luận đi kèm điều kiện ràng buộc (thể chế, nguồn lực, bối cảnh) và điều kiện có thể sai (`00_core/stance_and_judgment.md` §6).\n9. **Đối xứng 1-1 (Symmetric Parity):** khi so sánh đa chủ thể, độ sâu dữ kiện, cơ chế và tử huyệt của mỗi bên phải ngang nhau; cấm \"bên dày bên mỏng\".\n\n> Đây là bản gốc duy nhất của luật cấu trúc (user chốt 02/10/2026, WO-00 Q13). Persona và rule khác chỉ trỏ về đây, không chép lại.","Q13")
# B. AGENTS.md §4 ba gạch đầu lặp → trỏ
R('.agents/AGENTS.md',
"- **Quy chuẩn Steelmanning & Cấm Tuyệt Đối Ngụy Biện Bù Nhìn Rơm (Anti-Strawman Rule):**\n  * Tuyệt đối CẤM dựng lên những luận điểm đối lập ngây thơ, yếu ớt để dễ bề bác bỏ. Phản đề BẮT BUỘC phải được xây dựng ở phiên bản thông minh, sắc bén và giàu dữ liệu thực chứng nhất của phe đối lập.\n- **Bắt Buộc Có [THE DEVIL'S CHAPTER] Tại Cao Trào Hồi 2:**\n  * Kịch bản BẮT BUỘC phải dành riêng 1 chương độc lập (50–70% thời lượng, chiếm 18–24% ngân sách từ) mang nhãn `[THE DEVIL'S CHAPTER — CHƯƠNG PHẢN ĐỀ BẢN CHẤT]` để dồn nén toàn bộ phản đề thép, thử lửa toàn diện Chính đề.\n- **Tam Đoạn Luận Phản Biện 3 Nhịp (The 3-Beat Steelmanning Mandate):**\n  * Mọi phân tích luận điểm then chốt bắt buộc đi qua 3 nhịp: (1) Công kích Phản đề Thép bằng số liệu đối kháng $\\rightarrow$ (2) Thừa nhận cái lý và áp lực sinh tồn khách quan của phe phản biện $\\rightarrow$ (3) Hợp đề bằng quy luật khách quan và công khai thừa nhận sự đánh đổi cấu trúc (`admitted_trade_offs`).",
"- **Luật cấu trúc đi kèm** (Steelman, 3 nhịp, Devil's Chapter ở cao trào Hồi 2, đánh đổi, kết luận có điều kiện, đối xứng 1-1): bản gốc duy nhất ở "+SA+" (Q13). Vị trí và tỷ trọng Devil's Chapter là hằng số mục 5 ở đầu file này.","Q13")
# C. content-os-pipeline §4 bốn gạch lặp → trỏ
R('.agents/rules/content-os-pipeline.md',
"    *   **Bắt Buộc Có [THE DEVIL'S CHAPTER] Tại Cao Trào Hồi 2:** Cấu trúc Outline BẮT BUỘC dành 1 chương độc lập (50–70% thời lượng, chiếm 18–24% ngân sách từ) mang nhãn `[THE DEVIL'S CHAPTER — CHƯƠNG PHẢN ĐỀ BẢN CHẤT]`. Chương này đứng hẳn về phía phe đối lập ở phiên bản Steelman mạnh nhất, dồn toàn bộ dữ liệu đối kháng để thử lửa luận điểm chính.\n    *   **Tam Đoạn Luận Phản Biện 3 Nhịp (The 3-Beat Steelmanning Mandate):** Tuyệt đối CẤM ngụy biện bù nhìn rơm (Strawman) hoặc phản biện hình thức (*\"Tuy nhiên, một số ý kiến cho rằng X, nhưng thực tế là Y\"*). Mọi luận điểm chính BẮT BUỘC triển khai qua 3 nhịp: (1) Công kích Phản đề Thép bằng dữ liệu đối kháng sắc sảo nhất, (2) Thừa nhận động lực sinh tồn và tính chính đáng của bên phản biện, (3) Hợp đề bằng quy luật khách quan và công khai thừa nhận sự đánh đổi cấu trúc (`admitted_trade_offs`).\n    *   **Bắt Buộc Phân Tích Đánh Đổi (Trade-offs) & Chi Phí Cơ Hội (Opportunity Costs):** Mọi phân tích mô hình, chính sách hoặc chiến lược đều PHẢI chỉ rõ: Ai đang hưởng lợi vs Ai đang âm thầm gánh chịu chi phí/rủi ro? Chi phí cơ hội của quốc gia/xã hội là gì? Hệ lụy phụ (Unintended Consequences) trong 3–5 năm tới là gì?\n    *   **Kết Luận Có Điều Kiện (Conditional Conclusion):** Tuyệt đối CẤM kết luận nhị nguyên đen-trắng (người tốt - kẻ xấu, đúng tuyệt đối - sai tuyệt đối). Mọi kết luận đều phải đi kèm các điều kiện ràng buộc về thể chế, nguồn vốn và bối cảnh quốc tế.",
"    *   **Luật cấu trúc** (Devil's Chapter, Steelman 3 nhịp, đánh đổi, kết luận có điều kiện, đối xứng 1-1): bản gốc duy nhất ở "+SA+" (Q13); không chép lại ở đây.","Q13")
# D. the_dialectic_architect: Mô hình 2–6 → trỏ (giữ Mô hình 1 Hegel vì là lăng kính riêng của persona)
f='.agents/personas/the_dialectic_architect.md'
old_d=open(os.path.join(ROOT,f)).read()
i=old_d.find("### Mô hình 2: Bài Test \"So What?\""); j=old_d.find("---\n\n## 4. Vùng Cấm Tuyệt Đối")
assert i>0 and j>i, "dialectic block"
R(f,old_d[i:j],"### Mô hình 2–6: Luật cấu trúc dùng chung\nSo What Test, Therefore/But, Payoff Void, Anti-Burying-The-Lede, Steelman & đánh đổi: bản gốc duy nhất ở "+SA+" (Q13). Persona này áp các luật đó khi dựng Tam hồi Hegel ở Mô hình 1; không định nghĩa lại.\n\n","Q13")
# E. the_editorial_strategist §B, §C → trỏ
f='.agents/personas/the_editorial_strategist.md'
old_e=open(os.path.join(ROOT,f)).read()
i=old_e.find("### B. Quy Luật Động Lực Nhân Quả"); j=old_e.find("---\n\n## 3. Ba Trọng Tài")
assert i>0 and j>i, "editorial block"
R(f,old_e[i:j],"### B–C. Therefore/But và Búp bê Nga\nLuật nhân quả Therefore/But (0% \"và rồi\") và cấu trúc búp bê Nga 4 tầng (bề mặt → cơ chế → điểm gãy ở cao trào Màn 2 → chuyển hóa): bản gốc duy nhất ở "+SA+" (Q13). Persona này dùng chúng để giữ sợi chỉ đỏ (§A), không định nghĩa lại.\n\n","Q13")
# F. the_narrative_director Mô hình 2 → trỏ
R('.agents/personas/the_narrative_director.md',
"### Mô hình 2: Tam Đoạn Luận Phản Biện 3 Nhịp (The 3-Beat Dialectical Syllogism)\nMỗi phân đoạn phân tích xung đột trong từng chương phải được cấu trúc theo 3 nhịp biện chứng:\n- **Nhịp 1 — Bộc Lộ Phản Đề Đanh Thép (Steelman Attack):** Nêu lập luận mạnh nhất, sắc bén nhất của phe phản biện kèm số liệu thực chứng rực lửa. Không dùng \"bù nhìn rơm\" để tự trấn an.\n- **Nhịp 2 — Thấu Cảm Động Lực Sinh Tồn (Survival Incentives):** Lý giải vì sao chủ thể lại hành động như vậy. Đặt mình vào áp lực sống còn, ràng buộc thể chế và bài toán chi phí cơ hội tại thời điểm họ ra quyết định.\n- **Nhịp 3 — Hợp Đề Giải Phẫu & Đánh Đổi Sòng Phẳng (Synthesis & Admitted Trade-Offs):** Phân tích hệ thống qua quy luật khách quan, chỉ ra cái giá phải trả và sự đánh đổi bắt buộc (`admitted_trade_offs`), không đưa ra các giải pháp màu hồng phi vật lý.",
"### Mô hình 2: Tam Đoạn Luận Phản Biện 3 Nhịp\nNguyên tắc: "+SA+" mục 7 (Q13). Thủ tục viết và khẩu ngữ gợi ý: `.agents/skills/chapter_writer/SKILL.md` §2.1. Persona này lo nhịp nghe của ba nhịp đó, không định nghĩa lại nội dung.","Q13")
# G. the_critical_auditor Khóa 2–4 thân → trỏ
f='.agents/personas/the_critical_auditor.md'
R(f,"   - Lập luận của phe phản biện phải ở phiên bản mạnh nhất và có dữ liệu sắc bén nhất.\n   - Thừa nhận sòng phẳng sự đánh đổi (`admitted_trade_offs`): Không có giải pháp hoàn hảo miễn phí.\n   - Bảo đảm độ sâu đối xứng 1-1 giữa các chủ thể đối kháng trên bàn cờ.",
"   - Kiểm theo "+SA+" mục 7–9 (Steelman, đánh đổi, đối xứng 1-1).","Q13")
R(f,"   - 100% các chương phải phục vụ Biến cố trung tâm.\n   - 0% cấu trúc \"And Then\" (liệt kê ngăn tủ vô hồn) hoặc niên biểu hành chính chán ngắt. Mọi chuyển đoạn phải là động lực nhân quả \"Vì vậy...\" [THEREFORE] hoặc \"Nhưng...\" [BUT].",
"   - Kiểm theo "+SA+" mục 3 (Therefore/But) và Single Spine; cấm niên biểu hành chính mở màn.","Q13")
R(f,"   - Cao trào Màn 2 (`[THE DEVIL'S CHAPTER]`) phải chứa đựng điểm gãy cấu trúc lớn nhất. Cấm giấu nút thắt xuống 2 phút cuối.",
"   - Kiểm theo "+SA+" mục 5 (Anti-Burying-The-Lede) và hằng số Devil's Chapter (`.agents/AGENTS.md` mục 5).","Q13")
# H. câu gắn model
R('.agents/AGENTS.md',"Gemini 3.8 Flash có xu hướng hành văn trang trọng, lý tính. Do đó, ngay từ khâu viết nháp,","Model viết thường trượt về văn trang trọng, lý tính. Do đó, ngay từ khâu viết nháp,","model")
R('.agents/rules/content-os-pipeline.md',"Gemini 3.8 Flash có xu hướng hành văn lý tính, kỹ trị và trang trọng nếu không được định hướng phong cách ngay từ đầu.","Model viết thường trượt về văn lý tính, kỹ trị và trang trọng nếu không được định hướng phong cách ngay từ đầu.","model")
R('.agents/skills/chapter_writer/SKILL.md',"ngăn chặn hoàn toàn tật viết hàn lâm/báo cáo của Gemini 3.8 Flash.","ngăn tật viết hàn lâm/báo cáo của model.","model")
R('.agents/skills/chapter_writer/SKILL.md',"Gemini 3.8 Flash tận dụng khối suy luận ngầm (Thinking Process) để tự động rà soát bản nháp dựa trên 14 tiêu chí vàng trước khi xuất tệp:","Người viết rà soát bản nháp theo 14 tiêu chí dưới đây trước khi xuất tệp (cổng chấm chính thức do người khác và cổng máy thực hiện, xem WO-10):","model")
R('02_templates/llm_error_log_template.md',"*Gemini 3.8 Flash / the_industrial_economist*","*[model] / the_industrial_economist*","model")
R('02_templates/llm_error_log_template.md',"[Ví dụ: Gemini 3.8 Flash (High) + the_industrial_economist]","[Ví dụ: [model] + the_industrial_economist]","model")
errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {tag} {f}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
