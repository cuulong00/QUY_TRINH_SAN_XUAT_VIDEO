# claude_code_playbook.md

Claude Code là lựa chọn mạnh nếu bạn muốn vận hành pipeline kịch bản tài chính dài theo từng pha rõ ràng, với state files, slash commands, subagents, và hard review gates.

## Thiết lập
1. Mở repo này trong Claude Code.
2. Claude Code sẽ đọc `CLAUDE.md` ở root như project memory.
3. Kiểm tra `.claude/commands/` đã hiện trong `/help`.
4. Kiểm tra `.claude/agents/` trong `/agents`.

## Cách dùng khuyến nghị
### Cách 1 — dùng slash commands theo pha
- `/init_episode [slug]`
- `/qualify_topic [slug]`
- `/build_brief [slug]`
- `/build_research_map [slug]`
- `/hook_lab [slug]`
- `/build_thesis [slug]`
- `/build_retention_map [slug]`
- `/build_outline [slug]`
- `/build_chapter_briefs [slug]`
- `/write_chapter [slug] chapter_01`
- `/merge_voiceover [slug]`
- `/financial_qa [slug]`
- `/oral_qa [slug]`
- `/build_visual_map [slug]`
- `/render_slideshow [slug]`
- `/production_handoff [slug]`
- `/postmortem [slug]`

### Cách 2 — dùng subagents chủ động
Yêu cầu Claude Code dùng các subagent sau:
- script-architect
- hook-engine
- chapter-writer
- financial-qa
- oral-polisher

Ví dụ:
- "Use the script-architect subagent to qualify and brief episodes/bam-lam-phat"
- "Use the hook-engine subagent to produce hook options and re-hooks for episodes/bam-the-tin-dung"
- "Use the financial-qa subagent to review final_voiceover.md for episodes/tam-ly-dau-tu"
- "Use the oral-polisher subagent to polish final_voiceover.md for spoken Vietnamese"

## Review gates nên giữ
Bạn nên duyệt tay ở 7 điểm:
- Topic Qualification
- Brief
- Hook Lab
- Thesis Map + Retention Map + Outline
- Final Merge
- Financial QA + Oral QA
- Slideshow Render nếu muốn duyệt video base trước khi handoff

## Khi nào Claude Code đặc biệt mạnh
- Khi bạn muốn làm việc dài nhiều phiên.
- Khi bạn muốn tách vai trò bằng subagents để tránh nhiễu context chính.
- Khi bạn muốn slash commands chạy đúng quy trình lặp lại.
- Khi bạn muốn state files là nguồn sự thật thay vì chat memory.

## Validate repo và episode
- Audit toàn repo:
  ```bash
  node scripts/validate_repo.js all
  ```
- Audit một episode cụ thể:
  ```bash
  node scripts/validate_repo.js episode [slug]
  ```
- Nếu cần machine-readable output:
  ```bash
  node scripts/validate_repo.js all --json
  ```

## Điều cần nhớ
- Không dùng Claude Code để viết full script one-shot từ raw topic.
- Mỗi lần chỉ làm đúng một pha.
- Sau mỗi pha phải cập nhật state file tương ứng.
- `06_claim_ledger.md` luôn phải dùng taxonomy: `verified_data`, `market_analysis`, `opinion_commentary`.
- `render_slideshow` chỉ chạy sau khi đã có thư mục ảnh final.
