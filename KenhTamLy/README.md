# Script IDE Studio

Bộ repo này biến Antigravity hoặc Claude Code thành một "xưởng biên kịch" thay vì chỉ là chat IDE.

## Mục tiêu
- Giữ chất lượng nội dung ổn định giữa nhiều phiên làm việc.
- Giữ được trí nhớ làm việc bằng file state, không phụ thuộc vào trí nhớ ngầm của model.
- Tạo kịch bản video dài 40–60 phút theo quy trình nhiều chặng.
- Dùng được trong cả Antigravity và Claude Code trên cùng một repo.

## Nguyên tắc nền
1. Repo là nguồn sự thật duy nhất.
2. Mỗi video là một thư mục riêng dưới `episodes/`.
3. Không bao giờ viết full script one-shot từ chủ đề thô.
4. Sau mỗi bước phải cập nhật file state.
5. Chất lượng được giữ bằng state + rubric + QA, không chỉ bằng prompt hay model.

## Cấu trúc chính
- `00_core/`: 8 file DNA của kênh.
- `01_management/`: backlog, registry, learning log.
- `02_templates/episode_template/`: mẫu cho từng video.
- `03_playbooks/`: cách vận hành trên Antigravity hoặc Claude Code.
- `CLAUDE.md`: project memory chính cho Claude Code.
- `.claude/commands/`: slash commands của Claude Code.
- `.claude/agents/`: subagents chuyên môn cho Claude Code.
- `.agents/workflows/`: workflows legacy cho Antigravity.
- `.claude/rules/`: rule files mô-đun cho Claude Code.
- `.claude/settings.json`: shared hooks / guardrails / repo-local config cho Claude Code.
- `ANTIGRAVITY_WORKSPACE_RULES.md`: rules để paste vào Antigravity.

## Nên dùng IDE nào?
- Nếu ưu tiên **độ ổn định, memory rõ ràng, tài liệu chính thức đầy đủ**: nghiêng về Claude Code.
- Nếu ưu tiên **giao diện, cảm giác orchestration, artifacts, mission-control**: Antigravity dễ dùng hơn.
- Cách tối ưu nhất là: **dùng cùng một repo cho cả hai**, Antigravity để vận hành hằng ngày, Claude Code để làm máy QA/biên tập phụ hoặc fallback.

## Quick start
1. Copy repo này vào máy của bạn.
2. Mở repo trong Antigravity hoặc Claude Code.
3. Nếu dùng Claude Code, file `CLAUDE.md` sẽ được đọc như project memory.
4. Nếu dùng Antigravity, paste `ANTIGRAVITY_WORKSPACE_RULES.md` vào workspace rules hoặc user rules của project.
5. Nếu dùng Claude Code, authority runtime chính nằm ở `CLAUDE.md` + `.claude/*`.
5. Tạo episode mới bằng script:
   ```bash
   bash scripts/new_episode.sh ten-chu-de-cua-ban
   ```
6. Làm theo `03_playbooks/episode_workflow.md`.

## Quy tắc vàng
- Core files quyết định giọng và tiêu chuẩn.
- State files quyết định trí nhớ.
- Commands/workflows quyết định tính kỷ luật.
- Rubric quyết định chất lượng.