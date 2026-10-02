import sys,os,glob
ROOT=sys.argv[1]; E=[]
P="/Users/pro16/Documents/VideoProject/GocNhinPodcast/"
E.append(('.agents/workflows/merge_voiceover.md',"## 🛑 HARD GATE ĐẦU VÀO BẮT BUỘC",
f"## 🛑 HARD GATE PERSONA\n\nTrước khi thực thi, agent PHẢI đọc lần lượt (khớp Pre-flight và bảng pha Pha 8; kiểm bằng `scripts/kiem_dna.py --persona`):\n\n1. `{P}.agents/personas/the_quality_czar.md`\n2. `{P}.agents/personas/the_voice_architect.md`\n3. `{P}.agents/skills/chapter_writer/SKILL.md`\n\n## 🛑 HARD GATE ĐẦU VÀO BẮT BUỘC",False))
V=[("BẮT BUỘC PHẢI DÙNG TOOL `view_file` để đọc","BẮT BUỘC PHẢI ĐỌC"),("(Mandatory Inputs via `view_file`)","(Mandatory Inputs)"),("`view_file` → `","`"),
   ("chưa từng gọi `view_file` nạp","chưa đọc"),("bắt buộc phải gọi `view_file` nạp vào ngữ cảnh","bắt buộc phải đọc vào ngữ cảnh"),("Tài liệu nạp trực tiếp qua view_file","Tài liệu nạp trực tiếp"),
   ("Dùng tool `view_file` đọc","Đọc"),("đọc bằng view_file","đọc"),("dùng `view_file` rà soát","rà soát"),("PHẢI dùng `view_file` đọc","PHẢI đọc"),("gọi `view_file`","đọc"),("`view_file`","đọc trực tiếp")]
for f in glob.glob(os.path.join(ROOT,'.agents','**','*.md'),recursive=True):
    if '/tools/' in f: continue
    if 'view_file' in open(f).read():
        for a,b in V: E.append((os.path.relpath(f,ROOT),a,b,True))
errs=0;done=0
for f,old,new,multi in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if multi:
        if n==0: continue
    elif n!=1: print(f"LỖI {f}: {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); done+=1; print(f"OK {f}: {old[:38]!r} x{n}")
print("số sửa:",done,"lỗi:",errs); sys.exit(1 if errs else 0)
