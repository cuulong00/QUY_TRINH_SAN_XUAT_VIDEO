# quality_stability_system.md

Muốn chất lượng ổn định, bạn phải tối ưu hệ thống chứ không tối ưu một prompt đơn lẻ.

## 0. Vai trò của file này
Đây là file định nghĩa triết lý gate, ổn định chất lượng, và learning loop của repo.
Nó không thay thế `CLAUDE.md` hay `episode_workflow.md`, nhưng là tiêu chuẩn để quyết định khi nào một output được đi tiếp hay phải bị chặn.

## 1. Single source of truth
Mọi quyết định quan trọng phải được ghi vào file, không để tồn tại chỉ trong chat.

## 2. State over memory
Agent có thể quên. File state không quên.

## 3. One phase at a time
Viết sai thường đến từ việc model bị yêu cầu làm quá nhiều thứ cùng lúc.

## 4. Review gates
Chỉ chuyển pha khi đạt tiêu chí qua pha.
Gate không chỉ là cảm giác “nghe ổn”, mà phải chặn được các trường hợp đúng ý nhưng sụp quy mô, lệch lời hứa, hoặc mất kiến trúc.

## 5. Encode learnings
Mỗi khi phát hiện lỗi lặp, lỗi tone, lỗi doctrinal, phải thêm vào `lessons_learned.md` hoặc cập nhật file lõi.

## 6. Reuse strong patterns
Hook tốt, transition tốt, ending tốt phải được chuẩn hóa vào core files.

## 7. Human approval points
Bạn nên duyệt tay ở 4 điểm:
- duyệt brief
- duyệt hook
- duyệt outline
- duyệt final voiceover

Tuy nhiên, human approval không thay thế hard gate.
Một output vẫn phải bị chặn nếu vi phạm runtime contract, lệch packaging promise, hoặc sụp architecture coverage.

## 8. Stability loop
Sau mỗi video:
- xem lại bình luận và retention
- ghi 3 điều hiệu quả
- ghi 3 điều yếu
- cập nhật core files nếu có pattern mới
- đối chiếu target runtime / drafted words / final words / preservation ratio để phát hiện drift hệ thống
- với packaging, đối chiếu thêm concept brief vs assembled thumbnail spec để phát hiện drift giữa prompt nền ảnh và bản thumbnail thực thi