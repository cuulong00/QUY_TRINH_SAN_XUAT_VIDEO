---
name: capcut-master-editor
description: Master Video Editor & Cinematic Director Skill for CapCut Desktop (macOS). Use when creating, assembling, styling, or auditing CapCut video projects, managing multi-track audio/video/subtitles, cutting on beat, applying Ken Burns dynamics, and exporting broadcast-quality drafts.
---

# CapCut Master Editor Skill

This skill equips the Agent with broadcast-quality video editing capabilities on **CapCut Desktop (macOS)** using the deterministic `capcut-cli` engine and standard Python synchronization tools.

## Core Capabilities
1. **Audio Master Clock Synchronization:** Aligning AI/human voiceovers with video clips and sentence-level subtitles with zero microsecond drift.
2. **Documentary Visual Pacing:** Cắt nối clip phân cảnh khít theo từng câu thoại hoặc mốc ngắt ý (Cutting on Beat / Punctuation).
3. **Typography & Styling:** Subtitles styled in Amber Gold `#FFD700` or White `#FFFFFF` with high-contrast black border, centered at lower-third (`y: -0.6`).
4. **Motion Dynamics (Ken Burns):** Adding subtle pan/zoom keyframes to static or short video clips.
5. **Quality Audit & Pre-flight:** Running `capcut lint` and `capcut register` to prevent relink prompts in CapCut 9.x+ on macOS.
6. **Channel Awareness & BGM Harmonization:** Automatically identifies target YouTube channel (`GocNhinPodcast`, `Dong_Chay`, `HieuBietHon`) and applies dedicated, seamless background music (e.g. `nhac-nen-goc-nhin.mp3` at ~3% volume for Góc Nhìn Podcast).
7. **Rigorous 3-Tier Audio Separation:** Bắt buộc loại bỏ hoàn toàn audio stream khỏi video clips AI B-roll bằng ffmpeg (`-an -c:v copy`), đồng thời cấu hình `has_audio: false` và `has_sound_separated: true` trong draft materials, không bao giờ chỉ hạ âm lượng `volume: 0.0`.
8. **Disclaimer Outro Integration:** Tự động chèn video tuyên bố trách nhiệm (`tuyenbo_trachnhiem_<channel>_clean_audio.mp4`) ở cuối video cho Góc Nhìn Podcast và Dòng Chảy với audio sạch (`volume: 1.0`, `has_audio: true`), nhạc nền Track 2 loop trùm qua và fade out ở cuối.

## Standard 6-Step Workflow
1. **Làm sạch & Tách âm (Pre-flight & Strip Audio):** Chạy `ffmpeg -an -c:v copy` trên toàn bộ video clips AI B-roll trước khi đưa vào dự án để triệt tiêu vĩnh viễn tạp âm AI.
2. **Inspect & Measure:** Probe voiceover duration, identify channel context, và nạp timestamp từng từ (`timestamps.json`).
3. **Plan & Allocate:** Tính toán mốc cắt âm tiết chuẩn xác (Master Clock Rule) khớp vào khoảng lặng tự nhiên (Zero-Drift).
4. **Draft Spec Generation:** Xây dựng file `spec.json` với Video B-roll (volume 0.0) + Disclaimer Outro (volume 1.0), Voiceover (volume 1.0) và Channel BGM (volume 3% phủ trọn timeline).
5. **Compile & Post-Process:** Thực thi `capcut compile`, đồng bộ companion speeds, cấu hình `has_audio: false` cho AI B-roll, giữ `has_audio: true` cho Disclaimer Outro.
6. **Audit & Register:** Chạy `capcut register --materials --apply` và `capcut lint` (bắt buộc 0 errors, 0 warnings).



## References & Tools
- `references/api-reference.md`: Tra cứu toàn diện tham số, format thời gian, mã hiệu ứng.
- `references/pitfalls.md`: Cẩm nang phòng ngừa cạm bẫy CapCut (alpha keyframe, speed math, file locking).
- `scripts/ken-burns.sh`: Tự động tạo chuyển động zoom/pan điện ảnh.
- `scripts/sync_timing_engine.py`: Engine tính toán nhịp microsecond chuẩn xác.
