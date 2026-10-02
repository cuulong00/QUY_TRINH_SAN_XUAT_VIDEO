import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new): E.append((f,old,new))
KR="`.agents/skills/kb_reader/SKILL.md`"
P="/Users/pro16/Documents/VideoProject/GocNhinPodcast/"
R('.agents/workflows/build_global_vision.md',f"4. `{P}.agents/skills/strategy_council/SKILL.md`\n\nNGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc nạp ngữ cảnh chuyên gia.",
f"4. `{P}.agents/skills/strategy_council/SKILL.md`\n5. `{P}.agents/skills/kb_reader/SKILL.md` (cách đọc kho khi nhận đề tài)\n\nNGHIÊM CẤM tạo bất kỳ output nào nếu chưa hoàn thành việc nạp ngữ cảnh chuyên gia.")
R('.agents/workflows/build_global_vision.md',"1. Hỏi kho theo thứ tự trong `.agents/rules/orchestration-protocol.md` mục \"Kho tri thức dùng chung\" (`kbq evidence` trước, rồi `entity`, `links`, `facts`), chạy `kbaudit`.",
"1. Đọc kho theo "+KR+": từ câu hỏi trung tâm ra thực thể (`find`), mở rộng theo cơ chế (`links 2`), rồi `evidence` → `between` → `facts <mã> <nhóm>` (không gọi trần), `grep` theo khái niệm; đầu ra dài ghi ra `research_raw/` và đọc theo đoạn; chủ động tìm dữ kiện ngược; chạy `kbaudit`.")
R('.agents/rules/orchestration-protocol.md',"## Kho tri thức dùng chung (bắt buộc, áp dụng từ 29/09/2026)\n",
"## Kho tri thức dùng chung (bắt buộc, áp dụng từ 29/09/2026)\nCách tư duy trên kho khi nhận đề tài (từ câu hỏi ra thực thể, thứ tự tra, đọc đầu ra dài, tìm dữ kiện ngược, nhiều bản lệch số, độ mới): "+KR+" — bắt buộc cho mọi agent ở Pha 1, 2, 7.\n")
R('.agents/personas/the_macro_strategist.md',"để lấy bức tranh đã có từ thế giới → khu vực → quốc gia → ngành → doanh nghiệp.",
"để lấy bức tranh đã có từ thế giới → khu vực → quốc gia → ngành → doanh nghiệp; cách đọc đúng (thứ tự tra, đọc theo đoạn, tìm dữ kiện ngược) theo "+KR+".")
R('.agents/skills/deep_researcher/SKILL.md',"> 📚 Kho tri thức dùng chung: làm theo mục \"Kho tri thức dùng chung\" trong `.agents/rules/orchestration-protocol.md` (Pha 1 hỏi kho, Pha 1b `kbaudit`, Pha 2 chỉ nghiên cứu GAP, sau Pha 2 ghi ngược vào kho).",
"> 📚 Kho tri thức dùng chung: làm theo mục \"Kho tri thức dùng chung\" trong `.agents/rules/orchestration-protocol.md` (Pha 1 hỏi kho, Pha 1b `kbaudit`, Pha 2 chỉ nghiên cứu GAP, sau Pha 2 ghi ngược vào kho). Cách đọc kho: "+KR+" (trước khi viết prompt nghiên cứu, kiểm lại bằng `kbq grep`/`facts <mã> <nhóm>` rằng kho thật sự chưa trả lời được).")
R('.agents/skills/chapter_writer/SKILL.md',"- `00_hien_chuong.md` — đề bài khóa, từ khóa đã loại, N1–N5; `00_bang_gia_thuyet.md` — giả thuyết còn đứng và mã E để trỏ thay cho chép câu",
"- `00_hien_chuong.md` — đề bài khóa, từ khóa đã loại, N1–N5; `00_bang_gia_thuyet.md` — giả thuyết còn đứng và mã E để trỏ thay cho chép câu; khi cần dữ kiện ngoài sổ, tra kho theo "+KR+" (không tra thì không viết)")
errs=0
for f,old,new in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {f}: {n} lần :: {old[:50]!r}"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print("OK",f)
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
