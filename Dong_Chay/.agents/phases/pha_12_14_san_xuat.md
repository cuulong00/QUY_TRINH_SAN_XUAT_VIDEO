# Thẻ Pha 12–14: Hình ảnh, âm thanh, video, thu âm (chỉ khi user yêu cầu)

**Mục tiêu.** Chuyển hóa kịch bản các chương đã duyệt thành toàn bộ tài nguyên sản xuất nghe - nhìn (visual, audio, video footage, voiceover). **Các pha này không tự động chạy, chỉ kích hoạt khi User yêu cầu trực tiếp.**

## Đọc theo việc được giao
| Việc | Skill / Workflow | Tài liệu quy chuẩn bắt buộc |
|---|---|---|
| Blueprint & Kịch bản Thị giác (12A-12B) | `.agents/skills/visual_prompter/SKILL.md`, `.agents/workflows/generate_visual_prompts.md` | Đầu vào là các `chapter_XX.md`, tuyệt đối không đọc `voiceover.md`; `00_core/visual_style_guide.md` |
| I2V+ theo nhịp ý (12+) | `.agents/skills/visual_prompter_plus/SKILL.md`, `.agents/workflows/generate_visual_prompts_plus.md` | Tuân thủ Hợp đồng: `.agents/contracts/i2v_nhip_y.md`; đầu vào là từng `chapter_XX.md` |
| Prompt ảnh & video AI (12C) | `.agents/skills/visual_prompter/SKILL.md` | `.agents/rules/visual-asset-safety.md`; DNA thị giác điện ảnh Noir, Cinematic Documentary |
| m thanh & Nhạc nền (13) | `.agents/skills/music_composer/SKILL.md` | Persona `.agents/personas/the_cinematic_sonic_alchemist.md`; xuất file `episodes/<slug>/music_prompts.txt` |
| Săn tư liệu B-roll thực tế (14) | `.agents/skills/footage-hunter/SKILL.md` | Quy chuẩn VPOS: `/Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md` |
| Sản xuất video AI (14) | `.agents/skills/batch_video_generator/SKILL.md` | Pure Optical Camera Motion; Google Vids Omni Video Engine hoặc MiniMax H3 |
| Thu âm Voiceover TTS | `.agents/workflows/record_voiceover.md` | Tốc độ đọc chuẩn 223-235 từ/phút; chuẩn âm thanh EBU R128 Loudnorm |

## Luật cứng của nhóm pha này
1. **Quy tắc đầu vào:** Pha 12 làm cuốn chiếu độc lập theo từng chương, đầu vào là các tệp `chapter_XX.md`, tuyệt đối không đọc tệp `voiceover.md` gộp.
2. **Không sinh prompt bằng code máy móc:** Toàn bộ prompt ảnh và video phải do LLM viết theo suy luận nghệ thuật và ngữ cảnh điện ảnh; tuyệt đối cấm dùng script lặp code để tự động sinh prompt hàng loạt (hiến pháp §3.5).
3. **An toàn nhân sự & danh tính:** Tuyệt đối không gọi thẳng tên người thật trong prompt ảnh (`.agents/rules/visual-asset-safety.md`). Với video AI, áp dụng Delta-Motion Prompting: chỉ mô tả chuyển động camera, ánh sáng và vi vật lý, tuyệt đối không tả lại nhân vật để tránh biến dạng khuôn mặt.
4. **Khóa Cương vực Chủ quyền Biển Đảo:** Bất kỳ phân cảnh nào có xuất hiện bản đồ Việt Nam bắt buộc phải mô tả đầy đủ: Quần đảo Hoàng Sa, Quần đảo Trường Sa, Đảo Phú Quốc, Côn Đảo; tuyệt đối cấm đường lưỡi bò phi pháp.
5. **Cách ly thoại (Stage 3 Isolation):** Prompt sinh ảnh không bao giờ được chứa nguyên văn câu thoại thuyết minh; prompt chỉ thuần túy mô tả không gian, ánh sáng, vật thể và chất liệu điện ảnh.
6. **Khóa thời lượng B-roll thực chứng:** Toàn bộ clip B-roll thực tế bắt buộc đạt thời lượng tối thiểu từ 5.0s đến 8.0s (chuẩn 5.5s - 7.0s); cấm tuyệt đối cắt B-roll dưới 5 giây. Tước 100% âm thanh gốc (-an); né tránh vùng chết MC phòng thu 0-8s đầu clip; ưu tiên kênh YouTube chính chủ của doanh nghiệp/tổ chức.

## Dừng
User duyệt Visual Storyboard Blueprint trước khi sinh prompt chi tiết; duyệt video base và voiceover trước khi lắp ráp timeline hoàn thiện.
