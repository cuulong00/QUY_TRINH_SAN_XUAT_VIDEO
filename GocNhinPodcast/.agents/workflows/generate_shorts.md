# generate_shorts

## Mục tiêu
Workflow này điều phối mọi yêu cầu short-form trong repo GocNhinPodcast.
Nó là nhánh song song với long-form, không thay thế pipeline episode 16 pha.

## Khi nào dùng
Dùng workflow này khi user yêu cầu:
- làm YouTube Shorts
- cắt short từ episode dài
- làm short độc lập
- lên kế hoạch 3-5 shorts cho một episode
- viết short script / short metadata / short voiceover / short prompts

## Nguồn canonical bắt buộc
Trước khi làm bất kỳ bước nào, phải đọc:
- `00_core/shorts_style_guide.md`
- `00_core/shorts_map_template.md`
- `00_core/voice_dna.md`
- `CLAUDE.md`

Nếu xung đột, ưu tiên file canonical của repo.

## Bước 1 — Xác định source type
Phải chốt short thuộc một trong hai nhóm:

### A. Shorts phái sinh
Nguồn từ asset long-form đã có trong `episodes/[slug]/`.
Ví dụ nguồn hợp lệ:
- `02_hook_pack.md`
- `chapter_XX.md`
- `07_golden_lines.md`
- `final_voiceover.md`
- planning notes hoặc visuals liên quan

### B. Shorts độc lập
Nguồn nằm trong `shorts/standalone/[slug]/`.
Không phụ thuộc trực tiếp vào một episode dài.

## Bước 2 — Chọn loại Short
Mỗi short phải khóa một trong 6 loại canonical:
- `data_shock`
- `paradox`
- `comparison`
- `golden_quote`
- `hook_teaser`
- `mini_essay`

Không tạo hybrid lộn xộn nếu không có lý do rõ ràng.

## Bước 3 — Khóa planning artifact

### Nếu phái sinh từ episode
Dùng hoặc tạo:
- `episodes/[slug]/shorts/shorts_map.md`

### Nếu standalone
Dùng hoặc tạo:
- `shorts/standalone/[slug]/shorts_map.md`

Planning phải bám cấu trúc trong `00_core/shorts_map_template.md`.

## Bước 4 — Khóa output cần sản xuất
Tùy yêu cầu user, workflow này có thể đi tới:
- short planning map
- short script/spec file
- short voiceover file
- short metadata
- short visual prompts / scene notes

Ví dụ output hợp lệ:
- `shorts_map.md`
- `voiceover_XX_*.md`
- `metadata*.md`
- `video_prompts.txt`
- các spec files như `short_comparison.md`, `short_data_shock.md`, `short_paradox.md`

## Bước 5 — Quy tắc execution
- Mỗi short chỉ giữ 1 insight duy nhất.
- Mọi short từ 30 giây trở lên phải có 4 beat: Hook → Context → Insight → Twist/CTA.
- Nếu là short so sánh quốc gia hoặc chạm pride, bắt buộc có twist tỉnh táo ở cuối.
- Visual mặc định cho short là 9:16 và giữ lane Editorial Political Cartoon trừ khi user yêu cầu khác.

## Bước 6 — CTA logic
- **Short phái sinh:** CTA kéo về video dài / pinned comment / end screen
- **Short độc lập:** CTA kéo về kênh hoặc playlist

Không dùng CTA sáo rỗng kiểu xin follow cho có.

## Bước 7 — Scope mặc định
- Nếu user yêu cầu planning shorts cho một episode: mặc định nghĩ theo cụm **3-5 shorts**.
- Nếu user chỉ yêu cầu một short: chỉ làm đúng một short.

## Must not do
- Không ép short-form đi qua chapter workflow của long-form.
- Không biến short thành bản tóm tắt máy móc của video dài.
- Không dùng short để đưa buy/sell advice.
- Không dùng pride rỗng thay cho dữ liệu và twist.
- Không tạo output đi lệch `00_core/shorts_style_guide.md`.

## Kết quả mong muốn
Sau workflow này, request short-form phải được route sạch về đúng lane Shorts, với:
- source type rõ ràng
- short type rõ ràng
- planning artifact rõ ràng
- output file rõ ràng
- CTA và safety đúng chuẩn GocNhinPodcast
