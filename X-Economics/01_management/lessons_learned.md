# lessons_learned.md

Mỗi khi bạn rút ra được một bài học giúp script hay hơn, đừng để nó chết trong chat. Ghi lại vào đây.

## Cấu trúc entry
### YYYY-MM-DD — Tên bài học
- Vấn đề:
- Dấu hiệu nhận biết:
- Cách sửa:
- Áp dụng vào file lõi nào:
- Episode đã phát hiện:

## Entries

### 2026-03-27 — Episode template phải phản ánh toàn bộ state machine
- Vấn đề: Template cũ thiếu nhiều artifact trung gian quan trọng nên Claude dễ nhảy pha hoặc viết prose khi chưa khóa thesis, retention, và safety.
- Dấu hiệu nhận biết: Không có file riêng cho topic qualification, research map, retention map, financial QA, oral QA, production handoff, postmortem.
- Cách sửa: Dùng template episode đầy đủ theo pipeline 15 pha và để bootstrap script tạo sẵn toàn bộ state files ngay từ đầu.
- Áp dụng vào file lõi nào: `CLAUDE.md`, `README.md`, `03_playbooks/episode_workflow.md`, `02_templates/episode_template/*`, `scripts/new_episode.sh`
- Episode đã phát hiện: repo-level dry run
