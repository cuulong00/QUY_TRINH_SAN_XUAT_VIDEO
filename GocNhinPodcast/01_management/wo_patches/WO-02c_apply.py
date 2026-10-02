import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag): E.append((f,old,new,tag))
R('02_templates/masterpiece_pipeline/01_global_vision_synthesis_template.md',"qua 3 lăng kính Market Skeptic, Institutional Realist, Forensic Cash Auditor...]","qua các lăng kính đã chọn cho đề tài (tối thiểu 2, xem mục 1.3)...]","Q10")
R('.agents/skills/compliance_council/SKILL.md',"[Nhận xét Steelman, 3 lăng kính, [THE DEVIL'S CHAPTER], trade-offs, đối xứng 1-1]","[Nhận xét Steelman, các lăng kính đã chọn trong hiến chương, [THE DEVIL'S CHAPTER], trade-offs, đối xứng 1-1]","Q10")
R('.agents/skills/compliance_council/SKILL.md',"số trang dữ liệu, số lượng chỉ số tài chính (FCF, đòn bẩy, biên lãi) và mức độ đào sâu nguyên nhân gốc rễ của bên thứ hai có ngang bằng bên thứ nhất không?","số dữ kiện có nguồn, số cơ chế được bóc tách và mức độ đào sâu nguyên nhân gốc rễ của bên thứ hai có ngang bằng bên thứ nhất không? (Chỉ số tài chính chỉ là một loại dữ kiện, không bắt buộc.)","R2")
R('.agents/skills/compliance_council/SKILL.md',"bảo đảm độ sâu BCTC, cơ cấu nợ, biên lợi nhuận và tử huyệt của cả hai bên đều được mổ xẻ ngang nhau.","bảo đảm độ sâu dữ kiện, cơ chế và tử huyệt của cả hai bên đều được mổ xẻ ngang nhau (BCTC, cơ cấu nợ chỉ khi đề tài là tài chính).","R2")
R('.agents/skills/script_architect/SKILL.md',"tại cao trào Màn 2 với sự kích hoạt của 3 lăng kính phản biện.","tại cao trào Màn 2 với sự kích hoạt của các lăng kính phản biện đã chọn trong hiến chương tập (tối thiểu 2).","Q10")
R('.agents/skills/strategy_council/SKILL.md',"(bắt buộc có màn phản biện 3 lăng kính gay gắt từ `the_critical_auditor`).","(bắt buộc có màn phản biện gay gắt từ `the_critical_auditor` qua các lăng kính đã chọn, tối thiểu 2).","Q10")
R('.agents/personas/the_viral_alchemist.md',
"### Engine 2: The Forensic Balance Sheet Collision (Vụ Va Chạm Của Hai Bảng Cân Đối Kế Toán)\n*   **Triết lý:** Đi thẳng vào sự đối lập tột cùng của các con số kiểm toán thực tế và các mô hình tài chính. Đặt hai triết lý tư bản cạnh nhau để làm lộ ra sự đánh đổi nghiệt ngã giữa đòn bẩy và an toàn, giữa dòng tiền phòng thủ và chiếc bẫy nợ nần.\n*   **Tâm lý tiếp nhận:** Kích thích tò mò trí tuệ sâu sắc của giới quan sát tài chính và những bộ óc kinh doanh thông minh.",
"### Engine 2: The Two-Model Collision (Vụ Va Chạm Của Hai Mô Hình)\n*   **Triết lý:** Đặt hai cách làm đối lập cạnh nhau (hai chiến lược, hai mô hình vận hành, hai luật chơi) để làm lộ ra sự đánh đổi của mỗi bên bằng dữ kiện có nguồn. Số tài chính chỉ là một loại dữ kiện, dùng khi đề tài là tài chính (WO-00 Q10).\n*   **Tâm lý tiếp nhận:** Kích thích tò mò của người thích nhìn hệ thống: ai trả giá, và điều gì quyết định bên nào đứng vững.","R2")
errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {tag} {f}")
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
