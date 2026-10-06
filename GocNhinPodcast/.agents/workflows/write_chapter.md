---
description: >-
  Chapter writing phase workflow. Entry point: .agents/phases/pha_07_viet_chuong.md
  (reads only what the phase card points to).
---

Chapter writing workflow only.

**Cổng vào duy nhất: thẻ `.agents/phases/pha_07_viet_chuong.md`** (từ 03/10/2026). Đọc đúng những gì thẻ trỏ tới, theo đúng thứ tự trong thẻ: hiến chương mục 1–3, brief của chương, các hàng sổ kèm nguồn gốc, các chương trước, các mục luật được chỉ định.
- Chạy Chặng 1 (khung xương cơ chế) và Chặng 2 (bảng nhịp chương, rồi văn) là hai lượt riêng biệt (`chapter_writer/SKILL.md` Bước 1).
- Trước khi nộp, tự soi theo **Phiếu B** của `00_core/narrative_craft_rubric.md` (`chapter_writer/SKILL.md` Bước 3b): mọi điểm 4–5 và 1–2 trích câu, không chấm bằng đếm; tự soi để sửa câu yếu trước khi nộp, không phải điều kiện lưu file và không tính vào điểm K (chương đạt hay không do chấm mù ở Pha 10 quyết định); chép phiếu vào `episodes/[slug]/11_narrative_craft_scorecard.md` (phần tự soi).
- Chạy `python3 scripts/kiem_pha.py <slug> --pha 7`, báo Claude, rồi dừng chờ duyệt.

Các phần cũ của workflow này (pre-flight log, gọi hội đồng chấm sau khi viết) không còn bắt buộc. Chấm do người khác làm theo thẻ Pha 9–11.
