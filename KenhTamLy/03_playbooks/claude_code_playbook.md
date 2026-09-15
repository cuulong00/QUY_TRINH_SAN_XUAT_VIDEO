# claude_code_playbook.md

Claude Code là lựa chọn an toàn hơn nếu bạn ưu tiên sự ổn định của memory và hành vi, vì nó có project memory qua `CLAUDE.md`, custom slash commands, subagents và hooks được tài liệu hóa chính thức. Điều này rất hợp với bài toán long-form cần nhớ trạng thái giữa nhiều phiên và cần tách vai trò làm việc.

## Thiết lập
1. Mở repo này trong Claude Code.
2. Claude Code sẽ đọc `CLAUDE.md` ở root như project memory.
3. Kiểm tra `CLAUDE.md` và `.claude/rules/` đã phản ánh đúng workflow hiện tại.
4. Kiểm tra `.claude/commands/` đã hiện trong `/help`.
5. Kiểm tra `.claude/agents/` trong `/agents`.
6. Kiểm tra `.claude/settings.json` đang tồn tại nếu repo dùng hooks / guardrails.

## Cách dùng khuyến nghị
### Cách 1 — dùng slash commands
- `/generate_episode [topic-or-slug]`
- `/init_episode [slug]`
- `/hook_lab [slug]`
- `/build_outline [slug]`
- `/write_chapter [slug] chapter_01`
- `/merge_voiceover [slug]`
- `/qa_review [slug]`

### Cách 2 — dùng subagents chủ động
Yêu cầu Claude Code dùng các subagent sau:
- script-architect
- hook-engine
- chapter-writer
- doctrinal-qa
- oral-polisher

Ví dụ:
- "Use the script-architect subagent to create the brief for episodes/buong-bo-nguoi-cu"
- "Use the hook-engine subagent to produce 10 hooks for episodes/buong-bo-nguoi-cu"

## Khi nào Claude Code đặc biệt mạnh
- Khi bạn muốn làm việc dài nhiều phiên.
- Khi bạn muốn tách vai trò bằng subagents để tránh nhiễu context chính.
- Khi bạn muốn slash commands chạy đúng quy trình lặp lại.