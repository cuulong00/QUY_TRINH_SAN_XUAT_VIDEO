#!/usr/bin/env python3
import os
import sys
import time
import urllib.parse
import re
from playwright.sync_api import sync_playwright

EPISODE_DIR = "episodes/thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"
ch7_path = os.path.join(EPISODE_DIR, "chapter_07.md")

with open(ch7_path, "r", encoding="utf-8") as f:
    full_text = f.read()

# Setup concise query
setup_query = (
    "Audit phản biện kinh tế vĩ mô 2026: Đối sánh kinh tế Việt Nam và Thái Lan. "
    "Kiểm chứng các số liệu: GDP PPP Việt Nam 2026 đạt 2.025 nghìn tỷ USD vượt Thái Lan (IMF), "
    "Tăng trưởng kinh tế 8.02% vs 1.3%-1.9%, Xuất khẩu $475B vs $339.6B, Nợ công VN 30% vs Thái Lan 66.1%, "
    "Kế hoạch đầu tư công VN 400 tỷ USD (2026-2030), Giá nhà/Thu nhập >30 lần, Nợ hộ gia đình VN ~40% GDP, "
    "Mốc Dân số Vàng 2036, Dự báo CEBR 2035 GDP VN $994B vs Thái Lan $839B. Đánh giá tính chính xác năm 2026."
)

encoded_setup = urllib.parse.quote(setup_query)
init_url = f"https://www.google.com/search?q={encoded_setup}&udm=50"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel="chrome", args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        locale="vi-VN",
        timezone_id="Asia/Ho_Chi_Minh",
        viewport={"width": 1280, "height": 800}
    )
    context.add_init_script("delete navigator.__proto__.webdriver")
    page = context.new_page()
    print("🌐 Đang điều hướng đến Google AI Search...")
    page.goto(init_url)
    
    # Wait for SGE response
    time.sleep(10)
    
    last_len = 0
    stable_count = 0
    for _ in range(30):
        time.sleep(2)
        curr_len = page.evaluate("document.body.innerText.length")
        print(f"Length: {curr_len}")
        if curr_len == last_len and curr_len > 1000:
            stable_count += 1
            if stable_count >= 3:
                break
        else:
            stable_count = 0
            last_len = curr_len
            
    text = page.evaluate("document.body.innerText")
    
    out_path = os.path.join(EPISODE_DIR, "google_ai_audit_07.md")
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(f"# Google AI Search Mode Audit - Chương 07\n\n- **Nguồn kiểm chứng:** Google Search AI Mode (udm=50)\n- **Thời gian audit:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n- **File kịch bản:** [chapter_07.md](file://{os.path.abspath(ch7_path)})\n\n## Kết quả phản biện & Đối chiếu nguồn tin:\n\n{text}\n")
        
    page.screenshot(path=os.path.join(EPISODE_DIR, "google_ai_audit_07.png"))
    print(f"✅ Đã lưu audit Chương 07 thành công vào {out_path}")
    browser.close()
