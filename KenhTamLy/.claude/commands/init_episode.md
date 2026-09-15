Khởi tạo thư mục làm việc cho một tập video mới (Pha 1 — Topic Qualification).

Arguments: `$ARGUMENTS` (chứa slug của tập video)

Workflow:
1. Xác định target slug của tập video từ `$ARGUMENTS`. Nếu chưa có, hỏi user.
2. Nếu thư mục `episodes/[slug]` chưa tồn tại, tạo mới bằng cách sao chép toàn bộ thư mục `02_templates/episode_template/`.
3. Thay thế toàn bộ placeholder `__EPISODE_SLUG__` trong các file vừa sao chép bằng slug thực tế.
4. Đọc các tài liệu trước khi viết:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/quality_constraints.md`
   - all files in `00_core/`
   - `.agents/personas/the_topic_strategist.md`
5. Đi qua Gate 1 (Topic Qualification Gate): Điền đầy đủ thông tin vào `episodes/[slug]/01_topic_qualification.md` dựa trên ý tưởng thô của tập video.
6. Xác định rõ: surface topic, hidden pain, false belief to attack, viral angle candidates.
7. 🛑 **CHECKPOINT:** Gửi file `01_topic_qualification.md` cho user duyệt. KHÔNG tự ý chuyển sang pha deep research khi chưa được duyệt chặng này.
8. Trả về nội dung file `01_topic_qualification.md` đã hoàn thiện và báo cáo kết quả.
