# deep_research_orchestration.md — Từ ý tưởng đến kế hoạch Deep Research

> Dùng ở Pha 2 (Deep Research), sau khi bàn cờ Pha 1 đã được duyệt.
> **Phân vai:** Antigravity lập kế hoạch nghiên cứu và tự gọi NotebookLM qua API. Claude **không tự soạn kế hoạch**; Claude dùng các mục A–D bên dưới làm **checklist duyệt** kế hoạch của Antigravity, và dùng mục F để audit vault sau khi nạp nguồn.
> Đầu ra chính: file kế hoạch nghiên cứu của episode (xem `.agents/skills/deep_researcher/SKILL.md`).

## Vì sao khâu này quyết định chất lượng
NotebookLM nạp nguồn theo đúng những gì được hỏi. Kế hoạch lệch thì vault đầy nguồn đúng chủ đề nhưng sai câu hỏi; kế hoạch thiếu chiều thì kịch bản chỉ có một phía và phần phản biện thành hình thức. Sửa ở đây rẻ hơn sửa ở chapter gấp nhiều lần.

## Đầu vào bắt buộc
- File đánh giá chủ đề (persona, niềm tin sai/tranh luận steelman, góc đã khóa).
- File bàn cờ Pha 1 (5 câu hỏi bản thể học, Target Evidence Checklist / danh mục dữ liệu cần điều tra).
- Các file xác minh đã có (dữ kiện ĐÚNG/SAI/KHÔNG RÕ). Mục KHÔNG RÕ là danh sách điểm mù có sẵn.

## Checklist duyệt kế hoạch của Antigravity (Claude áp dụng, không tự soạn)
**Số lượng không cố định:** số prompt nạp nguồn và số câu trích xuất co giãn theo độ phức tạp đề tài (số chủ thể, số quốc gia, số lớp tranh cãi). Khi duyệt, kiểm số lượng có tương xứng với độ phức tạp thật không: thiếu thì lộ điểm mù, thừa thì loãng nguồn và tốn quota NotebookLM.

1. Các prompt phủ đủ 5 câu hỏi bản thể học (Entity Anchors, Arena & Circuit, Incentives & Survival, Governing Laws & Paradoxes, Contested Evidence & Dissent), không nhồi một query khổng lồ.
2. Mỗi claim chịu lực (khẳng định kịch bản sẽ phải đứng lên) có cả nguồn ủng hộ lẫn nguồn phản biện trong phạm vi tìm kiếm.
3. Mỗi prompt có thực thể neo bằng tên riêng và từ khóa song ngữ Việt–Anh; có phạm vi thời gian rõ (ưu tiên 2024–2026, dữ liệu cũ chỉ để so sánh lịch sử).
4. Khía cạnh phản biện/thất bại (Contested Evidence & Dissent) gọi tên cụ thể loại phản biện cần tìm: báo cáo kiểm toán/thanh tra, chuyên gia độc lập phản đối, case tương tự thất bại/đội vốn/chậm tiến độ. Không chấp nhận viết chung chung "rủi ro và thách thức".
5. Mỗi câu hỏi trích xuất gắn với một claim/mã dữ liệu cụ thể trong Target Evidence Checklist của Pha 1; có yêu cầu "nếu nguồn mâu thuẫn thì liệt kê đủ các phía kèm nguồn, không tự chọn một con số".
6. Bám đúng góc đã khóa ở phần đánh giá chủ đề, không trôi sang đề tài lân cận.
7. Loại nguồn ưu tiên/loại trừ được nêu rõ cho từng prompt (ưu tiên: cổng Chính phủ/Quốc hội, báo cáo tài chính, hãng tin lớn, tổ chức quốc tế, học thuật; loại trừ: mạng xã hội, blog vô danh, diễn đàn không kiểm chứng).

Sai bất kỳ điểm nào → ghi yêu cầu sửa cụ thể (không mơ hồ), gọi lại Antigravity, lặp tới khi đạt cả 7 điểm.

## Vận hành: Antigravity chạy, Claude dự phòng
1. Gọi `agy` lần 1 — chỉ lập kế hoạch, không chạy NotebookLM, không ghi file nếu quyền `write_file` chưa mở (yêu cầu trả lời qua chat, Claude tự lưu).
2. Claude duyệt theo 7 điểm trên.
3. Gọi `agy` lần 2 — chạy nền, tự gọi NotebookLM: tạo Master Notebook, nạp nguồn tuần tự từng prompt (`--mode deep --import-all`), rồi chạy các câu hỏi trích xuất, ghi kết quả ra `research_vault/`.
4. Nếu Antigravity chưa đủ quyền chạy lệnh/ghi file ở chế độ nền (xem `orchestration-protocol.md` mục "Antigravity — tình trạng quyền hiện tại"): Claude tự chạy trực tiếp bằng CLI NotebookLM (`/Users/pro16/Documents/VideoProject/X-Economic/.venv_notebooklm/bin/notebooklm`, hồ sơ mặc định `~/.notebooklm_home`), chạy nền, không poll trong hội thoại chính.
5. Claude audit vault (mục dưới) và viết file research map + synthesis.

## Audit vault (Claude, sau khi nạp nguồn xong)
1. **Độ mới:** số liệu có mốc thời gian, ưu tiên 2024–2026.
2. **Tầng nguồn:** Tầng 1 (văn bản nhà nước, báo cáo tài chính, tổ chức quốc tế, hãng tin lớn) > Tầng 2 (báo chí chính thống trong nước) > Tầng 3 (loại bỏ: mạng xã hội, blog vô danh).
3. **Độ phủ:** đối chiếu lại với Target Evidence Checklist của Pha 1 — mục nào vẫn trống là lỗ hổng.
4. **Cặp bất đồng:** đánh dấu số liệu mâu thuẫn giữa các nguồn; đây là nguyên liệu cho phần Dữ liệu Bất đồng & Đánh đổi.
5. **Vòng bổ sung:** tối đa 2 lần nạp thêm nhắm đúng lỗ hổng. Sau đó vẫn thiếu thì ghi KHÔNG RÕ, và kịch bản không được đứng trên claim đó.

## Kỷ luật token
- Claude không đọc fulltext nguồn; chỉ đọc file trong `research_vault/`, dùng grep khi cần tìm một con số.
- Việc tra web ngoài NotebookLM (tin tức vài ngày gần nhất, số liệu YouTube) giao Antigravity/user theo `orchestration-protocol.md`.
