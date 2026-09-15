---
description: BƯỚC BẮT BUỘC để thu âm TTS voiceover cho tập phim X-Economics (từ chapter_XX.md) bằng hệ thống OmniVoice RunPod GPU chuẩn hóa.
---

# Quy trình Thu âm Voiceover (Record Voiceover)

> 🎙️ **HẠ TẦNG THU ÂM CHUẨN KÊNH (OMNIVOICE RUNPOD GPU):**
> - Toàn bộ động cơ TTS, mô hình giọng đọc, và **thư viện chuẩn hóa phiên âm** được tập trung quản lý tại `/Users/pro16/Documents/Code/TTS` (Single Source of Truth).
> - Tại dự án `X-Economics`, thu âm được kích hoạt nhanh chóng thông qua script cầu nối:
>   ```bash
>   python3 scripts/record_voiceover.py [episode_slug_hoặc_đường_dẫn]
>   ```
> - Script này tự động gọi sang engine `Code/TTS/run_production.py` với cấu hình chuẩn của kênh:
>   `--voice mc_nam_refined_short --speed 0.9 --temperature 0.5 --num-step 64 --no-cache`
> - Đảm bảo GPU RunPod tự động bật, xử lý batch toàn bộ chương, tải file `.wav` về thư mục `episodes/[slug]/audio/`, và tắt pod ngay lập tức để tiết kiệm chi phí.

---

## Các Bước Thực Hiện

### Bước 1: Xác định tập phim & Kiểm toán kịch bản (Pre-flight Audit)
1. Xác định `slug` của tập phim (ví dụ: `byd-vs-toyota-no-america-strategy` hoặc `episodes/byd-vs-toyota-no-america-strategy`).
2. Kiểm tra tính sẵn sàng của các file kịch bản `episodes/[slug]/chapter_XX.md`.
3. Chạy lệnh kiểm toán kịch bản trước khi thu âm:
   ```bash
   python3 scripts/record_voiceover.py [slug] --audit-only
   ```
   *Mục đích:* Quét phát hiện các câu quá dài (> 150 ký tự), các tiêu đề `# chapter_XX.md` còn sót, hoặc các đơn vị đo lường viết dính (`kilômét`, `kilôvôn`...).

### Bước 2: Tự động Chuẩn hóa Phiên âm (Normalize Scripts)
Nếu phát hiện kịch bản còn chứa từ ngữ chưa chuẩn hoặc tiêu đề markdown thừa, chạy lệnh tự động làm sạch và phiên âm:
```bash
python3 scripts/record_voiceover.py [slug] --normalize-only
```
*Lưu ý:* Thư viện phiên âm từ `Code/TTS` sẽ tự động tách âm đơn vị (`ki lô mét`, `ki lô vôn`, `héc ta`), chuẩn hóa từ viết tắt (`L D R`, `T O D`, `M T R`, `Pô-xcô`, `Sin-can-xen`, `Ben Phlai-béc`...), và xóa sạch các dòng `# chapter_XX.md`.

### Bước 3: Kích hoạt Lệnh Thu Âm (Production Run)
Chạy lệnh thu âm chính thức:
```bash
python3 scripts/record_voiceover.py [slug]
```

> **Lưu ý khi chạy qua AI Assistant / IDE:**
> Quá trình kết nối GPU RunPod và đọc toàn bộ các chương có thể kéo dài 2-5 phút. Bắt buộc đặt `WaitMsBeforeAsync: 10000` và `BypassSandbox: true` để tiến trình chạy nền an toàn.

#### Các tùy chọn nâng cao (nếu cần):
- **Thu âm lại một số chương cụ thể:**
  ```bash
  python3 scripts/record_voiceover.py [slug] --chapters 1,3
  ```
- **Tạo thư mục phiên bản mới (ví dụ audio_v2):**
  ```bash
  python3 scripts/record_voiceover.py [slug] --suffix v2
  ```
- **Thay đổi tốc độ hoặc giọng đọc:**
  ```bash
  python3 scripts/record_voiceover.py [slug] --voice mc_nam_short --speed 0.95
  ```

### Bước 4: Nghiệm thu & Kiểm tra File Âm thanh
1. Kiểm tra thư mục `episodes/[slug]/audio/`.
2. Đảm bảo đầy đủ các file âm thanh `chapter_01.wav` đến `chapter_XX.wav`.
3. Xác nhận **CHỈ CÓ FILE .WAV**, không để sót file phụ đề hay file rác.
4. Kiểm tra pod RunPod đã được STOPPED hoàn toàn (`Running pods: 0`).
5. Báo cáo tổng thời lượng âm thanh và dung lượng hoàn tất cho User.
