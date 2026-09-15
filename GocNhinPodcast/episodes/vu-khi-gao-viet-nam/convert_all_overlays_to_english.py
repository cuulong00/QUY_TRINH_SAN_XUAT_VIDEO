"""
Script to convert all text overlays in prompts_chapter_01.txt to prompts_chapter_09.txt
and chapter_01_visual.md to chapter_09_visual.md into clean, professional ENGLISH.
Prevents video generation font corruption and character morphing in Google Veo.
"""

import os
import re

overlay_map = {
    # Chapter 01
    "US FARM BILL: ~1.000 TY USD": "US FARM BILL: ~$1,000B",
    "EU: 1/3 TOAN BO NGAN SACH": "EU CAP: 1/3 TOTAL BUDGET",
    "THUE GAO NHAT: 778%": "JAPAN RICE TARIFF: 778%",
    "VIEN LUA IRRI (LOS BANOS)": "IRRI RICE INSTITUTE (LOS BAÑOS)",
    "MUA HE NAM 2023": "SUMMER 2023 FOOD CRISIS",
    "AN DO CAM XUAT KHAU (20/07/2023)": "INDIA RICE EXPORT BAN (JULY 20, 2023)",
    "AN DO: 40% NGUON CUNG": "INDIA: 40% GLOBAL SUPPLY",
    "DINH GIA: 650 USD/TAN": "PEAK RICE PRICE: 650 USD/TON",
    "LAM PHAT THUC PHAM: > 8%": "FOOD INFLATION: > 8%",
    "SAC LENH GIA TRAN: EO 39": "PRICE CEILING: EO 39",
    "SAN LUONG: 43.4 TRIEU TAN LUA": "PADDY OUTPUT: 43.4M TONS",
    "XUAT KHAU: 8.1 - 8.3 TRIEU TAN": "RICE EXPORTS: 8.1 - 8.3M TONS",
    "CHI THI 24/CT-TTg": "DIRECTIVE 24/CT-TTg",
    "GIA THE GIOI: +30%": "GLOBAL RICE PRICE: +30%",
    "GAO TE: 15.000 - 16.000 D/KG": "DOMESTIC RICE: 15,000 - 16,000 VND/KG",
    "BAT COM BINH DAN: 35.000 D": "WORKER LUNCH: 35,000 VND (~$1.40)",
    "LAM PHAT 2023: 3.25%": "VIETNAM CPI 2023: 3.25%",
    "VI THE BAN CO DIA KINH TE": "GEO-ECONOMIC FOOD SOVEREIGNTY",

    # Chapter 02
    "LUONG CONG NHAN: 7 - 9 TRIEU DONG": "WORKER SALARY: 7 - 9M VND ($300 - $370)",
    "BAT COM BINH DAN: 35.000 DONG": "WORKER LUNCH: 35,000 VND (~$1.40)",
    "LAM PHAT MUC TIEU: < 4%": "INFLATION TARGET: < 4%",
    "CPI THUC PHAM: BI ANH HUONG BOI GAO": "CPI BASKET: RICE PRICE ANCHOR",
    "SAN LUONG LUA: 43.4 - 43.5M TAN": "ANNUAL PADDY OUTPUT: 43.4M TONS",
    "NANG SUAT LUA: 6.1 - 7.2 TAN/HA": "AVERAGE YIELD: 6.1 - 7.2 TONS/HA",
    "XUAT KHAU: 5.75 TY USD (2024)": "RECORD EXPORTS: $5.75B (2024)",
    "GIA TRI GIA TANG RONG (DVA): 75% - 80%": "DOMESTIC VALUE ADDED: 75% - 80%",
    "FDI CONG NGHIEP: CHI PHI NHAN CONG ON DINH": "FDI ANCHOR: COMPETITIVE LABOR COST",
    "CHI PHI PHAN BON: +80%": "FERTILIZER COST: +80%",
    "BIEN LOI NHUAN NONG DAN: 10% - 15%": "FARMER NET MARGIN: 10% - 15%",
    "LO XO GIAM XOC VI MO": "MACROECONOMIC SHOCK ABSORBER",
    "BUONG MAY DONG BANG: 3 VU LIEN TUC": "DELTA ENGINE: 3 CONTINUOUS CROPS",

    # Chapter 03
    "DAT CHUYEN CANH LUA: 1.5M HA": "DEDICATED RICE LAND: 1.5M HA",
    "DIEN TICH GIEO TRONG: ~3.9M HA": "ANNUAL CULTIVATED AREA: ~3.9M HA",
    "HE SO QUAY VONG: 2.4 LAN": "LAND ROTATION COEFFICIENT: 2.4X",
    "3 VU: DONG XUAN - HE THU - THU DONG": "3 CROPS: WINTER-SPRING / SUMMER-AUTUMN / AUTUMN-WINTER",
    "NANG SUAT DONG XUAN: 7 - 8 TAN/HA": "WINTER-SPRING YIELD: 7 - 8 TONS/HA",
    "GIONG LUA NGAN NGAY: 90 - 100 NGAY": "SHORT-DURATION SEED: 90 - 100 DAYS",
    "AN DO & THAI LAN: 1 VU CHINH/NAM": "INDIA & THAILAND: 1 MAIN CROP/YEAR",
    "CHUOI CUNG UNG CUON TRON (ROLLING)": "ROLLING SUPPLY CHAIN MODEL",
    "XAY XAT & DONG BAO: 48 GIO": "MILLING & PACKAGING: 48 HOURS",
    "TIET KIEM LUU KHO: 40% - 50%": "WAREHOUSING COST SAVINGS: 40% - 50%",
    "DBSCL: > 90% GAO XUAT KHAU": "MEKONG DELTA: > 90% EXPORT SHARE",
    "XUAT KHAU: > 8 TRIEU TAN GAO/NAM": "ANNUAL EXPORTS: > 8M TONS",
    "TIEN DON IRRI (LOS BANOS)": "IRRI LOS BAÑOS RESEARCH GATE",

    # Chapter 04
    "IRRI - LOS BAÑOS, 1960s": "IRRI - LOS BAÑOS, 1960s",
    "GIỐNG LÚA THẦN NÔNG IR8": "MIRACLE RICE IR8",
    "DỊCH VỤ BPO & KIỀU HỐI": "BPO SERVICES & REMITTANCES",
    "BẪY PHI CÔNG NGHIỆP HÓA NON": "PREMATURE DEINDUSTRIALIZATION TRAP",
    "NĂNG SUẤT LÚA: < 4 TẤN/HA": "RICE YIELD: < 4 TONS/HA",
    "DÂN SỐ: > 115 TRIỆU NGƯỜI": "POPULATION: > 115 MILLION",
    "NHẬP KHẨU: 3,8 - 4,5 TRIỆU TẤN/NĂM": "IMPORTS: 3.8 - 4.5M TONS/YEAR",
    "> 80% NHẬP TỪ VIỆT NAM": "> 80% IMPORTS FROM VIETNAM",
    "LẠM PHÁT THỰC PHẨM > 8%": "FOOD INFLATION: > 8%",
    "SẮC LỆNH KHẨN CẤP SỐ 39": "EXECUTIVE ORDER NO. 39",
    "HIỆP ĐỊNH LIÊN CHÍNH PHỦ 5 NĂM": "5-YEAR BILATERAL RICE AGREEMENT",

    # Chapter 05
    "XUẤT KHẨU: > 9 TRIỆU TẤN (~5,7 TỶ USD)": "EXPORTS: > 9M TONS (~$5.7B)",
    "NHẬP KHẨU: 1,5 - 2,5 TRIỆU TẤN/NĂM": "IMPORTS: 1.5 - 2.5M TONS/YEAR",
    "> 80% DIỆN TÍCH: GẠO THƠM CAO CẤP": "> 80% AREA: PREMIUM AROMATIC RICE",
    "GIÁ XUẤT KHẨU: 600 - 900 USD/TẤN": "EXPORT PRICE: 600 - 900 USD/TON",
    "TIÊU THỤ: BÚN, PHỞ, BÁNH TRÁNG, HỦ TIẾU": "DOMESTIC FOOD: NOODLES & RICE PAPER",
    "HÓA SINH: GẠO AMYLOSE CAO (> 25%)": "BIOCHEMISTRY: HIGH AMYLOSE (> 25%)",
    "NGHỊCH LÝ CUNG - CẦU CHẾ BIẾN": "PROCESSING SUPPLY-DEMAND PARADOX",
    "CHÊNH LỆCH GIÁ: GẠO THÔ RẺ HƠN 50%": "RAW PADDY ARBITRAGE: 50% CHEAPER",
    "TRUNG TÂM XAY XÁT: THỐT NỐT & CÁI BÈ": "MILLING HUBS: THOT NOT & CAI BE",
    "TRUNG TÂM TINH CHẾ TIỂU VÙNG MEKONG": "LOWER MEKONG REFINING HUB",
    "ẤN ĐỘ XẢ KHO DỰ TRỮ (2024 - 2025)": "INDIA STRATEGIC RESERVE RELEASE",

    # Chapter 06
    "ĐỈNH CAO 2024: > 9M TẤN (~5,7 TỶ USD)": "HISTORIC PEAK 2024: > 9M TONS ($5.7B)",
    "GIÁ ĐỈNH: 627 USD/TẤN": "PEAK BENCHMARK: 627 USD/TON",
    "SẢN LƯỢNG ẤN ĐỘ: > 138M TẤN": "INDIA HARVEST: > 138M TONS",
    "KHO DỰ TRỮ FCI: ~50M TẤN (GẤP 4 LẦN)": "FCI GRAIN RESERVES: ~50M TONS (4X BUFFER)",
    "ẤN ĐỘ DỠ BỎ CẤM XUẤT KHẨU": "INDIA LIFTS RICE EXPORT EMBARGO",
    "CHỈ SỐ GIÁ FAO: GIẢM 29% (2025)": "FAO RICE PRICE INDEX: -29% (2025)",
    "GIÁ GẠO THẾ GIỚI: < 500 USD/TẤN": "GLOBAL BENCHMARK: < 500 USD/TON",
    "VIỆT NAM 2025: ~4,1 TỶ USD": "VIETNAM 2025: ~$4.1 BILLION",
    "GIÁ BÌNH QUÂN: 509 USD/TẤN": "AVERAGE EXPORT PRICE: 509 USD/TON",
    "ĐẤT LÚA ẤN ĐỘ: > 44M HA (GẤP 11 LẦN)": "INDIA PADDY LAND: > 44M HA (11X VIETNAM)",
    "> 80% XUẤT KHẨU: GẠO THƠM CAO CẤP": "> 80% EXPORTS: PREMIUM AROMATIC RICE",
    "ÁO GIÁP THƯƠNG HIỆU & CHẤT LƯỢNG": "BRAND & QUALITY VALUE SHIELD",

    # Chapter 07
    "11+ ĐẬP THỦY ĐIỆN BẬC THANG MEKONG": "11+ MEKONG CASCADE MEGA-DAMS",
    "50% - 70% PHÙ SA BỊ CHẶN LẠI": "50% - 70% SEDIMENT TRAPPED",
    "HIỆN TƯỢNG 'NƯỚC ĐÓI PHÙ SA'": "'HUNGRY WATER' RIVERBED SCOURING",
    "KÊNH PHÙ NAM TECHO: 180 KM (~1,7 TỶ USD)": "FUNAN TECHO CANAL: 180 KM ($1.7B)",
    "RANH MẶN 4‰: ĂN SÂU 60 - 95 KM": "4‰ SALINITY FRONTIER: 60 - 95 KM INLAND",
    "SỤT LÚN ĐỒNG BẰNG: 1 - 3 CM/NĂM": "DELTA SUBSIDENCE: 1 - 3 CM/YEAR",
    "TƯ DUY 'NGỌT HÓA CƯỠNG BỨC'": "'FORCED FRESHWATER' INFRASTRUCTURE",
    "LÚA: CHỊU MẶN < 2‰": "RICE SALINITY TOLERANCE: < 2‰",
    "TÔM: CẦN MẶN 10 - 25‰": "SHRIMP SALINITY REQUIREMENT: 10 - 25‰",
    "XUNG ĐỘT SINH KẾ LÚA - TÔM": "RICE VS SHRIMP LIVELIHOOD CONFLICT",
    "CHI PHÍ LOGISTICS: 25% - 30%": "LOGISTICS COST BURDEN: 25% - 30%",
    "ĐIỂM NGHẼN: LUỒNG ĐỊNH AN BỒI LẮNG": "BOTTLENECK: DINH AN CHANNEL SILTATION",
    "CHI PHÍ PHÁT SINH: 7 - 10 USD/TẤN": "DETOUR PENALTY: 7 - 10 USD/TON",

    # Chapter 08
    "NGHỊ QUYẾT 120/NQ-CP: PHÁT TRIỂN THUẬN THIÊN": "GOVERNMENT RESOLUTION 120: NATURE-BASED ADAPTATION",
    "LÚA - TÔM: 80 - 120 TRIỆU ĐỒNG/HA": "RICE-SHRIMP REVENUE: 80 - 120M VND/HA",
    "SIÊU THỦY LỢI CÁI LỚN - CÁI BÉ": "CAI LON - CAI BE SLUICE MEGA-PROJECT",
    "BẢO VỆ GẦN 400.000 HA ĐỒNG RUỘNG": "PROTECTING ~400,000 HA AGRICULTURAL LAND",
    "ĐỀ ÁN 1 TRIỆU HA LÚA PHÁT THẢI THẤP": "1-MILLION-HA LOW-EMISSION RICE PROJECT",
    "TƯỚI NGẬP KHÔ XEN KẼ (AWD)": "ALTERNATE WETTING & DRYING (AWD)",
    "BÁN TÍN CHỈ CARBON NÔNG NGHIỆP": "AGRICULTURAL CARBON CREDIT MONETIZATION",
    "ĐẠI CẢNG NƯỚC SÂU TRẦN ĐỀ: ~50.000 TỶ": "TRAN DE DEEP-SEA GATEWAY PORT: ~$2B",
    "CẮT GIẢM 30% CHI PHÍ LOGISTICS": "30% LOGISTICS COST REDUCTION",
    "LUẬT ĐẤT ĐAI 2024: NỚI HẠN MỨC 15 LẦN": "2024 LAND LAW: 15X ACREAGE EXPANSION",

    # Chapter 09
    "TRAO CẦN CÂU SINH KẾ NÔNG NGHIỆP": "PROVIDING THE FISHING ROD: KNOWLEDGE TRANSFER",
    "GS. VÕ TÒNG XUÂN (SIERRA LEONE)": "PROF. VO TONG XUAN (SIERRA LEONE)",
    "DỰ ÁN HỢP TÁC FAO: 5 TRIỆU USD": "FAO TRIPARTITE PARTNERSHIP: $5 MILLION",
    "VÌ VIỆT NAM, CUBA SẴN SÀNG HIẾN DÂNG CẢ MÁU": "'FOR VIETNAM, CUBA WILL SHED ITS BLOOD' - FIDEL CASTRO",
    "NĂNG SUẤT TẠI CUBA: 5,5 TẤN/HA (~50.000 HA)": "YIELD IN CUBA: 5.5 TONS/HA (~50,000 HA)",
    "DÒNG LÚA THUẦN VIBA (VIỆT NAM - CUBA)": "VIBA PURE RICE STRAIN (VIETNAM - CUBA)",
    "DỰ ÁN AGRI VMA: 1.000 HA (PINAR DEL RÍO)": "AGRI VMA PROJECT: 1,000 HA (PINAR DEL RÍO)",
    "NĂNG SUẤT ĐẠT 9 TẤN/HA (BÀN GIAO 2.400 TẤN)": "RECORD YIELD: 9 TONS/HA (2,400 TONS HANDOVER)",
    "SỨ GIẢ HÒA BÌNH & NHÂN PHẨM DÂN TỘC": "AMBASSADOR OF PEACE & HUMAN DIGNITY"
}

episodes_dir = "episodes/vu-khi-gao-viet-nam"

# 1. Update prompts_chapter_XX.txt
for ch in range(1, 10):
    prompt_file = os.path.join(episodes_dir, f"prompts_chapter_{ch:02d}.txt")
    if not os.path.exists(prompt_file):
        continue
    with open(prompt_file, "r", encoding="utf-8") as f:
        content = f.read()

    replaced_count = 0
    for vn_text, en_text in overlay_map.items():
        pattern = f'reading "{vn_text}"'
        if pattern in content:
            content = content.replace(pattern, f'reading "{en_text}"')
            replaced_count += 1

    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Updated {prompt_file}: {replaced_count} overlays converted to English")

# 2. Update chapter_XX_visual.md
for ch in range(1, 10):
    vis_file = os.path.join(episodes_dir, f"chapter_{ch:02d}_visual.md")
    if not os.path.exists(vis_file):
        continue
    with open(vis_file, "r", encoding="utf-8") as f:
        content = f.read()

    replaced_count = 0
    for vn_text, en_text in overlay_map.items():
        # Match markdown bolded quotes
        pattern1 = f'**"{vn_text}"**'
        pattern2 = f'"{vn_text}"'
        if pattern1 in content:
            content = content.replace(pattern1, f'**"{en_text}"**')
            replaced_count += 1
        elif pattern2 in content:
            content = content.replace(pattern2, f'"{en_text}"')
            replaced_count += 1

    with open(vis_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Updated {vis_file}: {replaced_count} overlays converted to English")

print("\n🚀 All prompt files and storyboard tables successfully converted to English overlays!")
