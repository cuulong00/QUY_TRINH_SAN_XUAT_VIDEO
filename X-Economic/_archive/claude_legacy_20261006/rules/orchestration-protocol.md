# orchestration-protocol

Áp dụng cho mọi session làm việc với `episodes/**`, chọn chủ đề mới, hoặc nghiên cứu cho kênh.
Mục tiêu: session nào cũng tự biết phải làm gì, không cần user hướng dẫn lại.

## Vai trò
- **Claude (tổng điều phối, "bộ não"):** chọn chủ đề, lập kế hoạch nghiên cứu, phán quyết dữ liệu (taxonomy, dữ liệu bất đồng), kiến trúc biện chứng, viết chapter, merge, chấm QA, cùng user quyết gate.
- **NotebookLM (qua CLI, Claude gọi trực tiếp):** nạp nguồn deep research và đọc nguồn thô, trích xuất ra `research_vault/`.
- **Antigravity (tay chân web):** tra cứu và xác minh diện rộng trên web, quét đối thủ YouTube, nén file thô thành bảng.
- **User:** duyệt gate, cung cấp số liệu YouTube Studio, chạy prompt Antigravity khi `agy` chạy nền chưa có quyền dùng công cụ.

## Khởi động session (tự làm, không đợi nhắc)
1. Xác định episode từ lời user. Nếu là ý tưởng mới chưa có slug → bắt đầu từ bước 0a (Scouting).
2. Đọc dòng của episode trong `01_management/episode_registry.csv` và khối cuối của `episodes/[slug]/00_pipeline_operator_log.md`.
3. Báo user một dòng: pha hiện tại, `gate_status`, pha hợp lệ kế tiếp, chuyên gia sẽ hóa thân.
4. Chỉ làm đúng pha đó rồi dừng ở gate.

## Chuỗi pha
0a Scouting chủ đề → 0b `qualify_topic` (`00_topic_qualification.md`) → Pha 1 Global Vision → Pha 2 Deep Research (kế hoạch → nạp nguồn → trích xuất → research map/synthesis) → 3 Brief → 4 Outline → 5 Hook Lab → 6 Chapter Briefs + NST → 7 Chapters → 8 Merge → 9 Retention Audit → 10–11 QA → (12–14 chỉ khi user yêu cầu) → 15 Handoff → 16 Postmortem.

- **0a Scouting:** đọc `01_management/master_channel_analytics_audit.md` (mục VII: chân dung khán giả thật) và `01_management/topic_backlog.md`; ưu tiên dữ liệu kênh thật hơn giả định. Đầu ra: một entry trong backlog.

## Hóa thân chuyên gia (bắt buộc trước mỗi pha)
- Mở `SKILL.md` của pha (`.claude/skills/*` hoặc `.agents/skills/*`) và `.claude/specialist_map.md`; đọc đủ mọi persona được chỉ định. Chưa đọc thì không tạo output.
- Pha 1: `.agents/workflows/build_global_vision.md` và các persona nó chỉ định.
- Pha 2: `.agents/skills/deep_researcher/SKILL.md` (Industrial Economist + Policy Analyst; thêm Capital Markets Analyst nếu đề tài thuộc thị trường vốn), cộng phương pháp trong `03_playbooks/deep_research_orchestration.md`.

## Phân công theo pha
| Pha | Claude | NotebookLM / Antigravity / User |
|---|---|---|
| 0a–0b | Phán đoán chủ đề, persona, niềm tin sai, rủi ro | Antigravity/user: xác minh dữ kiện thời sự |
| 1 | Toàn bộ bàn cờ, lăng kính, phản biện | Antigravity: số liệu nền nếu thiếu |
| 2 | **Duyệt** kế hoạch nghiên cứu của Antigravity (sai hướng → yêu cầu sửa ngay), audit vault, research map, synthesis | Antigravity: lập `02_research_plan.md` (các prompt nạp nguồn phủ đủ 5 khía cạnh + các câu trích xuất; **số lượng co giãn theo độ phức tạp đề tài**), sau khi Claude duyệt thì **Claude tự chạy NotebookLM CLI trực tiếp** (Antigravity KHÔNG tự chạy được — xem giới hạn quyền lệnh động bên dưới) để nạp nguồn + trích xuất ra `research_vault/` |
| 3–9 | Toàn bộ (không giao prose ra ngoài) | — |
| 10–11 | Chấm điểm, quyết ngưỡng | Script `google_ai_audit.py`; Antigravity: quét cơ học |
| 12 | Prompt nghệ thuật cuối | Antigravity: scene list thô |
| 16 | Rút bài học | User: số liệu YouTube Studio |

## Kênh giao việc
### Deep research Pha 2 — Antigravity lập kế hoạch và chạy, Claude duyệt
1. Gọi agy lần 1 (chỉ lập kế hoạch, không chạy NotebookLM): theo `.agents/workflows/deep_research.md` + `.agents/skills/deep_researcher/SKILL.md`, đọc `01_global_vision_synthesis.md`, ghi `episodes/[slug]/02_research_plan.md` rồi dừng.
2. Claude duyệt kế hoạch theo checklist trong `03_playbooks/deep_research_orchestration.md`. Sai hướng/thiếu chiều/thiếu phản biện → ghi yêu cầu sửa cụ thể, gọi agy sửa lại. Lặp tới khi đạt.
3. Gọi agy lần 2 (chạy nền): nạp nguồn 5 prompt vào một Master Notebook, trích xuất ra `research_vault/`, ghi id vào `.notebook_id`.
4. Claude audit vault và viết `02_research_map.md` + `02_research_synthesis.md`.

### NotebookLM — Claude gọi trực tiếp (chỉ khi cần tra thêm lẻ tẻ)
- Dùng hồ sơ mặc định `~/.notebooklm`. **Không** đặt `NOTEBOOKLM_HOME=.notebooklm_home`: hồ sơ đó hết hạn đăng nhập (kiểm tra 26/09/2026). Kiểm tra trước khi chạy: `notebooklm auth check --test --json` phải có `token_fetch: true`.
- Lệnh chạy lâu (`add-research --mode deep`, 15–30 phút) chạy nền, không poll.
- Một episode = một notebook; ghi id vào `episodes/[slug]/.notebook_id`.
- Kết quả trích xuất ghi thẳng ra `episodes/[slug]/research_vault/*.md`. Claude chỉ đọc vault, không đọc fulltext nguồn.

### Antigravity
> Giới hạn kỹ thuật chung của `agy` (permission model, headless vs interactive, web search, hook Stop) đã chuyển sang bản gốc dùng chung **`/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md` mục 8b-8c**. Đọc ở đó trước, không lặp lại ở đây.
> Riêng cho kênh này (đã kiểm chứng 26/09/2026): `agy -p --project GocNhinPodcast` chạy NỀN (headless) gọi được đúng `notebooklm list`, nhưng KHÔNG chạy được `notebooklm source list -n <id> --json` hay bất kỳ lệnh con NotebookLM nào có tham số động (bị chặn quyền, đúng mục 8b). **Nhưng pipeline nạp nguồn/trích xuất NotebookLM (Bước E) vẫn giao qua mailbox cho phiên Antigravity IDE tương tác như bình thường** — giới hạn trên chỉ áp dụng cho `agy -p` chạy nền, không áp dụng cho phiên IDE tương tác (đã có đủ quyền công cụ). Claude chỉ tự chạy CLI trực tiếp khi chưa có phiên IDE nào đang kết nối.
- Mặc định: Claude soạn prompt → user chạy trong Antigravity → lưu kết quả vào `episodes/[slug]/research_raw/` hoặc `01_management/` → Claude đọc.
- Khi user đã cấu hình allowlist cho agy: Claude được gọi `agy -p "..." --model gemini-3.1-pro-high`, đầu ra ghi vào `research_raw/`.
- Mọi prompt giao đi phải có: mục tiêu, format dòng cố định, URL + ngày dd/mm/yyyy, ghi "KHÔNG RÕ" thay vì đoán, cấm nguồn nhóm Facebook/blog vô danh, giới hạn số từ.

## Ranh giới cứng
- Công cụ phụ không ghi vào file pha chính thức (`0X_*.md`, `chapter_XX.md`, `voiceover.md`); chỉ ghi `research_raw/`, `research_vault/`, hoặc file thô trong `01_management/`.
- Mọi output bên ngoài là **chưa xác minh** cho tới khi Claude kiểm: URL trùng, ngày thiếu, số vô lý, link YouTube (đã từng bị bịa).
- `01_management/episode_registry.csv` phải sửa bằng tool Edit/Write, không bằng Bash (hook `stop_guard` chỉ ghi nhận Write/Edit).
- Gate chỉ do user và Claude quyết.

## Hợp tác 2 agent (Claude ↔ Antigravity IDE)

Giao thức chính thức (user chốt 26/09/2026) nằm ở **`/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`** (bản chung cho mọi dự án). Đọc file đó trước khi trao đổi với Antigravity. Không chép lại nội dung ở đây.

Tóm tắt những điểm Claude hay quên:
- Mỗi episode có 2 agent: Claude và **đúng một** hội thoại Antigravity IDE (có đủ quyền công cụ). Không dùng `agy -p` cho việc cần ghi file hay chạy lệnh.
- Kênh: `episodes/<slug>/_agent_chat/` gồm `mailbox.jsonl`, `tasks/<taskId>.json`, `session.json`. Tin nhắn chỉ là lời báo, file mới là sự thật: luôn tự kiểm tra artifact.
- Tối đa 5 tin cho mỗi việc. Antigravity chỉ báo cáo, không chuyển pha.
- Đánh thức: dùng `Monitor` với `tail -n 0 -F mailbox.jsonl | grep --line-buffered '"to": "claude"'` (bắt cả định dạng cũ `"from": "antigravity"`). Không dùng vòng `sleep` hay `ScheduleWakeup`.

## Khi thiếu dữ liệu
Không tự cào web diện rộng. NotebookLM làm được thì chạy NotebookLM. Cần web ngoài hoặc YouTube Studio thì soạn prompt hoặc nêu yêu cầu cụ thể cho user.
