Chạy quy trình nghiên cứu sâu (Pha 2 — Data Mining & Verification) sử dụng NotebookLM MCP.

Arguments: `$ARGUMENTS` (slug của tập video)

Workflow:
1. Xác định target slug của tập video từ `$ARGUMENTS`. Nếu chưa có, hỏi user.
2. Đọc file `episodes/[slug]/.notebook_url` để lấy URL của Master Notebook. Nếu file chưa tồn tại hoặc rỗng, yêu cầu user cung cấp URL notebook hoặc tạo mới rồi ghi nhận vào file này. TUYỆT ĐỐI KHÔNG tự tiện tạo notebook mới làm phân mảnh tri thức.
3. Đọc các tài liệu hướng dẫn và persona trước khi bắt đầu:
   - `.agents/personas/the_research_scientist.md`
   - `.agents/skills/deep_researcher/SKILL.md`
   - `.agents/skills/notebooklm_librarian/SKILL.md`
4. Thực thi chặng 1 — Deep Research (Nạp nguồn):
   - Chạy `deep_research` ít nhất 6 lần (chủ đề thông thường) hoặc 9 lần (chuyên sâu thần kinh/tâm lý học lâm sàng).
   - Đảm bảo ≥ 50% query được thực hiện bằng tiếng Anh để thu thập tài liệu học thuật gốc (PubMed, Nature, APA...).
   - Bao phủ đủ các góc nhìn: Thesis (ủng hộ lý thuyết), Counter-Thesis (phản bác, giới hạn của lý thuyết), Context (ví dụ thực tế, thí nghiệm lâm sàng).
   - Kiểm đếm tổng số nguồn sau mỗi lần chạy. Đảm bảo tổng số nguồn trong notebook ≥ 40-60 nguồn.
5. Thực thi chặng 2 — Batch Extraction (Trích xuất):
   - Tạo thư mục `episodes/[slug]/research_vault/` nếu chưa có.
   - Thiết kế bộ câu hỏi chiến lược ≥ 8 câu thuộc 3 tầng: Thesis (≥3 câu), Counter-Thesis (≥2 câu), Context (≥2 câu).
   - Gọi tool `mcp_notebooklm-mcp_batch_to_vault` để lưu thẳng kết quả từ NotebookLM thành các file markdown trong thư mục `research_vault/`.
6. Thực thi chặng 3 — Verify & Cross (Xác minh):
   - Rà soát phương pháp thí nghiệm, cỡ mẫu thử, năm công bố (ưu tiên 2024-2026), loại bỏ các giả thuyết tâm lý học đại chúng lỗi thời.
   - Xác minh chéo đảm bảo mỗi claim khoa học quan trọng có ít nhất 2 nguồn xác thực độc lập.
7. Thực thi chặng 4 — Synthesize (Tổng hợp):
   - Tạo file `episodes/[slug]/02_research_map.md` theo mẫu chuẩn.
   - Điền đầy đủ các bảng dữ liệu: Thesis, Counter-Thesis, Cơ chế tâm lý hoạt động, Điểm mù & Giả định, Case Studies, Data Gaps.
   - **BẮT BUỘC:** Mỗi luận điểm trong Research Map phải có toạ độ `Vault Ref` (ví dụ: `001_mechanism.md` L15-L30) trỏ chính xác về dòng trong `research_vault/`.
8. 🛑 **CHECKPOINT:** Gửi file `02_research_map.md` cho user duyệt. KHÔNG tự ý chuyển sang pha tiếp theo khi chưa có sự đồng ý của user.
9. Trả về kết quả và file `02_research_map.md` đã hoàn thiện.
