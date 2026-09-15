#!/usr/bin/env python3
"""
scripts/refine_same_clip_pairs.py
Tinh chỉnh timeline cho các phân đoạn dùng chung clip:
- Xóa bỏ transition giữa 2 phân đoạn của cùng một clip (tránh tự hòa tan vào chính mình)
- Nối mượt mà source_timerange để clip chạy liền mạch tự nhiên không bị nhảy hình
"""

import json
from pathlib import Path
import subprocess

DRAFT_DIR = Path("/Users/pro16/Movies/CapCut/User Data/Projects/com.lveditor.draft/KemTrangTien_Ch01")
DRAFT_INFO = DRAFT_DIR / "draft_info.json"
TEMPLATE_TMP = DRAFT_DIR / "template-2.tmp"

with open(DRAFT_INFO, "r", encoding="utf-8") as f:
    draft = json.load(f)

vtrack = [t for t in draft["tracks"] if t["type"] == "video"][0]
mats = {m["id"]: m["path"] for m in draft["materials"]["videos"]}
transitions = {t["id"]: t for t in draft.get("materials", {}).get("transitions", [])}

removed_transitions = 0
smoothed_pairs = 0

for i in range(len(vtrack["segments"]) - 1):
    seg1 = vtrack["segments"][i]
    seg2 = vtrack["segments"][i+1]
    p1 = mats[seg1["material_id"]].split("/")[-1]
    p2 = mats[seg2["material_id"]].split("/")[-1]
    
    if p1 == p2:
        # 1. Gỡ transition khỏi seg1
        extra_refs = seg1.get("extra_material_refs", [])
        new_refs = [r for r in extra_refs if r not in transitions]
        if len(new_refs) != len(extra_refs):
            seg1["extra_material_refs"] = new_refs
            removed_transitions += 1
            
        # 2. Nối source_timerange của seg2
        d1_us = seg1["target_timerange"]["duration"]
        d2_us = seg2["target_timerange"]["duration"]
        
        # Nếu tổng thời lượng <= 8.0s (8_000_000us)
        if d1_us + d2_us <= 8_000_000:
            seg1["source_timerange"] = {"start": 0, "duration": d1_us}
            seg2["source_timerange"] = {"start": d1_us, "duration": d2_us}
        else:
            # Nếu > 8s, seg1 chạy từ 0, seg2 kết thúc ở đúng 8_000_000us
            seg1["source_timerange"] = {"start": 0, "duration": d1_us}
            start2 = max(0, 8_000_000 - d2_us)
            seg2["source_timerange"] = {"start": start2, "duration": d2_us}
        smoothed_pairs += 1

# Ghi lại draft_info.json và template-2.tmp
raw_json = json.dumps(draft, ensure_ascii=False)
with open(DRAFT_INFO, "w", encoding="utf-8") as f:
    f.write(raw_json)
with open(TEMPLATE_TMP, "w", encoding="utf-8") as f:
    f.write(raw_json)

print(f"[✓] Đã tinh chỉnh {smoothed_pairs} cặp phân cảnh cùng clip.")
print(f"[✓] Đã gỡ bỏ {removed_transitions} transition thừa trên cùng một clip.")

# Re-register and lint
cli = Path("/Users/pro16/Documents/VideoProject/AutoCapCut/tools/capcut-cli/dist/index.js")
subprocess.run(["node", str(cli), "register", str(DRAFT_DIR), "--materials", "--apply"], check=True)
res = subprocess.run(["node", str(cli), "lint", str(DRAFT_DIR)], capture_output=True, text=True)
print(res.stdout)
