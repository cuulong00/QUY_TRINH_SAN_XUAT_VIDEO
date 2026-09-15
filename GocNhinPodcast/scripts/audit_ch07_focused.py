#!/usr/bin/env python3
import os
import sys
import time
import urllib.parse
from playwright.sync_api import sync_playwright

EPISODE_DIR = "episodes/thai-lan-no-ngap-dau-vet-xe-do-nhat-ban"
ch7_path = os.path.join(EPISODE_DIR, "chapter_07.md")

with open(ch7_path, "r", encoding="utf-8") as f:
    full_text = f.read()

setup_prompt = (
    "Tôi muốn bạn đóng vai trò là một chuyên gia phản biện khoa học, chính sách công và kinh tế độc lập chuyên ngành phân tích vĩ mô Đông Nam Á. "
    "Tôi sẽ gửi cho bạn kịch bản Chương 07 về đối sánh kinh tế Việt Nam - Thái Lan năm 2026 để kiểm chứng nghiêm ngặt tính chính xác của dữ liệu thực tế thời điểm giữa năm 2026. "
    "Bạn BẮT BUỘC phải thực hiện tìm kiếm internet thời gian thực với các từ khóa cập nhật nhất năm 2026 để đối chiếu với: "
    "các số liệu thống kê vĩ mô (GDP PPP $2.025T vượt Thái Lan, Tăng trưởng 8.02%, Xuất khẩu $475B vs $339.6B, Nợ công VN 30% vs Thái Lan 66.1%, Giá nhà >30 lần thu nhập, Nợ hộ gia đình VN, Mốc Dân số Vàng 2036, Dự báo CEBR 2035). "
    "Hãy chỉ ra: (1) các thông tin bị sai lệch, thiếu sót hoặc đã lỗi thời, (2) các số liệu thực tế đắt giá mới nhất trong năm 2026 có thể bổ sung, "
    "và (3) gợi ý cách sửa đổi tối ưu kèm nguồn đối chiếu cụ thể. Hãy phản hồi 'SẴN SÀNG' nếu bạn đã hiểu rõ nhiệm vụ."
)

encoded_setup = urllib.parse.quote(setup_prompt)
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
    print("🌐 Đang kết nối Google AI Search...")
    page.goto(init_url)
    
    time.sleep(6) # wait for page
    
    # Wait for follow-up input
    input_el = None
    for _ in range(15):
        els = page.locator("textarea")
        for i in range(els.count()):
            item = els.nth(i)
            if item.is_visible() and item.get_attribute("name") != "q":
                input_el = item
                break
        if input_el:
            break
        time.sleep(2)
        
    if not input_el:
        print("Không tìm thấy ô nhập liệu.")
        browser.close()
        sys.exit(1)
        
    print("✍️ Gửi nội dung Chương 07...")
    ch7_prompt = (
        f"Hãy tiến hành tìm kiếm thời gian thực năm 2026 và audit chi tiết nội dung của Chương 07 dưới đây. "
        f"Đối chiếu nghiêm ngặt mọi số liệu, tuyên bố, chính sách, và logic tài chính trong văn bản với thực tế cập nhật mới nhất tính đến tháng 6/2026 tại Việt Nam và Thái Lan. "
        f"Nếu phát hiện sai số hoặc logic toán học/tài chính bị mâu thuẫn, hãy vạch rõ và cung cấp dữ liệu chính xác kèm nguồn:\n\n{full_text}"
    )
    
    input_el.fill(ch7_prompt)
    time.sleep(1)
    
    # Click send
    btn = page.locator("button[aria-label*='Gửi'], button[aria-label*='Submit'], button[aria-label*='Send'], button[aria-label*='Tìm kiếm']").first
    if btn.is_visible():
        btn.click()
    else:
        input_el.press("Enter")
        
    print("⏳ Chờ AI phản hồi...")
    time.sleep(5)
    
    # Wait for stable text
    last_len = 0
    stable_count = 0
    for _ in range(40):
        time.sleep(3)
        curr_len = page.evaluate("document.body.innerText.length")
        print(f"Length: {curr_len}")
        if curr_len == last_len and curr_len > 0:
            stable_count += 1
            if stable_count >= 3:
                break
        else:
            stable_count = 0
            last_len = curr_len
            
    # Extract
    text = page.evaluate("document.body.innerText")
    
    # Save
    out_path = os.path.join(EPISODE_DIR, "google_ai_audit_07.md")
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(f"# Google AI Search Mode Audit - Chương 07\n\n- **Nguồn:** Google Search AI Mode (udm=50)\n- **Thời gian:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n## Kết quả phản biện & Đối chiếu nguồn tin:\n\n{text}\n")
        
    page.screenshot(path=os.path.join(EPISODE_DIR, "google_ai_audit_07.png"))
    print(f"✅ Đã lưu audit Chương 07 vào {out_path}")
    browser.close()
