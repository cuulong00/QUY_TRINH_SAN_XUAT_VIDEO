# orchestration-protocol

Áp dụng cho mọi session làm việc với `episodes/**`, chọn chủ đề mới, hoặc nghiên cứu cho kênh.
Mục tiêu: session nào cũng tự biết phải làm gì, không cần user hướng dẫn lại.

## Vai trò
> Kỹ năng điều phối đầy đủ (phiếu giao, thứ tự chấm, trả lỗi, sống chết agent, sổ vấn đề): `.agents/skills/orchestrator/SKILL.md`. File này giữ chuỗi pha và phân công.

- **Claude (tổng điều phối, "bộ não"):** chọn chủ đề, lập kế hoạch nghiên cứu, phán quyết dữ liệu (taxonomy, dữ liệu bất đồng), kiến trúc biện chứng, viết chapter, merge, chấm QA, cùng user quyết gate.
- **NotebookLM (qua CLI, Claude gọi trực tiếp):** nạp nguồn deep research và đọc nguồn thô, trích xuất ra `research_vault/`.
- **Antigravity (tay chân web):** tra cứu và xác minh diện rộng trên web, quét đối thủ YouTube, nén file thô thành bảng.
- **User:** duyệt gate, cung cấp số liệu YouTube Studio, chạy prompt Antigravity khi `agy` chạy nền chưa có quyền dùng công cụ.

## Khởi động session (tự làm, không đợi nhắc)
1. Xác định episode từ lời user. Nếu là ý tưởng mới chưa có slug → bắt đầu từ bước 0a (Scouting).
2. Đọc dòng của episode trong `01_management/episode_registry.csv`, khối cuối của `episodes/[slug]/00_pipeline_operator_log.md`, và `episodes/[slug]/00_hien_chuong.md` (đề bài khóa, chỉ đạo user, hồ sơ đề tài). Chưa có hiến chương thì làm Pha 0 trước.
3. Báo user một dòng: pha hiện tại, `gate_status`, pha hợp lệ kế tiếp, chuyên gia sẽ hóa thân.
4. Chỉ làm đúng pha đó rồi dừng ở gate.
5. **Cổng máy trước cổng người:** trước khi Claude chấm bất kỳ pha nào, chạy `KB_GRAPH=kb_v2 scripts/kiem_pha.py <slug> --pha <n>` (mã lỗi và ý nghĩa ở đầu file script). Lỗi `OBS-THIEU`, `OBS-LECH`, `SO-KHONG-NGUON`, `NHAN-ROI`, `HC-*`, `GT-BAC`, `SO-CHANDO` là lỗi dữ kiện: trả agent kèm nguyên văn dòng lỗi, không cần hỏi user. Agent báo "đã sửa" phải kèm đầu ra chạy lại cổng. Fixture tự kiểm cổng: `scripts/tests/fixtures/kiem_pha_v22/`.

## Kho tri thức dùng chung (bắt buộc, áp dụng từ 29/09/2026)
Cách tư duy trên kho khi nhận đề tài (từ câu hỏi ra thực thể, thứ tự tra, đọc đầu ra dài, tìm dữ kiện ngược, nhiều bản lệch số, độ mới): `.agents/skills/kb_reader/SKILL.md` — bắt buộc cho mọi agent ở Pha 1, 2, 7.
Cập nhật kho thường xuyên theo thực thể (web): `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/kb_entity_update/SKILL.md`. Rà và sửa lỗi kho: `.agents/skills/kb_auditor/SKILL.md`. Nạp từ research vault của một tập (Pha 2b): `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/kb_ingest/SKILL.md`. Đề xuất chủ đề hằng ngày (bản thiết kế): `/Users/pro16/Documents/VideoProject/GocNhinPodcast/.agents/skills/daily_scout/SKILL.md`.
Kho `kb_main` dùng chung cho GocNhinPodcast và Dong_Chay. Script ở `/Users/pro16/Documents/VideoProject/GocNhinPodcast/scripts/` (gọi bằng đường dẫn tuyệt đối, chạy từ thư mục kênh).
1. **Pha 1:** trước khi vẽ bàn cờ, hỏi kho theo thứ tự: `kbq evidence <các mã trọng tâm + khối/đối thủ trực tiếp>` TRƯỚC (tầng cơ chế: giao dịch, phụ thuộc, quản lý, so sánh giữa các thực thể — loại bằng chứng dễ sót nhất nếu tra từng thực thể), rồi `kbq entity`, `kbq links <mã> 2`, `kbq facts <mã> [nhóm]`. Dữ kiện lấy từ kho ghi kèm mã `OBS-…`. Mỗi dữ kiện nối tới mọi bên tham gia (cạnh INVOLVES), nên `facts` của một thực thể có cả dữ kiện của bên khác mà nó tham gia. Sau bản đồ nền: đặt ≥ 3 giả thuyết cạnh tranh và lập ma trận bằng chứng trong `00_bang_gia_thuyet.md` (`.agents/workflows/build_global_vision.md` Bước 2b); chạy `kbaudit --check-evidence` ngay sau Pha 1, không đợi Pha 4.
2. **Pha 1b — Kiểm kê hiểu biết:** `kbaudit <slug> <mã trọng tâm...> [--moi "tên chưa có trong danh mục"]` → `01b_knowledge_audit.md` (ma trận phủ + danh sách GAP + các tập cũ đã làm) và `01c_evidence_dossier.md` (hồ sơ bằng chứng liên-thực-thể, có câu nguồn + URL, đọc được như vault; user soát tập bằng file này thay cho việc đọc kho). Chạy lại `kbaudit` giữ nguyên mục E đã điền. Điền mục E (luận điểm Pha 1 → mã OBS đỡ; chưa đỡ thì thêm GAP). Chỉ dữ kiện có mã OBS mới tính là "đã biết"; hiểu biết sẵn có của model không tính.
2c. **Sau Pha 4 (Outline) và sau Pha 8 (Merge):** `kbaudit --check-evidence <slug>` → `01c_evidence_unused.md`: bằng chứng liên-thực-thể trong hồ sơ mà tập chưa dẫn. Claude soát: dữ kiện nào đỡ, bác, hoặc làm rõ luận điểm mà tập bỏ qua thì sửa Outline/chapter trước khi đi tiếp; ghi kết luận ngắn vào `00_pipeline_operator_log.md`.
3. **Pha 2:** chỉ nghiên cứu các GAP. Mỗi prompt trong `02_research_plan.md` ghi mã GAP nó lấp; ô ✅ dùng thẳng kho, không nghiên cứu lại. Kiểm: `kbaudit --check-plan <slug>` phải ra ĐẠT trước khi nạp nguồn. Chỗ trống lộ ra giữa chừng thì thêm GAP mới, không chờ.
4. **Pha 2b — Cập nhật kho (tự động nạp, user chốt 30/09/2026):** ngay sau khi Pha 2 xong (vault NotebookLM, kết quả web search trong `research_raw/`) và `load_file.py --check` ra ĐẠT, Claude tự làm, KHÔNG cần dừng hỏi user mỗi đợt:
   1. Soát mẫu 5-10 dữ kiện đối chiếu câu nguồn gốc (idx.json) — không bịa, số khớp.
   2. Nạp theo đường chuẩn: `annotate_vault.py` → `index_vaults.py` → `load_file.py --orders` → `make_packs.py <tập>` → agent điền JSON theo gói (có cổng kiểm) → `load_file.py <json>` (phải ra KẾT QUẢ: ĐẠT; cổng nhật ký từ chối do đã đối chiếu tay sạch thì dùng `--reviewed "<ghi chú>"`, ghi rõ lý do từ chối và bằng chứng đã soát).
   3. Chạy lại `kbaudit <slug> …` để xác nhận GAP đã đóng.
   4. Chỉ DỪNG hỏi user khi: có thực thể mới cần thêm vào danh mục (`--moi`) mà không rõ có tập nào cần, dữ liệu chạm ranh giới tài chính/pháp lý nhạy cảm, hoặc mẫu đối chiếu phát hiện sai lệch/bịa — nêu rõ lý do cụ thể, không hỏi chung chung "có nạp không".
   Kết quả web search không đi qua NotebookLM thì chỉ nạp khi có URL + ngày và câu trích nguyên văn. Ghi lại đã nạp gì vào `00_pipeline_operator_log.md` (không cần hỏi trước, báo sau).
5. **Sau khi xuất bản — ghi bộ nhớ tập:** luận điểm, góc, khung, câu mở của tập vào `01_management/kg_research/episode_memory/data/` theo `08_episode_memory_spec.md`, nạp bằng `scripts/kg_epmem/load_one.py`.

## Chuỗi pha
0a Scouting chủ đề → 0b `qualify_topic` (`00_topic_qualification.md`) → Pha 1 Global Vision → Pha 1b Kiểm kê hiểu biết (`kbaudit`) → Pha 2 Deep Research (kế hoạch → nạp nguồn → trích xuất → research map/synthesis) → Pha 2b Cập nhật kho (hỏi user) → 3 Brief → 4 Outline → 5 Hook Lab → 6 Chapter Briefs + NST → 7 Chapters → 8 Merge → 9 Retention Audit → 10–11 QA → (12–14 chỉ khi user yêu cầu) → 15 Handoff → 16 Postmortem.

- **0a Scouting:** đọc `01_management/master_channel_analytics_audit.md` (mục VII: chân dung khán giả thật) và `01_management/topic_backlog.md`; ưu tiên dữ liệu kênh thật hơn giả định. Đầu ra: một entry trong backlog.

## Hóa thân chuyên gia (bắt buộc trước mỗi pha)
- Mở `SKILL.md` của pha (`.agents/skills/*`, kèm workflow `.agents/workflows/*`) và `.agents/specialist_map.md`; đọc đủ mọi persona được chỉ định. Chưa đọc thì không tạo output.
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
