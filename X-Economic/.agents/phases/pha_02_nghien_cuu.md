# Thẻ Pha 2: Topographical Deep Research (Nghiên cứu sâu thực chứng)

**Mục tiêu.** Khóa chặt backbone dữ liệu thực chứng từ Research Vault, giải mã các câu hỏi điều tra và điểm nghẽn của Tầng 4 Global Vision. Thiết lập Kho vật chứng (`VC-01` đến `VC-XX`) thực tế có nguồn gốc kiểm chứng (quyết định có số hiệu/ngày, văn bản pháp quy, công trình, khoảnh khắc đối đầu có thật). Xây dựng Contested Data & Trade-offs Ledger. Tuyệt đối không bịa đặt số liệu.

## Đọc, theo thứ tự
1. `episodes/<slug>/01_global_vision_synthesis.md` (Tầng 4: Target Evidence Checklist & Dissent Prompts).
2. `.agents/workflows/deep_research.md` và `.agents/skills/deep_researcher/SKILL.md` (các bước vận hành engine NotebookLM).
3. `03_playbooks/deep_research_orchestration.md`: Tiêu chuẩn nạp nguồn và kiểm duyệt hồ sơ bóc tách.
4. Khuôn: `02_templates/episode_template/02_research_plan.md`, `02_templates/episode_template/02_research_map.md`, `02_templates/episode_template/02_research_synthesis.md`.
5. Persona: `.agents/personas/the_policy_analyst.md`, `.agents/personas/the_macro_financial_researcher.md`, `.agents/personas/the_critical_auditor.md`.

## Không cần đọc
Skill viết chương, outline kịch bản, các file phong cách âm thanh/hình ảnh, `00_core/voice_dna.md`.

## Chuyên gia (Persona)
- `.agents/personas/the_macro_financial_researcher.md`: Chuyên gia Tài chính & Dữ liệu Vĩ mô.
- `.agents/personas/the_policy_analyst.md`: Chuyên gia Pháp chế & Thể chế.
- `.agents/personas/the_critical_auditor.md`: Kiểm toán Bằng chứng Đối kháng.

## Luật riêng (trỏ bản gốc)
- Chuẩn mực chứng cứ thực nghiệm (Grounded Evidence Mandate): `00_core/content_principles.md` §1.
- Không bịa số, không bịa trích dẫn. Nguồn NotebookLM tự sinh chỉ là manh mối, bắt buộc mở file gốc kiểm chứng.
- Kho vật chứng thực tế: lập danh mục `VC-01` đến `VC-XX` trong `episodes/<slug>/02_research_map.md`. Cấm nhân vật bịa, cấm hiện trường giả tưởng.

## Câu tự hỏi
- Kế hoạch nghiên cứu đã bao quát đủ các câu hỏi lớn và điểm nghẽn của Tầng 4 Global Vision chưa?
- Đã nạp đủ tối thiểu 10 nguồn khả dụng (ready) vào Master Notebook chưa?
- Đã có tối thiểu 5 file bóc tách chi tiết trong `episodes/<slug>/research_vault/` chưa?
- Các bằng chứng đối kháng (Counter-Thesis) và chi phí đánh đổi đã được ghi nhận sòng phẳng chưa?

## Giới hạn
`episodes/<slug>/02_research_synthesis.md` tối đa 3.000 từ (tối thiểu 1.000 từ).

## Đầu ra
`episodes/<slug>/02_research_plan.md`, `episodes/<slug>/research_vault/*.md`, `episodes/<slug>/02_research_map.md` (chứa Kho vật chứng `VC-xx`), `episodes/<slug>/02_research_synthesis.md`.

## Cổng và dừng
Chạy cổng kiểm toán máy: `python3 scripts/verify_phase_gate.py --phase 2 --episode <slug>` (bắt buộc PASS). User duyệt Research Map & Synthesis trước khi sang Pha 3.
