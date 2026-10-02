# CHANGELOG — DNA GocNhinPodcast (`.agents/`, `00_core/`, `02_templates/`)

Mỗi sửa đổi DNA ghi một mục: ngày · mã việc · nội dung · lý do (mã V trong sổ vấn đề, mã R trong kế hoạch, hoặc mã Q trong bảng quyết định). Mục mới nhất ở trên. Bản thiết kế: `01_management/KE_HOACH_NANG_CAP_TOAN_DIEN_20261002_FABLE.md`.

## Quyết định nền (02/10/2026, user chốt tại `01_management/WO-00_BANG_QUYET_DINH_20261002.md`)
Q1 Loại B ≤2 case · Q2 Ch.2 theo loại đề tài · Q3 chương kết theo chế độ A/B, không CTA, không tóm tắt · Q4 trần chương 1.050 từ · Q5 <150 ký tự là giới hạn cứng, 8–15 từ là gợi ý · **Q6 cấm tả cảnh (user)** · **Q7 đọc toàn bộ chương trước (user)** · Q8 hook không kết luận · Q9 giữ `build_global_vision` · Q10 lăng kính phản biện chọn theo đề, dòng tiền không mặc định · Q11 bỏ tự chấm · **Q12 giữ ví dụ GSM, sửa đúng kho (user)** · Q13 luật cấu trúc một bản ở `script_architect` · Q14 thumbnail brief song song Pha 5 · Q15 rút gọn ≥30% · Q16 mặc định `kb_v2` (cổng 🔒) · Q17 Opus nộp patch, Fable áp.

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
