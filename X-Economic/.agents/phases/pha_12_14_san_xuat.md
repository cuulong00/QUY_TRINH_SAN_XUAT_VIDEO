# Thẻ Pha 12-14: Hình ảnh, âm thanh, video, thu âm (chỉ khi user yêu cầu)

**Mục tiêu.** Chuyển hóa kịch bản các chương đã duyệt thành toàn bộ tài nguyên sản xuất nghe - nhìn (visual, audio, video footage, voiceover). **Các pha này không tự động chạy, chỉ kích hoạt khi User yêu cầu trực tiếp.**

## Hai điều cốt lõi cho sản xuất kênh X-Economy
Khắc phục triệt để nguyên nhân gốc kênh từng bị tắt kiếm tiền do hình ảnh thiếu chau chuốt và lệch tiếng:
1. **Chuyển động có chủ đích ở mọi cảnh, ảnh tĩnh chỉ là ngoại lệ có lý do:** Mọi phân cảnh phải có chuyển động thị giác rõ ràng (chuyển động quang học camera pan/dolly, vi vật lý môi trường, hoặc chuyển động đồ họa dữ liệu HyperFrames). Ảnh tĩnh chỉ là ngoại lệ có lý do giải trình cụ thể (như bản chụp văn kiện mật, điều ước mộc đỏ cần giữ tĩnh để người xem đọc chữ).
2. **Tiếng và hình khớp bằng giờ thật:** Thời lượng từng cảnh được xác định chính xác từ file âm thanh thật cộng nhận dạng giọng nói (Whisper alignment) tại thời điểm dựng, đối chiếu kiểm tra mã sha256 của file âm thanh, tuyệt đối không dùng bảng thời gian chép tay hay ước tính cảm tính.

## Đọc theo việc được giao
| Việc | Skill / Workflow | Tài liệu quy chuẩn bắt buộc |
|---|---|---|
| I2V+ phân cảnh theo nhịp ý (Pha 12) | `.agents/skills/visual_prompter_plus/SKILL.md`, `.agents/workflows/generate_visual_prompts_plus.md` | Hợp đồng kỹ thuật: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_nhip_y.md`; đầu vào là từng `chapter_XX.md`, tuyệt đối không đọc `voiceover.md` gộp; phong cách và bảng màu trỏ tới `00_core/visual_style_guide.md` |
| Săn tư liệu B-roll thực tế (Pha 14) | `.agents/skills/footage-hunter/SKILL.md` | Quy chuẩn VPOS: `/Users/pro16/Documents/VideoProject/.agents/rules/broll-production-standard.md`; hợp đồng: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_broll.md`; phụ lục bối cảnh và nguồn quốc tế: `.agents/reference/broll_the_gioi.md` |
| Dựng video I2V+ (infographic, broll, ghép chương, nền động, ghép tập) | Công cụ ở `/Users/pro16/Documents/VideoProject/.agents/tools/i2v/` | Quy trình chuẩn: `/Users/pro16/Documents/VideoProject/.agents/contracts/i2v_quy_trinh_dung_video.md` (sáu bước, một tập một màu nền, đồng bộ giờ thật, nghiệm thu, dọn dẹp) |
| Sản xuất video AI điện ảnh (Pha 14) | `.agents/skills/batch_video_generator/SKILL.md` | Pure Optical Camera Motion; Google Vids Omni Video Engine hoặc MiniMax H3 dự phòng |
| m thanh & Nhạc nền (Pha 13) | `.agents/skills/music_composer/SKILL.md` | Thiết kế không gian âm thanh, drop và khoảng lặng; xuất `music_prompts.txt` |
| Thu âm Voiceover TTS | `.agents/workflows/record_voiceover.md` | Tốc độ đọc chuẩn 223-235 từ/phút; chuẩn âm thanh EBU R128 Loudnorm |

## Luật cứng của nhóm pha sản xuất
1. **Quy tắc đầu vào:** Pha 12 làm cuốn chiếu độc lập theo từng chương, đầu vào là các tệp `chapter_XX.md`. Tuyệt đối không đọc tệp `voiceover.md` gộp.
2. **Không sinh prompt bằng code:** Toàn bộ prompt ảnh, video và mô tả đồ họa phải do chính Agent biên soạn dựa trên ngữ cảnh lập luận; tuyệt đối cấm dùng script lặp code để tự động sinh prompt hàng loạt.
3. **An toàn nhân sự & danh tính:** Tuyệt đối không dùng AI dựng ảnh hay video của người thật. Với video AI bối cảnh, áp dụng Delta-Motion Prompting: chỉ mô tả chuyển động camera và môi trường vật lý, không tả lại nhân vật để tránh biến dạng.
4. **Khóa Cương vực Chủ quyền Biển Đảo:** Bất kỳ phân cảnh hoặc bản đồ nào có lãnh thổ Việt Nam bắt buộc phải mô tả đầy đủ: Quần đảo Hoàng Sa, Quần đảo Trường Sa, Đảo Phú Quốc, Côn Đảo; tuyệt đối cấm đường lưỡi bò phi pháp.
5. **Cách ly thoại:** Prompt sinh ảnh và video không bao giờ chứa nguyên văn câu thoại thuyết minh; prompt chỉ thuần túy mô tả không gian, ánh sáng, vật thể và chất liệu điện ảnh.
6. **Khóa thời lượng B-roll thực chứng:** Toàn bộ clip B-roll thực tế bắt buộc đạt thời lượng tối thiểu từ 5.0s đến 8.0s (chuẩn 5.5s - 7.0s); cấm tuyệt đối cắt B-roll dưới 5 giây. Tước 100% âm thanh gốc (-an); né tránh vùng chết MC 0-8s đầu clip; ưu tiên kênh chính chủ của doanh nghiệp/tổ chức.
7. **Kỷ luật dựng video:** Mọi lệnh render, tải, ghép là lệnh đồng bộ in `KET_QUA:`, không dùng lệnh chờ ngầm; một tập một màu nền từ đầu đến cuối; số liệu trên màn hình lấy từ kịch bản hoặc sổ claim của tập.

## Dừng
User duyệt Visual Storyboard Blueprint trước khi sinh prompt chi tiết; duyệt video base và audio trước khi hoàn thiện sản phẩm.
