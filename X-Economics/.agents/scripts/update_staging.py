import re

staging_file = "/Users/pro16/Documents/VideoProject/X-Economics/youtube_citations_staging.md"

with open(staging_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update BYD Phá Giá
byd_new = """- **Citations To Add**:
  - Hong Kong Stock Exchange (HKEX) - BYD Company Limited Filings (1211.HK) — https://www.hkex.com.hk/
  - Reuters — BYD Q1 net profit drops 55% as EV price war takes toll
  - U.S. Federal Register / Bureau of Industry and Security (BIS) Rule 15 CFR Part 791
  - European Commission — Anti-Subsidy Countervailing Duties on Chinese BEVs (27% total)
  - Nikkei Asia — Japanese automakers scale back Southeast Asia output as Chinese EVs gain
  - Vingroup / VinFast Official Investor Relations — V-Green 150,000 charging ports strategy"""
content = re.sub(r"- \*\*Local Folder\*\*: neu-khong-co-vinfast \(Match score: 0\.46\)\n- \*\*Citations To Add\*\*:\n(.*?)(?=\n\n---)", f"- **Local Folder**: BYD-The-gioi-xua-duoi (Reverse Search)\n{byd_new}", content, flags=re.DOTALL)

# 2. Update Hòa Phát VS VinMetal
hp_new = """- **Citations To Add**:
  - Hoa Phat Group Official IR (hoaphat.com.vn) — Dung Quat 2 HRC Capacity & High-Speed Rail Plant
  - Vietnam Ministry of Industry and Trade (MoIT) / VnEconomy — Anti-dumping duties on Chinese HRC
  - Ha Tinh Economic Zone Authority / VnEconomy — VinMetal 80,000 billion VND steel complex approval
  - European Commission Official Portal — Carbon Border Adjustment Mechanism (CBAM) regulations
  - World Steel Association (worldsteel.org) — Embedded carbon intensity data"""
content = re.sub(r"## VIDEO: Hòa Phát VS VinMetal: Ai Sẽ Thâu Tóm Ngành Thép\n- \*\*ID\*\*: q3PBqQ1EFL8\n- \*\*Local Folder\*\*: HoaPhat_VinMetal \(Match score: 0\.60\)\n- \*\*Citations To Add\*\*:\n  - \(Không tìm thấy nguồn trong tệp research_map\)", f"## VIDEO: Hòa Phát VS VinMetal: Ai Sẽ Thâu Tóm Ngành Thép\n- **ID**: q3PBqQ1EFL8\n- **Local Folder**: HoaPhat_VinMetal (Reverse Search)\n{hp_new}", content)

# 3. Update Có Kịp Hóa Rồng Không?
hr_new = """- **Citations To Add**:
  - World Bank Country and Lending Groups — GNI per capita Atlas thresholds & UMIC classification
  - World Bank Policy Report — Adapting to an Aging Society in Vietnam (Demographic transition speed)
  - UNFPA Vietnam — Population Ageing and Older Persons in Viet Nam
  - General Statistics Office of Vietnam (GSO) — FDI export contribution and input import ratios
  - OECD Economic Surveys: Viet Nam — Global value chain integration analysis
  - Ministry of Planning and Investment (MPI) — Public investment multiplier (1.61)"""
content = re.sub(r"## VIDEO: Có Kịp Hóa Rồng Không\?\n- \*\*ID\*\*: QBsQ7xFvmP4\n- \*\*Local Folder\*\*: hoa-rong-v2 \(Match score: 0\.52\)\n- \*\*Citations To Add\*\*:\n  - \(Không tìm thấy nguồn trong tệp research_map\)", f"## VIDEO: Có Kịp Hóa Rồng Không?\n- **ID**: QBsQ7xFvmP4\n- **Local Folder**: hoa-rong-v2 (Reverse Search)\n{hr_new}", content)

# 4. Update Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc?
tv_new = """- **Citations To Add**:
  - VinFast Auto Ltd. SEC EDGAR Filings (Form 20-F / Form 6-K) — Shareholder voting structure and grant agreements
  - Reuters — Vingroup, founder pledge $2.5 bln financial support for VinFast
  - Vingroup Official IR Press Release — GSM VN Holding 95% ownership structure
  - VAMA (Vietnam Automobile Manufacturers Association) — 2024 Domestic auto sales volume
  - Forbes / Bloomberg Billionaires Index — Pham Nhat Vuong profile and Technocom sale to Nestlé"""
content = re.sub(r"## VIDEO: Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc\?\n- \*\*ID\*\*: L7oucqEzuWM\n- \*\*Local Folder\*\*: pham-nhat-vuong-tinh-than-dan-toc \(Match score: 0\.60\)\n- \*\*Citations To Add\*\*:\n  - \(Không tìm thấy nguồn trong tệp research_map\)", f"## VIDEO: Tham Vọng Cá Nhân Hay Tinh Thần Dân Tộc?\n- **ID**: L7oucqEzuWM\n- **Local Folder**: pham-nhat-vuong-tinh-than-dan-toc (Reverse Search)\n{tv_new}", content)

# Append the 4 missing videos
missing_vids = """
## VIDEO: Trung Quốc Sợ Mỹ Vì Đâu? Bóc Trần Sự Thật Kiềm Chế
- **ID**: WxEBgp0qeAE
- **Local Folder**: trung-quoc-ren-my (Reverse Search)
- **Citations To Add**:
  - National Bureau of Statistics of China (NBS) — Demographic Bulletin on annual births and population decline
  - State Administration of Foreign Exchange (SAFE China) — Foreign exchange reserves data ($3.44 trillion)
  - U.S. Energy Information Administration (EIA) — World Oil Transit Chokepoints (Strait of Malacca)
  - U.S. Bureau of Industry and Security (BIS) — Export Administration Regulations (EAR) on semiconductor equipment
  - ASML Official Statements — Export control regulations for EUV/DUV shipments to China

---

## VIDEO: Phép Thuật Tài Chính Hay Sóng Gió Đã Qua?
- **ID**: 6nBCWNke_dg
- **Local Folder**: vingroup-co-may-hoa-rong (Reverse Search)
- **Citations To Add**:
  - VinFast Auto Ltd. SEC EDGAR Filings — FY 2025 and Q1 2026 audited financial statements and net losses
  - Vinhomes Investor Relations — FY 2025 and Q1 2026 audited consolidated financial statements and net profits
  - Government Web Portal of Vietnam (chinhphu.vn) — Politburo Resolution 68-NQ/TW on private sector development
  - The Wall Street Journal / Reuters — Archival reporting on Daewoo Group collapse and $15.3B accounting fraud

---

## VIDEO: Cú Hích VinFast Ở Philippines: Khi Nước Bạn Bị Vượt Mặt
- **ID**: f-gFbIsFF3I
- **Local Folder**: vietnam-vuot-philippines (Reverse Search)
- **Citations To Add**:
  - IMF World Economic Outlook Database — Nominal GDP forecasts for Vietnam and Philippines
  - San Miguel Corporation Investor Relations — Annual consolidated revenues
  - IBPAP (IT & Business Process Association of the Philippines) — IT-BPM industry export revenues and employment
  - Philippine News Agency (PNA) — Public Transport Modernization Program (PUVMP) minibus costs

---

## VIDEO: Nội Địa Hóa 80% Và Sắp Có Lãi Trên Toàn Cầu
- **ID**: TWsTsRQT8OM
- **Local Folder**: VinfastNoiDiaHoa (Reverse Search)
- **Citations To Add**:
  - NHTSA Part 583 American Automobile Labeling Act Reports — US/Canadian domestic parts content for Tesla
  - VietnamNews / VietnamPlus — VinFast domestic localization rate and 2026 targets
  - Vingroup Press Release Portal — VinES-Gotion Vũng Áng LFP battery cell plant capacity and investment
  - ASEAN NCAP Official Assessment Reports — 5-Star safety rating and awards for VinFast VF 8

---
"""

content += missing_vids

with open(staging_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated staging file with reverse-searched citations.")
