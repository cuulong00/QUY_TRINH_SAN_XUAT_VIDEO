# Dòng Chảy: chỉ dẫn cho Claude Code

Mọi chỉ dẫn của dự án (cho Claude, Antigravity và mọi IDE) nằm DUY NHẤT trong `.agents/` (user chốt 06/10/2026). File này chỉ nạp hiến pháp và vai điều phối của Claude; không chứa luật riêng. `.claude/` chỉ chứa cấu hình (quyền, hook).

@.agents/AGENTS.md
@.agents/rules/orchestration-protocol.md

Khi làm một pha: mở thẻ pha `.agents/phases/<pha>.md` (bảng ở hiến pháp §5) và chỉ đọc những gì thẻ trỏ tới. Các rule khác trong `.agents/rules/` (claim-ledger, chapter-writing, editorial-quality, final-merge, operator-visibility, episodes-general, visual-asset-safety, slideshow-render) được thẻ pha gọi đúng lúc, không nạp sẵn.

Khi sửa DNA: theo hiến pháp §7, và kiểm đường tới agent bằng `python3 GocNhinPodcast/scripts/kiem_nap.py <conversationId>`.

Tập mới: file chấm nghệ thuật kịch bản `11_narrative_craft_scorecard.md` bắt buộc từ 06/10/2026 theo `00_core/narrative_craft_rubric.md` (tập đã đăng không bổ sung).
