# CHANGELOG — DNA GocNhinPodcast (`.agents/`, `00_core/`, `02_templates/`)

Mỗi sửa đổi DNA ghi một mục: ngày · mã việc · nội dung · lý do (mã V trong sổ vấn đề, mã R trong kế hoạch, hoặc mã Q trong bảng quyết định). Mục mới nhất ở trên. Bản thiết kế: `01_management/KE_HOACH_NANG_CAP_TOAN_DIEN_20261002_FABLE.md`.

## Quyết định nền (02/10/2026, user chốt tại `01_management/WO-00_BANG_QUYET_DINH_20261002.md`)
Q1 Loại B ≤2 case · Q2 Ch.2 theo loại đề tài · Q3 chương kết theo chế độ A/B, không CTA, không tóm tắt · Q4 trần chương 1.050 từ · Q5 <150 ký tự là giới hạn cứng, 8–15 từ là gợi ý · **Q6 cấm tả cảnh (user)** · **Q7 đọc toàn bộ chương trước (user)** · Q8 hook không kết luận · Q9 giữ `build_global_vision` · Q10 lăng kính phản biện chọn theo đề, dòng tiền không mặc định · Q11 bỏ tự chấm · **Q12 giữ ví dụ GSM, sửa đúng kho (user)** · Q13 luật cấu trúc một bản ở `script_architect` · Q14 thumbnail brief song song Pha 5 · Q15 rút gọn ≥30% · Q16 mặc định `kb_v2` (cổng 🔒) · Q17 Opus nộp patch, Fable áp.

## 2026-10-02 · WO-03 · Làm sạch ví dụ (Q12 = A: giữ ví dụ GSM, sửa đúng kho)
`00_core/stance_and_judgment.md`: 5 chỗ. "113 tỷ/ngày" (không có trong kho, phép chia tự làm) → chi phí lãi vay hợp nhất Vingroup 2025 = 29.160 tỷ (`OBS-0a95967c83f5df86`), kèm luật không tự chia "mỗi ngày" và không đặt số toàn tập đoàn cạnh một mảng; "SEC gọi đội taxi là phòng lái thử di động" → đúng phạm vi câu 424B3/F-1 (`OBS-70086fcb436a21a8`); "1.500 chiếc… gần như không chiếc nào đến tay người mua cá nhân" → hai nguồn 1.500/1.300 (`OBS-0a1f03ba501ff9f2`, `OBS-a93e5b03ae44a7b6`) + 28 xe bán lẻ 2024–2025 (`OBS-edd9166742f77150`); ví dụ kết bài bỏ khung "bảng cân đối trả tiền bao lâu" → câu hỏi cơ chế (khách đi xe thành người mua; luật chơi Đan Mạch/Hà Lan); ví dụ §1b bỏ "dòng tiền Vinhomes". 8 file ví dụ (`.agents/examples/*`, `golden_samples/golden_analysis`, `golden_transition`) thêm header: số lấy từ tập gdp-quy-1-2026, chỉ minh họa, không chép. Xóa 2 placeholder chưa từng điền và không ai tham chiếu: `skills/hook_engine/examples/golden_hook.md`, `skills/chapter_writer/examples/golden_chapter.md`. Phát hiện V31 (kho có hai số lãi vay 2025 lệch nhau). Nguồn: Q12, R3, V29.

## 2026-10-02 · WO-02 · Gỡ thiên lệch Loại A và khung tài chính
17 file, 42 chỗ (3 đợt). Q10: hội đồng phản biện đổi từ 3 lăng kính cố định (có dòng tiền mặc định) thành danh mục 5 lăng kính ở `AGENTS.md` (bản gốc duy nhất), chọn tối thiểu 2 theo nút N5 và ghi vào hiến chương; lăng kính dòng tiền chỉ bật cho đề tài doanh nghiệp/thị trường vốn. Mọi chỗ liệt kê cứng 3 lăng kính (`content-os-pipeline`, `the_critical_auditor`, `the_dialectic_architect`, `the_macro_strategist`, `script_architect`, `chapter_writer`, `strategy_council`, `compliance_council`, `quality_rubric`, template 01/07/08) → trỏ về `AGENTS.md`. R2: hook biến thể 2 "va chạm bảng cân đối" → "va chạm hai mô hình" (`hook_engine`, `the_viral_alchemist`); `golden_hook` #5 "gắn túi tiền" → điểm tựa theo loại A/B/C; `longform_blueprint` §2 Personal-First → điểm tựa theo loại, tách luật "Loại A và B" thành A và B riêng, §14 và §15 tách A/B; `retention_gate` Gate 1 và Gate 2 Loại B bỏ "áp lực chi phí, dòng tiền, biên lợi nhuận"; `masterpiece` 2.1, `chapter_quality` 2.2, `compliance_council` đối xứng 1-1 bỏ "điểm hòa vốn, BCTC" khỏi tiêu chí chung; `build_outline` Loại B Ch.2 "cơ chế chi phí" → bài toán doanh nghiệp/quốc gia. Nguồn: WO-00 Q10, R2, V15. Fable làm cả hai vai (user chốt bỏ luân phiên model); cổng máy: `wo_patches/WO-02*_apply.py` (mỗi chuỗi cũ đúng 1 lần), `WO-02_check.sh`.

## 2026-10-02 · WO-01 · Gom luật Q1–Q8 về một nơi
10 file, 27 chỗ: `AGENTS.md`, `rules/chapter-writing.md`, `rules/content-os-pipeline.md`, `skills/chapter_writer/SKILL.md`, `workflows/build_brief.md`, `workflows/build_outline.md`, `00_core/{longform_blueprint,masterpiece_quality_standard,chapter_quality_standard,golden_samples/golden_hook}.md`.
- Q1: "đúng 1 / tối đa 1 case Loại B" → trỏ `content_principles` §5.
- Q2: "Chapter 2 Contract nối đời sống" và quy tắc 3 phút → trỏ `content_principles` §2.
- Q3: chương kết trong `longform_blueprint` §3/§10/§13 → theo `stance_and_judgment` §1, §8; bỏ CTA chương kết (trỏ `AGENTS.md` mục 4).
- Q4: "~2,5 phút/chương" → trần 1.050 từ. Q5: 8–15 từ thành gợi ý, 150 ký tự là cứng.
- Q6: tiêu chí "gợi hình điện ảnh / Mind's Eye / Chiaroscuro" trong hai bộ chấm → "cụ thể bằng dữ kiện, không tả cảnh"; giữ nguyên số điểm tới WO-10.
- Q7: rule đọc toàn bộ chương trước; bỏ lý do gắn model ở 4 chỗ liên quan.
- Q8: `golden_hook` #3 "lập trường rõ" → "cách đọc riêng, chưa kết luận".
Nguồn: WO-00, R1. Patch và báo cáo: `01_management/wo_patches/WO-01*`. Opus soạn, Fable kiểm và áp.

## Trước 02/10/2026
- 2026-09-29: đợt rà DNA lớn, xem `01_management/dna_audit_20260929.md` (gộp `.claude/` về `.agents/`, tạo `stance_and_judgment.md`, thống nhất hằng số 223–235, một cổng chấm mỗi khâu, §3b anti_ai_isms).
- 2026-10-02 (Opus, trước kế hoạch): chẩn đoán 8 bản chất R1–R8 và sổ vấn đề V01–V30 từ tập thử gsm-chau-au; chưa sửa DNA.
