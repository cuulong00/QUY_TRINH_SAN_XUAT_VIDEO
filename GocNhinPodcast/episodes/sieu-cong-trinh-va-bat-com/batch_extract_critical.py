import subprocess
import os
import json

NOTEBOOK_ID = "6fa782f3-fc2c-4709-ac76-58c66932be51"
HOME_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.notebooklm_home"
CLI_PATH = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/.venv_notebooklm/bin/notebooklm"
VAULT_DIR = "/Users/pro16/Documents/VideoProject/GocNhinPodcast/episodes/sieu-cong-trinh-va-bat-com/research_vault"

os.makedirs(VAULT_DIR, exist_ok=True)

CRITICAL_QUERIES = [
    {
        "filename": "13_freight_vs_passenger_railway_dilemma.md",
        "title": "Nghịch lý Vận tải Hàng hóa vs Hành khách và Bẫy Phân phối Thu nhập Ngược",
        "prompt": """Phân tích phản biện chuyên sâu về cơ cấu vận tải và công bằng xã hội của Dự án Đường sắt tốc độ cao Bắc - Nam (67,34 tỷ USD):
1. Nghịch lý Chở khách vs Chở hàng: Tuyến 350km/h thiết kế chủ yếu chở khách (và hàng nhẹ khi cần thiết), trong khi đường sắt khổ 1.000mm cũ được nâng cấp để chở hàng. Đánh giá mức độ giải quyết chiếc thòng lọng chi phí logistics hàng hóa 16.8% GDP của Việt Nam (khi 77-80% hàng hóa, container, nông sản ĐBSCL đang dồn lên đường bộ). Liệu tuyến đường sắt 67 tỷ USD có giúp hạ giá thành rau củ, thực phẩm mâm cơm hay chiếc thòng lọng logistics hàng hóa vẫn còn nguyên vẹn?
2. Khả năng chi trả (Affordability) và Độ co giãn cầu theo giá (Price Elasticity): Giá vé dự kiến bằng 75% vé máy bay (~1.5 - 1.8 triệu VNĐ). So sánh với thu nhập bình quân của công nhân, người lao động phổ thông (6-8 triệu VNĐ/tháng). Tỷ lệ người dân thực tế có khả năng tiếp cận phương tiện này thường xuyên.
3. Bẫy Phân phối Thu nhập Ngược (Regressive Redistribution): Khi tuyến đường sắt bù lỗ vận hành/bảo trì (O&M) hơn 1 tỷ USD/năm (>25.400 tỷ đồng) từ ngân sách nhà nước (thu từ thuế toàn dân, bao gồm thuế VAT mà người nghèo mua gói mì, chai mắm cũng phải đóng), liệu có xảy ra nghịch lý: Người nghèo không đủ tiền đi tàu nhưng phải đóng thuế để trợ giá vé cho tầng lớp trung lưu và khá giả đi tàu cao tốc? Phân tích các giải pháp khắc phục bất công bằng xã hội này."""
    },
    {
        "filename": "14_cost_overruns_optimism_bias_flyvbjerg.md",
        "title": "Bẫy Đội vốn, Thiên kiến Lạc quan và Kinh tế học Siêu dự án (Bent Flyvbjerg)",
        "prompt": """Phân tích lý thuyết kinh tế học siêu dự án (Megaprojects) của Giáo sư Bent Flyvbjerg (Đại học Oxford) và bài học thực chứng về nguy cơ đội vốn của các đại dự án hạ tầng tại Việt Nam:
1. Lý thuyết 'Luật sắt của các siêu dự án' (The Iron Law of Megaprojects) của Bent Flyvbjerg: 'Over budget, over time, under benefits, over and over again'. Thống kê toàn cầu: 90% siêu dự án đội vốn (bình quân 50%); các dự án đường sắt trên thế giới vượt dự toán chi phí trung bình 44.7% và lưu lượng hành khách thực tế thấp hơn 51.4% so với dự báo tiền khả thi do Thiên kiến lạc quan (Optimism Bias) và Xuyên tạc chiến lược (Strategic Misrepresentation).
2. Kiểm toán thực chứng các tuyến đường sắt đô thị (Metro) tại Việt Nam: Cát Linh - Hà Đông (đội vốn từ 8.770 tỷ lên 18.000 tỷ, chậm 8 năm), Nhổn - Ga Hà Nội, Bến Thành - Suối Tiên (đội vốn gần 100%, chậm gần 10 năm). Bóc tách các nguyên nhân gốc rễ: Vướng giải phóng mặt bằng, thay đổi thiết kế cơ sở, năng lực đàm phán hợp đồng quốc tế FIDIC/EPC, trượt giá vật liệu và chi phí lãi vay trong thời gian xây dựng (IDC).
3. Kịch bản ứng phó cho Tuyến đường sắt tốc độ cao 67,34 tỷ USD: Nếu dự án bị đội vốn 30% - 50% (lên 90 - 100 tỷ USD) và kéo dài thêm 5 năm: Áp lực nợ công, tỷ lệ trả nợ trực tiếp của Chính phủ (nguy cơ vượt trần 25% tổng thu NSNN) và rủi ro chênh lệch tỷ giá ngoại tệ (Currency Mismatch) đối với phần linh kiện/tàu điện nhập khẩu sẽ tác động thế nào đến an toàn tài chính quốc gia? Điều kiện quản trị để phá vỡ 'Luật sắt của Bent Flyvbjerg'."""
    },
    {
        "filename": "15_social_infrastructure_crowding_out.md",
        "title": "Sự Chèn ép Ngân sách Hạ tầng Xã hội và Hệ lụy Ngoại ứng Môi trường Sinh thái",
        "prompt": """Phân tích sự đánh đổi chi phí cơ hội và ngoại ứng tiêu cực của chiến dịch đầu tư siêu công trình tại Việt Nam:
1. Sự chèn ép Hạ tầng xã hội (Crowding-out of Social Infrastructure): Khi bội chi ngân sách đẩy lên 4.2% - 5% GDP và dồn 1,71 triệu tỷ đồng vào hạ tầng cứng (bê tông, sắt thép), ngân sách dành cho hạ tầng mềm (y tế công lập, bệnh viện tuyến huyện, trường học công lập, bảo hiểm y tế, nhà ở xã hội cho công nhân, quỹ an sinh) chịu áp lực cắt giảm hoặc tăng chậm ra sao? Phân tích bài toán chi phí cơ hội đối với chất lượng cuộc sống thực tế của người dân bình thường.
2. Hệ lụy sinh thái hủy diệt từ cơn đói cát san lấp: Hoạt động khai thác hàng chục triệu m³ cát sông tại Đồng bằng sông Cửu Long làm hạ thấp lòng dẫn sông Tiền, sông Hậu từ 2-3 mét, kích hoạt hàng trăm điểm sạt lở bờ sông nghiêm trọng làm trôi nhà cửa, mất tư liệu sản xuất của nông dân, và kéo mặn xâm nhập sâu thêm 10-15km vào nội đồng.
3. Thách thức kỹ thuật và rủi ro môi trường của Cát biển rửa mặn: Đánh giá thực tế việc thí điểm sử dụng cát biển đắp nền đường; các rủi ro ăn mòn rỉ sét cốt thép bê tông, nguy cơ rò rỉ độ mặn làm ô nhiễm tầng nước ngầm và nhiễm mặn đất nông nghiệp lân cận nếu quy trình rửa mặn không đạt tiêu chuẩn kỹ thuật nghiêm ngặt."""
    }
]

def run_extraction():
    env = os.environ.copy()
    env["NOTEBOOKLM_HOME"] = HOME_DIR

    for i, q in enumerate(CRITICAL_QUERIES, 1):
        target_path = os.path.join(VAULT_DIR, q["filename"])
        print(f"\n==================================================")
        print(f"[{i}/{len(CRITICAL_QUERIES)}] Đang trích xuất: {q['title']}")
        print(f"File đích: {target_path}")
        print(f"==================================================")

        cmd = [
            CLI_PATH,
            "ask",
            q["prompt"],
            "-n", NOTEBOOK_ID
        ]

        try:
            res = subprocess.run(
                cmd,
                env=env,
                capture_output=True,
                text=True,
                check=True
            )
            output = res.stdout.strip()
            
            # Format markdown file
            content = f"""# {q['title']}

{output}
"""
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ Hoàn tất trích xuất: {q['filename']} ({len(content)} ký tự)")

        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi trích xuất {q['filename']}: {e.stderr}")

if __name__ == "__main__":
    run_extraction()
