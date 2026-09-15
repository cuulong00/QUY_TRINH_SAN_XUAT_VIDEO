# episode_workflow.md

Đây là SOP vận hành theo từng pha để tạo một video xuất sắc.

## Luật nền của SOP này
- SOP này phải phục tùng `CLAUDE.md`.
- Không skill, workflow hay lệnh thực thi nào được phép mâu thuẫn với SOP này.
- Không được bypass contract đã khóa ở `01_brief.md`, `02_hook_pack.md`, `03_thesis_map.md`, `04_outline.md`.
- `final_voiceover.md` là bản merge bảo toàn kiến trúc, không phải nơi tái diễn giải lời hứa mở đầu.

## Nhánh riêng — Source Video Ingestion
Khi input là một video tham khảo hoặc source video:
1. Lấy transcript
2. Lưu transcript artifacts vào workspace đích
3. Đọc transcript
4. Viết `01_source_analysis.md`
5. Khóa differentiation strategy / angle shift
6. Chỉ sau đó mới vào brief hoặc short script

### Transcript artifacts bắt buộc
- `00_raw_transcript.txt`
- `00_transcript_meta.json`
- `00_transcript_segments.json`

Nếu transcript fail:
- `00_transcript_status.md`
- `00_transcript_error.json`

> CẤM suy đoán nội dung video chỉ từ URL hoặc tiêu đề. Transcript fail = dừng flow.

## Pha 0 — Khởi tạo
- Tạo folder episode mới.
- Xác định persona chính.
- Chưa viết script.

## Pha 1 — Brief
Mục tiêu: hiểu đúng người xem, pain, promise và behavioral lens.
Output: `01_brief.md`

Tiêu chí qua pha:
- pain đủ cụ thể
- promise đủ rõ
- tone đúng kênh
- behavioral lens và vùng cấm đủ rõ
- có Topic Depth Score
- khóa được `target_minutes_min/max`, `target_words_min/max`, `target_chapters_min/max`
- ghi rõ giả định words-per-minute dùng cho episode đó
- brief trở thành runtime contract cho các pha sau

## Pha 2 — Packaging + Hook Lab
Mục tiêu: khóa một lời hứa thống nhất giữa title, thumbnail và hook.
Output: `02_hook_pack.md`

Tiêu chí qua pha:
- có 1 hook final
- có 3 hook dự phòng
- có 5 mini re-hooks
- có intro kênh + CTA chính thức sau hook
- có alignment note giữa title, thumbnail và opening promise
- opening không phản bội packaging promise
- hook set phải thể hiện diversity của opening families, không được chỉ là nhiều biến thể của cùng một nhịp câu hỏi
- với episode misconception-correction hoặc corrective episode, phải thử ít nhất một direct clarification opening hoặc belief-flip opening
- rationale chọn hook final phải nói rõ vì sao family opening đó hợp với packaging promise, channel voice và loại episode

## Pha 3 — Thesis Map
Mục tiêu: khóa xương sống tư tưởng và payoff requirements trước khi dựng outline.
Output: `03_thesis_map.md`

Tiêu chí qua pha:
- thesis rõ
- anti-thesis rõ
- 3 open loops rõ
- ending destination rõ
- payoff requirements khớp với lời hứa đã mở từ hook/title/thumbnail

## Pha 4 — Retention-first Outline
Mục tiêu: biến thesis thành một hành trình giữ được người nghe từ đầu đến cuối.
Output: `04_outline.md`

Tiêu chí qua pha:
- mỗi chapter có nhiệm vụ khác nhau
- outline có retention moves rõ
- 3 open loops được map vào các chapter
- có cao trào nhận thức ở nửa sau
- có payoff map cho lời hứa title-thumbnail-hook
- mỗi chapter có `target_words` và vai trò cảm xúc rõ
- tổng budget chapter phải roll up khớp runtime contract từ brief
- outline phải cho thấy cumulative runtime plan, không chỉ ý tưởng chương

## Pha 5 — Viết từng chapter
Mục tiêu: viết chương theo state, không drift, không nói ra nhãn chương trong voiceover.
Output: `chapter_XX.md`, cập nhật `05_continuity_packet.md`, `06_claim_ledger.md`

Sau mỗi chapter phải kiểm:
- có lặp ví dụ cũ không
- có lặp ẩn dụ cũ không
- có advance lập luận không
- bridge có kéo được sang chapter sau không
- retention move của chapter có được thực thi không
- chapter có đạt band `target_words` đã khóa không
- chapter có đủ khối lượng triển khai cho vai trò của nó không, hay chỉ đúng ý nhưng quá mỏng
- chapter có ít nhất một micro-situation / life example / emotional turn phục vụ chapter function không
- chapter có loop progress hoặc payoff contribution rõ không

Trước khi qua pha merge phải kiểm toàn bộ chapter set:
- tổng số từ chapter set không được thấp hơn 90% `target_words_min` của brief nếu không có lý do được QA ghi nhận
- không chapter nào hụt sâu làm sập vai trò của nửa sau
- chapter set phải còn đủ peaks, rest point, và ending runway như outline đã khóa

## Pha 6 — Visual Planning
Mục tiêu: map script thành chiến lược visual ở cấp segment.
Output: `visual_map.csv`

Tiêu chí:
- xác định rõ visual role, motion style, source needs, editor notes
- đây là worksheet planning upstream, không phải source of truth cuối cho render

## Pha 7 — Scene Mapping
Mục tiêu: Dịch toàn bộ chữ thành các khối scene có thể đại diện bằng một hình ảnh duy nhất.
Output: `scene_map.json`

Tiêu chí:
- Hook zone: bắt buộc 1 câu = 1 ảnh
- Các phần khác: tối đa 3 câu = 1 ảnh
- Không gộp nếu làm mất reveal, contradiction, emotional turn, interpretive pivot, hoặc behavioral reframe
- `visual_summary` phải lột tả được toàn bộ linh hồn của các câu đã gộp vào, tuyệt đối không làm mất ý, rơi ý
- `visual_summary` phải đủ cụ thể để prompt generator dựng được hình
- Bắt buộc chạy qua Skill `build_scene_map`

## Pha 8 — Sinh Prompt AI
Mục tiêu: Dịch `scene_map.json` thành các block prompt tiếng Anh cho công cụ tạo ảnh.
Output: `visual_prompts.md`

Tiêu chí:
- 1 scene = 1 prompt block
- Prompt phải giữ trọn meaning của `visual_summary`, không chỉ chọn một motif đẹp mắt
- Prompt tuân thủ cấu trúc cinematic / photography
- Không chứa chữ text trong ảnh
- Bắt buộc chạy qua Skill `generate_visual_prompts`

## Pha 9 — QA cuối
QA cuối bắt buộc gồm:
- behavioral safety QA
- repetition QA (AI Self-Audit trực tiếp trên kịch bản, KHÔNG sử dụng API ASR/Whisper do Whisper tự động sửa lỗi và làm mượt khiến bỏ sót từ lặp)
- retention QA
- oral QA (AI Self-Audit quét các ký tự đặc biệt như &, chuỗi dấu ngoặc kép dày đặc, từ dễ phát âm sai để xử lý trước khi chạy TTS)
- packaging/alignment QA
- runtime compliance QA
- architecture coverage QA

Verdict QA chỉ có 2 loại:
- PASS
- BLOCK

## Pha 10 — Video Clip Finalization
Sau khi có prompt và user/operator chạy công cụ tạo video.
Output: thư mục `videos_final/`

Tiêu chí:
- số video clip khớp số scene hoặc có giải thích rõ khi lệch
- file video được đánh số/đặt tên theo thứ tự scene để ghép nối không bị lệch
- video không phản bội `visual_summary`

## Pha 11 — Video Render (CapCut Stitching - Manual)
Sau khi có video trong `videos_final/`.
Mục tiêu: dựng hậu kỳ và ghép nối các video clip thủ công trong phần mềm CapCut theo voiceover.
Output: `video/slideshow_base.mp4`

Tiêu chí:
- Nhập (import) toàn bộ video clip `.mp4` từ thư mục `videos_final/` vào CapCut.
- Cắt ghép, căn chỉnh thời lượng từng phân cảnh khớp hoàn hảo với nhịp điệu của file voiceover đã thu âm.
- Lồng nhạc nền theo sơ đồ Audio Landscape đã thiết lập.
- Xuất video base hoàn chỉnh ở định dạng 1080p, 30fps, codec H.264, tỷ lệ 16:9 và lưu vào đường dẫn `video/slideshow_base.mp4` để phục vụ các bước kiểm tra tiếp theo.
- Ghi lại nhật ký dựng và thông số trong `production_notes.md`.

## Pha 12 — Production Handoff
Mục tiêu: khóa ghi chú vận hành sau khi có clip và base video.
Output: `production_notes.md`

Tiêu chí:
- có `videos_final_dir`
- có `slideshow_output_file`
- có `slideshow_render_status`
- có asset / handoff notes đủ cho bước dựng tiếp theo

## Sau publish
- cập nhật `01_management/episode_registry.csv`
- ghi bài học vào `01_management/lessons_learned.md`
