import os
import json
import subprocess
import time

env = os.environ.copy()
env["NOTEBOOKLM_HOME"] = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
bin_path = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
notebook_id = "d5c3d243-fab4-4376-8a53-418e43d11c36"
vault_dir = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/kbc-donald-trump-ban-khong-khi/research_vault"

os.makedirs(vault_dir, exist_ok=True)

queries = [
    (
        "001_dong_tien_that_va_co_cau_gop_von.md",
        "Bóc tách dòng tiền thật 1,5 tỷ USD và cơ cấu góp vốn KBC vs Trump",
        """Trong con số 1,5 tỷ USD (~40.000 tỷ VNĐ) tổng mức đầu tư được công bố của dự án Trump International Hưng Yên, cơ cấu nguồn vốn thực tế được phân bổ như thế nào giữa: Vốn tự có của KBC/HYG, vốn tín dụng ngân hàng, vốn huy động trái phiếu, và The Trump Organization có góp đồng vốn chủ sở hữu (Equity) nào không? Thỏa thuận chia sẻ lợi nhuận và nghĩa vụ gánh lỗ được quy định như thế nào? KBC đã rót bao nhiêu tiền vào công ty này đến nay? Hãy trích dẫn số liệu cụ thể từ tài liệu."""
    ),
    (
        "002_hop_dong_brand_licensing_va_phi_nhuong_quyen.md",
        "Cấu trúc hợp đồng Brand Licensing và các loại phí trả cho The Trump Organization",
        """Các điều khoản pháp lý cốt lõi trong thỏa thuận hợp tác giữa KBC/HYG và The Trump Organization là gì? Khoản phí bản quyền cấp phép ban đầu (Upfront License Fee) trả cho gia đình Trump là bao nhiêu (có phải 5 triệu USD không)? Tỷ lệ phần trăm phí nhượng quyền hàng năm (Royalty Fee) và phí quản lý sân golf/khách sạn (Management Fee) mà HYG phải thanh toán định kỳ cho The Trump Organization là bao nhiêu? Có điều khoản bảo đảm hiệu quả hay ràng buộc gì không? Trích dẫn nguồn tài liệu."""
    ),
    (
        "003_suc_khoe_tai_chinh_kbc_va_ap_luc_no_vay.md",
        "Kiểm toán sức khỏe tài chính KBC, nợ trái phiếu và áp lực dòng tiền Capex",
        """Dựa trên báo cáo tài chính kiểm toán giai đoạn 2023-2026 của KBC: Sức khỏe tài chính, dòng tiền từ hoạt động kinh doanh (CFO), cơ cấu nợ vay và áp lực nợ trái phiếu của KBC ra sao? Tồn kho tại dự án Tràng Cát (gần 17.000 tỷ) và việc lợi nhuận quý 2/2026 giảm 91% do thất thu KCN tác động thế nào đến khả năng tài trợ vốn cho dự án Hưng Yên? KBC huy động 6.000 tỷ trái phiếu để làm gì? Trích dẫn các chỉ số tài chính định lượng."""
    ),
    (
        "004_kinh_te_hoc_san_golf_54_ho_va_chi_phi_opex.md",
        "Phương trình kinh tế học sân golf 54 hố và bài toán hòa vốn Opex",
        """Mô hình kinh tế học và chi phí vận hành (Opex) của cụm sân golf 54 hố đẳng cấp quốc tế: Chi phí đầu tư xây dựng 54 hố là bao nhiêu? Chi phí vận hành hàng năm (bảo dưỡng cỏ, điện nước, nhân sự, kiểm định) là bao nhiêu? Cần bao nhiêu lượt chơi (rounds of golf)/năm và giá trung bình mỗi round bao nhiêu USD để hòa vốn chi phí Opex và có lãi thể thao thuần túy nếu không tính tiền bán đất? Trích dẫn số liệu thực tế."""
    ),
    (
        "005_boc_tach_thu_ngoai_te_va_ngoai_te_rong.md",
        "Bóc tách khái niệm 'Thu ngoại tệ' và dòng ngoại tệ ròng thực tế",
        """Bóc tách khái niệm 'Bán không khí thu ngoại tệ' dưới góc độ du lịch golf: Thống kê chi tiêu trung bình của một golfer quốc tế tại Việt Nam là bao nhiêu USD/ngày và mỗi chuyến đi? Sau khi khấu trừ chi phí nhập khẩu cỏ giống, máy móc bảo dưỡng, phân bón hóa chất và phí bản quyền chuyển về cho gia tộc Trump tại Mỹ, dòng ngoại tệ ròng (Net Foreign Exchange Retained) thực sự đọng lại trong nền kinh tế Việt Nam là bao nhiêu? Đối chiếu các dữ liệu ngành du lịch golf."""
    ),
    (
        "006_co_cau_doanh_thu_bds_sinh_thai_vs_san_golf.md",
        "Bất động sản sinh thái và biệt thự thương mại — Cỗ máy dòng tiền ẩn hoàn vốn",
        """Quy hoạch phân khu và cơ cấu doanh thu thực tế của dự án Trump International Hưng Yên (gần 990 ha): Tỷ lệ diện tích và doanh thu giữa sân golf 240 ha, công viên 99 ha, khu dân cư sinh thái và nhà ở thương mại là bao nhiêu? Việc dự án được cấp phép bán nhà cho người nước ngoài có ý nghĩa gì? Có phải doanh thu bán biệt thự bất động sản nghỉ dưỡng mới là cỗ máy hoàn vốn chính cho 1,5 tỷ USD, còn sân golf đóng vai trò thỏi nam châm nâng giá địa tô?"""
    ),
    (
        "007_hanh_lang_thoat_lu_song_hong_va_quyet_dinh_257.md",
        "Giải mã hành lang thoát lũ sông Hồng theo Quyết định 257/QĐ-TTg và Luật Đê điều",
        """Pháp lý bãi bồi sông Hồng: Vị trí bãi sông huyện Khoái Châu chịu sự điều chỉnh như thế nào bởi Quyết định số 257/QĐ-TTg của Thủ tướng Chính phủ và Luật Đê điều 2006? Tỷ lệ diện tích xây dựng kiên cố tối đa được phép trên bãi thoát lũ sông Hồng là bao nhiêu? Phương án bảo đảm an toàn thoát lũ khi xảy ra lũ cực đoan đã được các bộ ngành và Bộ NN&PTNT thẩm định ra sao?"""
    ),
    (
        "008_tuan_thu_nghi_dinh_35_ve_san_golf.md",
        "Tuân thủ Nghị định 35/2020/NĐ-CP về điều kiện kinh doanh sân golf",
        """Nghị định 35/2020/NĐ-CP của Chính phủ quy định về điều kiện kinh doanh sân golf: Các điều kiện cấm nghiêm ngặt (không sử dụng đất lúa, không được xây dựng nhà ở trong diện tích quy hoạch sân golf, mật độ xây dựng công trình phụ trợ ≤ 10%). Dự án Trump International Hưng Yên đã tách bạch pháp lý và ranh giới quy hoạch giữa sân golf 240 ha và khu đô thị sinh thái như thế nào để tuân thủ đúng luật?"""
    ),
    (
        "009_kiem_toan_den_bu_dat_va_sinh_ke_nong_dan.md",
        "Kiểm toán đền bù 558 ha đất, 3.000 hộ dân Khoái Châu và sinh kế thay thế",
        """Kiểm toán công tác thu hồi 558 ha đất bãi bồi và đền bù cho khoảng 3.000 hộ dân tại huyện Khoái Châu: Khung giá bồi thường đất nông nghiệp bãi bồi trong các đợt giao đất là bao nhiêu? Mức chênh lệch giữa giá đền bù đất nông nghiệp và giá bán biệt thự dự kiến ra sao? Các cam kết về tạo việc làm, chuyển đổi sinh kế cho người dân địa phương được thực hiện thế nào?"""
    ),
    (
        "010_case_study_thua_lo_trump_golf_scotland.md",
        "Giải phẫu case study thua lỗ Trump Turnberry và Aberdeen tại Scotland",
        """Giải phẫu hồ sơ thua lỗ kéo dài hơn 10 năm của hai sân golf mang thương hiệu Trump tại Scotland (Trump Turnberry và Trump International Golf Links Aberdeen) được nộp lên Companies House: Số lỗ lũy kế là bao nhiêu? Nguyên nhân cốt lõi dẫn đến thua lỗ là gì? Các xung đột môi trường và tranh chấp với chính quyền Scotland về cồn cát ven biển để lại bài học gì cho dự án Hưng Yên?"""
    ),
    (
        "011_rui_ro_oc_dao_du_lich_enclave_tourism.md",
        "Đánh giá rủi ro ốc đảo du lịch (Enclave Tourism) và rò rỉ dòng tiền ngoại tệ",
        """Mô hình 'Ốc đảo du lịch biệt lập' (Enclave Tourism) và hiện tượng rò rỉ dòng tiền du lịch (Tourism Leakage): Vì sao các khu nghỉ dưỡng khép kín thường không tạo ra giá trị lan tỏa cho cư dân và tiểu thương địa phương xung quanh? Các nghiên cứu quốc tế về Enclave Tourism và bài học áp dụng cho dự án tổ hợp sân golf biệt lập tại Hưng Yên?"""
    ),
    (
        "012_rui_ro_thuong_hieu_ca_nhan_va_dia_chinh_tri.md",
        "Rủi ro thương hiệu cá nhân Donald Trump và biến động chính trị quốc tế",
        """Đánh giá rủi ro thương hiệu cá nhân và biến động địa chính trị: Việc gắn toàn bộ dự án 1,5 tỷ USD vào thương hiệu Donald Trump mang lại lợi thế truyền thông gì, nhưng tiềm ẩn những rủi ro nào nếu tình hình chính trị Mỹ biến động hoặc có các phán quyết pháp lý quốc tế liên quan đến Trump Organization? Các điều khoản bảo vệ chủ đầu tư Việt Nam trong hợp đồng hợp tác?"""
    )
]

print(f"Bắt đầu Batch Extraction cho 12 queries từ Notebook {notebook_id}...", flush=True)

for idx, (filename, title, query_text) in enumerate(queries, 1):
    out_path = os.path.join(vault_dir, filename)
    print(f"\n[{idx}/12] Đang trích xuất: {title}...", flush=True)
    
    cmd = [
        bin_path,
        "ask",
        query_text,
        "-n", notebook_id,
        "--json",
        "--save-as-note",
        "-t", title,
        "--timeout", "300"
    ]
    
    start_time = time.time()
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    duration = time.time() - start_time
    
    if res.returncode == 0:
        try:
            data = json.loads(res.stdout)
            answer = data.get("answer", "")
            refs = data.get("references", [])
            
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("<!--\n")
                f.write("=== VAULT DOCUMENT PROVENANCE ===\n")
                f.write(f"- Master Notebook ID: {notebook_id}\n")
                f.write(f"- Query Index: EQ-{idx:02d}\n")
                f.write(f"- Topic: {title}\n")
                f.write(f"- Extracted Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=================================\n")
                f.write("-->\n\n")
                f.write(f"# {title.upper()}\n\n")
                f.write("## 1. NỘI DUNG PHÂN TÍCH & DỮ LIỆU ĐỊNH LƯỢNG\n\n")
                f.write(answer + "\n\n")
                f.write("## 2. NGUỒN DỮ LIỆU TRÍCH DẪN (CITATIONS)\n\n")
                if refs:
                    for r in refs:
                        r_idx = r.get("index", "")
                        r_title = r.get("title", "")
                        r_url = r.get("url", "")
                        f.write(f"- **[{r_idx}]** {r_title}")
                        if r_url:
                            f.write(f" — *URL: {r_url}*")
                        f.write("\n")
                else:
                    f.write("*Không có citations rời.*\n")
            
            print(f"-> THÀNH CÔNG: {filename} ({len(answer)} ký tự, {len(refs)} trích dẫn) trong {duration:.1f}s", flush=True)
        except Exception as e:
            print(f"-> LỖI PARSE JSON: {e}", flush=True)
    else:
        print(f"-> THẤT BẠI: {res.stderr}", flush=True)

print("\n=== HOÀN TẤT TOÀN BỘ 12 TRÍCH XUẤT RA RESEARCH VAULT! ===", flush=True)
