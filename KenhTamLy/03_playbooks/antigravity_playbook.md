# antigravity_playbook.md

Antigravity phù hợp nếu bạn thích cảm giác mission-control, artifacts và orchestration nhiều agent. Tuy nhiên, docs công khai về rule file và workflow system hiện vẫn rời rạc hơn Claude Code, nên cách an toàn nhất là dùng chính repo này làm nguồn sự thật, còn Antigravity chỉ là lớp điều phối và giao diện.

## Thiết lập
1. Mở repo này trong Antigravity.
2. Paste `ANTIGRAVITY_WORKSPACE_RULES.md` vào workspace rules / project rules.
3. Dùng các workflow trong `.agents/workflows/`.
4. Mỗi episode vẫn phải bám chặt vào các file state dưới `episodes/`.

## Cách dùng khuyến nghị
### Flow chuẩn
- Khởi tạo episode mới bằng terminal: `bash scripts/new_episode.sh [slug]`
- Kích hoạt workflow khởi tạo / brief
- Kích hoạt workflow hook lab
- Kích hoạt workflow outline
- Kích hoạt workflow write chapter cho từng chapter
- Kích hoạt workflow merge và QA

## Điều cần nhớ
- Antigravity giỏi ở plan -> execute -> verify.
- Nhưng chất lượng nội dung không nên gửi gắm cho chat memory của IDE.
- Hãy luôn yêu cầu agent đọc và cập nhật file state.

## Khi nào Antigravity đặc biệt mạnh
- Khi bạn muốn review artifacts, tiến độ và kết quả từng pha.
- Khi bạn muốn giao diện trực quan hơn cho việc điều phối nhiều tác vụ.
- Khi bạn thích workflow-based vận hành hằng ngày.