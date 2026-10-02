import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new): E.append((f,old,new))
SO="`00_so_du_kien.md`"
R('.agents/rules/claim-ledger.md',"Áp dụng cho bảng claim trong `episodes/**/10_compliance_report.md`",
"Nguồn gốc của mọi claim là **sổ dữ kiện xuyên tập** `episodes/**/00_so_du_kien.md` (khuôn: `02_templates/masterpiece_pipeline/00_so_du_kien_template.md`, tạo ở Pha 1, chỉ thêm dòng). Bảng claim trong `10_compliance_report.md` là bản trích từ sổ, không tạo mã mới. Áp dụng cho sổ và cho bảng claim trong `episodes/**/10_compliance_report.md`")
R('.agents/rules/claim-ledger.md',"- Ledger phải luôn bám sát script/chapter hiện hành, không để claim mồ côi.",
"- Ledger phải luôn bám sát script/chapter hiện hành, không để claim mồ côi.\n- Outline, brief, chương trỏ mã `M-xx` của sổ thay cho chép lại câu; nhãn đi theo mã, không gán lại khi viết lại. Mắt xích chưa có trong sổ thì thêm dòng trước khi viết.\n- Phép tính kênh tự làm phải ghi `tự tính: M? / M?` và mang nhãn `market_analysis`.")
R('.agents/rules/chapter-writing.md',"- Sau khi viết chapter phải cập nhật `09_narrative_state_tracker.md`, `10_compliance_report.md`, và `01_management/episode_registry.csv`.",
"- Mọi số và nhận định trong chapter trỏ về một mã `M-xx` trong "+SO+" và viết đúng tầng giọng của nhãn đó (`00_core/stance_and_judgment.md` §5). Mắt xích mới thì thêm dòng vào sổ trước khi viết; không viết câu nào vượt nhãn.\n- Sau khi viết chapter phải cập nhật "+SO+" (dòng mới, cột \"Dùng ở\"), `09_narrative_state_tracker.md`, `10_compliance_report.md` (bảng claim trích từ sổ), và `01_management/episode_registry.csv`.")
R('.agents/skills/chapter_writer/SKILL.md',"- **Mỗi nhận định phải phân loại**: `verified_data` / `market_analysis` / `opinion_commentary`",
"- **Mỗi nhận định đi theo nhãn của hàng `M-xx` trong "+SO+"** (`verified_data` nói thẳng; `market_analysis` chỉ ra đường đi từ dữ kiện; `opinion_commentary` nhận là của kênh). Không tự gán nhãn mới khi viết; mắt xích chưa có trong sổ thì thêm dòng trước. Số không có mã M không được xuất hiện trong thoại.")
R('.agents/skills/chapter_writer/SKILL.md',"- `10_compliance_report.md` — claim mới phân loại",
"- "+SO+" — mắt xích mới (nhãn, nguồn, kỳ/phạm vi), điền cột \"Dùng ở\" cho chương vừa viết\n- `10_compliance_report.md` — bảng claim trích từ sổ dữ kiện, không tạo mã mới")
R('.agents/skills/compliance_council/SKILL.md',"12. 🚩 Claim thiếu nhãn taxonomy (`verified_data` / `market_analysis` / `opinion_commentary`) hoặc thiếu dòng lưu ý nội dung bắt buộc.",
"12. 🚩 Claim thiếu nhãn taxonomy (`verified_data` / `market_analysis` / `opinion_commentary`) hoặc thiếu dòng lưu ý nội dung bắt buộc.\n13. 🚩 Số hoặc nhận định trong kịch bản không có hàng `M-xx` trong "+SO+", hoặc viết vượt nhãn của hàng (suy luận viết như dữ kiện); chân đỡ của giả thuyết dẫn đầu (sổ, mục cuối) biến mất không lý do.")
R('.agents/rules/final-merge.md',"- Đảm bảo dòng lưu ý nội dung bắt buộc xuất hiện đúng nguyên văn",
"- Đối chiếu `voiceover.md` với "+SO+": mọi số có mã M; mỗi mắt xích giữ đúng tầng giọng của nhãn khi gộp; không cộng dồn câu đặt cược từ nhiều chương.\n- Đảm bảo dòng lưu ý nội dung bắt buộc xuất hiện đúng nguyên văn")
R('02_templates/masterpiece_pipeline/08_chapter_briefs_template.md',"| **4** | `data_verified` | Danh mục các con số thực chứng bắt buộc phải xuất hiện 100%. | Macro Strategist |",
"| **4** | `data_verified` | Danh mục mã `M-xx` từ `00_so_du_kien.md` bắt buộc xuất hiện trong chương (kèm nhãn); trỏ mã, không chép câu. | Macro Strategist |")
R('02_templates/episode_template/10_compliance_report.md',"## 1. Editorial & Brand Safety Verification",
"## 0. Bảng claim (trích từ `00_so_du_kien.md`, không tạo mã mới)\n| Mã M | Claim trong kịch bản (chương, câu) | Nhãn | Nguồn | Khớp nhãn khi viết? |\n|---|---|---|---|---|\n| | | | | |\n\n## 1. Editorial & Brand Safety Verification")
R('.agents/workflows/build_global_vision.md',"4. Hội đồng tranh biện (Bước 3, Phần I.2) tranh luận trên các giả thuyết",
"3b. Tạo `episodes/[slug]/00_so_du_kien.md` theo `02_templates/masterpiece_pipeline/00_so_du_kien_template.md`: mọi OBS ở mục 1.4 thành hàng `M-xx` nhãn `verified_data` (kèm kỳ, phạm vi, mã E); phản biện và suy luận của hội đồng thành hàng `market_analysis` / `opinion_commentary`. Điền bảng \"Chân đỡ của giả thuyết dẫn đầu\".\n4. Hội đồng tranh biện (Bước 3, Phần I.2) tranh luận trên các giả thuyết")
R('.agents/workflows/deep_research.md',"3. **CẬP NHẬT MA TRẬN (phần E của form tư duy):**","3. **CẬP NHẬT MA TRẬN VÀ SỔ DỮ KIỆN (phần E của form tư duy):** mỗi dữ kiện mới từ vault thêm một hàng `M-xx` vào `00_so_du_kien.md` (nhãn `verified_data` chỉ khi có câu nguyên văn + URL + ngày; không thì `market_analysis`).")
R('.agents/workflows/build_brief.md',"   [ ] Bảng mỏ neo số liệu chiến lược — Data Passport: mỗi dòng có `OBS-…` hoặc file vault, kỳ/phạm vi/đơn vị, nhãn mắt xích và mã E",
"   [ ] Bảng mỏ neo số liệu chiến lược — Data Passport là bản trích từ `00_so_du_kien.md`: mỗi dòng có mã M, `OBS-…` hoặc file vault, kỳ/phạm vi/đơn vị, nhãn và mã E; không tạo mã mới ngoài sổ")
R('02_templates/masterpiece_pipeline/03_brief_template.md',"| Nhãn mắt xích (`verified_data` / `market_analysis` / `opinion_commentary`) và mã E trong `00_bang_gia_thuyet.md` | Ý Nghĩa Phân Tích |",
"| Mã M (`00_so_du_kien.md`) · nhãn (`verified_data` / `market_analysis` / `opinion_commentary`) · mã E (`00_bang_gia_thuyet.md`) | Ý Nghĩa Phân Tích |")
R('02_templates/masterpiece_pipeline/03_brief_template.md',"| `verified_data` · `E03` | `[Ý nghĩa]` |\n| `DATA-02` | `[Con số 2]` | … | … | … | `market_analysis` · `E07` | `[Ý nghĩa]` |",
"| `M01` · `verified_data` · `E03` | `[Ý nghĩa]` |\n| `DATA-02` | `[Con số 2]` | … | … | … | `M07` · `market_analysis` · `E07` | `[Ý nghĩa]` |")
R('.agents/workflows/build_outline.md',"   [ ] Quota mã DATA-XX phân bổ độc quyền cho từng chương, không trùng lặp",
"   [ ] Quota mã DATA-XX phân bổ độc quyền cho từng chương, không trùng lặp\n   [ ] Mỗi Key Insight, Causal Exit, câu chốt trỏ mã `M-xx` (sổ dữ kiện) hoặc `E-xx`/`H-x` (bảng giả thuyết); không khẳng định vượt nhãn của mã được trỏ\n   [ ] Bằng chứng BÁC còn đứng trong `00_bang_gia_thuyet.md` có chương chứa và dòng \"luận điểm đổi gì\"; chân đỡ Pha 1 (sổ dữ kiện, mục cuối) còn mặt hoặc có lý do bỏ")
errs=0
for f,old,new in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {f}: {n} lần :: {old[:50]!r}"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print("OK",f)
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
