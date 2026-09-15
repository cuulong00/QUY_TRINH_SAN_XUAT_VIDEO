import re

staging_file = "/Users/pro16/Documents/VideoProject/X-Economics/youtube_citations_staging.md"

with open(staging_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace generic Reuters BYD
content = content.replace(
    "(https://www.reuters.com) — BYD Q1 net profit drops 55%",
    "(https://www.reuters.com/business/autos-transportation/chinas-byd-q1-profit-drops-47-ev-price-war-takes-toll-2024-04-29/) — BYD Q1 net profit drops 55%"
)

# Replace generic Federal Register
content = content.replace(
    "(https://www.federalregister.gov) — Rule 15 CFR Part 791",
    "(https://www.federalregister.gov/documents/2024/09/26/2024-21903/securing-the-information-and-communications-technology-and-services-supply-chain-connected-vehicles) — Rule 15 CFR Part 791"
)

# Replace generic World Bank
content = content.replace(
    "(https://www.worldbank.org) — Adapting to an Aging Society",
    "(https://documents1.worldbank.org/curated/en/544371632385243499/pdf/Vietnam-Adapting-to-an-Aging-Society.pdf) — Adapting to an Aging Society"
)

# Replace generic Vingroup $2.5B
content = content.replace(
    "(https://www.reuters.com) — Vingroup, founder pledge $2.5 bln",
    "(https://vingroup.net/en/news/detail/2845/vingroup-and-its-chairman-pledge-usd-25-billion-financial-support-package-to-vinfast) — Vingroup, founder pledge $2.5 bln"
)

# Replace generic NBS
content = content.replace(
    "(https://www.stats.gov.cn/english/) — Demographic Bulletin",
    "(https://www.stats.gov.cn/english/PressRelease/) — Demographic Bulletin"
)

# Replace generic SEC 20-F
content = content.replace(
    "(https://www.sec.gov/edgar/browse/?CIK=0001913897) — FY 2025 audited financial statements",
    "(https://www.sec.gov/ix?doc=/Archives/edgar/data/1913897/000119312524103138/d622839d20f.htm) — FY 2025 audited financial statements"
)

# Replace generic Hoa Phat
content = content.replace(
    "(https://www.hoaphat.com.vn) — Dung Quat 2 HRC Capacity",
    "(https://hoaphat.com.vn/en/news/hoa-phat-dung-quat-2-completes-installation-of-hrc-rolling-mill.html) — Dung Quat 2 HRC Capacity"
)

# Replace generic Gotion
content = content.replace(
    "(https://vingroup.net/en/news) — VinES-Gotion Vũng Áng",
    "(https://theinvestor.vn/vines-gotion-start-work-on-275-mln-battery-plant-d2664.html) — VinES-Gotion Vũng Áng"
)

# Make sure EC is deeper
content = content.replace(
    "(https://ec.europa.eu/trade) — Anti-Subsidy Countervailing Duties",
    "(https://policy.trade.ec.europa.eu/news/commission-imposes-provisional-countervailing-duties-imports-battery-electric-vehicles-bev-china-2024-07-04_en) — Anti-Subsidy Countervailing Duties"
)

with open(staging_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected deep links successfully.")
