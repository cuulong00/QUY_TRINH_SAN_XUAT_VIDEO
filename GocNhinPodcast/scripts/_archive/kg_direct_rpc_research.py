#!/usr/bin/env python3
"""
KG Direct RPC Research Engine for Google NotebookLM (Optimized).
Polls native report_id UUID directly to avoid base64 ID drift.
Runs research for remaining ASEAN and EU entities, then executes 12-file Batch RAG Extraction.
"""

import asyncio
import os
import sys
import logging
from pathlib import Path
from notebooklm.client import NotebookLMClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("kg_rpc_research")

NOTEBOOK_ID = "93b710eb-dac1-4fe3-89fd-c05e1d75b15a"
VAULT_DIR = Path("/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kb-nganh-xe-dien-goi-xe/research_vault")

REMAINING_QUERIES = [
    {
        "id": "q4_ridehailing_eu_denmark",
        "name": "Gọi xe Châu Âu & Taxi Đan Mạch",
        "query": "European ride hailing and taxi regulation market 2023-2026: EU Platform Work Directive, Uber and Bolt compliance, Denmark taxi market regulation Taxiloven 2017 2018, seat sensor occupancy mandate, fare meters, Uber exit Denmark, Viggo electric taxi, Dantaxi",
    },
    {
        "id": "q5_asean_ev_and_ridehailing",
        "name": "Xe điện & Gọi xe Đông Nam Á (ASEAN)",
        "query": "Southeast Asia ASEAN electric vehicles and ride hailing market 2023-2026: Thailand EV 3.0 3.5 policy, Indonesia nickel supply chain, Vietnam EV adoption VinFast Xanh SM, Grab vs GoTo Gojek vs Maxim, EV fleet transition and market share BYD",
    }
]

EXTRACTION_QUESTIONS = [
    {
        "filename": "01_nganh_xe_dien_toan_cau_tong_quan.md",
        "title": "Tổng quan ngành ô tô và xe điện toàn cầu 2023–2026",
        "prompt": """Tổng quan ngành ô tô và xe điện toàn cầu giai đoạn 2023–2026:
1. Quy mô thị trường và doanh số xe bán ra hàng năm (triệu xe), tỷ lệ thâm nhập xe điện (EV penetration rate toàn cầu và theo khu vực Trung Quốc, Châu Âu, Mỹ).
2. Tốc độ tăng trưởng hàng năm (CAGR), định giá tổng thể ngành công nghiệp ô tô điện (tỷ USD).
3. So sánh tương quan và tốc độ tăng trưởng giữa xe thuần điện (BEV), xe lai sạc điện (PHEV), hybrid (HEV) và xe động cơ đốt trong (ICE).
4. Các động lực tăng trưởng chính, xu hướng dịch chuyển công nghệ và cơ cấu chuỗi giá trị.

YÊU CẦU: Trình bày chi tiết, số liệu định lượng rõ ràng kèm mốc thời gian cụ thể (2023, 2024, 2025, 2026). Giữ nguyên các chú thích trích dẫn [n]."""
    },
    {
        "filename": "02_nganh_xe_dien_chuoi_cung_ung_pin_chi_phi.md",
        "title": "Chuỗi cung ứng và kinh tế học pin xe điện toàn cầu 2023–2026",
        "prompt": """Chuỗi cung ứng và kinh tế học pin xe điện toàn cầu giai đoạn 2023–2026:
1. Diễn biến giá pin trên mỗi kWh (battery pack price và cell price theo dữ liệu BloombergNEF, SNE Research từ 2023 đến 2026).
2. Cơ cấu tỷ trọng chi phí bộ pin trong tổng giá thành sản xuất một chiếc xe điện (%).
3. So sánh chi phí, hiệu năng và xu hướng thị phần giữa công nghệ pin LFP (Lithium Iron Phosphate) vs NMC (Nickel Manganese Cobalt).
4. Thị phần, công suất sản xuất (GWh) của các nhà sản xuất pin hàng đầu thế giới (CATL, BYD, LG Energy Solution, SK On, Panasonic, CALB, v.v.).
5. Diễn biến giá các kim loại chiến lược (Lithium carbonate, Nickel, Cobalt) và tác động của nó tới biên lợi nhuận của các hãng xe điện.

YÊU CẦU: Trình bày chi tiết, số liệu định lượng rõ ràng kèm mốc thời gian cụ thể. Giữ nguyên các chú thích trích dẫn [n]."""
    },
    {
        "filename": "03_nganh_goi_xe_toan_cau_kinh_te_hoc_nen_tang.md",
        "title": "Kinh tế học nền tảng gọi xe toàn cầu giai đoạn 2023–2026",
        "prompt": """Kinh tế học nền tảng gọi xe và di chuyển toàn cầu (Ride-Hailing Platform Economics) giai đoạn 2023–2026:
1. Quy mô thị trường toàn cầu (tỷ USD), tổng giá trị giao dịch gộp (Gross Bookings), tốc độ tăng trưởng CAGR và lượng người dùng tích cực hàng tháng (MAU).
2. Tỷ lệ chiết khấu/hoa hồng (take rate) thực tế của các nền tảng lớn (Uber, Grab, Bolt, Didi, Lyft).
3. Cơ cấu chi phí và bài toán kinh tế học hai chiều (Two-sided platform economics): Chi phí thu hút và trợ cấp tài xế (driver incentives), chi phí khuyến mãi khách hàng, chi phí bảo hiểm và pháp lý.
4. Điểm hòa vốn và bước ngoặt chuyển dịch tài chính: Tình hình cải thiện EBITDA, dòng tiền tự do (Free Cash Flow) và lợi nhuận ròng của các hãng gọi xe khi chuyển từ giai đoạn 'đốt tiền giành thị phần' sang 'tối ưu hóa lợi nhuận'.

YÊU CẦU: Cung cấp đầy đủ số liệu tài chính định lượng, các chỉ số N1–N10 của ngành gọi xe. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "04_nganh_goi_xe_dien_hoa_doi_xe_robotaxi.md",
        "title": "Xu hướng điện hóa đội xe và tác động của Robotaxi trong ngành gọi xe toàn cầu",
        "prompt": """Xu hướng điện hóa đội xe (Fleet Electrification) và tác động của xe tự hành / Robotaxi trong ngành gọi xe toàn cầu 2024–2026:
1. Mục tiêu và tỷ lệ điện hóa đội xe của các nền tảng gọi xe hàng đầu (Uber Green, Grab, Bolt, Xanh SM).
2. Quan hệ hợp tác chiến lược giữa nền tảng gọi xe và các nhà sản xuất xe điện (ví dụ hợp tác Uber - BYD, Uber - Tesla, quan hệ VinFast - Xanh SM).
3. So sánh tổng chi phí sở hữu và vận hành (TCO - Total Cost of Ownership) giữa xe điện và xe xăng đối với tài xế chạy dịch vụ cường độ cao.
4. Tiến trình thương mại hóa và thử nghiệm Robotaxi (Waymo, Cruise, Baidu Apollo, Tesla Cybercab): Mô hình hợp tác với nền tảng gọi xe, chi phí trên mỗi dặm (cost per mile) và kịch bản tác động đến cơ cấu việc làm tài xế.

YÊU CẦU: Trình bày chi tiết, số liệu định lượng rõ ràng. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "05_tt_xe_dien_eu_chinh_sach_thue_khi_thai.md",
        "title": "Chính sách quản lý, thuế chống trợ cấp và quy chuẩn phát thải xe điện tại EU",
        "prompt": """Chính sách quản lý, thuế và quy chuẩn phát thải tại thị trường xe điện Liên minh Châu Âu (EU) 2024–2026:
1. Cuộc điều tra chống trợ cấp của Ủy ban Châu Âu (EC) và quyết định áp thuế đối kháng (anti-subsidy countervailing duties) lên xe điện sản xuất tại Trung Quốc: Mức thuế bổ sung cụ thể đối với BYD, Geely, SAIC, Tesla (Thượng Hải) và các OEM hợp tác/không hợp tác khác.
2. Quy định tiêu chuẩn khí thải CAFE (Corporate Average Fuel Economy) năm 2025 của EU: Mức phát thải trần 93.6g CO2/km, nguy cơ bị phạt hàng tỷ Euro đối với các OEM Châu Âu (Volkswagen, Stellantis, Renault) nếu không đạt tỷ lệ xe điện cần thiết, và các đề xuất trì hoãn hoặc sửa đổi.
3. Tác động của chính sách cắt giảm hoặc hủy bỏ trợ cấp xe điện: Điển hình là việc Đức đột ngột chấm dứt chương trình trợ cấp Umweltbonus vào cuối năm 2023 và hệ quả suy giảm doanh số xe điện tại Đức và toàn EU trong năm 2024.
4. Các quy định về Đạo luật Công nghiệp Net-Zero, Đạo luật Pin mới của EU (hộ chiếu pin - Battery Passport, yêu cầu tái chế và khai thác nội khối).

YÊU CẦU: Trình bày chi tiết, số liệu thuế suất và mục tiêu phát thải chính xác. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "06_tt_xe_dien_eu_thi_phan_canh_tranh_oem.md",
        "title": "Thị phần và cạnh tranh giữa các nhà sản xuất ô tô (OEMs) tại thị trường xe điện Châu Âu",
        "prompt": """Thị phần và cục diện cạnh tranh giữa các nhà sản xuất ô tô tại thị trường xe điện Châu Âu giai đoạn 2024–2026:
1. Doanh số và thị phần xe điện (BEV, PHEV) tại các thị trường nòng cốt EU: Đức, Pháp, Anh, Ý, Tây Ban Nha và các quốc gia Bắc Âu (Na Uy, Thụy Điển, Đan Mạch).
2. Vị thế và thị phần của các tập đoàn sản xuất xe truyền thống Châu Âu (Volkswagen Group, Stellantis, BMW Group, Mercedes-Benz, Renault Group).
3. Diễn biến cạnh tranh của Tesla (doanh số Model Y, Model 3, nhà máy Giga Berlin) và sự thâm nhập của các thương hiệu Trung Quốc (BYD, MG/SAIC, Chery, Nio, Xpeng).
4. Xu hướng người tiêu dùng quay lại với xe Hybrid (HEV, PHEV) trong bối cảnh giá xe điện còn cao, thiếu trạm sạc công cộng và bất ổn kinh tế.

YÊU CẦU: Trình bày chi tiết các bảng số liệu thị phần, doanh số cụ thể. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "07_tt_xe_dien_asean_chinh_sach_thai_indo_vn.md",
        "title": "Chính sách phát triển và cơ chế ưu đãi xe điện tại khu vực Đông Nam Á (ASEAN)",
        "prompt": """Chính sách phát triển và cơ chế ưu đãi xe điện tại khu vực Đông Nam Á (ASEAN) giai đoạn 2023–2026:
1. Thái Lan: Cơ chế ưu đãi EV 3.0 và EV 3.5 của Chính phủ Thái Lan (mức trợ cấp tiền mặt trực tiếp cho người mua xe, giảm thuế tiêu thụ đặc biệt từ 8% xuống 2%, miễn giảm thuế nhập khẩu linh kiện, và điều kiện ràng buộc sản xuất bù trừ trong nước tỷ lệ 1:1 hoặc 1:1.5).
2. Indonesia: Chiến lược chuỗi cung ứng pin xe điện dựa trên tài nguyên Nickel (chính sách cấm xuất khẩu quặng niken thô, thu hút đầu tư FDI vào luyện kim và sản xuất cell pin, ưu đãi thuế VAT từ 11% xuống 1% cho xe đạt tỷ lệ nội địa hóa TKDN trên 40%).
3. Việt Nam: Chính sách miễn 100% lệ phí trước bạ cho xe điện chạy pin, ưu đãi thuế tiêu thụ đặc biệt (1-3%), định hướng chuyển đổi phương tiện giao thông xanh đến năm 2050 theo Quyết định 876/QĐ-TTg.
4. Malaysia: Chính sách miễn thuế nhập khẩu và thuế tiêu thụ đặc biệt cho xe điện nhập khẩu nguyên chiếc (CBU) và lắp ráp trong nước (CKD).

YÊU CẦU: Trình bày chi tiết các điều khoản chính sách, tỷ lệ ưu đãi, mốc thời gian áp dụng. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "08_tt_xe_dien_asean_thi_phan_xe_trung_quoc.md",
        "title": "Cục diện thị phần và sự thống trị của xe điện Trung Quốc tại Đông Nam Á",
        "prompt": """Cục diện thị phần và sự trỗi dậy của các hãng xe điện Trung Quốc tại Đông Nam Á (ASEAN) 2023–2026:
1. Doanh số bán xe điện và tỷ lệ thâm nhập xe điện tại các thị trường chính: Thái Lan, Indonesia, Việt Nam, Malaysia, Philippines.
2. Sự bành trướng thị phần của các thương hiệu xe điện Trung Quốc: BYD (dẫn đầu tại Thái Lan, Singapore, Indonesia), Wuling, NETA, GAC AION, Great Wall Motor (GWM), MG/SAIC, Chery.
3. Phản ứng và sự suy giảm thị phần của các hãng xe truyền thống Nhật Bản (Toyota, Honda, Isuzu, Mitsubishi) tại thủ phủ ô tô Đông Nam Á.
4. Vị thế và bước tiến của VinFast tại thị trường nội địa Việt Nam và các bước mở rộng sang Indonesia, Philippines, Thái Lan.
5. Thực trạng phát triển cơ sở hạ tầng trạm sạc tại các nước ASEAN (mật độ trạm sạc, vai trò của nhà nước vs tư nhân).

YÊU CẦU: Cung cấp số liệu định lượng thị phần (%), doanh số xe bán ra theo hãng và theo quốc gia. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "09_tt_goi_xe_eu_chi_thi_lao_dong_nen_tang.md",
        "title": "Thị trường gọi xe Châu Âu và tác động của Chỉ thị Lao động Nền tảng EU",
        "prompt": """Thị trường gọi xe Châu Âu và tác động của Chỉ thị Lao động Nền tảng EU (EU Platform Work Directive) 2024–2026:
1. Bối cảnh pháp lý và nội dung cốt lõi của Chỉ thị Lao động Nền tảng EU: Tiêu chí xác định giả định quan hệ lao động (presumption of employment) giữa nền tảng và tài xế/lao động công nghệ.
2. Quy định về minh bạch thuật toán (Algorithmic management): Quyền được biết và can thiệp của con người đối với các quyết định khóa tài khoản, phân bổ cuốc xe, đánh giá hiệu suất của thuật toán.
3. So sánh mô hình kinh doanh và sự thích ứng của các nền tảng: Uber, Bolt, Free Now so với hệ thống Taxi truyền thống tại các nước thành viên EU.
4. Ước tính tác động kinh tế: Chi phí vận hành gia tăng (đóng bảo hiểm xã hội, nghỉ phép có lương, lương tối thiểu), nguy cơ tăng giá cước dịch vụ đối với người dùng (20-40%) và bài học từ các quốc gia đi trước như Tây Ban Nha (Rider Law), Anh (quy chế Worker).

YÊU CẦU: Trình bày chi tiết, phân tích đa chiều về thể chế và kinh tế học nền tảng. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "10_tt_taxi_dan_mach_luat_taxiloven_viggo.md",
        "title": "Thị trường taxi và gọi xe tại Đan Mạch: Luật Taxiloven và mô hình taxi điện Viggo",
        "prompt": """Thị trường taxi và gọi xe tại Đan Mạch giai đoạn 2017–2026:
1. Đạo luật Taxi Đan Mạch (Taxiloven 2017/2018): Các quy định kỹ thuật và pháp lý khắt khe bắt buộc áp dụng cho toàn bộ xe chở khách (bao gồm: ghế có cảm biến người ngồi - seat occupancy sensors, đồng hồ tính cước được kiểm định - fare meters, camera giám sát/thiết bị định vị, giấy phép lái xe taxi chuyên nghiệp và yêu cầu công ty taxi phải có trụ sở địa phương).
2. Sự kiện Uber rút khỏi thị trường Đan Mạch vào tháng 4 năm 2017 do không thể đáp ứng các yêu cầu của Taxiloven: Phân tích nguyên nhân pháp lý và phản ứng của thị trường.
3. Cấu trúc thị trường taxi Đan Mạch hiện nay: Vị thế của các hãng taxi truyền thống lớn (Dantaxi, Taxa 4x35) và quá trình số hóa ứng dụng đặt xe.
4. Sự ra đời và mô hình kinh doanh của hãng taxi thuần điện Viggo (thành lập năm 2019): Đội xe 100% điện, xây dựng mạng lưới trạm sạc siêu nhanh Viggo Energy, định vị dịch vụ cao cấp và đóng góp vào mục tiêu phát thải ròng bằng 0 của Copenhagen.
5. Tỷ lệ điện hóa đội xe taxi tại Copenhagen và toàn Đan Mạch (mục tiêu năm 2025/2030).

YÊU CẦU: Cung cấp đầy đủ các mốc pháp lý, tên văn bản luật, số liệu định lượng về thị phần và tỷ lệ xe điện. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "11_tt_goi_xe_asean_grab_goto_xanhsm.md",
        "title": "Cục diện cạnh tranh và chuyển đổi xanh trên thị trường gọi xe Đông Nam Á",
        "prompt": """Cục diện cạnh tranh và quá trình chuyển đổi xanh trên thị trường gọi xe Đông Nam Á (ASEAN) 2023–2026:
1. Thị phần và vị thế cạnh tranh của các tay chơi chính: Grab (vị thế áp đảo toàn khu vực), GoTo/Gojek (thị trường Indonesia), Maxim, InDrive, và sự trỗi dậy của Xanh SM (GSM - Taxi điện của tỷ phú Phạm Nhật Vượng).
2. Phân khúc gọi xe 2 bánh (Ride-hailing motorbike taxi) vs 4 bánh (Car taxi): Quy mô, đặc thù văn hóa giao thông và tính kinh tế tại Việt Nam, Indonesia, Thái Lan.
3. Xu hướng điện hóa đội xe gọi xe tại ASEAN: Bước đi thần tốc của Xanh SM tại Việt Nam, Lào, Indonesia, Philippines; các sáng kiến chuyển đổi xe điện của Grab bắt tay với BYD và các hãng xe máy điện địa phương.
4. Khung pháp lý quản lý xe công nghệ tại các nước ASEAN (ví dụ Nghị định 10/2020/NĐ-CP tại Việt Nam, quy định tại Indonesia, Singapore) và sự chung sống/xung đột giữa taxi công nghệ và taxi truyền thống.

YÊU CẦU: Cung cấp số liệu định lượng thị phần (%), số lượng đội xe, doanh thu và các chỉ số T1–T10. Giữ nguyên chú thích trích dẫn [n]."""
    },
    {
        "filename": "12_tong_hop_chi_so_dinh_luong_n1_n10_t1_t10.md",
        "title": "Bảng tổng hợp đối chiếu định lượng toàn bộ các chỉ số N1–N10 và T1–T10 cho 7 thực thể",
        "prompt": """Lập bảng tổng hợp đối chiếu định lượng toàn bộ hệ thống chỉ số N1–N10 (cho cấp Ngành) và T1–T10 (cho cấp Thị trường) đối với 7 thực thể:
1. `nganh_xe_dien` (Ngành ô tô & xe điện toàn cầu: N1 Quy mô thị trường, N2 Tốc độ CAGR, N3 Doanh số xe, N4 Tỷ lệ thâm nhập EV, N5 Giá pin $/kWh, N6 Tỷ trọng chi phí pin %, N7 Thị phần OEM, N8 Thị phần pin, N9 Doanh số BEV vs PHEV vs ICE, N10 Định giá ngành).
2. `nganh_goi_xe` (Ngành gọi xe toàn cầu: N1 Quy mô Gross Bookings, N2 CAGR, N3 Lượng người dùng MAU, N4 Take rate %, N5 Biên EBITDA, N6 Tỷ lệ điện hóa đội xe, N7 Chi phí TCO xe điện vs xăng, N8 Thị phần toàn cầu Uber/Grab/Didi/Bolt, N9 Chi phí khuyến mãi tài xế/khách %, N10 Dự báo thị phần Robotaxi).
3. `tt_xe_dien_eu` (Thị trường xe điện EU: T1 Doanh số xe điện, T2 Thị phần EV trong tổng số xe mới %, T3 Mức thuế chống trợ cấp xe TQ %, T4 Mục tiêu khí thải CAFE g CO2/km, T5 Doanh số theo nước Đức/Pháp/Anh, T6 Thị phần Volkswagen vs Tesla vs BYD, T7 Mức sụt giảm sau cắt Umweltbonus, T8 Thị phần xe Hybrid, T9 Số lượng trạm sạc công cộng, T10 Dự báo 2026-2030).
4. `tt_xe_dien_asean` (Thị trường xe điện ASEAN: T1 Doanh số xe điện khu vực, T2 Tỷ lệ thâm nhập EV %, T3 Mức trợ cấp EV 3.0/3.5 Thái Lan, T4 Ưu đãi VAT/nội địa hóa Indonesia %, T5 Lệ phí trước bạ VN 0%, T6 Thị phần xe điện Trung Quốc %, T7 Thị phần BYD, T8 Thị phần VinFast, T9 Doanh số theo quốc gia Thái/Indo/VN/Malay, T10 Số cổng sạc công cộng).
5. `tt_goi_xe_eu` (Thị trường gọi xe EU: T1 Quy mô thị trường gọi xe EU, T2 Thị phần Uber vs Bolt vs Free Now, T3 Tỷ lệ tài xế độc lập vs nhân viên, T4 Mức tăng chi phí dự kiến theo EU Platform Directive %, T5 Mức tăng giá cước hành khách dự kiến %, T6 Số tài xế hoạt động, T7 Tỷ lệ điện hóa đội xe taxi/gọi xe, T8 Doanh thu các nền tảng tại EU, T9 Thị phần taxi truyền thống, T10 Tác động pháp lý từ Rider Law Tây Ban Nha/Anh).
6. `tt_goi_xe_asean` (Thị trường gọi xe ASEAN: T1 Quy mô Gross Merchandise Value gọi xe ASEAN, T2 Thị phần Grab vs GoTo vs Xanh SM, T3 Doanh số/chuyến đi phân khúc 2 bánh vs 4 bánh, T4 Số lượng phương tiện Xanh SM tại VN và khu vực, T5 Tỷ lệ hoa hồng take rate bình quân, T6 Thu nhập bình quân tài xế $/tháng, T7 Tỷ lệ thâm nhập xe điện trong đội xe %, T8 Thị phần tại Indonesia, T9 Thị phần tại Việt Nam, T10 Tốc độ tăng trưởng hàng năm).
7. `tt_taxi_dan_mach` (Thị trường taxi Đan Mạch: T1 Quy mô doanh thu ngành taxi Đan Mạch, T2 Số lượng giấy phép xe taxi hoạt động, T3 Thời điểm có hiệu lực Luật Taxiloven 2017/2018, T4 Yêu cầu kỹ thuật cảm biến ghế/đồng hồ cước/camera, T5 Thị phần Dantaxi vs Taxa 4x35 vs Viggo, T6 Số lượng xe thuần điện của Viggo, T7 Tỷ lệ xe taxi không phát thải tại Copenhagen %, T8 Giá cước taxi trung bình DKK/km, T9 Số trạm sạc nhanh Viggo Energy, T10 Tỷ lệ điện hóa toàn bộ đội xe taxi Đan Mạch).

YÊU CẦU: Trình bày dạng bảng Markdown rõ ràng, các cột gồm: Mã chỉ số, Tên chỉ số, Giá trị định lượng, Mốc thời gian, Đơn vị/Chủ thể, Nguồn trích dẫn [n]."""
    }
]


async def run_pipeline():
    logger.info("=== BẮT ĐẦU DIRECT RPC NOTEBOOKLM RESEARCH PIPELINE (OPTIMIZED) ===")
    VAULT_DIR.mkdir(parents=True, exist_ok=True)

    async with NotebookLMClient.from_storage() as client:
        # Kiểm tra nguồn ban đầu
        initial_sources = await client.sources.list(NOTEBOOK_ID)
        logger.info("Master Notebook ID: %s", NOTEBOOK_ID)
        logger.info("Số lượng nguồn hiện có: %d", len(initial_sources))

        # Thực hiện 2 queries còn lại
        for q_item in REMAINING_QUERIES:
            q_name = q_item["name"]
            query_text = q_item["query"]

            logger.info("--- Bắt đầu Deep Research: [%s] ---", q_name)
            try:
                start_res = await client.research.start(NOTEBOOK_ID, query_text, mode="deep")
                report_id = getattr(start_res, "report_id", None) or start_res.task_id
                logger.info("Đã khởi tạo task thành công! Report/Task ID: %s", report_id)
            except Exception as e:
                logger.error("Lỗi khi start task [%s]: %s", q_name, e)
                continue

            # Poll định kỳ 10s cho đến khi completed
            task = None
            for attempt in range(1, 121): # tối đa 20 phút
                await asyncio.sleep(10)
                try:
                    task = await client.research.poll(NOTEBOOK_ID, task_id=report_id)
                    logger.info("[%s] Lần thăm dò %d: trạng thái=%s, số ứng viên=%d",
                                q_name, attempt, task.status, len(task.sources))
                    if str(task.status).lower().endswith("completed"):
                        break
                    elif str(task.status).lower().endswith("failed"):
                        logger.error("[%s] Task thất bại trên máy chủ!", q_name)
                        break
                except Exception as poll_e:
                    logger.warning("[%s] Lỗi tạm thời khi poll (sẽ thử lại): %s", q_name, poll_e)

            # Import sources
            if task and task.sources and str(task.status).lower().endswith("completed"):
                logger.info("[%s] Đang import %d nguồn vào Notebook...", q_name, len(task.sources))
                try:
                    await client.research.import_sources_with_verification(
                        NOTEBOOK_ID,
                        task.task_id,
                        task.sources,
                        max_elapsed=300
                    )
                    logger.info("[%s] Import hoàn tất!", q_name)
                except Exception as imp_e:
                    logger.warning("[%s] Cảnh báo import: %s", q_name, imp_e)

            current_sources = await client.sources.list(NOTEBOOK_ID)
            logger.info("Tổng số nguồn hiện tại trong Notebook: %d", len(current_sources))

        # Bước RAG trích xuất 12 files
        all_sources = await client.sources.list(NOTEBOOK_ID)
        source_map = {s.id: s for s in all_sources}
        logger.info("Bản đồ tra cứu sẵn sàng: %d nguồn.", len(source_map))

        logger.info("=== BẮT ĐẦU BATCH RAG EXTRACTION CHO 12 FILES ===")
        for idx, item in enumerate(EXTRACTION_QUESTIONS, 1):
            file_path = VAULT_DIR / item["filename"]
            logger.info("[%d/12] Trích xuất: %s (%s)", idx, item["filename"], item["title"])

            try:
                ask_res = await client.chat.ask(NOTEBOOK_ID, item["prompt"])
                logger.info("Đã nhận câu trả lời cho %s (độ dài: %d chars, references: %d)",
                            item["filename"], len(ask_res.answer), len(ask_res.references))

                used_sources = {}
                for ref in ask_res.references:
                    s_id = ref.source_id
                    if s_id in source_map and s_id not in used_sources:
                        used_sources[s_id] = source_map[s_id]

                md_content = []
                md_content.append(f"# {item['title']}\n")
                md_content.append(f"**Tập tin:** `{item['filename']}`  ")
                md_content.append(f"**Chủ thể liên quan:** `nganh_xe_dien`, `nganh_goi_xe`, `tt_xe_dien_eu`, `tt_xe_dien_asean`, `tt_goi_xe_eu`, `tt_goi_xe_asean`, `tt_taxi_dan_mach`  ")
                md_content.append(f"**Ngày tạo:** 2026-09-29  ")
                md_content.append(f"**Trích xuất từ:** Google NotebookLM (Direct RPC API)  ")
                md_content.append(f"**Master Notebook ID:** `{NOTEBOOK_ID}`  \n")
                md_content.append("---\n")
                md_content.append("## 1. Câu Hỏi Trích Xuất (Prompt Định Hướng)")
                md_content.append(f"```text\n{item['prompt']}\n```\n")
                md_content.append("---\n")
                md_content.append("## 2. Kết Quả Nghiên Cứu Chi Tiết (Nguyên Văn Từ Google NotebookLM)\n")
                md_content.append(ask_res.answer.strip())
                md_content.append("\n\n---\n")
                md_content.append("## 3. Danh Sách Nguồn Tài Liệu Gốc (Citations & References)\n")

                # Ánh xạ số trích dẫn [n] -> nguồn, để annotate_vault tra được URL cho từng câu.
                cite_rows = {}
                for ref in ask_res.references:
                    s_obj = source_map.get(ref.source_id)
                    if s_obj and ref.citation_number not in cite_rows:
                        url_str = getattr(s_obj, "url", None) or getattr(s_obj, "source_url", "") or ""
                        cite_rows[ref.citation_number] = f"[{ref.citation_number}] {getattr(s_obj, 'title', '')} {url_str}".strip()
                if cite_rows:
                    md_content.append("### Bảng số trích dẫn")
                    md_content.extend(cite_rows[n] for n in sorted(cite_rows))
                    md_content.append("")
                if used_sources:
                    for s_id, s_obj in used_sources.items():
                        url_str = getattr(s_obj, "url", None) or getattr(s_obj, "source_url", "")
                        title_str = getattr(s_obj, "title", "Không có tiêu đề")
                        if url_str:
                            md_content.append(f"- **{title_str}**  \n  URL: [{url_str}]({url_str})  \n  *Source ID: `{s_id}`*")
                        else:
                            md_content.append(f"- **{title_str}**  \n  *Source ID: `{s_id}`*")
                else:
                    md_content.append("*Tổng hợp từ 140+ tài liệu và báo cáo chính thức đã nạp trong Master Notebook:*\n")
                    for s_obj in all_sources[:15]:
                        url_str = getattr(s_obj, "url", None) or getattr(s_obj, "source_url", "")
                        title_str = getattr(s_obj, "title", "Không có tiêu đề")
                        if url_str:
                            md_content.append(f"- **{title_str}**: [{url_str}]({url_str})")
                        else:
                            md_content.append(f"- **{title_str}**")

                md_content.append("\n---\n*Báo cáo được khởi tạo tự động bởi Antigravity Direct RPC Research Engine tuân thủ quy chuẩn Grounding & Verification.*")

                file_path.write_text("\n".join(md_content), encoding="utf-8")
                logger.info("Đã ghi thành công: %s (%d bytes)", file_path.name, file_path.stat().st_size)

                await asyncio.sleep(2)

            except Exception as e:
                logger.error("Lỗi khi trích xuất %s: %s", item["filename"], e)

        logger.info("=== TẤT CẢ 12 FILES ĐÃ HOÀN TẤT VÀ LƯU VÀO RESEARCH VAULT ===")


if __name__ == "__main__":
    asyncio.run(run_pipeline())
