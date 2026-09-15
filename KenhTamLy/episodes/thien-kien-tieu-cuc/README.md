# Episode Template

Mỗi video là một thư mục riêng dưới `episodes/`.

## Cách tạo nhanh
```bash
bash scripts/new_episode.sh ten-episode
```

## Trình tự dùng file
1. Điền `01_brief.md`
2. Tạo `02_hook_pack.md` với hook final, intro kênh, CTA mềm sau hook, và alignment giữa title-thumbnail-hook
3. Tạo `03_thesis_map.md`
4. Tạo `04_outline.md` theo retention-first outline
5. Viết từng `chapter_XX.md`
6. Sau mỗi chapter, cập nhật `05_continuity_packet.md` và `06_claim_ledger.md`
7. Tạo `final_voiceover.md`
8. Chốt `08_thumbnail_brief.md` và `09_youtube_metadata.md`
9. Cuối cùng tạo `visual_map.csv`

## Nguyên tắc bắt buộc
- `02_hook_pack.md` phải khóa được một lời hứa thống nhất giữa title, thumbnail và hook.
- Intro kênh và CTA phải nằm ngay sau hook, nhưng vẫn giữ cảm giác một dòng voiceover liền mạch.
- `04_outline.md` không chỉ là dàn ý logic; nó phải map được retention moves, open loops, và payoff targets.
- Voiceover cuối cùng không đọc ra các nhãn chương; chapter chỉ là cấu trúc sản xuất nội bộ.
