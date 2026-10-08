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

### 2026-09-26 — Hook/voiceover bị viết theo văn viết thay vì văn nói (Claude tự mắc, không phải lỗi user)
- Vấn đề: Khi soạn hook, Claude nhồi nhiều tiêu chí (pain_precision, curiosity_tension, con số chính xác...) vào cùng một câu bằng mệnh đề lồng và cấu trúc quan hệ song song "mà X, mà Y" — hợp lệ khi đọc lại trên giấy nhưng không nghe được qua tai một lần. Gốc rễ: (1) phản xạ nhồi cả bảng tiêu chí vào từng câu thay vì để cả đoạn hook cộng lại mới đạt đủ tiêu chí; (2) lo giữ độ chính xác số liệu (sợ Critical Auditor bắt lỗi ZUI) nên phản xạ là thêm mệnh đề thay vì cắt và để dành số liệu đầy đủ cho thân bài; (3) tự chấm điểm hook bằng cách điền bảng phân tích trừu tượng, bỏ qua bước đọc thành tiếng mà chính hook-engine đã quy định.
- Dấu hiệu nhận biết: Câu hook/voiceover có so sánh lồng kiểu "X lớn hơn Y hơn N lần" trong cùng câu với mệnh đề khác; câu hỏi kết dùng "mà...mà..."; câu dài phải đọc 2 lần mới hiểu chủ ngữ liên kết với gì.
- Cách sửa: Mỗi câu thoại chỉ mang đúng MỘT sự kiện/ý. Cấm cấu trúc "mà X, mà Y" trong văn nói. Số liệu cần ngữ cảnh/so sánh phức tạp thì để dành cho chương thân bài (có chỗ viết đầy đủ + trích nguồn), hook chỉ giữ con số trần trụi nhất. Bắt buộc tự đọc thành tiếng (mô phỏng) trước khi chốt hook hoặc câu voiceover, không chỉ điền bảng điểm.
- Áp dụng vào file lõi nào: `00_core/voice_dna.md` (mục Clarity-First đã có nhưng nên bổ sung ví dụ cụ thể "mà X mà Y"), `.claude/agents/hook-engine.md`, `.claude/skills/hook_lab/SKILL.md`, và cần nhắc lại ở Pha 7 (`chapter-writing.md`) vì lỗi tương tự có thể tái diễn khi viết chapter dài.
- Episode đã phát hiện: tu-chu-duong-sat-cao-toc-bac-nam (Pha 5, user chỉ ra hook "lòng vòng khó hiểu")
