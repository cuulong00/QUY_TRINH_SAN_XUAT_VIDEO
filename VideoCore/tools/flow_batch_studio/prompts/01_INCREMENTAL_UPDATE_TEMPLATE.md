# 🛡️ TEMPLATE CẬP NHẬT TÍNH NĂNG MỚI (CHỐNG GHI ĐÈ / REGRESSION LOCK)

Khi bạn muốn yêu cầu AI trong Google Flow bổ sung thêm tính năng hoặc sửa lỗi, **HÃY SAO CHÉP TOÀN BỘ KHỐI DƯỚI ĐÂY** và dán vào ô chat. Bạn chỉ cần điền yêu cầu mới vào mục `[NEW FEATURE REQUEST]`.

---

```markdown
[CRITICAL REGRESSION LOCK - DO NOT ALTER EXISTING CONFIGURATIONS]
Before implementing the new request, you MUST strictly preserve these exact constants and architecture:
1. Video Model Default: MUST REMAIN EXACTLY `Veo 3.1 - Lite [Lower Priority]`. Do not change or shorten to `Veo 3.1 - Lite` or `Veo 3.1`.
2. Image Model Default: MUST REMAIN EXACTLY `🍌 Nano Banana 2`.
3. Target Download Rule: 
   - When mode is `Chained: Image → Video`, ONLY download the video (`.mp4`). Never download intermediate images.
   - When mode is `Image Only`, download only images (`.png`).
   - When mode is `Video Only`, download only videos (`.mp4`).
4. Storyboard Input: MUST preserve the `<input type="file" accept=".txt">` for uploading .txt files directly.
5. Prompt Sanitization: MUST strip `@CH01_SCXXX.png ->` and `--ar 16:9` from the prompt string before passing to Veo.
6. Auto-retry limit: MUST remain 5 times with exponential backoff per scene [4s, 10s, 20s, 40s, 60s].
7. Concurrency & Jitter: Slider 1 to 6 active slots, with TWO separate sliders for Min Jitter (s) and Max Jitter (s).
8. Safety Protocols: Hard timeout 240s for Veo Lower Priority, and Global Circuit Breaker 60s on 429 rate limit.
9. Bulk Action: MUST preserve the "🔄 Retry All Failed" button in the top header.
10. Memory Management: Maintain `URL.revokeObjectURL()` cleanup after passing image references to Veo.

[NEW FEATURE REQUEST]:
<!-- ĐIỀN TÍNH NĂNG BẠN MUỐN BỔ SUNG HOẶC THAY ĐỔI VÀO ĐÂY -->

[MANDATORY INSTRUCTION]:
Implement the new feature above WITHOUT modifying, resetting, or deleting any of the existing states, constants, or UI components protected in the lock above.
```
