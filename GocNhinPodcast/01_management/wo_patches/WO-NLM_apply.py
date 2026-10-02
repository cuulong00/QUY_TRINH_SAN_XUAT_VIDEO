import sys,os,re
ROOT=sys.argv[1]; E=[]
def R(f,old,new): E.append(('R',f,old,new))
def B(f,start,end,new): E.append(('B',f,start,end,new))   # thay khối từ dòng chứa start tới trước dòng chứa end
ENG="`scripts/kg_registry/kb_research_run.py`"
WHY=("Nạp nguồn và trích xuất của Pha 2 chạy qua **engine Direct RPC dùng chung** "+ENG+" (gọi `NotebookLMClient` trực tiếp). "
     "Cách dùng nằm ở docstring đầu file: viết một file kế hoạch `01_management/kg_research/kb_plans/<slug>.json` (nguồn = prompt nạp, mỗi nguồn ghi mã ô/GAP; trích xuất = câu hỏi, mỗi câu một file vault), rồi chạy engine. "
     "Vì sao không gọi CLI từng lệnh: engine dùng lại `.notebook_id`, ghi `run_state.json` nên bị ngắt thì chạy lại là làm tiếp, chờ nghiên cứu sâu không bị cắt lượt, và vault ra đúng khuôn (bảng số trích dẫn) để nạp kho sau này. "
     "CLI `notebooklm` chỉ dùng cho kiểm tra lẻ: `auth check`, `list`, `source list`. Chạy cần `BypassSandbox: true`.")
# deep_researcher Bước 1 + Bước 2 (khối lệnh CLI)
B('.agents/skills/deep_researcher/SKILL.md',"### Bước 1: DEEP INGESTION (Nạp Nguồn Sâu Vào Master Notebook)","### Bước 3",
  "### Bước 1–2: NẠP NGUỒN SÂU VÀ TRÍCH XUẤT RA VAULT\n\n"+WHY+"\n\nTư duy khi viết file kế hoạch: mỗi nguồn nạp nhắm một ô chưa phân biệt của ma trận hoặc một GAP mà kho thật sự chưa có (đã tra bằng `kb_reader`); nguồn phản biện luôn có; mỗi câu trích xuất hỏi đúng dữ kiện sẽ phân biệt hai giả thuyết, không hỏi \"hãy tóm tắt\". Nguồn sơ cấp sẵn có (PDF, URL văn bản gốc) thì thêm vào notebook trước khi chạy để trích xuất đọc thẳng nguyên văn.\n\n---\n\n")
# librarian: khối cú pháp Quy tắc 1, bước 3 Quy tắc 3, bảng CLI
f='.agents/skills/notebooklm_librarian/SKILL.md'
B(f,"* **Cú pháp Lệnh Deep Research & Auto-Import:**","* **Thời gian xử lý Deep Mode:**","* **Cách chạy:** "+WHY+"\n")
R(f,"3. **Thực thi trích xuất:** Gọi script Python hoặc vòng lặp CLI `notebooklm ask --prompt-file ... -n <notebook_id> --json` để lưu trực tiếp từng câu trả lời thành các file `research_vault/XX_topic.md`",
  "3. **Thực thi trích xuất:** qua mục `extractions` của file kế hoạch, engine "+ENG+" ghi từng câu trả lời thành `research_vault/<file>` kèm bảng số trích dẫn; không viết script trích xuất riêng cho từng tập.")
R(f,"## 🛠️ DANH MỤC LỆNH CLI PHỔ BIẾN CHO AGENT\n\n| Hành động | Lệnh CLI (`NOTEBOOKLM_HOME` bắt buộc) |",
  "## 🛠️ LỆNH CLI CHỈ ĐỂ KIỂM TRA LẺ (nạp nguồn và trích xuất dùng engine "+ENG+")\n\n| Hành động | Lệnh CLI (hồ sơ mặc định `~/.notebooklm`, KHÔNG đặt `NOTEBOOKLM_HOME`) |")
R(f,"| **Deep Research (Sâu)** | `notebooklm source add-research \"<Query>\" -n <id> --mode deep --import-all --timeout 1800` |\n","")
R(f,"| **Truy vấn RAG & Lưu Note** | `notebooklm ask --prompt-file <file.txt> -n <id> --save-as-note -t \"<Tiêu đề>\" --json` |\n","")
# deep_research workflow Bước 4
f='.agents/workflows/deep_research.md'
R(f,"1. **DEEP RESEARCH EXECUTION (Nạp nguồn phân hạch):** Chạy tuần tự các lệnh `notebooklm source add-research` (hoặc công cụ Deep Research) cho từng Prompt chuyên sâu đã thiết kế ở Bước 3, nạp dồn toàn bộ nguồn vào **CÙNG 1 Master Notebook duy nhất** (`-n <notebook_id> --mode deep --import-all`).\n2. **EXTRACTION & VERIFICATION (Trích xuất):** Chạy `mcp_notebooklm-mcp_batch_to_vault` hoặc script trích xuất để rút dữ liệu theo danh sách câu hỏi đã thiết kế, lưu vào `episodes/[slug]/research_vault/` và tiến hành đối chiếu số liệu.",
  "1. **NẠP NGUỒN VÀ TRÍCH XUẤT (một engine):** "+WHY+"\n2. **ĐỐI CHIẾU:** tự mở lại nguồn gốc các câu then chốt trong vault (URL mở được, câu nguyên văn khớp, số đúng kỳ và phạm vi).")
R(f,"   - ⛔ **CẤM:** Tuyệt đối KHÔNG ĐƯỢC dùng tool `create_notebook` để tạo notebook mới mỗi khi research. Nếu đã có file `.notebook_url`, BẮT BUỘC dùng URL trong đó cho mọi tool (deep_research, ask_question).",
  "   - Một tập một notebook: engine "+ENG+" tự tạo notebook khi chưa có và ghi `.notebook_id`; có rồi thì dùng lại.")
# AGENTS.md mục NotebookLM: thêm dòng dẫn engine
f='.agents/AGENTS.md'
R(f,"> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI CHẠY LỆNH NOTEBOOKLM:**\n> 1. **BẮT BUỘC DÙNG `BypassSandbox: true`:**",
  "> ⚠️ **BẮT BUỘC TUÂN THỦ 100% KHI CHẠY LỆNH NOTEBOOKLM:**\n> 0. **Đường chạy chuẩn:** nạp nguồn và trích xuất của mọi tập và mọi đợt kho đi qua engine Direct RPC dùng chung "+ENG+" (file kế hoạch → chạy tiếp được khi dở → vault đúng khuôn nạp kho). Không gọi `notebooklm source add-research` / `ask` từng lệnh, không viết script riêng cho từng tập. CLI chỉ để kiểm tra lẻ (auth, list, source list).\n> 1. **BẮT BUỘC DÙNG `BypassSandbox: true`:**")
R(f,"giúp tích lũy 40–80 nguồn dữ liệu chuyên sâu đa tầng, không bị sót mảng nào.","giúp tích lũy 40–80 nguồn dữ liệu chuyên sâu đa tầng, không bị sót mảng nào. (Engine chạy các nguồn trong file kế hoạch theo thứ tự này.)")
# orchestration-protocol
f='.agents/rules/orchestration-protocol.md'
R(f,"- **NotebookLM (qua CLI, Claude gọi trực tiếp):** nạp nguồn deep research và đọc nguồn thô, trích xuất ra `research_vault/`.",
  "- **NotebookLM (qua engine Direct RPC "+ENG+"):** nạp nguồn deep research và trích xuất ra `research_vault/` theo file kế hoạch; ai chạy (Antigravity hay Claude) cũng dùng cùng engine.")
errs=0
for op,*a in E:
    if op=='R':
        f,old,new=a; p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
        if n!=1: print(f"LỖI {f}: {n} lần :: {old[:60]!r}"); errs+=1; continue
        open(p,'w').write(s.replace(old,new)); print("OK",f)
    else:
        f,st,en,new=a; p=os.path.join(ROOT,f); s=open(p).read()
        i=s.find(st); j=s.find(en,i+1)
        if i<0 or j<0: print(f"LỖI khối {f}: {st[:30]!r}→{en[:20]!r}"); errs+=1; continue
        open(p,'w').write(s[:i]+new+s[j:]); print("OK khối",f)
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
