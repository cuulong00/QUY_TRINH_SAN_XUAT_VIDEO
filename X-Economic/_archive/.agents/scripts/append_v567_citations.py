import os

staging_file = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/youtube_citations_staging.md"

new_content = """
## VIDEO: BYD Đại Chiến Toyota: VinFast Sẽ Đi Về Đâu?
- **ID**: TBD_BYDTOYOTA_5
- **Local Folder**: Thach-thuc-nha-vua-toyota (Reverse Search)
- **Citations To Add**:
  - Reuters (https://www.reuters.com/business/autos-transportation/toyota-retains-top-spot-global-car-sales-2023-2024-01-30/) — Toyota Retains Top Spot Global Car Sales
  - Reuters (https://www.reuters.com/business/autos-transportation/chinas-byd-q4-ev-sales-top-tesla-first-time-2024-01-02/) — BYD Q4 EV Sales Top Tesla
  - CSIS (https://www.csis.org/analysis/chinese-ev-subsidies-explaining-230-billion-support) — Chinese EV Subsidies & Ten Cities, Thousand Vehicles Program
  - Toyota Global Newsroom (https://global.toyota/en/newsroom/corporate/39288520.html) — Solid-State Battery Commercialization

---

## VIDEO: BYD Sắp Tấn Công Mạnh Vào Việt Nam?
- **ID**: TBD_BYD_VN_6
- **Local Folder**: byd-co-may-hoan-hao-2 (Reverse Search)
- **Citations To Add**:
  - Reuters (https://www.reuters.com/business/autos-transportation/eu-ev-tariffs-take-effect-despite-hopes-deal-2024-10-29/) — EU Countervailing Tariffs on Chinese EVs
  - Bloomberg (https://www.bloomberg.com/news/articles/2024-05-15/china-s-auto-association-asks-ev-makers-to-cut-supplier-payment-terms) — BYD Supplier Financing & Short-Term Debt
  - VietnamPlus (https://en.vietnamplus.vn/vgreen-to-build-super-charging-hubs-nationwide-post304565.vnp) — V-Green 150,000 Charging Ports
  - Financial Times (https://www.ft.com/content/8a9a2c3a-2a22-4a00-9286-905c5b3671a5) — Chinese EV Price War & Overcapacity

---

## VIDEO: "Sếu Đầu Đàn" Đang Được Nuôi Dưỡng Thế Nào?
- **ID**: TBD_SEU_DAU_DAN_7
- **Local Folder**: seu-dau-dan (Reverse Search)
- **Citations To Add**:
  - Vietnam Government Portal (https://baochinhphu.vn/bo-chinh-tri-ban-hanh-nghi-quyet-so-79-nq-tw-ve-phat-trien-kinh-te-nha-nuoc-102260106170535359.htm) — Resolution 79-NQ/TW on SOEs
  - Vietnam Government Portal (https://baochinhphu.vn/nghi-quyet-41-nq-tw-luong-gio-moi-cho-doi-ngu-doanh-nhan-viet-nam-102231011153018446.htm) — Resolution 41-NQ/TW & Private Sector GDP
  - VnEconomy (https://vneconomy.vn/hoa-phat-rot-hon-14-000-ty-dong-lam-ray-thep-cho-duong-sat-toc-do-cao.htm) — Hoa Phat Dung Quat 2 Railway Steel
  - The Korea Herald (https://www.koreaherald.com/view.php?ud=20251125000543) — Chaebol Economic Concentration

---
"""

with open(staging_file, "a", encoding="utf-8") as f:
    f.write(new_content)

print("Appended Video 5, 6, 7 citations to staging file.")
