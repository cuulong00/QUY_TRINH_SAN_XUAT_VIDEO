import sys,os
ROOT=sys.argv[1]; E=[]
def R(f,old,new): E.append((f,old,new))
R('00_core/masterpiece_quality_standard.md',"5. **Gate 5 (Vi phạm Giới hạn Kỹ thuật Tai nghe):** Tồn tại câu voiceover dài quá 150 ký tự hoặc chứa dấu gạch ngang dài (`—`).",
"5. **Gate 5 (Vi phạm Giới hạn Kỹ thuật Tai nghe):** Tồn tại câu voiceover dài quá 150 ký tự hoặc chứa dấu gạch ngang dài (`—`).\n6. **Gate 6 (Bịa chi tiết / Suy luận viết như dữ kiện):** chi tiết cụ thể (số, địa danh, so sánh nhất, mô tả vật thể, câu gán cho nguồn) không có mã `M-xx` trong `00_so_du_kien.md` hoặc mã OBS hiện hành; hoặc câu mang nhãn `market_analysis` / `opinion_commentary` được viết bằng giọng dữ kiện. Cổng máy `scripts/kiem_pha.py` bắt trước (`SO-KHONG-NGUON`, `SOSANH-NHAT`, `NHAN-ROI`, `OBS-LECH`); người chấm xác nhận.\n\n> **Ai chấm:** người chấm khác agent viết. Cổng máy chạy trước, đầu ra dán vào báo cáo. Không chấm \"trong khối suy nghĩ\" của người viết (user chốt 02/10/2026, WO-00 Q11).")
R('00_core/chapter_quality_standard.md',"### 🛑 KIỂM TOÁN 5 ĐIỀU KIỆN LOẠI BỎ TRỰC TIẾP (HARD-FAIL GATES)\n* [x] **Gate 1 (Mạch nối tự sự):**",
"### 🛑 KIỂM TOÁN 6 ĐIỀU KIỆN LOẠI BỔ TRỰC TIẾP (HARD-FAIL GATES)\n* [ ] **Đầu ra `scripts/kiem_pha.py --pha 7` (dán nguyên văn):** [ĐẠT / danh sách lỗi]\n* [ ] **Gate 0 (ZUI — suy diễn vô căn cứ, bịa chi tiết, viết vượt nhãn):** [Đạt / lỗi, kèm mã M hoặc OBS liên quan]\n* [x] **Gate 1 (Mạch nối tự sự):**")
R('00_core/chapter_quality_standard.md',"> File này là **cổng chính thức cấp chương** (CHQB-50).",
"> File này là **cổng chính thức cấp chương** (CHQB-50). Người chấm khác agent viết; cổng máy `scripts/kiem_pha.py --pha 7` chạy trước và đầu ra dán vào báo cáo (Q11).")
R('.agents/skills/chapter_writer/SKILL.md',"### Bước 3: TỰ SCAN & CRITIC QUA KHỐI THINKING NGẦM (Internal Co-pilot Audit)",
"### Bước 3: TỰ RÀ TRƯỚC KHI NỘP (không phải cổng chấm)\n> Người viết tự rà để nộp bản sạch. Cổng chấm chính thức là `scripts/kiem_pha.py --pha 7` (chạy và dán đầu ra vào tin nộp) rồi người chấm khác theo `00_core/chapter_quality_standard.md`. Không tự cho điểm mình (Q11).")
R('.agents/skills/chapter_writer/SKILL.md',"Chỉ lưu và xuất tệp kịch bản `chapter_XX.md` khi 100% 14 tiêu chí đã ĐẠT.",
"Lưu `chapter_XX.md`, chạy `KB_GRAPH=kb_v2 scripts/kiem_pha.py <slug> --pha 7`, sửa tới khi ra ĐẠT, rồi nộp kèm đầu ra lệnh. Việc cho điểm thuộc người chấm.")
R('.agents/skills/compliance_council/SKILL.md',"> Nếu chưa nạp đủ các chuyên gia này trong phiên làm việc, NGHIÊM CẤM tạo báo cáo compliance.",
"> Nếu chưa nạp đủ các chuyên gia này trong phiên làm việc, NGHIÊM CẤM tạo báo cáo compliance.\n> **Tách vai (Q11):** hội đồng chấm là agent hoặc phiên khác với agent đã viết. Bước 0 của mọi lần chấm: chạy `KB_GRAPH=kb_v2 scripts/kiem_pha.py <slug> --pha 8` và dán đầu ra vào báo cáo; trụ cột 4 (Data Anchoring) chấm trên đầu ra đó, không chấm lại bằng cảm nhận. Cờ đỏ 13 (bịa chi tiết / vượt nhãn) là hard-fail.")
R('.agents/skills/compliance_council/SKILL.md',"# Editorial & Compliance Report — [Slug]\n\n## 1. Điểm số chất lượng",
"# Editorial & Compliance Report — [Slug]\n\n## 0. Đầu ra cổng máy (`scripts/kiem_pha.py --pha 8`, dán nguyên văn)\n```\n[đầu ra]\n```\n\n## 1. Điểm số chất lượng")
R('.agents/skills/compliance_council/SKILL.md',"| 10 | Rò rỉ nhãn template `[BLOCK X]` | Không | ✅ PASS |",
"| 10 | Rò rỉ nhãn template `[BLOCK X]` | Không | ✅ PASS |\n| 11 | Ranh giới tư vấn đầu tư (`financial_boundaries.md`) | Không | ✅ PASS |\n| 12 | Claim thiếu nhãn / thiếu dòng lưu ý | Không | ✅ PASS |\n| 13 | Không có mã M / vượt nhãn / mất chân đỡ (hard-fail) | Không | ✅ PASS |")
R('00_core/retention_gate_checklist.md',"> File này là **cổng chính thức cấp dàn ý** (Gate 1 / Gate D1) và cổng Ch.2 (Gate 2).",
"> File này là **cổng chính thức cấp dàn ý** (Gate 1 / Gate D1) và cổng Ch.2 (Gate 2). Người chấm khác agent viết; chạy `scripts/kiem_pha.py --pha 4` trước và đính đầu ra (Q11).")
R('.agents/AGENTS.md',"— Agent chỉ viết đúng 1 chương rồi dừng chờ User duyệt trước khi sang chương tiếp theo.",
"— Agent chỉ viết đúng 1 chương rồi dừng chờ User duyệt trước khi sang chương tiếp theo. **Thứ tự chấm mọi pha:** cổng máy `scripts/kiem_pha.py` → người chấm khác người viết (Claude hoặc agent khác) → user quyết gate. Không có khâu nào do agent viết tự cho điểm (Q11). Kỹ năng điều phối: `.agents/skills/orchestrator/SKILL.md`.")
R('.agents/rules/orchestration-protocol.md',"## Vai trò\n","## Vai trò\n> Kỹ năng điều phối đầy đủ (phiếu giao, thứ tự chấm, trả lỗi, sống chết agent, sổ vấn đề): `.agents/skills/orchestrator/SKILL.md`. File này giữ chuỗi pha và phân công.\n\n")
errs=0
for f,old,new in E:
    p=os.path.join(ROOT,f); s=open(p).read(); n=s.count(old)
    if n!=1: print(f"LỖI {f}: {n} lần :: {old[:50]!r}"); errs+=1; continue
    open(p,'w').write(s.replace(old,new)); print("OK",f)
print("số sửa:",len(E)-errs,"lỗi:",errs); sys.exit(1 if errs else 0)
