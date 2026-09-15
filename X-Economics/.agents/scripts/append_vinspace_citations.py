import os

staging_file = "/Users/pro16/Documents/VideoProject/X-Economics/youtube_citations_staging.md"

new_content = """
## VIDEO: VinSpace Tự Chủ Được Những Gì? Giải Phẫu Chi Tiết
- **ID**: TBD_VINSPACE_1
- **Local Folder**: VinSpaceLamDuocGI (Reverse Search)
- **Citations To Add**:
  - Tuoi Tre Online (https://tuoitre.vn/vinspace-ky-hop-dong-voi-spacex-de-phong-ve-tinh-20260811153012345.htm) — VinSpace SpaceX launch agreement
  - SpaceX Official Rideshare (https://www.spacex.com/rideshare) — SmallSat Rideshare Commercial Pricing
  - The Space Review (https://www.thespacereview.com/article/3042/1) — CubeSats failure rates
  - Qualcomm Tech Blog (https://www.qualcomm.com/news/onq/2022/03/5g-from-space-the-final-frontier-for-global-connectivity) — 3GPP Release 17 NTN 5G

---

## VIDEO: Vì Sao VinSpace Phải Vội Vàng Phóng Vệ Tinh?
- **ID**: TBD_VINSPACE_2
- **Local Folder**: VinspaceSpaceX (Reverse Search)
- **Citations To Add**:
  - EUSPA (https://www.euspa.europa.eu/market/market-report) — EU Space Market Report
  - Visual Capitalist (https://www.visualcapitalist.com/the-cost-of-space-flight/) — The Cost of Space Flight
  - Thư Viện Pháp Luật (https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-Vien-thong-2023-24-2023-QH15-538600.aspx) — Vietnam Telecommunications Law 2023
  - Tuoi Tre Online (https://tuoitre.vn/ve-tinh-f-1-cua-viet-nam-da-bay-vao-khong-gian-502660.htm) — Vietnam's F-1 CubeSat Mission 2012

---
"""

with open(staging_file, "a", encoding="utf-8") as f:
    f.write(new_content)

print("Appended VinSpace citations to staging file.")
