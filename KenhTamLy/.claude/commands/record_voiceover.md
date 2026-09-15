Thực hiện thu âm giọng đọc kịch bản qua hệ thống TTS.

Arguments: `$ARGUMENTS` (slug của tập video)

Workflow:
1. Xác định target slug của tập video từ `$ARGUMENTS`. Nếu chưa có, hỏi user.
2. Kiểm tra xem các file `chapter_XX.md` đã có đầy đủ và được kiểm định Scientific QA + Oral QA với verdict PASS chưa.
3. Đọc các tài liệu trước khi thu âm:
   - `CLAUDE.md`
   - `.claude/rules/script_production_flow.md`
   - all files `chapter_XX.md` trong thư mục tập video.
4. Chạy script thu âm TTS của repo (đọc tuần tự từng `chapter_XX.md` từ chapter_01 đến hết).
5. Giám sát quá trình xử lý từng chunk âm thanh của mô hình TTS. Ghi nhận các chunk bị lỗi hoặc không khớp thời gian.
6. Hỗ trợ chạy thu âm lại (retry) các chunk hoặc chương cụ thể bị lỗi, tránh việc chạy lại toàn bộ tập video gây lãng phí tài nguyên và chi phí API.
7. Xác nhận file âm thanh đầu ra cuối cùng được lưu trữ đúng vị trí trong thư mục tập video (ví dụ: `episodes/[slug]/audio/`).
8. Trả về báo cáo kết quả thu âm, đường dẫn file audio thành phẩm, và thống kê các chunk bị lỗi/sửa đổi.
