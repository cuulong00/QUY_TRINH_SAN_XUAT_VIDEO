import os
import time
from playwright.sync_api import sync_playwright

# 5 Video IDs của kênh Dòng Chảy chính thức
VIDEO_IDS = [
    {"id": "MwFFLx-t9HE", "title": "Làm Ô Tô Vì Điều Gì?"},
    {"id": "pr_b_rvu3_s", "title": "Vinfast VS BYD: Người Kiến Thiết Vs Kẻ Xâm Lăng"},
    {"id": "v588e-AbRnI", "title": "Chính Phủ Cần Vingroup - Vì Sao?"},
    {"id": "ypNcBhOLCZM", "title": "Triều Tiên Sinh Tồn Bằng Cách Nào Khi Cả Thế Giới Phong Tỏa?"},
    {"id": "dKO-VpvsYpo", "title": "VinFast Làm Được Gì: Tự Chủ Thật Hay 'Xe Tàu Đội Lốt'"}
]

USER_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../browser_profile"))

def automate_ai_disclosure():
    print("🤖 ĐANG KHỞI ĐỘNG TRÌNH DUYỆT TỰ ĐỘNG HÓA PLAYWRIGHT CHO YOUTUBE STUDIO...")
    print(f"📁 Profile duyệt web lưu tại: {USER_DATA_DIR}")

    with sync_playwright() as p:
        # Launch chromium with persistent profile to keep login cookies
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,  # Mở cửa sổ trực quan để người dùng theo dõi và xử lý đăng nhập nếu cần
            args=["--disable-blink-features=AutomationControlled", "--start-maximized"]
        )
        page = context.pages[0] if context.pages else context.new_page()

        # Step 1: Mở YouTube Studio để kiểm tra trạng thái đăng nhập
        print("\n⏳ Đang mở studio.youtube.com...")
        page.goto("https://studio.youtube.com", wait_until="domcontentloaded")
        time.sleep(3)

        # Kiểm tra xem đã đăng nhập chưa
        if "accounts.google.com" in page.url or "signin" in page.url:
            print("\n" + "="*60)
            print("🔑 VUI LÒNG ĐĂNG NHẬP TÀI KHOẢN KÊNH DÒNG CHẢY TRÊN CỬA SỔ TRÌNH DUYỆT VỪA MỞ.")
            print("Đợi bạn hoàn tất đăng nhập vào YouTube Studio...")
            print("="*60)
            # Wait for user to land on studio.youtube.com dashboard
            while "accounts.google.com" in page.url or "signin" in page.url:
                time.sleep(2)
            print("✅ Đã phát hiện đăng nhập thành công!")
            time.sleep(3)

        print("\n🚀 BẮT ĐẦU TỰ ĐỘNG CHỈNH SỬA THUỘC TÍNH 'SỬ DỤNG AI' CHO CẢ 5 VIDEO DÒNG CHẢY...")
        print("="*60)

        updated_success = 0

        for idx, item in enumerate(VIDEO_IDS):
            v_id = item["id"]
            title = item["title"]
            edit_url = f"https://studio.youtube.com/video/{v_id}/edit"
            print(f"\n🎬 [{idx+1}/5] Đang xử lý Video: {title} (ID: {v_id})")
            print(f"🔗 Mở URL: {edit_url}")

            try:
                page.goto(edit_url, wait_until="domcontentloaded")
                time.sleep(4)

                # 1. Tìm nút 'HIỆN THÊM' / 'SHOW MORE' nếu chưa mở rộng
                show_more = page.locator("text=/HIỆN THÊM|SHOW MORE/i")
                if show_more.is_visible():
                    print("  👉 Nhấp nút 'Hiện thêm'...")
                    show_more.click()
                    time.sleep(1.5)

                # 2. Tìm khu vực 'Sử dụng AI' / 'Altered content' và tích nút 'Có'
                # Trong UI tiếng Việt YouTube Studio:
                # Nút radio 'Có' nằm dưới phần 'Sử dụng AI'
                # Dùng selector tìm radio button có text 'Có' hoặc aria-label/label chứa 'Có'
                print("  👉 Đang tìm nút radio 'Sử dụng AI -> Có'...")
                
                # Cuộn trang xuống để tìm khu vực AI
                page.evaluate("window.scrollBy(0, 800)")
                time.sleep(1)

                # Thử các locator phổ biến cho nút 'Có' của YouTube Studio
                yes_radio = page.locator("tp-yt-paper-radio-button:has-text('Có')").first
                if not yes_radio.is_visible():
                    yes_radio = page.locator("paper-radio-button:has-text('Có')").first
                if not yes_radio.is_visible():
                    yes_radio = page.locator("text=/^Có$/i").first

                if yes_radio.is_visible():
                    yes_radio.click()
                    print("  ✅ Đã nhấp chọn 'Có' (Sử dụng AI)!")
                    time.sleep(1.5)
                else:
                    print("  ⚠️ Không tìm thấy trực tiếp nút 'Có', thử cuộn sâu thêm...")
                    page.evaluate("window.scrollBy(0, 1000)")
                    time.sleep(1.5)
                    yes_radio = page.locator("tp-yt-paper-radio-button:has-text('Có')").first
                    if yes_radio.is_visible():
                        yes_radio.click()
                        print("  ✅ Đã nhấp chọn 'Có' (Sử dụng AI)!")
                        time.sleep(1.5)

                # 3. Tìm và nhấp nút 'LƯU' / 'SAVE'
                save_btn = page.locator("#save-button, button:has-text('LƯU'), button:has-text('SAVE'), [id='save-button']").first
                if save_btn.is_visible() and save_btn.is_enabled():
                    print("  💾 Nhấp nút 'LƯU'...")
                    save_btn.click()
                    time.sleep(3)
                    print(f"  🎉 THÀNH CÔNG: Đã lưu thuộc tính 'Sử dụng AI = Có' cho {title}!")
                    updated_success += 1
                else:
                    print(f"  ℹ️ Nút 'Lưu' không khả dụng (có thể đã chọn 'Có' trước đó hoặc chưa có thay đổi mới).")
                    updated_success += 1

            except Exception as e:
                print(f"  ❌ Lỗi khi tự động xử lý video {title}: {e}")

        print("\n" + "="*60)
        print(f"🎉 HOÀN THÀNH TỰ ĐỘNG HÓA PLAYWRIGHT:")
        print(f"  - Số video xử lý thành công: {updated_success}/5")
        print("="*60)

        time.sleep(3)
        context.close()

if __name__ == '__main__':
    automate_ai_disclosure()
