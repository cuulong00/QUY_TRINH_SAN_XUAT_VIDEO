# antigravity_playbook.md

Antigravity phù hợp nếu bạn thích cảm giác mission-control, artifacts và orchestration nhiều agent. Cách an toàn nhất là dùng chính repo này làm nguồn sự thật, còn Antigravity chỉ là lớp điều phối và giao diện.

## Thiết lập
1. Mở repo này trong Antigravity.
2. Paste `ANTIGRAVITY_WORKSPACE_RULES.md` vào workspace rules / project rules.
3. Dùng các workflow trong `.agent/workflows/`.
4. Mỗi episode vẫn phải bám chặt vào các file state dưới `episodes/`.

## Flow chuẩn (16 Bước)
- `/init_episode` (Xử lý bước 1: Topic Qualification & bước 2: Brief)
- `/hook_lab` (Xử lý bước 3: Research Map & bước 4: Hook Lab)
- `/build_outline` (Xử lý bước 5: Thesis Map, bước 6: Retention Map, bước 7: Outline & bước 8: Chapter Briefs)
- `/write_chapter` (Xử lý bước 9: Viết từng chapter kèm Data Validation)
- `/merge_voiceover` (Xử lý bước 10: Final Merge)
- `/qa_review` (Xử lý bước 11: Editorial & Legal QA & bước 12: Oral QA)
- (Xử lý bước 13: Visual Map)
- (Xử lý bước 14: Slideshow Render khi đã có thư mục ảnh final)
- (Xử lý bước 15: Production Handoff & bước 16: Postmortem)

## Điều cần nhớ
- Antigravity giỏi ở plan -> execute -> verify.
- Nhưng chất lượng nội dung không nên gửi gắm cho chat memory của IDE.
- Hãy luôn yêu cầu agent đọc và cập nhật file state.
- Mọi kịch bản phải qua editorial QA trước khi xuất bản.
- Oral QA là gate riêng, không được gộp thành phần sửa câu chữ linh tinh ở cuối.
- Slideshow Render là bước sản xuất riêng, không được coi như đã xong ngay sau visual map.

## Khi nào Antigravity đặc biệt mạnh
- Khi bạn muốn review artifacts, tiến độ và kết quả từng pha.
- Khi bạn muốn giao diện trực quan hơn cho việc điều phối nhiều tác vụ.
- Khi bạn thích workflow-based vận hành hằng ngày.

## Khuyến nghị vận hành
- Luôn coi `CLAUDE.md` và file state là nguồn sự thật.
- Nếu workflow trong `.agent/workflows/` đang gộp nhiều pha, hãy xem đó là lớp compatibility chứ không phải canonical editorial model.
