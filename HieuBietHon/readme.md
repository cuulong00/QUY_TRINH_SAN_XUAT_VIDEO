# Script IDE Studio — Hiểu Biết Hơn

Bộ repo này biến Antigravity hoặc Claude Code thành một xưởng sản xuất kịch bản podcast phân tích xã hội dài hơi, nơi chất lượng không phụ thuộc vào trí nhớ ngầm của model mà được khóa bằng state files, review gates và QA riêng cho từng pha.

## Mục tiêu
- Giữ chất lượng nội dung ổn định giữa nhiều phiên làm việc.
- Biến raw topic thành long-form script sắc, sâu, dễ nghe và có retention tốt.
- Tối ưu viral potential mà không rơi vào clickbait rẻ, overclaim hay vi phạm bản quyền và chính sách an toàn.
- Dùng được trong cả Antigravity và Claude Code trên cùng một repo.

## Nguyên tắc nền
1. Repo là nguồn sự thật duy nhất.
2. Mỗi video là một thư mục riêng dưới `episodes/`.
3. Không bao giờ viết full script one-shot từ chủ đề thô.
4. Sau mỗi bước phải cập nhật file state.
5. Chất lượng được giữ bằng state + rubric + QA, không chỉ bằng prompt hay model.
6. Editorial & legal compliance và voiceover readiness là hard gates, không phải phần sửa sau cùng.

## Cấu trúc chính
- `00_core/`: DNA của kênh — voice, audience, hook, safety, long-form, anti-patterns.
- `01_management/`: backlog, registry, learning log.
- `02_templates/episode_template/`: template state machine cho mỗi episode.
- `03_playbooks/`: cách vận hành trên Antigravity hoặc Claude Code.
- `CLAUDE.md`: canonical operating system cho Claude Code.
- `.claude/commands/`: slash commands theo pha.
- `.claude/agents/`: subagents chuyên môn.
- `.agent/workflows/`: workflows cho Antigravity.
- `ANTIGRAVITY_WORKSPACE_RULES.md`: rules để paste vào Antigravity.
- `scripts/slideshow_video/`: module render slideshow video từ thư mục ảnh bằng FFmpeg.

## Pipeline chính thức
Mỗi episode mới nên đi theo chuỗi sau:
1. Topic Qualification
2. Data Mining & Verification
3. Strategy Brief
4. Hook Lab
5. Thesis Map
6. Retention Map
7. Outline
8. Chapter Briefs
9. Chapter Writing
10. Editorial & Legal QA
11. Oral QA
12. Visual Map
13. Audio Landscape
14. Video Render (CapCut - Manual)
15. Production Handoff
16. Postmortem
17. Performance Review

## Required vs optional artifacts
### Required artifacts
- `01_topic_qualification.md`
- `02_research_map.md`
- `03_brief.md`
- `04_hook_pack.md`
- `05_thesis_map.md`
- `06_retention_map.md`
- `07_outline.md`
- `08_chapter_briefs.md`
- `09_narrative_state_tracker.md`
- `10_claim_ledger.md`
- `chapter_XX.md`
- `10_compliance_report.md` (thay thế cho editorial_qa và oral_qa)
- `visual_map.csv`
- `production_notes.md`
- `postmortem.md`

### Optional-supported artifacts
- `07_golden_lines.md`
- `generated output như `video/slideshow_base.mp4``

## Nên dùng IDE nào?
- Nếu ưu tiên **độ ổn định, memory rõ ràng, phase discipline rõ**: nghiêng về Claude Code.
- Nếu ưu tiên **giao diện orchestration và mission-control**: Antigravity dễ dùng hơn.
- Cách tối ưu nhất là dùng chung repo này cho cả hai, nhưng luôn coi file state là nguồn sự thật.

## Quick start
1. Copy repo này vào máy của bạn.
2. Mở repo trong Antigravity hoặc Claude Code.
3. Nếu dùng Claude Code, file `CLAUDE.md` sẽ được đọc như project memory.
4. Nếu dùng Antigravity, paste `ANTIGRAVITY_WORKSPACE_RULES.md` vào workspace rules hoặc user rules của project.
5. Tạo episode mới bằng script:
   ```bash
   bash scripts/new_episode.sh ten-chu-de-cua-ban
   ```
6. Làm theo `03_playbooks/episode_workflow.md`.
7. Khi đã có thư mục video clips cuối, import chúng vào CapCut cùng voiceover để dựng thủ công và xuất video hoàn chỉnh:
   - Import `videos_final/` và voiceover audio
   - Dựng hậu kỳ, đồng bộ thời lượng khớp với audio
   - Xuất video base chất lượng cao (H.264, 1080p, 30fps) lưu vào `episodes/[slug]/video/slideshow_base.mp4`
8. Khi cần audit repo hoặc kiểm tra một episode, chạy validator:
   ```bash
   node scripts/validate_repo.js all
   node scripts/validate_repo.js episode ten-chu-de-cua-ban
   ```

## Quy tắc vàng
- Core files quyết định giọng và tiêu chuẩn.
- State files quyết định trí nhớ.
- Commands/workflows quyết định tính kỷ luật.
- Rubric quyết định chất lượng.
- Claim ledger quyết định độ an toàn thông tin và chính thống.
- Retention map quyết định video có chết ở giữa hay không.
- Video Render (CapCut) thực hiện dựng thủ công sau khi đã có thư mục video clips final được sắp thứ tự đúng và file voiceover.