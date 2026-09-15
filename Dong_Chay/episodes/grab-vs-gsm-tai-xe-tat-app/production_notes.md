<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/grab-vs-gsm-tai-xe-tat-app/production_notes.md
- Activated Persona: The Quality Czar (.agents/personas/the_quality_czar.md)
- Activated Skill: production-handoff (.agents/skills/production_handoff/SKILL.md)
- Source Documents Consulted:
  * episodes/grab-vs-gsm-tai-xe-tat-app/voiceover.md (Toàn văn kịch bản 65 đoạn, 100% <= 120 ký tự/câu)
  * episodes/grab-vs-gsm-tai-xe-tat-app/financial_qa.md (Kiểm toán số liệu tài chính)
  * episodes/grab-vs-gsm-tai-xe-tat-app/10_compliance_report.md (Báo cáo tuân thủ khẩu ngữ & TTS)
  * episodes/grab-vs-gsm-tai-xe-tat-app/scene_timing_map.json (229 phân cảnh Veo 3.1)
  * episodes/grab-vs-gsm-tai-xe-tat-app/music_prompts.txt (Cảnh quan âm thanh 7 chương)
  * episodes/grab-vs-gsm-tai-xe-tat-app/08_thumbnail_brief.md (Thumbnail 5 prompt A/B testing)
  * episodes/grab-vs-gsm-tai-xe-tat-app/09_youtube_metadata.md (SEO Title, Description, Tags)
- Execution Timestamp: 2026-09-11 10:37
-->

# Production Notes — Grab Đình Công: Các Hãng Gọi Xe Khác Thì Sao?

episode_slug: grab-vs-gsm-tai-xe-tat-app
voice_model: Google Gemini 3.1 Flash TTS (Vietnamese Male Deep Documentary / Chuyên gia tài chính điềm đạm)
voice_speed: 1.0x (Tốc độ đọc trung bình 3.81 từ/giây, nhịp thở tự nhiên bên bàn trà)
voice_direction: Giọng nam trầm, đĩnh đạc, sắc sảo và ấm áp. Viết cho đôi tai nghe: như một chuyên gia tài chính vĩ mô ngồi uống trà trò chuyện thân mật với một người bạn thông minh vào lúc 1 giờ sáng. Tuyệt đối không đọc kiểu hô hào tin tức kịch tính giật gân, không đạo mạo thuyết giáo.
pacing_profile: 
  - Chương 1: Dồn nén ngấm ngầm, đối lập nhịp điệu giữa sự bùng nổ của Grab và làn sóng tắt app trong đêm.
  - Chương 2: Nhịp chậm rãi, xót xa, tính toán lạnh lùng khi giải phẫu chiếc bẫy khấu hao cơ khí.
  - Chương 3: Nhịp điệu máy móc chính xác, đanh thép, tốc độ tăng nhẹ khi phân tích cỗ máy thâm dụng vốn Xanh SM.
  - Chương 4: Nhịp thực dụng, toan tính, lắng đọng khi nói về rào cản trần kính của Be Group.
  - Chương 5: Nhịp kiên cường, nhấc bổng bất ngờ khi giải mã sự phản công của Taxi truyền thống qua xe Hybrid.
  - Chương 6: Căng thẳng tăng tiến, đếm ngược thời gian hướng về hạn chót Net Zero 2030.
  - Chương 7: Lắng đọng, triết lý, mở rộng không gian suy ngẫm bên bàn trà lúc 5h30 sáng khi thành phố thức giấc.

pronunciation_watchlist:
  - "Grab" -> phát âm rõ "G-ráp" (không nuốt âm b).
  - "GSM / Xanh SM" -> "G-S-M" / "Xanh Ét-Em".
  - "EBITDA" -> "Ê-bít-đa" (E-bit-da).
  - "SEC" -> "Ủy ban Giao dịch Chứng khoán Mỹ" (đã được phiên âm trực tiếp trong văn bản).
  - "Hybrid" -> "Hai-bờ-rít" hoặc xe xăng lai điện.
  - "V-GREEN" -> "V-Gờ-rin".
  - "CCS2 / GBT" -> "C-C-S-Hai" và "G-B-T".
  - "Gojek" -> "Gô-dếch".

music_direction: 
  - Master Track: Ambient Noir tài chính vĩ mô, nhịp 72 BPM sub-bass pulse, khoét rỗng trung âm (mid-range scoop) nhường chỗ cho narration.
  - Track 1-7: Thiết kế bám sát từng cung bậc cảm xúc kịch bản theo tệp `music_prompts.txt`.
  - Drop & Silence: Câm lặng âm nhạc 1-2 giây tại các điểm truth-punch: "Đó là phần xác xe đang bị mài mòn từng ngày trên mặt đường nhựa", "Grab không phải công ty vận tải, họ là công ty phần mềm".

footage_notes: 
  - 229 video clip (mỗi clip 8 giây do Google Veo 3.1 tạo ra từ `prompts_chapter_01.txt` đến `prompts_chapter_07.txt`).
  - Toàn bộ clip tuân thủ Cinematic 2D Editorial Visual DNA: tông Modern Slate (#1E2530, #2A323D) và Warm Ivory Cream (#FAF7EE), điểm nhấn Amber Gold (#F59E0B) và Teal (#0D9488).
  - Khóa cú máy tĩnh Steady Shot cho 54 cảnh có chữ Text Overlay ở góc dưới bên trái cách mép đáy 25%.

asset_requests:
  - 5 ảnh tham chiếu nhân vật biểu tượng độ phân giải cao đã lưu tại `ref_images/`:
    * `ceo_anthony_tan.jpg` (Anthony Tan - WEF Davos)
    * `ceo_gsm_nguyen_van_thanh.jpg` (Nguyễn Văn Thanh - CEO GSM)
    * `be_leadership.jpg` (Vũ Hoàng Yến - CEO Be Group)
    * `vinasun_leadership.jpg` (Đặng Phước Thành - Vinasun)
    * `veteran_driver.jpg` (Tài xế công nghệ kỳ cựu dạn dày sương gió)

images_final_dir: episodes/grab-vs-gsm-tai-xe-tat-app/rendered_images/
slideshow_output_file: episodes/grab-vs-gsm-tai-xe-tat-app/final_video.mp4
slideshow_duration_per_image: 8.0s
slideshow_transition_duration: 0.5s (Smooth cross-dissolve)
slideshow_fps: 30
slideshow_seed: 42
slideshow_render_status: Ready for Batch Render via Flow Batch Studio

thumbnail_direction: 
  - Đã chốt Headline: "GRAB TẮT APP? | BÀN CỜ 3 TỶ $"
  - 5 phiên bản Prompt A/B testing chuyên sâu sẵn sàng trong `08_thumbnail_brief.md`.
  - Phiên bản đề xuất: Phiên bản 1 (Editorial Cover - Bìa Báo Phân Tích Chính Luận & Đối Lập Hai Thái Cực).

packaging_hooks: 
  - YouTube Title đề xuất: "Grab Đình Công: Các Hãng Gọi Xe Khác Thì Sao? | Bóc Trần Bàn Cờ 3 Tỷ USD"
  - Đầy đủ Description 7 Block, Timestamp, Tags, Hashtags và Pinned Comment sẵn sàng trong `09_youtube_metadata.md`.

legal_caution_notes: 
  - Tuân thủ 100% nguyên tắc YMYL (Your Money Your Life): Video phân tích cơ chế vận hành kinh tế khách quan, không phải tư vấn mua bán cổ phiếu hay lời khuyên đầu tư tài chính.
  - Không công kích cá nhân hay vi phạm quy định cạnh tranh; số liệu lấy từ Báo cáo tài chính SEC, Mordor Intelligence, Vinasun, Mai Linh và văn bản pháp luật chính thức (Nghị định 10/2020/NĐ-CP, Quyết định 876/QĐ-TTg).

publish_notes: 
  - Khung giờ xuất bản tối ưu: Thứ 5 hoặc Chủ Nhật, 18:00 - 20:00 (khung giờ vàng người đi làm và giới đầu tư theo dõi video dài).
  - Ghim ngay comment mồi tương tác đã chuẩn bị trong `09_youtube_metadata.md` trong 15 phút đầu tiên sau khi xuất bản.

postmortem_scheduled: true (Lên lịch review chỉ số CTR, AVD và Retention Curve sau 7-14 ngày theo `02_templates/postmortem_template.md`).
approved_for_production: YES (S-GRADE CERTIFIED BY THE QUALITY CZAR)
