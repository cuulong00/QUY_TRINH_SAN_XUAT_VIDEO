import os

staging_file = "/Users/pro16/Documents/VideoProject/HieuBietHon/youtube_citations_staging.md"

new_content = """
## VIDEO: VinFast Quyết Chiếm Mỏ Vàng 2 Tỷ Dân
- **ID**: TBD_VINFAST_AN_DO_3
- **Local Folder**: vinfast-an-do (Reverse Search)
- **Citations To Add**:
  - Reuters (https://www.reuters.com/business/autos-transportation/vietnams-vinfast-breaks-ground-first-india-ev-factory-2024-02-25/) — VinFast breaks ground on first India EV factory
  - Reuters (https://www.reuters.com/business/autos-transportation/chinas-byd-proposes-1-bln-india-ev-investment-sources-2023-07-14/) — BYD $1 bln India EV investment proposal rejected
  - Reuters (https://www.reuters.com/business/autos-transportation/vietnams-vinfast-delays-north-carolina-ev-plant-start-2028-2024-07-13/) — VinFast delays North Carolina EV plant
  - The Economic Times (https://economictimes.indiatimes.com/industry/renewables/evs-to-account-for-nearly-10-pc-of-indias-pv-market-by-fy28-tata-motors/articleshow/111867160.cms) — Tata Motors Dominance

---

## VIDEO: Vì Sao Chúng Ta Bị Coi Thường?
- **ID**: TBD_VN_BI_COI_THUONG_4
- **Local Folder**: VN_bi_coi_thuong (Reverse Search)
- **Citations To Add**:
  - Tuổi Trẻ Online (https://tuoitre.vn/tong-bi-thu-to-lam-cu-lung-thung-buoc-di-chung-ta-kho-bat-kip-cac-nuoc-20250212093510564.htm) — Tổng Bí thư: Cứ lững thững bước đi khó bắt kịp
  - Báo Chính phủ (https://baochinhphu.vn/chong-lang-phi-102241013144820297.htm) — Chống lãng phí
  - Bloomberg (https://www.bloomberg.com/news/articles/2024-03-17/how-a-small-malaysian-island-became-a-semiconductor-powerhouse) — Penang: Silicon Valley of the East
  - World Bank (https://www.worldbank.org/en/news/press-release/2021/08/11/vietnam-needs-to-prepare-for-an-aging-society-world-bank-report) — Vietnam Aging Society Demographics
  - South China Morning Post (https://www.scmp.com/week-asia/economics/article/3253018/malaysias-brain-drain-singapore-shows-no-sign-slowing-low-pay-and-lack-prospects-drive-exodus) — Malaysia's Brain Drain to Singapore

---
"""

with open(staging_file, "a", encoding="utf-8") as f:
    f.write(new_content)

print("Appended Video 3, 4 citations to staging file.")
