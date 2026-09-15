Xây dựng Thesis Map, Retention Map, Outline và Chapter Briefs (Pha 5–8).

Arguments: `$ARGUMENTS` (slug của tập video)

Workflow:
1. Xác định target slug của tập video từ `$ARGUMENTS`. Nếu chưa có, hỏi user.
2. Đọc các tài liệu trước khi viết:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/core_references.md`
   - `.claude/rules/quality_constraints.md`
   - all files in `00_core/`
   - `episodes/[slug]/03_brief.md` (Chiến lược brief đã được duyệt)
   - `episodes/[slug]/04_hook_pack.md` (Hook pack đã được duyệt)
3. Kích hoạt chuyên gia **Script Architect** và hóa thân vào persona `the_behavioral_psychologist.md` + `the_narrative_director.md`.
4. Tạo hoặc cập nhật đồng loạt các file sau:
   - `episodes/[slug]/05_thesis_map.md` (Pha 5)
   - `episodes/[slug]/06_retention_map.md` (Pha 6)
   - `episodes/[slug]/07_outline.md` (Pha 7)
   - `episodes/[slug]/08_chapter_briefs.md` (Pha 8)
5. Thiết lập chi tiết cho từng file:
   - **05_thesis_map.md**: Khóa luận đề trung tâm, phản đề (anti-thesis), các luận điểm phụ (sub-claims), 3 vòng lặp mở (open loops), và các ranh giới khoa học (scientific boundaries) cho tập này.
   - **06_retention_map.md**: Xác định điểm rơi nhận thức, điểm lật cơ chế, các vị trí đặt mid-video rehooks, đường cong năng lượng (energy curve) và dự báo rủi ro tụt tương tác (fatigue risk zones).
   - **07_outline.md**: Dàn ý chi tiết các chương (chapter_01 -> chapter_10). Mỗi chương bao gồm: tiêu đề, vai trò lập luận, câu hỏi cốt lõi, claim chính, thí nghiệm/dữ liệu cần dùng (trỏ toạ độ `Vault Ref` từ `02_research_map.md`), emotional target, bridge in/out.
   - **08_chapter_briefs.md**: Tóm lược nhiệm vụ chi tiết của từng chương: listener state in/out, những thứ bắt buộc phải viết (must include), những điều cấm kỵ (must avoid), strongest line target.
6. Xác minh cấu trúc:
   - Không có hai chương kế tiếp nhau làm cùng một nhiệm vụ cảm xúc.
   - Luôn đi theo luồng: Nỗi đau (Pain) -> Cơ chế hoạt động (Mechanism) -> Tái định khung nhận thức/Thực hành hành vi (Reframe/Action Plan). Tránh rơi vào lý thuyết suông.
   - Đảm bảo ranh giới khoa học được giữ vững, không chẩn đoán bệnh lý bừa bãi.
7. 🛑 **CHECKPOINT:** Dừng lại gửi cụm file dàn ý này (từ Pha 5 đến Pha 8) cho user duyệt. Tuyệt đối không tự ý viết prose kịch bản chương khi chưa được duyệt dàn ý.
8. Trả về báo cáo tóm tắt cấu trúc dàn ý mới và các file đã tạo.
