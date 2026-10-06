# Episode Template

Mỗi video là một thư mục riêng dưới `episodes/`.

## Cách tạo nhanh
```bash
bash scripts/new_episode.sh ten-episode
```

## Trình tự dùng file
1. `01_global_vision_synthesis.md` (Pha 1: Master Systemic Topography & Global Vision)
2. `02_research_plan.md` → `02_research_map.md` & `02_research_synthesis.md` (Pha 2: Topographical Deep Research)
3. `03_brief.md` (Pha 3: Strategy Brief)
4. `07_outline.md` (Pha 4: Master Outline Engine — Biện chứng Hegel & Orientation Frame 45-60s)
5. `04_hook_pack.md` (Pha 5: Hook Lab — may đo bám sát Grand Payoff)
6. `08_chapter_briefs.md` & `09_narrative_state_tracker.md` (Pha 6: Chapter Briefs & NST)
7. `08_thumbnail_brief.md` (Thumbnail Brief — chốt song song với Pha 6/7, trước khi bàn giao)
8. Viết từng `chapter_XX.md` (Pha 7: Claim Ledger in ra chat theo PRE_FLIGHT_GATE.md, không lưu file riêng)
9. Gộp `voiceover.md` (Pha 8)
10. Kiểm toán `retention_bridge_audit.md` (Pha 9)
11. Chạy `10_compliance_report.md` (Pha 10 & 11) và hoàn tất `11_narrative_craft_scorecard.md` (người khác chấm dàn ý và người dựng tự soi ở Pha 4, tự soi rà soát câu yếu từng chương ở Pha 7, chấm mù ở Pha 10; chuẩn `00_core/narrative_craft_rubric.md`)
12. Tạo `visual_storyboard_blueprint_plus.md` (toàn tập) và 5 tệp cho từng chương: `chapter_XX_ban_do_nhip.md`, `chapter_XX_video_ai.md`, `chapter_XX_broll.json`, `chapter_XX_infographic.md`, `chapter_XX_bao_chi.md` (Pha 12 — Phân cảnh theo nhịp ý tuân thủ `.agents/contracts/i2v_nhip_y.md`)
13. `metadata.md` (SEO/YouTube metadata — hậu kịch bản)
14. Hoàn tất `production_notes.md` (Pha 15)
15. Sau publish hoặc review nội bộ, ghi `postmortem.md` (Pha 16)

## Required artifacts
- `01_global_vision_synthesis.md`
- `02_research_plan.md`
- `02_research_map.md`
- `02_research_synthesis.md`
- `03_brief.md`
- `04_hook_pack.md`
- `07_outline.md`
- `08_chapter_briefs.md`
- `08_thumbnail_brief.md`
- `09_narrative_state_tracker.md`
- `chapter_XX.md`
- `voiceover.md`
- `retention_bridge_audit.md`
- `10_compliance_report.md`
- `11_narrative_craft_scorecard.md` (bắt buộc với tập mới từ 06/10/2026; tập đã đăng không bổ sung)
- `metadata.md`
- `production_notes.md`
- `postmortem.md`

## Optional-supported artifacts (Chỉ khi có yêu cầu)
- `07_golden_lines.md`
- `visual_storyboard_blueprint.md`, `chapter_XX_visual.md`, `prompts_chapter_XX.txt` (nhánh Classic I2V)
- `visual_storyboard_blueprint_plus.md`, `chapter_XX_ban_do_nhip.md`, `chapter_XX_video_ai.md`, `chapter_XX_broll.json`, `chapter_XX_infographic.md`, `chapter_XX_bao_chi.md` (nhánh I2V+ Phân cảnh theo Nhịp Ý)
- `images_final/`
- `video/slideshow_base.mp4`

## Nguyên tắc
- Không viết full script one-shot từ topic thô.
- Mỗi pha chỉ cập nhật đúng file state của pha đó.
- Mọi claim trong `10_compliance_report.md` phải dùng taxonomy: `verified_data`, `market_analysis`, `opinion_commentary`.
- Mọi video đều phải có lưu ý nội dung bắt buộc: "Nội dung chia sẻ góc nhìn khách quan, mang tính thảo luận và xây dựng".
- Ranh giới nội dung tài chính (cấm khuyến nghị mua/bán, dự đoán giá...): xem `00_core/financial_boundaries.md`.
- Chỉ chạy slideshow render sau khi thư mục ảnh final đã được chốt thứ tự file.
