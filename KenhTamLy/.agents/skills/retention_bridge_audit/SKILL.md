# Retention Bridge Audit — Kiểm Toán Mạch Nối Chương

> **Chuyên gia:** The Quality Czar (Giám Đốc Chất Lượng)
> **Persona:** `.agents/personas/the_quality_czar.md`
> **Chức năng:** Kiểm toán TOÀN BỘ chuỗi liên kết giữa các chương SAU khi tất cả chapter đã viết xong.
> **Khi nào dùng:** Sau Phase 9 (viết xong chapter cuối) và TRƯỚC Phase 10 (Editorial & Legal QA).
> **Tần suất:** MỘT LẦN DUY NHẤT cho mỗi episode — không chạy từng chương riêng lẻ.

---

## Tại sao bước này tồn tại

Episode KenhTamLy: toàn bộ các chương được viết tuần tự, mỗi chương vượt qua Quality Czar scan cá nhân.
Nhưng khi ghép lại, chuỗi mối nối giữa các chương bộc lộ 5 lỗi cấu trúc:
- Không có MACRO LOOP xuyên suốt video
- Template transition bị cấm tại mối nối chương
- Recap không cần thiết tại mối nối
- Stacking loops không được thiết kế — Mất lực kéo ở các chương cuối
- Typos xuyên chương không ai bắt

**Quality Czar scan từng chương → bắt lỗi MỨC CHƯƠNG.**
**Retention Bridge Audit scan mối nối → bắt lỗi MỨC VIDEO.**

---

## Input bắt buộc

- TẤT CẢ file `chapter_XX.md` trong `episodes/[slug]/`
- `06_retention_map.md` (nếu có phần Stacking Loops Map)
- `00_core/anti_patterns.md`
- `00_core/voiceover_style_guide.md`

---

## Quy trình — 4 Lượt Kiểm Toán

### Lượt 1: CHAIN READ (Đọc chuỗi mối nối)

**Cách thực hiện:** Đọc LIÊN TỤC chỉ 3 dòng cuối mỗi chương + 3 dòng đầu chương sau. Bỏ qua phần thân chương.

Ghi ra bảng sau cho MỖI mối nối:

```
## Mối nối: Ch[X] → Ch[X+1]

### Kết Ch[X] (trích nguyên văn 2-3 câu cuối):
> "..."

### Mở Ch[X+1] (trích nguyên văn 1-3 câu đầu):
> "..."

### Checklist:
| # | Test | Đạt? |
|---|---|---|
| 1 | VALUE CLOSE: Khán giả biết chương vừa rồi cho họ insight gì cụ thể? | |
| 2 | OPEN LOOP: Có chi tiết cụ thể (con số/nhân vật/sự kiện) gây tò mò, CHƯA giải đáp? | |
| 3 | ANSWER HOOK: Chương sau trả lời hook trong 1-3 câu đầu? | |
| 4 | 3-WORD TEST: Tóm câu mở chương sau trong ≤3 từ được không? | |
| 5 | BUT/THEREFORE: Chèn "NHƯNG" hoặc "DO ĐÓ" giữa 2 chương. Nếu chỉ chèn được "VÀ SAU ĐÓ" → FAIL. | |
| 6 | SPOILER TEST: Kết chương có tiết lộ nội dung chương sau không? | |
| 7 | DEAD AIR TEST: Mở chương có mini-intro ("Trong phần này...", "Để hiểu rõ hơn...")? | |
| 8 | PATTERN INTERRUPT: Có thay đổi nhịp câu tại mối nối? (Câu ngắn đột ngột sau chuỗi dài?) | |
| 9 | BANNED PHRASES: Có dùng cụm từ trong bảng CẤM? | |

### Verdict mối nối: [PASS / CẦN SỬA]
### Lỗi cụ thể (nếu có):
```

---

### Lượt 2: STACKING LOOPS MAP (Bản đồ vòng mở)

Vẽ bản đồ loop cho TOÀN BỘ video:

```
## Stacking Loops Map

| Chương | Loops MỞ | Loops ĐÓNG | Tổng loops đang mở |
|---|---|---|---|
| Ch1 | MACRO: "..." / MESO-1: "..." | (không) | 2 |
| Ch2 | MESO-2: "..." | MESO-1 | 2 |
| Ch3 | MESO-3: "..." | MESO-2 | 2 |
| ... | ... | ... | ... |

### Kiểm tra:
| # | Quy tắc | Đạt? |
|---|---|---|
| 1 | MACRO LOOP mở từ Ch1, chỉ đóng ở chương cuối? | |
| 2 | Tại MỌI thời điểm có ≥1 loop đang mở? | |
| 3 | Khi đóng 1 loop → mở ngay 1 loop mới? (không để khoảng trống) | |
| 4 | Có ≥2 cấp loop hoạt động song song? (Macro + Meso) | |
| 5 | Chương cuối đóng sạch mọi loop? | |
```

---

### Lượt 3: BUT/THEREFORE CHAIN (Chuỗi nhân quả)

Test nhanh toàn bộ chuỗi:

```
## But/Therefore Chain

| Mối nối | Nối bằng gì? | Đạt? |
|---|---|---|
| Ch1 → Ch2 | (NHƯNG / DO ĐÓ / VÀ SAU ĐÓ) + giải thích | |
| Ch2 → Ch3 | ... | |
| Ch3 → Ch4 | ... | |
| ... | ... | |

### Verdict: Nếu có bất kỳ mối nối nào chỉ nối được bằng "VÀ SAU ĐÓ" → CẦN SỬA.
```

---

### Lượt 4: MOMENTUM PROFILE (Hồ sơ nhịp chương)

Đánh giá nhịp năng lượng tại mỗi mối nối:

```
## Momentum Profile

| Mối nối | Nhịp cuối Ch[X] | Nhịp đầu Ch[X+1] | Đánh giá |
|---|---|---|---|
| Ch1→2 | (dài/ngắn/trung bình) | (dài/ngắn/trung bình) | |
| Ch2→3 | ... | ... | |
| ... | ... | ... | |

### Quy tắc:
- Nếu cuối chương = câu DÀI phân tích → đầu chương sau PHẢI là câu NGẮN (pattern interrupt)
- Nếu cuối chương = câu NGẮN hook → đầu chương sau PHẢI là đáp án NGẮN (slippery slope)
- TRÁNH: Dài → Dài (mệt), Ngắn → Dài (mất momentum)
```

---

## Output

Sau khi chạy xong 4 lượt, tạo file `retention_bridge_audit.md` trong `episodes/[slug]/` với format:

```markdown
# Retention Bridge Audit — [Episode Name]
Ngày audit: [YYYY-MM-DD]

## Tổng quan
- Số mối nối: [X]
- Mối nối PASS: [X]
- Mối nối CẦN SỬA: [X]

## Điểm trung bình: [X/9] (theo checklist Lượt 1)

## Stacking Loops: [PASS / CẦN SỬA]
## But/Therefore Chain: [PASS / CẦN SỬA]
## Momentum Profile: [PASS / CẦN SỬA]

## Chi tiết từng mối nối
(Kết quả Lượt 1 cho mỗi mối nối)

## Các lỗi cần sửa (ưu tiên cao → thấp)
1. ...
2. ...

## Verdict: [DUYỆT / SỬA LẠI]
```

Nếu Verdict = SỬA LẠI → Chapter Writer nhận danh sách lỗi cụ thể và sửa ĐÚNG các đoạn kết/mở bị đánh dấu. KHÔNG viết lại toàn bộ chương.

---

## Lưu ý quan trọng

1. **Retention Bridge Audit KHÔNG scan nội dung chương.** Đó là việc của Quality Czar scan (Phase 9.5). Audit này CHỈ scan các mối nối.
2. **Audit này chạy MỘT LẦN sau khi TẤT CẢ chương đã viết xong.** Không chạy từng chương riêng lẻ — vì mối nối cần 2 chương mới kiểm tra được.
3. **If Chapter Writer modifies a connection → re-run audit for the affected connections.**
