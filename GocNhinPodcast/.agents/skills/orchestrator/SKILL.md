---
name: orchestrator
description: "Kỹ năng điều phối cho Claude: giao việc theo kết quả, chấm bằng cổng máy trước, trả lỗi có bằng chứng, giữ agent bận, ghi sổ vấn đề. Dùng ở mọi pha khi Claude giao cho Antigravity hoặc chấm."
---

# Orchestrator — Điều phối và chấm (WO-11)

Áp dụng khi Claude giao việc cho agent Antigravity (phòng `_agent_chat/<slug>/`) và khi chấm đầu ra của bất kỳ pha nào. Giao thức liên lạc chung: `/Users/pro16/Documents/VideoProject/.agents/rules/agent-collaboration.md`. Chuẩn viết phiếu cho Gemini: `/Users/pro16/Documents/VideoProject/.agents/rules/antigravity-prompt-standard.md`.

## 1. Vai
- **Agent viết** không chấm mình. **Cổng máy** chấm trước. **Claude** chấm sau, bằng tay, trên những gì máy không kiểm được (cách đọc riêng, lập trường, giọng). **User** quyết gate.
- Claude không viết nội dung thay agent, không tự vá file sản phẩm rồi im lặng (xem §4).

## 2. Phiếu giao việc (một phiếu, một tin)
Phiếu ghi **kết quả cần đạt**, không ghi cách làm. Dài 1–2 KB. Nhiệm vụ đặt cuối, sau ngữ cảnh.
1. Pha, file đầu ra, và câu "mở thẻ pha `.agents/phases/<pha>.md` và chỉ đọc những gì thẻ trỏ tới". Thẻ pha là đường duy nhất để luật pha tới agent: Antigravity chỉ tự nạp hiến pháp `.agents/AGENTS.md`, không tự nạp skill (đo 03/10/2026, `01_management/phan_tich_nap_pha7_20261003.md`).
2. Đầu vào đã chốt: `00_hien_chuong.md` (đề bài, chỉ đạo user, điều đã loại, N1–N5), `00_bang_gia_thuyet.md`, `00_so_du_kien.md`. Không chép lại nội dung các file đó vào phiếu.
3. Tiêu chí đạt, mỗi dòng một tiêu chí kiểm được: cổng kỹ thuật và dữ liệu máy kiểm được (ví dụ: "mọi số có mã M", "≥3 giả thuyết", "`kiem_pha.py --pha 4` ra ĐẠT") và tiêu chí chất chuyện theo khung 10 chỉ tiêu hai cấp (`00_core/narrative_craft_rubric.md`), có trích câu, không đếm.
4. Việc agent phải tự làm trước khi nộp: chạy `scripts/kiem_pha.py <slug> --pha <n>` và dán đầu ra vào tin báo. Pre-flight log "đã đọc file nào" do agent tự khai không phải bằng chứng; Claude kiểm bằng `scripts/kiem_nap.py`.
5. Tin báo khi xong: ngắn, có đầu ra lệnh kiểm, liệt kê điều chưa chắc. Không nhận "đã xong" trống.
Không: viết sẵn lệnh CLI, khoanh sẵn nguồn, ép công cụ đọc, giới hạn số lần chạy cổng, hỏi tiến độ giữa chừng. Agent có trình duyệt, API và skill của nó.
Nếu thiết kế còn đang đổi thì chưa giao. Đổi giữa chừng thì gửi một `directive` nêu rõ chỗ sai là của Claude và nghĩa đúng.

## 3. Chấm (thứ tự bắt buộc)
1. Chạy `scripts/kiem_pha.py <slug> --pha <n>`. Lỗi dữ kiện (`SO-KHONG-NGUON`, `NHAN-ROI`, `TRICH-KHONG-THAY`, `HC-*`, `GT-*`, `SO-CHANDO`) → trả agent ngay (§4), không cần hỏi user. Cổng ra ĐẠT chưa có nghĩa là bài hay: agent có thể đọc mã cổng để viết cho qua.
2. Đọc nhật ký của agent trước khi gán nguyên nhân: `python3 scripts/kiem_nap.py <id> --tu <bước>` (rule nào được chèn, có bị cắt không, agent mở file nào). Kết luận "agent không đọc", "bị cắt đầu ra", "không tra kho" phải có số step làm bằng chứng (bài học V17).
3. Tự mở nguồn với mọi câu trích then chốt (URL, PDF): khớp nguyên văn, URL mở được, số đúng kỳ và phạm vi. Không tin lời báo "đã kiểm".
4. Đối chiếu hiến chương: tiêu đề, câu hỏi trung tâm nguyên văn, từ khóa đã loại, N3/N5.
5. Phép thử hướng phân tích: cách ghép dữ kiện có ra cách đọc khán giả chưa có không. Không bắt dữ kiện phải mới.
5b. Với lời thoại: đọc to vài đoạn. Trả lại chỗ vấp kèm câu đề xuất, theo luật "Viết Câu Cho Tai" (Chỉ tiêu IX của khung 10 chỉ tiêu).
5c. Chấm chất chuyện bằng khung 10 chỉ tiêu hai cấp (`00_core/narrative_craft_rubric.md`): với dàn ý chấm Phiếu A (do người khác ngoài người dựng outline chấm); với từng chương chấm mù Phiếu B độc lập (Critical Auditor hoặc Claude chấm, không dựa vào bản tự soi của người viết); với kịch bản hoàn chỉnh đối chiếu Phiếu A và Phiếu B theo quy trình 5 bước. Mọi điểm 4-5 và 1-2 bắt buộc trích câu dẫn chứng; không dùng phép đếm để đánh giá chất chuyện. Chỉ tiêu nào chưa đạt thì ra lệnh sửa chỉ rõ chương, chỉ tiêu và câu lỗi.
6. Trình user vài dòng: đạt gì, lỗi gì, điều còn ngỏ. Gate do user quyết.

## 4. Trả lỗi và giữ agent bận
- Tin `failed`: mục có số, mỗi mục một dòng, kèm bằng chứng (file:dòng, mã OBS, câu nguyên văn nguồn). Yêu cầu tin báo sửa kèm bằng chứng máy kiểm được: `grep` câu cũ = 0, câu mới ở dòng số, đầu ra `kiem_pha.py`.
- Tối đa 5 tin cho một việc; vòng sửa theo `max_rework` trong `session.json`.
- Lỗi lặp → thành một dòng trong phiếu mẫu cho lần sau, không chỉ sửa trong tập.
- Agent xong thì phiếu đã có việc tiếp. Không để agent rảnh chờ tin; không hỏi tiến độ, nhìn file đầu ra.
- Đầu ra nghi bịa (URL 404, câu trích không khớp): hỏi agent nguồn và cách làm, cách ly file, giao lại rõ hơn. Không dừng agent làm mặc định.
- Claude không tự vá file sản phẩm rồi im lặng. Ngoại lệ duy nhất: `episode_registry.csv` và `00_pipeline_operator_log.md` (hook chỉ nhận Edit/Write của Claude).

## 5. Sống chết và xoay vòng
- Agent im: đọc `max(idx)` của bảng `steps` hai lần cách 30–60 giây. Tăng → còn sống. Đứng → chuyển hàng đợi sang agent khác ngay.
- Hội thoại gần đầy (~200k token): xoay theo `KHOI_TAO_AGENT_MOI.md`; viết bàn giao cho chính Claude.
- Theo dõi hộp thư bằng `Monitor` trên `mailbox.jsonl`, bật lại khi hết hạn; không dùng vòng `sleep`.

## 6. Sổ vấn đề
Mỗi lỗi phát hiện khi chấm ghi ngay vào `01_management/so_van_de/SO_VAN_DE_<slug>.md` theo khối: mã, pha, tầng (NẠP / TỔ CHỨC / CÔNG CỤ ĐỌC / AGENT DÙNG / ĐIỀU PHỐI / HẠ TẦNG), hiện tượng có bằng chứng, bản chất (chưa xác minh thì ghi GIẢ THUYẾT), hướng xử lý theo cơ chế chung, trạng thái. Cuối lượt gom theo bản chất để ra việc nâng cấp; sửa DNA ghi `.agents/CHANGELOG.md`.
