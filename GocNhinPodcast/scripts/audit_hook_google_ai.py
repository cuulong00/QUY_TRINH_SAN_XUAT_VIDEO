#!/usr/bin/env python3
"""
Audit Hook Script using Google Search AI Mode (udm=50) via Chrome CDP (Port 9222)
"""

import os
import sys
import time
import urllib.parse
from playwright.sync_api import sync_playwright

AUDIT_QUERIES = [
    {
        "id": "AUDIT_01_GRAB_INCOME_HISTORY_VS_2026",
        "title": "Kiểm chứng thu nhập tài xế công nghệ thời kỳ đầu (2015-2018) vs năm 2026",
        "query": (
            "Kiểm chứng thực tế và số liệu tại Việt Nam: "
            "1. Giai đoạn 2015-2018: Thu nhập thực tế của tài xế Grab, Uber xe máy và ô tô là bao nhiêu? "
            "Thông tin 'chạy xe công nghệ kiếm 30-40 triệu/tháng' là doanh thu gộp của ô tô hay thu nhập ròng xe máy? Có phải chiến dịch truyền thông PR của nền tảng? "
            "2. Giai đoạn 2026: Tài xế GrabBike chạy 14 tiếng/ngày, sau khi trừ chiết khấu, xăng xe, bảo dưỡng, thu nhập ròng theo giờ có phải khoảng 20.000 đồng/giờ và thấp hơn lương tối thiểu vùng I?"
        )
    },
    {
        "id": "AUDIT_02_ECOMMERCE_FEES_TIMELINE",
        "title": "Kiểm chứng tiến trình lịch sử phí sàn TMĐT: Shopee (2016-2026) & TikTok Shop (2022-2026)",
        "query": (
            "Kiểm chứng lịch sử và số liệu phí sàn TMĐT Việt Nam: "
            "1. Shopee ra mắt năm 2016 có đúng là miễn phí sàn 0% (0% hoa hồng, 0% thanh toán) và freeship ngập tràn đến năm 2019 không? "
            "2. TikTok Shop ra mắt tại Việt Nam tháng 4/2022 với mức phí ban đầu là bao nhiêu (1%?) và thời kỳ đầu 2022-2023 hoa hồng affiliate KOC là bao nhiêu? "
            "3. Năm 2026, tổng gánh nặng phí sàn Shopee (phí cố định, phí xử lý giao dịch 6%, phí hạ tầng 3.000đ, voucher xtra) có lên tới 20%-28% doanh thu?"
        )
    },
    {
        "id": "AUDIT_03_HOOK_VALIDATION_CRITIQUE",
        "title": "Google AI Mode phản biện và audit trực tiếp đoạn Hook mở đầu",
        "query": (
            "Bạn là chuyên gia kinh tế và kiểm toán truyền thông độc lập. Hãy audit tính chính xác của đoạn mở đầu kịch bản sau: "
            "'Những năm 2015-2021: Một người trẻ bỏ việc văn phòng khoác áo chạy xe công nghệ có thể dễ dàng đút túi ba mươi, bốn mươi triệu đồng mỗi tháng; một chủ shop bật livestream bán nghìn đơn thâu đêm với mức phí sàn gần như bằng không; một bạn trẻ quay video ngắn có thể nhận hoa hồng gấp mấy lần lương giám đốc. "
            "Đến năm 2026: Tài xế cày 14 tiếng chỉ còn kiếm được 20.000 đồng một giờ (thấp hơn lương tối thiểu vùng); tiểu thương oằn mình trước ma trận phí sàn gần 30% và bão hàng giá xưởng biên giới; hàng vạn người uất ức tắt ứng dụng, âm thầm rời sàn.' "
            "Hãy chỉ rõ: Đoạn này có điểm nào bị nói quá, lệch mốc thời gian, hay không đúng bản chất kinh tế không? Cần sửa lại như thế nào cho chuẩn xác 100%?"
        )
    }
]

def clean_google_ai_text(raw_text):
    lines = raw_text.split("\n")
    filtered = []
    skip_headers = [
        "Bỏ qua để đến phần nội dung chính",
        "Hỗ trợ truy cập",
        "Chế độ AI",
        "Tất cả",
        "Hình ảnh",
        "Video",
        "Tin tức",
        "Mua sắm",
        "Thêm",
        "Công cụ",
        "ULTRA",
        "Cuộc trò chuyện ở Chế độ AI:"
    ]
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if any(s == h or s.startswith(h) for h in skip_headers):
            continue
        if s.startswith("Phản hồi được tạo bằng AI"):
            continue
        filtered.append(s)
    return "\n\n".join(filtered)

def main():
    print("🚀 Bắt đầu Audit Hook qua Google Search AI Mode (Chrome CDP 9222)...")
    out_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/bay-mat-ngot-kinh-te-nen-tang/google_ai_audit"
    os.makedirs(out_dir, exist_ok=True)
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            context = browser.contexts[0]
            print("✅ Đã kết nối thành công với Chrome CDP 9222 của người dùng.")
        except Exception as e:
            print(f"❌ Không thể kết nối với Chrome CDP 9222: {e}")
            sys.exit(1)
            
        page = context.new_page()
        
        for idx, item in enumerate(AUDIT_QUERIES):
            qid = item["id"]
            title = item["title"]
            query = item["query"]
            print(f"\n[{idx+1}/{len(AUDIT_QUERIES)}] 🔍 Đang gửi truy vấn Google AI Mode: {title}...")
            
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&udm=50&hl=vi"
            page.goto(url, wait_until="domcontentloaded")
            
            # Wait for AI response to render
            time.sleep(8)
            
            # Wait for text to stabilize
            pre_len = 0
            for _ in range(6):
                curr_len = len(page.locator("body").inner_text())
                if curr_len == pre_len and curr_len > 250:
                    break
                pre_len = curr_len
                time.sleep(2)
                
            raw_text = page.locator("body").inner_text()
            cleaned_text = clean_google_ai_text(raw_text)
            
            out_file = os.path.join(out_dir, f"{qid}.md")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# Google AI Mode Audit — {title}\n\n")
                f.write(f"- **Mã kiểm toán:** `{qid}`\n")
                f.write(f"- **Thời gian thực hiện:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"- **Truy vấn:** `{query}`\n")
                f.write(f"- **Nguồn engine:** Google Search AI Mode (udm=50 / Gemini)\n\n")
                f.write(f"---\n\n## Phản hồi chi tiết từ Google AI Search:\n\n")
                f.write(cleaned_text + "\n")
                
            print(f"💾 Đã lưu kết quả: {out_file} ({len(cleaned_text)} ký tự)")
            
        page.close()
        print("\n🎉 Hoàn thành kiểm toán 3 chuyên đề qua Google Search AI Mode!")

if __name__ == "__main__":
    main()
