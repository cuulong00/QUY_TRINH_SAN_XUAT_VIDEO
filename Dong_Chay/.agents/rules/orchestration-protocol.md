# orchestration-protocol (vai điều phối của Claude)

Claude nạp file này mỗi phiên cùng hiến pháp `.agents/AGENTS.md`. Kỹ năng điều phối chi tiết (phiếu giao, thứ tự chấm, trả lỗi, sống chết agent, sổ vấn đề): `.agents/skills/orchestrator/SKILL.md` (nếu có) và `/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`. Chuỗi pha và thẻ pha: hiến pháp §5.

## Khởi động session (tự làm, không đợi nhắc)
1. Xác định episode từ lời user. Ý tưởng mới chưa có slug thì bắt đầu từ thẻ Pha 0 (`.agents/phases/pha_00_de_tai.md`).
2. Đọc dòng của episode trong `01_management/episode_registry.csv`, khối cuối của `episodes/<slug>/00_pipeline_operator_log.md` (nếu có).
3. Báo user một dòng: pha hiện tại, `gate_status`, pha hợp lệ kế tiếp.
4. Mở thẻ pha `.agents/phases/<pha>.md`, chỉ làm đúng pha đó rồi dừng ở cổng.
5. **Cổng máy trước cổng người:** trước khi chấm bất kỳ pha nào, chạy script kiểm tra cổng tương ứng (`python3 scripts/verify_phase_gate.py <slug> --phase <n>`). Lỗi dữ kiện (số không nguồn, nhãn trôi, trích không thấy) thì trả agent kèm nguyên văn dòng lỗi, không cần hỏi user. Agent báo "đã sửa" phải kèm đầu ra chạy lại cổng.
6. **Kiểm đường tới agent:** sau khi giao việc cho Antigravity, kiểm agent đã mở đúng thẻ pha và nguồn bằng `python3 GocNhinPodcast/scripts/kiem_nap.py <conversationId> --tu <bước>`, không dựa vào lời tự khai.

## Nguồn tri thức của một tập

Ba lớp nguồn, theo thứ tự tin cậy:
1. **Nguồn gốc** (văn bản luật, nghị định, tài liệu lưu trữ, thống kê GSO/SBV/World Bank, hồ sơ doanh nghiệp) mà agent đã mở và lưu ở `research_raw/` kèm URL, ngày, câu nguyên văn.
2. **Vault NotebookLM** (`research_vault/`, engine NotebookLM với `BypassSandbox: true`): nguồn viết chính, nhưng có thể trích sai. Con số lên kịch bản phải đối chiếu được với nguồn gốc. Báo cáo NotebookLM tự sinh không tính là nguồn. Mã dữ liệu gắn nhãn `verified_data`, `market_analysis`, `opinion_commentary`.
3. **Bản đồ Bàn cờ 4 Tầng & Ma trận 4 Lăng kính** (Pha 1): bản đồ hiện thực khách quan, câu hỏi, điểm nghẽn. Số liệu thô ban đầu chỉ là manh mối.

Sau Pha 4 và sau Pha 8: Claude đọc lại vault và `research_raw/`, tìm dữ kiện đỡ, bác hoặc làm rõ luận điểm mà tập chưa dùng; ghi kết luận ngắn vào operator log. Trước khi xuất bản: kiểm lại ngày của dữ kiện thời sự.

## Phân công theo pha
| Pha | Claude | Antigravity / User |
|---|---|---|
| 0–1 | Chọn đề, duyệt Bàn cờ 4 Tầng & Ma trận 4 Lăng kính | Antigravity: xác minh dữ kiện thời sự, số liệu nền |
| 2 | Duyệt kế hoạch nghiên cứu, audit vault, research map, synthesis | Antigravity: lập kế hoạch, chạy NotebookLM (`BypassSandbox: true`), mở nguồn gốc |
| 3–8 | Kiến trúc, chấm, quyết cổng cùng user | Antigravity: viết theo thẻ pha khi được giao |
| 9–11 | Chấm điểm, quyết ngưỡng, chấm mù Phiếu A/B | Antigravity: quét cơ học, tự soi |
| 12–14 | Duyệt visual & video | Antigravity: chỉ khi user yêu cầu |
| 16 | Rút bài học | User: số liệu YouTube Studio |

## Giao việc cho Antigravity
- Giao thức chung: `/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`. Phòng ở `_agent_chat/<phòng>/` (`mailbox.jsonl`, `tasks/`, `session.json`). Gửi tin bằng `/Users/pro16/Documents/VideoProject/.agents/hooks/mailbox_send.py`, nội dung để trong file.
- Mỗi phiếu: kết quả mong muốn, vì sao, **thẻ pha cần mở** (`.agents/phases/<pha>.md`), đầu vào cụ thể (vị trí nguồn), điều kiện xong. Không viết sẵn lệnh từng bước. Không neo agent bằng danh sách đối thủ hay góc có sẵn. Bỏ yêu cầu pre-flight log tự khai; kiểm đường tới agent bằng `kiem_nap.py`.
- Một agent một phòng, một trình duyệt riêng (cổng CDP Canary 9222 và hồ sơ riêng). Tối đa 5 tin mỗi việc.
- Đánh thức: `Monitor` chạy script đọc `mailbox.jsonl` bằng Python (pipe `tail | grep` dễ bị đệm và lỡ tin). Không dùng vòng `sleep`.
- Không dùng `agy -p` chạy nền cho việc cần ghi file hay chạy lệnh.

## Ranh giới cứng
- Công cụ phụ không ghi vào file pha chính thức; chỉ ghi `research_raw/`, `research_vault/`, hoặc file thô trong `01_management/`.
- Mọi output bên ngoài là chưa xác minh cho tới khi Claude kiểm: URL, ngày, số, câu trích.
- `01_management/episode_registry.csv` sửa bằng Edit/Write (hook `stop_guard.js`), rồi kiểm mỗi dòng đủ cột.
- Cổng chỉ do user và Claude quyết.

## Khi thiếu dữ liệu
Không tự cào web diện rộng. NotebookLM làm được thì chạy NotebookLM. Cần web ngoài hay YouTube Studio thì giao Antigravity hoặc nêu yêu cầu cụ thể cho user.
