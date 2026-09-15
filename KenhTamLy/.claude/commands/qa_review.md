Chạy quy trình kiểm định kịch bản chuyên sâu (Pha 10 - Scientific QA và Pha 11 - Oral QA).

Arguments: `$ARGUMENTS` (slug của tập video)

Workflow:
1. Xác định target slug của tập video từ `$ARGUMENTS`. Nếu chưa có, hỏi user.
2. Đọc các tài liệu hướng dẫn và files kịch bản:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - `.claude/rules/quality_constraints.md`
   - `.claude/rules/expert_panel.md`
   - `00_core/quality_rubric.md`
   - `00_core/anti_ai_isms.md`
   - `00_core/voiceover_style_guide.md`
   - `episodes/[slug]/03_brief.md`
   - `episodes/[slug]/07_outline.md`
   - `episodes/[slug]/10_claim_ledger.md`
   - `episodes/[slug]/02_research_map.md`
   - TẤT CẢ các file `chapter_XX.md` hiện có của tập video.
3. Kích hoạt vai trò **Scientific QA** (rà soát khoa học) và **Oral Polisher** (rà soát giọng nói):
   - Soạn thảo và chạy thử thách kiểm định qua các skill `.agents/skills/scientific_qa/SKILL.md` và `.agents/skills/oral_polisher/SKILL.md`.
4. Tiến hành **Pha 10 — Scientific QA** (tạo file `episodes/[slug]/scientific_qa.md`):
   - Kiểm tra tính chính xác của nguồn và thí nghiệm trỏ tới `02_research_map.md`.
   - Rà soát các cảnh báo an toàn sức khỏe tinh thần (mental health safety), tránh chẩn đoán bệnh lý cho người xem, tránh đưa ra cẩm nang trị liệu thay thế chuyên môn.
   - Kiểm định sự trung thực của bao bì (Packaging CTR) so với nội dung thực tế.
5. Tiến hành **Pha 11 — Oral QA** (tạo file `episodes/[slug]/oral_qa.md`):
   - Kiểm tra độ dài câu trực tiếp trên từng file `chapter_XX.md`. Phát hiện các câu vượt quá 150 ký tự (20-25 từ) để bắt buộc tách nhỏ.
   - Kiểm định nhịp ngắt nghỉ, dấu chấm, dấu phẩy hỗ trợ mô hình đọc TTS.
   - Rà soát các cầu nối chương (Bridge Audit) theo Luật But/Therefore và Subconscious Loop.
   - Quét từ vựng AI-isms sáo rỗng thông qua file `00_core/anti_ai_isms.md`.
   - **Thực hiện AI Script Self-Audit (Non-API):** Đọc kỹ văn bản từng chapter, rà soát triệt tiêu lỗi lặp từ cơ học (do Whisper không phát hiện được vì cơ chế tự động sửa của ASR), loại bỏ bẫy tự hồi quy (dấu ngoặc kép liên tiếp, các ký tự đặc biệt như `&` chuyển thành `và`).
6. Đánh giá chất lượng dựa trên `00_core/quality_rubric.md` để cho điểm số.
7. Đưa ra phán quyết (Verdict):
   - **PASS**: Đạt tiêu chuẩn, cho phép chuyển sang khâu audio/visual (visual map, scene map, slides render).
   - **BLOCK**: Có lỗi nghiêm trọng (bịa số liệu, câu hụt hơi nặng, pop-psychology, overclaim...). Chỉ rõ vị trí dòng và chương cần sửa.
8. 🛑 **CHECKPOINT:** Dừng lại gửi hai báo cáo QA (`scientific_qa.md` và `oral_qa.md`) xin duyệt của user.
9. Trả về báo cáo QA chi tiết cho từng chương kịch bản.
