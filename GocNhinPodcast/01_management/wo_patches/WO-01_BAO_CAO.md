# WO-01 · Báo cáo nộp Fable (Opus, 02/10/2026)

Viết cho: Fable kiểm và áp patch. File DNA thật chưa bị đụng; mọi sửa nằm trong `WO-01.patch`.

## Đã làm
27 chỗ sửa trên 10 file, theo lựa chọn ở `WO-00_BANG_QUYET_DINH_20261002.md`:

| Q | Lựa chọn | File | Sửa |
|---|---|---|---|
| Q1 | B: Loại B tối đa 2 case | `build_outline.md:123`, `build_brief.md:63` | "đúng 1" / "tối đa 1" → trỏ `content_principles` §5 (A/B 2, C 3, ≤3 phút/case) |
| Q2 | B: Ch.2 theo loại đề tài | `rules/chapter-writing.md` | "Chapter 2 Contract BẮT BUỘC nối đời sống" → trỏ `content_principles` §2; quy tắc 3 phút lấy bản chung (con số mới / phép loại suy / câu hỏi phản biện), bỏ "liên hệ đời sống" |
| Q3 | B: chương kết theo chế độ A/B, không CTA, không tóm tắt | `longform_blueprint` §3 (chương kết), §10, §13 (2 dòng checklist) | Bỏ "đóng toàn bộ open loops", "action framework", "CTA dẫn video tiếp"; trỏ `stance_and_judgment` §1, §8 và `AGENTS.md` mục 4 |
| Q4 | B: trần 1.050 từ | `longform_blueprint` §11 | "tối đa ~2.5 phút" → trỏ ngân sách outline, trần 1.050 từ, tách chương khi vượt |
| Q5 | B: <150 ký tự là cứng, 8–15 từ là gợi ý | `longform_blueprint` §12 | Ghi rõ giới hạn cứng và gợi ý nhịp không bắt buộc |
| Q6 | B: cấm tả cảnh (user chốt) | `masterpiece_quality_standard` (mục tiêu 4, sở cứ Chiaroscuro, 5.1, 5.3, bảng hạng), `chapter_quality_standard` (§1, §2.4, 2.3, bảng hạng, mẫu báo cáo) | Tiêu chí "gợi hình điện ảnh / Mind's Eye / Chiaroscuro" → "Cụ thể bằng dữ kiện, không tả cảnh"; sức căng = hai dữ kiện đối nghịch. Giữ nguyên số điểm (6) để không vỡ thang trước WO-10 |
| Q7 | A: đọc toàn bộ chương trước (user chốt) | `rules/chapter-writing.md`, `AGENTS.md:254`, `chapter_writer` (tiêu đề + câu dẫn Rolling Context), `content-os-pipeline.md:109` | Rule đổi thành đọc toàn bộ; lý do "1 triệu token Gemini 3.8 Flash" → "kịch bản chỉ vài nghìn từ" |
| Q8 | B: hook không kết luận | `golden_samples/golden_hook.md` #3 + checklist | "Lập trường rõ" → "cách đọc riêng qua nghịch lý và câu hỏi, chưa kết luận", trỏ `stance` §8 |

## Lệnh kiểm và đầu ra (chạy trên bản nháp ghép vào bản sao toàn bộ `.agents/` (trừ tools), `00_core/`, `02_templates/`)

```
$ python3 WO-01_apply.py <nháp>
số sửa: 27 lỗi: 0          # mỗi chuỗi cũ phải xuất hiện đúng 1 lần mới sửa

$ bash WO-01_check.sh <cây nháp>
== Q1 case study 1 cho B
00_core/longform_blueprint.md:127  "Tối đa 1 case study ... mỗi chương, và không quá 2 case (Loại A/B)"   # hợp lệ: 1/chương, 2/video
00_core/longform_blueprint.md:189  "tối đa 1 case mỗi chương, ≤ 2–3 case trong toàn video"               # hợp lệ
== Q2 Ch.2 B ép đời sống        (0 dòng)
== Q3 đóng toàn bộ loop / CTA chương kết
00_core/longform_blueprint.md:150  "Không CTA ở chương kết..."                                            # dòng mới, hợp lệ
== Q4 2.5 phút                   (0 dòng)
== Q5 8-15 từ bắt buộc
the_shorts_strategist.md:34, the_short_script_writer.md:23     # lane Shorts, ngoài phạm vi long-form
longform_blueprint.md:280                                      # dòng mới, đã ghi "không bắt buộc"
== Q6 gợi hình / chiaroscuro văn
(còn lại toàn bộ là luật HÌNH ẢNH, không phải lời văn — xem "Ngoài phạm vi")
== Q7 không đọc lại toàn bộ      (0 dòng)
== Q8 hook lập trường            (voice_dna.md:16 nói giọng kênh có lập trường; không phải luật hook, hợp lệ)

$ patch -p1 --dry-run < WO-01.patch     # trên repo thật
patching file ... (10 file, không lỗi, không hunk lệch)
```

## Ngoài phạm vi WO-01, phát hiện khi quét (đề xuất giao vào WO sau)
1. **Mâu thuẫn hình ảnh mới:** `AGENTS.md:363` dạy "chiaroscuro lighting, deep noir shadows" trong khi `visual_style_guide.md:58`, `visual_prompter` dòng 33 và 116, `the_visual_storyteller.md:45` cấm đúng các từ đó; `thumbnail_style_guide.md:28` cũng dùng "chiaroscuro". → WO-13 (hoặc WO-05).
2. Các câu gắn model còn lại ("Gemini 3.8 Flash có xu hướng hành văn trang trọng", `AGENTS.md:256`, `chapter_writer` dòng 79 và 187, `content-os-pipeline.md:117`) không thuộc lý do đọc toàn bộ → WO-05.
3. **Q13 (luật cấu trúc lặp ở persona) chưa được gán WO nào trong kế hoạch.** Đề xuất gộp vào WO-05.
4. `longform_blueprint` §2 và §15 ("Loại A và B ... nói về CHÍNH HỌ", "bước hành động cụ thể (Loại A/B)") và `golden_hook.md` #5 ("gắn túi tiền") cố ý để lại cho WO-02 đúng như kế hoạch, dù cùng file.

## Dòng CHANGELOG đề xuất
`2026-10-02 · WO-01 · Gom luật Q1–Q8 về một nơi (10 file, 27 chỗ). Q1 case Loại B ≤2; Q2 Ch.2 theo loại; Q3 chương kết theo chế độ A/B, không CTA; Q4 trần 1.050 từ; Q5 <150 ký tự cứng; Q6 cấm tả cảnh, gỡ tiêu chí gợi hình; Q7 đọc toàn bộ chương trước; Q8 hook không kết luận. Nguồn: WO-00, R1.`

## File nộp
- `01_management/wo_patches/WO-01.patch` (274 dòng, 22 hunk)
- `01_management/wo_patches/WO-01_apply.py` (sinh lại patch từ bản gốc)
- `01_management/wo_patches/WO-01_check.sh` (quét mâu thuẫn trên cây bất kỳ)
