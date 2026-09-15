import re

staging_file = "/Users/pro16/Documents/VideoProject/HieuBietHon/youtube_citations_staging.md"

with open(staging_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update BYD Phá Giá
byd_new = """- **Citations To Add**:
  - Hong Kong Stock Exchange (HKEX) (https://www.hkex.com.hk) — BYD Company Limited Filings (1211.HK) 
  - Reuters (https://www.reuters.com) — BYD Q1 net profit drops 55% as EV price war takes toll
  - U.S. Federal Register / BIS (https://www.federalregister.gov) — Rule 15 CFR Part 791
  - European Commission (https://ec.europa.eu/trade) — Anti-Subsidy Countervailing Duties on Chinese BEVs (27% total)
  - Nikkei Asia (https://asia.nikkei.com) — Japanese automakers scale back Southeast Asia output as Chinese EVs gain
  - Vingroup Investor Relations (https://vingroup.net/en/investor-relations) — V-Green 150,000 charging ports strategy"""
content = re.sub(r"- \*\*Local Folder\*\*: BYD-The-gioi-xua-duoi \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"- **Local Folder**: BYD-The-gioi-xua-duoi (Reverse Search)\n{byd_new}", content, flags=re.DOTALL)

# 2. Update Hòa Phát VS VinMetal
hp_new = """- **Citations To Add**:
  - Hoa Phat Group Official IR (https://www.hoaphat.com.vn) — Dung Quat 2 HRC Capacity & High-Speed Rail Plant
  - Vietnam Ministry of Industry and Trade / VnEconomy (https://vneconomy.vn) — Anti-dumping duties on Chinese HRC
  - Ha Tinh Economic Zone Authority / VnEconomy (https://vneconomy.vn) — VinMetal 80,000 billion VND steel complex approval
  - European Commission Official Portal (https://ec.europa.eu) — Carbon Border Adjustment Mechanism (CBAM) regulations
  - World Steel Association (https://worldsteel.org) — Embedded carbon intensity data"""
content = re.sub(r"## VIDEO: Hòa Phát VS VinMetal: Ai Sẽ Thâu Tóm Ngành Thép\n- \*\*ID\*\*: q3PBqQ1EFL8\n- \*\*Local Folder\*\*: HoaPhat_VinMetal \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Hòa Phát VS VinMetal: Ai Sẽ Thâu Tóm Ngành Thép\n- **ID**: q3PBqQ1EFL8\n- **Local Folder**: HoaPhat_VinMetal (Reverse Search)\n{hp_new}", content, flags=re.DOTALL)

# 3. Update Có Kịp Hóa Rồng Không?
hr_new = """- **Citations To Add**:
  - World Bank (https://datahelpdesk.worldbank.org) — GNI per capita Atlas thresholds & UMIC classification
  - World Bank Policy Report (https://www.worldbank.org) — Adapting to an Aging Society in Vietnam 
  - UNFPA Vietnam (https://vietnam.unfpa.org) — Population Ageing and Older Persons in Viet Nam
  - General Statistics Office of Vietnam (https://www.gso.gov.vn) — FDI export contribution and input import ratios
  - OECD Economic Surveys (https://www.oecd.org) — Global value chain integration analysis
  - Ministry of Planning and Investment (https://www.mpi.gov.vn) — Public investment multiplier (1.61)"""
content = re.sub(r"## VIDEO: Có Kịp Hóa Rồng Không\?\n- \*\*ID\*\*: QBsQ7xFvmP4\n- \*\*Local Folder\*\*: hoa-rong-v2 \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Có Kịp Hóa Rồng Không?\n- **ID**: QBsQ7xFvmP4\n- **Local Folder**: hoa-rong-v2 (Reverse Search)\n{hr_new}", content, flags=re.DOTALL)

# 4. Update Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc?
tv_new = """- **Citations To Add**:
  - VinFast Auto Ltd. SEC EDGAR (https://www.sec.gov/edgar/browse/?CIK=0001913897) — Shareholder voting structure and grant agreements
  - Reuters (https://www.reuters.com) — Vingroup, founder pledge $2.5 bln financial support for VinFast
  - Vingroup Official IR (https://vingroup.net/en/news) — GSM VN Holding 95% ownership structure
  - VAMA (https://vama.org.vn) — 2024 Domestic auto sales volume
  - Forbes (https://www.forbes.com/profile/pham-nhat-vuong/) — Pham Nhat Vuong profile and Technocom sale to Nestlé"""
content = re.sub(r"## VIDEO: Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc\?\n- \*\*ID\*\*: L7oucqEzuWM\n- \*\*Local Folder\*\*: pham-nhat-vuong-tinh-than-dan-toc \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc?\n- **ID**: L7oucqEzuWM\n- **Local Folder**: pham-nhat-vuong-tinh-than-dan-toc (Reverse Search)\n{tv_new}", content, flags=re.DOTALL)


# Update the 4 appended missing videos
tq_new = """- **Citations To Add**:
  - National Bureau of Statistics of China (https://www.stats.gov.cn/english/) — Demographic Bulletin on annual births
  - SAFE China (https://www.safe.gov.cn/en/) — Foreign exchange reserves data ($3.44 trillion)
  - U.S. EIA (https://www.eia.gov) — World Oil Transit Chokepoints (Strait of Malacca)
  - U.S. BIS (https://www.bis.doc.gov) — Export Administration Regulations (EAR) on semiconductor equipment
  - ASML Official Statements (https://www.asml.com) — Export control regulations for EUV/DUV"""
content = re.sub(r"## VIDEO: Trung Quốc Sợ Mỹ Vì Đâu\? Bóc Trần Sự Thật Kiềm Chế\n- \*\*ID\*\*: WxEBgp0qeAE\n- \*\*Local Folder\*\*: trung-quoc-ren-my \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Trung Quốc Sợ Mỹ Vì Đâu? Bóc Trần Sự Thật Kiềm Chế\n- **ID**: WxEBgp0qeAE\n- **Local Folder**: trung-quoc-ren-my (Reverse Search)\n{tq_new}", content, flags=re.DOTALL)

pt_new = """- **Citations To Add**:
  - VinFast Auto Ltd. SEC EDGAR Filings (https://www.sec.gov/edgar/browse/?CIK=0001913897) — FY 2025 audited financial statements
  - Vinhomes Investor Relations (https://ir.vinhomes.vn/en) — FY 2025 audited consolidated financial statements
  - Government Web Portal of Vietnam (https://baochinhphu.vn) — Politburo Resolution 68-NQ/TW on private sector development
  - The Wall Street Journal (https://www.wsj.com) — Archival reporting on Daewoo Group collapse and $15.3B accounting fraud"""
content = re.sub(r"## VIDEO: Phép Thuật Tài Chính Hay Sóng Gió Đã Qua\?\n- \*\*ID\*\*: 6nBCWNke_dg\n- \*\*Local Folder\*\*: vingroup-co-may-hoa-rong \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Phép Thuật Tài Chính Hay Sóng Gió Đã Qua?\n- **ID**: 6nBCWNke_dg\n- **Local Folder**: vingroup-co-may-hoa-rong (Reverse Search)\n{pt_new}", content, flags=re.DOTALL)

phil_new = """- **Citations To Add**:
  - IMF World Economic Outlook Database (https://www.imf.org/en/Publications/WEO) — Nominal GDP forecasts for Vietnam and Philippines
  - San Miguel Corporation Investor Relations (https://www.sanmiguel.com.ph) — Annual consolidated revenues
  - IBPAP Philippines (https://www.ibpap.org) — IT-BPM industry export revenues and employment
  - Philippine News Agency (https://www.pna.gov.ph) — Public Transport Modernization Program (PUVMP) minibus costs"""
content = re.sub(r"## VIDEO: Cú Hích VinFast Ở Philippines: Khi Nước Bạn Bị Vượt Mặt\n- \*\*ID\*\*: f-gFbIsFF3I\n- \*\*Local Folder\*\*: vietnam-vuot-philippines \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"## VIDEO: Cú Hích VinFast Ở Philippines: Khi Nước Bạn Bị Vượt Mặt\n- **ID**: f-gFbIsFF3I\n- **Local Folder**: vietnam-vuot-philippines (Reverse Search)\n{phil_new}", content, flags=re.DOTALL)

ndh_new = """- **Citations To Add**:
  - NHTSA Part 583 AALA Reports (https://www.nhtsa.gov) — US/Canadian domestic parts content for Tesla
  - VietnamPlus (https://en.vietnamplus.vn) — VinFast domestic localization rate and 2026 targets
  - Vingroup Press Release Portal (https://vingroup.net/en/news) — VinES-Gotion Vũng Áng LFP battery cell plant capacity and investment
  - ASEAN NCAP Official Assessment (https://www.aseancap.org) — 5-Star safety rating and awards for VinFast VF 8"""
content = re.sub(r"## VIDEO: Nội Địa Hóa 80% Và Sắp Có Lãi Trên Toàn Cầu\n- \*\*ID\*\*: TWsTsRQT8OM\n- \*\*Local Folder\*\*: VinfastNoiDiaHoa \(Reverse Search\)\n- \*\*Citations To Add\*\*:\n(.*)", f"## VIDEO: Nội Địa Hóa 80% Và Sắp Có Lãi Trên Toàn Cầu\n- **ID**: TWsTsRQT8OM\n- **Local Folder**: VinfastNoiDiaHoa (Reverse Search)\n{ndh_new}\n", content, flags=re.DOTALL)


with open(staging_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated staging file with actual HTTP links.")
