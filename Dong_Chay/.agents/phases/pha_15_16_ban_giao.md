# Thẻ Pha 15–16: Bàn giao, metadata, Shorts & postmortem

**Mục tiêu.** Đóng gói hoàn chỉnh tập phim để xuất bản (Hồ sơ bàn giao Production Notes, siêu dữ liệu Metadata YouTube, gói Shorts phái sinh). Sau khi video lên sóng và có số liệu phân tích thực tế, tiến hành Postmortem để đúc kết bài học đưa ngược vào hệ thống DNA.

## Đọc theo việc được giao
| Việc | Skill / Workflow / Template | Persona / Tài liệu tham chiếu |
|---|---|---|
| Metadata YouTube (tiêu đề, mô tả, tags) | `.agents/skills/metadata_strategist/SKILL.md`, `00_core/youtube_seo_guide.md` | Persona `.agents/personas/the_algorithm_whisperer.md`; `00_core/thumbnail_style_guide.md` |
| Bàn giao sản xuất (Pha 15) | `.agents/skills/production_handoff/SKILL.md`, `.agents/workflows/production_handoff.md` | Đầu vào: `episodes/<slug>/10_compliance_report.md`, `episodes/<slug>/voiceover.md`, `episodes/<slug>/11_narrative_craft_scorecard.md` |
| Sản xuất Shorts phái sinh | `.agents/skills/shorts_producer/SKILL.md`, `00_core/shorts_style_guide.md` | Persona `.agents/personas/the_shorts_strategist.md`; cắt từ các cú lật đắt trong `voiceover.md` đã duyệt |
| Kiểm toán Postmortem (Pha 16) | `02_templates/postmortem_template.md` | Số liệu YouTube Studio do User cung cấp; `00_core/performance_benchmarks.md` |
| Quản trị & Phân tích kênh | `.agents/skills/channel_manager/SKILL.md` | Đọc dữ liệu AVD, CTR, Retention Curve và đề xuất chiến lược tối ưu |

## Cách làm & Luật riêng
1. **Chuẩn hóa Metadata:**
   - 100% tuân thủ `00_core/brand_safety_guidelines.md` và `00_core/financial_boundaries.md`.
   - Tiêu đề phải khơi gợi tò mò trí tuệ sâu sắc, tuyệt đối không dùng giật tít câu view rẻ tiền.
   - Phần mô tả video bắt buộc chứa đầy đủ: Tuyên bố miễn trừ trách nhiệm pháp lý (disclaimer), bảng phân đoạn thời gian (timestamps), và danh mục nguồn tài liệu tham khảo chính thức.
2. **Hồ sơ bàn giao (Production Notes):**
   - Tập hợp toàn bộ đường dẫn tài nguyên đã nghiệm thu (bản thu âm voiceover, bảng danh mục B-roll, video AI, đồ họa) vào `episodes/<slug>/production_notes.md`.
   - Đính kèm bảng tổng kết điểm kiểm định QA và phiếu chấm mù Narrative Craft.
3. **Quy tắc phái sinh Shorts:**
   - Shorts không phải là bản tóm tắt thu nhỏ của video dài. Mỗi video Short phải khai thác trọn vẹn MỘT nghịch lý, một con số bất ngờ hoặc một cú lật nhận thức duy nhất, có nhịp mở đầu giật gân trí tuệ trong 3 giây đầu.
4. **Quy trình Postmortem:**
   - Chỉ kích hoạt sau khi video đã phát hành tối thiểu 7 ngày và có đầy đủ báo cáo phân tích từ YouTube Studio.
   - Đối chiếu đường cong giữ chân thực tế (Retention Curve) với các điểm dự báo trong `episodes/<slug>/retention_bridge_audit.md`.
   - Bất kỳ bài học nào làm thay đổi quy trình phải được ghi vào `.agents/CHANGELOG.md` theo luật sửa DNA (hiến pháp §7): sửa trực tiếp tại bản gốc, không tạo thêm bản sao.
   - Tuyệt đối không có bước nạp dữ liệu thủ công sau tập vào knowledge base.

## Dừng
User duyệt trọn gói Metadata và Production Notes trước khi publish; Postmortem chỉ thực hiện khi đã có số liệu thực chứng từ YouTube Studio.
