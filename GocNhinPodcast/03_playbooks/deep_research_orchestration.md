# deep_research_orchestration.md — Từ ý tưởng đến kế hoạch Deep Research

> Dùng ở Pha 2, sau khi `01_global_vision_synthesis.md` đã được duyệt.
> **Phân vai (user chốt 26/09/2026):** Antigravity lập `02_research_plan.md` và tự gọi NotebookLM qua API. Claude **không tự soạn kế hoạch**; Claude dùng các Bước A–D bên dưới làm **checklist duyệt** kế hoạch của Antigravity, và dùng Bước F để audit vault sau khi nạp.
> **Số lượng không cố định:** số prompt nạp nguồn và số câu trích xuất co giãn theo độ phức tạp đề tài (số chủ thể, số quốc gia, số lớp tranh cãi). Con số 5 prompt / 8–12 câu trong tài liệu chỉ là mức tham chiếu. Khi duyệt, Claude kiểm số lượng có tương xứng với ma trận phủ không: thiếu thì lộ điểm mù, thừa thì loãng nguồn và tốn quota NotebookLM.
> Checklist duyệt nhanh: (1) các prompt phủ đủ 5 câu hỏi bản thể học, không nhồi một query khổng lồ; (2) mỗi claim chịu lực có cả nguồn ủng hộ lẫn phản biện trong ma trận phủ; (3) có thực thể neo + từ khóa song ngữ; (4) Prompt 5 gọi đích danh loại phản biện (kiểm toán, chuyên gia đối lập, case thất bại); (5) câu trích xuất gắn với claim/Target Evidence Checklist và các câu hỏi lớn của Pha 1 (nhắm vào cả số liệu lẫn vật chứng thực tế VC-xx, yêu cầu liệt kê đủ các phía khi số liệu mâu thuẫn); (6) bám đúng góc đã khóa ở `00_topic_qualification.md`, không trôi sang đề tài lân cận.

## Vì sao khâu này quyết định chất lượng
NotebookLM nạp nguồn theo đúng những gì được hỏi. Kế hoạch lệch thì vault đầy nguồn đúng chủ đề nhưng sai câu hỏi; kế hoạch thiếu chiều thì kịch bản chỉ có một phía và Devil's Chapter thành hình thức. Sửa ở đây rẻ hơn sửa ở chapter gấp nhiều lần.

## Đầu vào bắt buộc
- `00_topic_qualification.md`: persona, niềm tin sai, góc đã khóa.
- `01_global_vision_synthesis.md`: bàn cờ 4 tầng, 5 câu hỏi scoping, Target Evidence Checklist.
- Các file xác minh đã có (dữ kiện ĐÚNG/SAI/KHÔNG RÕ). Mục KHÔNG RÕ là danh sách điểm mù có sẵn.

## Bước A — Phân rã ý tưởng thành câu hỏi nghiên cứu
Viết ra, ngắn gọn, trước khi soạn bất kỳ prompt nào:
1. **Thesis tạm** (1 câu), **niềm tin sai** cần đánh đổ, **antithesis mạnh nhất** (steelman của phía bên kia).
2. **Danh sách chủ thể** (nhà nước, doanh nghiệp, đối tác nước ngoài, người dân/ngành liên quan) và câu hỏi động lực của từng chủ thể: họ chịu áp lực gì, được gì, mất gì.
3. **5–8 claim chịu lực**: những khẳng định mà kịch bản sẽ phải đứng lên. Mỗi claim cần một số liệu chính thống và ít nhất một nguồn phản biện.
4. **Điểm mù đã biết**: các mục KHÔNG RÕ từ lần xác minh trước.

## Bước B — Ma trận phủ (Coverage Matrix)
Dòng = 5 câu hỏi bản thể học. Cột = loại bằng chứng bắt buộc. Mỗi ô ghi ngắn "cần tìm gì". Ô trống là điểm mù; phải có prompt bao phủ nó hoặc ghi rõ lý do bỏ.

| | Văn bản pháp lý có số hiệu | Số liệu định lượng chính thống | Vật chứng thực tế (VC-xx có ngày giờ, chủ thể, nguồn) | Phân tích quốc tế | Phản biện độc lập / kiểm toán | Case so sánh |
|---|---|---|---|---|---|---|
| 1. Entity Anchors & Anatomy | | | | | | |
| 2. Arena, Circuit & Flows | | | | | | |
| 3. Incentives & Survival | | | | | | |
| 4. Governing Laws & Paradoxes | | | | | | |
| 5. Contested Evidence & Failures | | | | | | |

Kiểm tra trước khi đi tiếp: mỗi claim chịu lực ở Bước A nằm trong ít nhất một ô có cả nguồn ủng hộ lẫn nguồn phản biện.

## Bước C — Soạn 5 prompt nạp nguồn
Mỗi prompt ứng với đúng một dòng của ma trận. Cấu trúc một prompt tốt:
- **Phạm vi:** địa lý, khung thời gian (ưu tiên 2024–2026; dữ liệu cũ chỉ dùng cho so sánh lịch sử, nói rõ).
- **Thực thể neo và từ khóa song ngữ:** tên riêng tiếng Việt + tiếng Anh (thêm tên gốc nếu là đối tác Trung Quốc, Nhật, Hàn), số hiệu văn bản nếu đã biết.
- **Loại nguồn ưu tiên:** cổng Chính phủ/Quốc hội, báo cáo bộ ngành, báo cáo tài chính, Reuters/Nikkei/Bloomberg/FT, báo cáo World Bank/ADB/JICA, nghiên cứu học thuật.
- **Loại nguồn loại trừ:** nhóm Facebook, blog vô danh, trang tổng hợp lại tin không ghi nguồn.
- **Câu hỏi dẫn:** 3–5 câu cụ thể mà nguồn tìm được phải trả lời.

Lỗi thường gặp cần tránh:
- Nhồi cả đề tài vào một query lớn (nguồn loãng, nông).
- Từ khóa chung chung không có thực thể neo.
- Chỉ dùng tiếng Việt, bỏ sót nguồn quốc tế.
- Prompt 5 viết mơ hồ kiểu "rủi ro và thách thức". Phải gọi đích danh loại phản biện: báo cáo kiểm toán/thanh tra, chuyên gia độc lập phản đối, dự án tương tự đội vốn/chậm tiến độ/thất bại, số liệu hai bên mâu thuẫn.

## Bước D — Soạn 8–12 câu hỏi trích xuất
- Mỗi câu gắn với một claim chịu lực hoặc một mục của Target Evidence Checklist; ghi rõ gắn với cái nào.
- Bổ sung câu hỏi trích xuất nhắm vào vật chứng thực tế (quyết định, văn bản, công trình, khoảnh khắc có ngày giờ và chủ thể đứng sau) để trả lời các câu hỏi lớn của Pha 1; cấm cảnh dựng lại hay nhân vật bịa.
- Yêu cầu đầu ra dạng bảng: chỉ số | giá trị | thời điểm | nguồn.
- Luôn thêm: "Nếu các nguồn mâu thuẫn, liệt kê đủ các phía kèm nguồn; không tự chọn một con số."
- Ít nhất 2 câu hỏi dành riêng cho phía phản biện và case thất bại.

## Bước E — Chạy trên NotebookLM (Claude gọi CLI trực tiếp)
Dùng hồ sơ đăng nhập mặc định (không đặt `NOTEBOOKLM_HOME`).
```bash
NLM=/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm
$NLM auth check --test --json                       # cần token_fetch: true
$NLM create "GocNhin_[slug]" --json                 # lưu .notebook.id vào episodes/[slug]/.notebook_id
$NLM source add-research --prompt-file prompt_1.txt -n <id> --mode deep --import-all --timeout 1800 --json
# lặp tuần tự prompt_2 … prompt_5; chạy nền, không poll
$NLM source list -n <id> --json > episodes/[slug]/research_vault/00_source_index.json
$NLM ask --prompt-file q_01.txt -n <id> --json > episodes/[slug]/research_vault/q_01.json
```
- Các file prompt và câu hỏi đặt trong `episodes/[slug]/research_vault/_queries/`.
- `00_source_index.json` dùng để đối chiếu citation (source_id) sang URL khi audit.

## Bước F — Audit vault (Claude)
1. **Độ mới:** số liệu có mốc thời gian, ưu tiên 2024–2026.
2. **Tầng nguồn:** Tầng 1 (văn bản nhà nước, báo cáo tài chính, tổ chức quốc tế, hãng tin lớn) > Tầng 2 (báo chí chính thống trong nước) > Tầng 3 (loại bỏ: mạng xã hội, blog vô danh).
3. **Ma trận phủ:** tô lại ma trận Bước B bằng dữ liệu thật; ô nào vẫn trống là lỗ hổng.
4. **Cặp bất đồng:** đánh dấu số liệu mâu thuẫn giữa các nguồn; đây là nguyên liệu cho Contested Data & Trade-offs Ledger.
5. **Vòng bổ sung:** tối đa 2 lần `add-research` nhắm đúng lỗ hổng. Sau đó vẫn thiếu thì ghi KHÔNG RÕ, và kịch bản không được đứng trên claim đó.
6. **Kho vật chứng (`VC-01` đến `VC-XX`):** kiểm tra xem mỗi câu hỏi lớn của Pha 1 đã có vật chứng thực tế đi kèm chưa (vật chứng mô tả 1 câu, ngày giờ, chủ thể và điều họ muốn, nguồn mở được kèm câu nguyên văn, câu hỏi Pha 1 mà nó trả lời). Cấm cảnh dựng lại hay nhân vật bịa. Không bắt buộc với tập đang chạy trước ngày 06/10/2026.

## Kỷ luật token
- Claude không đọc fulltext nguồn; chỉ đọc file trong `research_vault/`, dùng grep khi cần tìm một con số.
- Việc tra web ngoài NotebookLM (ví dụ lượt xem YouTube, tin vài ngày gần nhất) giao Antigravity/user theo `.agents/rules/orchestration-protocol.md`.
