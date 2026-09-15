# Shorts Map Template — Kênh GocNhinPodcast

> **Hướng dẫn:** Copy file này vào `episodes/[slug]/shorts/shorts_map.md` khi bắt đầu lập kế hoạch Shorts cho một episode.
> Đối với Shorts độc lập, copy vào `shorts/standalone/[slug]/shorts_map.md`.

---

episode_slug: [ĐIỀN SLUG]
long_video_title: "[ĐIỀN TIÊU ĐỀ VIDEO DÀI]"
total_shorts: [ĐIỀN SỐ]

---

## Lịch Phát Hành (Funnel Spiral)

| Ngày | Short # | Loại | Giờ đăng | CTA |
|------|---------|------|----------|-----|
| D-2 | #1 | Hook Teaser | 20:00 | Pinned comment → video dài |
| D+0 | #2 | Data Shock / Nghịch Lý | 12:00 | End screen → video dài |
| D+1 | #3 | So Sánh Quốc Gia / Mini Essay | 20:00 | Pinned comment |
| D+3 | #4 | Golden Quote | 19:00 | End screen |
| D+5 | #5 | Standalone (Độc lập) | 20:00 | Subscribe CTA |

---

## Short #1 — [LOẠI]

```yaml
short_id: 01
type: [hook_teaser / data_shock / paradox / comparison / golden_quote / mini_essay]
source_chapter: [chapter_XX hoặc "standalone"]
duration_target: [XX]s
total_scenes: [X]
publish_timing: [D-2 / D+0 / D+1 / D+3 / D+5]
cta_type: [pinned_comment / end_screen / link_bio / subscribe]

hook_sentence: >
  [ĐIỀN CÂU HOOK]

twist_or_cta: >
  [ĐIỀN CÂU KẾT / CTA]

scenes:
  - id: s01
    time: "0-Xs"
    narration: "[ĐIỀN]"
    emotional_beat: [shock / pride / tension / hope / urgency / curiosity / dread]
    motion_type: [WIDE / CLOSE-UP / LOW-ANGLE / PAN / ZOOM / STATIC]

  - id: s02
    time: "X-Xs"
    narration: "[ĐIỀN]"
    emotional_beat: [...]
    motion_type: [...]
```

---

## Short #2 — [LOẠI]

```yaml
# (Copy template từ Short #1 và điền)
```

---

## Short #3 — [LOẠI]

```yaml
# (Copy template từ Short #1 và điền)
```

---

## Short #4 — [LOẠI]

```yaml
# (Copy template từ Short #1 và điền)
```

---

## Short #5 — [LOẠI]

```yaml
# (Copy template từ Short #1 và điền)
```

---

## Quy tắc nhớ

1. Mỗi episode sinh tối thiểu **3 Shorts**, tối đa **5 Shorts**.
2. Shorts phái sinh PHẢI có link về video dài trong metadata.
3. Shorts độc lập PHẢI có CTA về kênh/playlist.
4. Mọi Short PHẢI tuân thủ `shorts_style_guide.md`.
5. Golden Quote chỉ lấy từ `07_golden_lines.md` — KHÔNG tự bịa.
