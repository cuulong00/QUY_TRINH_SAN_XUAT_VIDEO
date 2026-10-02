import sys,os,glob,re
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag,multi=False): E.append((f,old,new,tag,multi))
P="/Users/pro16/Documents/VideoProject/GocNhinPodcast/"
# Q9: init_episode thành tệp trỏ, build_global_vision là workflow Pha 1 duy nhất
INIT="""# /init_episode — Tạo thư mục tập (tệp trỏ)

Workflow tư duy của Pha 1 (bàn cờ, giả thuyết, bản đồ nền từ kho) nằm **duy nhất** ở `.agents/workflows/build_global_vision.md` (user chốt 02/10/2026, WO-00 Q9). File này chỉ còn việc tạo thư mục.

## Các bước
1. Hỏi episode slug nếu chưa có.
2. Nếu `episodes/[slug]` chưa tồn tại, copy `02_templates/episode_template/` vào `episodes/[slug]`; thay toàn bộ placeholder `__EPISODE_SLUG__` bằng slug thực.
3. Thêm dòng cho tập vào `01_management/episode_registry.csv` (bằng Edit/Write, không bằng Bash) và tạo `episodes/[slug]/00_pipeline_operator_log.md` theo `.agents/rules/operator-visibility.md`.
4. Chạy `/build_global_vision` để làm Pha 1. Không tạo `01_global_vision_synthesis.md` từ file này.
"""
E.append(('.agents/workflows/init_episode.md',None,INIT,"Q9",'W'))
R('.agents/rules/content-os-pipeline.md',"| `/init_episode` (Strategy Council — Bàn cờ 4 Tầng","| `/build_global_vision` (Strategy Council — Bàn cờ 4 Tầng","Q9")
R('.agents/rules/content-os-pipeline.md',"| 8. Merge Voiceover | `voiceover.md` | `the_quality_czar` |","| 8. Merge Voiceover | `voiceover.md` | `the_quality_czar` + `the_voice_architect` |","persona")
# hook_lab: hard gate khớp pre-flight và bảng pha (viral_alchemist + critical_auditor)
R('.agents/workflows/hook_lab.md',
f"1. `{P}.agents/skills/hook_engine/SKILL.md`\n2. `{P}.agents/personas/the_macro_strategist.md`\n\nNGHIÊM CẤM tạo bất kỳ hook hay output nào nếu chưa hoàn thành việc đọc cả hai file trên.",
f"1. `{P}.agents/personas/the_viral_alchemist.md`\n2. `{P}.agents/personas/the_critical_auditor.md`\n3. `{P}.agents/skills/hook_engine/SKILL.md`\n\nNGHIÊM CẤM tạo bất kỳ hook hay output nào nếu chưa hoàn thành việc đọc cả ba file trên. (Danh sách này phải khớp persona khai báo ở Pre-flight và bảng pha `content-os-pipeline.md`; kiểm bằng `scripts/kiem_dna.py --persona`.)","persona")
R('.agents/skills/hook_engine/SKILL.md',
"> 1. `the_viral_alchemist` (Master Attention Architect & Packaging Dramaturg — Bản ngã nhận thức sắc bén, trực giác va đập khái niệm)\n> 2. `the_narrative_director` (Cảm thức thẩm mỹ âm thanh, nhịp điệu phát thanh, duy trì Sợi Chỉ Đỏ)\n> 3. `the_critical_auditor` (Giám sát tính liêm chính của dữ liệu thực chứng và rào cản ZUI)",
"> 1. `the_viral_alchemist` (Master Attention Architect & Packaging Dramaturg — Bản ngã nhận thức sắc bén, trực giác va đập khái niệm)\n> 2. `the_critical_auditor` (Giám sát tính liêm chính của dữ liệu thực chứng và rào cản ZUI)\n> (Nhịp điệu nói và Sợi chỉ đỏ: áp theo `00_core/voice_dna.md`; không cần hóa thân thêm persona thứ ba, để khớp bảng pha Pha 5.)","persona")
# build_outline: hard gate khớp pre-flight (editorial + dialectic + critical) + skill
R('.agents/workflows/build_outline.md',
f"1. `{P}.agents/personas/the_macro_strategist.md`\n2. `{P}.agents/personas/the_narrative_director.md`\n3. `{P}.agents/skills/script_architect/SKILL.md`\n\nNGHIÊM CẤM tạo bất kỳ outline, thesis map, hay chapter brief nào nếu chưa đọc đủ 3 file trên.",
f"1. `{P}.agents/personas/the_editorial_strategist.md`\n2. `{P}.agents/personas/the_dialectic_architect.md`\n3. `{P}.agents/personas/the_critical_auditor.md`\n4. `{P}.agents/skills/script_architect/SKILL.md`\n\nNGHIÊM CẤM tạo bất kỳ outline, thesis map, hay chapter brief nào nếu chưa đọc đủ 4 file trên. (Danh sách khớp Pre-flight và bảng pha Pha 4; kiểm bằng `scripts/kiem_dna.py --persona`.)","persona")
# bỏ chữ gắn IDE "dùng tool `view_file`"
for f in glob.glob(os.path.join(ROOT,'.agents','**','*.md'),recursive=True):
    if '/tools/' in f: continue
    s=open(f).read()
    if 'view_file' in s:
        rel=os.path.relpath(f,ROOT)
        R(rel,"PHẢI dùng tool `view_file` để đọc lần lượt","PHẢI đọc lần lượt","view_file",True)
        R(rel,"PHẢI dùng tool `view_file` đọc lần lượt","PHẢI đọc lần lượt","view_file",True)
        R(rel,"dùng tool `view_file`","đọc","view_file",True)
        R(rel,"bằng `view_file`","","view_file",True)
errs=0; done=0
for f,old,new,tag,mode in E:
    p=os.path.join(ROOT,f); s=open(p).read() if os.path.exists(p) else ""
    if mode=='W': open(p,'w').write(new); print(f"OK {tag} {f} (viết lại)"); done+=1; continue
    n=s.count(old)
    if mode is True:
        if n==0: continue
    elif n!=1: print(f"LỖI {tag} {f}: chuỗi cũ xuất hiện {n} lần"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print(f"OK {tag} {f} x{n}"); done+=1
print("số sửa:",done,"lỗi:",errs); sys.exit(1 if errs else 0)
