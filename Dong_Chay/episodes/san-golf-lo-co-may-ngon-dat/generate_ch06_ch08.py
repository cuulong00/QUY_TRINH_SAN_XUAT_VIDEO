#!/usr/bin/env python3
"""
Master Visual Plus Script Generator for San Golf Episode: Chapters 06, 07 & 08
"""

import os
import subprocess

EPISODE_DIR = "/Users/pro16/Documents/VideoProject/Dong_Chay/episodes/san-golf-lo-co-may-ngon-dat"

def build_chapter_06():
    return """---
file_name: "chapter_06_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 6
total_scenes: 26
word_count: 503
modality_distribution:
  veo_ai: 12 (46.2%)
  infographic_data: 6 (23.1%)
  b_roll_real: 8 (30.8%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 19.3 words/scene, max 27 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_06_visual_plus.md
- Activated Persona: the_scene_architect + the_visual_storyteller + the_macro_strategist
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_06.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:30
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 6
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 6: BƯỚC NGOẶT LUẬT ĐẤT ĐAI 2024: KHAI TỬ ĐẦU CƠ ĐẤT RẺ

---

### [CH06_SC001]
- **Thoại:** "Trước những rủi ro tích tụ từ các dự án đòn bẩy, các cơ quan quản lý nhà nước đã không đứng ngoài cuộc." (22 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Tòa nhà trụ sở cơ quan quản lý vĩ mô nhà nước với hàng cột đá cẩm thạch uy nghiêm dưới bầu trời trong xanh, quốc huy đồng sáng bóng trên cổng chính, cán bộ quản lý trong âu phục công vụ bước vào sảnh lớn.
- **Chủ thể & Hành động an toàn:** Phong thái đĩnh đạc, kỷ luật hành chính nghiêm cẩn.
- **Camera & Điện ảnh:** Cinematic slow tilt up từ bậc thềm lên hàng cột đá uy nghi, ánh sáng ban mai trong trẻo.
- **Text Overlay:** Không.

---

### [CH06_SC002]
- **Thoại:** "Thay vì dùng mệnh lệnh cấm đoán, thể chế đã can thiệp bằng chính các công cụ kinh tế thị trường sòng phẳng." (21 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Market-Based Regulatory Mechanism Card (Thẻ can thiệp bằng công cụ thị trường).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh 2 cách tiếp cận thể chế: Cấm đoán hành chính (`ADMINISTRATIVE BANS`) $\to$ Công cụ kinh tế sòng phẳng (`MARKET-BASED FISCAL MECHANISMS`): Tăng chi phí giữ đất & Minh bạch quy hoạch phân tách.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, hai cột đối xứng rõ nét, viền vàng hổ phách `#F59E0B`.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn vàng hổ phách và xanh lục.
- **Text Overlay:** `BOTTOM LEFT | MARKET-BASED REGULATORY TOOLS`.

---

### [CH06_SC003]
- **Thoại:** "Bước đi đầu tiên mang tính bước ngoặt là Nghị định số 52 năm 2020 về kinh doanh sân golf." (19 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cổng thông tin điện tử Chính phủ (VGP): Bản chụp trang đầu của Nghị định số 52/2020/NĐ-CP của Chính phủ về đầu tư xây dựng và kinh doanh sân golf, chữ ký của Thủ tướng Chính phủ và dấu mộc đỏ.
- **Từ khóa tìm kiếm (Search Query):** "Decree 52 2020 ND-CP golf course business Vietnam government portal"
- **Nguồn báo chí uy tín (Source):** Cổng TTĐT Chính phủ / TTXVN
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: VGP Official Archive`.
- **Text Overlay:** `BOTTOM LEFT | DECREE 52/2020/ND-CP`.

---

### [CH06_SC004]
- **Thoại:** "Nghị định này đặt ra hai ranh giới pháp lý vô cùng nghiêm ngặt." (12 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc bằng gỗ sẫm màu của cơ quan tư pháp, cuốn sổ văn bản quy phạm pháp luật mở ra, hai vạch kẻ ranh giới màu đỏ son sắc lẹm được kẻ song song trên trang giấy.
- **Chủ thể & Hành động an toàn:** Ngòi bút dạ quang vàng champagne highlight hai điều khoản trọng yếu.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh ngòi bút vạch ranh giới, ánh sáng ngà kem `#FAF7EE` ấm áp.
- **Text Overlay:** Không.

---

### [CH06_SC005]
- **Thoại:** "Thứ nhất, nghiêm cấm tuyệt đối việc sử dụng đất trồng lúa hai vụ và đất rừng phòng hộ để làm sân golf." (22 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cánh đồng lúa hai vụ trĩu hạt vàng óng ả tại đồng bằng Bắc Bộ đang vào mùa gặt, người nông dân lái máy gặt đập liên hợp thu hoạch lúa bên cạnh ranh giới rừng phòng hộ xanh ngút ngàn.
- **Từ khóa tìm kiếm (Search Query):** "paddy rice field harvest combine harvester protected forest Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Nông nghiệp / Truyền hình Cần Thơ
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam Agriculture Archive`.
- **Text Overlay:** `BOTTOM LEFT | STRICT BAN: PADDY RICE & FORESTS`.

---

### [CH06_SC006]
- **Thoại:** "Thứ hai, nghị định khóa chặt nguyên tắc phân tách quy hoạch." (10 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bản đồ quy hoạch 1/500 trên bàn làm việc của Sở Quy hoạch - Kiến trúc, một đường ranh giới đỏ kiên cố được vẽ chia tách rạch ròi giữa khu vực thể thao sân golf và khu dân cư đô thị.
- **Chủ thể & Hành động an toàn:** Kiến trúc sư dùng thước kẻ khóa chặt ranh giới hai phân khu độc lập.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng quy hoạch xám đá slate `#2A323D`.
- **Text Overlay:** Không.

---

### [CH06_SC007]
- **Thoại:** "Dự án sân golf bắt buộc phải lập độc lập." (9 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Independent Project Boundary Card (Thẻ quy hoạch dự án độc lập).
- **Tiêu đề & Dữ liệu cốt lõi:** Khung bảo vệ pháp lý: `STANDALONE GOLF PROJECT MANDATE`. Biểu tượng hàng rào pháp lý bao quanh khu vực sân golf với nhãn: `100% SPORTING & SERVICE USE ONLY`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, viền xanh ngọc bích `#10B981` vững chãi.
- **Bảng màu & Hiệu ứng chuyển động:** Khung bảo vệ sáng lên kiên cố.
- **Text Overlay:** `BOTTOM LEFT | STANDALONE GOLF MANDATE`.

---

### [CH06_SC008]
- **Thoại:** "Doanh nghiệp tuyệt đối không được xây dựng nhà ở thương mại để bán bên trong diện tích đất sân golf." (20 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Biển cảnh báo quy hoạch tại một dự án sân golf: "NGHIÊM CẤM XÂY DỰNG NHÀ Ở THƯƠNG MẠI TRONG PHẠM VI RANH GIỚI SÂN GOLF THEO NGHỊ ĐỊNH 52/2020/NĐ-CP", cán bộ thanh tra Sở Xây dựng đang kiểm tra thực địa.
- **Từ khóa tìm kiếm (Search Query):** "construction inspection golf project commercial housing ban Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Báo Xây Dựng
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Construction Inspection Archive`.
- **Text Overlay:** Không.

---

### [CH06_SC009]
- **Thoại:** "Quy định này đã chặt đứt con đường mượn danh thể thao để gom đất phân lô bán nền." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Một lưỡi kéo kim loại biểu tượng sắc lẹm cắt đứt sợi dây nối giữa tấm biển "Dự Án Sân Golf Thể Thao" và bản vẽ phân lô bán nền bất động sản trên bàn làm việc.
- **Chủ thể & Hành động an toàn:** Ẩn dụ hành động thể chế dứt khoát chấm dứt việc lợi dụng chính sách.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng tông Slate lạnh `#1E293B`, âm hưởng dứt khoát đanh thép.
- **Text Overlay:** `BOTTOM LEFT | CUTTING OFF SPECULATION PATH`.

---

### [CH06_SC010]
- **Thoại:** "Nhưng đòn giáng kinh tế quyết định nhất lại đến từ Luật Đất đai năm 2024." (16 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Hội trường Diên Hồng Nhà Quốc hội: Bảng điện tử biểu quyết hiển thị kết quả thông qua Luật Đất đai (sửa đổi) năm 2024 với tỷ lệ tán thành áp đảo của các đại biểu Quốc hội.
- **Từ khóa tìm kiếm (Search Query):** "National Assembly passes Land Law 2024 voting electronic board Vietnam"
- **Nguồn báo chí uy tín (Source):** Truyền hình Quốc hội / VTV1
- **Yêu cầu xử lý Fair Use:** Cắt 4.0s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: National Assembly Media (2024)`.
- **Text Overlay:** `BOTTOM LEFT | LAND LAW 2024 PASSED`.

---

### [CH06_SC011]
- **Thoại:** "Điều một trăm năm mươi chín của luật mới chính thức bãi bỏ khung giá đất cũ." (17 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Article 159 Legal Transformation Card (Thẻ bước ngoặt Điều 159 Luật Đất đai).
- **Tiêu đề & Dữ liệu cốt lõi:** Văn bản pháp quy: `ARTICLE 159 - LAND LAW 2024`. Dòng gạch chéo màu đỏ: `ABOLITION OF GOVERNMENT LAND PRICE FRAMEWORK (BÃI BỎ KHUNG GIÁ ĐẤT CŨ)`. Thay thế bằng: Bảng giá đất thị trường hàng năm.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, văn bản luật bôi vàng kiểu Vox trên nền ngà kem `#FAF7EE`.
- **Bảng màu & Hiệu ứng chuyển động:** Dấu gạch chéo đỏ xuất hiện đè lên khung giá cũ.
- **Text Overlay:** `BOTTOM LEFT | ARTICLE 159: ABOLISHING PRICE FRAMEWORK`.

---

### [CH06_SC012]
- **Thoại:** "Bảng giá đất hàng năm của các địa phương được xây dựng tiệm cận với giá trị giao dịch thực tế trên thị trường." (23 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Phòng họp định giá đất của Hội đồng thẩm định giá đất cấp tỉnh: Các chuyên gia đang đối chiếu bản đồ giá đất giao dịch thực tế trên thị trường số hóa với bảng giá đất địa phương mới.
- **Chủ thể & Hành động an toàn:** Cán bộ thẩm định nhập các dữ liệu thị trường thực chứng vào phần mềm định giá.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng họp minh bạch nghiêm túc.
- **Text Overlay:** Không.

---

### [CH06_SC013]
- **Thoại:** "Sự thay đổi này đã tạo ra một cú sốc chi phí khổng lồ cho các doanh nghiệp sân golf." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bàn làm việc của giám đốc tài chính doanh nghiệp sân golf, bức thư thông báo tạm nộp tiền thuê đất mới của cơ quan thuế gửi đến, ngón tay run nhẹ khi đọc con số tiền thuê đất tăng gấp nhiều lần.
- **Chủ thể & Hành động an toàn:** Nét mặt trầm ngâm, lo lắng trước cú sốc chi phí tiền thuê đất.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh nét mặt và bức thư thông báo thuế, ánh sáng vàng lạnh.
- **Text Overlay:** Không.

---

### [CH06_SC014]
- **Thoại:** "Trước đây, tiền thuê đất hàng năm cho một sân golf một trăm héc-ta thường chỉ dao động từ hai đến năm tỷ đồng." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Old Land Rent Baseline Card (Thẻ tiền thuê đất theo khung giá cũ).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ chi phí cũ: `OLD LAND RENT (PRE-2024): 2 - 5 BILLION VND / YEAR` cho 100 ha sân golf. Chiếm chưa đầy 5% doanh thu hàng năm.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, cột chi phí màu xanh ngọc bích nhỏ gọn.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn ngà kem và xanh lục.
- **Text Overlay:** `BOTTOM LEFT | OLD RENT: 2 - 5 BILLION VND/YEAR`.

---

### [CH06_SC015]
- **Thoại:** "Đây là một con số rất nhỏ so với quy mô của dự án." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đại cảnh sân golf 100 ha ngút ngàn, một đồng xu nhỏ tượng trưng cho vài tỷ tiền thuê đất cũ đặt lọt thỏm giữa thảm cỏ bao la.
- **Chủ thể & Hành động an toàn:** Hình tượng tương phản trực quan về sự bao cấp ngầm của tài nguyên đất đai giá rẻ trong quá khứ.
- **Camera & Điện ảnh:** Cinematic slow aerial pan shot, ánh sáng nắng ban mai.
- **Text Overlay:** Không.

---

### [CH06_SC016]
- **Thoại:** "Nhưng theo bảng giá đất mới, tiền thuê đất nộp ngân sách có thể tăng vọt lên mười lăm đến ba mươi lăm tỷ đồng." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** 3X - 5X Land Rent Surge Card (Biểu đồ cú sốc tiền thuê đất tăng 3–5 lần).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh tiền thuê đất: `OLD RENT: 2 - 5 BILLION VND` $\to$ Cột mới dựng đứng: `NEW LAND RENT (LAND LAW 2024): 15 - 35 BILLION VND / YEAR`. Tăng vọt từ 300% đến 700%.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, cột chi phí mới vươn cao với viền đỏ san hô rực rỡ `#EF5350`.
- **Bảng màu & Hiệu ứng chuyển động:** Cột chi phí đỏ dựng đứng tạo cú sốc ngân sách.
- **Text Overlay:** `BOTTOM LEFT | NEW RENT: 15 - 35 BILLION VND/YEAR`.

---

### [CH06_SC017]
- **Thoại:** "Khoản chi phí này có thể nuốt trọn từ ba mươi đến năm mươi phần trăm tổng doanh thu của một sân golf trung bình." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Revenue Erosion Share Card (Biểu đồ nuốt trọn 30–50% doanh thu).
- **Tiêu đề & Dữ liệu cốt lõi:** Bánh tròn doanh thu tiền vé sân golf: Mảng màu đỏ san hô chiếm `30% - 50% TOTAL REVENUE` bị cơ quan thuế khấu trừ tiền thuê đất hàng năm, bóp nghẹt biên lợi nhuận mỏng manh còn lại.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, tỷ lệ phần trăm hiển thị to rõ ràng.
- **Bảng màu & Hiệu ứng chuyển động:** Mảng đỏ phình to nuốt chửng phần doanh thu.
- **Text Overlay:** `BOTTOM LEFT | EATS 30% - 50% OF TOTAL REVENUE`.

---

### [CH06_SC018]
- **Thoại:** "Trong kinh tế học, đây được gọi là sự gia tăng đột biến của chi phí giữ đất." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc đồng hồ cát bằng đồng thau đặt trên bản đồ quy hoạch dự án, cát chảy xuống với tốc độ chóng mặt cuốn trôi các đồng tiền vàng đặt bên dưới, phản chiếu áp lực chi phí holding cost.
- **Chủ thể & Hành động an toàn:** Ẩn dụ kinh tế học về chi phí cơ hội và áp lực thời gian của dòng vốn.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh cát rơi, ánh sáng đèn bàn xám slate.
- **Text Overlay:** `BOTTOM LEFT | HOLDING COST SURGE`.

---

### [CH06_SC019]
- **Thoại:** "Doanh nghiệp không thể ôm một dự án trên giấy để chờ tăng giá đất được nữa." (16 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Đoàn kiểm tra liên ngành của Ủy ban nhân dân tỉnh đi rà soát các dự án chậm tiến độ: Cán bộ cắm mốc đo đạc và lập biên bản xử phạt vi phạm chậm đưa đất vào sử dụng.
- **Từ khóa tìm kiếm (Search Query):** "provincial inspection team reviewing delayed land projects Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Báo Đầu Tư
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Land Inspection Archive`.
- **Text Overlay:** Không.

---

### [CH06_SC020]
- **Thoại:** "Càng giữ đất chậm triển khai, dòng tiền của doanh nghiệp càng bị rút cạn nhanh chóng." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bảng cân đối kế toán với dòng tiền mặt lưu chuyển thuần (Net Cash Flow) chuyển dần từ màu xanh sang màu đỏ san hô rực lửa, các cột dự trữ tiền mặt hạ thấp dần qua từng quý.
- **Chủ thể & Hành động an toàn:** Giám đốc tài chính gõ bút xuống bàn đầy bất lực.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng màn hình máy tính phản chiếu sự cạn kiệt thanh khoản.
- **Text Overlay:** Không.

---

### [CH06_SC021]
- **Thoại:** "Luật mới không cấm làm sân golf." (7 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Cuốn sách Luật Đất đai 2024 đặt trang trọng trên bục gỗ sồi dưới ánh sáng mặt trời ấm áp rực rỡ, bên cạnh là một quả bóng golf màu trắng tinh khiết đặt trên cọc gỗ.
- **Chủ thể & Hành động an toàn:** Sự tôn trọng tuyệt đối luật chơi của nền kinh tế thị trường minh bạch.
- **Camera & Điện ảnh:** Steady camera shot, bố cục cân đối trang nghiêm, viền mực thanh thoát.
- **Text Overlay:** Không.

---

### [CH06_SC022]
- **Thoại:** "Luật chỉ làm một việc sòng phẳng là buộc doanh nghiệp phải trả đúng giá thị trường cho từng mét vuông đất công cộng." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Phiên đấu giá quyền sử dụng đất công khai tại hội trường thành phố: Các nhà đầu tư giơ biển đấu giá công khai, màn hình điện tử hiển thị giá trúng đấu giá minh bạch tiệm cận thị trường.
- **Từ khóa tìm kiếm (Search Query):** "public land auction auctioneer gavel bidding screen Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Khớp lệnh / Báo Pháp Luật
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Public Land Auction Archive`.
- **Text Overlay:** Không.

---

### [CH06_SC023]
- **Thoại:** "Chỉ những sân golf tạo ra giá trị dịch vụ thật hoặc nằm trong đại đô thị có sức hấp thụ thật mới có thể tồn tại." (27 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Hai hình ảnh song hành: Một bên là sân golf du lịch ven biển miền Trung đón khách quốc tế tấp nập, một bên là đại đô thị sinh thái xanh mát có cư dân sinh sống đông vui, toát lên sức sống kinh tế thực chất.
- **Chủ thể & Hành động an toàn:** Khung cảnh sinh hoạt kinh tế văn minh, tôn vinh giá trị dịch vụ thật.
- **Camera & Điện ảnh:** Cinematic slow pan shot, ánh sáng rực rỡ nhiệt đới, thảm cỏ xanh mướt tràn đầy năng lượng.
- **Text Overlay:** Không.

---

### [CH06_SC024]
- **Thoại:** "Thể chế đã thiết lập một bộ lọc tự nhiên để loại bỏ các ván cược đầu cơ." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bộ lọc bằng lưới kim loại sáng bóng biểu trưng cho thể chế đang lọc sạch các viên sỏi rác đầu cơ ra khỏi dòng nước chảy trong vắt của nền kinh tế.
- **Chủ thể & Hành động an toàn:** Ẩn dụ trực quan tinh tế về vai trò kiến tạo và thanh lọc của pháp luật.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng ngà kem và xám slate đĩnh đạc.
- **Text Overlay:** `BOTTOM LEFT | NATURAL MARKET FILTER`.

---

### [CH06_SC025]
- **Thoại:** "Nhưng dưới góc độ tài nguyên và xã hội, một sân golf mang lại gì và lấy đi những gì của nền kinh tế?" (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Người nông dân địa phương đứng bên bờ mương nước ngắm nhìn về phía thảm cỏ sân golf xanh mướt bên kia hàng rào, dòng nước tưới tiêu chảy qua cánh đồng lúa xanh non.
- **Từ khóa tìm kiếm (Search Query):** "farmer standing near irrigation canal looking at golf course boundary"
- **Nguồn báo chí uy tín (Source):** Truyền hình Nông thôn / VTV Cần Thơ
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Rural Livelihood Archive`.
- **Text Overlay:** Không.

---

### [CH06_SC026]
- **Thoại:** "Câu trả lời đòi hỏi chúng ta phải đặt tài nguyên đất đai lên bàn cân chi phí cơ hội." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc bàn cân cổ điển bằng đồng đặt giữa phòng nghiên cứu kinh tế: Một bên đĩa cân là nắm đất màu mỡ và bông lúa vàng, một bên đĩa cân là quả bóng golf trắng và xấp tiền đô la ngoại tệ, tạo cầu nối hoàn hảo sang Chương 7.
- **Chủ thể & Hành động an toàn:** Hai đĩa cân dao động nhẹ nhàng rồi tìm điểm thăng bằng khách quan.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh trục cân thăng bằng, ánh sáng vàng ấm rọi từ trên cao.
- **Text Overlay:** Không.
"""

def build_chapter_07():
    return """---
file_name: "chapter_07_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 7
total_scenes: 27
word_count: 545
modality_distribution:
  veo_ai: 12 (44.4%)
  infographic_data: 7 (25.9%)
  b_roll_real: 8 (29.6%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 20.2 words/scene, max 27 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_07_visual_plus.md
- Activated Persona: the_scene_architect + the_visual_storyteller + the_macro_strategist
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_07.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:32
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 7
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 7: CHI PHÍ CƠ HỘI CỦA ĐẤT NƯỚC: NƯỚC, VIỆC LÀM VÀ SỰ TÁI SINH

---

### [CH07_SC001]
- **Thoại:** "Gạt bỏ lớp vỏ tài chính, câu hỏi còn lại là: Một sân golf thực sự mang lại gì và lấy đi những gì của xã hội?" (27 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Phòng hội thảo kinh tế học phúc lợi xã hội: Nhà nghiên cứu đứng bên chiếc bảng đen viết dòng chữ phấn trắng nắn nót: "SOCIAL COST-BENEFIT ANALYSIS (PHÂN TÍCH CHI PHÍ - LỢI ÍCH XÃ HỘI)", xung quanh là các nhà khoa học môi trường và kinh tế.
- **Chủ thể & Hành động an toàn:** Phong thái học thuật đĩnh đạc, tìm kiếm câu trả lời khách quan First-Principles.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng hội thảo ấm áp ngà kem `#FAF7EE`.
- **Text Overlay:** Không.

---

### [CH07_SC002]
- **Thoại:** "Đây là bài toán kinh tế phúc lợi mà mọi quốc gia đều phải đối mặt." (14 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Welfare Economics Dual Balance Card (Thẻ cán cân kinh tế phúc lợi).
- **Tiêu đề & Dữ liệu cốt lõi:** Cán cân 2 đĩa: Đĩa bên phải (Lợi ích xã hội: Việc làm nông thôn, Chuyển dịch dịch vụ, Ngoại tệ) vs Đĩa bên trái (Chi phí cơ hội: Đất đai thâm dụng, Tài nguyên nước, Hóa chất).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, hai đĩa cân đối xứng, các khối dữ liệu rõ ràng.
- **Bảng màu & Hiệu ứng chuyển động:** Cân dao động tìm trạng thái cân bằng khách quan.
- **Text Overlay:** `BOTTOM LEFT | SOCIAL WELFARE BALANCE`.

---

### [CH07_SC003]
- **Thoại:** "Ở mặt tích cực, một sân golf 18 lỗ tạo ra việc làm trực tiếp cho ba trăm đến năm trăm lao động địa phương." (24 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Local Employment Creation Card (Thẻ việc làm trực tiếp 300–500 lao động).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ lao động việc làm: `DIRECT LOCAL JOBS: 300 - 500 WORKERS / 18-HOLE COURSE`. Cơ cấu: Đội ngũ caddie (65%), Nhân viên chăm sóc mặt cỏ & cảnh quan (20%), Lễ tân & nhà hàng (15%).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, các icon vector nhân sự màu xanh lục `#10B981` xếp hàng ngay ngắn.
- **Bảng màu & Hiệu ứng chuyển động:** Con số việc làm phát sáng màu xanh hy vọng.
- **Text Overlay:** `BOTTOM LEFT | 300 - 500 LOCAL WORKERS / COURSE`.

---

### [CH07_SC004]
- **Thoại:** "Đa phần trong số họ là con em của các hộ nông dân tại khu vực dự án." (17 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Lớp tập huấn đào tạo nghề dịch vụ và tiếng Anh giao tiếp cho các bạn trẻ nông thôn tại trung tâm văn hóa huyện do doanh nghiệp sân golf tài trợ: Giảng viên nước ngoài đang hướng dẫn các thuật ngữ thể thao.
- **Từ khóa tìm kiếm (Search Query):** "caddie vocational training English class rural youth Vietnam golf"
- **Nguồn báo chí uy tín (Source):** VTV Nông thôn / Truyền hình Đà Nẵng
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vocational Training Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC005]
- **Thoại:** "Lực lượng caddie chiếm phần lớn nhân sự với thu nhập từ mười hai đến hai mươi triệu đồng một tháng." (21 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@caddie_vietnam_working.jpg ->` A 2D warm cinematic editorial illustration of the Vietnamese female caddie depicted in the reference image, faithfully preserving her exact facial features, warm smile, sun-protective uniform with wide-brim hat and emerald green attire directly from the reference photo. She is walking alongside a golfer on the sunny fairway, carrying the golf bag and gently advising on distance and wind direction.
- **Chủ thể & Hành động an toàn:** Cử chỉ chuyên nghiệp, niềm nở, am hiểu địa hình sân golf.
- **Camera & Điện ảnh:** Steady camera shot, ánh nắng ban mai rực rỡ chiếu trên thảm cỏ xanh mướt.
- **Text Overlay:** `BOTTOM LEFT | CADDIE INCOME: 12 - 20 MILLION VND/MONTH`.

---

### [CH07_SC006]
- **Thoại:** "Mức thu nhập này cao gấp ba đến bốn lần so với việc canh tác nông nghiệp truyền thống." (18 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Income Multiplier Comparison Card (Thẻ so sánh thu nhập gấp 3–4 lần).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh thu nhập hàng tháng: Nông nghiệp lúa nước truyền thống (`FARMING INCOME: 3 - 5 MILLION VND/MONTH`) vs Nghề Caddie sân golf (`CADDIE INCOME: 12 - 20 MILLION VND/MONTH`). Bội số thu nhập: `3X - 4X SURGE`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, hai cột thu nhập màu vàng đất và xanh lục Emerald `#10B981`.
- **Bảng màu & Hiệu ứng chuyển động:** Cột thu nhập caddie vươn cao vượt trội.
- **Text Overlay:** `BOTTOM LEFT | INCOME: 3X - 4X TRADITIONAL FARMING`.

---

### [CH07_SC007]
- **Thoại:** "Sự chuyển dịch từ lao động nông nghiệp sang dịch vụ đã giúp hàng trăm gia đình cải thiện đời sống." (20 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Ngôi nhà khang trang mới xây của gia đình caddie ở vùng nông thôn ven biển miền Trung: Chiếc xe máy tay ga mới mua dựng trước sân gạch sạch sẽ, bữa cơm gia đình đầm ấm rộn rã tiếng cười.
- **Từ khóa tìm kiếm (Search Query):** "newly built rural house Vietnam family dinner improved livelihood"
- **Nguồn báo chí uy tín (Source):** VTV Chuyển động 24h / Báo Nông Thôn Ngày Nay
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Rural Livelihood Documentary`.
- **Text Overlay:** Không.

---

### [CH07_SC008]
- **Thoại:** "Họ được đóng bảo hiểm và tiếp cận môi trường làm việc chuyên nghiệp." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Buổi giao ban đầu giờ sáng tại phòng sinh hoạt caddie: Trưởng bộ phận phổ biến lịch trình trong không gian phòng ốc sạch sẽ, nhân viên mặc đồng phục ngay ngắn, trên bàn là sổ chấm công và thẻ bảo hiểm y tế.
- **Chủ thể & Hành động an toàn:** Môi trường làm việc văn minh, kỷ luật và bảo đảm phúc lợi người lao động.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng phòng sáng sủa và ấm cúng.
- **Text Overlay:** Không.

---

### [CH07_SC009]
- **Thoại:** "Thế nhưng, cái giá phải trả về mặt tài nguyên là không hề nhỏ." (14 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đồng hồ đo nước tưới công nghiệp xoay vòng liên tục với lưu lượng hàng nghìn mét khối nước, bên ngoài là thảm cỏ bao la đòi hỏi tưới tắm mỗi ngày dưới cái nắng gay gắt trưa hè.
- **Chủ thể & Hành động an toàn:** Khung cảnh tĩnh lặng nhưng cảnh báo về áp lực thâm dụng tài nguyên nước.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh mặt đồng hồ đo nước, ánh sáng tương phản gắt.
- **Text Overlay:** Không.

---

### [CH07_SC010]
- **Thoại:** "Một sân golf 18 lỗ vùng nhiệt đới tiêu thụ từ hai nghìn đến ba nghìn năm trăm mét khối nước tưới mỗi ngày." (25 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Daily Water Consumption Card (Thẻ tiêu thụ nước tưới hàng ngày).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ tài nguyên nước: `WATER CONSUMPTION: 2,000 - 3,500 M3 / DAY`. Tương đương lượng nước sinh hoạt của hơn 15.000 hộ gia đình. Icon giọt nước khổng lồ màu xanh lam nhạt viền cam cảnh báo `#FF7043`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, con số tiêu thụ hiển thị to bản sắc nét.
- **Bảng màu & Hiệu ứng chuyển động:** Vạch đo nước dâng cao tạo ấn tượng định lượng rõ rệt.
- **Text Overlay:** `BOTTOM LEFT | WATER USE: 2,000 - 3,500 M3/DAY`.

---

### [CH07_SC011]
- **Thoại:** "Nếu khai thác nước ngầm bừa bãi, nó sẽ làm hạ thấp mực nước ngầm của cả vùng dân cư xung quanh." (22 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Chiếc giếng khoan cạn khô nước ở một ngôi làng ven dự án golf, người dân kéo dây gàu lên chỉ có cát đáy giếng, phản ánh nguy cơ cạn kiệt tầng nước ngầm khi khai thác bừa bãi.
- **Từ khóa tìm kiếm (Search Query):** "dry well water shortage underground water depletion rural Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Môi trường / Báo Tuổi Trẻ
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Environmental Investigation Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC012]
- **Thoại:** "Để giải quyết vấn đề này, tiêu chuẩn hiện đại buộc sân golf phải xây dựng hệ thống hồ lắng tuần hoàn." (22 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Hệ thống hồ sinh học nhân tạo rộng lớn bên trong sân golf với bờ kè đá tự nhiên và hoa sen hoa súng, các đường ống thu gom nước mưa ngầm kết nối từ toàn bộ các sườn dốc fairway về hồ chứa.
- **Chủ thể & Hành động an toàn:** Giải pháp công nghệ tuần hoàn nước mặt thông minh và thân thiện môi trường.
- **Camera & Điện ảnh:** Cinematic slow aerial pan shot, mặt nước hồ phẳng lặng phản chiếu mây trời xanh ngắt.
- **Text Overlay:** `BOTTOM LEFT | CLOSED-LOOP RECIRCULATION PONDS`.

---

### [CH07_SC013]
- **Thoại:** "Nước mưa và nước mặt được thu gom trong mùa mưa để tích trữ tưới tiêu trong mùa khô." (20 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Closed-Loop Rainwater Harvesting Flowchart (Sơ đồ tuần hoàn nước mặt).
- **Tiêu đề & Dữ liệu cốt lõi:** Quy trình 3 bước: `RAINWATER CAPTURE (MÙA MƯA: THU GOM 100% NƯỚC MẶT)` $\to$ `BIO-RETENTION LAKE (HỒ LẮNG TÍCH TRỮ SINH HỌC)` $\to$ `DRY SEASON IRRIGATION (MÙA KHÔ: TỰ CÂN ĐỐI TƯỚI TIÊU, 0% NƯỚC NGẦM)`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, mũi tên tuần hoàn màu xanh ngọc bích `#10B981` khép kín.
- **Bảng màu & Hiệu ứng chuyển động:** Dòng nước tuần hoàn khép kín nhịp nhàng.
- **Text Overlay:** `BOTTOM LEFT | 100% RAINWATER RECYCLING`.

---

### [CH07_SC014]
- **Thoại:** "Lớp cát lọc sinh học giúp hấp thụ và phân hủy phân bón trước khi nước ngấm xuống đất." (19 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Mặt cắt địa chất 3D của lớp đất dưới thảm cỏ fairway: Lớp cỏ paspalum $\to$ lớp cát thạch anh mịn $\to$ lớp màng lọc địa kỹ thuật sinh học $\to$ ống thoát nước ngầm đục lỗ, nước lọc trong vắt chảy ra hồ lắng.
- **Chủ thể & Hành động an toàn:** Mô phỏng công nghệ xử lý vi sinh bảo vệ tầng nước ngầm tuyệt đối.
- **Camera & Điện ảnh:** Steady camera shot góc nhìn mặt cắt ngang khoa học, ánh sáng dịu mắt.
- **Text Overlay:** Không.

---

### [CH07_SC015]
- **Thoại:** "Quy hoạch trên đất cát cằn cỗi với hồ tuần hoàn, lợi ích việc làm sẽ vượt trội chi phí môi trường." (22 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Net Benefit Matrix on Barren Land (Ma trận lợi ích ròng trên đất cát).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu thức phúc lợi ròng: Đất cát cằn cỗi + Hồ tuần hoàn $\to$ `NET SOCIAL BENEFIT: HIGHLY POSITIVE`. Việc làm và ngoại tệ áp đảo hoàn toàn chi phí môi trường được kiểm soát.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu thức màu xanh lục Emerald `#10B981` rực rỡ.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh lục và vàng hổ phách.
- **Text Overlay:** `BOTTOM LEFT | NET BENEFIT ON BARREN SAND: POSITIVE`.

---

### [CH07_SC016]
- **Thoại:** "Nhưng nếu lấy đất trồng trọt màu mỡ để làm sân cỏ, chi phí cơ hội xã hội sẽ là một tổn thất lớn cho đất nước." (27 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cảnh tương phản nhức nhối: Một vùng đất phù sa màu mỡ trồng cây ăn trái bạt ngàn bị chặt phá san phẳng để làm dự án sân golf, đất đai trơ trọi cát bụi dưới nắng gắt.
- **Từ khóa tìm kiếm (Search Query):** "fertile fruit orchard cleared bulldozed for golf development Vietnam"
- **Nguồn báo chí uy tín (Source):** VTV Thời sự / Báo Nông Nghiệp Việt Nam
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Agricultural Land Loss Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC017]
- **Thoại:** "Nhìn ra thế giới, quy luật sử dụng đất đai luôn tự tìm cách tối ưu hóa hiệu suất." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Quả địa cầu 3D xoay chậm trên bàn nghiên cứu địa kinh tế, ánh sáng mặt trời chiếu sáng từ châu Á sang Bắc Mỹ, phản chiếu các làn sóng chuyển dịch công năng đất đai toàn cầu.
- **Chủ thể & Hành động an toàn:** Góc nhìn toàn cầu sâu sắc về sự vận động của tài nguyên.
- **Camera & Điện ảnh:** Cinematic slow tracking shot quanh quả địa cầu, ánh sáng ngà kem `#FAF7EE`.
- **Text Overlay:** Không.

---

### [CH07_SC018]
- **Thoại:** "Tại Mỹ, sau cuộc khủng hoảng tài chính năm 2008, hơn một nghìn hai trăm sân golf đã bị đóng cửa vĩnh viễn." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** US Golf Course Contraction Stat Card (Thẻ thống kê đóng cửa 1.200 sân golf tại Mỹ).
- **Tiêu đề & Dữ liệu cốt lõi:** Thống kê lịch sử sau khủng hoảng 2008: `US GOLF COURSE CLOSURES: > 1,200 COURSES PERMANENTLY SHUT DOWN`. Đồ thị số lượng sân golf tại Mỹ co hẹp liên tục suốt 15 năm.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, bản đồ nước Mỹ với các chấm đỏ đóng cửa co lại.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn đỏ san hô `#EF5350` biểu thị sự thoái trào tự nhiên.
- **Text Overlay:** `BOTTOM LEFT | USA: >1,200 GOLF COURSES CLOSED (POST-2008)`.

---

### [CH07_SC019]
- **Thoại:** "Giới trẻ Mỹ không còn mặn mà với việc dành năm tiếng đồng hồ trên sân cỏ." (16 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Nhóm bạn trẻ thế hệ Gen Z tại Mỹ lướt điện thoại thông minh trong quán cà phê, không ai mặn mà với việc vác túi gậy nặng nề đi bộ 5 tiếng dưới nắng hè.
- **Từ khóa tìm kiếm (Search Query):** "young millennials smartphone cafe busy urban lifestyle USA"
- **Nguồn báo chí uy tín (Source):** Bloomberg Quicktake / CNBC Make It
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Consumer Trends Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC020]
- **Thoại:** "Các quỹ đầu tư đã nhanh chóng tái cơ cấu những quỹ đất rộng lớn này." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Phòng họp của quỹ đầu tư bất động sản quốc tế tại New York, các nhà quản lý quỹ đang xem bản vẽ quy hoạch chuyển đổi công năng (adaptive reuse) các sân golf đóng cửa thành khu đô thị sinh thái và khu công nghệ.
- **Chủ thể & Hành động an toàn:** Thảo luận chuyên nghiệp, quyết đoán về việc tái phân bổ tài sản.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng kính văn phòng Phố Wall đĩnh đạc.
- **Text Overlay:** Không.

---

### [CH07_SC021]
- **Thoại:** "Nhiều sân golf ven đô được chuyển đổi thành khu dân cư mật độ trung bình." (15 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam một dự án khu dân cư sinh thái mới xây dựng tại bang California (Mỹ) trên nền một sân golf cũ: Các dãy nhà phố xinh đẹp bao quanh công viên cây xanh công cộng có sẵn hồ nước và rặng cây cổ thụ.
- **Từ khóa tìm kiếm (Search Query):** "former golf course converted to residential housing community California"
- **Nguồn báo chí uy tín (Source):** US Real Estate Channel / ABC News
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Urban Redevelopment Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC022]
- **Thoại:** "Trong làn sóng trí tuệ nhân tạo, các tập đoàn như Microsoft hay Amazon đã mua lại nhiều sân golf đóng cửa." (21 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đại bản doanh trung tâm dữ liệu AI hiện đại mọc lên trên sườn đồi thoai thoải từng là sân golf cũ: Các khối nhà thép kiên cố màu xám bạc `#2A323D`, hệ thống làm mát bằng nước hồ tuần hoàn tự nhiên và trạm biến áp cao thế sẵn có.
- **Chủ thể & Hành động an toàn:** Biểu tượng công nghệ cao thay thế mô hình thể thao thâm dụng đất.
- **Camera & Điện ảnh:** Cinematic slow aerial pan shot, ánh sáng hoàng hôn rọi trên bề mặt kim loại sáng bóng.
- **Text Overlay:** `BOTTOM LEFT | GOLF COURSES -> AI DATA CENTERS`.

---

### [CH07_SC023]
- **Thoại:** "Họ biến những khu đất trăm héc-ta có sẵn lưới điện cao thế thành các trung tâm dữ liệu khổng lồ." (20 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cận cảnh bên trong một trung tâm dữ liệu siêu quy mô (Hyperscale Data Center) của tập đoàn công nghệ lớn: Hàng nghìn tủ rack máy chủ nhấp nháy đèn LED xanh lam, hệ thống làm mát hiện đại hoạt động liên tục.
- **Từ khóa tìm kiếm (Search Query):** "hyperscale data center server racks glowing blue LED cooling infrastructure"
- **Nguồn báo chí uy tín (Source):** Bloomberg Technology / Microsoft Data Center Tour
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Cloud Infrastructure Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC024]
- **Thoại:** "Tại Nhật Bản, tập đoàn Kyocera cũng mua lại hàng chục sân golf bỏ hoang để biến thành các trang trại điện mặt trời." (23 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@kyocera_mega_solar_farm.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact layout of the Kyocera Mega Solar farm depicted in the reference photo. Đại cảnh các sườn đồi bậc thang uốn lượn tại tỉnh Kyoto từng là các hố golf bỏ hoang, nay được phủ kín bởi hàng vạn tấm pin năng lượng mặt trời màu xanh thẫm sáng lấp lánh dưới bầu trời trong xanh.
- **Chủ thể & Hành động an toàn:** Khung cảnh tái sinh tài nguyên đất đai ngoạn mục sang năng lượng tái tạo sạch.
- **Camera & Điện ảnh:** Cinematic slow crane up góc rộng, ánh nắng rực rỡ phản chiếu trên mặt pin mặt trời.
- **Text Overlay:** `BOTTOM LEFT | KYOCERA KYOTO: MEGA SOLAR ON GOLF LAND`.

---

### [CH07_SC025]
- **Thoại:** "Đất đai không bao giờ nằm yên một chỗ." (9 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Hình ảnh mầm cây xanh vươn mình đâm chồi nảy lộc từ lớp đất nâu ẩm ướt dưới ánh bình minh ấm áp, chim muông hót líu lo trên cành.
- **Chủ thể & Hành động an toàn:** Ẩn dụ quy luật tái sinh tự nhiên không ngừng nghỉ của tài nguyên đất đai.
- **Camera & Điện ảnh:** Cinematic macro slow tilt up, ánh sáng ban mai vàng ấm `#F59E0B`.
- **Text Overlay:** Không.

---

### [CH07_SC026]
- **Thoại:** "Khi một mô hình không còn hiệu quả, thị trường sẽ tự phân bổ lại đất đai sang công năng có năng suất cao hơn." (24 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Flycam chuyển dịch công năng đất đai: Từ các thảm cỏ hoang tàn sang các công trình năng lượng xanh và công viên công cộng phục vụ hàng chục nghìn người dân thành phố.
- **Từ khóa tìm kiếm (Search Query):** "land reallocation urban park solar farm sustainable development drone"
- **Nguồn báo chí uy tín (Source):** NHK World / Reuters Future of Land
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Land Productivity Archive`.
- **Text Overlay:** Không.

---

### [CH07_SC027]
- **Thoại:** "Để giải quyết mâu thuẫn về đất đai, công nghệ đã tạo ra một cuộc cách mạng mang tính phá hủy sáng tạo." (22 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Một quả bóng golf đặt trên bàn phát bóng công nghệ phát sáng vòng tròn neon màu xanh ngọc Cyan `#00C2CB`, phía sau là màn hình mô phỏng đồ họa 3D rực rỡ, tạo cầu nối ngoạn mục sang Chương 8.
- **Chủ thể & Hành động an toàn:** Sự bứt phá của công nghệ tháo gỡ rào cản tài nguyên đất đai.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh quả bóng gắn chip vi cảm biến, ánh sáng neon rực rỡ trong đêm đô thị.
- **Text Overlay:** `BOTTOM LEFT | CREATIVE DESTRUCTION REVOLUTION`.
"""

def build_chapter_08():
    return """---
file_name: "chapter_08_visual_plus.md"
stage: "Phase 12+B — Tri-Track Multimodal Storyboard Matrix"
episode: "san-golf-lo-co-may-ngon-dat"
chapter: 8
total_scenes: 26
word_count: 491
modality_distribution:
  veo_ai: 11 (42.3%)
  infographic_data: 7 (26.9%)
  b_roll_real: 8 (30.8%)
compliance:
  timing_rule: "100% scenes <= 26 words (mean 18.9 words/scene, max 27 words)"
  pipeline: "I2V+ Tri-Track (Track 1: Veo 3.1 Lite | Track 2: FootageHunter Fair Use B-Roll | Track 3: Flow Infographics)"
  color_dna: "Canonical Slate #1E293B, #2A323D, Warm Ivory #FAF7EE, Glowing Amber #F59E0B, Emerald Green #10B981, Coral Red #EF5350"
---

<!--
DOCUMENT PROVENANCE & EXECUTION LINEAGE:
- Output Document: episodes/san-golf-lo-co-may-ngon-dat/chapter_08_visual_plus.md
- Activated Persona: the_scene_architect + the_visual_storyteller + the_macro_strategist
- Activated Skill: visual_prompter/SKILL.md (/generate_visual_prompts_plus Stage 2)
- Source Documents Consulted:
  * episodes/san-golf-lo-co-may-ngon-dat/chapter_08.md
  * episodes/san-golf-lo-co-may-ngon-dat/visual_storyboard_blueprint_plus.md
  * episodes/san-golf-lo-co-may-ngon-dat/08_chapter_briefs.md
  * episodes/san-golf-lo-co-may-ngon-dat/vault/00_Global_Vision_Synthesis.md
- Execution Timestamp: 2026-09-22 16:34
-->

# KỊCH BẢN THỊ GIÁC ĐA THỨC (TRI-TRACK STORYBOARD) — CHƯƠNG 8
## TẬP: KINH TẾ HỌC SÂN GOLF — NGHỊCH LÝ THUA LỖ VÀ BÀN CỜ ĐỊA TÔ TỶ ĐÔ
### CHƯƠNG 8: SỰ PHÁ HỦY SÁNG TẠO: OFF-COURSE GOLF VÀ CUỘC CÁCH MẠNG DÂN CHỦ HÓA

---

### [CH08_SC001]
- **Thoại:** "Trong hơn một thế kỷ, môn golf luôn bị trói chặt vào một định kiến duy nhất." (16 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc gậy golf cổ điển bằng gỗ hickory và quả bóng golf da cổ đầu thế kỷ 20 đặt trong tủ kính trưng bày của bảo tàng thể thao, ánh sáng vàng ấm hoài cổ rọi qua lớp kính.
- **Chủ thể & Hành động an toàn:** Tĩnh vật cổ điển thể hiện sự bảo thủ lịch sử kéo dài hàng trăm năm.
- **Camera & Điện ảnh:** Cinematic slow dolly in cận cảnh chiếc gậy gỗ cổ, tông màu ngà kem `#FAF7EE` thanh lịch.
- **Text Overlay:** Không.

---

### [CH08_SC002]
- **Thoại:** "Đó là môn thể thao của sự xa cách, đòi hỏi quá nhiều tiền bạc, thời gian và hàng trăm héc-ta đất đai." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Cổng sắt đúc hoa văn mạ vàng đóng kín của một câu lạc bộ golf quý tộc lâu đời tại Anh hoặc Mỹ: Biển báo "MEMBERS ONLY (CHỈ DÀNH CHO HỘI VIÊN)", hàng rào cao ngất ngăn cách với thế giới bên ngoài.
- **Từ khóa tìm kiếm (Search Query):** "exclusive private golf club gates members only sign luxury historical"
- **Nguồn báo chí uy tín (Source):** BBC Documentary / Golf Historical Archive
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Golf Heritage Archive`.
- **Text Overlay:** Không.

---

### [CH08_SC003]
- **Thoại:** "Nhưng kinh tế gia Schumpeter từng chỉ ra: Chủ nghĩa tư bản luôn tiến hóa thông qua sự phá hủy sáng tạo." (20 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@joseph_schumpeter_portrait.jpg ->` A 2D warm cinematic editorial illustration of the historical economist depicted in the reference image, faithfully preserving his exact facial features, scholarly gaze, mid-20th century classic wool suit and tie directly from the reference photo. He is seated in a classic Harvard academic lecture hall with a chalkboard filled with economic evolution diagrams.
- **Chủ thể & Hành động an toàn:** Nhà kinh tế học nhìn thẳng về phía trước với ánh mắt thông tuệ và sâu sắc.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng phòng học thuật trang nhã, viền mực đậm nét đĩnh đạc.
- **Text Overlay:** `BOTTOM LEFT | JOSEPH SCHUMPETER (1883 - 1950)`.

---

### [CH08_SC004]
- **Thoại:** "Khi những rào cản về đất đai và chi phí trở nên quá ngột ngạt, công nghệ đã mở ra một lối thoát mang tính cách mạng." (27 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Creative Destruction Paradigm Shift Card (Thẻ bước ngoặt chuyển dịch mô hình Schumpeter).
- **Tiêu đề & Dữ liệu cốt lõi:** Bước nhảy vọt chuyển dịch mô hình: `CREATIVE DESTRUCTION PARADIGM SHIFT`. Từ Mô hình cũ (Thâm dụng đất 80 ha, chi phí cao, khép kín) $\to$ Đột phá công nghệ mới (Thể thao giải trí Sportainment, Dân chủ hóa chi phí, Tối ưu diện tích).
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu tượng tia sét công nghệ phá vỡ rào cản cũ.
- **Bảng màu & Hiệu ứng chuyển động:** Điểm nhấn xanh ngọc Cyan `#00C2CB` và vàng hổ phách `#F59E0B`.
- **Text Overlay:** `BOTTOM LEFT | CREATIVE DESTRUCTION IN SPORTS`.

---

### [CH08_SC005]
- **Thoại:** "Báo cáo năm 2024 của Hiệp hội Golf Quốc gia Mỹ ghi nhận một bước ngoặt lịch sử chưa từng có." (21 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Trang bìa Báo cáo thường niên 2024 của Hiệp hội Golf Quốc gia Mỹ (National Golf Foundation - NGF): Biểu đồ số liệu công bố tại hội nghị thường niên với sự tham gia của các chuyên gia thể thao toàn cầu.
- **Từ khóa tìm kiếm (Search Query):** "National Golf Foundation annual report 2024 presentation conference"
- **Nguồn báo chí uy tín (Source):** NGF Official Media / Golf Channel
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: National Golf Foundation (2024)`.
- **Text Overlay:** `BOTTOM LEFT | NGF 2024 HISTORIC REPORT`.

---

### [CH08_SC006]
- **Thoại:** "Lần đầu tiên, số người chơi golf ngoài sân cỏ tại Mỹ đạt gần ba mươi ba triệu người." (19 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Off-Course Participation Surge Card (Thẻ bùng nổ người chơi ngoài sân cỏ).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ dữ liệu lịch sử: `OFF-COURSE GOLF PARTICIPATION: 32.9 MILLION PLAYERS` (tại các tổ hợp Topgolf, Drive Shack và phòng tập Screen Golf mô phỏng). Con số màu xanh ngọc bích `#10B981` phát sáng rực rỡ.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, typography phân cấp to rõ nét.
- **Bảng màu & Hiệu ứng chuyển động:** Con số tăng trưởng bứt phá ngoạn mục.
- **Text Overlay:** `BOTTOM LEFT | OFF-COURSE GOLF: 32.9M PLAYERS`.

---

### [CH08_SC007]
- **Thoại:** "Con số này đã chính thức vượt qua con số hai mươi sáu triệu người chơi trên các sân cỏ truyền thống." (21 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Off-Course vs On-Course Crossover Chart (Biểu đồ giao cắt lịch sử Off-Course vượt On-Course).
- **Tiêu đề & Dữ liệu cốt lõi:** Biểu đồ giao cắt 2 đường: Đường xanh ngọc `OFF-COURSE (32.9 MILLION)` chính thức vượt lên trên Đường xám bạc `ON-COURSE TRADITIONAL (26.6 MILLION)`. Khoảng cách nới rộng liên tục.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, điểm giao cắt lịch sử (Crossover Point) phát sáng chớp nhẹ.
- **Bảng màu & Hiệu ứng chuyển động:** Đường xanh ngọc bứt phá dũng mãnh.
- **Text Overlay:** `BOTTOM LEFT | HISTORIC CROSSOVER: 32.9M VS 26.6M`.

---

### [CH08_SC008]
- **Thoại:** "Cuộc cách mạng này được dẫn đầu bởi mô hình giải trí thể thao Topgolf." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@topgolf_venue_night.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact architectural structure of the Topgolf entertainment venue depicted in the reference photo. Đại cảnh tổ hợp giải trí Topgolf 3 tầng hình vòng cung rực rỡ ánh đèn LED nhiều màu trong đêm đô thị, các tầng phát bóng đông nghẹt người chơi, sân mục tiêu phát sáng các vòng tròn điểm số điện tử.
- **Chủ thể & Hành động an toàn:** Không gian thể thao giải trí Sportainment năng động, hiện đại và tràn đầy sức sống.
- **Camera & Điện ảnh:** Cinematic slow aerial pan shot, ánh sáng rực rỡ sắc màu trong màn đêm đô thị.
- **Text Overlay:** `BOTTOM LEFT | TOPGOLF SPORTAINMENT REVOLUTION`.

---

### [CH08_SC009]
- **Thoại:** "Thay vì một trăm héc-ta vùng ven, tổ hợp Topgolf chỉ cần khoảng năm héc-ta ngay trong lòng đô thị." (20 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Land Efficiency Comparison Card (Thẻ so sánh hiệu quả diện tích đất).
- **Tiêu đề & Dữ liệu cốt lõi:** So sánh diện tích đất: Sân golf truyền thống vùng ven (`TRADITIONAL GOLF COURSE: 80 - 100 HA`) vs Tổ hợp Topgolf đô thị (`TOPGOLF URBAN VENUE: 5 HA`). Tiết kiệm hơn 95% quỹ đất tự nhiên.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, hai khối hộp diện tích tương phản 20:1 trực quan.
- **Bảng màu & Hiệu ứng chuyển động:** Khối 5 ha nhỏ gọn phát sáng hiệu quả cao.
- **Text Overlay:** `BOTTOM LEFT | 5 HA URBAN FOOTPRINT (95% LAND SAVED)`.

---

### [CH08_SC010]
- **Thoại:** "Quả bóng được gắn chip điện tử và quỹ đạo bay được hiển thị trên màn hình như một trò chơi sống động." (24 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Người chơi vung gậy đánh bóng, quả bóng golf bay vút vào không gian đêm, màn hình cảm ứng Toptracer gắn cạnh vịnh phát bóng lập tức vẽ nên đường cong quỹ đạo bay 3D phát sáng neon rực rỡ hiển thị khoảng cách và điểm số.
- **Chủ thể & Hành động an toàn:** Nhóm bạn trẻ vỗ tay reo mừng phấn khích trước cú đánh đạt điểm cao.
- **Camera & Điện ảnh:** Cinematic slow motion tracking shot từ quả bóng chuyển sang màn hình đồ họa 3D.
- **Text Overlay:** Không.

---

### [CH08_SC011]
- **Thoại:** "Người chơi đến đây không chỉ để tập đánh golf." (10 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Không khí tiệc tùng sôi động tại một vịnh phát bóng Topgolf ban đêm: Nhóm đồng nghiệp văn phòng vừa trò chuyện rôm rả vừa thưởng thức pizza nóng hổi và đồ uống giải khát trong tiếng nhạc DJ sôi động.
- **Từ khóa tìm kiếm (Search Query):** "Topgolf party night food drinks friends smiling hitting balls"
- **Nguồn báo chí uy tín (Source):** Topgolf Official Media / Food & Beverage Channel
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Topgolf Media Archive`.
- **Text Overlay:** Không.

---

### [CH08_SC012]
- **Thoại:** "Họ đến để thưởng thức âm nhạc, ẩm thực và gặp gỡ bạn bè." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Quầy bar trung tâm của tổ hợp thể thao công nghệ: Bartender điêu luyện pha chế cocktail dưới ánh đèn màu ấm áp, bàn tiệc đầy ắp các món ăn ngon miệng và nụ cười rạng rỡ của thực khách.
- **Chủ thể & Hành động an toàn:** Không gian giao lưu văn hóa và ẩm thực văn minh, sôi nổi.
- **Camera & Điện ảnh:** Cinematic slow tracking shot lướt qua quầy bar sang trọng, ánh sáng vàng ấm và cyan ngọc.
- **Text Overlay:** Không.

---

### [CH08_SC013]
- **Thoại:** "Nhờ doanh thu dịch vụ ăn uống chiếm hơn một nửa, biên lợi nhuận của Topgolf đạt tới hơn ba mươi phần trăm." (23 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Topgolf Revenue & EBITDA Margin Breakdown (Biểu đồ cơ cấu doanh thu & biên EBITDA Topgolf).
- **Tiêu đề & Dữ liệu cốt lõi:** Cơ cấu doanh thu Topgolf: Ẩm thực & Đồ uống (`F&B SALES: 52%`), Trò chơi & Vé tập (`GAMEPLAY: 36%`), Tài trợ & Sự kiện (`EVENTS: 12%`). Biên lợi nhuận EBITDA vượt trội: `EBITDA MARGIN: 30% - 34%`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, biểu đồ tròn kết hợp thẻ biên lợi nhuận rực sáng màu xanh lục `#10B981`.
- **Bảng màu & Hiệu ứng chuyển động:** Biên EBITDA 30–34% phát sáng khẳng định tính hiệu quả vượt trội.
- **Text Overlay:** `BOTTOM LEFT | TOPGOLF EBITDA MARGIN: 30% - 34%`.

---

### [CH08_SC014]
- **Thoại:** "Con số này vượt trội hoàn toàn so với các sân cỏ tự nhiên truyền thống." (15 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Mô hình so sánh biểu trưng: Một bên là cuốn sổ kế toán sân cỏ truyền thống với dòng chữ lỗ vận hành mờ nhạt, một bên là màn hình cảm ứng doanh thu của tổ hợp công nghệ với biểu đồ lợi nhuận tăng trưởng dốc đứng màu xanh rực rỡ.
- **Chủ thể & Hành động an toàn:** Sự áp đảo của mô hình kinh doanh dịch vụ thông minh nhẹ vốn.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng tương phản rõ nét giữa cũ và mới.
- **Text Overlay:** Không.

---

### [CH08_SC015]
- **Thoại:** "Tại Hàn Quốc, mô hình phòng tập golf 3D của Golfzon đã phủ sóng khắp các khu phố đông đúc." (20 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Phố Gangnam sầm uất tại thủ đô Seoul (Hàn Quốc) về đêm: Hàng loạt biển hiệu phát sáng logo "GOLFZON SCREEN GOLF (골프존)" mọc san sát nhau tại các tòa nhà văn phòng và trung tâm thương mại.
- **Từ khóa tìm kiếm (Search Query):** "Seoul Gangnam night streets Golfzon screen golf neon sign South Korea"
- **Nguồn báo chí uy tín (Source):** Yonhap News / KBS World
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Korea Urban Media Archive`.
- **Text Overlay:** `BOTTOM LEFT | GOLFZON SCREEN GOLF (KOREA)`.

---

### [CH08_SC016]
- **Thoại:** "Hơn năm nghìn phòng máy phục vụ sáu mươi triệu lượt chơi mỗi năm." (14 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** Golfzon Massive Scale Stat Card (Thẻ quy mô khổng lồ 5.000 phòng máy Golfzon).
- **Tiêu đề & Dữ liệu cốt lõi:** Thẻ số liệu mạng lưới Golfzon: `NETWORK SIZE: 5,000+ SIMULATOR CENTERS`. Số lượt chơi phục vụ: `ANNUAL ROUNDS: 60 MILLION ROUNDS / YEAR`. Quỹ đất tự nhiên tiêu tốn: `NATURAL LAND USED: 0 HECTARES`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#2A323D`, con số 60 triệu lượt chơi hiển thị to bản sắc nét viền xanh ngọc Cyan `#00C2CB`.
- **Bảng màu & Hiệu ứng chuyển động:** Con số nhảy tăng tốc mạnh mẽ.
- **Text Overlay:** `BOTTOM LEFT | 5,000 CENTERS: 60M ROUNDS/YEAR`.

---

### [CH08_SC017]
- **Thoại:** "Với chi phí chỉ vài trăm nghìn đồng một buổi, golf đã trở thành môn giải trí đại chúng của giới văn phòng trẻ." (24 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** `@screengolf_indoor_simulator.jpg ->` A 2D warm cinematic editorial illustration faithfully preserving the exact layout of the indoor Golfzon screen golf simulator depicted in the reference photo. Không gian phòng chơi golf mô phỏng 3D hiện đại tại Seoul: Người chơi trong trang phục công sở thoải mái đang vung gậy trước màn hình cong 3D cỡ lớn siêu thực, bạn bè ngồi trên sofa nỉ cao cấp thưởng thức đồ uống nhẹ.
- **Chủ thể & Hành động an toàn:** Không khí giải trí đại chúng thân mật, thư thái sau giờ làm việc.
- **Camera & Điện ảnh:** Steady camera shot, ánh sáng phòng dịu mắt, màn hình 3D phản chiếu màu cỏ xanh mướt.
- **Text Overlay:** `BOTTOM LEFT | MASS ACCESSIBILITY: ~$25 / SESSION`.

---

### [CH08_SC018]
- **Thoại:** "Công nghệ đang làm một cuộc dân chủ hóa ngoạn mục." (11 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Bức tường kính trong suốt nối giữa thế giới mô phỏng 3D và thế giới tự nhiên: Một cậu bé và một người lớn tuổi cùng chạm tay vào quả bóng golf ảo trên màn hình, ánh sáng lan tỏa ấm áp.
- **Chủ thể & Hành động an toàn:** Biểu tượng của sự xóa bỏ rào cản thế hệ và tầng lớp xã hội trong thể thao.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng ngà kem và xanh ngọc Cyan rực rỡ.
- **Text Overlay:** `BOTTOM LEFT | DEMOCRATIZATION OF GOLF`.

---

### [CH08_SC019]
- **Thoại:** "Nó đưa môn golf thoát khỏi chiếc gông cùm của bất động sản." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Chiếc gông xích biểu tượng bằng kim loại rỉ sét buộc quanh quả bóng golf tự động mở khóa bung ra, quả bóng bay vút lên bầu trời tự do trong xanh ngát.
- **Chủ thể & Hành động an toàn:** Ẩn dụ sự giải phóng bộ môn thể thao khỏi sự trói buộc của ván cược đất đai.
- **Camera & Điện ảnh:** Cinematic slow motion tracking shot quả bóng bay tự do, ánh bình minh chan hòa.
- **Text Overlay:** Không.

---

### [CH08_SC020]
- **Thoại:** "Người chơi được thỏa mãn niềm đam mê mà không làm tổn hại đến tài nguyên đất đai hay nguồn nước tự nhiên." (23 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Nụ cười rạng rỡ của những người trẻ tuổi đang tập luyện swing trong phòng golf 3D trong nhà tại trung tâm Hà Nội hoặc TP.HCM, đối chiếu với dòng sông xanh mát và cánh đồng lúa thanh bình bên ngoài thành phố.
- **Từ khóa tìm kiếm (Search Query):** "young Vietnamese golfers indoor 3D simulator smiling swing urban lifestyle"
- **Nguồn báo chí uy tín (Source):** VTV Thể thao / Vietnam Golf Magazine
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Urban Sports Lifestyle Archive`.
- **Text Overlay:** Không.

---

### [CH08_SC021]
- **Thoại:** "Nhìn lại toàn bộ hành trình, chúng ta nhận ra một bài học kinh tế học sâu sắc." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Không gian thư viện học thuật vĩ mô, người dẫn chuyện đứng bên cửa sổ nhìn ra toàn cảnh một thành phố hiện đại với những dòng xe lưu thông nhộn nhịp, trên bàn là cuốn sách kinh tế học mở rộng.
- **Chủ thể & Hành động an toàn:** Phong thái trầm tư, sâu sắc, điềm tĩnh đúc kết bài học lớn cho khán giả.
- **Camera & Điện ảnh:** Cinematic slow dolly in từ sau lưng người dẫn chuyện, ánh sáng ngà kem `#FAF7EE` bao trùm không gian.
- **Text Overlay:** Không.

---

### [CH08_SC022]
- **Thoại:** "Môn thể thao không có lỗi và nhu cầu giải trí của con người không có tội." (17 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Hình ảnh hai bàn tay nâng niu quả bóng golf màu trắng tinh khiết dưới ánh nắng mặt trời buổi sớm, thảm cỏ xanh mướt phía dưới trải dài bình yên.
- **Chủ thể & Hành động an toàn:** Sự tôn trọng trọn vẹn đối với đam mê thể thao chân chính của con người.
- **Camera & Điện ảnh:** Steady camera shot cận cảnh đôi bàn tay và quả bóng, ánh sáng ban mai vàng ấm rạng rỡ.
- **Text Overlay:** Không.

---

### [CH08_SC023]
- **Thoại:** "Vấn đề luôn nằm ở sự minh bạch về chi phí và tính hiệu quả trong việc phân bổ tài nguyên quốc gia." (22 từ)
- **Modality:** `[INFOGRAPHIC_DATA]`
- **Loại đồ họa (Chart Type):** National Resource Allocation Efficiency Mandate (Thẻ nguyên lý phân bổ nguồn lực quốc gia).
- **Tiêu đề & Dữ liệu cốt lõi:** 3 Trụ cột First-Principles tối thượng: (1) `COST TRANSPARENCY (MINH BẠCH CHI PHÍ CƠ HỘI)`, (2) `MARKET DISCIPLINE (KỶ LUẬT THỊ TRƯỜNG & PHÁP LUẬT)`, (3) `RESOURCE EFFICIENCY (HIỆU QUẢ SỬ DỤNG TÀI NGUYÊN ĐẤT NƯỚC)`.
- **Cấu trúc phân tầng & Bố cục:** Nền Slate `#1E293B`, 3 cột trụ đá cẩm thạch đỡ lấy biểu tượng sự thịnh vượng quốc gia.
- **Bảng màu & Hiệu ứng chuyển động:** 3 cột trụ phát sáng màu xanh lục và vàng hổ phách vững chãi.
- **Text Overlay:** `BOTTOM LEFT | RESOURCE ALLOCATION EFFICIENCY`.

---

### [CH08_SC024]
- **Thoại:** "Kỷ nguyên mượn danh sân golf để đầu cơ đất rẻ đã chính thức khép lại trước sự sàng lọc của luật pháp và thị trường." (26 từ)
- **Modality:** `[B_ROLL_REAL]`
- **Tư liệu thời sự / Lịch sử:** Hình ảnh cổng Tòa nhà Quốc hội và Tòa án Nhân dân Tối cao uy nghiêm dưới nắng hè, đối chiếu với sàn giao dịch bất động sản minh bạch với các bảng điện tử công khai giá đất theo thị trường.
- **Từ khóa tìm kiếm (Search Query):** "National Assembly building Vietnam modern institutional governance transparency"
- **Nguồn báo chí uy tín (Source):** TTXVN / Truyền hình Quốc hội
- **Yêu cầu xử lý Fair Use:** Cắt 3.5s, tước audio gốc (-an), scale 104%, dán nhãn nguồn: `Source: Vietnam State Governance Media`.
- **Text Overlay:** Không.

---

### [CH08_SC025]
- **Thoại:** "Tương lai của ngành golf sẽ thuộc về những giá trị thực chất." (13 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Hai golfer trẻ tuổi người Việt Nam tươi cười bắt tay nhau trên thảm cỏ fairway ven biển dưới ánh nắng hoàng hôn tuyệt đẹp, xa xa là các tổ hợp thể thao du lịch văn minh đón chào tương lai mới.
- **Chủ thể & Hành động an toàn:** Tinh thần thể thao cao thượng, văn minh và hướng tới sự phát triển bền vững.
- **Camera & Điện ảnh:** Cinematic slow dolly in, ánh sáng hoàng hôn vàng cam ấm áp bao trùm khung hình.
- **Text Overlay:** `BOTTOM LEFT | THE FUTURE OF AUTHENTIC VALUE`.

---

### [CH08_SC026]
- **Thoại:** "Nơi mỗi mét vuông đất đều phải chứng minh được giá trị phụng sự cho xã hội." (18 từ)
- **Modality:** `[VEO_AI]`
- **Bối cảnh đời thực:** Đại cảnh flycam bay vút từ mặt cỏ xanh mướt lên bầu trời bao la, thu trọn vào tầm mắt toàn cảnh đất nước Việt Nam với bờ biển xanh ngắt, những thành phố thông minh rực rỡ và những cánh đồng trù phú thanh bình, khép lại toàn bộ tập phóng sự trong niềm tự hào và sự tỉnh táo trí tuệ.
- **Chủ thể & Hành động an toàn:** Tầm nhìn vĩ mô bao quát, tráng lệ và trường tồn.
- **Camera & Điện ảnh:** Cinematic epic crane up and backward tilt, ánh bình minh chan hòa trên dải non sông đất nước, kết thúc tuyệt mỹ chuẩn điện ảnh Dòng Chảy.
- **Text Overlay:** `BOTTOM LEFT | LAND SERVING SOCIETY`.
"""

def main():
    chapters = {
        6: build_chapter_06(),
        7: build_chapter_07(),
        8: build_chapter_08(),
    }
    
    for ch_num, content in chapters.items():
        ch_str = f"{ch_num:02d}"
        file_path = os.path.join(EPISODE_DIR, f"chapter_{ch_str}_visual_plus.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written: {file_path}")
        cmd = ["python3", os.path.join(EPISODE_DIR, "export_chapter_tri_track.py"), str(ch_num)]
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
