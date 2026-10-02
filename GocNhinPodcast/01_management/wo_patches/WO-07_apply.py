import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new,tag="HC"): E.append((f,old,new,tag))
HC="`episodes/[slug]/00_hien_chuong.md`"
R('.agents/workflows/init_episode.md',"4. Chạy `/build_global_vision` để làm Pha 1. Không tạo `01_global_vision_synthesis.md` từ file này.",
"4. **Pha 0 — Hiến chương tập:** cùng user điền `episodes/[slug]/00_hien_chuong.md` (đã có sẵn từ template): tiêu đề chính/phụ, câu hỏi trung tâm nguyên văn, loại A/B/C, chỉ đạo user, điều đã loại, lăng kính phản biện (≥2), chế độ kết dự kiến, nút N3 và N5. Agent không tự điền thay user ở mục 1–3.\n5. Chạy `/build_global_vision` để làm Pha 1. Không tạo `01_global_vision_synthesis.md` từ file này.")
R('.agents/workflows/hook_lab.md',"2. Đọc: `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/07_outline.md`",
"2. Đọc: "+HC+" (tiêu đề, câu hỏi trung tâm nguyên văn, lời hứa đóng gói phải khớp; từ khóa đã loại), `episodes/[slug]/00_bang_gia_thuyet.md` (hook đặt câu hỏi, không lộ giả thuyết còn đứng), `00_core/voice_dna.md`, `00_core/anti_ai_isms.md`, `00_core/vietnam_macro_context.md`, `episodes/[slug]/03_brief.md`, `episodes/[slug]/07_outline.md`")
R('.agents/workflows/build_outline.md',"2. Đọc: `00_core/longform_blueprint.md`, `00_core/voice_dna.md`,",
"2. Đọc: "+HC+" (đề bài khóa, N1–N5, lăng kính đã chọn), `episodes/[slug]/00_bang_gia_thuyet.md` (giả thuyết còn đứng, bằng chứng BÁC còn đứng → Devil's Chapter), `00_core/longform_blueprint.md`, `00_core/voice_dna.md`,")
R('.agents/workflows/write_chapter.md',"  >   * `01_global_vision_synthesis.md` (Tầm nhìn tổng thể & Mỏ neo số liệu)",
"  >   * `episodes/[slug]/00_hien_chuong.md` (đề bài khóa, từ khóa đã loại) và `00_bang_gia_thuyet.md` (nhãn và mã mắt xích)\n  >   * `01_global_vision_synthesis.md` (Tầm nhìn tổng thể & Mỏ neo số liệu)")
R('.agents/skills/chapter_writer/SKILL.md',"- `02_research_synthesis.md` — GRS đã có và đã nạp vào ngữ cảnh",
"- `00_hien_chuong.md` — đề bài khóa, từ khóa đã loại, N1–N5; `00_bang_gia_thuyet.md` — giả thuyết còn đứng và mã E để trỏ thay cho chép câu\n- `02_research_synthesis.md` — GRS đã có và đã nạp vào ngữ cảnh")
R('.agents/rules/chapter-writing.md',"- Trước khi viết chapter phải đọc tối thiểu: `03_brief.md`,",
"- Trước khi viết chapter phải đọc tối thiểu: `00_hien_chuong.md`, `00_bang_gia_thuyet.md`, `03_brief.md`,")
R('.agents/workflows/merge_voiceover.md',"> - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**",
"> - 📚 **Tài Liệu Nguồn Đã Đọc & Nạp (Input References):**\n>   * `episodes/[slug]/00_hien_chuong.md` (tiêu đề, câu hỏi trung tâm, chế độ kết N3, từ khóa đã loại — bản merge phải khớp)")
R('.agents/skills/compliance_council/SKILL.md',"## 2. Sát Hạch Hội Đồng Phản Biện Đa Diện (Tri-Adversarial Red Team Stress-Test)",
"## 1b. Đối Chiếu Hiến Chương Tập (`00_hien_chuong.md`)\n* **Tiêu đề và câu hỏi trung tâm:** [khớp nguyên văn? Đạt / Lệch ở đâu]\n* **Từ khóa / khung đã loại:** [0 lần xuất hiện? liệt kê nếu có]\n* **Chế độ kết (N3), lăng kính (N5), số giả thuyết (N2):** [khớp hồ sơ đề tài? bằng chứng BÁC còn đứng trong `00_bang_gia_thuyet.md` có được chương kết chung sống?]\n\n## 2. Sát Hạch Hội Đồng Phản Biện Đa Diện (Tri-Adversarial Red Team Stress-Test)")
R('.agents/rules/orchestration-protocol.md',"2. Đọc dòng của episode trong `01_management/episode_registry.csv` và khối cuối của `episodes/[slug]/00_pipeline_operator_log.md`.",
"2. Đọc dòng của episode trong `01_management/episode_registry.csv`, khối cuối của `episodes/[slug]/00_pipeline_operator_log.md`, và `episodes/[slug]/00_hien_chuong.md` (đề bài khóa, chỉ đạo user, hồ sơ đề tài). Chưa có hiến chương thì làm Pha 0 trước.")
R('.agents/rules/content-os-pipeline.md',"## Kiểm tra trạng thái episode TRƯỚC KHI viết",
"## Kiểm tra trạng thái episode TRƯỚC KHI viết\n\n> Mọi pha đọc `episodes/[slug]/00_hien_chuong.md` trước (đề bài khóa, chỉ đạo user, điều đã loại, hồ sơ đề tài N1–N5; khuôn `02_templates/masterpiece_pipeline/00_hien_chuong_template.md`) và `00_bang_gia_thuyet.md` (giả thuyết, ma trận bằng chứng). Agent không sửa hai file này ngoài phần được giao; cổng máy đối chiếu đầu ra từng pha với hiến chương.")
errs=0
for f,old,new,tag in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {f}: {n} lần :: {old[:50]!r}"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print("OK",f)
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
