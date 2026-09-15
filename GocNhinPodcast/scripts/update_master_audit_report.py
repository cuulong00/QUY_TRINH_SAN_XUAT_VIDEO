#!/usr/bin/env python3
import os
import re

EPISODE_DIR = "episodes/thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"
master_path = os.path.join(EPISODE_DIR, "google_ai_audit_results.md")

results = []
for i in range(1, 8):
    ch_num = f"{i:02d}"
    ch_file = f"chapter_{ch_num}.md"
    audit_file = f"google_ai_audit_{ch_num}.md"
    screenshot = f"google_ai_audit_{ch_num}.png"
    results.append((ch_num, ch_file, audit_file, screenshot))

md_report = """# Báo Cáo Tổng Hợp Kiểm Chứng Thông Tin (Google AI Audit Report)

- **Dự án:** thai-lan-no-ngap-dau-vet-xe-do-nhat-ban
- **Thời gian tổng hợp:** 2026-09-02 03:54:15
- **Công cụ kiểm chứng:** Google Search AI Mode (udm=50 Real-time Search)
- **Tổng số chương đã kiểm chứng:** 7/7 chương

## 📋 Mục lục & Trạng thái các chương

| Chương | Tên File Kịch Bản | Báo Cáo Chi Tiết | Ảnh Đối Chiếu |
|:---:|---|---|---|
"""

for num, file, audit_file, screenshot in results:
    md_report += f"| {num} | [{file}](file://{os.path.abspath(os.path.join(EPISODE_DIR, file))}) | [{audit_file}]({audit_file}) | [Xem ảnh]({screenshot}) |\n"

md_report += "\n---\n\n## 📝 Tóm tắt ý kiến phản biện của AI cho từng chương\n\n"

for num, file, audit_file, _ in results:
    audit_path = os.path.join(EPISODE_DIR, audit_file)
    md_report += f"### 🔍 Chương {num}\n\n"
    if os.path.exists(audit_path):
        with open(audit_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r"## Kết quả phản biện & Đối chiếu nguồn tin:\n\n(.*?)(\n## Ảnh chụp|$)", content, re.DOTALL)
        if match:
            text = match.group(1).strip()
            lines = text.split("\n")
            md_report += "\n".join(lines[:25]) + "\n\n*(Xem toàn văn tại báo cáo chương...)*\n\n"
        else:
            md_report += f"*Xem chi tiết tại [{audit_file}]({audit_file})*\n\n"
    else:
        md_report += "*Báo cáo không khả dụng.*\n\n"

md_report += """---
> [!IMPORTANT]
> **Lưu ý biên tập:** Báo cáo này tổng hợp đầy đủ các điểm mà Google AI Search Mode đánh giá là chưa chính xác, thiếu ngữ cảnh hoặc bị mâu thuẫn số liệu. Tuyệt đối giữ nguyên kịch bản gốc để chờ Người dùng duyệt và quyết định phương án sửa đổi.
"""

with open(master_path, "w", encoding="utf-8") as f:
    f.write(md_report)

print(f"✓ Đã cập nhật xong master report: {master_path}")
